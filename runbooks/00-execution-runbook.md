# ▶️ Phase 06 — Reproducible Execution Runbook

![Runbook](https://img.shields.io/badge/Runbook-REBUILD%20FROM%20ZERO-7c3aed?style=for-the-badge)
![Validated](https://img.shields.io/badge/Phase%2006-VALIDATED-16a34a?style=for-the-badge)

> **Purpose:** this is the operator/rebuild guide for Phase 06. The README tells the portfolio story; this file records how I can reproduce the delivery system without relying on chat history.

## 🧭 Mental model

```text
Source change
  ↓
Pull Request
  ↓
Gitleaks → pytest → pip-audit → Docker → Trivy
  ↓
Merge to protected main
  ↓
GitHub OIDC → temporary AWS credentials
  ↓
ECR image tagged with Git SHA
  ↓
new ECS task-definition revision
  ↓
ECS service deployment
  ↓
/api/health + /api/ready
  ↓
release accepted OR rollback
```

## ⚠️ Safety / cost boundary

The AWS runtime in this phase is intentionally temporary. Before rebuilding it, confirm the account/region, current billing/credits and the cleanup plan. Never paste AWS passwords, database passwords, access keys or tokens into this repository. The workflow authenticates to AWS through OIDC; no long-lived AWS access keys are required.

The values below document the **validated Phase 06 lab**. Deleted resources must be recreated and their new IDs/DNS names substituted where appropriate.

## 0 — Prerequisites

**Goal:** prove the workstation and account context before changing anything.

```powershell
aws sts get-caller-identity
aws configure get region
git --version
docker --version
```

Expected account for the validated lab was `197821101770`, region `us-east-1`. `aws sts get-caller-identity` proves which AWS identity is active; the remaining commands prove Git/Docker are available.

Repository:

```powershell
git clone https://github.com/EngMohammedBashir/MADAR-cicd-devsecops.git
cd MADAR-cicd-devsecops
git checkout -b feature/<short-purpose>
```

**Why a feature branch?** `main` is protected. Changes should reach it through a PR and required CI rather than direct pushes.

---

## 1 — Application baseline and local container proof

The workload lives in `app/`. Its two operational signals intentionally mean different things:

- `/api/health` = Flask process is alive.
- `/api/ready` = Flask can reach PostgreSQL.

Run tests:

```powershell
cd app
python -m pip install -r requirements-dev.txt
$env:MADAR_DB_PASSWORD="dummy-test-only"
$env:PYTHONPATH="."
python -m pytest -q
cd ..
```

Build and start the image:

```powershell
docker build -t madar-phase06-local ./app
docker run -d --name madar-p06-local -p 8080:8080 -e MADAR_DB_PASSWORD=dummy-local-only madar-phase06-local
curl.exe http://localhost:8080/api/health
curl.exe -i http://localhost:8080/api/ready
docker rm -f madar-p06-local
```

Expected without a real database: health is `200`; readiness is `503`. That is a **correct** result, not a failure of the health model.

---

## 2 — CI / DevSecOps gates

The authoritative implementation is `.github/workflows/ci.yml`. On PRs it performs:

```text
checkout full history
→ Gitleaks
→ Python 3.12
→ pytest
→ pip-audit
→ Docker build
→ Trivy HIGH/CRITICAL scan
→ temporary container
→ /api/health
```

Useful local equivalents:

```powershell
cd app
python -m pytest -q
python -m pip_audit -r requirements.txt
cd ..
docker build -t madar-phase06-ci:local ./app
```

Gitleaks and Trivy are enforced authoritatively by GitHub Actions. The controlled Gitleaks negative test used a **synthetic** secret in an unmerged PR and proved the gate fails unsafe changes; never use a real credential as a test fixture.

### Branch protection exit condition

Before merging, the PR must show the required CI job green. The validated `main` ruleset required a PR, blocked force pushes/deletion and required the actual CI status check.

---

## 3 — GitHub OIDC → AWS

**Goal:** let GitHub Actions obtain short-lived AWS credentials without repository access keys.

Validated provider:

```text
Provider URL: https://token.actions.githubusercontent.com
Audience:     sts.amazonaws.com
```

Validated role:

```text
MADAR-Phase06-GitHubActionsRole
```

The current GitHub immutable subject used by the validated trust relationship was:

```text
repo:EngMohammedBashir@210871383/MADAR-cicd-devsecops@1356428590:ref:refs/heads/main
```

**Important lesson:** the initial generic subject assumption did not match the subject GitHub emitted for this repository. The trust policy was corrected to the observed immutable owner/repository-ID form above.

The role needs only the delivery permissions required by the pipeline:

```text
ECR authorization token
ECR layer/image push actions → madar-phase06 only
ECS Register/DescribeTaskDefinition
ECS Update/DescribeService → madar-p06-service only
iam:PassRole → MADAR-Phase06-ECSTaskExecutionRole only
```

The workflow then uses:

```yaml
permissions:
  contents: read
  id-token: write
```

and `aws-actions/configure-aws-credentials` with the GitHub Actions role in `us-east-1`.

---

## 4 — ECR immutable image registry

**Goal:** every deployed image must map back to one Git commit.

```powershell
aws ecr create-repository --repository-name madar-phase06 --image-tag-mutability IMMUTABLE --image-scanning-configuration scanOnPush=true --encryption-configuration encryptionType=AES256 --region us-east-1
```

Why: `IMMUTABLE` prevents silently replacing an existing SHA tag; scan-on-push adds registry-side scanning; the CI workflow also runs Trivy before publication.

The workflow uses `${{ github.sha }}` as the image tag, so the traceability chain is:

```text
Git commit SHA ↔ ECR tag ↔ ECS task-definition revision
```

---

## 5 — Minimum validation network

The validated lab reused the **default VPC** to avoid creating unnecessary network infrastructure.

Validated subnets:

```text
us-east-1a  subnet-04e63af31360b080a
us-east-1b  subnet-0d70c1cf55218c14f
```

Create three security boundaries, not one shared SG:

```text
Internet :80 → ALB SG
ALB SG :8080 → ECS SG
ECS SG :5432 → RDS SG
```

Validated names:

```text
madar-p06-alb-sg
madar-p06-ecs-sg
madar-p06-rds-sg
```

**Why:** each hop expresses exactly who may initiate traffic to the next layer. Do not open ECS `8080` or PostgreSQL `5432` directly to the internet.

---

## 6 — PostgreSQL restore and relock

Validated database design:

```text
Identifier       madar-p06-postgres
Engine           PostgreSQL
Class            db.t4g.micro
Storage          20 GiB gp3
Database         madar_legacy
Username         postgres
Topology         Single-AZ lab
Backups          0-day retention for short-lived lab
Deletion protect disabled
```

The authoritative retained dump is:

```text
s3://madar-operational-files-197821101770/database-backups/madar_legacy_final.dump
```

Expected restored business counts:

```text
customers          10
shipments          50
shipment_events   150
```

For the validated restore, RDS was made public **temporarily**, PostgreSQL `5432` was restricted to the operator's single public `/32`, the dump was restored with a PostgreSQL 18 client, counts were reconciled, then the temporary ingress was revoked and `PubliclyAccessible` returned to `False`.

Never commit the RDS-managed master password. Retrieve it at execution time from the RDS-managed Secrets Manager secret and keep it out of shell history/screenshots.

Exit condition:

```text
RDS available
PubliclyAccessible = False
5432 source = ECS SG only
10 / 50 / 150 rows reconciled
```

📸 Evidence: [`../evidence/phase06-database-restore-and-relock.png`](../evidence/phase06-database-restore-and-relock.png)

---

## 7 — ECS/Fargate runtime

Create the cluster and short-retention log group:

```powershell
aws ecs create-cluster --cluster-name madar-p06-cluster --region us-east-1
aws logs create-log-group --log-group-name /ecs/madar-p06 --region us-east-1
aws logs put-retention-policy --log-group-name /ecs/madar-p06 --retention-in-days 1 --region us-east-1
```

Validated task-definition contract:

```text
family              madar-p06-app
launch type          FARGATE
network mode         awsvpc
cpu / memory         256 / 512
container            madar-app
container port       8080
logs                 /ecs/madar-p06
DB password          Secrets Manager reference
execution role       MADAR-Phase06-ECSTaskExecutionRole
```

The execution role uses `AmazonECSTaskExecutionRolePolicy` plus `secretsmanager:GetSecretValue` scoped to the RDS-managed secret. There was no general application Task Role in the validated Phase 06 runtime.

---

## 8 — ALB + target group + ECS service

Validated load-balancing contract:

```text
ALB             madar-p06-alb
Listener        HTTP :80
Target group    madar-p06-tg
Target type     ip
Target port     8080
Health path     /api/health
Service         madar-p06-service
Desired count   1
Launch type     FARGATE
```

This was a short-lived HTTP lab. HTTPS/ACM was not claimed.

After creating the service, wait for stability:

```powershell
aws ecs wait services-stable --cluster madar-p06-cluster --services madar-p06-service --region us-east-1
```

Then validate independently:

```powershell
curl.exe http://<NEW-ALB-DNS>/api/health
curl.exe http://<NEW-ALB-DNS>/api/ready
```

Expected healthy runtime:

```text
/api/health  → HTTP 200
/api/ready   → HTTP 200 + database connected
```

---

## 9 — Automated deployment from `main`

The source of truth is `.github/workflows/ci.yml`. On a successful **push to main**, the workflow continues after CI:

```text
OIDC credentials
→ ECR login
→ tag/push image with github.sha
→ describe current task definition
→ replace only container image
→ register new task revision
→ update ECS service
→ wait stable
→ health check
→ readiness check
```

The workflow intentionally copies the existing task definition and removes AWS read-only fields with `jq` before registering the next revision. This keeps runtime configuration stable while changing the immutable image identity.

A successful deployment is accepted only after both endpoints pass.

📸 Evidence: [`../evidence/phase06-automated-ecs-deployment-success.png`](../evidence/phase06-automated-ecs-deployment-success.png)

---

## 10 — Controlled failed release and rollback

Do not invent a production outage. Use the repository's manual workflow `.github/workflows/controlled-rollback.yml`.

The validated test:

```text
known-good task definition :3
        ↓
register controlled bad revision :4
MADAR_DB_HOST = controlled-failure.invalid
        ↓
health = PASS
readiness = HTTP 503 (EXPECTED)
        ↓
release gate detects failure
        ↓
service rolled back to :3
        ↓
health = PASS
readiness = PASS / database connected
```

This proves why liveness alone is not a safe deployment gate.

Full recovery procedure: [`90-rollback-runbook.md`](90-rollback-runbook.md).

---

## 11 — Evidence and closeout

Capture evidence only at meaningful gates: required CI/security gate, OIDC/ECR traceability, automated deployment, restored live data, controlled failure/rollback and final cleanup. The evidence index is `../evidence/README.md`.

---

## 12 — Cleanup

Cleanup is part of Definition of Done, not an optional afterthought. Follow [`99-cleanup-runbook.md`](99-cleanup-runbook.md) in dependency-safe order and finish with a residual audit.

Do **not** delete these Phase 03 continuity assets:

```text
AMI       ami-0cbd2e9ec0d6f9168
Snapshot  snap-0920a020c47fb6447
S3        madar-operational-files-197821101770
Default VPC and default subnets
```

---

## 🧯 Troubleshooting notes from the real build

| Symptom | What it meant | Resolution |
|---|---|---|
| GitHub OIDC could not assume role | Trust `sub` did not match GitHub's actual immutable subject | Trust exact repository/owner ID subject used by the run |
| Health works but readiness fails | App process is alive but PostgreSQL dependency is unavailable | Treat readiness as release failure; inspect DB/network/secret |
| RDS restore needs temporary reachability | Local restore client cannot reach private-only RDS | Temporary `/32` ingress/public accessibility, restore, then immediately revoke/relock |
| SG deletion returns dependency violation | AWS-managed ENI/reference has not been released yet | Verify ENIs/SG references, wait for dependency release, retry; never force-delete unrelated networking |
| GitHub Actions Node runtime warning | Action targets older Node runtime while GitHub migrates runner runtime | Warning only when job remains successful; update pinned action versions when appropriate |

## 🏁 Definition of Done

Phase 06 is reproducible/closed when all of these are true:

```text
✅ PR security/quality gates pass
✅ synthetic secret negative test is blocked
✅ GitHub uses OIDC, not stored AWS keys
✅ ECR image is immutable and Git-SHA traceable
✅ ECS deploy is automated from main
✅ /api/health and /api/ready pass after deployment
✅ controlled bad release is rejected
✅ rollback restores readiness
✅ temporary AWS runtime is deleted
✅ residual audit is clean
✅ retained Phase 03 assets remain intact
```
