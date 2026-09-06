# 🚀 MADAR — CI/CD & DevSecOps

> **Phase 06 of the MADAR Cloud Transformation Journey**  
> 🟢 **Status: GitHub-side CI/DevSecOps baseline validated; AWS delivery stage not started**

![Phase](https://img.shields.io/badge/MADAR-Phase%2006-7c3aed)
![Focus](https://img.shields.io/badge/Focus-CI%2FCD%20%2B%20DevSecOps-2563eb)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088ff)
![Security](https://img.shields.io/badge/Security-Shift--Left-16a34a)
![AWS](https://img.shields.io/badge/AWS-Delivery%20Pending-f59e0b)

## 🎯 Mission

Phase 05 proved the MADAR Flask workload could be containerized and operated on ECS/Fargate. Phase 06 modernizes **how that same application is tested, secured, built and delivered**.

```text
👨‍💻 Code change
   ↓
🔀 Pull Request
   ↓
🔐 Gitleaks secret scan
   ↓
🧪 pytest application tests
   ↓
🛡️ pip-audit dependency scan
   ↓
🐳 Docker build
   ↓
🔎 Trivy image scan
   ↓
❤️ local runtime /api/health check
   ↓
[ next stage ] GitHub OIDC → ECR → ECS/Fargate
   ↓
🚦 post-deploy /api/health + /api/ready
   ↓
✅ Promote OR ↩️ rollback
```

## ✅ What is already proven

| Capability | Status | Evidence |
|---|---|---|
| Pull-request CI | ✅ VALIDATED | PR #1 |
| Full Phase 05 application restored | ✅ VALIDATED | PR #2 |
| Python dependency vulnerability scanning | ✅ VALIDATED | PR #3 / `pip-audit` |
| Secret scanning | ✅ VALIDATED | PR #4 / Gitleaks |
| Controlled negative security test | ✅ VALIDATED | PR #5 intentionally failed and was closed without merge |
| Container image vulnerability scanning | ✅ VALIDATED | PR #6 / Trivy HIGH + CRITICAL blocking policy |
| Liveness semantics | ✅ VALIDATED | `/api/health` tests |
| Database readiness semantics | ✅ VALIDATED | `/api/ready` success + failure tests in PR #7 |
| Post-merge readiness CI | ✅ VALIDATED | main Actions run #22 |
| GitHub → AWS OIDC | ⏳ NOT CREATED | AWS stage pending |
| ECR publication | ⏳ NOT IMPLEMENTED | AWS stage pending |
| ECS deployment | ⏳ NOT IMPLEMENTED | AWS stage pending |
| Release failure / rollback | ⏳ NOT TESTED | AWS stage pending |

## 🛡️ Security gates

The current CI uses independent blocking controls because they answer different questions:

- **Gitleaks** — detects committed credentials, tokens and secret-like material.
- **pip-audit** — checks Python dependencies against known vulnerabilities.
- **Trivy** — scans the built container image for HIGH/CRITICAL OS and library vulnerabilities; unfixed findings are ignored by current policy.
- **pytest** — validates application behavior, including separation of liveness and database readiness.

A controlled negative test on PR #5 used a synthetic fixture only. Gitleaks failed the run as designed, and the PR was never merged.

## ❤️ Health vs 🚦 readiness

- `/api/health` answers: **is the application process responding?**
- `/api/ready` answers: **is the application ready for real traffic with PostgreSQL available?**

The two signals are intentionally independent. An application process may be alive while its database dependency is unavailable.

## 🔗 Continuity from earlier phases

```text
Phase 03 → migrated the legacy workload and retained recovery artifacts
Phase 05 → containerized the workload and validated ECS/Fargate behavior
Phase 06 → secures and automates software delivery for the same workload
```

The temporary Phase 05 AWS runtime was cleaned up after validation. Phase 06 therefore does **not** currently claim a running ECR/ECS/ALB/RDS environment.

## 🔐 AWS delivery design

The next stage will use GitHub Actions with AWS OIDC and short-lived credentials. Long-lived AWS access keys must not be stored in GitHub or committed to the repository. Images will use immutable Git-SHA traceability before deployment to the minimum temporary ECS/Fargate runtime.

## 📚 Repository map

- `.github/workflows/` — CI and security gates
- `app/` — MADAR Flask application, Dockerfile and tests
- `docs/` — architecture, implementation notes, ADRs and runbooks
- `checklists/` — execution gates
- `evidence/` — evidence index and portfolio screenshots
- `CURRENT-STATE.md` — authoritative implementation status

## 🧠 Evidence standard

Claims follow a strict rule:

`PLANNED` → design only  
`IMPLEMENTED` → code/config exists  
`VALIDATED` → observed execution proves the behavior

No AWS deployment, rollback, resilience or cost claim is marked validated until the corresponding AWS work is actually executed and evidenced.