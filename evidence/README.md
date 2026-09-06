# 📸 Phase 06 Evidence Index

> Evidence is tied to observed behavior, not planned architecture.

| Evidence | What it proves |
|---|---|
| [`phase06-pre-aws-closeout-ci-success.png`](phase06-pre-aws-closeout-ci-success.png) | Pre-AWS CI baseline green |
| [`phase06-branch-protection.png`](phase06-branch-protection.png) | Protected `main` / required workflow path |
| [`phase06-container-scan-success.png`](phase06-container-scan-success.png) | Trivy blocking image scan passed |
| [`phase06-readiness-ci-success.png`](phase06-readiness-ci-success.png) | Readiness behavior covered in CI |
| [`phase06-secret-gate-negative-test.png`](phase06-secret-gate-negative-test.png) | Synthetic secret was blocked |
| [`phase06-oidc-ecr-publish-success.png`](phase06-oidc-ecr-publish-success.png) | GitHub OIDC authenticated and published to ECR |
| [`phase06-ecr-sha-traceability.png`](phase06-ecr-sha-traceability.png) | Immutable Git-SHA traceability |
| [`phase06-required-check-pr9-success.png`](phase06-required-check-pr9-success.png) | Real required check passed on PR |
| [`phase06-database-restore-and-relock.png`](phase06-database-restore-and-relock.png) | Operational DB restored and returned private |
| [`phase06-live-dashboard-restored-data.png`](phase06-live-dashboard-restored-data.png) | Live workload served restored Phase 03 data |
| [`phase06-runtime-validation-summary.png`](phase06-runtime-validation-summary.png) | Runtime validation milestone |
| [`phase06-automated-ecs-deployment-success.png`](phase06-automated-ecs-deployment-success.png) | Automated ECS deployment succeeded |
| [`phase06-controlled-failure-rollback-success.png`](phase06-controlled-failure-rollback-success.png) | Failed release detected and rollback recovered |
| [`phase06-final-cleanup-verification.png`](phase06-final-cleanup-verification.png) | Temporary Phase 06 runtime cleaned |

## 🧠 Evidence rule

`PLANNED` → idea/design  
`IMPLEMENTED` → code/config exists  
`VALIDATED` → observed execution proves it

Only the last category is treated as portfolio proof.
