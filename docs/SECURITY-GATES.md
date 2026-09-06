# Phase 06 Security Gates

## Secret scanning

Phase 06 uses Gitleaks in GitHub Actions to detect committed credentials, API keys, tokens, private keys, and similar secret patterns before later build and deployment stages can proceed.

The workflow checks out full Git history (`fetch-depth: 0`) so Gitleaks can inspect repository history rather than only the shallow checkout.

### Failure policy

Secret findings are blocking. The Gitleaks step does not use `continue-on-error`; a finding therefore fails the CI job and prevents subsequent successful completion of the pipeline.

### Controlled negative test

A later dedicated test branch/PR will introduce only a synthetic detector fixture, never a real credential. The expected result is a red Gitleaks gate. The fixture will not be merged to `main` and must not contain a usable AWS, GitHub, database, or other real secret.

### Evidence standard

Record the successful PR workflow run for this change and, separately, the intentionally failed workflow run from the controlled negative test. Do not treat a historical unrelated CI failure as proof that the security gate blocks unsafe changes.
