# Secret Scanning Portfolio Rationale

Secret scanning is intentionally independent from dependency scanning: pip-audit evaluates known vulnerabilities in Python packages, while Gitleaks evaluates repository content/history for accidentally committed secret material. Keeping both as blocking CI checks demonstrates defense in depth before AWS delivery is enabled.
