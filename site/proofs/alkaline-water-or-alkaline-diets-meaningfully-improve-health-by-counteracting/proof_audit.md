# Audit: Alkaline water or alkaline diets meaningfully improve health by counteracting body acidity

- **Generated:** 2026-04-01
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

*Source: proof.py JSON summary*

| Field | Value |
|-------|-------|
| Subject | Alkaline water and alkaline diets |
| Compound operator | AND |
| Proof direction | disprove |
| Operator note | The claim uses OR to name two interventions (alkaline water, alkaline diets), both claimed to work through the same mechanism ('counteracting body acidity'). Disproving an OR claim requires showing that NEITHER intervention achieves the stated mechanism (SC1) nor produces meaningful health improvements (SC2). |

**Sub-claims:**

| ID | Property | Operator | Threshold | Operator Note |
|----|----------|----------|-----------|---------------|
| SC1 | counteracts body acidity by producing a meaningful, sustained change in blood pH | >= | 3 | SC1 tests the mechanistic premise: that alkaline water/diet can alter blood pH in a clinically meaningful way. Disproof counts authoritative sources confirming blood pH is NOT meaningfully altered by diet or alkaline water in healthy individuals. |
| SC2 | produces meaningful health improvements beyond those attributable to diet quality alone | >= | 3 | SC2 tests the health outcome claim. Disproof counts authoritative sources (systematic reviews, major medical centers) finding no significant health benefits from alkaline water/diet beyond general diet quality. |

---

## Fact Registry

*Source: proof.py JSON summary*

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_source_a | SC1: Harvard Health — alkaline water cannot durably change blood pH |
| B2 | sc1_source_b | SC1: MD Anderson Cancer Center — dietary changes don't affect blood pH |
| B3 | sc1_source_c | SC1: PMC/Schwalfenberg 2011 — body maintains steady blood pH via renal and respiratory mechanisms |
| B4 | sc2_source_a | SC2: De Gruyter systematic review 2023 — no additional health effects of alkaline water vs mineral water |
| B5 | sc2_source_b | SC2: British Journal of Nutrition / Fenton & Huang 2016 — alkaline promotion not justified for cancer |
| B6 | sc2_source_c | SC2: PMC/Schwalfenberg 2011 — no substantial evidence alkaline diet improves bone health |
| A1 | — | SC1 verified disproof source count |
| A2 | — | SC2 verified disproof source count |

---

## Full Evidence Table

### Type A (Computed) Facts

*Source: proof.py JSON summary*

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1 verified disproof source count | count(verified SC1 disproof citations) = 3 | 3 |
| A2 | SC2 verified disproof source count | count(verified SC2 disproof citations) = 3 | 3 |

### Type B (Empirical) Facts

*Source: proof.py JSON summary*

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1: Harvard Health — blood pH rebalanced by kidneys | Harvard Health Publishing | https://www.health.harvard.edu/staying-healthy/is-alkaline-water-better | "Even if you drank enough alkaline water to slightly raise the pH of your blood, your kidneys would quickly go into action to rebalance your blood pH." | verified | full_quote | Tier 4 (academic) |
| B2 | SC1: MD Anderson — dietary changes don't affect blood pH | MD Anderson Cancer Center | https://www.mdanderson.org/cancerwise/alkaline-diet--what-cancer-patients-should-know.h00-159223356.html | "dietary changes will not impact the pH level of your blood" | verified | full_quote | Tier 2 (unclassified) |
| B3 | SC1: PMC — body maintains steady blood pH | PMC — Schwalfenberg 2011, The Alkaline Diet, Journal of Environmental and Public Health | https://pmc.ncbi.nlm.nih.gov/articles/PMC3195546/ | "The human body has an amazing ability to maintain a steady pH in the blood with the main compensatory mechanisms being renal and respiratory." | verified | full_quote | Tier 5 (government) |
| B4 | SC2: De Gruyter — no additional health effects | De Gruyter — systematic review, Reviews on Environmental Health 2023 | https://www.degruyterbrill.com/document/doi/10.1515/reveh-2022-0057/html?lang=en | "Recent evidences do not prove any additional health effects of alkaline, oxygenated, or demineralized water compared to mineral water." | verified | full_quote | Tier 2 (unclassified) |
| B5 | SC2: PubMed — alkaline promotion not justified | PubMed — Fenton & Huang 2016, British Journal of Nutrition (systematic review) | https://pubmed.ncbi.nlm.nih.gov/27297008/ | "Promotion of alkaline diet and alkaline water to the public for cancer prevention or treatment is not justified" | verified | full_quote | Tier 5 (government) |
| B6 | SC2: PMC — no evidence for bone health | PMC — Schwalfenberg 2011, The Alkaline Diet, Journal of Environmental and Public Health | https://pmc.ncbi.nlm.nih.gov/articles/PMC3195546/ | "There is no substantial evidence that this improves bone health or protects from osteoporosis." | verified | full_quote | Tier 5 (government) |

---

## Citation Verification Details

*Source: proof.py JSON summary*

**B1 — Harvard Health Publishing**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: full match

**B2 — MD Anderson Cancer Center**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: full match

**B3 — PMC / Schwalfenberg 2011**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: full match

**B4 — De Gruyter systematic review 2023**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: full match

**B5 — PubMed / Fenton & Huang 2016**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: full match

**B6 — PMC / Schwalfenberg 2011 (second quote)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: full match

No citations failed verification. The DISPROVED verdict does not depend on any unverified citation.

---

## Computation Traces

*Source: proof.py inline output (execution trace)*

```
  SC1: sources confirming blood pH not changed by alkaline water/diet: 3 >= 3 = True
  SC2: sources rejecting meaningful health benefits from alkaline water/diet: 3 >= 3 = True
  compound: both sub-claims meet disproof threshold: 2 == 2 = True
```

---

## Independent Source Agreement (Rule 6)

*Source: proof.py JSON summary*

**SC1 cross-check:**

| Source | Status | Institution |
|--------|--------|-------------|
| sc1_source_a | verified | Harvard Health Publishing |
| sc1_source_b | verified | MD Anderson Cancer Center |
| sc1_source_c | verified | PMC / NIH (Schwalfenberg 2011) |

Independence note: Harvard Health Publishing, MD Anderson Cancer Center, and Schwalfenberg 2011 (PMC) are independently published by different institutions.

**SC2 cross-check:**

| Source | Status | Institution |
|--------|--------|-------------|
| sc2_source_a | verified | De Gruyter / Reviews on Environmental Health |
| sc2_source_b | verified | PubMed / British Journal of Nutrition |
| sc2_source_c | verified | PMC / NIH (Schwalfenberg 2011) |

Independence note: De Gruyter systematic review (2023), Fenton & Huang 2016 (British Journal of Nutrition), and Schwalfenberg 2011 (PMC) are independently published. Schwalfenberg 2011 appears in both SC1 and SC2 for different facts; each SC has two additional independent institutional sources.

---

## Adversarial Checks (Rule 5)

*Source: proof.py JSON summary*

**Check 1: Do any RCTs demonstrate meaningful health benefits from alkaline water or alkaline diet?**
- Search performed: Searched PubMed and Google Scholar for 'alkaline water RCT health benefits', 'alkaline diet randomized controlled trial outcomes'. Found the De Gruyter 2023 systematic review explicitly concluding no RCT evidence of benefit. The IJAHS systematic review (2022) noted that the majority of studies are animal models, in vitro work, or small exploratory human trials — not large-scale RCTs.
- Finding: No large-scale RCTs demonstrate meaningful health benefits. The 2023 De Gruyter systematic review found no significant difference in blood parameters, gut microbiota, or fitness between alkaline water and mineral water groups. Consistent with SC2 disproof.
- Breaks proof: No

**Check 2: Does alkaline water show benefits for specific conditions like acid reflux (GERD)?**
- Search performed: Searched for 'alkaline water GERD acid reflux clinical evidence'. Found a 2012 in vitro study (Koufman & Johnston) showing alkaline water (pH 8.8) may inactivate pepsin, and a small 2016 observational study. Also found the American College of Gastroenterology does not list alkaline water in GERD treatment guidelines.
- Finding: Limited in vitro and observational evidence for laryngopharyngeal reflux. However: (a) this is condition-specific, not "meaningful health improvement" in general; (b) not from large RCTs; (c) acts locally in the esophagus/stomach, not through blood pH change. Does not restore SC1 or generalize SC2.
- Breaks proof: No

**Check 3: Does observational evidence show alkaline water consumers have better health outcomes?**
- Search performed: Searched for 'alkaline water observational study health outcomes'. Found the PLOS One 2022 cross-sectional study (PMC9621423) on postmenopausal women showing lower fasting blood glucose and triglycerides.
- Finding: The PLOS One cross-sectional study found lower fasting blood glucose and triglycerides in alkaline water drinkers among postmenopausal women. However: (a) cross-sectional studies cannot establish causation; (b) confounding by healthier lifestyle not controlled; (c) one observational study is outweighed by systematic reviews of controlled data. Does not break SC2 disproof.
- Breaks proof: No

**Check 4: Does the alkaline diet have health benefits, even if not through pH change?**
- Search performed: Searched for 'alkaline diet health benefits mechanism'. Found MD Anderson and Schwalfenberg 2011 acknowledging that alkaline diets may have health benefits — but attributing these to antioxidants, phytochemicals, and the K/Na ratio, not to alkalizing the blood.
- Finding: Any health advantages of alkaline-leaning diets are attributed to diet quality (fruits, vegetables, legumes), not to pH effects. MD Anderson states: "these benefits are not caused by alkalizing the body." Since the claim specifically asserts the mechanism "by counteracting body acidity," and SC1 disproves that mechanism, diet-quality benefits do not rescue the claim as stated.
- Breaks proof: No

---

## Source Credibility Assessment

*Source: proof.py JSON summary*

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | harvard.edu | academic | 4 | Academic domain (.edu) — Harvard Health Publishing |
| B2 | mdanderson.org | unknown | 2 | Automated classifier: unclassified domain. Manual verification: MD Anderson Cancer Center is a leading NCI-designated comprehensive cancer center, highly authoritative. |
| B3 | nih.gov | government | 5 | Government domain (.gov) — PMC/NIH |
| B4 | degruyterbrill.com | unknown | 2 | Automated classifier: unclassified domain. Manual verification: De Gruyter is a major academic publisher; *Reviews on Environmental Health* is a peer-reviewed journal. Source is authoritative despite classifier limitation. |
| B5 | nih.gov | government | 5 | Government domain (.gov) — PubMed/NIH |
| B6 | nih.gov | government | 5 | Government domain (.gov) — PMC/NIH |

Two sources (B2, B4) have automated tier 2 (unclassified) ratings because the classifier does not recognize mdanderson.org and degruyterbrill.com. Both are authoritative: MD Anderson Cancer Center is a major NCI-designated cancer center; De Gruyter is a major academic publisher of peer-reviewed journals. The disproof is independently supported by three tier-4/5 sources (B1, B3, B5, B6), so the conclusions do not depend solely on the tier-2 sources.

---

## Extraction Records

*Source: proof.py JSON summary (qualitative proof — extraction records reflect citation verification status)*

| ID | Value (Citation Status) | Countable (verified or partial) | Quote Snippet |
|----|------------------------|---------------------------------|---------------|
| B1 | verified | Yes | "Even if you drank enough alkaline water to slightly raise the pH of your blood, " |
| B2 | verified | Yes | "dietary changes will not impact the pH level of your blood" |
| B3 | verified | Yes | "The human body has an amazing ability to maintain a steady pH in the blood with " |
| B4 | verified | Yes | "Recent evidences do not prove any additional health effects of alkaline, oxygena" |
| B5 | verified | Yes | "Promotion of alkaline diet and alkaline water to the public for cancer preventio" |
| B6 | verified | Yes | "There is no substantial evidence that this improves bone health or protects from" |

*Extraction method: qualitative proof — no numeric extraction. Citation verification status is the evidence unit. All 6 citations verified by full_quote match on live fetch.*

*Source: author analysis*

---

## Hardening Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Rule 1: No hand-typed extracted values | ✓ Pass | Qualitative proof — no numeric value extraction. No data_values or parse_number_from_quote patterns. |
| Rule 2: All citations fetched and verified | ✓ Pass | `verify_all_citations()` called; all 6 citations returned status=verified via full_quote match on live fetch. |
| Rule 3: System time anchored | ✓ Pass | `date.today()` used via the generator block; no time-dependent claim logic in this proof. |
| Rule 4: Claim interpretation explicit | ✓ Pass | `CLAIM_FORMAL` with `operator_note` present; both sub-claims have documented operator rationale and threshold justification. |
| Rule 5: Adversarial checks searched independently | ✓ Pass | 4 adversarial searches performed covering RCT evidence, condition-specific claims (GERD), observational data, and diet-quality alternative mechanisms. |
| Rule 6: Cross-checks use independent inputs | ✓ Pass | SC1: 3 independent institutional sources (Harvard Health, MD Anderson, PMC). SC2: 3 independent sources (De Gruyter, British Journal of Nutrition, PMC). Schwalfenberg 2011 appears in both SCs for different facts; two additional independent sources per SC ensure independence. |
| Rule 7: No hard-coded constants or formulas | ✓ Pass | No numeric formulas; `compare()` from `computations.py` used for all evaluations. |
| validate_proof.py | ✓ PASS | 17/17 checks passed, 0 issues, 0 warnings. |

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
