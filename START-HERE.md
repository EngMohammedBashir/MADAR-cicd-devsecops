# 🧭 START HERE

![Phase](https://img.shields.io/badge/MADAR-Phase%2006-7c3aed)
![Status](https://img.shields.io/badge/Status-COMPLETED-16a34a)

This repository documents how I moved MADAR from a containerized application to a **secured, automated and recoverable delivery pipeline**.

## ⚡ Fast tour

1. **[`README.md`](README.md)** — portfolio overview, architecture and screenshots.
2. **[`CURRENT-STATE.md`](CURRENT-STATE.md)** — authoritative final status.
3. **[`docs/PIPELINE-ARCHITECTURE.md`](docs/PIPELINE-ARCHITECTURE.md)** — delivery architecture and trust boundaries.
4. **[`docs/SECURITY-GATES.md`](docs/SECURITY-GATES.md)** — blocking security controls.
5. **[`decisions/`](decisions/)** — why GitHub Actions, OIDC and immutable tags were chosen.
6. **[`runbooks/`](runbooks/)** — execution, rollback and cleanup operations.
7. **[`evidence/README.md`](evidence/README.md)** — indexed proof from the actual implementation.

## 🧠 Mental model

```text
Code → PR → Test/Scan → Build → OIDC → ECR → ECS → Validate → Release / Rollback → Cleanup
```

The project is intentionally evidence-driven: design alone is not marked as validated. The repository records what was actually executed and observed.
