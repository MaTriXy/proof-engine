import pytest
from tools.lib.section_extractor import extract_sections, validate_required_sections

SAMPLE_PROOF_MD = """\
# Proof: Test claim

Some intro text.

## Key Findings

- Finding 1
- Finding 2

## Claim Interpretation

The claim means X.

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | Something | Yes |

## Proof Logic

### Step 1: Do thing

Some reasoning.

### Step 2: Do other thing

More reasoning.

## Counter-Evidence Search

Nothing found.

## Conclusion

The claim is PROVED.
"""


def test_extract_sections_returns_dict():
    sections = extract_sections(SAMPLE_PROOF_MD)
    assert isinstance(sections, dict)


def test_extract_sections_finds_all_level2_headings():
    sections = extract_sections(SAMPLE_PROOF_MD)
    assert "Key Findings" in sections
    assert "Claim Interpretation" in sections
    assert "Evidence Summary" in sections
    assert "Proof Logic" in sections
    assert "Counter-Evidence Search" in sections
    assert "Conclusion" in sections


def test_extract_sections_preserves_subheadings():
    sections = extract_sections(SAMPLE_PROOF_MD)
    assert "### Step 1: Do thing" in sections["Proof Logic"]
    assert "### Step 2: Do other thing" in sections["Proof Logic"]


def test_extract_sections_normalizes_to_title_case():
    md = "## KEY FINDINGS\n\nSome text.\n"
    sections = extract_sections(md)
    assert "Key Findings" in sections


def test_extract_sections_strips_heading_whitespace():
    md = "##   key findings  \n\nSome text.\n"
    sections = extract_sections(md)
    assert "Key Findings" in sections


def test_validate_required_sections_passes():
    sections = extract_sections(SAMPLE_PROOF_MD)
    required = ["Key Findings", "Claim Interpretation", "Evidence Summary",
                 "Proof Logic", "Conclusion"]
    missing = validate_required_sections(sections, required)
    assert missing == []


def test_validate_required_sections_reports_missing():
    sections = {"Key Findings": "text"}
    required = ["Key Findings", "Conclusion"]
    missing = validate_required_sections(sections, required)
    assert "Conclusion" in missing


def test_validate_required_sections_case_insensitive():
    sections = {"KEY FINDINGS": "text", "conclusion": "text"}
    required = ["Key Findings", "Conclusion"]
    missing = validate_required_sections(sections, required)
    assert missing == []


def test_intro_text_before_first_heading_excluded():
    sections = extract_sections(SAMPLE_PROOF_MD)
    assert "Some intro text" not in str(sections.values())
