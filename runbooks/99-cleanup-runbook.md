# 🧹 Phase 06 — Cleanup Runbook

> 🟡 Resource IDs do not exist yet. Populate the inventory as resources are created.

## 🛑 Before deleting anything

Maintain an explicit table:

| Resource | ID/Name | Purpose | DELETE / RETAIN | Why |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## 🎯 Cleanup objective

Delete short-lived cost-bearing Phase 06 runtime resources after all required evidence is captured while preserving only intentionally selected portfolio/continuity artifacts.

## 🔍 Residual audit must cover

- ECS services/tasks/clusters created by Phase 06,
- ECR repositories/images according to retention decision,
- ALB/TG/listeners,
- RDS if recreated,
- VPC/subnets/routes/IGW/NAT/endpoints if created,
- public IPv4/ENIs,
- CloudWatch log groups created for the lab,
- Phase 06 IAM deployment roles/policies/OIDC resources according to explicit retention decision,
- Secrets Manager resources if created,
- Application Auto Scaling resources if created.

## 💰 Final closeout

Capture a Cost Explorer checkpoint after cleanup and state clearly that billing data may lag. Do not claim real-time exact zero merely because the current display rounds to `$0.00`.