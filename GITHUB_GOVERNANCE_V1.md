# GitHub Governance v1

GITHUB_GOVERNANCE_VERSION = 1

This repository adopts the central standard from `office138-org/ci-standards`.

## PR-before-merge requirements

- repository safety
- Ruff correctness lint
- mypy on changed production Python
- governance validation
- critical smoke tests
- important unit tests

## Post-merge requirements

- full regression
- integration tests
- E2E tests
- exhaustive validation

Python repositories use `pytest -n auto --dist worksteal` after repository-specific compatibility validation.

## Operating rules

- direct push to `main` is prohibited
- a PR is mandatory
- Human Approval is mandatory after the final material PR change
- Auto Merge is disabled
- a post-merge failure blocks release/formal closure until corrected or reverted

## GitHub Free compensating control

For private repositories where GitHub Free cannot technically enforce the full PR/approval policy, the central post-merge workflow checks whether the default-branch SHA is associated with a merged PR. A direct-push violation fails with `GOVERNANCE_VIOLATION_DIRECT_MAIN_PUSH`.

## Repository-specific governance

Product-specific governance remains authoritative for runtime behavior, product boundaries, specifications, security contracts, and test selection. This document governs GitHub lifecycle and CI execution only.
