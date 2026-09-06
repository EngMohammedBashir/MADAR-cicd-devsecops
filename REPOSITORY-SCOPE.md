# 🎯 Repository Scope

> **MADAR Phase 06 — CI/CD & DevSecOps**

## ✅ In scope

This repository owns the software-delivery layer for the MADAR containerized workload:

- GitHub pull-request workflow and required checks
- application/unit/readiness validation
- secret, dependency and container vulnerability scanning
- Docker image build
- GitHub OIDC federation to AWS
- immutable Git-SHA image publication to ECR
- automated ECS/Fargate deployment
- post-deploy health/readiness checks
- controlled failed-release validation
- rollback and recovery
- evidence collection and temporary AWS runtime cleanup

## 🚫 Intentionally out of scope

- Kubernetes / EKS
- Terraform-based platform provisioning
- WAF, custom domain and ACM/TLS
- long-lived production infrastructure
- permanent NAT Gateway
- multi-region disaster recovery
- organization-wide governance

Those belong to later MADAR phases rather than being hidden inside Phase 06.

## 🔗 Continuity

```text
Phase 03  🏗️ Migration baseline + retained recovery assets
    ↓
Phase 05  🐳 Containerized application on ECS/Fargate
    ↓
Phase 06  🚀 Secure CI/CD + automated deployment + rollback
```

## 🧹 Lifecycle rule

The AWS environment created for validation was temporary by design. After the release and rollback tests were proven, the Phase 06 runtime was removed while the Phase 03 recovery baseline remained intact.
