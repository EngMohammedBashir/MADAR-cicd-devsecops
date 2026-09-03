# 🚀 MADAR — CI/CD & DevSecOps

> **Phase 06 of the MADAR Cloud Transformation Journey**  
> 🟡 **Status: DESIGN / PREFLIGHT — implementation not started**

![Phase](https://img.shields.io/badge/MADAR-Phase%2006-7c3aed)
![Focus](https://img.shields.io/badge/Focus-CI%2FCD%20%2B%20DevSecOps-2563eb)
![AWS](https://img.shields.io/badge/AWS-ECR%20%7C%20ECS%20Fargate-ff9900)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088ff)
![Security](https://img.shields.io/badge/Security-Shift--Left-16a34a)
![State](https://img.shields.io/badge/State-Preflight-f59e0b)

## 🎯 Mission

Phase 05 proved that I could recover MADAR's legacy Flask workload, containerize it, run it on ECS/Fargate behind an ALB, connect it to PostgreSQL, validate self-healing and scale-out, inject a database-network failure, observe recovery, and clean the temporary AWS environment.

Phase 06 attacks the next bottleneck: **manual software delivery**.

```text
👨‍💻 Code change
   ↓
🔀 Pull Request
   ↓
🧪 Tests + quality gates
   ↓
🛡️ Security / dependency / secret checks
   ↓
🐳 Docker build
   ↓
🔎 Container image scan
   ↓
🔐 GitHub OIDC → temporary AWS credentials
   ↓
📦 Amazon ECR
   ↓
🚀 Amazon ECS / Fargate deployment
   ↓
🩺 /api/health + /api/ready validation
   ↓
✅ Promote OR ↩️ rollback
```

## 🧠 What I intend to prove

This is not a repository whose only claim is "I made a GitHub Actions YAML file." I want evidence that the delivery system behaves correctly when things go right **and when they fail**.

| Capability | Planned proof |
|---|---|
| 🔀 Pull-request CI | A change cannot bypass required validation |
| 🧪 Automated testing | Broken application behavior fails before deployment |
| 🔐 Keyless AWS auth | GitHub Actions assumes an AWS role using OIDC; no long-lived AWS access keys in GitHub |
| 🐳 Reproducible build | Immutable image built from repository source |
| 🏷️ Traceability | Image/deployment tied to Git commit SHA |
| 🛡️ DevSecOps gates | Secret/dependency/container scanning produces visible evidence |
| 📦 Artifact promotion | Approved image is published to ECR |
| 🚀 Automated deployment | Pipeline updates the ECS workload rather than relying on manual console deployment |
| 🩺 Post-deploy validation | Health/readiness checks verify the deployed revision |
| 💥 Failure test | Intentionally bad release is blocked or detected |
| ↩️ Recovery | Rollback/recovery path is exercised and evidenced |
| 🧹 Cost discipline | Temporary AWS runtime is cleaned up after validation |

## 🔗 Continuity from Phase 05

Phase 06 continues the **same MADAR workload**. It does not invent a disconnected demo application.

```text
Phase 03  → migrated legacy workload
Phase 05  → modernized runtime into containers
Phase 06  → modernizes how that container is tested, secured and delivered
```

The Phase 05 AWS runtime was intentionally destroyed after validation. Phase 06 therefore must first decide what minimum runtime needs to be recreated and how to do so reproducibly.

## 🛡️ Non-negotiable security principles

- 🚫 No AWS access keys committed to Git.
- 🚫 No database passwords, tokens or `.env` secrets committed.
- 🔐 Prefer GitHub Actions → AWS **OIDC** with short-lived credentials.
- 🎯 IAM trust and permissions must be scoped to the repository/workflow need.
- 🏷️ Deploy immutable/traceable image tags; do not rely only on `latest`.
- 🛑 Security checks must be capable of failing the pipeline when the agreed threshold is crossed.
- 📸 Evidence must never expose secret values.

## 💰 Cost rule

Phase 06 starts with design and account/cost preflight. Cost-bearing AWS resources are created only when needed for deployment validation and removed after evidence capture.

> 🧠 **Important:** Phase 05 intentionally cleaned its ECS/ALB/RDS/VPC runtime. We will not pretend those resources still exist.

## 🏭 Lab vs production

The lab will demonstrate the delivery controls with the smallest safe environment our account/budget permits. Production recommendations may be stronger than what we deploy in the short-lived portfolio lab—for example private networking, HTTPS/domain, HA database design, protected environments, richer policy-as-code and multi-environment promotion.

Those differences will be documented explicitly rather than hidden.

## 📂 Repository map

```text
.
├── README.md
├── CURRENT-STATE.md
├── REPOSITORY-SCOPE.md
├── START-HERE.md
├── .gitignore
├── docs/
│   ├── PHASE-06-IMPLEMENTATION-PLAN.md
│   └── PIPELINE-ARCHITECTURE.md
├── decisions/
│   ├── ADR-001-github-actions.md
│   ├── ADR-002-aws-oidc.md
│   └── ADR-003-immutable-image-tags.md
├── checklists/
│   └── 00-preflight.md
├── runbooks/
│   ├── 00-execution-runbook.md
│   ├── 90-rollback-runbook.md
│   └── 99-cleanup-runbook.md
└── evidence/
    └── README.md
```

Workflow/application files will be added only when implementation reaches those gates. Documentation does not claim that a control is deployed before it actually exists.

## 🚦 Tomorrow's first gate

```text
1️⃣ Verify GitHub/AWS/account prerequisites
2️⃣ Confirm Phase 05 source/artifacts needed for continuity
3️⃣ Freeze CI/CD architecture
4️⃣ Freeze authentication model (OIDC preferred)
5️⃣ Define pass/fail security thresholds
6️⃣ Define image tagging + deployment/rollback strategy
7️⃣ Estimate cost and DELETE/RETAIN inventory
8️⃣ Only then begin implementation
```

## 🏁 Definition of Done

Phase 06 closes only when a reviewer can follow a real code change from commit/PR to automated validation, security gates, image publication and ECS deployment—and can see an intentionally tested failure/recovery path, operational runbooks, evidence, cost closeout and cleanup.

---

### 🧭 MADAR engineering philosophy

**Build it → break it safely → observe it → recover it → document the truth → clean it up.**