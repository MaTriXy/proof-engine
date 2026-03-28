# Audit: Intermittent fasting is scientifically proven superior to other diets for fat loss and longevity.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Intermittent fasting |
| Compound operator | AND |
| Proof direction | disprove |
| SC1 property | scientifically proven superior to other diets for fat loss |
| SC1 operator | >= |
| SC1 threshold | 2 |
| SC2 property | scientifically proven superior to other diets for longevity in humans |
| SC2 operator | >= |
| SC2 threshold | 2 |
| Operator note | The original claim asserts BOTH (a) proven fat loss superiority AND (b) proven longevity superiority. An AND claim is false if either conjunct is false. This proof shows both conjuncts fail. proof_direction='disprove': empirical_facts sources REJECT each sub-claim; claim_holds=True triggers verdict DISPROVED (not PROVED). |

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_source_a | SC1-A: Systematic review & meta-analysis of IF vs. caloric restriction (PMC11930668, 2025) — weight loss difference not statistically significant |
| B2 | sc1_source_b | SC1-B: Meta-analysis of IF vs. caloric restriction in humans (PMC9108547, 2022) — IF outcomes did not differ from CR |
| B3 | sc2_source_a | SC2-A: Review of IF health benefits (PMC11262566, 2024) — human longevity studies are short-duration with high variability |
| B4 | sc2_source_b | SC2-B: American Heart Association newsroom, 2024 — time-restricted eating not associated with living longer |
| A1 | — | SC1: count of verified rejection sources for fat loss superiority |
| A2 | — | SC2: count of verified rejection sources for longevity superiority |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1: count of verified rejection sources for fat loss superiority | count(verified SC1 rejection sources) = 2 | 2 |
| A2 | SC2: count of verified rejection sources for longevity superiority | count(verified SC2 rejection sources) = 2 | 2 |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1-A | Evaluation of the effectiveness of intermittent fasting versus caloric restriction in weight loss and improving cardiometabolic health: A systematic review and meta-analysis (PMC, 2025) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11930668/ | IF resulted in a slightly greater, but statistically nonsignificant, decrease in weight | verified | full_quote | Tier 5 (government) |
| B2 | SC1-B | Effects of Intermittent Fasting in Human Compared to a Non-intervention Diet and Caloric Restriction: A Meta-Analysis of Randomized Controlled Trials (PMC, 2022) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9108547/ | IF outcomes did not differ from CR except for reduced WC | verified | full_quote | Tier 5 (government) |
| B3 | SC2-A | Review Article: Health Benefits of Intermittent Fasting (PMC, 2024) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11262566/ | reported human studies have been of short duration, and the baseline parameters of the study populations are highly variable | verified | full_quote | Tier 5 (government) |
| B4 | SC2-B | American Heart Association newsroom: 8-hour time-restricted eating linked to a 91% higher risk of cardiovascular death (AHA, 2024) | https://newsroom.heart.org/news/8-hour-time-restricted-eating-linked-to-a-91-higher-risk-of-cardiovascular-death | Limiting food intake to less than 8 hours per day was not associated with living longer | verified | full_quote | Tier 2 (unclassified) |

---

## Citation Verification Details

**B1 — PMC11930668 (SC1-A)**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

**B2 — PMC9108547 (SC1-B)**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

**B3 — PMC11262566 (SC2-A)**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

**B4 — AHA newsroom (SC2-B)**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

No citations failed verification. No impact analysis required.

---

## Computation Traces

```
  [✓] sc1_source_a: Full quote verified for sc1_source_a (source: tier 5/government)
  [✓] sc1_source_b: Full quote verified for sc1_source_b (source: tier 5/government)
  [✓] sc2_source_a: Full quote verified for sc2_source_a (source: tier 5/government)
  [✓] sc2_source_b: Full quote verified for sc2_source_b (source: tier 2/unknown)
  SC1 confirmed rejection sources: 2 / 2
  SC2 confirmed rejection sources: 2 / 2
  SC1: verified sources showing IF NOT proven superior for fat loss: 2 >= 2 = True
  SC2: verified sources showing IF NOT proven superior for longevity: 2 >= 2 = True
  compound: all sub-claims hold: 2 == 2 = True
```

---

## Independent Source Agreement (Rule 6)

**SC1 — Fat loss sources:**

| Source | Publication | Status |
|--------|-------------|--------|
| sc1_source_a | PMC11930668 (2025 systematic review, separate author team) | verified |
| sc1_source_b | PMC9108547 (2022 meta-analysis, separate author team and data set) | verified |

Independence note: Sources are from separate publications with different author teams and data sets. Both independently conclude IF does not significantly outperform CCR for fat loss.

**SC2 — Longevity sources:**

| Source | Publication | Status |
|--------|-------------|--------|
| sc2_source_a | PMC11262566 (2024 review article) | verified |
| sc2_source_b | AHA newsroom (2024, reporting on >20,000-person observational study) | verified |

Independence note: Sources are from separate institutions — an academic review published via PMC and the American Heart Association newsroom reporting on a population-level observational study.

---

## Adversarial Checks (Rule 5)

**Check 1**
- Question: Do any meta-analyses clearly show IF is significantly and clinically superiorly effective for fat loss vs. calorie-matched CCR?
- Verification performed: Searched: 'intermittent fasting significantly superior fat loss meta-analysis'; 'IF vs caloric restriction fat mass randomized controlled trial superiority'. Reviewed Nutrients 2024 (PMID 39458528), PMC11930668 (2025), PMC9099935 (2022), PMC9108547 (2022), and Lancet eClinicalMedicine umbrella review (2024).
- Finding: Some meta-analyses find modest statistically significant advantages in specific metrics (e.g., BMI in one study, insulin sensitivity in another), but no meta-analysis concludes IF is clearly clinically superior for overall fat loss. Nutrients 2024: 'FBS did not show superior long-term outcomes compared to CCR.' PMC11930668 2025: weight loss difference 'statistically nonsignificant.' The scientific literature consistently describes IF as equivalent — not proven superior — to matched caloric restriction for fat loss.
- Breaks proof: **No**

**Check 2**
- Question: Is there any human randomized controlled trial demonstrating that IF significantly extends lifespan or healthspan beyond other diets?
- Verification performed: Searched: 'intermittent fasting human lifespan RCT randomized controlled trial'; 'time-restricted eating longevity humans clinical trial'; 'IF longevity human evidence 2022 2023 2024'. Reviewed PMC11262566, PMC8932957, ScienceDirect S1568163724000928.
- Finding: No such RCT exists. All evidence for IF extending lifespan comes from animal models (C. elegans, Drosophila, mice). Human studies measure short-term metabolic proxies (weight, insulin, lipids), not lifespan. PMC11262566: 'reported human studies have been of short duration.' The most recent large observational study (AHA 2024, n>20,000) found that time-restricted eating was NOT associated with longer life, and was linked to 91% higher cardiovascular mortality.
- Breaks proof: **No**

**Check 3**
- Question: Is the AHA 2024 study on TRE and cardiovascular mortality robust enough to count as evidence against longevity claims?
- Verification performed: Searched: 'time-restricted eating AHA 2024 cardiovascular mortality limitations observational study confounders'; 'TRE longevity criticism 2024'. Reviewed Science Media Centre expert reactions and TCTMD debate coverage.
- Finding: The AHA 2024 abstract has limitations: it was observational (not an RCT), relied on only 2 days of dietary recall, and may have reverse causation (sick people may eat within a shorter window). However, for SC2 the key point is not that IF harms longevity, but that IF has NOT been proven to extend human lifespan. Even discounting the AHA study, SC2 source A (PMC11262566) independently establishes insufficient human longevity evidence.
- Breaks proof: **No**

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central, NIH |
| B2 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central, NIH |
| B3 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central, NIH |
| B4 | heart.org | unclassified | 2 | Unclassified domain — verify source authority manually. The American Heart Association is a major recognized nonprofit health authority; Tier 2 reflects absence from the classifier's pre-classified list, not low credibility. The SC2 verdict does not depend solely on B4: B3 (Tier 5) independently supports SC2. |

---

## Extraction Records

| ID | Extracted Value | Value in Quote | Quote Snippet |
|----|----------------|---------------|---------------|
| B1 | verified (citation status) | Yes | "IF resulted in a slightly greater, but statistically nonsignificant, decrease in" |
| B2 | verified (citation status) | Yes | "IF outcomes did not differ from CR except for reduced WC" |
| B3 | verified (citation status) | Yes | "reported human studies have been of short duration, and the baseline parameters " |
| B4 | verified (citation status) | Yes | "Limiting food intake to less than 8 hours per day was not associated with living" |

Extraction method: For qualitative/consensus proofs, the extraction records citation verification status per source. No numeric parsing was performed. The "value" field records the citation status string (verified/partial/not_found/fetch_failed); "value_in_quote" records whether the status is countable (verified or partial).

---

## Hardening Checklist

| Rule | Status | Note |
|------|--------|------|
| Rule 1: Values parsed from quotes, not hand-typed | N/A — qualitative proof; no numeric extraction | Auto-pass: no value-extraction patterns |
| Rule 2: Every citation URL fetched and quote checked | PASS | All 4 citations verified via `verify_all_citations()` |
| Rule 3: System time used for date-dependent logic | N/A — no time-dependent logic in this proof | Auto-pass: no date/age computations |
| Rule 4: Claim interpretation explicit with operator rationale | PASS | `CLAIM_FORMAL` with `operator_note` and per-sub-claim `operator_note` |
| Rule 5: Adversarial checks searched for independent counter-evidence | PASS | 3 adversarial checks with web searches for supporting evidence; none found |
| Rule 6: Cross-checks used independently sourced inputs | PASS | SC1: 2 separate author teams; SC2: PMC review + AHA observational study |
| Rule 7: Constants and formulas from computations.py | N/A — qualitative proof; no constants | Auto-pass: no inline formulas |
| validate_proof.py | PASS (16/17, 1 warning) | Warning: validator pattern match did not detect existing else-branch fallback — cosmetic only |

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
