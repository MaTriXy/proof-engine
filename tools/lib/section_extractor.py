import re


def _normalize_heading(heading: str) -> str:
    """Normalize heading to title case for consistent key lookup."""
    return heading.strip().title()


def extract_sections(markdown: str) -> dict:
    """Split markdown into sections by level-2 headings.

    Returns dict mapping normalized heading text (title-cased) to section content.
    Level-3+ subheadings are included in their parent section's content.
    Content before the first ## heading is discarded.
    """
    pattern = re.compile(r"^## (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(markdown))

    sections = {}
    for i, match in enumerate(matches):
        heading = _normalize_heading(match.group(1))
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        content = markdown[start:end].strip()
        sections[heading] = content

    return sections


def validate_required_sections(sections: dict, required: list[str]) -> list[str]:
    """Check that all required sections are present.

    Comparison is case-insensitive (both sides normalized via title()).
    Returns list of missing section names.
    """
    section_names = {name.lower() for name in sections}
    missing = []
    for req in required:
        if req.lower() not in section_names:
            missing.append(req)
    return missing
