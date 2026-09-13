# Project Structure

Recommended baseline for Python AI repositories:

```text
.
├─ .github/
│  ├─ CODEOWNERS
│  ├─ ISSUE_TEMPLATE/
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/
├─ docs/
│  ├─ architecture/
│  └─ governance/
├─ src/ or tools/
├─ tests/
├─ README.md
├─ CONTRIBUTING.md
├─ GITHUB_GOVERNANCE_V1.md
├─ PROJECT_STRUCTURE.md
├─ requirements.txt
└─ requirements-dev.txt
```

## Boundaries

- product/runtime code belongs in product-owned source directories
- product-specific governance belongs in `docs/governance/`
- architecture/specification authority belongs in `docs/architecture/`
- reusable CI orchestration does not belong in the product repository; callers reference `office138-org/ci-standards`
- tests must include explicit governance coverage and critical smoke/important unit coverage

Repositories may adapt directory names when product architecture requires it, but must preserve the Governance v1 lifecycle and equivalent validation coverage.
