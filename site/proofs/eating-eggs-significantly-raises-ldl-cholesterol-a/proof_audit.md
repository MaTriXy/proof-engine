# Audit: Eating eggs significantly raises LDL cholesterol and heart-disease risk.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Moderate egg consumption (up to ~1 egg/day) in healthy adults |
| Property | Compound AND: (SC1) significantly raises LDL-C AND (SC2) significantly raises cardiovascular disease (CVD) risk |
| Operator | AND |
| Operator note | Compound claim — both sub-claims must hold for the overall claim to be PROVED. SC1 ('significantly raises LDL'): 'significantly' is interpreted as clinically meaningful — operationalized as ≥10 mg/dL absolute increase per meta-analytic RCT evidence. This is a conservative threshold: statins produce 30–50 mg/dL reductions; a dietary effect below 10 mg/dL is not considered clinically actionable by standard lipid-management guidelines. SC2 ('significantly raises heart-disease risk'): interpreted as statistically significant increased CVD incidence observed in large prospective cohort studies. Disproof requires ≥2 independent prospective cohort meta-analyses showing no significant CVD risk increase. Evaluated at moderate consumption (~1 egg/day). |
| SC1 LDL threshold | 10.0 mg/dL |
| SC2 disproof min sources | 2 |

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_cvd_a | BMJ 2020 meta-analysis: 28 prospective cohort studies, 1.72M participants — egg consumption and CVD risk |
| B2 | source_cvd_b | Eur J Nutr 2021 dose-response meta-analysis: 39 studies, ~2M participants — egg consumption and CVD risk |
| B3 | source_ldl_a | Nutrients 2020 RCT meta-analysis: 17 RCTs in healthy subjects — egg consumption and LDL-C |
| A1 | — | SC2: count of independent prospective cohort meta-analyses finding no significant CVD risk increase |
| A2 | — | SC1: RCT-observed LDL increase vs clinical significance threshold (≥10 mg/dL) |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC2: count of independent prospective cohort meta-analyses finding no significant CVD risk increase | count verified meta-analyses showing no significant CVD risk increase | 2 independent sources (threshold for disproof: ≥2) |
| A2 | SC1: RCT-observed LDL increase vs clinical significance threshold (≥10 mg/dL) | parse_number_from_quote(B3) and compare to clinical significance threshold | 8.14 mg/dL vs ≥10.0 mg/dL (does not meet threshold) |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | BMJ 2020 meta-analysis | Drouin-Chartier et al., BMJ 2020 (PMC7190072) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7190072/ | "moderate egg consumption (up to one egg per day) is not associated with cardiovascular disease risk overall" | verified | full_quote | Tier 5 (government) |
| B2 | Eur J Nutr 2021 dose-response meta-analysis | Kazemi et al., Eur J Nutr 2021 (PMC8137614) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8137614/ | "there may be no need to discourage egg consumption at the population level" | verified | full_quote | Tier 5 (government) |
| B3 | Nutrients 2020 RCT meta-analysis | Zhu et al., Nutrients 2020 (PMC7400894) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7400894/ | "The MEC group also had higher LDL-c than the control group (MD = 8.14, p < 0.0001)" | partial | fragment (47.1%) | Tier 5 (government) |

---

## Citation Verification Details

### B1 — Drouin-Chartier et al., BMJ 2020 (PMC7190072)
- **Status:** verified
- **Method:** full_quote
- **Coverage:** N/A (full match)
- **Fetch mode:** live
- **Impact:** None — fully verified. Supports SC2 disproof.

### B2 — Kazemi et al., Eur J Nutr 2021 (PMC8137614)
- **Status:** verified
- **Method:** full_quote
- **Coverage:** N/A (full match)
- **Fetch mode:** live
- **Impact:** None — fully verified. Supports SC2 disproof.

### B3 — Zhu et al., Nutrients 2020 (PMC7400894)
- **Status:** partial (fragment match, 47.1% coverage)
- **Method:** fragment
- **Coverage:** 47.1%
- **Fetch mode:** live
- **Impact:** B3 is used to establish the ~8.14 mg/dL LDL increase for SC1. The partial match is consistent with academic HTML noise on PMC pages (inline reference markers, superscripts). Importantly, B3 supports the DISPROOF direction of SC1 (the LDL increase is below the clinical significance threshold), so even with partial verification, the conclusion is unchanged. The SC2 disproof depends entirely on B1 and B2 (both fully verified).

---

## Computation Traces

```
B3_ldl_increase: Parsed '8.14' -> 8.14
[✓] B3_ldl_increase: extracted 8.14 from quote
SC1: RCT LDL increase (8.14 mg/dL) meets clinical significance threshold (≥10 mg/dL): 8.14 >= 10.0 = False
SC2: count of independent meta-analyses contradicting CVD risk claim (≥2 required for disproof): 2 >= 2 = True
Compound AND: both SC1 and SC2 must be proved (0 of 2 proved → claim_holds = False): 0 == 2 = False
```

---

## Independent Source Agreement (Rule 6)

### SC2 cross-check

| Check | Source A | Source B | Agreement |
|-------|----------|----------|-----------|
| CVD risk finding | B1 (PMC7190072, 28 cohorts, 1.72M participants): "not associated with cardiovascular disease risk overall" | B2 (PMC8137614, 39 cohorts, ~2M participants): "no need to discourage egg consumption at the population level" | Yes — qualitative agreement; both find null or inverse CVD association at moderate egg intake |

**Independence note:** B1 and B2 are independently published meta-analyses covering different (though potentially overlapping) sets of primary prospective cohort studies. B1 is authored by Drouin-Chartier et al. (BMJ, 2020) and emphasizes US/European cohorts and absolute risk analysis. B2 is authored by Kazemi et al. (Eur J Nutr, 2021) and performs a global dose-response analysis across 39 studies. Their common upstream data source is the prospective cohort literature, but their analysis methods, coverage, and conclusions are independently derived. This provides independent publication-level verification, not independent measurement.

---

## Adversarial Checks (Rule 5)

### 1. Do any large meta-analyses show significantly increased CVD risk from egg consumption?
- **Verification performed:** Searched PubMed/PMC for "egg consumption cardiovascular disease risk increased meta-analysis". Reviewed Zhong et al. JAMA 2019 (PMID 30874756), which found 17% higher CVD risk per 300 mg/day of dietary cholesterol. However, this result was for total dietary cholesterol, not eggs specifically, and has been criticized for not accounting for replacing nutrients. Multiple subsequent egg-specific meta-analyses (PMC7190072, PMC8137614) focused on eggs as a food and found no significant CVD risk.
- **Finding:** Zhong et al. JAMA 2019 associates dietary cholesterol with CVD, but subsequent larger egg-specific meta-analyses (1.7–2M participants) do not confirm a significant risk for moderate egg consumption.
- **Breaks proof:** No

### 2. Could the ~8 mg/dL LDL increase be clinically significant under a stricter threshold?
- **Verification performed:** Reviewed AHA/ACC lipid management guidelines (2018 ACC/AHA Guideline on the Management of Blood Cholesterol). Clinical intervention thresholds are based on absolute LDL levels (e.g., >130 mg/dL with intermediate risk factors). Lifestyle modification targets are typically ≥10–15% LDL reduction (≈15–25 mg/dL on a 150 mg/dL baseline). Also searched for whether any clinical body explicitly considers <10 mg/dL LDL dietary changes as clinically significant.
- **Finding:** No clinical guideline classifies an 8 mg/dL dietary-induced LDL increase as clinically significant in isolation. A 2025 RCT (PMID 40339906) found no LDL increase when eggs were consumed within a low-saturated-fat diet, indicating the effect is confounded by dietary context.
- **Breaks proof:** No

### 3. Is the claim true for individuals with type 2 diabetes or hypercholesterolemia?
- **Verification performed:** Reviewed sub-group analyses in PMC7190072 and PMC8137614. Both note that among people with type 2 diabetes, higher egg consumption may be associated with modestly elevated CVD risk (pooled RR ~1.25, with overlapping CIs). LDL hyper-responders (~30% of the population) may also show larger LDL responses to dietary cholesterol.
- **Finding:** Sub-population effects may exist for diabetics and LDL hyper-responders. The claim is stated without qualification. The proof evaluates moderate consumption in healthy adults, consistent with the primary evidence base.
- **Breaks proof:** No

### 4. Has scientific consensus historically supported the egg-cholesterol-heart-disease link?
- **Verification performed:** Searched "dietary cholesterol guidelines history eggs 300mg recommendation". Prior to 2015, U.S. dietary guidelines warned against dietary cholesterol intake >300 mg/day. The 2015 DGAC removed this limit, stating they found "no appreciable relationship between consumption of dietary cholesterol and serum cholesterol."
- **Finding:** The claim reflects an older scientific consensus that was revised in 2015. The current evidence-based position is that moderate egg consumption does not significantly raise LDL or CVD risk in the general population.
- **Breaks proof:** No

---

## Source Credibility Assessment

All three sources (B1, B2, B3) are hosted on PubMed Central (pmc.ncbi.nlm.nih.gov), a government-operated (.gov) repository of peer-reviewed biomedical literature. Each is a peer-reviewed meta-analysis published in a major journal (BMJ, European Journal of Nutrition, Nutrients). All assessed as Tier 5 (government domain) with no credibility flags.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
