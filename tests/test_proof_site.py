"""Integration tests for tools/proof-site.py CLI."""

import json
import subprocess
import sys
import pytest
from pathlib import Path


TOOL_PATH = Path(__file__).parent.parent / "tools" / "proof-site.py"


def run_cli(*args, cwd=None):
    """Run proof-site.py and return CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(TOOL_PATH)] + list(args),
        capture_output=True, text=True, cwd=cwd,
    )


@pytest.fixture
def site_dir(tmp_path):
    """Create a minimal site structure."""
    proofs = tmp_path / "site" / "proofs"
    proofs.mkdir(parents=True)
    return tmp_path / "site"


@pytest.fixture
def source_proof(tmp_path):
    """Create a source directory with valid proof artifacts."""
    src = tmp_path / "my-proof"
    src.mkdir()
    (src / "proof.py").write_text(
        "import json\n"
        "print('running proof')\n"
        "summary = {\n"
        '    "claim_natural": "Water boils at 100C",\n'
        '    "verdict": "PROVED",\n'
        '    "fact_registry": {"A1": {"label": "boiling point"}},\n'
        '    "claim_formal": {"subject": "water", "property": "boiling_point"},\n'
        '    "key_results": {"boiling_point": 100},\n'
        '    "generator": {"name": "proof-engine", "version": "1.0.0",\n'
        '        "repo": "https://github.com/yaniv-golan/proof-engine",\n'
        '        "generated_at": "2026-03-30"},\n'
        "}\n"
        "print('=== PROOF SUMMARY (JSON) ===')\n"
        "print(json.dumps(summary))\n"
    )
    (src / "proof.md").write_text(
        "# Water Boils at 100C\n\n"
        "## Key Findings\n\n- Boils at 100C\n\n"
        "## Claim Interpretation\n\nStandard pressure.\n\n"
        "## Evidence Summary\n\n| ID | Fact |\n|---|---|\n| A1 | 100C |\n\n"
        "## Proof Logic\n\nThermodynamics.\n\n"
        "## Conclusion\n\n**Verdict: PROVED**\n"
    )
    (src / "proof_audit.md").write_text(
        "# Audit\n\n## Hardening Checklist\n\nAll pass.\n"
    )
    (src / "proof.json").write_text(json.dumps({
        "claim_natural": "Water boils at 100C",
        "verdict": "PROVED",
        "fact_registry": {"A1": {"label": "boiling point"}},
        "claim_formal": {"subject": "water", "property": "boiling_point"},
        "key_results": {"boiling_point": 100},
        "generator": {
            "name": "proof-engine", "version": "1.0.0",
            "repo": "https://github.com/yaniv-golan/proof-engine",
            "generated_at": "2026-03-30",
        },
    }))
    return src


def test_feature_creates_featured_json(site_dir):
    """feature should create featured.json if missing."""
    slug = "test-proof"
    (site_dir / "proofs" / slug).mkdir()
    (site_dir / "proofs" / slug / "proof.json").write_text('{"claim_natural":"test"}')
    result = run_cli("feature", slug, "--site-dir", str(site_dir))
    assert result.returncode == 0
    data = json.loads((site_dir / "proofs" / "featured.json").read_text())
    assert slug in data


def test_feature_idempotent(site_dir):
    """Featuring an already-featured proof should succeed."""
    slug = "test-proof"
    (site_dir / "proofs" / slug).mkdir()
    (site_dir / "proofs" / slug / "proof.json").write_text('{"claim_natural":"test"}')
    run_cli("feature", slug, "--site-dir", str(site_dir))
    result = run_cli("feature", slug, "--site-dir", str(site_dir))
    assert result.returncode == 0


def test_feature_nonexistent_proof(site_dir):
    """Featuring a non-existent proof should fail."""
    result = run_cli("feature", "no-such-proof", "--site-dir", str(site_dir))
    assert result.returncode != 0


def test_unfeature_removes_slug(site_dir):
    slug = "test-proof"
    (site_dir / "proofs" / slug).mkdir()
    (site_dir / "proofs" / slug / "proof.json").write_text('{"claim_natural":"test"}')
    run_cli("feature", slug, "--site-dir", str(site_dir))
    result = run_cli("unfeature", slug, "--site-dir", str(site_dir))
    assert result.returncode == 0
    data = json.loads((site_dir / "proofs" / "featured.json").read_text())
    assert slug not in data


def test_unfeature_not_featured(site_dir):
    """Unfeaturing a non-featured proof should fail."""
    result = run_cli("unfeature", "no-such", "--site-dir", str(site_dir))
    assert result.returncode != 0


# --- Publish integration tests ---

def test_publish_missing_artifacts(site_dir, tmp_path):
    """Publish should fail if required artifacts are missing."""
    src = tmp_path / "incomplete"
    src.mkdir()
    (src / "proof.py").write_text("# only proof.py")
    result = run_cli("publish", str(src), "--site-dir", str(site_dir))
    assert result.returncode != 0
    assert "Missing" in result.stderr


def test_publish_slug_collision_without_force(site_dir, source_proof):
    """Publish should fail on slug collision without --force."""
    slug = "water-boils-at-100c"
    target = site_dir / "proofs" / slug
    target.mkdir(parents=True)
    (target / "proof.json").write_text(json.dumps({
        "claim_natural": "Water boils at 100C"
    }))
    result = run_cli("publish", str(source_proof), "--slug", slug, "--site-dir", str(site_dir))
    assert result.returncode != 0
    assert "force" in result.stderr.lower() or "exists" in result.stderr.lower()


def test_publish_duplicate_claim_different_slug_refuses(site_dir, source_proof):
    """Duplicate claim under different slug should fail even with --force."""
    existing = site_dir / "proofs" / "old-slug"
    existing.mkdir(parents=True)
    (existing / "proof.json").write_text(json.dumps({
        "claim_natural": "Water boils at 100C"
    }))
    result = run_cli(
        "publish", str(source_proof),
        "--slug", "new-slug", "--force",
        "--site-dir", str(site_dir)
    )
    assert result.returncode != 0
    assert "old-slug" in result.stderr


def test_publish_bad_thumbnail(site_dir, source_proof):
    """Publish should fail if thumbnail is wrong size."""
    from PIL import Image
    img = Image.new("RGB", (500, 300), "red")
    img.save(source_proof / "thumbnail.png")
    result = run_cli("publish", str(source_proof), "--site-dir", str(site_dir))
    assert result.returncode != 0
    assert "240x240" in result.stderr
