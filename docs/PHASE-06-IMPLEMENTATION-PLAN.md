# 📋 Phase 06 — Implementation Plan

## 🎯 Objective

Turn the manually delivered Phase 05 container into a traceable, security-gated, automated delivery path and prove both successful delivery and controlled failure/recovery.

## 🚦 Gates

| Gate | Outcome | State |
|---|---|---|
| 0️⃣ | Account/GitHub/AWS/cost/source preflight | ⏳ |
| 1️⃣ | Pipeline architecture + ADRs frozen | ⏳ |
| 2️⃣ | Application source/build baseline restored | ⏳ |
| 3️⃣ | PR CI tests operational | ⏳ |
| 4️⃣ | Security gates operational | ⏳ |
| 5️⃣ | AWS OIDC trust + least-privilege role validated | ⏳ |
| 6️⃣ | SHA-tagged image automatically published to ECR | ⏳ |
| 7️⃣ | Minimum ECS validation runtime available | ⏳ |
| 8️⃣ | Automated deployment succeeds | ⏳ |
| 9️⃣ | Post-deploy health/readiness succeeds | ⏳ |
| 🔟 | CI/security negative test proven | ⏳ |
| 1️⃣1️⃣ | Bad deployment/release failure observed | ⏳ |
| 1️⃣2️⃣ | Rollback/recovery proven | ⏳ |
| 1️⃣3️⃣ | Evidence + cost closeout | ⏳ |
| 1️⃣4️⃣ | Temporary resources cleaned + residual audit | ⏳ |
| 1️⃣5️⃣ | Repository/master closeout | ⏳ |

## 🧠 Learning requirement

Each implementation section must preserve the commands/configuration needed to reproduce it, plus a short explanation of what each critical command does, why it is required, expected output and troubleshooting clues.

## ⚠️ Known design questions for Gate 0/1

- Which exact Phase 05 source files are copied/continued here?
- What minimum AWS runtime should be recreated?
- Do account/repository features support the desired approval model?
- Which scanners give useful signal without turning the project into scanner collection?
- What severity blocks a build?
- How will rollback be implemented and proven?
- Which resources are DELETE vs RETAIN after Phase 06?

No answer is invented before we inspect the live constraints.