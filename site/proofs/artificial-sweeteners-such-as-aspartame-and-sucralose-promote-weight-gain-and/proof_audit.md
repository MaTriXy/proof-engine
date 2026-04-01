# Audit: Artificial sweeteners such as aspartame and sucralose promote weight gain and metabolic disease.

- **Generated:** 2026-04-01
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | artificial sweeteners, specifically aspartame and sucralose |
| Compound operator | AND |
| Proof direction | affirm |
| SC1 property | associated with weight gain and metabolic disease in human observational studies |
| SC1 operator | >= |
| SC1 threshold | 3 |
| SC1 operator_note | SC-association: at least 3 independent peer-reviewed sources must document a statistically significant positive association between artificial sweetener consumption and weight gain or metabolic disease markers (obesity, T2D, cardiovascular disease, metabolic syndrome, impaired glucose tolerance) in human populations. Observational study designs (cohort, cross-sectional) are sufficient for SC1. |
| SC2 property | causal relationship established via RCTs or equivalent causal inference methods in humans |
| SC2 operator | >= |
| SC2 threshold | 3 |
| SC2 operator_note | SC-causation: the word 'promote' implies causation. At least 3 independent sources must establish causation using RCTs, Mendelian randomization, Bradford Hill criteria, or equivalent methods. Observational sources do not satisfy SC2. Animal mechanistic studies do not satisfy SC2 without confirming human experimental data. |
| Compound operator_note | Both sub-claims must hold for PROVED. Reverse causality — overweight/at-risk individuals preferentially choosing diet products — cannot be eliminated without experimental design. If only SC1 holds: PARTIALLY VERIFIED. |

*Source: proof.py JSON summary `claim_formal`*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_source_a | Azad et al. 2017 CMAJ — meta-analysis, 30 cohort studies, 405,907 participants, observational association with weight/metabolic outcomes |
| B2 | sc1_source_b | Steffen et al. 2023 Int J Obesity (CARDIA) — 25-year prospective cohort, N=3,088, adipose tissue and obesity risk |
| B3 | sc1_source_c | Kuk & Brown 2016 APNM — NHANES III cross-sectional, N=2,856, aspartame and glucose tolerance |
| B4 | sc2_source_a | Suez et al. 2014 Nature — gut-microbiome mechanism for NAS-induced glucose intolerance (primarily mouse model; insufficient for SC2 threshold) |
| A1 | — | SC1 confirmed source count |
| A2 | — | SC2 confirmed source count |

*Source: proof.py JSON summary `fact_registry`*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1 confirmed source count | count(verified sc1 citations) = 3 | 3 |
| A2 | SC2 confirmed source count | count(verified sc2 citations) = 1 | 1 |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1: Azad 2017 CMAJ meta-analysis | Azad et al. 2017, CMAJ (PMC) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5515645/ | "consumption of nonnutritive sweeteners was associated with increases in weight and waist circumference, and higher incidence of obesity, hypertension, metabolic syndrome, type 2 diabetes and cardiovascular events" | verified | full_quote | Tier 5 (government) |
| B2 | SC1: Steffen 2023 CARDIA cohort | Steffen et al. 2023, Int J Obesity (PubMed) | https://pubmed.ncbi.nlm.nih.gov/37443272/ | "ArtSw, including diet soda, was associated with greater risks of incident obesity" | verified | full_quote | Tier 5 (government) |
| B3 | SC1: Kuk & Brown 2016 NHANES | Kuk & Brown 2016, APNM (PubMed) | https://pubmed.ncbi.nlm.nih.gov/27216413/ | "consumption of aspartame is associated with greater obesity-related impairments in glucose tolerance" | verified | full_quote | Tier 5 (government) |
| B4 | SC2: Suez 2014 gut microbiome mechanism | Suez et al. 2014, Nature (PubMed) | https://pubmed.ncbi.nlm.nih.gov/25231862/ | "consumption of commonly used NAS formulations drives the development of glucose intolerance through induction of compositional and functional alterations to the intestinal microbiota" | verified | full_quote | Tier 5 (government) |

**Note on credibility tiers:** All four sources are accessed via PubMed or PMC (nih.gov), which are US government databases (NLM/NIH). The Tier 5 rating reflects the `.gov` domain. The actual papers are peer-reviewed academic publications — Azad et al. (CMAJ, a top Canadian medical journal), Steffen et al. (International Journal of Obesity), Kuk & Brown (Applied Physiology, Nutrition and Metabolism), and Suez et al. (Nature). The tier 5 rating correctly indicates high source credibility.

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — Azad et al. 2017, CMAJ (PMC)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B2 — Steffen et al. 2023, CARDIA (PubMed)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)
- Note: "ArtSw" is the abbreviation for artificial sweeteners as used in the abstract of the paper.

**B3 — Kuk & Brown 2016, APNM (PubMed)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B4 — Suez et al. 2014, Nature (PubMed)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)
- Note: "NAS" = non-caloric artificial sweeteners, as used in the paper's abstract. The study primarily examines saccharin (not aspartame or sucralose), with results validated in a small human sample (n=7 controlled intervention; n=381 observational). Even with a verified citation, this source is insufficient for SC2: it is a mechanistic/animal study and does not constitute a randomized controlled trial or equivalent causal inference method in humans.

*Source: proof.py JSON summary*

---

## Computation Traces

```
SC1 confirmed sources: 3 / 3
SC2 confirmed sources: 1 / 1
SC1: association with weight gain and metabolic disease: 3 >= 3 = True
SC2: causation established via RCTs or causal inference: 1 >= 3 = False
compound: all sub-claims hold: 1 == 2 = False
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

### SC1 — Association sources

| Check | Value |
|-------|-------|
| Sources consulted | 3 |
| Sources verified | 3 |
| sc1_source_a (Azad 2017) | verified |
| sc1_source_b (Steffen 2023) | verified |
| sc1_source_c (Kuk 2016) | verified |
| Independence note | Sources are from different research groups, institutions, and study designs: Azad 2017 (Canadian systematic review/meta-analysis of 30 international cohort studies), Steffen 2023 (US CARDIA longitudinal cohort), Kuk 2016 (US NHANES cross-sectional survey). Different populations, methods, and outcome measures provide genuine independence. |

### SC2 — Causation sources

| Check | Value |
|-------|-------|
| Sources consulted | 1 |
| Sources verified | 1 |
| sc2_source_a (Suez 2014) | verified |
| Independence note | Only 1 SC2 source was identified. It proposes a gut-microbiome mechanism but is primarily mouse-model data with a very small human validation (n=7 intervention, n=381 observational). No RCTs, Mendelian randomization studies, or Bradford Hill analyses establishing causation in human populations were found. Multiple RCT meta-analyses (Miller 2014, McGlynn 2022, Qin 2025) actively contradict the causal claim. The Rule 6 warning for SC2 having only 1 source is intentional: there genuinely are no additional qualifying causal sources, and the experimental evidence contradicts causation. |

*Source: proof.py JSON summary `cross_checks`*

---

## Adversarial Checks (Rule 5)

**Check 1: Do RCTs show that artificial sweeteners cause weight gain or metabolic disease?**
- Verification performed: Searched "artificial sweeteners RCT weight gain randomized controlled trial meta-analysis". Reviewed Miller & Perez 2014 (AJCN, 15 RCTs), McGlynn et al. 2022 (JAMA Network Open, network meta-analysis), Qin et al. 2025 (Frontiers in Nutrition, 9 RCTs, 1,457 participants), and Toews et al. 2019 (BMJ, pre-specified WHO systematic review).
- Finding: Multiple RCT meta-analyses show no weight gain and no metabolic harm. Miller & Perez 2014 found a modest weight DECREASE (−0.80 kg; 95% CI: −1.17, −0.43) across 15 RCTs. McGlynn et al. 2022 found low/no-calorie sweetened beverages comparable to water. Qin et al. 2025 found no significant differences in any metabolic marker across 9 RCTs. This is strong counter-evidence against SC2 and is why it fails.
- Breaks proof: No — SC1 (observational association) is logically independent of SC2 and still holds. The RCT evidence informs the PARTIALLY VERIFIED verdict correctly.

**Check 2: Is the observational association confounded by reverse causality?**
- Verification performed: Searched "artificial sweeteners reverse causality confounding observational studies". Reviewed Azad et al. 2017 CMAJ limitations section, WHO 2023 guideline evidence grade, and Toews et al. 2019 BMJ on confounding.
- Finding: Reverse causality is the dominant competing explanation. Azad et al. 2017 acknowledges "The cohort results may reflect confounding by indication, as people who are overweight or at risk of metabolic disease may choose nonnutritive sweeteners." The WHO 2023 guideline is "conditional" specifically because of this limitation.
- Breaks proof: No — this confirms SC2 fails (causation not established), consistent with PARTIALLY VERIFIED.

**Check 3: Does the evidence apply equally to both aspartame AND sucralose?**
- Verification performed: Searched "sucralose weight gain adiposity evidence" and reviewed Steffen et al. 2023 (CARDIA) per-sweetener results for sucralose.
- Finding: CARDIA 2023 found sucralose showed "all ptrend > 0.05" — no significant association with adipose tissue or obesity — while aspartame and saccharin showed significant associations. The SC1 evidence is primarily for aspartame, not sucralose.
- Breaks proof: No — SC1 treats the sweetener class overall (multiple compounds across multiple studies), and the class-level association holds. However, this weakens the claim's specificity for sucralose.

**Check 4: Does the WHO 2023 guideline establish causation?**
- Verification performed: Reviewed the WHO May 2023 news release directly. Checked evidence grade. Reviewed Harvard T.H. Chan School commentary (June 2023).
- Finding: The WHO 2023 guideline is "conditional" (weakest guidance tier) due to predominantly observational evidence. The WHO statement uses associational language ("potential undesirable effects"). Harvard experts noted the WHO meta-analysis excluded large studies (>100,000 participants) showing beneficial substitution effects. The guideline does not establish causation.
- Breaks proof: No — consistent with PARTIALLY VERIFIED.

*Source: proof.py JSON summary `adversarial_checks`*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nih.gov (PMC) | government | 5 | US National Library of Medicine database; paper published in CMAJ (peer-reviewed) |
| B2 | nih.gov (PubMed) | government | 5 | US National Library of Medicine database; paper published in Int J Obesity (peer-reviewed) |
| B3 | nih.gov (PubMed) | government | 5 | US National Library of Medicine database; paper published in APNM (peer-reviewed) |
| B4 | nih.gov (PubMed) | government | 5 | US National Library of Medicine database; paper published in Nature (peer-reviewed) |

All citations are accessed via US government academic databases (PubMed/PMC). All underlying papers are published in peer-reviewed journals. No sources are flagged as low-credibility.

*Source: proof.py JSON summary `citations[].credibility`*

---

## Extraction Records

For qualitative/consensus proofs, each B-type fact records citation verification status rather than extracted numeric values.

| Fact ID | Value (citation status) | Value in Quote (countable) | Quote Snippet |
|---------|------------------------|---------------------------|---------------|
| B1 | verified | True | "consumption of nonnutritive sweeteners was associated with increases in weight a" |
| B2 | verified | True | "ArtSw, including diet soda, was associated with greater risks of incident obesit" |
| B3 | verified | True | "consumption of aspartame is associated with greater obesity-related impairments " |
| B4 | verified | True | "consumption of commonly used NAS formulations drives the development of glucose " |

*Source: proof.py JSON summary `extractions`*

---

## Hardening Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Rule 1: Every empirical value parsed from quote text, not hand-typed | N/A | Qualitative proof — no numeric values extracted from quotes. Citation verification status used as the counting mechanism. |
| Rule 2: Every citation URL fetched and quote checked | PASS | All 4 citations verified via `verify_all_citations()`. Status: B1=verified, B2=verified, B3=verified, B4=verified. All via live fetch. |
| Rule 3: System time used for date-dependent logic | PASS | `date.today()` present in proof.py. Proof is not time-sensitive but the generator timestamp uses the system date. |
| Rule 4: Claim interpretation explicit with operator rationale | PASS | `CLAIM_FORMAL` dict with `operator_note` at compound level and per sub-claim. Causal decomposition into SC1 and SC2 is explicitly documented. |
| Rule 5: Adversarial checks searched for independent counter-evidence | PASS | 4 adversarial checks: RCT meta-analyses contradicting causation, reverse causality confounding, sucralose-specific evidence, WHO guideline evidence grade. |
| Rule 6: Cross-checks used independently sourced inputs | PASS (with warning) | SC1 has 3 sources from different research groups and study designs. SC2 has 1 source — intentional, reflecting genuine absence of human causal evidence; documented in cross_checks independence_note. |
| Rule 7: Constants and formulas imported from computations.py, not hand-coded | N/A | No numeric constants or formulas. `compare()` from computations.py used for all evaluations. |
| validate_proof.py result | PASS with 2 warnings | 17/19 checks passed. 0 issues. 2 warnings: both are Rule 6 warnings for SC2 having only 1 source — intentional and documented. |

*Source: proof.py inline output + author analysis*

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
