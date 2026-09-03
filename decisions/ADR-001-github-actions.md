# 🧠 ADR-001 — GitHub Actions as the Delivery Engine

**Status:** 🟡 Proposed — validate/freeze at Gate 1

## Context

MADAR's source and portfolio evidence already live in GitHub. Phase 06 needs PR-triggered CI and AWS delivery automation with visible execution evidence.

## Proposed decision

Use **GitHub Actions** as the CI/CD orchestration layer.

## Why

- 🔗 close to source/PR lifecycle,
- 👀 workflow history is reviewer-visible,
- 🔐 integrates with GitHub OIDC for AWS,
- 🧩 sufficient for the learning objectives without adding Jenkins infrastructure merely to operate Jenkins.

## Consequence

The project demonstrates GitHub Actions deeply rather than pretending to cover every CI/CD platform. Jenkins/GitLab concepts remain transferable but are not claimed as implemented.