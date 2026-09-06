# Security Gate Validation Note

Phase 06 currently uses three independent blocking security controls before any AWS delivery stage:

- **Gitleaks** scans repository content/history for committed secrets.
- **pip-audit** checks Python dependencies for known vulnerabilities.
- **Trivy** scans the built container image for HIGH/CRITICAL OS and library vulnerabilities under the current policy.

## Controlled negative proof

PR #5 intentionally introduced only a synthetic detector fixture on a disposable test branch. Gitleaks detected it and failed Actions run #14 as expected. The PR was closed without merge, so the unsafe fixture never entered `main`.

This is the validated blocking proof for the secret-scanning gate; unrelated historical CI failures are not used as security evidence.

## Current pipeline order

Checkout full history → Gitleaks → pytest → pip-audit → Docker build → Trivy → container runtime `/api/health` validation.

No AWS credential or long-lived AWS access key is introduced by these GitHub-side gates.