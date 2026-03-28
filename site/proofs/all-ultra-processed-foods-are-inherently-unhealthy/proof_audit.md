# Audit: All ultra-processed foods are inherently unhealthy and should be avoided completely.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Ultra-processed foods (NOVA Group 4 classification) |
| Proof direction | disprove |
| Compound operator | AND |
| SC1 property | Every food classified as ultra-processed (NOVA Group 4) is inherently harmful regardless of context, quantity, or individual nutrient composition |
| SC1 operator | >= |
| SC1 threshold | 3 |
| SC1 proof direction | disprove |
| SC1 operator note | 'All UPFs are inherently unhealthy' is a universal claim. Logically, one credible counterexample disproves a universal. Threshold set to 3 (≥3 independent authoritative sources that reject the universal framing or identify UPFs acceptable in a healthy diet) to require multi-source consensus, not isolated dissent. |
| SC2 property | Authoritative health bodies recommend complete avoidance of all ultra-processed foods (i.e., no UPF should ever be consumed by anyone) |
| SC2 operator | >= |
| SC2 threshold | 3 |
| SC2 proof direction | disprove |
| SC2 operator note | 'Should be avoided completely' is read as an absolute, context-free recommendation. To disprove it, ≥3 independent authoritative health bodies or peer-reviewed sources must use reduction/limitation language — not elimination — and/or explicitly allow some UPFs in a healthy diet. |
| Compound operator note | The original claim is compound: (SC1 AND SC2). To disprove the AND claim, disproving either sub-claim is logically sufficient. This proof disproves both. |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_nhs | SC1: NHS — explicitly names UPFs acceptable in a healthy diet |
| B2 | sc1_harvard | SC1: Harvard T.H. Chan Nutrition Source — some UPFs may be useful |
| B3 | sc1_gibney | SC1: Gibney 2019 (Curr Dev Nutr) — no good/bad foods, only diets |
| B4 | sc2_nhs | SC2: NHS — recommends 'eating less' not complete avoidance |
| B5 | sc2_who | SC2: WHO Healthy Diet fact sheet — 'limit' not 'avoid completely' |
| B6 | sc2_harvard | SC2: Harvard — UPF use is consumer choice, pros and cons |
| A1 | — | SC1 verified disproof source count |
| A2 | — | SC2 verified disproof source count |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1 verified disproof source count | count(SC1 verified disproof citations >= 3) | 3 |
| A2 | SC2 verified disproof source count | count(SC2 verified disproof citations >= 3) | 3 |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1: NHS — UPFs acceptable in healthy diet | NHS (UK National Health Service) — What are processed foods? | https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/what-are-processed-foods/ | "Some ultra-processed foods can be included in a healthy diet – such as wholemeal sliced bread, wholegrain or higher fibre breakfast cereals or baked beans." | verified | full_quote | Tier 2 (unclassified) |
| B2 | SC1: Harvard — some UPFs may be useful | Harvard T.H. Chan School of Public Health — The Nutrition Source: Processed Foods | https://nutritionsource.hsph.harvard.edu/processed-foods/ | "some products may be a useful addition to a healthful diet" | verified | full_quote | Tier 4 (academic) |
| B3 | SC1: Gibney 2019 — no good/bad foods, only diets | Gibney MJ (2019), Ultra-Processed Foods: Definitions and Policy Issues, Current Developments in Nutrition, PMC6389637 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6389637/ | "there are good and bad diets, not good and bad foods" | verified | full_quote | Tier 5 (government) |
| B4 | SC2: NHS — 'eating less' not complete avoidance | NHS (UK National Health Service) — What are processed foods? | https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/what-are-processed-foods/ | "Most people would probably benefit from eating less ultra-processed foods that are high in saturated fat, salt or sugar." | verified | full_quote | Tier 2 (unclassified) |
| B5 | SC2: WHO — 'limit' not 'avoid completely' | World Health Organization — Healthy Diet Fact Sheet | https://www.who.int/news-room/fact-sheets/detail/healthy-diet | "Foods high in unhealthy fats, free sugars and sodium should be limited." | verified | full_quote | Tier 5 (government) |
| B6 | SC2: Harvard — consumer choice, pros and cons | Harvard T.H. Chan School of Public Health — The Nutrition Source: Processed Foods | https://nutritionsource.hsph.harvard.edu/processed-foods/ | "the use of processed and even ultra-processed foods is the choice of the consumer, and there are pros and cons that come with each type" | verified | full_quote | Tier 4 (academic) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — sc1_nhs**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B2 — sc1_harvard**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B3 — sc1_gibney**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B4 — sc2_nhs**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B5 — sc2_who**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

**B6 — sc2_harvard**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full quote match)

All 6 citations verified via live fetch. No unverified citations. No impact analysis required.

*Source: proof.py JSON summary*

---

## Computation Traces

```
  [✓] sc1_nhs: Full quote verified for sc1_nhs (source: tier 2/unknown)
  [✓] sc1_harvard: Full quote verified for sc1_harvard (source: tier 4/academic)
  [✓] sc1_gibney: Full quote verified for sc1_gibney (source: tier 5/government)
  [✓] sc2_nhs: Full quote verified for sc2_nhs (source: tier 2/unknown)
  [✓] sc2_who: Full quote verified for sc2_who (source: tier 5/government)
  [✓] sc2_harvard: Full quote verified for sc2_harvard (source: tier 4/academic)
  SC1 confirmed sources: 3 / 3
  SC2 confirmed sources: 3 / 3
  SC1 disproof: verified sources rejecting 'all UPFs inherently unhealthy': 3 >= 3 = True
  SC2 disproof: verified sources rejecting 'should be avoided completely': 3 >= 3 = True
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

### SC1 Disproof Sources

| Metric | Value |
|--------|-------|
| Sources consulted | 3 |
| Sources verified | 3 |
| sc1_nhs | verified |
| sc1_harvard | verified |
| sc1_gibney | verified |
| Independence note | NHS (UK government health body), Harvard T.H. Chan (US academic institution), Gibney 2019 in peer-reviewed journal (Current Developments in Nutrition) — independent institutions across different countries and sectors. |

### SC2 Disproof Sources

| Metric | Value |
|--------|-------|
| Sources consulted | 3 |
| Sources verified | 3 |
| sc2_nhs | verified |
| sc2_who | verified |
| sc2_harvard | verified |
| Independence note | NHS (UK), WHO (international UN agency), Harvard T.H. Chan (US academic) — three independent institutions across jurisdictions and sectors. |

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

**Check 1: Do any major health authorities support complete avoidance of all UPFs?**
- Verification performed: Searched for 'WHO ultra-processed foods avoid completely,' 'NHS avoid all ultra-processed foods,' 'USDA dietary guidelines ultra-processed avoid completely,' and reviewed Brazil 2014 Dietary Guidelines (origin of NOVA classification). Also checked AAP (American Academy of Pediatrics) infant formula guidance.
- Finding: No major health authority (WHO, NHS, CDC, USDA, AAP, BNF) recommends complete avoidance of all UPFs. Brazil's 2014 Dietary Guidelines say 'Avoid ultra-processed foods' but this is primarily a cultural/culinary preference statement and is explicitly contested by other nutrition bodies. The AAP continues to recommend infant formula (NOVA Group 4) for infants who cannot breastfeed, directly contradicting any universal avoidance directive.
- Breaks proof: No

**Check 2: Do observational studies show ALL UPF consumption is harmful, even at low levels?**
- Verification performed: Reviewed Rico-Campà et al. (BMJ 2019, PMC6538973) — largest-cited UPF mortality cohort study. Searched for 'ultra-processed food dose-response mortality low consumption' and 'ultra-processed food health benefit study.' Also reviewed Elizabeth et al. (Nutrients 2020, PMC7399967) systematic review.
- Finding: Rico-Campà et al. (BMJ 2019) found higher all-cause mortality in the highest quartile (≥4 servings/day) vs lowest quartile — a dose-dependent, not absolute, association. The lowest-quartile group had best outcomes while still consuming some UPFs. Authors explicitly note inability to rule out residual confounding. Elizabeth et al. (Nutrients 2020) reviewed 43 studies; all associations were at population/dietary-pattern level, not individual-product level. No peer-reviewed study demonstrates that any dose of any UPF is inherently harmful.
- Breaks proof: No

**Check 3: Is the NOVA 'ultra-processed' category scientifically coherent enough to support a universal health claim?**
- Verification performed: Searched 'NOVA classification criticism reliability,' 'ultra-processed food definition controversy,' and reviewed Gibney 2019 (PMC6389637). Checked whether infant formula is classified as UPF under NOVA.
- Finding: Gibney 2019 (PMC6389637) documents that NOVA classifies all commercially produced infant formula as ultra-processed and 'to be avoided,' yet 'no study has been undertaken to explore the implications of such a policy for this vulnerable group.' Harvard Nutrition Source states 'NOVA has been criticized for being too general in classifying certain foods, causing confusion.' The NOVA Group 4 category spans diet sodas, iron-fortified infant cereals, wholemeal sliced bread, and infant formula — a heterogeneous group that undermines any universal health claim.
- Breaks proof: No

**Check 4: Do NOVA originators themselves claim all UPFs are 'inherently' harmful?**
- Verification performed: Reviewed Monteiro et al. 2018 NOVA food classification paper and PAHO/WHO-aligned guidance. Searched 'Monteiro ultra-processed inherently unhealthy.'
- Finding: NOVA proponents (Monteiro et al.) argue that processing itself may cause harm beyond nutrient composition and advocate strong policy restrictions. However, their peer-reviewed papers phrase findings as population-level associations, not absolute per-food determinations. The 'inherently unhealthy' framing — implying harm regardless of quantity or context — exceeds what even the strongest pro-NOVA researchers assert in the literature.
- Breaks proof: No

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nhs.uk | unclassified | 2 | Unclassified domain — verify source authority manually. The NHS is the UK's national health service and is authoritative; the tier-2 score reflects a limitation of domain-based automated scoring (.uk TLD not in the government tier). |
| B2 | harvard.edu | academic | 4 | Academic domain (.edu) |
| B3 | nih.gov | government | 5 | Government domain (.gov) — PubMed Central, National Institutes of Health |
| B4 | nhs.uk | unclassified | 2 | Same as B1 — NHS is authoritative; tier-2 is a scoring artifact. |
| B5 | who.int | government | 5 | Known government/intergovernmental organization (WHO) |
| B6 | harvard.edu | academic | 4 | Academic domain (.edu) |

The two tier-2 citations (B1, B4) are both from nhs.uk, the official website of the UK National Health Service. Their authority is well established; the low tier score is an artifact of the automated domain classifier not recognizing .uk TLDs as government. The disproof does not depend solely on these sources: SC1 is also supported by B2 (Harvard, tier 4) and B3 (NIH, tier 5); SC2 is also supported by B5 (WHO, tier 5) and B6 (Harvard, tier 4).

*Source: proof.py JSON summary*

---

## Extraction Records

For qualitative proofs, the extraction records report citation verification status per source rather than numeric extraction.

| Fact ID | Value (Status) | Countable? | Quote Snippet |
|---------|---------------|------------|---------------|
| B1 | verified | Yes | "Some ultra-processed foods can be included in a healthy diet – such as wholemeal" |
| B2 | verified | Yes | "some products may be a useful addition to a healthful diet" |
| B3 | verified | Yes | "there are good and bad diets, not good and bad foods" |
| B4 | verified | Yes | "Most people would probably benefit from eating less ultra-processed foods that a" |
| B5 | verified | Yes | "Foods high in unhealthy fats, free sugars and sodium should be limited." |
| B6 | verified | Yes | "the use of processed and even ultra-processed foods is the choice of the consume" |

Countable = citation status is "verified" or "partial" (counts toward the confirmation threshold).

*Source: proof.py JSON summary (extractions)*

---

## Hardening Checklist

| Rule | Status | Details |
|------|--------|---------|
| Rule 1: No hand-typed extracted values | ✓ PASS | Qualitative proof — no numeric extraction. No date() literals or hand-typed values. |
| Rule 2: Citations verified by fetching | ✓ PASS | All 6 citations verified via live fetch using `verify_all_citations()`. |
| Rule 3: System time anchored | ✓ PASS | `date.today()` present in proof.py. |
| Rule 4: Explicit claim interpretation | ✓ PASS | `CLAIM_FORMAL` dict with `operator_note` for both sub-claims and the compound claim. |
| Rule 5: Adversarial checks | ✓ PASS | 4 independent adversarial checks documented, all returning `breaks_proof: False`. |
| Rule 6: Independent cross-checks | ✓ PASS | 6 distinct source references across two independent institution sets per sub-claim. |
| Rule 7: No hard-coded constants/formulas | ✓ PASS | `compare()` used for all claim evaluations; no inline formulas or eval(). |
| validate_proof.py | ✓ PASS | 13/13 checks passed, 0 issues, 0 warnings. |

*Source: proof.py inline output (execution trace); validate_proof.py output*

---

Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.
