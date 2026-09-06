# 📋 Phase 06 — Implementation Plan

## 🎯 Objective

Turn the manually delivered Phase 05 container into a traceable, security-gated, automated delivery path and prove both successful delivery and controlled failure/recovery.

## 🚦 Gates

| Gate | Outcome | State |
|---|---|---|
| 0️⃣ | Account/GitHub/AWS/cost/source preflight | ✅ VALIDATED |
| 1️⃣ | Pipeline architecture + ADRs frozen | ✅ COMPLETE |
| 2️⃣ | Application source/build baseline restored | ✅ VALIDATED |
| 3️⃣ | PR CI tests operational | ✅ VALIDATED |
| 4️⃣ | Security gates operational — Gitleaks, pip-audit, Trivy | ✅ VALIDATED |
| 5️⃣ | AWS OIDC trust + least-privilege role validated | ⏳ PENDING AWS |
| 6️⃣ | SHA-tagged image automatically published to ECR | ⏳ PENDING AWS |
| 7️⃣ | Minimum ECS validation runtime available | ⏳ PENDING AWS |
| 8️⃣ | Automated deployment succeeds | ⏳ PENDING AWS |
| 9️⃣ | Post-deploy health/readiness succeeds | ⏳ PENDING AWS |
| 🔟 | CI/security negative test proven | ✅ VALIDATED — PR #5 synthetic Gitleaks fixture blocked |
| 1️⃣1️⃣ | Bad deployment/release failure observed | ⏳ PENDING AWS |
| 1️⃣2️⃣ | Rollback/recovery proven | ⏳ PENDING AWS |
| 1️⃣3️⃣ | Evidence + cost closeout | ⏳ AFTER AWS VALIDATION |
| 1️⃣4️⃣ | Temporary resources cleaned + residual audit | ⏳ AFTER AWS VALIDATION |
| 1️⃣5️⃣ | Repository/master closeout | ⏳ FINAL |

## ✅ GitHub-side baseline now proven

The repository has a working pull-request CI path, full MADAR application source, automated pytest coverage, Gitleaks secret scanning, `pip-audit` dependency scanning, Docker build/runtime validation and Trivy container scanning. PR #5 intentionally demonstrated that the secret gate blocks a synthetic unsafe change and was closed without merge.

Health and readiness are treated as separate operational signals: `/api/health` validates application liveness while `/api/ready` validates PostgreSQL-backed readiness.

## 🧠 Learning requirement

Each implementation section must preserve the commands/configuration needed to reproduce it, plus a short explanation of what each critical command does, why it is required, expected output and troubleshooting clues.

## 🛑 Next boundary

Gate 5 is the first AWS delivery gate. It starts with GitHub OIDC/IAM and then the minimum temporary ECR/ECS validation runtime. No Gate 5+ claim becomes VALIDATED until the AWS work is executed and evidenced.