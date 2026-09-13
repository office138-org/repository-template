# Contributing

## Required workflow

1. Create a non-main branch.
2. Make the smallest bounded change that satisfies the approved objective.
3. Open a pull request.
4. Wait for the PR Quality Gate to pass.
5. Obtain Human Approval after the final material change.
6. Merge manually. Auto Merge is disabled.
7. Verify Post-Merge Full Validation on `main`.

Direct push to `main` is prohibited.

## Quality gates

Before merge, the repository must run repository safety, Ruff correctness lint, mypy, governance validation, critical smoke tests, and important unit tests.

Comprehensive full regression, integration, E2E, and exhaustive validation are post-merge responsibilities and must not be duplicated in normal PR CI.

## Failure handling

Do not merge a failing PR. If post-merge validation fails, stop release/formal-closure work and create an immediate corrective PR or revert until `main` is green again.
