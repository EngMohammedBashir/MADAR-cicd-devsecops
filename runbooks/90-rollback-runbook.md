# ↩️ Phase 06 — Rollback / Recovery Runbook

> 🟡 Design skeleton. Exact commands are frozen only after the deployment strategy exists.

## 🎯 Goal

Recover from a deliberately bad release using a known-good immutable artifact/revision and prove service health afterward.

## Required evidence chain

```text
Known-good release        ✅ identified
Bad release               💥 observed safely
Failure signal            🔎 captured
Rollback action           ↩️ executed
Known-good revision       🚀 restored
/api/health               🩺 healthy
/api/ready                🩺 healthy
Deployment stable         ✅ verified
```

## 🛡️ Rule

Do not call rollback "tested" merely because ECS supports rollback or because a command is documented. We must execute the selected path and capture the actual result.