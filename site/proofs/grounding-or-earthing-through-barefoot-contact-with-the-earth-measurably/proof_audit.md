# Audit: Grounding or earthing through barefoot contact with the Earth measurably reduces inflammation and improves recovery and sleep.

- **Generated:** 2026-04-01
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Grounding/earthing — direct electrical contact of the human body with the Earth surface |
| Compound operator | AND (all sub-claims must hold) |
| Proof direction | prove |
| SC1 property | SC-association (inflammation): earthing is associated with measurable reductions in objective inflammation biomarkers (e.g., CRP, cytokines, white blood cells) |
| SC1 threshold | ≥ 2 qualifying sources |
| SC1 operator_note | Threshold reduced from 3: domain scarcity (< 10 qualifying human controlled studies on PubMed); COI gate (Chevalier/Oschman/Sinatra hold equity in EarthFx Inc.); quality gate n≥30 |
| SC2 property | SC-association (recovery): earthing is associated with measurable improvements in physical recovery markers (e.g., creatine kinase, VAS pain score, DOMS) |
| SC2 threshold | ≥ 2 qualifying sources |
| SC2 operator_note | Same threshold reduction rationale as SC1; DOMS pilot (n=8) excluded by quality gate |
| SC3 property | SC-association (sleep): earthing is associated with measurable improvements in sleep quality (e.g., PSQI, ISI, actigraphy, sleep duration) |
| SC3 threshold | ≥ 2 qualifying sources |
| SC3 operator_note | Same threshold reduction rationale; only 1 qualifying source found (Ghaly & Teplitz 2004, n=12, excluded) |
| SC4 property | SC-causation: associations established by RCT-level evidence (randomized, placebo-controlled with sham-grounding arm) |
| SC4 threshold | ≥ 2 qualifying RCTs |
| SC4 operator_note | RCTs required per causal-claim guidelines; threshold=2 per domain scarcity; blinding imperfect; 2015 replication failure noted |
| Operator note | All four sub-claims must hold for PROVED; "measurably" requires objective biomarker evidence from n≥30 studies |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_review_coi | SC1: Chevalier 2015 PMC review — earthing and inflammation biomarkers (COI source) |
| B2 | sc1_surgery | SC1: Post-surgical earthing RCT 2025 (n=42) — CRP reduction |
| B3 | sc2_surgery | SC2: Post-surgical earthing RCT 2025 (n=42) — creatine kinase and pain recovery |
| B4 | sc2_bodyworkers_coi | SC2: Bodyworkers grounding RCT 2018 — pain and physical function (COI source) |
| B5 | sc3_sleep_rct | SC3: Earthing mat sleep quality RCT 2025 (n=60) — PSQI/ISI indices |
| B6 | sc4_surgery_rct | SC4 causation: Post-surgical RCT 2025 (n=42) — RCT design evidence |
| B7 | sc4_sleep_rct | SC4 causation: Sleep quality RCT 2025 (n=60) — RCT design evidence |
| A1 | — | SC1 qualifying source count (verified+partial) |
| A2 | — | SC2 qualifying source count (verified+partial) |
| A3 | — | SC3 qualifying source count (verified+partial) |
| A4 | — | SC4 qualifying RCT count (verified+partial) |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1 qualifying source count (verified+partial) | count(verified/partial sc1 citations) = 2 | 2 |
| A2 | SC2 qualifying source count (verified+partial) | count(verified/partial sc2 citations) = 2 | 2 |
| A3 | SC3 qualifying source count (verified+partial) | count(verified/partial sc3 citations) = 0 | 0 |
| A4 | SC4 qualifying RCT count (verified+partial) | count(verified/partial sc4 citations) = 1 | 1 |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1: Chevalier 2015 review — inflammation (COI) | PMC: Chevalier et al. 2015 — Earthing, Inflammation and Immune Response (COI) | https://pmc.ncbi.nlm.nih.gov/articles/PMC4378297/ | "Electrically conductive contact of the human body with the surface of the Earth produces measurable differences in the concentrations of white blood cells, cytokines, and other molecules involved in the inflammatory response." | Partial | fragment (50.0% coverage) | Tier 5 (government) |
| B2 | SC1: Post-surgical RCT 2025 (n=42) — CRP reduction | PMC/MDPI 2025 — Post-Spinal Surgery Earthing RCT (n=42) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12155732/ | "Earthing after spinal surgery seems to promote recovery by reducing inflammation and pain, and accelerating general healing" | Verified | full_quote | Tier 5 (government) |
| B3 | SC2: Post-surgical RCT 2025 (n=42) — recovery/pain | PMC/MDPI 2025 — Post-Spinal Surgery Earthing RCT (n=42) — recovery and pain outcomes | https://pmc.ncbi.nlm.nih.gov/articles/PMC12155732/ | "Earthing after spinal surgery seems to promote recovery by reducing inflammation and pain, and accelerating general healing" | Verified | full_quote | Tier 5 (government) |
| B4 | SC2: Bodyworkers grounding RCT 2018 (COI) | PubMed 2018 — Bodyworkers Grounding RCT (COI: Chevalier et al.) | https://pubmed.ncbi.nlm.nih.gov/30448083/ | "Consistent beneficial effects of grounding in pain, physical function, and mood" | Partial | fragment (54.5% coverage) | Tier 5 (government) |
| B5 | SC3: Sleep quality RCT 2025 (n=60) | ScienceDirect 2025 — Earthing mat sleep quality double-blind RCT (n=60) | https://www.sciencedirect.com/science/article/pii/S2212958825000059 | "Total sleep time was significantly increased compared to controls" | fetch_failed | — | Tier 4 (academic) |
| B6 | SC4: Post-surgical RCT 2025 — RCT design | PMC/MDPI 2025 — Post-Spinal Surgery Earthing RCT (n=42) — RCT design confirmation | https://pmc.ncbi.nlm.nih.gov/articles/PMC12155732/ | "Earthing after spinal surgery seems to promote recovery by reducing inflammation and pain, and accelerating general healing" | Verified | full_quote | Tier 5 (government) |
| B7 | SC4: Sleep quality RCT 2025 — RCT design | ScienceDirect 2025 — Sleep quality RCT (n=60) — RCT design confirmation | https://www.sciencedirect.com/science/article/pii/S2212958825000059 | "Total sleep time was significantly increased compared to controls" | fetch_failed | — | Tier 4 (academic) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

### B1 — sc1_review_coi
- **Status:** partial
- **Method:** fragment (50.0% coverage) — degraded result. PMC academic HTML embeds inline reference markers (`[1]`, superscripts) after HTML stripping, injecting noise into the string-matching window. The key claim is present but exact match fails.
- **Fetch mode:** live
- **Impact (partial, not full):** B1 is counted as a qualifying source because partial coverage ≥ 50% is accepted per skill rules. The COI constraint is noted in CLAIM_FORMAL; B1 counts as 1 of the 2 threshold sources (the allowed COI source). No independent conclusion depends solely on B1.

### B2 — sc1_surgery
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live

### B3 — sc2_surgery
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live

### B4 — sc2_bodyworkers_coi
- **Status:** partial
- **Method:** fragment (54.5% coverage) — PubMed abstract pages often embed navigation and sidebar text after HTML stripping, creating noise. The key phrase "consistent beneficial effects of grounding in pain, physical function, and mood" is present in partial form.
- **Fetch mode:** live
- **Impact (partial, not full):** B4 is counted as qualifying (partial ≥ 50%). B4 is the allowed COI source for SC2. No conclusion depends solely on B4.

### B5 — sc3_sleep_rct
- **Status:** fetch_failed
- **Method:** none (HTTP 403)
- **Fetch mode:** live; Wayback Machine fallback attempted but unavailable
- **Impact:** SC3's only source is unverified. SC3 fails (n_confirming=0 < threshold=2). The sleep sub-claim cannot be confirmed. This also contributes to SC4 failing.

### B6 — sc4_surgery_rct
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live

### B7 — sc4_sleep_rct
- **Status:** fetch_failed
- **Method:** none (HTTP 403)
- **Fetch mode:** live; Wayback Machine fallback attempted but unavailable
- **Impact:** SC4 has only 1 verified RCT (B6); the threshold of 2 is not met. SC4 fails.

*Source: proof.py JSON summary; impact analysis is author analysis*

---

## Computation Traces

```
[~] sc1_review_coi: Only 16/32 quote words matched for sc1_review_coi — partial verification only (source: tier 5/government)
[✓] sc1_surgery: Full quote verified for sc1_surgery (source: tier 5/government)
[✓] sc2_surgery: Full quote verified for sc2_surgery (source: tier 5/government)
[~] sc2_bodyworkers_coi: Only 6/11 quote words matched for sc2_bodyworkers_coi — partial verification only (source: tier 5/government)
[?] sc3_sleep_rct: Fetch failed for sc3_sleep_rct: HTTP 403 on https://www.sciencedirect.com/science/article/pii/S2212958825000059 (source: tier 4/academic)
[✓] sc4_surgery_rct: Full quote verified for sc4_surgery_rct (source: tier 5/government)
[?] sc4_sleep_rct: Fetch failed for sc4_sleep_rct: HTTP 403 on https://www.sciencedirect.com/science/article/pii/S2212958825000059 (source: tier 4/academic)
SC1: inflammation association (>= 2 verified sources, max 1 COI): 2 >= 2 = True
SC2: recovery association (>= 2 verified sources, max 1 COI): 2 >= 2 = True
SC3: sleep association (>= 2 verified sources, max 1 COI): 0 >= 2 = False
SC4: causation via RCTs (>= 2 verified RCT sources): 1 >= 2 = False
compound: all sub-claims hold: 2 == 4 = False
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

### SC1: Inflammation

| Description | Sources consulted | Sources verified |
|-------------|-------------------|-----------------|
| SC1: inflammation — independent sources consulted | 2 | 2 |

- `sc1_review_coi`: partial (Chevalier 2015 PMC review, COI)
- `sc1_surgery`: verified (post-surgical RCT 2025, non-COI)

**Independence note:** 1 COI review article + 1 non-COI primary RCT from distinct study contexts. The COI rule (max 1 COI per threshold) is respected.

### SC2: Recovery

| Description | Sources consulted | Sources verified |
|-------------|-------------------|-----------------|
| SC2: recovery — independent sources consulted | 2 | 2 |

- `sc2_surgery`: verified (post-surgical RCT 2025, non-COI; recovery and pain outcomes)
- `sc2_bodyworkers_coi`: partial (bodyworkers RCT 2018, COI)

**Independence note:** Post-surgical paper shared with SC1 — different clinical endpoints (CRP vs. creatine kinase/VAS). Treated as independent evidence for distinct outcomes.

### SC3: Sleep

| Description | Sources consulted | Sources verified |
|-------------|-------------------|-----------------|
| SC3: sleep — independent sources consulted | 1 | 0 |

- `sc3_sleep_rct`: fetch_failed (HTTP 403)

**Independence note:** Only 1 qualifying source exists for SC3; even with successful fetch, SC3 cannot meet threshold=2.

### SC4: Causation

| Description | Sources consulted | Sources verified |
|-------------|-------------------|-----------------|
| SC4: causation — qualifying RCTs consulted | 2 | 1 |

- `sc4_surgery_rct`: verified (post-surgical RCT 2025, n=42)
- `sc4_sleep_rct`: fetch_failed (HTTP 403)

**Independence note:** Both are the same papers as SC1/SC3 but confirming RCT design. Post-surgical (n=42) and sleep (n=60) are distinct study populations.

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

### Check 1: 2015 replication failure
- **Question:** Does a 2015 replication study directly contradict the foundational 2010 DOMS earthing findings?
- **Verification performed:** Searched for 'earthing grounding DOMS replication 2015 no effect contradiction'. Africa Check reported: "A 2010 study found large differences in inflammation and pain in earthing versus control groups, but a similar 2015 study found no significant differences."
- **Finding:** Confirmed: a direct replication attempt failed. This applies to the Chevalier DOMS study line, not directly to the 2025 post-surgical or sleep RCTs, which are newer and distinct. The replication failure raises broader reliability concerns but does not directly falsify the newer qualifying sources.
- **Breaks proof:** No

### Check 2: Physics-based critique
- **Question:** Do independent physicists or medical review bodies find earthing claims physically implausible?
- **Verification performed:** Searched for 'earthing grounding physics critique pseudoscience debunked'. Science-Based Medicine states: "From the perspective of basic physics, earthing makes no sense" and characterizes it as "clearly on the pseudoscience side."
- **Finding:** Confirmed: the antioxidant-electron transfer mechanism is disputed. Electrons are fungible; Earth electrons are not biologically unique. This challenges the proposed mechanism but does not override RCT findings. RCT effects could reflect placebo or unknown mechanisms.
- **Breaks proof:** No

### Check 3: Pervasive COI in authorship
- **Question:** Is the earthing research base predominantly authored by researchers with commercial COI?
- **Verification performed:** Searched for 'Chevalier Oschman Sinatra earthing conflict of interest EarthFx'. Africa Check and Science-Based Medicine both document financial ties to EarthFx Inc. Four of five major studies share these authors.
- **Finding:** Confirmed. The proof's COI gate (max 1 COI source per sub-claim) limits the impact. The 2025 qualifying sources appear independent of the COI group. However, the overall research tradition is shaped by the COI group, and independent replication is limited.
- **Breaks proof:** No

### Check 4: Systematic review — negative for robust studies
- **Question:** Do systematic reviews find that robust earthing studies show no health benefits?
- **Verification performed:** Searched for 'systematic review earthing grounding health benefits methodology'. A PCOM systematic review (referenced in Science-Based Medicine) states: "the majority of studies had significant methodological flaws, and the few studies with robust methodologies found no evidence of health benefits from grounding."
- **Finding:** Confirmed. This predates the 2025 RCTs, so newer studies are not captured. However, it establishes a pattern where improved methodology tends to reduce observed effects — a concerning pattern that contributes to SC4's failure even beyond the verification issue.
- **Breaks proof:** No

### Check 5: Absence of large independent RCTs
- **Question:** Are there large-scale independent RCTs (n > 100) from groups unaffiliated with the earthing industry?
- **Verification performed:** Searched for 'earthing grounding randomized controlled trial n>100 large scale independent NIH funded'. No large independent RCT found.
- **Finding:** No large independent RCT exists. The claim rests on a small, methodologically limited literature. This absence confirms the domain scarcity justification for threshold=2.
- **Breaks proof:** No

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | nih.gov | government | 5 | PMC hosting; Chevalier 2015 review. COI: authors hold equity in EarthFx Inc. Tier 5 reflects domain; COI is separately tracked. |
| B2 | nih.gov | government | 5 | PMC hosting of MDPI 2025 post-surgical RCT. No known COI flag for this paper. |
| B3 | nih.gov | government | 5 | Same paper as B2, different outcome focus. |
| B4 | nih.gov | government | 5 | PubMed abstract page for bodyworkers RCT. COI: Chevalier et al. authorship. |
| B5 | sciencedirect.com | academic | 4 | ScienceDirect 2025 sleep RCT; fetch failed (paywall). No known COI flag. |
| B6 | nih.gov | government | 5 | Same as B2/B3, confirming RCT design. |
| B7 | sciencedirect.com | academic | 4 | Same as B5; fetch failed (paywall). |

No cited source has tier ≤ 2. All sources are either government-hosted (nih.gov, Tier 5) or established academic publisher (sciencedirect.com, Tier 4). COI is tracked separately in CLAIM_FORMAL and operator_notes — it does not affect domain credibility tier.

*Source: proof.py JSON summary*

---

## Extraction Records

| Fact ID | Extracted value | Value in quote | Quote snippet |
|---------|----------------|----------------|---------------|
| B1 | partial | Yes (countable) | "Electrically conductive contact of the human body with the surface of the Earth " |
| B2 | verified | Yes (countable) | "Earthing after spinal surgery seems to promote recovery by reducing inflammation" |
| B3 | verified | Yes (countable) | "Earthing after spinal surgery seems to promote recovery by reducing inflammation" |
| B4 | partial | Yes (countable) | "Consistent beneficial effects of grounding in pain, physical function, and mood" |
| B5 | fetch_failed | No | "Total sleep time was significantly increased compared to controls" |
| B6 | verified | Yes (countable) | "Earthing after spinal surgery seems to promote recovery by reducing inflammation" |
| B7 | fetch_failed | No | "Total sleep time was significantly increased compared to controls" |

For this qualitative/consensus proof, `value` records citation verification status per source rather than a numeric extracted value. `value_in_quote` = True when status is verified or partial (countable toward threshold).

*Source: proof.py JSON summary*

---

## Hardening Checklist

- **Rule 1 — Every empirical value parsed from quote text, not hand-typed:** N/A — this is a qualitative proof; no numeric values are extracted from quotes. ✓ (auto-pass)
- **Rule 2 — Every citation URL fetched and quote checked:** `verify_all_citations()` called on all 7 empirical facts. 3 verified, 2 partial, 2 fetch_failed (HTTP 403 paywall). ✓ (verification executed; fetch failures documented)
- **Rule 3 — System time used for date-dependent logic:** `date.today()` called in generator block. No time-dependent claim evaluation in this proof. ✓
- **Rule 4 — Claim interpretation explicit with operator rationale:** `CLAIM_FORMAL` with `operator_note` for each of 4 sub-claims. Threshold reduction from 3→2 documented with domain scarcity, COI gate, and quality gate reasoning. ✓
- **Rule 5 — Adversarial checks searched for independent counter-evidence:** 5 adversarial checks performed via web search, covering replication failure, physics critique, COI, systematic review, and absence of large RCTs. All counter-evidence documented with explicit rebuttals. ✓
- **Rule 6 — Cross-checks used independently sourced inputs:** 4 sub-claim cross-checks documented. SC1 and SC2 each use 2 sources from different study contexts. SC3 has only 1 source (documented limitation). SC4 uses 2 distinct RCT papers. ✓ (with documented SC3 single-source limitation)
- **Rule 7 — Constants and formulas imported from computations.py:** `compare()` imported and used for all sub-claim and compound evaluations. No hand-coded formulas or constants. ✓
- **validate_proof.py result:** PASS with 2 warnings (SC3 has only 1 source — expected and documented by design). 0 issues.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
