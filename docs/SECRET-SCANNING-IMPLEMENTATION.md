# 🔐 Secret Scanning Implementation

![Gitleaks](https://img.shields.io/badge/Gitleaks-BLOCKING-16a34a)

Gitleaks runs as a blocking CI gate with full repository history available to the scanner. A finding fails the workflow before image publication or deployment.

## 🧪 Negative test

A synthetic, non-production secret fixture was introduced only on PR #5. The run failed exactly as intended and the PR was closed without merge. This proved the gate blocks unsafe changes instead of merely producing advisory output.

📸 Evidence: [`../evidence/phase06-secret-gate-negative-test.png`](../evidence/phase06-secret-gate-negative-test.png)

> No real credential was committed for this validation.
