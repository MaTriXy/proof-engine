"""Tests for verify_citations.py — build_citation_detail."""
from scripts.verify_citations import build_citation_detail


def test_build_citation_detail_single_source():
    """Standard pattern: one FACT_REGISTRY entry per source."""
    fact_registry = {
        "B1": {"type": "B", "key": "src_a"},
        "B2": {"type": "B", "key": "src_b"},
    }
    citation_results = {
        "src_a": {"status": "verified", "method": "full_quote", "coverage_pct": None,
                  "fetch_error": None, "fetch_mode": "live", "message": "ok"},
        "src_b": {"status": "not_found", "method": None, "coverage_pct": None,
                  "fetch_error": None, "fetch_mode": "live", "message": "nope"},
    }
    empirical_facts = {
        "src_a": {"source_name": "A", "url": "http://a.com", "quote": "hello"},
        "src_b": {"source_name": "B", "url": "http://b.com", "quote": "world"},
    }
    detail = build_citation_detail(fact_registry, citation_results, empirical_facts)
    assert "B1" in detail
    assert "B2" in detail
    assert detail["B1"]["status"] == "verified"
    assert detail["B2"]["status"] == "not_found"


def test_build_citation_detail_multi_source():
    """Multi-source: one FACT_REGISTRY entry, multiple sub-source results."""
    fact_registry = {
        "B1": {"type": "B", "key": "src_a"},
    }
    citation_results = {
        "src_a_source_0": {"status": "verified", "method": "full_quote",
                           "coverage_pct": None, "fetch_error": None,
                           "fetch_mode": "live", "message": "ok"},
        "src_a_source_1": {"status": "not_found", "method": None,
                           "coverage_pct": None, "fetch_error": None,
                           "fetch_mode": "live", "message": "nope"},
    }
    empirical_facts = {
        "src_a": {
            "source_name": "Test",
            "sources": [
                {"url": "http://a.com", "quote": "hello"},
                {"url": "http://b.com", "quote": "world"},
            ],
        },
    }
    detail = build_citation_detail(fact_registry, citation_results, empirical_facts)
    assert "B1_source_0" in detail
    assert "B1_source_1" in detail
    assert detail["B1_source_0"]["status"] == "verified"
    assert detail["B1_source_0"]["url"] == "http://a.com"
    assert detail["B1_source_1"]["status"] == "not_found"
    assert detail["B1_source_1"]["url"] == "http://b.com"


def test_build_citation_detail_multi_source_short_sources_list():
    """Guard: citation_results has more sub-keys than sources list."""
    fact_registry = {"B1": {"type": "B", "key": "src_a"}}
    citation_results = {
        "src_a_source_0": {"status": "verified", "method": "full_quote",
                           "coverage_pct": None, "fetch_error": None,
                           "fetch_mode": "live", "message": "ok"},
        "src_a_source_1": {"status": "not_found", "method": None,
                           "coverage_pct": None, "fetch_error": None,
                           "fetch_mode": "live", "message": "nope"},
    }
    empirical_facts = {
        "src_a": {
            "source_name": "Test",
            "sources": [{"url": "http://a.com", "quote": "hello"}],
        },
    }
    detail = build_citation_detail(fact_registry, citation_results, empirical_facts)
    assert "B1_source_0" in detail
    assert detail["B1_source_0"]["url"] == "http://a.com"
    assert "B1_source_1" in detail
    assert detail["B1_source_1"]["url"] == ""
