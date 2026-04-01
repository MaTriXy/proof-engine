# Audit: Sunscreen is more dangerous due to chemical absorption and vitamin D blocking than moderate sun exposure.

- **Generated:** 2026-03-31
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Chemical sunscreen |
| Property | Comparative harm vs. moderate sun exposure |
| Operator | >= |
| Proof direction | disprove |
| Threshold | 3 verified authoritative sources rejecting the claim |
| Operator note | The claim asserts sunscreen is MORE dangerous than moderate sun exposure, citing two mechanisms: (1) systemic absorption of chemical UV filters and (2) reduction of vitamin D synthesis. Interpreted as: the combined harm of sunscreen use >= the harm of moderate unprotected sun exposure. We DISPROVE this by gathering authoritative sources showing: (a) chemical absorption is documented but no human harm has been demonstrated; (b) real-world vitamin D reduction from sunscreen is minimal — population studies show no significant difference in vitamin D levels between sunscreen users and non-users with equivalent outdoor exposure; (c) UV radiation is the dominant cause of skin cancer (~86-90% of cases); and (d) sunscreen use reduces melanoma risk by ~50% and squamous cell carcinoma by ~40%. Threshold: 3 or more independently verified authoritative sources must reject the claim's conclusion for a DISPROVED verdict. |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_aad | American Academy of Dermatology: absorbed ingredients not proven harmful |
| B2 | source_mdanderson | MD Anderson Cancer Center: no medical evidence sunscreen causes cancer; UV does |
| B3 | source_pmc_cmaj | PMC/CMAJ 2020: high-quality evidence sunscreen reduces melanoma and nonmelanoma cancer |
| B4 | source_pmc_vitd | PMC 2022 expert panel: sunscreen does not limit vitamin D production in real-world use |
| B5 | source_skincancer | Skin Cancer Foundation: ~90% of nonmelanoma skin cancers associated with UV exposure |
| A1 | — | Verified disproof source count |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Verified disproof source count | count(verified disproof citations) = 5 | 5 |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | American Academy of Dermatology: absorbed ingredients not proven harmful | American Academy of Dermatology — Sunscreen FAQs | https://www.aad.org/media/stats-sunscreen | "Just because an ingredient is absorbed into the bloodstream does not mean that it is harmful or unsafe." | verified | full_quote | Tier 2 (unknown) |
| B2 | MD Anderson: no medical evidence sunscreen causes cancer; UV does | MD Anderson Cancer Center — Sunscreen Myths Debunked | https://www.mdanderson.org/cancerwise/sunscreen-myths-debunked.h00-159697545.html | "There is no medical evidence that sunscreen causes cancer. However, there is a lot of evidence that UV rays from the sun and tanning beds do." | verified | full_quote | Tier 2 (unknown) |
| B3 | PMC/CMAJ 2020: high-quality evidence sunscreen reduces melanoma and nonmelanoma cancer | PMC / CMAJ — Efficacy and Safety of Sunscreen (2020) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7759112/ | "High-quality evidence has shown that sunscreen reduces the risk of developing both melanoma and nonmelanoma skin cancer." | verified | full_quote | Tier 5 (government) |
| B4 | PMC 2022 expert panel: sunscreen does not limit vitamin D production in real-world use | PMC — Sunscreen and Vitamin D Expert Panel (2022) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9002342/ | "Sunscreens can be effective in preventing erythema from solar exposure without limiting the benefits with respect to vitamin D production." | verified | full_quote | Tier 5 (government) |
| B5 | Skin Cancer Foundation: ~90% of nonmelanoma skin cancers associated with UV exposure | Skin Cancer Foundation — Skin Cancer Facts & Statistics | https://www.skincancer.org/skin-cancer-information/skin-cancer-facts/ | "About 90 percent of nonmelanoma skin cancers are associated with exposure to ultraviolet (UV) radiation from the sun." | verified | full_quote | Tier 2 (unknown) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — American Academy of Dermatology**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B2 — MD Anderson Cancer Center**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B3 — PMC / CMAJ (2020)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B4 — PMC Sunscreen & Vitamin D Expert Panel (2022)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B5 — Skin Cancer Foundation**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

All five citations verified via full quote match on live page fetch. No citation failures. No impact notes required.

*Source: proof.py JSON summary*

---

## Computation Traces

```
  Date: 2026-03-31 (System date matches proof generation date)

Verifying citations...
  [✓] source_aad: Full quote verified for source_aad (source: tier 2/unknown)
  [✓] source_mdanderson: Full quote verified for source_mdanderson (source: tier 2/unknown)
  [✓] source_pmc_cmaj: Full quote verified for source_pmc_cmaj (source: tier 5/government)
  [✓] source_pmc_vitd: Full quote verified for source_pmc_vitd (source: tier 5/government)
  [✓] source_skincancer: Full quote verified for source_skincancer (source: tier 2/unknown)
  Confirmed sources: 5 / 5
  verified disproof sources vs threshold: 5 >= 3 = True
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

| Description | Sources Consulted | Sources Verified |
|-------------|-------------------|-----------------|
| Multiple independent authoritative institutions consulted | 5 | 5 |

**Verification status by source:**

| Source Key | Status |
|-----------|--------|
| source_aad | verified |
| source_mdanderson | verified |
| source_pmc_cmaj | verified |
| source_pmc_vitd | verified |
| source_skincancer | verified |

**Independence note:** Sources span distinct institution types: professional medical association (AAD), major cancer research and treatment center (MD Anderson), peer-reviewed academic literature (PMC/CMAJ 2020), international expert consensus panel (PMC 2022), and an independent cancer prevention foundation (Skin Cancer Foundation). All five are institutionally independent with no shared authorship. The two PMC citations (B3, B4) alone exceed the threshold of 3 when combined with any one other verified source.

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

**Check 1 — FDA absorption studies as potential support for the claim**
- Question: Does the FDA's own research confirm that sunscreen chemicals are absorbed, potentially supporting the danger claim?
- Verification performed: Searched for 'FDA sunscreen chemical absorption oxybenzone bloodstream JAMA 2019 2020'. Found two FDA-sponsored JAMA studies (2019 and 2020) confirming that oxybenzone and other ingredients are absorbed into the bloodstream at concentrations exceeding the FDA threshold of 0.5 ng/mL. Oxybenzone reached up to 258.1 ng/mL and remained detectable for up to 21 days. However, both study authors explicitly stated: 'These findings do not indicate that individuals should refrain from the use of sunscreen.' The FDA called for more research but did not conclude harm.
- Finding: FDA studies confirm absorption is real (oxybenzone up to 258 ng/mL, persisting 21 days), but the studies' own authors explicitly state this does not mean sunscreen should be avoided. Absorption documented; harm from that absorption: not demonstrated.
- Breaks proof: **No**

**Check 2 — Oxybenzone endocrine disruption in humans**
- Question: Is there evidence that oxybenzone or other absorbed chemicals disrupt hormones or cause cancer in humans at realistic exposure levels?
- Verification performed: Searched for 'oxybenzone endocrine disruptor humans evidence cancer realistic exposure'. Harvard Health and NYP/Weill Cornell both report that studies showing hormone disruption used concentrations equivalent to approximately 277 years of daily sunscreen application. Human volunteer studies confirmed no biologically significant alterations in reproductive hormones at real-world exposure levels. Oxybenzone has been in use since 1978 with no demonstrated human carcinogenicity.
- Finding: Animal-model endocrine effects require ~277 years of equivalent daily human use. Human studies show no biologically significant reproductive hormone changes. No human carcinogenicity has been demonstrated after decades of use.
- Breaks proof: **No**

**Check 3 — Clinically significant vitamin D deficiency from sunscreen**
- Question: Does sunscreen use lead to clinically significant vitamin D deficiency in real-world populations?
- Verification performed: Searched for 'sunscreen vitamin D deficiency real world population studies clinical'. PMC 2022 expert panel found that population studies of outdoor individuals (vacationers) showed vitamin D levels 'did not seem to differ between those applying sunscreen and those who did not, with exposure time and body surface area exposed being equivalent.' Real-world sunscreen application is typically incomplete; shorter UVB wavelengths that drive vitamin D synthesis are also attenuated by the ozone layer, partially compensating. The Skin Cancer Foundation recommends dietary sources and supplements as the safe route to vitamin D rather than UV exposure.
- Finding: Real-world population studies show no significant difference in vitamin D levels between sunscreen users and non-users given equivalent outdoor exposure time. Laboratory-controlled reductions do not translate to clinically meaningful deficiency in practice. Dietary supplementation is the recommended and safe vitamin D source.
- Breaks proof: **No**

**Check 4 — Peer-reviewed support for the direct claim**
- Question: Are there peer-reviewed studies directly concluding that sunscreen is more dangerous than moderate unprotected sun exposure on a net-harm basis?
- Verification performed: Searched for 'sunscreen more dangerous sun exposure net harm peer reviewed evidence'. Harvard Health explains that studies where sunscreen users appeared to have higher cancer rates reflect behavioral confounding: people who use more sunscreen tend to spend more time in the sun, reversing the causal arrow. MD Anderson, AAD, and the Skin Cancer Foundation all explicitly reject the conclusion that sunscreen causes net harm exceeding sun exposure. No peer-reviewed study was found concluding sunscreen use causes greater net harm than moderate unprotected sun exposure.
- Finding: No peer-reviewed studies support this conclusion. The observed correlation is reversed causation: higher-sunscreen users get more sun, not cancer from sunscreen. All major medical institutions — AAD, MD Anderson, Skin Cancer Foundation, CDC — explicitly reject the claim.
- Breaks proof: **No**

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | aad.org | unknown | 2 | Unclassified domain — verify source authority manually. The American Academy of Dermatology is the largest dermatological professional organization in the United States and a primary standard-setter for dermatological care. |
| B2 | mdanderson.org | unknown | 2 | Unclassified domain — verify source authority manually. MD Anderson Cancer Center is a National Cancer Institute-designated Comprehensive Cancer Center and one of the leading cancer research and treatment institutions in the world. |
| B3 | nih.gov | government | 5 | Government domain (.gov). PubMed Central (PMC) is the open-access archive of the U.S. National Institutes of Health. The underlying article is published in CMAJ (Canadian Medical Association Journal), a peer-reviewed medical journal. |
| B4 | nih.gov | government | 5 | Government domain (.gov). PubMed Central (PMC); underlying article is an international expert consensus panel review. |
| B5 | skincancer.org | unknown | 2 | Unclassified domain — verify source authority manually. The Skin Cancer Foundation is the leading international organization dedicated to skin cancer prevention, with an independent photobiology advisory committee. |

*Source: proof.py JSON summary*

Note on tier-2 sources: The automated credibility system classifies domains by allowlist membership, not institutional authority. The three tier-2 sources (AAD, MD Anderson, Skin Cancer Foundation) are among the most authoritative institutions in dermatology and oncology. Their tier-2 classification reflects only that their domains are not in the automated allowlist. The disproof conclusion is independently supported by the two tier-5 (NIH/PMC) sources (B3, B4), which alone provide two of the three required verified sources.

*Source: author analysis*

---

## Extraction Records

For this qualitative/consensus disproof proof, extraction records capture citation verification status rather than numeric values.

| Fact ID | Extracted Value (Citation Status) | Counts Toward Threshold | Quote Snippet (first 80 chars) |
|---------|----------------------------------|------------------------|-------------------------------|
| B1 | verified | Yes | "Just because an ingredient is absorbed into the bloodstream does not mean that i" |
| B2 | verified | Yes | "There is no medical evidence that sunscreen causes cancer. However, there is a l" |
| B3 | verified | Yes | "High-quality evidence has shown that sunscreen reduces the risk of developing bo" |
| B4 | verified | Yes | "Sunscreens can be effective in preventing erythema from solar exposure without l" |
| B5 | verified | Yes | "About 90 percent of nonmelanoma skin cancers are associated with exposure to ult" |

Extraction method: Citation verification status (verified/partial/not_found/fetch_failed) is assigned by `verify_all_citations()` in `scripts/verify_citations.py`. For qualitative proofs, this status serves as the "extracted value" — a source counts toward the disproof threshold if and only if its quote was found on the live page (status = "verified" or "partial"). All five sources returned "verified" via full_quote match on live fetch.

*Source: proof.py JSON summary + author analysis*

---

## Hardening Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Rule 1: Every empirical value parsed from quote text, not hand-typed | N/A — qualitative proof; no numeric values extracted from quotes | Qualitative consensus proof; citation status is the "value" |
| Rule 2: Every citation URL fetched and quote checked | PASS | All 5 citations verified via `verify_all_citations()` — full_quote match, live fetch |
| Rule 3: System time used for date-dependent logic | PASS | `date.today()` used; PROOF_GENERATION_DATE cross-checked against system date |
| Rule 4: Claim interpretation explicit with operator rationale | PASS | `CLAIM_FORMAL` with `operator_note` documents both mechanisms, comparative harm interpretation, and threshold rationale |
| Rule 5: Adversarial checks searched for independent counter-evidence | PASS | 4 adversarial searches conducted: FDA absorption studies, oxybenzone endocrine disruption, vitamin D deficiency in populations, direct peer-reviewed support |
| Rule 6: Cross-checks used independently sourced inputs | PASS | 5 sources from distinct institutions (AAD, MD Anderson, CMAJ, PMC expert panel, Skin Cancer Foundation) — no shared authorship |
| Rule 7: Constants and formulas imported from computations.py, not hand-coded | PASS | `compare()` used for claim evaluation; no hard-coded constants or inline formulas |
| validate_proof.py | PASS | 15/15 checks passed, 0 issues, 0 warnings |

*Source: author analysis*

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-03-31.*
