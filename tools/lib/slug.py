"""Slug derivation and duplicate claim detection."""

import json
import re
import unicodedata
from pathlib import Path


def slugify_claim(claim: str, max_length: int = 80) -> str:
    """Convert a claim string to a URL-safe slug.

    Lowercase, strip punctuation, replace spaces with hyphens,
    truncate at word boundary to max_length.
    """
    text = unicodedata.normalize("NFKC", claim)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    if len(text) > max_length:
        truncated = text[:max_length]
        last_sep = truncated.rfind("-")
        if last_sep > 0:
            truncated = truncated[:last_sep]
        text = truncated
    return text


def normalize_claim(claim: str) -> str:
    """Normalize a claim for duplicate comparison.

    Lowercase, strip all punctuation, collapse whitespace.
    """
    text = unicodedata.normalize("NFKC", claim)
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def find_duplicate_claim(proofs_dir: Path, claim: str) -> str | None:
    """Check if a normalized claim already exists in any published proof.

    Skips dot-prefixed directories (staging, backups).
    Returns the slug of the matching proof, or None if no duplicate.
    """
    proofs_dir = Path(proofs_dir)
    target_normalized = normalize_claim(claim)

    for slug_dir in sorted(proofs_dir.iterdir()):
        if not slug_dir.is_dir() or slug_dir.name.startswith("."):
            continue
        proof_json = slug_dir / "proof.json"
        if not proof_json.exists():
            continue
        try:
            data = json.loads(proof_json.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        existing_claim = data.get("claim_natural", "")
        if normalize_claim(existing_claim) == target_normalized:
            return slug_dir.name

    return None
