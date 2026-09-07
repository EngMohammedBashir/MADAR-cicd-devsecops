# ↩️ Phase 06 — Rollback & Recovery Runbook

![Status](https://img.shields.io/badge/Rollback-VALIDATED-16a34a?style=for-the-badge)
![Failure](https://img.shields.io/badge/Controlled%20Failure-HTTP%20503-dc2626?style=for-the-badge)

> Use this runbook when a new ECS revision reaches the service but fails post-deployment validation. The automated controlled test lives in `.github/workflows/controlled-rollback.yml`.

## 🚨 Trigger

Rollback when the candidate release fails `/api/ready`, introduces a dependency/configuration failure, or otherwise fails the release acceptance checks. `/api/health=200` alone is **not** enough to promote a release.

## 🧠 Recovery model

```text
Known-good revision
      ↓ capture ARN
Candidate revision
      ↓ deploy
health + readiness
      ↓ failure
STOP promotion
      ↓
ECS update-service → known-good revision
      ↓
wait services-stable
      ↓
health + readiness again
      ↓
RECOVERED
```

## 1 — Capture the known-good revision

```powershell
$CLUSTER="madar-p06-cluster"; $SERVICE="madar-p06-service"; $REGION="us-east-1"; $GOOD=(aws ecs describe-services --cluster $CLUSTER --services $SERVICE --region $REGION --query 'services[0].taskDefinition' --output text); Write-Host "Known-good: $GOOD"
```

**Why:** never begin a controlled deployment/failure test without a concrete recovery target.

Expected: an ECS task-definition ARN such as the validated `madar-p06-app:3`.

## 2 — Deploy/observe the candidate

For normal releases, `.github/workflows/ci.yml` registers the new revision and updates the service automatically. Wait for ECS stability:

```powershell
aws ecs wait services-stable --cluster $CLUSTER --services $SERVICE --region $REGION
```

## 3 — Validate both signals

```powershell
curl.exe -i http://<ALB-DNS>/api/health
curl.exe -i http://<ALB-DNS>/api/ready
```

Acceptance requires both to return HTTP `200`.

If health succeeds but readiness returns `503`, the process is alive but the workload is not ready to serve because its database dependency is unavailable. Do not promote it.

## 4 — Roll back

```powershell
aws ecs update-service --cluster $CLUSTER --service $SERVICE --task-definition $GOOD --region $REGION --query 'service.{Service:serviceName,TaskDefinition:taskDefinition,Desired:desiredCount}' --output table
aws ecs wait services-stable --cluster $CLUSTER --services $SERVICE --region $REGION
```

**What this does:** it points the ECS service back to the captured known-good task definition, then waits until replacement/recovery activity settles.

## 5 — Prove recovery

```powershell
curl.exe -i http://<ALB-DNS>/api/health
curl.exe -i http://<ALB-DNS>/api/ready
```

Do not call the incident recovered until both are healthy again.

## 🧪 Validated Phase 06 controlled failure

The manual workflow deliberately changed only the database host to:

```text
controlled-failure.invalid
```

Observed sequence:

```text
madar-p06-app:3   KNOWN GOOD
       ↓
madar-p06-app:4   CONTROLLED BAD REVISION
       ↓
/api/health       200 ✅
/api/ready        503 ❌ expected
       ↓
release gate      failure detected ✅
       ↓
rollback          madar-p06-app:3
       ↓
/api/health       200 ✅
/api/ready        200 / database connected ✅
```

This was a controlled configuration failure, not a fabricated production incident.

📸 [`../evidence/phase06-controlled-failure-rollback-success.png`](../evidence/phase06-controlled-failure-rollback-success.png)

## 🧯 If rollback does not recover readiness

Check in this order:

```text
1. ECS service events / running task count
2. target-group health
3. task logs in /ecs/madar-p06
4. MADAR_DB_HOST configuration
5. Secrets Manager reference / execution-role permission
6. ECS SG → RDS SG TCP 5432 path
7. RDS status
```

Do not keep registering random revisions. Establish whether the failure is image/configuration, service/networking, secret access or database availability first.

## 🏁 Exit criteria

```text
✅ service stable
✅ known-good task definition active
✅ /api/health = 200
✅ /api/ready = 200
✅ database connected
✅ failure/recovery evidence recorded
```
