# ✅ Phase 06 Preflight Checklist

![Gate](https://img.shields.io/badge/Gate%200-PASSED-16a34a)

## 🧾 Account & cost boundary

- [x] AWS account verified: `197821101770`
- [x] Region fixed to `us-east-1`
- [x] Free Plan/credits checked before runtime creation
- [x] No account upgrade performed
- [x] Phase 03 retained artifacts identified before cleanup

## 🔐 Access & safety

- [x] Administrative CLI access validated
- [x] No long-lived AWS keys added to GitHub
- [x] GitHub OIDC chosen for AWS authentication
- [x] Least-privilege deployment permissions scoped to the Phase 06 runtime
- [x] `main` protected by pull request + required CI check

## 🧪 Delivery prerequisites

- [x] Docker build succeeded locally/in CI
- [x] `/api/health` behavior validated
- [x] `/api/ready` failure/success semantics tested
- [x] Gitleaks, `pip-audit`, Trivy and pytest configured as blocking controls

## 🧹 Closeout prerequisites

- [x] Rollback path tested before teardown
- [x] Evidence captured
- [x] Temporary AWS resources removed
- [x] Residual audit completed in `us-east-1`
- [x] Phase 03 AMI, snapshot and S3 recovery assets preserved

> Gate 0 was not just a starting checklist; it also defined the safety constraints used through cleanup.
