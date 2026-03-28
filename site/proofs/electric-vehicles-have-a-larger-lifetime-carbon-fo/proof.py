"""
Proof: Electric vehicles have a larger lifetime carbon footprint than gasoline cars
when manufacturing and battery disposal are included.
Generated: 2026-03-28
"""
import json
import sys
import re

PROOF_ENGINE_ROOT = "/Users/yaniv/Documents/code/proof-engine/proof-engine/skills/proof-engine"
sys.path.insert(0, PROOF_ENGINE_ROOT)

from scripts.smart_extract import normalize_unicode, verify_extraction
from scripts.verify_citations import verify_all_citations, build_citation_detail
from scripts.computations import compare, explain_calc, cross_check
from scripts.extract_values import parse_number_from_quote

# ── 1. CLAIM INTERPRETATION (Rule 4) ─────────────────────────────────────────

CLAIM_NATURAL = (
    "Electric vehicles have a larger lifetime carbon footprint than gasoline cars "
    "when manufacturing and battery disposal are included."
)
CLAIM_FORMAL = {
    "subject": "Battery electric vehicles (BEVs) vs. internal combustion engine vehicles (ICEVs)",
    "property": (
        "Total cradle-to-grave lifecycle greenhouse gas (GHG) emissions in CO2-equivalent (CO2e), "
        "covering: vehicle manufacturing (including battery production), upstream energy "
        "(electricity/fuel supply chain), vehicle operation, and end-of-life (battery disposal/recycling)"
    ),
    "operator": ">",
    "operator_note": (
        "The claim asserts BEV total lifetime CO2e > ICEV total lifetime CO2e. "
        "This is a strict inequality evaluated on the global/US average case. "
        "Cradle-to-grave lifecycle analysis is the standard methodology for comparing vehicle "
        "lifetime emissions — it includes ALL phases: manufacturing (including battery production), "
        "upstream fuel/electricity, vehicle operation, and end-of-life. "
        "The claim is DISPROVED if multiple authoritative lifecycle analyses show BEV total < ICEV total "
        "even after manufacturing and battery disposal are included. "
        "The claim's PREMISE (that EVs have higher manufacturing emissions) is evaluated as TRUE; "
        "but the CONCLUSION (that this makes EVs' total lifetime footprint larger) is what we test here. "
        "Regional edge cases (coal-heavy grids) are examined in adversarial checks."
    ),
    "threshold": "ICEV total lifetime CO2e (the claim asserts BEV exceeds this)",
}

# ── 2. FACT REGISTRY ──────────────────────────────────────────────────────────

FACT_REGISTRY = {
    "B1": {
        "key": "source_doe_gas",
        "label": "DOE FOTW #1303 (2023): Gasoline SUV cradle-to-grave = 429 g CO2e per mile",
    },
    "B2": {
        "key": "source_doe_ev",
        "label": "DOE FOTW #1303 (2023): Battery EV emits 48% fewer GHGs than gasoline SUV (same cradle-to-grave scope)",
    },
    "B3": {
        "key": "source_iea",
        "label": "IEA Global EV Outlook 2024: BEV lifetime emissions are half of equivalent ICEV globally",
    },
    "B4": {
        "key": "source_recurrent_mfg",
        "label": "Recurrent Auto (citing multiple LCA studies): EV manufacturing >10 t CO2 vs gas car manufacturing ~6 t CO2",
    },
    "A1": {
        "label": "BEV-to-ICEV per-mile emissions ratio derived from DOE data",
        "method": "explain_calc: 1 - ev_reduction_pct / 100",
        "result": None,
    },
    "A2": {
        "label": "Cross-check: DOE per-mile ratio vs IEA 'half as much' ratio",
        "method": "cross_check(doe_ratio, iea_ratio, tolerance=0.05, mode='absolute')",
        "result": None,
    },
    "A3": {
        "label": "EV manufacturing CO2 premium over gasoline car manufacturing (metric tons)",
        "method": "explain_calc: ev_mfg_lower_bound - gas_mfg_tons",
        "result": None,
    },
}

# ── 3. EMPIRICAL FACTS ────────────────────────────────────────────────────────

empirical_facts = {
    # DOE FOTW #1303: gasoline lifecycle emissions per mile
    "source_doe_gas": {
        "quote": (
            "Cradle-to-grave greenhouse gas (GHG) emissions for a small gasoline SUV in 2020 "
            "were estimated to be 429 grams of carbon dioxide equivalent (CO2e) per mile"
        ),
        "url": "https://www.energy.gov/eere/vehicles/articles/fotw-1303-august-14-2023-cradle-grave-electric-vehicles-have-fewer",
        "source_name": "U.S. Department of Energy — FOTW #1303 (August 14, 2023)",
    },
    # DOE FOTW #1303: EV percentage reduction vs gasoline (same cradle-to-grave scope)
    "source_doe_ev": {
        "quote": "the same size EV with 300 miles of range had 48% fewer GHG emissions",
        "url": "https://www.energy.gov/eere/vehicles/articles/fotw-1303-august-14-2023-cradle-grave-electric-vehicles-have-fewer",
        "source_name": "U.S. Department of Energy — FOTW #1303 (August 14, 2023)",
    },
    # IEA Global EV Outlook 2024: global lifetime comparison
    "source_iea": {
        "quote": "A battery electric car sold in 2023 will emit half as much as conventional equivalents over its lifetime",
        "url": "https://www.iea.org/reports/global-ev-outlook-2024/outlook-for-emissions-reductions",
        "source_name": "International Energy Agency — Global EV Outlook 2024",
    },
    # Recurrent Auto (aggregating ICCT, MIT, Argonne, and DOE LCA studies): manufacturing phase
    "source_recurrent_mfg": {
        "quote": (
            "Manufacturing an average gas powered sedan creates about six metric tons of carbon dioxide "
            "emissions, but manufacturing an electric vehicle of the same size creates more than "
            "10 metric tons of carbon dioxide emissions"
        ),
        "url": "https://www.recurrentauto.com/research/just-how-dirty-is-your-ev",
        "source_name": "Recurrent Auto — Carbon Footprint Face-Off: A Full Picture of EVs vs. Gas Cars",
    },
}

# ── 4. CITATION VERIFICATION (Rule 2) ────────────────────────────────────────

print("\n=== Citation Verification ===")
citation_results = verify_all_citations(empirical_facts, wayback_fallback=True)

# ── 5. VALUE EXTRACTION (Rule 1) ─────────────────────────────────────────────

print("\n=== Value Extraction ===")

# B1: extract gasoline per-mile emissions (429 from DOE)
gas_grams_per_mile = float(parse_number_from_quote(
    empirical_facts["source_doe_gas"]["quote"],
    r"(\d+) grams of carbon dioxide equivalent",
    "B1"
))
verify_extraction(gas_grams_per_mile, empirical_facts["source_doe_gas"]["quote"], "B1_gas_grams_per_mile")
print(f"B1 gas per-mile: {gas_grams_per_mile} g CO2e/mile")

# B2: extract EV reduction percentage (48 from DOE)
ev_reduction_pct = float(parse_number_from_quote(
    empirical_facts["source_doe_ev"]["quote"],
    r"(\d+)%",
    "B2"
))
verify_extraction(ev_reduction_pct, empirical_facts["source_doe_ev"]["quote"], "B2_ev_reduction_pct")
print(f"B2 EV reduction: {ev_reduction_pct}% fewer GHG emissions than gasoline (cradle-to-grave)")

# B4: extract manufacturing tons (gas: "six" = word-form; EV: "10" = numeral)
# "six" is word-form — use a custom extraction
def extract_gas_mfg_tons(quote):
    """Extract gas manufacturing CO2 from Recurrent quote (word-form number 'six')."""
    normalized = normalize_unicode(quote)
    match = re.search(r"about (six) metric tons", normalized, re.IGNORECASE)
    if match:
        word_to_num = {"six": 6}
        return float(word_to_num[match.group(1).lower()])
    raise ValueError(f"Could not extract gas manufacturing tons from: {quote}")

gas_mfg_tons = extract_gas_mfg_tons(empirical_facts["source_recurrent_mfg"]["quote"])
# verify_extraction not applicable here: value is word-form ("six") not a numeral in the quote.
# The custom extraction function itself verifies the word "six" appears via regex match.
# Confirm the source word is present:
assert "six" in normalize_unicode(empirical_facts["source_recurrent_mfg"]["quote"]).lower(), \
    "Word 'six' not found in B4 quote — extraction basis missing"
print(f"B4 gas manufacturing: {gas_mfg_tons} metric tons CO2 (extracted from word-form 'six' in quote)")

ev_mfg_lower_bound = float(parse_number_from_quote(
    empirical_facts["source_recurrent_mfg"]["quote"],
    r"more than (\d+) metric tons",
    "B4_ev"
))
verify_extraction(ev_mfg_lower_bound, empirical_facts["source_recurrent_mfg"]["quote"], "B4_ev_mfg_lower_bound")
print(f"B4 EV manufacturing: more than {ev_mfg_lower_bound} metric tons CO2")

# B3: IEA "half as much" → ratio = 0.50 (qualitative; extract the fraction)
iea_ratio = 0.50  # "half as much" = 50% of ICEV; not a numeric pattern to extract
print(f"B3 IEA ratio: {iea_ratio} (BEV = half of ICEV over lifetime)")

# ── 6. COMPUTATIONS (Rule 7) ──────────────────────────────────────────────────

print("\n=== Computations ===")

# A1: BEV-to-ICEV per-mile ratio from DOE data
doe_ratio = explain_calc(
    "1 - ev_reduction_pct / 100",
    locals(),
    label="A1: BEV/ICEV lifetime emissions ratio (DOE cradle-to-grave per-mile)"
)
FACT_REGISTRY["A1"]["result"] = doe_ratio

# A3: EV manufacturing premium over gas manufacturing
mfg_premium = explain_calc(
    "ev_mfg_lower_bound - gas_mfg_tons",
    locals(),
    label="A3: EV manufacturing CO2 premium over gas car (metric tons, lower bound)"
)
FACT_REGISTRY["A3"]["result"] = mfg_premium

# ── 7. CROSS-CHECK (Rule 6) ───────────────────────────────────────────────────

print("\n=== Cross-Check (Rule 6) ===")
# DOE (per-mile, cradle-to-grave) → BEV/ICEV ratio = 0.52
# IEA (lifetime, cradle-to-grave) → BEV/ICEV ratio = 0.50
# These come from independent organizations using independent data.
# Tolerance 0.05 (5 percentage points) to allow for different grid mixes and vehicle size assumptions.
cross_check_passed = cross_check(
    doe_ratio,
    iea_ratio,
    tolerance=0.05,
    mode="absolute",
    label="A2: DOE per-mile ratio vs IEA lifetime ratio (BEV/ICEV)"
)
FACT_REGISTRY["A2"]["result"] = cross_check_passed
print(f"A2 cross-check passed: {cross_check_passed}")

# ── 8. CLAIM EVALUATION ───────────────────────────────────────────────────────

print("\n=== Claim Evaluation ===")
# The claim asserts: BEV lifetime CO2e > ICEV lifetime CO2e
# This holds only if BEV/ICEV ratio > 1.0
# Both DOE (0.52) and IEA (0.50) show BEV/ICEV ratio << 1.0 → claim is FALSE

claim_holds = compare(
    doe_ratio,
    ">",
    1.0,
    label="Claim check: BEV/ICEV lifetime ratio > 1.0 (claim holds only if TRUE)"
)
print(f"\nClaim holds: {claim_holds}")
print(f"BEV/ICEV ratio (DOE): {doe_ratio:.2f} — EVs emit {(1-doe_ratio)*100:.0f}% LESS than gasoline cars lifetime")
print(f"BEV/ICEV ratio (IEA): {iea_ratio:.2f} — EVs emit {(1-iea_ratio)*100:.0f}% LESS than gasoline cars lifetime")
print(f"EV manufacturing premium: >{mfg_premium:.0f} metric tons CO2 (higher than gas, but offset by operational savings)")

# ── 9. ADVERSARIAL CHECKS (Rule 5) ───────────────────────────────────────────

adversarial_checks = [
    {
        "question": (
            "Is there any scenario (e.g., coal-heavy electricity grid) where EV lifetime emissions "
            "exceed those of gasoline cars?"
        ),
        "verification_performed": (
            "Searched 'electric vehicles larger carbon footprint coal grid lifetime analysis 2023 2024'. "
            "Reviewed IEA Global EV Outlook 2024 regional breakdown. "
            "Found: IEA reports that even in India (highest coal-heavy scenario analyzed), "
            "BEVs still save 'less than 10 tonnes of CO2-eq over lifetime compared to an ICE medium-sized car' — "
            "meaning BEVs are still LOWER than ICE even in the most coal-intensive major economy studied. "
            "MIT Climate Portal confirms: even coal-grid EVs have 'fuel economy equivalent of about 50 to 60 mpg' "
            "and 'the dirtiest electric vehicle looks something like our best gasoline vehicles today' — "
            "matching or exceeding ICE efficiency, not worse."
        ),
        "finding": (
            "No authoritative source documents a scenario where EV total lifetime CO2e exceeds equivalent ICE "
            "vehicle — not even on coal-heavy grids. The IEA reports EVs are better (though by smaller margins) "
            "in every major electricity market studied globally."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Does battery disposal (end-of-life) increase EV emissions enough to flip the verdict?"
        ),
        "verification_performed": (
            "Searched 'EV battery disposal recycling lifecycle CO2 emissions end of life'. "
            "Reviewed PMC peer-reviewed study (PMC9171403) on BEV lifecycle assessment. "
            "Found: battery end-of-life recycling REDUCES BEV climate impact by approximately 8.3% "
            "(PMC9171403: 'Recycling reduced the BEV climate impacts by approximately 8.3%'). "
            "DOE cradle-to-grave scope explicitly includes 'vehicle end-of-life' and still shows "
            "EVs 48% better. "
            "Battery disposal/recycling does not increase total emissions — it decreases them."
        ),
        "finding": (
            "Battery disposal does not flip the verdict. The cradle-to-grave analyses (DOE, IEA) already "
            "include end-of-life phase, and recycling reduces — not increases — EV lifetime emissions. "
            "The premise in the claim (that battery disposal worsens EV footprint) is contradicted by evidence."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "Do studies funded by fossil fuel interests reach different conclusions? "
            "Is there credible peer-reviewed counter-evidence?"
        ),
        "verification_performed": (
            "Searched 'peer reviewed study electric vehicles worse lifetime carbon footprint gasoline 2023 2024'. "
            "Searched 'EV lifecycle emissions higher than ICE study'. "
            "Found: Institute for Energy Research (IER) and similar fossil-fuel-affiliated organizations "
            "publish skeptical claims about EV emissions. However, IER's arguments focus on manufacturing "
            "phase in isolation — they do not produce cradle-to-grave lifecycle analyses showing total EV > "
            "total ICE. No peer-reviewed study in major journals (Nature, Environmental Science & Technology, "
            "Science) found EVs to have higher total lifetime emissions than equivalent gasoline cars in "
            "any mainstream scenario. The European Parliament commissioned independent LCA found >60% CO2 "
            "savings for BEVs in EU conditions."
        ),
        "finding": (
            "No credible peer-reviewed counter-evidence found. Industry-funded skepticism focuses on the "
            "manufacturing phase in isolation, not the full lifecycle. Total-lifecycle studies consistently "
            "show EVs lower across all major peer-reviewed venues."
        ),
        "breaks_proof": False,
    },
    {
        "question": (
            "What if the vehicle lifetime is very short (e.g., 3 years), before operational savings "
            "offset the manufacturing premium?"
        ),
        "verification_performed": (
            "Searched 'EV break-even point carbon emissions manufacturing years'. "
            "Found: multiple sources (Recurrent Auto, MIT, IEA) place the break-even at 1-2 years of "
            "average driving, after which the EV has lower cumulative lifetime emissions than a gasoline car. "
            "The vast majority of vehicles are kept for 10-15 years, far exceeding the break-even."
        ),
        "finding": (
            "Even at a very short vehicle lifetime (3 years), the break-even occurs at 1-2 years. "
            "The claim uses no qualifier like 'in the first two years' — as a statement about full vehicle "
            "lifetime, it is DISPROVED. Only if a vehicle were scrapped within its first ~1-2 years of "
            "operation could the manufacturing premium not be offset."
        ),
        "breaks_proof": False,
    },
]

# ── 10. BUILD CITATION DETAILS ────────────────────────────────────────────────

citation_detail = build_citation_detail(FACT_REGISTRY, citation_results, empirical_facts)

# ── 11. VERDICT AND STRUCTURED OUTPUT ─────────────────────────────────────────

if __name__ == "__main__":
    any_unverified = any(
        cr["status"] not in ("verified", "partial")
        for cr in citation_results.values()
    )

    # The claim (BEV > ICEV) is FALSE → DISPROVED
    if not claim_holds and not any_unverified:
        verdict = "DISPROVED"
    elif not claim_holds and any_unverified:
        verdict = "DISPROVED (with unverified citations)"
    else:
        verdict = "UNDETERMINED"  # fallback if data unexpectedly supports claim

    key_results = [
        f"DOE cradle-to-grave analysis: gasoline SUV = {gas_grams_per_mile:.0f} g CO2e/mile; "
        f"equivalent EV = {gas_grams_per_mile * doe_ratio:.0f} g CO2e/mile — EV is {(1-doe_ratio)*100:.0f}% LOWER (B1, B2)",
        f"IEA Global EV Outlook 2024: BEV lifetime emissions = {iea_ratio*100:.0f}% of equivalent ICEV — "
        f"EVs emit {(1-iea_ratio)*100:.0f}% LESS over lifetime globally (B3)",
        f"EV manufacturing does emit >{mfg_premium:.0f} metric tons CO2 more than gasoline car manufacturing "
        f"(>{ev_mfg_lower_bound:.0f} vs ~{gas_mfg_tons:.0f} t CO2) — but this is overwhelmed by operational savings (B4)",
        f"Battery disposal included in cradle-to-grave scope; recycling REDUCES EV emissions by ~8.3% — "
        f"battery disposal does not worsen the EV footprint",
        f"Cross-check: DOE ratio ({doe_ratio:.2f}) and IEA ratio ({iea_ratio:.2f}) agree within "
        f"{abs(doe_ratio - iea_ratio)*100:.1f} percentage points from independent sources (A2)",
    ]

    summary = {
        "claim_natural": CLAIM_NATURAL,
        "claim_formal": CLAIM_FORMAL,
        "verdict": verdict,
        "key_results": key_results,
        "fact_registry": FACT_REGISTRY,
        "citations": citation_detail,
        "cross_checks": [
            {
                "label": "A2: DOE per-mile ratio vs IEA lifetime ratio (BEV/ICEV)",
                "value_a": {"source": "DOE FOTW #1303", "value": doe_ratio, "method": "1 - 0.48"},
                "value_b": {"source": "IEA Global EV Outlook 2024", "value": iea_ratio, "method": "BEV = half of ICEV → 0.50"},
                "tolerance": 0.05,
                "mode": "absolute",
                "passed": cross_check_passed,
                "note": "Independent organizations, independent methodologies, consistent finding",
            }
        ],
        "adversarial_checks": adversarial_checks,
        "generator": {
            "name": "proof-engine",
            "version": "1.0.0",
            "repo": "https://github.com/yaniv-golan/proof-engine",
            "generated_at": "2026-03-28",
        },
    }

    print("\n\n=== PROOF SUMMARY (JSON) ===")
    print(json.dumps(summary, indent=2, default=str))
