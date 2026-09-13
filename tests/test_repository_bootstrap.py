from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_required_governance_files_exist() -> None:
    required = (
        "README.md",
        "CONTRIBUTING.md",
        "GITHUB_GOVERNANCE_V1.md",
        "PROJECT_STRUCTURE.md",
        "SECURITY.md",
        ".github/CODEOWNERS",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/general.md",
        ".github/workflows/pr-quality.yml",
        ".github/workflows/post-merge.yml",
        "requirements.txt",
        "requirements-dev.txt",
    )
    assert all((ROOT / path).is_file() for path in required)


def test_workflows_use_central_v1_contract() -> None:
    pr = (ROOT / ".github/workflows/pr-quality.yml").read_text(encoding="utf-8")
    post = (ROOT / ".github/workflows/post-merge.yml").read_text(encoding="utf-8")

    assert "office138-org/ci-standards/.github/workflows/pr-gate.yml@v1" in pr
    assert "office138-org/ci-standards/.github/workflows/post-merge.yml@v1" in post
    assert "cancel-in-progress: true" in pr
    assert "pull-requests: read" in post
    assert "require_pr_provenance: true" in post


def test_governance_v1_required_rules_are_present() -> None:
    source = (ROOT / "GITHUB_GOVERNANCE_V1.md").read_text(encoding="utf-8")
    markers = (
        "Direct push to `main` is prohibited",
        "Human Approval is mandatory",
        "Auto Merge is disabled",
        "post-merge failure blocks release/formal closure",
        "GOVERNANCE_VIOLATION_DIRECT_MAIN_PUSH",
    )
    normalized = source.replace("direct push", "Direct push", 1)
    assert all(marker in normalized for marker in markers)
