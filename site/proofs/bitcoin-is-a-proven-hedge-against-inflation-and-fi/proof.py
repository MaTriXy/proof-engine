"""
Proof: Bitcoin is a proven hedge against inflation and fiat currency collapse.
Generated: 2026-03-28
"""
import json
import os
import sys

PROOF_ENGINE_ROOT = "/Users/yaniv/Documents/code/proof-engine/proof-engine/skills/proof-engine"
sys.path.insert(0, PROOF_ENGINE_ROOT)
from datetime import date

from scripts.verify_citations import verify_all_citations, build_citation_detail
from scripts.computations import compare

# 1. CLAIM INTERPRETATION (Rule 4)
CLAIM_NATURAL = "Bitcoin is a proven hedge against inflation and fiat currency collapse."
CLAIM_FORMAL = {
    "subject": "Bitcoin",
    "property": (
        "proven (consistent, empirically reliable) hedge against both "
        "(SC1) ordinary consumer-price-index (CPI) inflation and "
        "(SC2) fiat currency collapse or hyperinflation"
    ),
    "operator": "==",
    "operator_note": (
        "'Proven' is interpreted strictly: requires consistent, documented empirical "
        "performance under the claimed conditions with no verified counterexamples. "
        "The claim is a conjunction (SC1 AND SC2): both sub-claims must be proven. "
        "SC1 proof direction is FALSIFICATION — one verified counterexample (Bitcoin "
        "declining during a period of high CPI inflation) is sufficient to disprove the "
        "'proven' designation for SC1. SC2 proof direction is CONSENSUS — requires >= 3 "
        "independent verified sources establishing Bitcoin reliably protects value during "
        "fiat collapse; having found only partial evidence (stablecoins preferred over "
        "Bitcoin in hyperinflationary economies), SC2 does not reach 'proven' status. "
        "The compound claim holds only if BOTH SC1 and SC2 are individually proven."
    ),
    "threshold": True,
    "sub_claims": {
        "SC1": "Bitcoin is a proven hedge against ordinary CPI inflation",
        "SC2": "Bitcoin is a proven hedge against fiat currency collapse / hyperinflation",
    },
}

# 2. FACT REGISTRY
FACT_REGISTRY = {
    "B1": {
        "key": "sc1_bedel",
        "label": (
            "SC1 counter-evidence: Bitcoin returned -64.8% in 2022 — "
            "the worst inflation year since 1981 (Bedel Financial Advisors)"
        ),
    },
    "B2": {
        "key": "sc1_cpi",
        "label": (
            "SC1 context: US CPI peaked at 9.1% in June 2022 — "
            "largest year-over-year increase since November 1981 (Bedel Financial Advisors)"
        ),
    },
    "B3": {
        "key": "sc1_smales",
        "label": (
            "SC1 academic finding: cryptocurrencies are not a viable "
            "alternative to gold for inflation hedging (Smales 2024, Accounting & Finance)"
        ),
    },
    "B4": {
        "key": "sc2_venezuela",
        "label": (
            "SC2 partial context: Venezuelan citizens use crypto amid "
            "hyperinflation and currency collapse (AINFP)"
        ),
    },
    "A1": {
        "label": (
            "SC1 computation: count of verified counter-evidence sources "
            "for Bitcoin-as-inflation-hedge claim (any >=1 disproves 'proven')"
        ),
        "method": None,
        "result": None,
    },
    "A2": {
        "label": (
            "SC2 computation: count of verified support sources "
            "versus 'proven' threshold of 3"
        ),
        "method": None,
        "result": None,
    },
}

# 3. EMPIRICAL FACTS
empirical_facts = {
    "sc1_bedel": {
        "quote": (
            "bitcoin ended the year down an abysmal -64.8%, while gold ended the "
            "year relatively flat, down about -0.7%"
        ),
        "url": "https://www.bedelfinancial.com/inflation-hedge-in-2022-bitcoin-vs-gold",
        "source_name": "Bedel Financial Advisors — Inflation Hedge in 2022: Bitcoin vs. Gold",
    },
    "sc1_cpi": {
        "quote": (
            "By June, the 12-month CPI was up to 9.1%. "
            "This was the largest year-over-year increase since November 1981"
        ),
        "url": "https://www.bedelfinancial.com/inflation-hedge-in-2022-bitcoin-vs-gold",
        "source_name": (
            "Bedel Financial Advisors — Inflation Hedge in 2022: Bitcoin vs. Gold "
            "(CPI peak data)"
        ),
    },
    "sc1_smales": {
        "quote": (
            "cryptocurrencies do not currently offer investors a viable alternative "
            "to gold for hedging inflation"
        ),
        "url": "https://ideas.repec.org/a/bla/acctfi/v64y2024i2p1589-1611.html",
        "source_name": (
            "IDEAS/RepEC — Smales (2024), Accounting & Finance: "
            "Cryptocurrency as an alternative inflation hedge?"
        ),
    },
    "sc2_venezuela": {
        "quote": (
            "Annual inflation at 229% in May 2025 and the currency losing "
            "over 70% of its value since January"
        ),
        "url": "https://ainfp.org/how-venezuelans-use-crypto-amid-hyperinflation",
        "source_name": "AINFP — How Venezuelans Use Crypto Amid Hyperinflation",
    },
}

# 4. CITATION VERIFICATION (Rule 2)
citation_results = verify_all_citations(empirical_facts, wayback_fallback=True)

# 5. CLAIM EVALUATION

# SC1: count verified counter-evidence sources
# One verified source showing Bitcoin declined during high inflation disproves SC1.
sc1_counter_verified = sum(
    1 for k, v in citation_results.items()
    if k in ("sc1_bedel", "sc1_cpi", "sc1_smales")
    and v["status"] in ("verified", "partial")
)

# SC2: count verified support sources (threshold = 3 for "proven")
SC2_PROVEN_THRESHOLD = 3
sc2_support_verified = sum(
    1 for k, v in citation_results.items()
    if k == "sc2_venezuela"
    and v["status"] in ("verified", "partial")
)

# SC1 is "proven" only if there are zero verified counterexamples.
# The 2022 data establishes a direct counterexample: Bitcoin fell 65% while
# CPI inflation hit a 40-year high of 9.1%.
sc1_no_counterexample = compare(
    sc1_counter_verified,
    "==",
    0,
    label=(
        "SC1 (inflation hedge): zero verified counter-evidence sources "
        "(required for 'proven' status)"
    ),
)
# Expected result: False — counterexamples exist.

# SC2 "proven" requires >= 3 independent verified sources.
sc2_proven = compare(
    sc2_support_verified,
    ">=",
    SC2_PROVEN_THRESHOLD,
    label=(
        "SC2 (fiat collapse hedge): verified support sources >= "
        f"proven threshold of {SC2_PROVEN_THRESHOLD}"
    ),
)
# Expected result: False — only 1 source found, and it describes stablecoin use more than Bitcoin.

# Compound claim: both SC1 (no counterexample) AND SC2 (proven) must hold.
claim_holds = compare(
    int(sc1_no_counterexample) + int(sc2_proven),
    "==",
    2,
    label="Compound claim: SC1 (no counterexample) AND SC2 (proven) both hold",
)

# Sub-claim verdicts
sc1_verdict = "DISPROVED" if not sc1_no_counterexample else "PROVED"
sc2_verdict = "UNDETERMINED" if not sc2_proven else "PROVED"

# 6. ADVERSARIAL CHECKS (Rule 5)
adversarial_checks = [
    {
        "question": (
            "Does any academic study confirm Bitcoin as a reliable, "
            "consistent inflation hedge?"
        ),
        "verification_performed": (
            "Searched Google Scholar and PubMed Central for 'Bitcoin inflation hedge' "
            "peer-reviewed studies. Found Bouri et al. (2021) in Finance Research Letters "
            "(PMC/NCB PMC8995501) which concluded 'Bitcoin appreciates against inflation or "
            "inflation expectation shocks, confirming its inflation-hedging property claimed "
            "by investors.' Also reviewed MDPI Axioms 11/7/339 on high-adoption countries."
        ),
        "finding": (
            "Several studies using data primarily from 2010–2020 find some inflation-hedging "
            "signal in Bitcoin. However, Smales (2024) — using a longer, post-COVID series — "
            "finds the effect 'only significant for short-term inflation expectations' and "
            "'only when inflation or market-implied inflation expectations are below 2%,' "
            "meaning Bitcoin hedges inflation precisely when no hedge is needed. The 2022 "
            "real-world test invalidated earlier positive findings: Bitcoin fell 65% during "
            "the worst US inflation in 40 years."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Could Bitcoin's long-term appreciation (from <$1 in 2009 to >$10,000+) "
            "constitute an inflation hedge?"
        ),
        "verification_performed": (
            "Searched for 'Bitcoin long-term inflation-adjusted returns' and 'inflation hedge "
            "definition finance'. Reviewed academic definitions of an inflation hedge: an asset "
            "whose returns co-move positively with inflation, providing purchasing power "
            "protection during inflationary episodes."
        ),
        "finding": (
            "Long-term appreciation does not establish an asset as an inflation hedge in the "
            "financial-economics sense. A hedge must reliably co-move with inflation during "
            "inflationary episodes. Bitcoin's 2022 performance (down 65% during peak inflation) "
            "demonstrates that its long-run appreciation coexists with sharp declines during "
            "the very periods a hedge would be needed. High-volatility assets with strong "
            "long-run trends (e.g., equities, real estate) are not classified as inflation "
            "hedges for the same reason."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Does Bitcoin adoption in Argentina (276% inflation in 2024) support "
            "SC2 (fiat collapse hedge)?"
        ),
        "verification_performed": (
            "Searched 'Argentina Bitcoin crypto adoption hyperinflation 2024' and reviewed "
            "Chainalysis 2023 Geography of Cryptocurrency report. Found Argentina among top "
            "global crypto adopters during its 2024 inflation crisis."
        ),
        "finding": (
            "Argentina and Venezuela both show elevated crypto adoption during fiat crises. "
            "However, the dominant instruments are dollar-pegged stablecoins (USDT, USDC) "
            "rather than Bitcoin itself. In Venezuela, 'USDT' is the everyday transaction "
            "currency ('Binance dollars') while Bitcoin plays a secondary role. In Argentina, "
            "stablecoins dominate daily transactions. Bitcoin's own extreme volatility "
            "(capable of -50% in a single month) makes it a poor store of value during "
            "economic crises where price stability is paramount. This weakens the 'Bitcoin "
            "specifically' component of SC2."
        ),
        "breaks_proof": False,
    },
]

# 7. VERDICT AND STRUCTURED OUTPUT
if __name__ == "__main__":
    any_unverified = any(
        cr["status"] != "verified" for cr in citation_results.values()
    )

    if claim_holds and not any_unverified:
        verdict = "PROVED"
    elif claim_holds and any_unverified:
        verdict = "PROVED (with unverified citations)"
    elif not claim_holds and not any_unverified:
        verdict = "DISPROVED"
    elif not claim_holds and any_unverified:
        verdict = "DISPROVED (with unverified citations)"
    else:
        verdict = "UNDETERMINED"

    FACT_REGISTRY["A1"]["method"] = (
        "count verified SC1 counter-evidence sources in {sc1_bedel, sc1_cpi, sc1_smales}"
    )
    FACT_REGISTRY["A1"]["result"] = (
        f"{sc1_counter_verified} verified "
        f"(>= 1 needed to disprove 'proven' status for SC1)"
    )
    FACT_REGISTRY["A2"]["method"] = (
        f"count verified SC2 support sources vs threshold of {SC2_PROVEN_THRESHOLD}"
    )
    FACT_REGISTRY["A2"]["result"] = (
        f"{sc2_support_verified} verified "
        f"(< {SC2_PROVEN_THRESHOLD} = not proven for SC2)"
    )

    citation_detail = build_citation_detail(FACT_REGISTRY, citation_results, empirical_facts)

    extractions = {
        "B1": {
            "value": (
                "verified"
                if citation_results.get("sc1_bedel", {}).get("status") in ("verified", "partial")
                else "not_verified"
            ),
            "value_in_quote": (
                citation_results.get("sc1_bedel", {}).get("status") in ("verified", "partial")
            ),
            "quote_snippet": empirical_facts["sc1_bedel"]["quote"][:80],
        },
        "B2": {
            "value": (
                "verified"
                if citation_results.get("sc1_cpi", {}).get("status") in ("verified", "partial")
                else "not_verified"
            ),
            "value_in_quote": (
                citation_results.get("sc1_cpi", {}).get("status") in ("verified", "partial")
            ),
            "quote_snippet": empirical_facts["sc1_cpi"]["quote"][:80],
        },
        "B3": {
            "value": (
                "verified"
                if citation_results.get("sc1_smales", {}).get("status")
                in ("verified", "partial")
                else "not_verified"
            ),
            "value_in_quote": (
                citation_results.get("sc1_smales", {}).get("status") in ("verified", "partial")
            ),
            "quote_snippet": empirical_facts["sc1_smales"]["quote"][:80],
        },
        "B4": {
            "value": (
                "verified"
                if citation_results.get("sc2_venezuela", {}).get("status")
                in ("verified", "partial")
                else "not_verified"
            ),
            "value_in_quote": (
                citation_results.get("sc2_venezuela", {}).get("status")
                in ("verified", "partial")
            ),
            "quote_snippet": empirical_facts["sc2_venezuela"]["quote"][:80],
        },
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
                "description": (
                    "SC1 cross-check: real-world 2022 data (Bedel Financial) "
                    "independently corroborated by peer-reviewed academic consensus "
                    "(Smales 2024, Accounting & Finance)"
                ),
                "values_compared": [
                    "Bedel Financial (2022): Bitcoin -64.8% while CPI peaked at 9.1%",
                    "Smales (2024): cryptocurrencies not a viable gold alternative for hedging inflation",
                ],
                "agreement": True,
                "note": (
                    "Both independently confirm Bitcoin failed as an inflation hedge. "
                    "Sources are independent: one financial advisory (real-world data), "
                    "one peer-reviewed academic study (econometric analysis)."
                ),
            }
        ],
        "adversarial_checks": adversarial_checks,
        "verdict": verdict,
        "sub_claim_verdicts": {
            "SC1": sc1_verdict,
            "SC2": sc2_verdict,
        },
        "sub_claim_results": {
            "SC1": {
                "result": bool(sc1_no_counterexample),
                "counter_evidence_verified": sc1_counter_verified,
                "conclusion": (
                    "DISPROVED — verified counterexample: Bitcoin declined 64.8% in 2022 "
                    "while US CPI peaked at 9.1% (40-year high). Academic consensus "
                    "(Smales 2024) confirms Bitcoin is not a reliable inflation hedge."
                ),
            },
            "SC2": {
                "result": bool(sc2_proven),
                "support_verified": sc2_support_verified,
                "threshold": SC2_PROVEN_THRESHOLD,
                "conclusion": (
                    "UNDETERMINED — partial evidence: citizens in Venezuela and Argentina "
                    "do turn to crypto during fiat crises, but (a) stablecoins (USDT) are "
                    "the dominant instrument rather than Bitcoin, (b) Bitcoin's own extreme "
                    "volatility undermines its store-of-value role, and (c) the 'proven' "
                    "threshold of 3 independent verified sources was not reached."
                ),
            },
        },
        "key_results": {
            "sc1_counter_evidence_verified": sc1_counter_verified,
            "sc2_support_verified": sc2_support_verified,
            "sc2_proven_threshold": SC2_PROVEN_THRESHOLD,
            "sc1_verdict": sc1_verdict,
            "sc2_verdict": sc2_verdict,
            "claim_holds": claim_holds,
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
