# 🔐 ADR-002 — GitHub OIDC Instead of Long-Lived AWS Keys

**Status:** 🟡 Proposed — validate against live account at Gate 1

## Context

A deployment workflow needs AWS authorization. Storing a permanent IAM access key in GitHub would create unnecessary long-lived credential risk.

## Proposed decision

Use GitHub's OIDC identity to request **short-lived AWS STS credentials** by assuming a narrowly scoped IAM role.

```text
GitHub workflow
   ↓ OIDC token
AWS IAM trust policy
   ↓ AssumeRole
Temporary STS credentials
   ↓
Required deployment APIs only
```

## Guardrails

- restrict trust to the intended repository and execution context,
- grant only required AWS permissions,
- never print credentials,
- never commit access keys,
- validate the trust path with evidence before calling it complete.

## Production lesson

Credential lifetime and trust conditions are part of CI/CD architecture, not an afterthought.