# Secret Scan Check

Expected CI order: checkout full history → Gitleaks → Python tests/dependency audit → Docker build → runtime health. A Gitleaks finding exits non-zero and blocks later successful pipeline completion.
