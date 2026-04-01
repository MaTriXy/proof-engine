# Audit: Multivitamins and most supplements provide meaningful health benefits for the general healthy population.

- **Generated:** 2026-03-31
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | multivitamins and most dietary supplements |
| Property | provide meaningful (clinically significant) health benefits to the general healthy adult population |
| Operator | >= |
| Threshold | 3 |
| Proof direction | disprove |
| Operator note | This proof uses a disproof strategy: we gather authoritative sources that REJECT the claim and require at least 3 independently verified sources to establish disproof. 'Meaningful health benefits' is interpreted as clinically significant improvements in primary outcomes — all-cause mortality, cardiovascular disease, or cancer incidence — for community-dwelling adults without nutritional deficiencies or known medical conditions. This conservative scope excludes populations with known deficiencies, pregnant persons, elderly with specific risks, or those under medical supervision. Threshold = 3: the claim is disproved if at least 3 independent authoritative sources confirm the claim is false. All 4 sources here confirm the same direction. |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_uspstf_rec | USPSTF 2022 Recommendation: Grade D (recommend against) for beta-carotene and vitamin E supplements in healthy adults |
| B2 | source_ncbi_review | NCBI Bookshelf — USPSTF Systematic Evidence Review 2022: vitamin/mineral supplementation provides little to no benefit in preventing cancer, CVD, and death |
| B3 | source_nih_ods | NIH Office of Dietary Supplements Fact Sheet: MVMs do not reliably reduce risk of chronic diseases |
| B4 | source_annals_2019 | Annals of Internal Medicine 2019 umbrella meta-analysis: dietary supplements not associated with mortality benefits in U.S. adults |
| A1 | — | Verified source count — independent sources confirming the claim is false |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Verified source count — independent sources confirming the claim is false | count(verified citations) = 4 | 4 independent sources confirm the claim is false (threshold: 3) |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | USPSTF 2022 Recommendation: Grade D for beta-carotene and vitamin E | U.S. Preventive Services Task Force (USPSTF) — 2022 Recommendation Statement | https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vitamin-supplementation-to-prevent-cvd-and-cancer-preventive-medication | "The USPSTF recommends against the use of beta carotene or vitamin E supplements for the prevention of cardiovascular disease or cancer." | verified | full_quote | Tier 2 (unknown) — see credibility note |
| B2 | USPSTF Systematic Evidence Review 2022: little to no benefit | NCBI Bookshelf — USPSTF Systematic Evidence Review 2022 (Lam et al., AHRQ) | https://www.ncbi.nlm.nih.gov/books/NBK581642/ | "Vitamin and mineral supplementation provides little to no benefit in preventing cancer, CVD, and death, with the exception of a possible small benefit for cancer incidence with multivitamin use" | verified | full_quote | Tier 5 (government) |
| B3 | NIH ODS: MVMs do not reliably reduce chronic disease risk | NIH Office of Dietary Supplements — Multivitamin/Mineral Supplements: Health Professional Fact Sheet | https://ods.od.nih.gov/factsheets/MVMS-HealthProfessional/ | "Overall, MVMs do not appear to reliably reduce the risk of chronic diseases when people choose to take these products for up to a decade (or more)." | verified | fragment (81.5%) | Tier 5 (government) |
| B4 | Annals of Internal Medicine 2019: supplements not associated with mortality benefits | Annals of Internal Medicine 2019 — Umbrella meta-analysis (Jenkins et al., PMID 30959527) | https://pubmed.ncbi.nlm.nih.gov/30959527/ | "Use of dietary supplements is not associated with mortality benefits among U.S. adults." | verified | full_quote | Tier 5 (government) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — USPSTF 2022 Recommendation Page**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote matched)

**B2 — NCBI Bookshelf (USPSTF Evidence Review 2022)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote matched)

**B3 — NIH Office of Dietary Supplements**
- Status: verified
- Method: fragment
- Fetch mode: live
- Coverage: 81.5% (≥80% threshold for verified; parenthetical "(or more)" varies between page versions)

**B4 — PubMed / Annals of Internal Medicine 2019**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote matched)

*Source: proof.py JSON summary*

---

## Computation Traces

```
  [✓] source_uspstf_rec: Full quote verified for source_uspstf_rec (source: tier 2/unknown)
  [✓] source_ncbi_review: Full quote verified for source_ncbi_review (source: tier 5/government)
  [✓] source_nih_ods: Quote largely verified (22/27 words matched) for source_nih_ods (source: tier 5/government)
  [✓] source_annals_2019: Full quote verified for source_annals_2019 (source: tier 5/government)
  Confirmed sources (disproof direction): 4 / 4
  verified disproof source count vs threshold (>= 3 required): 4 >= 3 = True
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

| Property | Value |
|----------|-------|
| Sources consulted | 4 |
| Sources verified | 4 |
| source_uspstf_rec | verified |
| source_ncbi_review | verified |
| source_nih_ods | verified |
| source_annals_2019 | verified |

**Independence rationale:** Sources are from distinct institutions:
1. **USPSTF** — independent federal advisory body (congressionally authorized); conducts its own systematic reviews and issues graded recommendations.
2. **NCBI Bookshelf (AHRQ)** — the systematic evidence review was commissioned by the Agency for Healthcare Research and Quality and authored by an independent academic team (Lam et al.). It is the USPSTF's evidentiary basis but is an independently authored document.
3. **NIH Office of Dietary Supplements** — synthesizes evidence from NIH-funded and independent RCTs separately from USPSTF processes.
4. **Annals of Internal Medicine 2019** — peer-reviewed umbrella meta-analysis by an independent academic team (Jenkins et al.) at Tufts University, published before the 2022 USPSTF review, drawing on a different body of literature.

Each source independently reviewed different sets of underlying RCTs and observational studies. None is simply republishing another source's conclusions.

*Source: proof.py JSON summary; independence narrative is author analysis*

---

## Adversarial Checks (Rule 5)

**Check 1: COSMOS-Mind cognitive benefit signal**
- Question: Do large RCTs show cognitive benefits of multivitamins that constitute 'meaningful benefits' for the general healthy population?
- Verification performed: Searched for 'COSMOS trial multivitamin cognitive benefit 2022 2023'. Found COSMOS-Mind (Baker et al., AJCN 2023): modest cognitive improvement over 2 years in adults aged 60+ (mean age ~72). Effect size ~0.1 SD. USPSTF reviewed this trial in their 2022 evidence synthesis and still issued Grade I (insufficient evidence) for multivitamins.
- Finding: A modest cognitive signal exists in COSMOS-Mind, but only in older adults (mean age ~72), not the general healthy adult population. The effect size (0.1 SD) is small. The USPSTF reviewed this evidence and concluded insufficient evidence to recommend multivitamins. Does not constitute 'meaningful benefit' for the general healthy population and does not break the disproof.
- Breaks proof: **No**

**Check 2: Cancer-incidence signal for multivitamins**
- Question: Is there any positive cancer-incidence signal for multivitamins that would support 'meaningful benefits'?
- Verification performed: Searched for 'multivitamin cancer prevention RCT meta-analysis benefit 2020 2021 2022'. The NCBI Bookshelf evidence review notes 'a possible small benefit for cancer incidence with multivitamin use' from one trial, but characterizes it as having 'important limitations, including only three adequately powered trials.' USPSTF issued Grade I (insufficient evidence), not a positive recommendation.
- Finding: One meta-analysis suggested a marginal cancer-incidence signal for multivitamins. This was reviewed by USPSTF, which issued Grade I (insufficient evidence), meaning harms and benefits could not be balanced. Any marginal benefit is offset by evidence of harm from specific supplements (beta-carotene, vitamin E — both Grade D). Does not constitute 'meaningful benefit' for most supplements and does not break disproof.
- Breaks proof: **No**

**Check 3: Omega-3 and popular supplements**
- Question: Does omega-3 or fish oil supplementation provide meaningful cardiovascular benefits for healthy adults, suggesting 'most supplements' do provide benefit?
- Verification performed: Searched for 'omega-3 fish oil supplements healthy adults cardiovascular benefit VITAL 2019'. The VITAL trial (Manson et al., NEJM 2019) — 25,871 healthy adults, no prior heart disease — found that omega-3 fatty acid supplements did not significantly reduce major cardiovascular events versus placebo (HR 0.92, 95% CI 0.80–1.05). AHA updated guidance in 2017 moved omega-3 supplements from a Class I to Class IIb recommendation.
- Finding: The largest high-quality RCT (VITAL) found omega-3 did not significantly reduce CVD events in the general healthy population without prior heart disease. This reinforces that even omega-3 — one of the most popular supplements — does not meet the bar for 'meaningful benefits' in the general healthy population. Does not break disproof.
- Breaks proof: **No**

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | uspreventiveservicestaskforce.org | unknown | 2 | Unclassified domain — automated scorer does not recognize non-.gov government advisory sites. The USPSTF is a congressionally authorized, independent federal advisory body; its recommendations are published in *JAMA* and referenced by all major U.S. health agencies. Low tier reflects a classifier gap, not an authority concern. |
| B2 | nih.gov | government | 5 | Government domain (.gov) |
| B3 | nih.gov | government | 5 | Government domain (.gov) |
| B4 | nih.gov | government | 5 | Government domain (.gov) — PubMed is the NLM/NIH abstract database |

**Note:** 1 citation (B1) received tier 2 (unclassified) from the automated credibility scorer. This is due to a domain classification gap: USPSTF operates at uspreventiveservicestaskforce.org rather than a .gov subdomain. The USPSTF's authority is independently established; its 2022 recommendation was published in *JAMA* (PMID 35727271) and is the standard of care reference for vitamin supplementation in the United States. The disproof does not depend solely on B1 — the claim is also disproved by B2, B3, and B4 alone (3 ≥ 3 threshold).

*Source: proof.py JSON summary; credibility note is author analysis*

---

## Extraction Records

For qualitative proofs, each B-type fact records citation verification status rather than a numeric extracted value.

| Fact ID | Value (citation status) | Countable? | Quote snippet |
|---------|------------------------|------------|---------------|
| B1 | verified | Yes | "The USPSTF recommends against the use of beta carotene or vitamin E supplements " |
| B2 | verified | Yes | "Vitamin and mineral supplementation provides little to no benefit in preventing " |
| B3 | verified | Yes | "Overall, MVMs do not appear to reliably reduce the risk of chronic diseases when" |
| B4 | verified | Yes | "Use of dietary supplements is not associated with mortality benefits among U.S. " |

*Source: proof.py JSON summary*

---

## Hardening Checklist

- **Rule 1 (No hand-typed values):** N/A — qualitative proof; no numeric values extracted from quotes. Auto-pass confirmed by validator.
- **Rule 2 (Citations verified by fetching):** PASS — `verify_all_citations()` called; all 4 citations fetched live and confirmed present on source pages.
- **Rule 3 (Anchored to system time):** N/A — no time-dependent computation. Proof generation date recorded in `generator.generated_at` via `date.today()`.
- **Rule 4 (Explicit claim interpretation):** PASS — `CLAIM_FORMAL` dict present with `operator_note` documenting the disproof strategy, "meaningful benefits" definition, population scope, and threshold rationale.
- **Rule 5 (Adversarial checks):** PASS — 3 independent adversarial searches performed: COSMOS-Mind cognitive signal, cancer-incidence signal, and omega-3 CVD evidence. None breaks the disproof.
- **Rule 6 (Independent cross-checks):** PASS — 4 sources from distinct institutions (USPSTF, AHRQ/NCBI, NIH ODS, Annals umbrella meta-analysis) independently reviewed different bodies of evidence.
- **Rule 7 (No hard-coded constants):** N/A — no numeric constants or formulas. `compare()` imported from `computations.py`. Auto-pass confirmed by validator.
- **validate_proof.py result:** PASS — 15/15 checks passed, 0 issues, 0 warnings.

*Source: validate_proof.py output (author analysis for N/A items)*

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-03-31.*
