# 📸 Phase 06 — Evidence Index

> 🟡 No implementation screenshots are claimed yet.

## 🌈 Evidence categories

| Category | What will deserve evidence |
|---|---|
| 🔀 PR / CI | required validation actually runs |
| 🧪 Tests | passing baseline + intentional failing test |
| 🛡️ Security | a meaningful security gate blocks the agreed negative case |
| 🔐 OIDC | GitHub successfully assumes the intended AWS role without stored long-lived AWS keys |
| 🐳 Build | reproducible image build |
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

A screenshot is not decoration. It must prove a specific engineering claim. Prefer a small set of strong evidence over dozens of repetitive console images.