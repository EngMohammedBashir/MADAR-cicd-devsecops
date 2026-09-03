# 🏷️ ADR-003 — Git SHA as the Deployable Image Identity

**Status:** 🟡 Proposed

## Problem

A mutable tag such as `latest` alone makes it difficult to prove exactly which source revision produced a running container.

## Proposed decision

Tag the deployable ECR image with the Git commit SHA and carry that identity into deployment evidence.

```text
commit abc123...
      ↓
image :abc123...
      ↓
ECS task revision
      ↓
release evidence
```

A friendly alias may be added if useful, but it must not replace the immutable traceability tag.

## Why it matters

- 🔎 auditability,
- ↩️ deterministic rollback target,
- 🐛 easier incident correlation,
- 🧠 clear connection between source, artifact and deployment.