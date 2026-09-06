# 📸 Phase 06 — Evidence Index

Evidence records engineering claims; planned work is never presented as validated.

## ✅ Validated milestones

| Milestone | Status | Evidence |
|---|---|---|
| PR CI flow | VALIDATED | PR #1 merged after successful CI |
| Full MADAR application restoration | VALIDATED | PR #2 and successful post-merge CI |
| Python dependency vulnerability scan | VALIDATED | PR #3; `pip-audit` reported no known vulnerabilities; successful post-merge main run #11 |
| Docker build + process health baseline | VALIDATED | GitHub Actions main runs; `/api/health` returns application status |

## 🛡️ Gate 4 in progress

| Milestone | Status | Evidence |
|---|---|---|
| Secret scanning with Gitleaks | IMPLEMENTED / PENDING VALIDATION | `phase06-gate4-secret-scanning.md`; feature PR CI required |
| Controlled secret-scan negative test | PLANNED | Synthetic non-credential fixture on a non-main test branch/PR |
| Container image vulnerability scan | PLANNED | Not yet implemented |

## 🌈 Future evidence categories

| Category | What will deserve evidence |
|---|---|
| 🔐 OIDC | GitHub assumes the intended AWS role without stored long-lived AWS keys |
| 🏷️ Traceability | Git SHA ↔ ECR image ↔ deployed revision |
| 🚀 Deploy | automated ECS deployment succeeds |
| 🩺 Validation | health/readiness after deployment |
| 💥 Failure | intentionally bad release is detected |
| ↩️ Recovery | known-good revision restored |
| 💰 Cost | cost checkpoint/closeout |
| 🧹 Cleanup | residual-resource audit |

## 🛡️ Screenshot hygiene

Never capture passwords, secret values, AWS credentials, tokens, private keys or sensitive environment values.

## 🧠 Evidence rule

`IMPLEMENTED` means the change exists in code/configuration. `VALIDATED` requires an observed test or workflow result. A screenshot is not decoration: prefer a small set of strong evidence over dozens of repetitive console images.
