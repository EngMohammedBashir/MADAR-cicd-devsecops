# 🎯 Repository Scope — MADAR Phase 06

## 🟢 In scope

- 🔀 GitHub pull-request CI and delivery workflow.
- 🧪 automated application/build validation.
- 🛡️ secret, dependency and container-image security checks selected during preflight.
- 🔐 GitHub Actions → AWS authentication with OIDC/short-lived credentials where account capability permits.
- 🐳 reproducible Docker build.
- 🏷️ immutable Git-SHA-based image traceability.
- 📦 Amazon ECR publication.
- 🚀 automated deployment to an ECS/Fargate validation runtime.
- 🩺 post-deployment `/api/health` and `/api/ready` checks.
- 💥 deliberately test a failed/bad delivery path.
- ↩️ prove rollback/recovery.
- 📊 capture pipeline and AWS evidence.
- 💰 cost checkpoint and final cleanup.
- 🧰 leave enough commands/explanation that another engineer can reproduce the work.

## 🔴 Not automatically in scope

- ☸️ EKS/Kubernetes migration.
- 🏢 multi-account landing zone.
- 🧱 enterprise WAF/SOC platform.
- 🌍 full production multi-region deployment.
- 🐘 production Multi-AZ database unless required by a later approved design.
- 🌐 buying a domain solely for this lab.
- 💸 permanent NAT infrastructure solely for screenshots.
- 🧩 microservice rewrite.

## 🟠 Conditional / decide during preflight

- Infrastructure as Code depth for recreating the minimum runtime.
- GitHub Environments/approval features based on repository/account capability.
- exact scanners and severity thresholds.
- deployment strategy: rolling ECS deployment vs another strategy justified by cost/capability.

## 🧠 Scope principle

The project should demonstrate **delivery engineering**, not inflate the architecture with unrelated AWS services. Any constraint or unavailable feature will be recorded honestly with the production-grade alternative.