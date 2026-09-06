# Branch Protection / Ruleset

Desired protection for `main`:
- require a pull request before merge,
- require the Phase 06 CI status check,
- block force pushes,
- block branch deletion,
- do not require an external reviewer for this solo portfolio repository.

Connector limitation observed on 2026-09-06: the connected GitHub integration can read repository rulesets but does not expose administration write access for branch protection. Repository rulesets currently returned an empty list. Therefore the policy is documented but not falsely claimed as enabled.

Manual GitHub administration is required to activate this policy.
