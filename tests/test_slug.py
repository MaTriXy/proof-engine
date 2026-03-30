import json
import pytest
from pathlib import Path
from tools.lib.slug import slugify_claim, normalize_claim, find_duplicate_claim


def test_slugify_basic():
    assert slugify_claim("The Earth is flat") == "the-earth-is-flat"


def test_slugify_strips_punctuation():
    assert slugify_claim("Is it true? Yes!") == "is-it-true-yes"


def test_slugify_collapses_hyphens():
    assert slugify_claim("one -- two --- three") == "one-two-three"


def test_slugify_strips_leading_trailing_hyphens():
    assert slugify_claim("--hello world--") == "hello-world"


def test_slugify_truncates_long_claims():
    long_claim = "a " * 100
    slug = slugify_claim(long_claim)
    assert len(slug) <= 80


def test_slugify_truncates_at_word_boundary():
    claim = "the quick brown fox jumps over the lazy dog and keeps on running forever"
    slug = slugify_claim(claim, max_length=30)
    assert "-" not in slug or not slug.endswith("-")
    assert len(slug) <= 30


def test_normalize_claim():
    assert normalize_claim("The Earth Is FLAT!") == "the earth is flat"
    assert normalize_claim("It's 100% true.") == "its 100 true"


def test_normalize_claim_unicode():
    assert normalize_claim("it\u2019s a \u201ctest\u201d") == "its a test"


def test_find_duplicate_none(tmp_path):
    proofs_dir = tmp_path / "proofs"
    proofs_dir.mkdir()
    slug_dir = proofs_dir / "existing-proof"
    slug_dir.mkdir()
    (slug_dir / "proof.json").write_text(json.dumps({
        "claim_natural": "The sky is blue"
    }))
    result = find_duplicate_claim(proofs_dir, "The Earth is round")
    assert result is None


def test_find_duplicate_exact(tmp_path):
    proofs_dir = tmp_path / "proofs"
    proofs_dir.mkdir()
    slug_dir = proofs_dir / "sky-is-blue"
    slug_dir.mkdir()
    (slug_dir / "proof.json").write_text(json.dumps({
        "claim_natural": "The sky is blue"
    }))
    result = find_duplicate_claim(proofs_dir, "The sky is blue!")
    assert result == "sky-is-blue"


def test_find_duplicate_normalized(tmp_path):
    proofs_dir = tmp_path / "proofs"
    proofs_dir.mkdir()
    slug_dir = proofs_dir / "earth-round"
    slug_dir.mkdir()
    (slug_dir / "proof.json").write_text(json.dumps({
        "claim_natural": "The Earth is round."
    }))
    result = find_duplicate_claim(proofs_dir, "the earth is round")
    assert result == "earth-round"
