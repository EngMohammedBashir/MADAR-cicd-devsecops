# ✅ Gate 0 — Phase 06 Preflight

> Do this **before** cost-bearing deployment resources.

## ☁️ AWS / Cost

- [ ] Confirm AWS account/plan still usable without upgrade.
- [ ] Check remaining promotional credits/time.
- [ ] Check current month cost baseline.
- [ ] Confirm region.
- [ ] Confirm no unintended Phase 05 runtime survived cleanup.
- [ ] Re-verify intentionally retained AMI/snapshot/S3 before touching them.

## 🔗 Source continuity

- [ ] Identify exact Phase 05 application source to continue.
- [ ] Confirm Dockerfile/dependencies/build locally.
- [ ] Confirm `/api/health` behavior.
- [ ] Confirm `/api/ready` dependency semantics.
- [ ] Do not import secrets or machine-specific artifacts.

## 🐙 GitHub

- [ ] Repository visibility/settings verified.
- [ ] GitHub Actions available.
- [ ] Decide branch/PR strategy.
- [ ] Check whether desired environment approval/protection features are available.
- [ ] Decide required checks before merge/deploy.

## 🔐 Authentication / IAM

- [ ] Check whether AWS IAM OIDC provider for GitHub already exists before creating another.
- [ ] Define exact repository/ref/environment trust boundary.
- [ ] Design least-privilege deployment role.
- [ ] No long-lived AWS access keys in GitHub.

## 🛡️ DevSecOps gates

- [ ] Select secret scanning method.
- [ ] Select dependency scan method.
- [ ] Select container image scan method.
- [ ] Freeze severity threshold that blocks delivery.
- [ ] Plan one safe intentional negative test.

## 🚀 Deployment / rollback

- [ ] Decide minimum ECS/Fargate runtime needed.
- [ ] Decide image tag strategy (`git SHA` baseline).
- [ ] Decide deployment trigger.
- [ ] Decide health/readiness post-deploy verification.
- [ ] Decide rollback/recovery mechanism.
- [ ] Define proof that rollback actually succeeded.

## 💰 DELETE / RETAIN

- [ ] Build resource inventory before creation.
- [ ] Mark every resource `DELETE` or `RETAIN`.
- [ ] Estimate cost drivers.
- [ ] Define residual audit.

## 🟢 Gate result

Do not mark **GO** until the above decisions are based on live account/repository facts.