# Gate 4 — Secret Scanning Evidence

Status: IMPLEMENTED, pending CI validation on the feature pull request.

## Change

- Added Gitleaks as a blocking GitHub Actions step.
- Updated checkout to full history for repository-history scanning.
- Kept the job at least privilege with `contents: read`.
- Improved failure log handling so CI does not emit a misleading Docker `No such container` message when failure occurs before container creation.

## Validation required

1. Feature PR executes the CI workflow.
2. Gitleaks step succeeds on the legitimate repository state.
3. Existing pytest, dependency audit, Docker build, container startup, and `/api/health` checks continue to pass.
4. A separate controlled negative test later proves a synthetic secret fixture causes the gate to fail.

Do not mark the negative-test requirement VALIDATED until that dedicated failing run exists.
