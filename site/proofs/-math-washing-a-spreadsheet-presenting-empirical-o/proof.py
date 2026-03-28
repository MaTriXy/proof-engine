"""
Proof: "Math washing" a spreadsheet (presenting empirical observations as universal theorems)
       is valid scientific practice.
Generated: 2026-03-28
Proof direction: DISPROVE — three independent authoritative sources confirm this
practice violates core standards of valid scientific methodology.
"""
import json
import os
import sys
from datetime import date

PROOF_ENGINE_ROOT = "/Users/yaniv/Documents/code/proof-engine/proof-engine/skills/proof-engine"
sys.path.insert(0, PROOF_ENGINE_ROOT)

from scripts.verify_citations import verify_all_citations, build_citation_detail
from scripts.computations import compare

# 1. CLAIM INTERPRETATION (Rule 4)
CLAIM_NATURAL = (
    '"Math washing" a spreadsheet (presenting empirical observations as universal '
    "theorems) is valid scientific practice."
)
CLAIM_FORMAL = {
    "subject": "Math washing (presenting empirical spreadsheet observations as universal theorems)",
    "property": "constitutes valid scientific practice",
    "operator": ">=",
    "operator_note": (
        "'Valid scientific practice' is interpreted as methodology meeting the standards "
        "recognized by the scientific community: specifically, the hypothetico-deductive "
        "model requiring hypothesis formation, falsifiability, and controlled testing. "
        "The DISPROOF threshold is 3 independent authoritative sources that confirm "
        "that presenting empirical observations alone as universal theorems—without "
        "hypothesis formation, testing for falsifiability, and independent replication—"
        "violates these standards. 'Universal theorem' is interpreted in the strict "
        "sense: a claim that holds without exception for all instances, not merely a "
        "statistical regularity or empirical generalization. A threshold of 3 is used "
        "to require broad expert consensus; a single contrary source would be insufficient."
    ),
    "threshold": 3,
    "proof_direction": "disprove",
}

# 2. FACT REGISTRY
FACT_REGISTRY = {
    "B1": {
        "key": "source_britannica_popper",
        "label": "Britannica: Popper's falsifiability criterion — scientific validity requires falsifiability",
    },
    "B2": {
        "key": "source_sep_scientific_method",
        "label": "Stanford Encyclopedia of Philosophy: scientific method requires reasoning beyond observation",
    },
    "B3": {
        "key": "source_catalog_of_bias",
        "label": "Catalog of Bias: data-dredging is a recognized methodological distortion in science",
    },
    "A1": {
        "label": "Count of authoritative sources confirming math-washing is not valid scientific practice",
        "method": None,
        "result": None,
    },
}

# 3. EMPIRICAL FACTS
# These are sources that REJECT the claim — confirming math-washing is NOT valid science.
empirical_facts = {
    "source_britannica_popper": {
        "quote": (
            "a theory is genuinely scientific only if it is possible in principle to establish "
            "that it is false."
        ),
        "url": "https://www.britannica.com/topic/criterion-of-falsifiability",
        "source_name": "Encyclopaedia Britannica — criterion of falsifiability",
    },
    "source_sep_scientific_method": {
        "quote": (
            "In addition to careful observation, then, scientific method requires a logic as a "
            "system of reasoning for properly arranging, but also inferring beyond, what is known "
            "by observation."
        ),
        "url": "https://plato.stanford.edu/entries/scientific-method/",
        "source_name": "Stanford Encyclopedia of Philosophy — scientific method",
    },
    "source_catalog_of_bias": {
        "quote": (
            "A distortion that arises from presenting the results of unplanned statistical tests "
            "as if they were a fully prespecified course of analyses."
        ),
        "url": "https://catalogofbias.org/biases/data-dredging-bias/",
        "source_name": "Catalog of Bias — data-dredging bias",
    },
}

# 4. CITATION VERIFICATION (Rule 2)
citation_results = verify_all_citations(empirical_facts, wayback_fallback=True)

# 5. COUNT SOURCES WITH VERIFIED CITATIONS
# A source counts toward the threshold if its quote was found on the page
# (status = "verified" or "partial").
COUNTABLE_STATUSES = ("verified", "partial")
n_confirmed = sum(
    1 for key in empirical_facts
    if citation_results[key]["status"] in COUNTABLE_STATUSES
)
print(f"  Confirmed sources: {n_confirmed} / {len(empirical_facts)}")

# 6. CLAIM EVALUATION — MUST use compare(), never hardcode claim_holds (Rule 7)
# claim_holds = True means we have enough confirmed sources to DISPROVE the claim.
claim_holds = compare(
    n_confirmed,
    CLAIM_FORMAL["operator"],
    CLAIM_FORMAL["threshold"],
    label="verified source count vs disproof threshold",
)

# 7. ADVERSARIAL CHECKS (Rule 5)
# Searching for counter-evidence: arguments that this practice might be valid science.
adversarial_checks = [
    {
        "question": (
            "Is there a scientific tradition that validates presenting inductive "
            "generalizations from data as universal laws without further testing?"
        ),
        "verification_performed": (
            "Searched 'defense inductive reasoning empirical observations sufficient "
            "universal scientific laws' and 'Bacon inductivism valid science pattern "
            "observation'. Found inductivism (Bacon's model) as a candidate defense."
        ),
        "finding": (
            "Even Bacon's inductivism — the strongest defense of inductive science — "
            "requires systematic collection, replication, and elimination of observer "
            "bias before generalizing. Naive inductivism has been largely discredited "
            "in philosophy of science (Popper, 1934; Hempel, 1965). More importantly, "
            "no form of inductivism endorses presenting patterns as universal 'theorems' "
            "(a term implying deductive necessity) rather than empirical generalizations."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Does Exploratory Data Analysis (EDA) validate presenting spreadsheet "
            "patterns as scientific findings?"
        ),
        "verification_performed": (
            "Searched 'Tukey exploratory data analysis purpose hypothesis generation "
            "not confirmation'. Reviewed EDA methodology documentation."
        ),
        "finding": (
            "EDA (Tukey 1977) is an explicitly hypothesis-generating practice, not "
            "hypothesis-confirming. Tukey's framework is designed to produce candidate "
            "hypotheses for subsequent testing, not to generate universal theorems. "
            "This supports the disproof: the EDA literature itself distinguishes "
            "pattern-finding from universal claims."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Could 'math washing' be valid in limited empirical domains like actuarial "
            "science, empirical economics, or physics phenomenology?"
        ),
        "verification_performed": (
            "Searched 'stylized facts empirical economics vs universal law', "
            "'actuarial science empirical observation universal theorem'. Reviewed "
            "terminology used in empirical economic methodology."
        ),
        "finding": (
            "Empirical economics explicitly distinguishes between 'stylized facts' "
            "(regularities observed in data) and 'economic laws' or theorems. "
            "Kaldor (1961) introduced 'stylized facts' precisely because observed "
            "patterns in data do NOT constitute universal theorems without theoretical "
            "grounding. Even in phenomenological physics, empirical regularities "
            "(e.g., Kepler's laws) were only elevated to scientific law status after "
            "being derived from deeper theoretical principles (Newton's mechanics). "
            "No domain endorses presenting data patterns as universal theorems directly."
        ),
        "breaks_proof": False,
    },
]

# 8. VERDICT AND STRUCTURED OUTPUT
if __name__ == "__main__":
    any_unverified = any(
        cr["status"] != "verified" for cr in citation_results.values()
    )
    is_disproof = CLAIM_FORMAL.get("proof_direction") == "disprove"
    any_breaks = any(ac.get("breaks_proof") for ac in adversarial_checks)

    if any_breaks:
        verdict = "UNDETERMINED"
    elif claim_holds and not any_unverified:
        verdict = "DISPROVED" if is_disproof else "PROVED"
    elif claim_holds and any_unverified:
        verdict = (
            "DISPROVED (with unverified citations)"
            if is_disproof
            else "PROVED (with unverified citations)"
        )
    elif not claim_holds:
        verdict = "UNDETERMINED"
    else:
        verdict = "UNDETERMINED"

    FACT_REGISTRY["A1"]["method"] = f"count(verified citations) = {n_confirmed}"
    FACT_REGISTRY["A1"]["result"] = (
        f"{n_confirmed} sources confirmed (threshold: {CLAIM_FORMAL['threshold']})"
    )

    citation_detail = build_citation_detail(FACT_REGISTRY, citation_results, empirical_facts)

    # For qualitative proofs, each B-type fact records citation status
    extractions = {}
    for fid, info in FACT_REGISTRY.items():
        if not fid.startswith("B"):
            continue
        ef_key = info["key"]
        cr = citation_results.get(ef_key, {})
        extractions[fid] = {
            "value": cr.get("status", "unknown"),
            "value_in_quote": cr.get("status") in COUNTABLE_STATUSES,
            "quote_snippet": empirical_facts[ef_key]["quote"][:80],
        }

    summary = {
        "fact_registry": {
            fid: {k: v for k, v in info.items()}
            for fid, info in FACT_REGISTRY.items()
        },
        "claim_formal": CLAIM_FORMAL,
        "claim_natural": CLAIM_NATURAL,
        "citations": citation_detail,
        "extractions": extractions,
        "cross_checks": [
            {
                "description": "Multiple independent authoritative sources consulted (Britannica, SEP, Catalog of Bias)",
                "n_sources_consulted": len(empirical_facts),
                "n_sources_verified": n_confirmed,
                "sources": {k: citation_results[k]["status"] for k in empirical_facts},
                "independence_note": (
                    "Sources are from different institutions and traditions: "
                    "encyclopedic philosophy (Britannica), academic philosophy reference "
                    "(Stanford Encyclopedia), and medical/scientific methodology catalog "
                    "(Oxford-affiliated Catalog of Bias). Each addresses a distinct "
                    "failure mode of math-washing: falsifiability failure (B1), "
                    "insufficiency of observation alone (B2), and data-dredging distortion (B3)."
                ),
            }
        ],
        "adversarial_checks": adversarial_checks,
        "verdict": verdict,
        "key_results": {
            "n_confirmed": n_confirmed,
            "threshold": CLAIM_FORMAL["threshold"],
            "operator": CLAIM_FORMAL["operator"],
            "claim_holds": claim_holds,
            "proof_direction": "disprove",
        },
        "generator": {
            "name": "proof-engine",
            "version": open(os.path.join(PROOF_ENGINE_ROOT, "VERSION")).read().strip(),
            "repo": "https://github.com/yaniv-golan/proof-engine",
            "generated_at": date.today().isoformat(),
        },
    }

    print("\n=== PROOF SUMMARY (JSON) ===")
    print(json.dumps(summary, indent=2, default=str))
