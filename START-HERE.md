# 🧭 START HERE — Phase 06

> If I reopen this project tomorrow—or another engineer opens it months later—start here.

## 📍 Where we are

Phase 05 is closed. Phase 06 repository documentation is initialized, but **no CI/CD or AWS deployment implementation is claimed yet**.

## ▶️ First session

1. Read `CURRENT-STATE.md`.
2. Read `REPOSITORY-SCOPE.md`.
3. Execute `checklists/00-preflight.md`.
4. Review `docs/PIPELINE-ARCHITECTURE.md`.
5. Review ADRs before creating IAM/OIDC resources.
6. Freeze DELETE vs RETAIN inventory and expected cost.
7. Update `CURRENT-STATE.md` after every meaningful gate.

## 🧠 How to work

For every important command, record:

```text
Command → what it does → why we need it → expected result → what failure means
```

For every major discovery:

```text
Where did I learn it? → what does it mean? → why does it matter?
```

Do not paste secrets into terminals/screenshots/docs. Do not use long-lived AWS access keys in GitHub when OIDC can satisfy the requirement.

## 📸 Evidence rule

Capture evidence only when it proves a reviewer-relevant claim: CI gate, security block, OIDC assumption, ECR artifact traceability, deployment, health, failed release, rollback/recovery, observability, cost or cleanup.