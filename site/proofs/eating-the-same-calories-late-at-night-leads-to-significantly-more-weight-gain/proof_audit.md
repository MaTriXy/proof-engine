# Audit: Eating the same calories late at night leads to significantly more weight gain and fat storage than earlier in the day.

- **Generated:** 2026-04-01
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

*Source: proof.py JSON summary*

| Field | Value |
|-------|-------|
| Subject | Late-night caloric intake (same total calories as daytime eating) |
| Compound operator | AND |
| Proof direction | affirm |

**Sub-claims:**

| ID | Property | Operator | Threshold |
|----|----------|----------|-----------|
| SC1 | Late eating (same total calories) measurably increases fat storage and reduces fat oxidation compared to earlier eating — confirmed by independent RCTs and controlled studies | >= | 3 |
| SC2 | Late eating (same total calories) causes significantly more overall weight gain over time — both statistically and clinically meaningful — compared to earlier eating | >= | 3 |

**Operator note:** The claim uses causal language ("leads to") requiring decomposition into SC-association/causation sub-claims per engine rules. SC1 covers fat storage and fat oxidation effects — established if 3+ RCTs and controlled studies confirm with same-calorie intake. SC2 covers the "significantly more weight gain" component — established only if 3+ independent sources confirm clinically meaningful weight differences under controlled calorie conditions. Both must hold for PROVED. SC2's failure yields PARTIALLY VERIFIED (SC1 established, SC2 not established).

---

## Fact Registry

*Source: proof.py JSON summary*

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_source_a | SC1: Gu et al. 2020 RCT — late dinner reduces dietary fat oxidation by ~10 percentage points (P=.02) |
| B2 | sc1_source_b | SC1: McHill et al. 2017 — circadian food timing associated with body fat independent of calories and activity |
| B3 | sc1_source_c | SC1: Harvard Gazette 2022 — Vujovic et al. RCT: late eating shifts adipose gene expression toward fat accumulation |
| B4 | sc2_source_a | SC2: Liu et al. 2024 JAMA meta-analysis — 29 RCTs: earlier eating produces 1.75 kg more weight loss, but effect "small and of uncertain clinical importance" |
| A1 | (computed) | SC1 verified source count (fat storage effects) |
| A2 | (computed) | SC2 verified source count (clinically significant weight gain) |

---

## Full Evidence Table

### Type A (Computed) Facts

*Source: proof.py JSON summary*

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1 verified source count (fat storage effects) | count(verified sc1 citations) = 3 | 3 |
| A2 | SC2 verified source count (clinically significant weight gain) | count(verified sc2 citations) = 1 | 1 |

### Type B (Empirical) Facts

*Source: proof.py JSON summary*

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1: Gu et al. 2020 RCT — fat oxidation | Gu et al. (2020) J Clin Endocrinol Metab (PMC/NIH) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7337187/ | "total palmitate oxidized was lower for LD (74.5% ± 5.7%) than RD (84.5% ± 5.2%, P = .02)" | verified | full_quote | Tier 5 (government) |
| B2 | SC1: McHill et al. 2017 — circadian timing and body fat | McHill et al. (2017) Am J Clin Nutr (PMC/NIH) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5657289/ | "the consumption of food during the circadian evening and/or night, independent of more traditional risk factors such as amount or content of food intake and activity level, plays an important role in body composition" | verified | full_quote | Tier 5 (government) |
| B3 | SC1: Vujovic 2022 adipose gene expression | Harvard Gazette (2022) | https://news.harvard.edu/gazette/story/2022/10/study-looks-at-why-late-night-eating-increases-obesity-risk/ | "adipose tissue gene expression toward increased adipogenesis and decreased lipolysis, which promote fat growth" | verified | full_quote | Tier 4 (academic) |
| B4 | SC2: JAMA 2024 meta-analysis weight outcomes | Liu et al. (2024) JAMA Network Open (PMC/NIH) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11530941/ | "consuming the majority of calories earlier in the day resulted in more weight loss compared with consuming them later in the day (MD, -1.75 kg; 95% CI, -2.37 to -1.13 kg)" | verified | fragment (80%) | Tier 5 (government) |

---

## Citation Verification Details

*Source: proof.py JSON summary*

**B1 — Gu et al. 2020 (PMC7337187)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B2 — McHill et al. 2017 (PMC5657289)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B3 — Harvard Gazette 2022**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)
- Note: B3 is a news article reporting the Vujovic et al. 2022 Cell Metabolism RCT. The Cell Metabolism paper itself returned HTTP 403 on live fetch. The Harvard Gazette is the official institutional news outlet of Harvard University (tier 4/academic) and accurately quotes from the study. The quote about adipose gene expression is verbatim from the Gazette's reporting of the underlying RCT.

**B4 — Liu et al. 2024 JAMA Network Open (PMC11530941)**
- Status: verified
- Method: fragment (coverage_pct = 80.0%)
- Fetch mode: live
- Note: Fragment match at exactly the engine's 80% verification threshold. The MD and 95% CI values (-1.75 kg; -2.37 to -1.13 kg) are distinctive numeric strings. The quote's core claim about earlier eating producing more weight loss is confirmed by the fragment match. This is the minimum passing threshold per engine rules.

---

## Computation Traces

*Source: proof.py inline output (execution trace)*

```
  [✓] sc1_source_a: Full quote verified for sc1_source_a (source: tier 5/government)
  [✓] sc1_source_b: Full quote verified for sc1_source_b (source: tier 5/government)
  [✓] sc1_source_c: Full quote verified for sc1_source_c (source: tier 4/academic)
  [✓] sc2_source_a: Quote largely verified (24/30 words matched) for sc2_source_a (source: tier 5/government)
  SC1 confirmed sources: 3 / 3
  SC2 confirmed sources: 1 / 1
  SC1: fat storage/fat oxidation effects confirmed: 3 >= 3 = True
  SC2: clinically significant weight gain confirmed: 1 >= 3 = False
  compound: all sub-claims hold: 1 == 2 = False
```

---

## Independent Source Agreement (Rule 6)

*Source: proof.py JSON summary*

**SC1 sources (fat storage effects):**

| Source | Status | Independence |
|--------|--------|--------------|
| sc1_source_a (Gu et al. 2020, J Clin Endocrinol Metab) | verified | Independent RCT, Brigham and Women's Hospital / Harvard |
| sc1_source_b (McHill et al. 2017, Am J Clin Nutr) | verified | Independent observational study, Brigham and Women's Hospital / Harvard (different research group from Vujovic 2022) |
| sc1_source_c (Vujovic et al. 2022, via Harvard Gazette) | verified | Independent RCT, Brigham and Women's Hospital / Harvard |

Independence note: All three SC1 sources are from peer-reviewed journals (J Clin Endocrinol Metab, Am J Clin Nutr, Cell Metabolism) by different first authors, published in different years (2017, 2020, 2022). Although all involve Brigham and Women's Hospital / Harvard groups, they are distinct studies measuring different outcomes (fat oxidation rate, body fat composition, adipose gene expression) using different methodologies (metabolic chamber, observational DEXA, crossover RCT with adipose biopsy). They are independently published; no upstream measurement is shared.

**SC2 sources (clinically significant weight gain):**

| Source | Status | Independence note |
|--------|--------|-------------------|
| sc2_source_a (Liu et al. 2024 JAMA Network Open) | verified | Only 1 source; threshold not met (1 of 3 required) |

Only 1 source was found for SC2. The JAMA 2024 meta-analysis synthesizes 29 RCTs but the meta-analysis itself qualifies the weight difference as clinically modest. No additional independent sources met the criteria for confirming clinically significant weight gain from same-calorie late eating.

---

## Adversarial Checks (Rule 5)

*Source: proof.py JSON summary*

**Check 1: Gold-standard TDEE measurement RCTs**
- Question: Do high-quality RCTs with gold-standard energy expenditure measurement show no metabolic difference between morning and evening calorie loading?
- Search performed: "meal timing energy expenditure RCT doubly labeled water" and "calorie timing no effect metabolism controlled trial"
- Finding: Ruddick-Collins et al. 2022 (Cell Metabolism, PMC9605877): 30-subject 4-week crossover RCT using doubly-labeled water found no TDEE difference (2,871 vs 2,846 kcal/day, p=0.184). Conclusion: "calorie utilization does not vary with time of day." This is counter-evidence against SC2 but does not undermine SC1's fat-oxidation/gene-expression endpoints, which are already accounted for by SC2 failing to reach threshold.
- Breaks proof: No

**Check 2: TREAT randomized clinical trial**
- Question: Does the TREAT trial show no significant between-group weight difference for time-restricted vs unrestricted eating?
- Search performed: "TREAT trial time restricted eating weight loss RCT"
- Finding: Lowe et al. 2020 (JAMA Internal Medicine, PMID 32986097): 116 participants, 12-week RCT, no significant between-group weight difference (-0.26 kg; 95% CI -1.30 to 0.78; P=0.63). Counter-evidence for SC2; already reflected in SC2 failing threshold.
- Breaks proof: No

**Check 3: Clinical significance caveat in JAMA 2024 meta-analysis**
- Question: Does the JAMA 2024 meta-analysis itself describe the weight difference as clinically unimportant?
- Search performed: Fetched PMC11530941 (Liu et al. 2024 JAMA Network Open, 29 RCTs, 2,485 participants)
- Finding: Authors state "the effect sizes found were small and of uncertain clinical importance" and "weight loss was not clinically significant (<5%)." Under the proof's interpretation of "significantly" as requiring both statistical and clinical meaningfulness, this meta-analysis does not establish SC2. This is the primary driver of SC2's failure.
- Breaks proof: No

**Check 4: Surrogate endpoint concern**
- Question: Are SC1 fat storage biomarker changes short-term surrogates that may not translate to clinically significant long-term weight gain?
- Search performed: "fat oxidation surrogate endpoint weight gain clinical relevance" and "circadian eating fat storage long-term outcomes"
- Finding: Gu et al. 2020 authors use hedged language: "If these changes occur on a chronic basis, they may contribute to the development of obesity." No RCT has bridged the ~10 percentage-point fat oxidation reduction from a single late dinner to clinically significant long-term weight gain under identical caloric conditions. Consistent with PARTIALLY VERIFIED verdict — SC1 effects are real, SC2 not established.
- Breaks proof: No

---

## Source Credibility Assessment

*Source: proof.py JSON summary*

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nih.gov | government | 5 | Government domain (.gov) — NIH PubMed Central |
| B2 | nih.gov | government | 5 | Government domain (.gov) — NIH PubMed Central |
| B3 | harvard.edu | academic | 4 | Academic domain (.edu) — Harvard University official news |
| B4 | nih.gov | government | 5 | Government domain (.gov) — NIH PubMed Central |

All citations are tier 4 or higher. No low-credibility sources were used.

---

## Extraction Records

*Source: proof.py JSON summary*

For qualitative/consensus proofs, extraction records document citation verification status per source:

| Fact ID | Value (citation status) | Value countable | Quote snippet |
|---------|------------------------|-----------------|---------------|
| B1 | verified | Yes | "total palmitate oxidized was lower for LD (74.5% ± 5.7%) than RD (84.5% ± 5.2%," |
| B2 | verified | Yes | "the consumption of food during the circadian evening and/or night, independent o" |
| B3 | verified | Yes | "adipose tissue gene expression toward increased adipogenesis and decreased lipol" |
| B4 | verified | Yes | "consuming the majority of calories earlier in the day resulted in more weight lo" |

*Source: proof.py JSON summary*

Extraction method: Citation verification status (verified/partial/not_found/fetch_failed) is used as the countable evidence unit. All four citations were verified against live pages. B4 was verified via fragment matching at 80% coverage (the engine's minimum threshold for "verified" status).

*Source: author analysis*

---

## Hardening Checklist

- **Rule 1 (No hand-typed extracted values):** N/A — qualitative consensus proof. No numeric values are extracted from quotes. The validator auto-passed Rule 1.
- **Rule 2 (Verify citations by fetching):** PASS — `verify_all_citations()` called; all 4 citations verified against live pages. B3's underlying study (Cell Metabolism) returned 403, but the Harvard Gazette page (B3's direct URL) was fetched successfully and the quote was verified.
- **Rule 3 (Anchor to system time):** N/A — proof contains no time-dependent logic. `date.today()` is present in `generator.generated_at` only.
- **Rule 4 (Explicit claim interpretation):** PASS — `CLAIM_FORMAL` dict present with sub-claims, operators, thresholds, and `operator_note` fields documenting the "significantly" interpretation choice and its rationale.
- **Rule 5 (Adversarial checks):** PASS — 4 adversarial checks performed, including 2 that found direct counter-evidence (Ruddick-Collins TDEE, TREAT trial). Each counter-evidence finding includes an explicit rebuttal explaining why it does not break SC1 (different endpoints) and is already captured by SC2 failing to reach threshold.
- **Rule 6 (Independent cross-checks):** PASS — SC1 uses 3 sources from different research groups measuring different outcomes. SC2's single source is documented with an independence note explaining why only 1 source was found and why it does not meet the threshold.
- **Rule 7 (No hard-coded constants):** N/A — qualitative consensus proof. No numeric constants or formulas used. `compare()` imported and used for all boolean evaluations.
- **validate_proof.py result:** PASS with warnings — 17/19 checks passed, 0 issues, 2 warnings. Warnings are about SC2 having only 1 source (by design — SC2 fails for insufficient evidence).

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
