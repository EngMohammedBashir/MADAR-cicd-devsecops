# ADR-001 — ⚙️ GitHub Actions for CI/CD

**Status:** ✅ Accepted and validated

## Decision
Use GitHub Actions as the Phase 06 delivery engine.

## Why
The source already lives in GitHub, so Actions keeps pull requests, required checks, security gates, OIDC identity and deployment history in one auditable workflow. It also provides enough control for a portfolio-scale ECS delivery pipeline without adding another CI platform.

## Consequences
- ✅ Native PR/status-check integration
- ✅ Direct GitHub OIDC federation to AWS
- ✅ Reproducible workflow-as-code
- ⚠️ Workflow permissions and action versions must be reviewed like application code
