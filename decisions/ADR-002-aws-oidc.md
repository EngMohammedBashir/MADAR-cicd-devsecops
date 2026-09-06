# ADR-002 — 🔑 AWS authentication through GitHub OIDC

**Status:** ✅ Accepted and validated

## Decision
Use GitHub OIDC + AWS STS instead of storing AWS access keys in repository secrets.

## Why
The workflow needs AWS access only while a deployment is running. Short-lived federation removes the operational burden and exposure of long-lived credentials.

## Validated implementation
The trust policy was restricted to the immutable repository identity and `main` branch subject. The role received only the ECR/ECS/PassRole permissions required by this phase.

## Consequences
- ✅ No long-lived AWS access key in GitHub
- ✅ Short-lived, attributable sessions
- ✅ Smaller credential blast radius
- ⚠️ Trust-policy subject format must match GitHub exactly
