# 🚀 MADAR — CI/CD & DevSecOps

> **Phase 06 · Secure software delivery for the MADAR containerized workload**  
> ✅ **Status: COMPLETED & VALIDATED** · 🔐 **OIDC** · 🛡️ **DevSecOps gates** · 🐳 **ECR** · ⚙️ **ECS/Fargate** · ↩️ **Rollback tested** · 🧹 **AWS runtime cleaned**

![Phase](https://img.shields.io/badge/MADAR-Phase%2006-7c3aed?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-COMPLETED-16a34a?style=for-the-badge)
![CI](https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-OIDC%20%2B%20ECS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Security](https://img.shields.io/badge/Security-Gitleaks%20%7C%20pip--audit%20%7C%20Trivy-0f766e?style=for-the-badge)

## 🧭 Start here

| I want to... | Go to |
|---|---|
| 👀 Understand the project in 5 minutes | **This README** |
| 🛠️ Rebuild Phase 06 from the engineering record | [`runbooks/00-execution-runbook.md`](runbooks/00-execution-runbook.md) |
| ↩️ Recover a failed ECS release | [`runbooks/90-rollback-runbook.md`](runbooks/90-rollback-runbook.md) |
| 🧹 Tear down the temporary AWS runtime safely | [`runbooks/99-cleanup-runbook.md`](runbooks/99-cleanup-runbook.md) |
| 🧠 Understand architecture/security decisions | [`decisions/`](decisions/) + [`docs/`](docs/) |
| 📸 Inspect proof instead of trusting claims | [`evidence/README.md`](evidence/README.md) |

> The README is intentionally the **portfolio landing page**. The runbooks carry the reproducible operator detail, commands, expected results, troubleshooting and cleanup order.

## 🎯 What I built

Phase 05 proved the MADAR application could run as a container. Phase 06 turned that workload into a **controlled software-delivery system**: every change is tested, scanned, built, traceable to a Git commit, deployed with short-lived AWS credentials, validated after release, and recoverable through rollback.

```mermaid
flowchart LR
    A[👨‍💻 Code] --> B[🔀 Pull Request]
    B --> C[🔐 Gitleaks]
    C --> D[🧪 pytest]
    D --> E[🛡️ pip-audit]
    E --> F[🐳 Docker Build]
    F --> G[🔎 Trivy]
    G --> H[🔑 GitHub OIDC]
    H --> I[📦 ECR · Git SHA]
    I --> J[⚙️ ECS/Fargate]
    J --> K{🚦 health + ready}
    K -->|Pass| L[✅ Release]
    K -->|Fail| M[↩️ Rollback]
```

## 🧰 Technology stack

`GitHub Actions` · `GitHub OIDC` · `AWS IAM/STS` · `Docker` · `Amazon ECR` · `Amazon ECS/Fargate` · `ALB` · `Amazon RDS PostgreSQL` · `Secrets Manager` · `CloudWatch Logs` · `pytest` · `Gitleaks` · `pip-audit` · `Trivy`

## 🏆 Final result

| Capability | Result | Proof |
|---|---:|---|
| Pull-request CI | ✅ VALIDATED | Required checks on protected `main` |
| Unit + readiness tests | ✅ VALIDATED | `/api/health` and `/api/ready` tested independently |
| Secret scanning | ✅ VALIDATED | Gitleaks blocked a synthetic secret in an unmerged PR |
| Dependency scanning | ✅ VALIDATED | `pip-audit` blocking gate |
| Container scanning | ✅ VALIDATED | Trivy HIGH/CRITICAL policy |
| GitHub → AWS authentication | ✅ VALIDATED | OIDC + short-lived credentials, no long-lived AWS keys |
| Image traceability | ✅ VALIDATED | Immutable ECR image tags based on Git SHA |
| Automated ECS deployment | ✅ VALIDATED | Successful GitHub Actions deployment |
| Post-deploy validation | ✅ VALIDATED | Liveness + database readiness checks |
| Controlled failed release | ✅ VALIDATED | Bad DB host produced expected readiness failure |
| Rollback & recovery | ✅ VALIDATED | ECS returned from task definition `:4` to known-good `:3` |
| Cleanup | ✅ VALIDATED | Temporary Phase 06 AWS runtime removed |

## ❤️ Liveness vs readiness

The dashboard and release checks intentionally use two different signals:

- **`/api/health`** → the Flask process is alive and responding.
- **`/api/ready`** → the application can actually reach PostgreSQL and is ready for real traffic.

That separation matters during real incidents: an application can be alive while its database dependency is unavailable.

## 🔐 Security model

```text
No stored AWS access keys
        ↓
GitHub OIDC federation
        ↓
Short-lived STS credentials
        ↓
Least-privilege GitHub Actions role
        ↓
ECR publish + ECS deployment only
```

The pipeline uses four independent blocking controls because each answers a different question: **Gitleaks** protects secrets, **pytest** protects application behavior, **pip-audit** protects Python dependencies, and **Trivy** protects the built container image.

## 🧯 Failure story that matters

The strongest release proof was intentionally negative. I deployed a controlled task-definition revision with an invalid database host. The Flask process stayed alive, so `/api/health` remained healthy, while `/api/ready` correctly failed with HTTP `503`. The gate treated the release as bad, the workflow returned ECS to the known-good revision, and readiness recovered.

That test proved three things at once: **liveness is not readiness**, a green process is not automatically a safe release, and rollback was an exercised recovery path rather than a diagram-only claim.

## 📸 Evidence gallery

### 🔑 OIDC → ECR publication
![OIDC ECR publish](evidence/phase06-oidc-ecr-publish-success.png)

### 📦 Immutable Git-SHA image traceability
![ECR SHA traceability](evidence/phase06-ecr-sha-traceability.png)

### ⚙️ Automated ECS deployment
![Automated ECS deployment](evidence/phase06-automated-ecs-deployment-success.png)

### 🚚 Live workload with restored operational data
![Live dashboard](evidence/phase06-live-dashboard-restored-data.png)

### ↩️ Controlled failure and rollback recovery
![Controlled rollback](evidence/phase06-controlled-failure-rollback-success.png)

### 🧹 Final cleanup verification
![Final cleanup](evidence/phase06-final-cleanup-verification.png)

<details>
<summary><strong>🖼️ View the rest of the Phase 06 evidence</strong></summary>

#### 🛡️ Branch protection
![Branch protection](evidence/phase06-branch-protection.png)

#### 🔎 Container scan
![Container scan](evidence/phase06-container-scan-success.png)

#### 🗄️ Database restore and relock
![Database restore](evidence/phase06-database-restore-and-relock.png)

#### ✅ Pre-AWS CI closeout
![Pre AWS CI](evidence/phase06-pre-aws-closeout-ci-success.png)

#### 🚦 Readiness CI
![Readiness CI](evidence/phase06-readiness-ci-success.png)

#### ✅ Required PR check
![Required PR check](evidence/phase06-required-check-pr9-success.png)

#### 📊 Runtime validation summary
![Runtime validation](evidence/phase06-runtime-validation-summary.png)

#### 🚨 Negative secret-gate test
![Secret gate negative test](evidence/phase06-secret-gate-negative-test.png)

</details>

## 🧩 AWS runtime used for validation

The temporary validation environment used the default VPC in `us-east-1`, an internet-facing HTTP ALB, ECS/Fargate, ECR, a single-AZ PostgreSQL RDS instance, CloudWatch Logs, scoped security groups, and IAM/OIDC roles. The environment was intentionally short-lived and removed after validation.

The retained Phase 03 recovery baseline remains separate from this phase: the migration AMI, its EBS snapshot, and the operational S3 bucket are preserved for later portfolio work.

## ⚖️ Lab choices vs production direction

| Phase 06 validation lab | Production direction |
|---|---|
| HTTP ALB | HTTPS with ACM + DNS |
| Single-AZ RDS | HA/Multi-AZ according to business RTO/RPO |
| short-lived default-VPC runtime | dedicated network/environment boundaries |
| master DB credential for lab continuity | least-privilege application DB principal |
| one-task validation service | capacity/HA sized to workload requirements |

These are deliberate lab trade-offs, not claims that the temporary topology is the production target.

## 🧹 Cleanup outcome

After validation I removed the temporary Phase 06 ECS service and cluster, ECR repository, ALB/listener/target group, RDS instance and managed secret, CloudWatch log group, task definitions, IAM roles/policies, OIDC provider, DB subnet group, and Phase 06 security groups. The default VPC/subnets were intentionally preserved because they are account defaults and do not incur charges simply by existing.

## 🗺️ Repository map

| Path | Purpose |
|---|---|
| `.github/workflows/` | Production CI/CD and controlled rollback workflows |
| `app/` | Flask workload, Docker build and automated tests |
| `docs/` | Architecture, security controls and implementation record |
| `decisions/` | Architecture Decision Records |
| `runbooks/` | **Rebuild, rollback and cleanup operator procedures** |
| `checklists/` | Preflight and execution guardrails |
| `evidence/` | Screenshots and evidence index |
| `CURRENT-STATE.md` | Final authoritative status |

## 🧠 Evidence standard

> **PLANNED** = design only · **IMPLEMENTED** = code/configuration exists · **VALIDATED** = observed execution proves the behavior.

Phase 06 is closed only because the delivery path, security gates, failure behavior, recovery path, and cleanup were all observed and documented.
