# Secret Scanning Implementation

Phase 06 uses the official Gitleaks GitHub Action as a blocking CI security gate.

## Design

- Action: `gitleaks/gitleaks-action@v3`
- Checkout: full Git history (`fetch-depth: 0`)
- GitHub token: workflow-provided token only; no stored long-lived credential is introduced
- Failure behavior: blocking; no `continue-on-error`
- Repository type: personal-account repository, so the action does not require an organization Gitleaks license

The workflow also moves `actions/checkout` to the Node 24 generation (`@v6`) while adding this gate.

## Why this matters

Dependency scanning answers whether third-party packages have known vulnerabilities. Secret scanning answers a different question: whether credentials, tokens, private keys, or similar sensitive values were accidentally committed. Both gates are required before automated cloud delivery is trusted.

## Negative test safety

The negative test must use a synthetic detector fixture only. Never commit a real AWS key, GitHub token, database password, private key, or other usable credential merely to prove the scanner works.
