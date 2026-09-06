# 🛡️ Branch Protection

![Status](https://img.shields.io/badge/main-PROTECTED-16a34a)

`main` is protected through a GitHub ruleset requiring the pull-request path and the real Phase 06 CI status check. Force pushes and branch deletion are blocked.

## ✅ Validated controls

| Control | State |
|---|---:|
| Pull request required | ✅ |
| Required CI status check | ✅ |
| Force pushes blocked | ✅ |
| Branch deletion restricted | ✅ |
| Required approvals | `0` for this solo portfolio repo |

The goal is simple: **code cannot quietly bypass the delivery controls just because the repository has one contributor.**

📸 Evidence: [`../evidence/phase06-branch-protection.png`](../evidence/phase06-branch-protection.png)
