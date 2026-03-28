"""
Proof: The climate has always changed — today's warming is not unusual or alarming.
Generated: 2026-03-28

Claim type: Compound qualitative — two sub-claims evaluated independently.
  SC1 (affirm):  Earth's climate has undergone natural change throughout history.
  SC2 (disprove): Today's warming is not unusual or alarming relative to that natural variability.
"""
import json
import os
import sys

PROOF_ENGINE_ROOT = "/Users/yaniv/Documents/code/proof-engine/proof-engine/skills/proof-engine"
sys.path.insert(0, PROOF_ENGINE_ROOT)
from datetime import date

from scripts.verify_citations import verify_all_citations, build_citation_detail
from scripts.computations import compare

# ---------------------------------------------------------------------------
# 1. CLAIM INTERPRETATION (Rule 4)
# ---------------------------------------------------------------------------
CLAIM_NATURAL = "The climate has always changed — today's warming is not unusual or alarming."

CLAIM_FORMAL = {
    "subject": "current global warming",
    "sub_claims": [
        {
            "id": "SC1",
            "property": (
                "Earth's climate has undergone documented natural changes "
                "(glacial/interglacial cycles, natural forcings) throughout geological history"
            ),
            "operator": ">=",
            "threshold": 2,
            "proof_direction": "affirm",
            "operator_note": (
                "SC1 is universally accepted — natural climate variability is real and well-documented. "
                "True if at least 2 independent authoritative sources confirm natural climate cycles and forcings. "
                "This sub-claim is not in dispute."
            ),
        },
        {
            "id": "SC2",
            "property": (
                "today's warming is not unusual or alarming "
                "(i.e., falls within the range of natural variability)"
            ),
            "operator": ">=",
            "threshold": 3,
            "proof_direction": "disprove",
            "operator_note": (
                "SC2 is the contentious part of the claim. "
                "A disproof requires at least 3 independent authoritative sources "
                "establishing that current warming IS unprecedented or unusual — "
                "directly contradicting the sub-claim's 'not unusual' assertion. "
                "Threshold of 3 chosen because the domain has many authoritative independent sources "
                "(IPCC, NASA, NOAA) and strong scientific consensus, so high source count is achievable. "
                "If threshold is met, SC2 is DISPROVED (the 'not unusual or alarming' claim is false)."
            ),
        },
    ],
    "compound_operator": "AND",
    "operator_note": (
        "The compound claim asserts both SC1 (natural variability is real) AND SC2 "
        "(today's warming is not unusual). Both must hold for the claim to be PROVED. "
        "If SC1 is proved but SC2 is disproved, the verdict is PARTIALLY VERIFIED: "
        "the climate does indeed always change, but that historical variability does not imply "
        "today's warming is within natural bounds."
    ),
}

# ---------------------------------------------------------------------------
# 2. FACT REGISTRY
# ---------------------------------------------------------------------------
FACT_REGISTRY = {
    "B1": {
        "key": "sc1_source_a",
        "label": "SC1: NOAA Climate.gov Q&A — natural glacial-interglacial cycles on 100,000-year timescales",
    },
    "B2": {
        "key": "sc1_source_b",
        "label": "SC1: NOAA NCEI — natural climate forcing mechanisms (solar and volcanic)",
    },
    "B3": {
        "key": "sc2_source_a",
        "label": "SC2 disproof: IPCC AR6 (2021) — current changes unprecedented in thousands of years",
    },
    "B4": {
        "key": "sc2_source_b",
        "label": "SC2 disproof: NASA Earth Observatory — 2024 was 1.47°C above pre-industrial baseline",
    },
    "B5": {
        "key": "sc2_source_c",
        "label": "SC2 disproof: NOAA Climate.gov — atmospheric CO2 higher than any point in human history",
    },
    "B6": {
        "key": "sc2_source_d",
        "label": "SC2 disproof: NOAA NCEI — temperatures increased at unprecedented rate over 50 years",
    },
    "A1": {"label": "SC1: confirmed source count (natural variability)", "method": None, "result": None},
    "A2": {"label": "SC2: confirmed disproof source count (warming IS unusual)", "method": None, "result": None},
}

# ---------------------------------------------------------------------------
# 3. EMPIRICAL FACTS
# ---------------------------------------------------------------------------
empirical_facts = {
    # SC1: sources confirming natural climate variability
    "sc1_source_a": {
        "quote": (
            "Yes. Earth has experienced cold periods (informally referred to as "
            "\"ice ages,\" or \"glacials\") and warm periods (\"interglacials\") "
            "on roughly 100,000-year cycles for at least the last 1 million years"
        ),
        "url": "https://www.climate.gov/news-features/climate-qa/hasnt-earth-warmed-and-cooled-naturally-throughout-history",
        "source_name": "NOAA Climate.gov — Has Earth warmed and cooled naturally throughout history? (Climate Q&A)",
    },
    "sc1_source_b": {
        "quote": (
            "Natural climate variations are a result of forcings, factors that drive the climate "
            "system to change. These forcings include solar and volcanic activity."
        ),
        "url": "https://www.ncei.noaa.gov/news/climate-change-context-paleoclimate",
        "source_name": "NOAA NCEI — Climate Change in the Context of Paleoclimate",
    },
    # SC2 disproof: sources establishing current warming IS unusual/unprecedented
    "sc2_source_a": {
        "quote": (
            "Many of the changes observed in the climate are unprecedented "
            "in thousands, if not hundreds of thousands of years"
        ),
        "url": "https://www.ipcc.ch/2021/08/09/ar6-wg1-20210809-pr/",
        "source_name": "IPCC — AR6 Working Group I Press Release (August 2021)",
    },
    "sc2_source_b": {
        "quote": (
            "Earth in 2024 was about 1.47 degrees Celsius (2.65 degrees Fahrenheit) "
            "warmer than the 1850-1900 average"
        ),
        "url": "https://science.nasa.gov/earth/earth-observatory/2024-was-the-warmest-year-on-record-153806/",
        "source_name": "NASA Earth Observatory — 2024 Was the Warmest Year on Record",
    },
    "sc2_source_c": {
        "quote": "Carbon dioxide levels today are higher than at any point in human history.",
        "url": "https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide",
        "source_name": "NOAA Climate.gov — Climate Change: Atmospheric Carbon Dioxide",
    },
    "sc2_source_d": {
        "quote": "Temperatures have increased over the last 50 years at an unprecedented rate.",
        "url": "https://www.ncei.noaa.gov/news/climate-change-context-paleoclimate",
        "source_name": "NOAA NCEI — Climate Change in the Context of Paleoclimate",
    },
}

# ---------------------------------------------------------------------------
# 4. CITATION VERIFICATION (Rule 2)
# ---------------------------------------------------------------------------
print("\n--- Citation Verification ---")
citation_results = verify_all_citations(empirical_facts, wayback_fallback=True)

# ---------------------------------------------------------------------------
# 5. COUNT VERIFIED SOURCES PER SUB-CLAIM
# ---------------------------------------------------------------------------
COUNTABLE_STATUSES = ("verified", "partial")

sc1_keys = [k for k in empirical_facts if k.startswith("sc1_")]
sc2_keys = [k for k in empirical_facts if k.startswith("sc2_")]

n_sc1 = sum(
    1 for k in sc1_keys
    if citation_results[k]["status"] in COUNTABLE_STATUSES
)
n_sc2_disproof = sum(
    1 for k in sc2_keys
    if citation_results[k]["status"] in COUNTABLE_STATUSES
)

print(f"\n  SC1 confirmed sources: {n_sc1} / {len(sc1_keys)}")
print(f"  SC2 disproof confirmed sources: {n_sc2_disproof} / {len(sc2_keys)}")

# ---------------------------------------------------------------------------
# 6. PER-SUB-CLAIM EVALUATION (Rule 7 — use compare())
# ---------------------------------------------------------------------------
sc1_threshold = CLAIM_FORMAL["sub_claims"][0]["threshold"]
sc2_threshold = CLAIM_FORMAL["sub_claims"][1]["threshold"]

sc1_holds = compare(
    n_sc1, ">=", sc1_threshold,
    label="SC1: natural variability confirmed by independent sources",
)
sc2_disproof_holds = compare(
    n_sc2_disproof, ">=", sc2_threshold,
    label="SC2 disproof: warming IS unprecedented (contradicts 'not unusual')",
)

# SC2 claim_holds: the sub-claim "today's warming is not unusual" holds only if
# the disproof FAILS (not enough counter-evidence).
sc2_claim_holds = not sc2_disproof_holds

# ---------------------------------------------------------------------------
# 7. ADVERSARIAL CHECKS (Rule 5)
# ---------------------------------------------------------------------------
adversarial_checks = [
    {
        "question": (
            "Does the Medieval Warm Period (MWP, ~900–1200 AD) show that current warming "
            "is within natural bounds?"
        ),
        "verification_performed": (
            "Searched for 'Medieval Warm Period global temperature comparison current warming' "
            "and 'MWP warmer than today scientific evidence'. "
            "Reviewed IPCC AR6 paleoclimate chapter findings and Mann et al. reconstructions."
        ),
        "finding": (
            "The MWP was a real regional warming (predominantly North Atlantic/Europe) but "
            "paleoclimate reconstructions consistently show global MWP temperatures were lower "
            "than current levels. IPCC AR6 WG1 states: 'The global nature and magnitude of "
            "current warmth is unprecedented in the context of the last 2000 years' (high confidence). "
            "The MWP does not establish that today's warming is within natural bounds globally."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Are there credible scientific sources that argue today's warming is within "
            "natural variability ranges?"
        ),
        "verification_performed": (
            "Searched for 'climate scientists natural variability explanation current warming', "
            "'Roy Spencer Judith Curry natural climate warming', and "
            "'scientific papers rejecting anthropogenic warming 2020 2021 2022'. "
            "Reviewed arguments from Spencer, Curry, and Lindzen."
        ),
        "finding": (
            "A small minority of climate scientists (Spencer, Curry, Lindzen) have argued that "
            "natural variability plays a larger role than IPCC consensus states. However, their "
            "analyses do not claim warming is 'not unusual' — they debate attribution and sensitivity, "
            "not the existence or magnitude of the trend. Spencer's UAH satellite dataset, often cited "
            "by skeptics, itself shows a warming trend of ~0.15°C/decade since 1979. "
            "No credible scientific source claims current CO2 (422+ ppm) or warming rate (~1.47°C above "
            "pre-industrial) is within the natural Holocene variability range."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Could urban heat island (UHI) effects or station biases explain the observed "
            "warming as a measurement artifact rather than real warming?"
        ),
        "verification_performed": (
            "Searched for 'urban heat island effect global temperature record bias correction', "
            "'Berkeley Earth temperature UHI adjustment', and NOAA station homogenization methodology."
        ),
        "finding": (
            "Berkeley Earth's independent analysis (Rohde et al. 2013) specifically accounted for UHI "
            "effects and found it explains less than 0.1°C of the ~1.5°C observed warming. "
            "Ocean temperature records (sea surface temperatures, Argo floats) — which are unaffected by "
            "UHI — show the same warming trend, ruling out land-station bias as the primary explanation. "
            "UHI does not account for observed warming."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Does the logical structure of the claim (climate has always changed, THEREFORE "
            "today's warming is not unusual) hold?"
        ),
        "verification_performed": (
            "Analyzed the logical structure: the premise (climate changes naturally) does not entail "
            "the conclusion (current change is within natural bounds). This is a non sequitur. "
            "Past natural changes occurred at different rates and magnitudes; their existence does not "
            "bound present or future change."
        ),
        "finding": (
            "The argument form is logically invalid. Natural climate variability confirms that "
            "forcing can drive large climate changes — but this does not show current forcing is natural "
            "or current rates are within historical norms. The IPCC AR6 explicitly addresses this: "
            "past natural changes are well-understood and cannot explain the post-industrial warming."
        ),
        "breaks_proof": False,
    },
]

# ---------------------------------------------------------------------------
# 8. VERDICT AND STRUCTURED OUTPUT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Independence note for cross-checks
    # SC1: two NOAA-family sources (climate.gov and NCEI) — same upstream authority,
    #   independently published; note: weaker independence than inter-agency sources
    # SC2 disproof: IPCC (intergovernmental, 234 scientists), NASA (GISS), NOAA (two pages) —
    #   genuinely independent organizations and datasets

    any_unverified = any(
        cr["status"] != "verified" for cr in citation_results.values()
    )
    sc1_any_unverified = any(
        citation_results[k]["status"] != "verified" for k in sc1_keys
    )
    sc2_any_unverified = any(
        citation_results[k]["status"] != "verified" for k in sc2_keys
    )

    # Sub-claim verdicts
    if sc1_holds and not sc1_any_unverified:
        sc1_verdict = "PROVED"
    elif sc1_holds and sc1_any_unverified:
        sc1_verdict = "PROVED (with unverified citations)"
    else:
        sc1_verdict = "UNDETERMINED"

    if sc2_disproof_holds and not sc2_any_unverified:
        sc2_verdict = "DISPROVED"
    elif sc2_disproof_holds and sc2_any_unverified:
        sc2_verdict = "DISPROVED (with unverified citations)"
    else:
        sc2_verdict = "UNDETERMINED"

    # Compound verdict
    if sc1_holds and sc2_disproof_holds and not any_unverified:
        verdict = "PARTIALLY VERIFIED"
    elif sc1_holds and sc2_disproof_holds and any_unverified:
        verdict = "PARTIALLY VERIFIED (with unverified citations)"
    elif sc1_holds and not sc2_disproof_holds:
        # SC2 neither proved nor disproved
        verdict = "UNDETERMINED"
    else:
        verdict = "UNDETERMINED"

    # Update FACT_REGISTRY with computed results
    FACT_REGISTRY["A1"]["method"] = f"count(SC1 verified citations) = {n_sc1}"
    FACT_REGISTRY["A1"]["result"] = f"{n_sc1} independent sources confirmed"
    FACT_REGISTRY["A2"]["method"] = f"count(SC2 disproof verified citations) = {n_sc2_disproof}"
    FACT_REGISTRY["A2"]["result"] = f"{n_sc2_disproof} independent sources confirmed warming IS unusual"

    citation_detail = build_citation_detail(FACT_REGISTRY, citation_results, empirical_facts)

    # Extractions: for qualitative proofs, record citation status per B-fact
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
                "description": "SC1 independent sources (natural variability)",
                "n_sources_consulted": len(sc1_keys),
                "n_sources_verified": n_sc1,
                "sources": {k: citation_results[k]["status"] for k in sc1_keys},
                "independence_note": (
                    "Both SC1 sources are NOAA-family (climate.gov and NCEI) — same upstream authority, "
                    "independently published pages. Provides corroboration but weaker than inter-agency independence."
                ),
            },
            {
                "description": "SC2 disproof independent sources (warming is unprecedented)",
                "n_sources_consulted": len(sc2_keys),
                "n_sources_verified": n_sc2_disproof,
                "sources": {k: citation_results[k]["status"] for k in sc2_keys},
                "independence_note": (
                    "SC2 disproof spans three independent organizations: "
                    "IPCC (intergovernmental body, 234 scientists from 65 countries), "
                    "NASA (Goddard Institute for Space Studies), and NOAA (two pages from NCEI and climate.gov). "
                    "These organizations maintain independent datasets and arrive at convergent conclusions."
                ),
            },
        ],
        "adversarial_checks": adversarial_checks,
        "sub_claim_verdicts": {
            "SC1": sc1_verdict,
            "SC2": sc2_verdict,
        },
        "verdict": verdict,
        "key_results": {
            "sc1_confirmed_sources": n_sc1,
            "sc1_threshold": sc1_threshold,
            "sc1_holds": sc1_holds,
            "sc1_verdict": sc1_verdict,
            "sc2_disproof_confirmed_sources": n_sc2_disproof,
            "sc2_threshold": sc2_threshold,
            "sc2_disproof_holds": sc2_disproof_holds,
            "sc2_claim_holds": sc2_claim_holds,
            "sc2_verdict": sc2_verdict,
            "compound_claim_holds": sc1_holds and sc2_claim_holds,
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
