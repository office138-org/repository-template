# AI Repository Template

Standard starting point for AI-assisted development under GitHub Governance v1.

## Bootstrap

After creating a repository from this template:

1. Replace this README with the product name, purpose, and operating context.
2. Confirm `CONTRIBUTING.md`, `GITHUB_GOVERNANCE_V1.md`, and `PROJECT_STRUCTURE.md` fit the product.
3. Replace the placeholder smoke test with product-specific critical smoke coverage.
4. Update governance and critical test paths in `.github/workflows/pr-quality.yml`.
5. Confirm `pytest-xdist` compatibility before relying on parallel post-merge validation.
6. Open a PR and verify the PR Quality Gate before product development begins.

## CI model

PRs call the central `office138-org/ci-standards` reusable PR gate. Full regression, integration, E2E, and exhaustive validation run only after merge.

Human Approval is mandatory. Auto Merge is disabled. Direct push to `main` is prohibited.
