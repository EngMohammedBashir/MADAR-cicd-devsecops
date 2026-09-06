# ↩️ Rollback Runbook

![Status](https://img.shields.io/badge/Rollback-VALIDATED-16a34a)

## Trigger
Rollback when the new ECS revision fails post-deploy validation or a release introduces a dependency failure.

## Validated procedure

1. Capture the currently known-good task definition.
2. Register/deploy the candidate revision.
3. Wait for ECS stability.
4. Test liveness and readiness.
5. On failure, update the service back to the captured known-good revision.
6. Wait for stability again.
7. Re-run both endpoint checks.

## Phase 06 proof

The controlled test deployed `madar-p06-app:4` with an invalid DB host. Health stayed up, readiness failed as expected, then the service returned to `madar-p06-app:3` and database readiness recovered.

📸 [`../evidence/phase06-controlled-failure-rollback-success.png`](../evidence/phase06-controlled-failure-rollback-success.png)
