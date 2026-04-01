# Audit: The body can only absorb 20-30 g of protein per meal; the rest is wasted.

- **Generated:** 2026-04-01
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Human protein absorption and utilization per meal |
| Property | Number of independent peer-reviewed sources establishing that (1) there is no fixed 20-30 g per-meal ceiling on protein absorption or utilization, AND (2) protein ingested above any such threshold is not simply 'wasted' (excreted unused) |
| Operator | >= |
| Threshold | 3 |
| Proof direction | disprove |
| Operator note | The claim makes two assertions: (A) a hard 20-30 g per-meal protein absorption ceiling exists, and (B) protein above that ceiling is wasted. Both are tested together: a source qualifies as a rebuttal if it establishes that protein utilization or anabolism continues beyond 20-30 g/meal, or that excess amino acids are metabolized for energy/other purposes rather than excreted unused. Proof direction is 'disprove' — sources must REJECT the claim. Threshold of 3 independent peer-reviewed sources is required. Note: studies showing that MPS rates plateau around 20 g of whey protein in the short-term post-exercise window do NOT support the claim as stated, because they measure synthesis rate optimization, not absorption capacity, and do not show that excess protein is excreted unused. |

*Source: proof.py JSON summary*

---

## Fact Registry

| Fact ID | Key | Label |
|---------|-----|-------|
| B1 | schoenfeld_aragon_2018 | Schoenfeld & Aragon 2018 (JISSN) — protein dose-response review |
| B2 | trommelen_2023 | Trommelen et al. 2023 (Cell Reports Medicine) — 100 g single-meal RCT |
| B3 | deutz_wolfe_2013 | Deutz & Wolfe 2013 (Clinical Nutrition) — anabolic upper limit review |
| A1 | *(computed)* | Verified source count (peer-reviewed sources rejecting the 20-30 g cap claim) |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Verified source count (peer-reviewed sources rejecting the 20-30 g cap claim) | count(verified citations) = 3 | 3 |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | Schoenfeld & Aragon 2018 (JISSN) — protein dose-response review | Schoenfeld BJ, Aragon AA. How much protein can the body use in a single meal for muscle-building? Implications for daily protein distribution. J Int Soc Sports Nutr. 2018;15(1):10. PMC5828430. | https://pmc.ncbi.nlm.nih.gov/articles/PMC5828430/ | "the preponderance of data indicate that while consumption of higher protein doses (> 20 g) results in greater AA oxidation, this is not the fate for all the additional ingested AAs as some are utilized for tissue-building purposes" | verified | full_quote | Tier 5 (government) |
| B2 | Trommelen et al. 2023 (Cell Reports Medicine) — 100 g single-meal RCT | Trommelen J et al. The anabolic response to protein ingestion during recovery from exercise has no upper limit in magnitude and duration in vivo in humans. Cell Rep Med. 2023;4(12):101324. PMC10772463. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10772463/ | "The anabolic response to protein ingestion has no apparent upper limit in magnitude and duration in vivo in humans" | verified | full_quote | Tier 5 (government) |
| B3 | Deutz & Wolfe 2013 (Clinical Nutrition) — anabolic upper limit review | Deutz NE, Wolfe RR. Is there a maximal anabolic response to protein intake with a meal? Clin Nutr. 2013;32(2):309-313. PMC3595342. | https://pmc.ncbi.nlm.nih.gov/articles/PMC3595342/ | "There is no practical upper limit to the anabolic response to protein or amino acid intake in the context of a meal" | verified | full_quote | Tier 5 (government) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — Schoenfeld & Aragon 2018**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B2 — Trommelen et al. 2023**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B3 — Deutz & Wolfe 2013**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

*Source: proof.py JSON summary*

---

## Computation Traces

```
  [✓] schoenfeld_aragon_2018: Full quote verified for schoenfeld_aragon_2018 (source: tier 5/government)
  [✓] trommelen_2023: Full quote verified for trommelen_2023 (source: tier 5/government)
  [✓] deutz_wolfe_2013: Full quote verified for deutz_wolfe_2013 (source: tier 5/government)
  Confirmed sources: 3 / 3
  SC: peer-reviewed sources rejecting the 20-30 g absorption cap claim: 3 >= 3 = True
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

| Description | Sources Consulted | Sources Verified | Agreement |
|-------------|-------------------|-----------------|-----------|
| Multiple independent peer-reviewed sources consulted | 3 | 3 | Yes (3/3) |

**Source verification statuses:**

| Key | Status |
|-----|--------|
| schoenfeld_aragon_2018 | verified |
| trommelen_2023 | verified |
| deutz_wolfe_2013 | verified |

**Independence note:** Sources are from different research groups and journals: Schoenfeld/Aragon (review, multiple US institutions, JISSN), Trommelen et al. (RCT, Maastricht University, Cell Reports Medicine), Deutz/Wolfe (review, Texas A&M/UT Medical Branch, Clinical Nutrition). All published in different peer-reviewed journals.

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

**Check 1:** Do peer-reviewed studies directly support a hard 20-30 g per-meal protein absorption ceiling?

- **Verification performed:** Searched PubMed and Google Scholar for "protein absorption 20g per meal limit," "protein meal size muscle protein synthesis ceiling," and "maximum protein per meal." Found Moore et al. 2009 (Am J Clin Nutr 89:161-168) showing MPS plateaus around 20 g of whey post-exercise, and Areta et al. 2013 (J Physiol 591:2319-2331) showing 20 g every 3 hours was optimal for MPS during a 12-hour recovery window.
- **Finding:** Moore et al. 2009 and Areta et al. 2013 showed that 20 g of whey protein optimized MUSCLE PROTEIN SYNTHESIS RATES in acute, tightly-controlled post-exercise windows. Neither study measures gut absorption capacity, and neither claims protein above 20 g is excreted unused. Moore et al. used fast-digesting isolated whey; mixed meals with slower proteins extend the utilization window. Neither study addresses the "wasted" claim. The Trommelen 2023 study (B2) directly tested 100 g in a single meal using isotope tracers and found protein incorporation into muscle continued for 12+ hours, refuting the ceiling interpretation.
- **Breaks proof:** No

**Check 2:** Does the ISSN position stand endorse a hard 20-40 g per meal limit that would support the claim?

- **Verification performed:** Searched for ISSN protein exercise position stand; reviewed Jager et al. 2017 (J Int Soc Sports Nutr, PMC5477153) and the ISSN nutrient timing position stand (Kerksick et al. 2017, PMC5596471).
- **Finding:** The ISSN position (Jager et al. 2017) frames 0.25 g/kg or 20-40 g per meal as a performance optimization recommendation for muscle protein synthesis. It does NOT claim protein above this amount is wasted or that intestinal absorption is capped. The recommendation is an ergogenic dosing target, not a physiological absorption limit.
- **Breaks proof:** No

**Check 3:** Is there a meaningful distinction between gut "absorption" and cellular "utilization" that could rescue any part of the claim?

- **Verification performed:** Searched "intestinal protein absorption capacity per meal physiology" and reviewed Boirie et al. 1997 (PNAS 94:14930) on fast vs slow proteins and Guadagni & Biolo 2009 (Curr Opin Clin Nutr Metab Care 12:58) on protein kinetics. Also reviewed the discussion section of Schoenfeld & Aragon 2018.
- **Finding:** Gut absorption of dietary protein is essentially complete (>90%) for all common protein sources regardless of meal size — the intestine does not have a 20-30 g ceiling. What studies sometimes show is that MUSCLE PROTEIN SYNTHESIS STIMULATION has diminishing returns above ~20 g of fast whey in certain contexts. However, Schoenfeld & Aragon 2018 explicitly state that additional AAs go to tissue-building beyond 20 g, and Deutz & Wolfe 2013 note that higher protein also suppresses protein breakdown (net anabolism continues). Any rescue of the claim via this distinction would require redefining "absorb" to mean "maximally stimulate MPS from whey in isolation" — which is not the plain meaning of the claim.
- **Breaks proof:** No

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central open-access archive |
| B2 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central open-access archive |
| B3 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central open-access archive |

All sources are Tier 5 (highest credibility). No low-credibility sources cited.

*Source: proof.py JSON summary*

---

## Extraction Records

For qualitative/consensus proofs, extraction records capture citation verification status per source rather than numeric values.

| Fact ID | Value (citation status) | Countable (verified or partial) | Quote snippet |
|---------|------------------------|--------------------------------|---------------|
| B1 | verified | Yes | "the preponderance of data indicate that while consumption of higher protein dose" |
| B2 | verified | Yes | "The anabolic response to protein ingestion has no apparent upper limit in magnit" |
| B3 | verified | Yes | "There is no practical upper limit to the anabolic response to protein or amino a" |

*Source: proof.py JSON summary*

---

## Hardening Checklist

- **Rule 1 (No hand-typed values):** N/A — qualitative consensus proof; no numeric value extraction from quotes.
- **Rule 2 (Citations verified by fetching):** ✓ `verify_all_citations()` called; all 3 citations verified live (full_quote, live fetch).
- **Rule 3 (System time anchoring):** N/A — no date-dependent computation in this proof.
- **Rule 4 (Explicit claim interpretation):** ✓ `CLAIM_FORMAL` dict present with `operator_note` explaining both sub-claims, operator choice, threshold, and proof direction.
- **Rule 5 (Adversarial checks):** ✓ Three adversarial checks performed via web search; Moore et al. 2009 and Areta et al. 2013 (the studies most commonly cited to support the claim) evaluated and rebutted; ISSN position stand assessed; absorption/utilization distinction examined.
- **Rule 6 (Independent cross-checks):** ✓ 3 sources from different research groups, institutions, and journals verified independently.
- **Rule 7 (No hard-coded constants):** N/A — no numeric constants or formulas used.
- **validate_proof.py result:** PASS (15/15 checks, 0 issues, 0 warnings)

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
