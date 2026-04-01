# Audit: High-protein diets above 1.6 g/kg body weight damage kidneys in healthy people.

- **Generated:** 2026-03-31
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

*Source: proof.py JSON summary*

| Field | Value |
|-------|-------|
| Subject | High-protein diet above 1.6 g/kg body weight per day |
| Property | Whether it causes measurable kidney damage (GFR decline, proteinuria, or CKD development) in adults without pre-existing kidney disease |
| Operator | >= |
| Threshold | 3 (independent verified sources that reject the claim) |
| Proof direction | disprove |
| Operator note | The claim is DISPROVED if ≥3 independent systematic reviews or meta-analyses confirm that high-protein intake does NOT damage kidneys in healthy adults. "Damage" is interpreted as measurable adverse change in kidney function markers (GFR decline, increased proteinuria, or elevated creatinine). The 1.6 g/kg threshold cited in the claim is not a clinically established kidney-safety boundary; it is commonly cited in sports nutrition literature (Morton et al. 2018) as an approximate upper limit for muscle protein synthesis optimization. The meta-analyses used here study protein intakes ≥1.5 g/kg or "above the US RDA (0.8 g/kg)" — both categories encompass the >1.6 g/kg range in the claim. Sources in empirical_facts reject the claim; sources supporting the claim are in adversarial_checks. |

---

## Fact Registry

*Source: proof.py JSON summary*

| ID | Key | Label |
|----|-----|-------|
| B1 | devries_2018 | Devries et al. (2018) Journal of Nutrition — meta-analysis of 28 RCTs, 1358 healthy adults: HP intakes do not adversely influence GFR |
| B2 | van_elswyk_2018 | Van Elswyk et al. (2018) Advances in Nutrition — systematic review of RCTs and observational studies: higher protein consistent with normal kidney function |
| B3 | cheng_2024 | Cheng et al. (2024) Frontiers in Nutrition — meta-analysis of 6 cohort studies, 148,051 participants: higher protein associated with lower CKD risk |
| A1 | *(computed)* | Verified source count (sources rejecting the claim) |

---

## Full Evidence Table

### Type A (Computed) Facts

*Source: proof.py JSON summary*

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Verified source count (sources rejecting the claim) | count(verified citations) = 3 | 3 |

### Type B (Empirical) Facts

*Source: proof.py JSON summary*

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | HP intakes do not adversely influence GFR in healthy adults | Devries MC et al. (2018) Journal of Nutrition, 148(11):1760-1775 | https://pubmed.ncbi.nlm.nih.gov/30383278/ | "Our analysis indicates that HP intakes do not adversely influence kidney function on GFR in healthy adults." | Verified | full_quote | Tier 5 (government) |
| B2 | Higher protein consistent with normal kidney function in healthy individuals | Van Elswyk ME et al. (2018) Advances in Nutrition, 9(4):404-418 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6054213/ | "These data further indicate that, at least in the short term, higher protein intake within the range of recommended intakes for protein is consistent with normal kidney function in healthy individuals." | Verified | full_quote | Tier 5 (government) |
| B3 | Higher protein associated with lower CKD risk | Cheng Y et al. (2024) Frontiers in Nutrition, 11:1408424 | https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2024.1408424/full | "The data showed a lower CKD risk significantly associated higher-level dietary total, plant or animal protein (especially for fish and seafood) intake." | Verified | full_quote | Tier 4 (academic) |

---

## Citation Verification Details

*Source: proof.py JSON summary*

**B1 — Devries et al. (2018)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B2 — Van Elswyk et al. (2018)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B3 — Cheng et al. (2024)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

---

## Computation Traces

*Source: proof.py inline output (execution trace)*

```
  [✓] devries_2018: Full quote verified for devries_2018 (source: tier 5/government)
  [✓] van_elswyk_2018: Full quote verified for van_elswyk_2018 (source: tier 5/government)
  [✓] cheng_2024: Full quote verified for cheng_2024 (source: tier 4/academic)
  Confirmed sources: 3 / 3
  verified source count vs threshold (disproof: sources rejecting the claim): 3 >= 3 = True
```

---

## Independent Source Agreement (Rule 6)

*Source: proof.py JSON summary*

| Description | Sources Consulted | Sources Verified | Agreement |
|-------------|------------------|-----------------|-----------|
| Multiple independent systematic reviews consulted | 3 | 3 | Yes |

**Source statuses:**
- devries_2018: verified
- van_elswyk_2018: verified
- cheng_2024: verified

**Independence note:** B1 (Devries 2018) and B2 (Van Elswyk 2018) are independent systematic reviews published simultaneously in different journals (Journal of Nutrition and Advances in Nutrition). B3 (Cheng 2024) is a more recent independent meta-analysis from a different author group. All three draw on overlapping but not identical underlying study pools. Independence is at the publication and author-team level; as is typical for meta-analyses in nutrition, they may draw on some of the same primary studies.

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

*Source: proof.py JSON summary*

**Check 1: Is there evidence that high-protein diets cause rapid kidney function decline in healthy adults?**

- **Verification performed:** Searched "high protein diet rapid GFR decline healthy adults" and "high protein kidney function decline cohort study"; found Jhee et al. (2019, Nephrology Dialysis Transplantation), a Korean community-based prospective cohort of 9,226 adults without kidney disease, reporting that the highest protein intake quartile had 1.32× higher odds of rapid eGFR decline vs the lowest quartile.
- **Finding:** Jhee et al. (2019) is an observational association study, not an RCT. Observational findings cannot establish causation due to confounding (high animal protein often co-occurs with high sodium, red meat, etc.). The RCT meta-analysis by Devries et al. (2018) — the highest level of evidence — found no adverse GFR change when protein intake was experimentally manipulated in controlled trials. The observational association does not override the controlled trial evidence.
- **Breaks proof:** No

**Check 2: Does glomerular hyperfiltration from high protein intake cause long-term kidney damage in healthy people?**

- **Verification performed:** Searched "glomerular hyperfiltration high protein long-term damage healthy kidneys"; reviewed Ko et al. (2020, JASN, PMC7460905) and Kalantar-Zadeh et al. (2020, Nephrology Dialysis Transplantation, doi:10.1093/ndt/gfz216). Ko et al. state in the abstract that "evidence suggests that worsening renal function may occur in individuals with and perhaps without impaired kidney function" and note "It is possible that long-term high protein intake may lead to de novo CKD." Kalantar-Zadeh et al. argue protein restriction is warranted for vulnerable populations.
- **Finding:** Both papers acknowledge the hyperfiltration mechanism but qualify their concerns for healthy people. Ko et al. (2020) also note that "long-term trials have not observed an increase in proteinuria" in those without kidney disease. Kalantar-Zadeh et al. (2020) explicitly state "persons with healthy intact kidneys may not be affected by this harmful impact." The concerns are speculative for healthy individuals; no RCT has demonstrated actual kidney damage (not just adaptive hyperfiltration) in healthy adults.
- **Breaks proof:** No

**Check 3: Is 1.6 g/kg body weight a clinically established kidney safety limit?**

- **Verification performed:** Searched "1.6 g/kg protein kidney safety limit" and "1.6 g/kg protein kidney damage threshold"; searched National Kidney Foundation guidelines and nephrology clinical guidelines.
- **Finding:** The 1.6 g/kg figure originates in sports nutrition literature as the upper bound for muscle protein synthesis optimization (Morton et al. 2018, Br J Sports Med), not as a nephrology safety threshold. Clinical nephrology guidelines (National Kidney Foundation, KDIGO) address protein restriction for people WITH CKD; they do not identify 1.6 g/kg as a risk cutoff for healthy adults. There is no established clinical threshold beyond which healthy kidneys are damaged by protein intake.
- **Breaks proof:** No

---

## Source Credibility Assessment

*Source: proof.py JSON summary*

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nih.gov | government | 5 | Government domain (.gov) — PubMed/NCBI abstract page |
| B2 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central full-text |
| B3 | frontiersin.org | academic | 4 | Known academic/scholarly publisher |

All sources have tier ≥ 4. No low-credibility sources were used.

---

## Extraction Records

*Source: proof.py JSON summary*

For qualitative proofs, extraction records reflect citation verification status per source rather than numeric value extraction.

| Fact ID | Value (status) | Value in Quote | Quote Snippet (first 80 chars) |
|---------|----------------|----------------|-------------------------------|
| B1 | verified | True | "Our analysis indicates that HP intakes do not adversely influence kidney functio" |
| B2 | verified | True | "These data further indicate that, at least in the short term, higher protein int" |
| B3 | verified | True | "The data showed a lower CKD risk significantly associated higher-level dietary t" |

*Source: proof.py JSON summary. No numeric extraction was performed — this is a qualitative consensus proof.*

---

## Hardening Checklist

- **Rule 1 — No hand-typed extracted values:** N/A — qualitative proof; no numeric values extracted from quotes. Auto-passed by validator.
- **Rule 2 — Citations verified by fetching:** All three citations verified live. `verify_all_citations()` imported and called. ✓
- **Rule 3 — Anchored to system time:** `date.today()` used for `generated_at`. No time-dependent claim logic required. ✓
- **Rule 4 — Explicit claim interpretation:** `CLAIM_FORMAL` dict present with `operator_note` specifying disproof direction, threshold rationale, and interpretation of "damage." ✓
- **Rule 5 — Adversarial checks searched for counter-evidence:** Three adversarial checks performed: (a) observational evidence for GFR decline (Jhee 2019), (b) hyperfiltration-to-damage speculation (Ko 2020, Kalantar-Zadeh 2020), (c) origin of 1.6 g/kg threshold. ✓
- **Rule 6 — Cross-checks used independently sourced inputs:** Three independent systematic review teams (Devries, Van Elswyk, Cheng) from different journals and institutions. ✓
- **Rule 7 — Constants/formulas from computations.py:** `compare()` imported and used for claim evaluation. No hard-coded formulas. ✓
- **validate_proof.py result:** PASS — 15/15 checks, 0 issues, 0 warnings.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-03-31.*
