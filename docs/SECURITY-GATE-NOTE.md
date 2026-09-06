# Security Gate Implementation Note

The current Phase 06 CI adds secret scanning before Python dependency installation, tests, Docker build, and runtime health validation. A detected secret therefore stops the job before build/deployment-oriented work can proceed.

The dedicated controlled negative test remains intentionally separate so a synthetic detector fixture is never merged to `main`.
