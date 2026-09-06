# 🛡️ Security Gates

| Gate | Protects against | Policy | Result |
|---|---|---|---:|
| 🔐 Gitleaks | committed secrets/tokens | blocking | ✅ VALIDATED |
| 🧪 pytest | application/regression defects | blocking | ✅ VALIDATED |
| 🛡️ pip-audit | vulnerable Python packages | blocking | ✅ VALIDATED |
| 🔎 Trivy | HIGH/CRITICAL fixed image vulnerabilities | blocking | ✅ VALIDATED |
| 🔑 OIDC | long-lived cloud credentials | short-lived STS only | ✅ VALIDATED |
| 🧱 Branch protection | bypassing CI on `main` | PR + required check | ✅ VALIDATED |
| 🚦 Readiness | broken dependency after deployment | release validation | ✅ VALIDATED |
| ↩️ Rollback | failed release recovery | known-good task definition | ✅ VALIDATED |

## 🎯 Why multiple gates?

These controls are intentionally independent. A clean dependency audit does not prove there is no secret in the repository; a clean container scan does not prove the application is ready; a successful build does not prove the release can reach its database.

The pipeline treats security and operability as release conditions, not optional reports.
