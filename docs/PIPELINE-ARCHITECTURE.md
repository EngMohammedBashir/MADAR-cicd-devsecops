# 🏗️ Phase 06 — Pipeline Architecture

> 🟡 **Proposed baseline — freeze after preflight.**

## 🌈 Delivery path

```text
🌿 Feature branch
      ↓
🔀 Pull Request
      ↓
┌──────────────────────── CI ────────────────────────┐
│ 🧪 tests / syntax / quality                       │
│ 🔐 secret scanning                                │
│ 🧩 dependency security                            │
│ 🐳 Docker build                                   │
│ 🔎 container scan                                 │
└────────────────────────────────────────────────────┘
      ↓ PASS
🟢 Merge / approved deployment trigger
      ↓
🔐 GitHub OIDC
      ↓ STS temporary credentials
☁️ AWS deployment role
      ↓
📦 ECR image: <git-sha>
      ↓
🚀 ECS service revision
      ↓
🩺 ALB /api/health + /api/ready
      ↓
   ┌───────────────┐
   │ healthy?      │
   └──────┬────────┘
      YES │ NO
          │  └──→ 💥 deployment failure → ↩️ rollback/recovery
          ↓
      ✅ release evidence
```

## 🔐 Trust boundary

GitHub must not receive a permanent AWS access key just to deploy. Preferred design:

```text
GitHub Actions OIDC token
        ↓
AWS IAM OIDC provider
        ↓ trust conditions
Deployment role
        ↓ least privilege
ECR / ECS operations actually required
```

The exact trust condition and IAM permissions are frozen only after the repository/account facts are verified.

## 🏷️ Artifact identity

Primary deployable tag should be tied to the Git commit SHA. Human-friendly aliases may exist, but the evidence must let a reviewer answer:

> Which source commit produced the image that was deployed?

## 💥 Required negative tests

At least one CI/security failure and one deployment/release failure path should be exercised intentionally and safely. The exact test will be selected before execution so we do not damage unrelated resources.

## ↩️ Recovery principle

Rollback is not considered proven because a button or command exists. Phase 06 must execute the selected recovery path and capture the result.