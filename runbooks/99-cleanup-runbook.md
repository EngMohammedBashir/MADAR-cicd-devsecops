# 🧹 Cleanup Runbook

![Cleanup](https://img.shields.io/badge/Phase%2006-CLEANED-16a34a)

## Cleanup order used

1. Scale ECS service to `0` and remove the service.
2. Delete ALB listener, ALB and target group.
3. Delete RDS without a final Phase 06 snapshot.
4. Delete ECR repository and Phase 06 log group.
5. Deregister task definitions.
6. Remove ECS cluster.
7. Remove DB subnet group after RDS disappears.
8. Remove Phase 06 IAM inline policies/roles and GitHub OIDC provider.
9. Confirm the RDS-managed secret no longer exists.
10. Remove Phase 06 security groups after AWS-managed dependencies/ENIs are released.
11. Run a residual audit in `us-east-1`.

## ✅ Final residual state

No Phase 06 EC2, ECS, ECR, RDS, ALB, target groups, NAT Gateways, Elastic IPs, Lambda functions, Secrets Manager secrets, CloudWatch log groups, ENIs or non-default security groups remained.

### 🟢 Intentionally retained
- Phase 03 AMI `ami-0cbd2e9ec0d6f9168`
- Phase 03 snapshot `snap-0920a020c47fb6447`
- S3 `madar-operational-files-197821101770`
- Default VPC/subnets

📸 [`../evidence/phase06-final-cleanup-verification.png`](../evidence/phase06-final-cleanup-verification.png)
