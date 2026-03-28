"""Tests for extract_values.py — leading-zero decimal parsing."""
from scripts.extract_values import parse_number_from_quote, parse_range_from_quote
import pytest


def test_parse_leading_zero_omitted_with_pattern():
    """r=.24 should parse as 0.24, not 24.0."""
    result = parse_number_from_quote("r=.24", pattern=r"r=(\.\d+)", fact_id="test")
    assert result == 0.24

def test_parse_leading_zero_omitted_auto():
    """Auto-detection should handle .40 format."""
    result = parse_number_from_quote("the correlation was r = .40 after correction", fact_id="test")
    assert abs(result - 0.40) < 0.001

def test_parse_leading_zero_omitted_negative():
    """Negative leading-zero-omitted: -.33 should parse as -0.33."""
    result = parse_number_from_quote("effect size was -.33", pattern=r"was (-?\.\d+)", fact_id="test")
    assert abs(result - (-0.33)) < 0.001

def test_parse_normal_decimal_unchanged():
    """0.24 should still parse as 0.24."""
    result = parse_number_from_quote("r = 0.24", pattern=r"r = ([\d.]+)", fact_id="test")
    assert result == 0.24

def test_parse_comma_number_unchanged():
    """13,988,129 should still parse correctly."""
    result = parse_number_from_quote("population reached 13,988,129", pattern=r"reached ([\d,]+)", fact_id="test")
    assert result == 13988129.0

def test_parse_auto_prefers_substantial():
    """Auto-detection should prefer comma-formatted numbers over small ones."""
    result = parse_number_from_quote("In 2023, population reached 13,988,129 people", fact_id="test")
    assert result == 13988129.0

def test_parse_mixed_numbers_with_leading_zero_omitted():
    """With a pattern targeting the decimal, it should return 0.40, not 2023."""
    result = parse_number_from_quote(
        "In 2023, the correlation was r=.40 after correction",
        pattern=r"r=(\.\d+)",
        fact_id="test",
    )
    assert abs(result - 0.40) < 0.001

def test_parse_auto_mixed_prefers_substantial_over_lzo():
    """Auto-detection with both 2023 and .40 should return 2023 (substantial wins)."""
    result = parse_number_from_quote("In 2023, the correlation was r=.40", fact_id="test")
    assert result == 2023.0


# ---------------------------------------------------------------------------
# parse_range_from_quote — ISO-date guard tests
# ---------------------------------------------------------------------------

def test_iso_date_not_parsed_as_range():
    """ISO date like 2020-01-01 must NOT be parsed as a numeric range."""
    with pytest.raises(ValueError, match="No range found"):
        parse_range_from_quote("published on 2020-01-01", fact_id="test")


def test_real_range_still_works():
    """A real numeric range like 1.0-2.0 should still parse."""
    low, high = parse_range_from_quote("warming of 1.0-2.0 degrees", fact_id="test")
    assert low == 1.0
    assert high == 2.0


def test_range_with_to_still_works():
    """N to N pattern should still work."""
    low, high = parse_range_from_quote("between 1.5 and 3.0", fact_id="test")
    assert low == 1.5
    assert high == 3.0


def test_range_after_iso_date_still_found():
    """A real range occurring after an ISO date should still be found."""
    low, high = parse_range_from_quote(
        "published 2020-01-01, warming of 1.0-2.0 degrees", fact_id="test"
    )
    assert low == 1.0
    assert high == 2.0


def test_range_immediately_after_date_still_found():
    """Range right after a date (tight spacing) should still be found."""
    low, high = parse_range_from_quote(
        "from 2020-01-01: 3.5-7.2 range observed", fact_id="test"
    )
    assert low == 3.5
    assert high == 7.2
