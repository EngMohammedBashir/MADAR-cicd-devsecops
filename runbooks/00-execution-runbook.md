# ▶️ Phase 06 Execution Runbook

## Delivery sequence

```text
PR → required CI/security checks → merge → OIDC → ECR SHA image → ECS task revision → service stability → health → readiness
```

## Operator checks

1. Confirm the PR required check is green before merge.
2. Confirm GitHub OIDC receives temporary AWS credentials.
3. Confirm the ECR tag equals the Git commit SHA.
4. Wait for ECS service stability.
5. Validate `/api/health` and `/api/ready` independently.
6. If readiness fails, do not promote the release; follow the rollback runbook.

## Safety rule

Never add static AWS credentials to the repository or workflow. Temporary runtime resources are evidence infrastructure, not permanent production assets.
