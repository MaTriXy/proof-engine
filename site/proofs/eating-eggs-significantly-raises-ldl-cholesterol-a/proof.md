# Proof: Eating eggs significantly raises LDL cholesterol and heart-disease risk.

- **Generated:** 2026-03-28
- **Verdict:** DISPROVED (with unverified citations)
- **Audit trail:** [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- **SC2 (CVD risk) — directly contradicted:** Two independent meta-analyses covering 1.7–2 million participants and 39–28 prospective cohort studies both find that moderate egg consumption (up to 1 egg/day) is **not** associated with increased cardiovascular disease risk (B1, B2 — both fully verified).
- **SC1 (LDL) — threshold not met:** The best RCT meta-analysis evidence (17 RCTs, healthy adults) shows an increase of **8.14 mg/dL** in LDL-C with higher egg consumption (B3). This is statistically significant but falls below the 10 mg/dL threshold for clinical meaningfulness — and disappears in dietary contexts low in saturated fat.
- **Compound claim fails:** The claim requires BOTH sub-claims to hold. Neither does: SC1's "significantly" is not supported at the clinical level, and SC2 is directly contradicted by large-scale prospective evidence.
- **Historical note:** The 2015 U.S. Dietary Guidelines Advisory Committee removed the previous 300 mg/day dietary cholesterol limit, citing "no appreciable relationship between consumption of dietary cholesterol and serum cholesterol," signaling a major shift in the scientific consensus underlying this claim.

---

## Claim Interpretation

**Natural language:** "Eating eggs significantly raises LDL cholesterol and heart-disease risk."

**Formal interpretation:**

| Field | Value |
|-------|-------|
| Subject | Moderate egg consumption (up to ~1 egg/day) in healthy adults |
| Property | Compound AND: (SC1) significantly raises LDL-C AND (SC2) significantly raises CVD risk |
| Operator | AND — both sub-claims must be true |
| SC1 threshold | ≥10 mg/dL absolute LDL-C increase per meta-analytic RCT evidence |
| SC2 disproof threshold | ≥2 independent prospective cohort meta-analyses showing no significant CVD risk |

**Operator note:** "Significantly" is interpreted as clinically meaningful — not merely statistically significant. This is the conservative interpretation: statins produce 30–50 mg/dL LDL reductions; a dietary effect below 10 mg/dL is not clinically actionable by standard lipid-management guidelines. For SC2, "significantly raises" requires a statistically significant CVD risk increase in large prospective cohort studies. Disproof requires ≥2 independent meta-analyses contradicting this. Moderate consumption (~1 egg/day) is the scope, consistent with the primary evidence base.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | BMJ 2020 meta-analysis: 28 prospective cohort studies, 1.72M participants — egg consumption and CVD risk | Yes |
| B2 | Eur J Nutr 2021 dose-response meta-analysis: 39 studies, ~2M participants — egg consumption and CVD risk | Yes |
| B3 | Nutrients 2020 RCT meta-analysis: 17 RCTs in healthy subjects — egg consumption and LDL-C | Partial (47.1% fragment match; academic HTML noise on PMC) |
| A1 | SC2: count of independent prospective cohort meta-analyses finding no significant CVD risk increase | Computed: 2 independent sources (threshold for disproof: ≥2) |
| A2 | SC1: RCT-observed LDL increase vs clinical significance threshold (≥10 mg/dL) | Computed: 8.14 mg/dL vs ≥10.0 mg/dL (does not meet threshold) |

---

## Proof Logic

### Sub-claim 1 (SC1): Does egg consumption significantly raise LDL cholesterol?

The most comprehensive RCT meta-analysis for healthy subjects (B3 — Zhu et al., Nutrients 2020, 17 RCTs) found that higher egg consumption was associated with an LDL-C increase of **8.14 mg/dL** (A2, parsed from B3 quote, p < 0.0001 statistically).

While this is statistically significant in a large pooled dataset, the clinical interpretation is different. Against a 10 mg/dL clinical threshold (A2), 8.14 mg/dL does not qualify as "clinically significant" by standard lipid guidelines. Additional context:

- A 2025 RCT (PMID 40339906) found **no LDL increase** when eggs were consumed as part of a diet low in saturated fat, indicating the effect is driven more by dietary context (saturated fat co-consumption) than by egg intake per se.
- The 2015 U.S. Dietary Guidelines Advisory Committee removed the 300 mg/day dietary cholesterol limit based on their finding of "no appreciable relationship between consumption of dietary cholesterol and serum cholesterol."
- SC1 claim does **not** meet the ≥10 mg/dL threshold.

### Sub-claim 2 (SC2): Does egg consumption significantly raise heart-disease risk?

Two independent, large-scale prospective cohort meta-analyses directly contradict this sub-claim (A1):

1. **B1** (Drouin-Chartier et al., BMJ 2020): 28 prospective cohort studies, 1,720,108 participants, 139,195 CVD events. Conclusion: *"moderate egg consumption (up to one egg per day) is not associated with cardiovascular disease risk overall."* Results were consistent for coronary heart disease and stroke.

2. **B2** (Kazemi et al., Eur J Nutr 2021): 39 prospective cohort studies, ~2 million participants. Conclusion: *"there may be no need to discourage egg consumption at the population level."*

Both B1 and B2 are independently verified, draw from different primary cohort datasets, and use different methodologies (meta-regression vs dose-response analysis). Their agreement constitutes a cross-check on SC2 (see below).

### Compound evaluation

The original claim is an AND: both SC1 and SC2 must hold. Neither does. The compound claim fails (A1, A2).

---

## Counter-Evidence Search

**JAMA 2019 (Zhong et al.):** A widely-cited 2019 JAMA paper found that each additional 300 mg/day of dietary cholesterol was associated with 17% higher CVD risk. However, this result is for **total dietary cholesterol intake**, not eggs as a food, and has been criticized for not adjusting for the nutrient displaced by eggs in the diet. More specific egg-consumption meta-analyses (B1, B2), with larger combined populations and direct food-based exposure assessment, do not replicate this finding for moderate egg intake.

**Sub-population caveat:** Both B1 and B2 note that in people with **type 2 diabetes**, higher egg consumption may be modestly associated with elevated CVD risk (pooled RR ~1.25 in some sub-analyses). Similarly, LDL hyper-responders (~30% of the general population) may show larger LDL responses to dietary cholesterol. These sub-population effects do not break the proof — the claim is stated without qualification, and the evidence base for the general healthy adult population is clear. Clinicians managing high-risk patients should apply individual judgment.

**Historical consensus shift:** Prior to 2015, both U.S. dietary guidelines and popular understanding held that eggs were harmful due to their cholesterol content. This assumption has been substantially revised by the evidence reviewed here, illustrating how this claim reflects an outdated consensus.

---

## Conclusion

**Verdict: DISPROVED (with unverified citations)**

The compound claim — that eggs *significantly* raise both LDL cholesterol AND heart-disease risk — is disproved on both sub-claims:

- **SC2** is directly contradicted by two fully verified, independent meta-analyses covering nearly 2 million participants (B1, B2). The weight of prospective cohort evidence shows no significant CVD risk increase from moderate egg consumption.
- **SC1** is not supported at the clinical significance level. The RCT meta-analysis (B3) shows a modest ~8.14 mg/dL LDL increase — statistically significant in pooled data but below clinical actionability thresholds, context-dependent, and consistent with the 2015 regulatory decision to remove dietary cholesterol limits.

The one partially unverified citation (B3 — partial, 47.1% fragment match due to academic HTML noise on PMC) supports the SC1 sub-claim in the DISPROOF direction. The core disproof of SC2 relies entirely on B1 and B2, which are both fully verified.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
