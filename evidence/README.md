# 📸 Phase 06 — Evidence Index

Evidence records engineering claims; planned work is never presented as validated.

## ✅ Validated milestones

| Milestone | Status | Evidence |
|---|---|---|
| PR CI flow | VALIDATED | PR #1 merged after successful CI |
| Full MADAR application restoration | VALIDATED | PR #2 and successful post-merge CI |
| Python dependency vulnerability scan | VALIDATED | PR #3; `pip-audit` reported no known vulnerabilities; successful post-merge main run #11 |
| Secret scanning with Gitleaks | VALIDATED | PR #4 merged after successful CI |
| Controlled secret-gate negative test | VALIDATED | PR #5 / Actions run #14 intentionally failed on a synthetic fixture; PR closed without merge |
| Container image vulnerability scan | VALIDATED | PR #6; Trivy HIGH/CRITICAL blocking scan; successful post-merge main run |
| Health/readiness semantics | VALIDATED | PR #7; tests prove `/api/health` liveness is independent from DB-backed `/api/ready`; successful post-merge main run #22 |
| Docker build + runtime health baseline | VALIDATED | GitHub Actions main runs build the image, start the container and verify `/api/health` |

## 📷 Screenshot set

| Filename | What it proves |
|---|---|
| `01-phase06-pr-ci-success.png` | Pull-request CI succeeds before merge |
| `02-phase06-full-app-restored-ci-success.png` | Full MADAR application restored and CI-validated |
| `03-phase06-dependency-scan-success.png` | `pip-audit` dependency gate succeeds |
| `04-phase06-secret-scan-success.png` | Clean-repository Gitleaks gate succeeds |
| `05-phase06-secret-gate-negative-test.png` | Synthetic secret-like fixture is blocked by Gitleaks |
| `06-phase06-container-scan-success.png` | Trivy container scan passes on the approved image |
| `07-phase06-readiness-ci-success.png` | Health/readiness tests pass on official `main` |
| `08-phase06-branch-protection.png` | `main` protection/ruleset requires PR + CI checks |

## 🌈 Future AWS evidence

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