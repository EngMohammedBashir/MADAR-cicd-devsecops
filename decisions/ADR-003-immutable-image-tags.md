# ADR-003 — 📦 Immutable Git-SHA image tags

**Status:** ✅ Accepted and validated

## Decision
Publish container images to ECR using the source Git commit SHA and enable immutable tags.

## Why
A deployment should answer one question immediately: **which exact source revision produced this running image?** Mutable labels such as `latest` cannot provide that guarantee.

## Consequences
- ✅ Source → image → task-definition traceability
- ✅ Rollback targets are deterministic
- ✅ Accidental tag replacement is blocked
- ⚠️ Image lifecycle/cleanup must be handled deliberately

📸 Evidence: [`../evidence/phase06-ecr-sha-traceability.png`](../evidence/phase06-ecr-sha-traceability.png)
