# 🧹 Phase 06 — Cleanup & Residual Audit Runbook

![Cleanup](https://img.shields.io/badge/Phase%2006-CLEANED-16a34a?style=for-the-badge)
![Rule](https://img.shields.io/badge/Rule-DEPENDENCY%20ORDER-f59e0b?style=for-the-badge)

> Cleanup is part of the engineering exit gate. This runbook records the dependency-safe order used for Phase 06 and the audit required before declaring the temporary runtime removed.

## 🛑 Never delete these

These belong to Phase 03 continuity/recovery or the AWS account default network:

```text
AMI       ami-0cbd2e9ec0d6f9168
Snapshot  snap-0920a020c47fb6447
S3        madar-operational-files-197821101770
VPC       vpc-015017581b8954e61   (default)
Default subnets in us-east-1
```

## 🧠 Why deletion order matters

```text
ECS service
   ↓ releases tasks / ENIs
ALB listener → ALB → target group
   ↓
RDS
   ↓ releases DB dependencies
ECR / task definitions / cluster / logs
   ↓
DB subnet group
   ↓
IAM / OIDC
   ↓
Security Groups LAST
```

Deleting SGs too early can return `DependencyViolation` because ENIs or another SG still references them.

## 1 — Stop and remove ECS service

```powershell
aws ecs update-service --cluster madar-p06-cluster --service madar-p06-service --desired-count 0 --region us-east-1 --query 'service.{Service:serviceName,Desired:desiredCount,Running:runningCount}' --output table
aws ecs delete-service --cluster madar-p06-cluster --service madar-p06-service --force --region us-east-1
```

Expected: desired/running workload goes to zero and the service enters deletion/draining.

## 2 — Delete ALB chain

Delete in this order:

```text
listener → load balancer → target group
```

Use the current ARNs from `aws elbv2 describe-*`; do not reuse a deleted lab ARN when rebuilding. Wait until the ALB disappears before expecting every attached network dependency to release.

## 3 — Delete RDS

For this disposable Phase 06 lab, deletion used **no final snapshot** because the authoritative source dump is retained separately in Phase 03 S3.

```powershell
aws rds delete-db-instance --db-instance-identifier madar-p06-postgres --skip-final-snapshot --delete-automated-backups --region us-east-1
aws rds wait db-instance-deleted --db-instance-identifier madar-p06-postgres --region us-east-1
```

Do not apply this pattern to a production database without an explicit retention/backup decision.

## 4 — Delete ECR and log group

```powershell
aws ecr delete-repository --repository-name madar-phase06 --force --region us-east-1
aws logs delete-log-group --log-group-name /ecs/madar-p06 --region us-east-1
```

`--force` on the ECR repository removes the Phase 06 images inside that disposable repository.

## 5 — Deregister task definitions and delete cluster

List revisions first:

```powershell
aws ecs list-task-definitions --family-prefix madar-p06-app --region us-east-1 --output table
```

Deregister every active Phase 06 revision, then remove the empty cluster:

```powershell
aws ecs delete-cluster --cluster madar-p06-cluster --region us-east-1
```

Validated Phase 06 had revisions `:1` through `:4`, all of which ended `INACTIVE`.

## 6 — Delete DB subnet group

After RDS is fully gone:

```powershell
aws rds delete-db-subnet-group --db-subnet-group-name madar-p06-db-subnets --region us-east-1
```

## 7 — IAM and OIDC cleanup

Remove role inline policies/managed-policy attachments before deleting their roles. Validated temporary identities were:

```text
MADAR-Phase06-GitHubActionsRole
MADAR-Phase06-ECSTaskExecutionRole
MADAR-Phase06-RestoreTaskRole
GitHub OIDC provider: token.actions.githubusercontent.com
```

The restore role was temporary/unused in the final restore path and was removed during closeout.

Also confirm the RDS-managed secret disappeared after database deletion. Do not print secret values during verification.

## 8 — Security Groups LAST

Validated IDs were:

```text
ALB  sg-0f568ca8195cf7208
ECS  sg-0f9a3569ed217bb1b
RDS  sg-0057bae3ba8d11449
```

If deletion reports `DependencyViolation`, do not suppress the error. Check remaining ENIs and SG references, wait for AWS-managed dependencies to release, then retry. In the validated cleanup, the ALB/ECS SGs required waiting for dependencies before final deletion.

## 9 — Regional residual audit

Use this audit after deletion. Empty Phase 06 categories are the desired result:

```powershell
$R="us-east-1"; Write-Host "`n========== PHASE 06 — FINAL CLEANUP ==========" -ForegroundColor Cyan; $checks=@(@("EC2 Instances",{aws ec2 describe-instances --region $R --filters "Name=instance-state-name,Values=pending,running,stopping,stopped" --query 'Reservations[].Instances[].InstanceId' --output text}),@("ECS Clusters",{aws ecs list-clusters --region $R --query 'clusterArns[]' --output text}),@("ECR Repositories",{aws ecr describe-repositories --region $R --query 'repositories[].repositoryName' --output text}),@("RDS Databases",{aws rds describe-db-instances --region $R --query 'DBInstances[].DBInstanceIdentifier' --output text}),@("Load Balancers",{aws elbv2 describe-load-balancers --region $R --query 'LoadBalancers[].LoadBalancerName' --output text}),@("NAT Gateways",{aws ec2 describe-nat-gateways --region $R --filter "Name=state,Values=available,pending" --query 'NatGateways[].NatGatewayId' --output text}),@("Elastic IPs",{aws ec2 describe-addresses --region $R --query 'Addresses[].PublicIp' --output text}),@("Non-Default Security Groups",{aws ec2 describe-security-groups --region $R --query 'SecurityGroups[?GroupName!=`default`].GroupId' --output text})); foreach($c in $checks){$x=(& $c[1] 2>&1 | Out-String).Trim(); if([string]::IsNullOrWhiteSpace($x) -or $x -eq "None"){Write-Host ("[DELETED / CLEAN]  " + $c[0]) -ForegroundColor Green}else{Write-Host ("[FOUND]            " + $c[0] + " -> " + $x) -ForegroundColor Red}}; Write-Host "`n========== CLEANUP AUDIT COMPLETE ==========" -ForegroundColor Cyan
```

This is an **audit**, not a deletion script. `[FOUND]` means inspect the resource before taking any action; never delete an unrelated resource merely to make the dashboard green.

## ✅ Validated final residual state

No Phase 06 EC2 instances, ECS clusters/services, ECR repositories, RDS instances, ALBs, target groups, NAT Gateways, Elastic IPs, Lambda functions, Secrets Manager secrets, CloudWatch log groups, ENIs or non-default security groups remained in the audited `us-east-1` scope.

The retained Phase 03 AMI, EBS snapshot and S3 bucket remained intentionally preserved. Snapshot/S3 storage may still have storage cost; Cost Explorer can lag, so a clean resource audit is not the same as claiming an absolute real-time `$0` bill.

📸 [`../evidence/phase06-final-cleanup-verification.png`](../evidence/phase06-final-cleanup-verification.png)

## 🏁 Exit criteria

```text
✅ temporary runtime gone
✅ IAM/OIDC delivery identities removed
✅ Phase 06 SGs gone
✅ default VPC/subnets preserved
✅ Phase 03 AMI/snapshot/S3 preserved
✅ residual audit recorded
✅ billing checked separately with awareness of reporting lag
```
