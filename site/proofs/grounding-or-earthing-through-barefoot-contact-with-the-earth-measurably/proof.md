# Proof: Grounding or earthing through barefoot contact with the Earth measurably reduces inflammation and improves recovery and sleep.

- **Generated:** 2026-04-01
- **Verdict:** PARTIALLY VERIFIED
- **Audit trail:** [proof_audit.md](proof_audit.md) · [proof.py](proof.py)

---

## Key Findings

- **SC1 (inflammation) — HOLDS:** 2 of 2 qualifying sources confirmed earthing's association with reduced inflammation biomarkers (CRP, cytokines, white blood cells). Sources: Chevalier 2015 PMC review (partial, COI) + post-surgical RCT 2025 (verified, non-COI).
- **SC2 (recovery) — HOLDS:** 2 of 2 qualifying sources confirmed earthing's association with improved physical recovery markers (creatine kinase, VAS pain score). Sources: post-surgical RCT 2025 (verified, non-COI) + bodyworkers RCT 2018 (partial, COI).
- **SC3 (sleep) — FAILS:** The only qualifying source (ScienceDirect 2025 sleep RCT, n=60) returned HTTP 403 and could not be verified. 0 of 1 sources verified; threshold of 2 not met. Additionally, no second qualifying sleep source (n≥30, non-COI) was found in the literature.
- **SC4 (causation) — FAILS:** Only 1 of 2 required qualifying RCTs was verified (post-surgical, n=42). The sleep RCT (n=60, ScienceDirect) returned HTTP 403. Additionally, a systematic review found that "the few studies with robust methodologies found no evidence of health benefits," and a 2015 study failed to replicate 2010 positive DOMS findings.

---

## Claim Interpretation

**Natural-language claim:** Grounding or earthing through barefoot contact with the Earth measurably reduces inflammation and improves recovery and sleep.

**Formal interpretation:** This is a compound causal claim decomposed into four sub-claims per the skill's causal-claim guidelines. The claim uses the word "reduces/improves" (causal language), requiring both an association sub-claim and a causation sub-claim per each outcome.

| Sub-claim | Description | Threshold | Operator note |
|-----------|-------------|-----------|---------------|
| SC1 | Earthing associated with reduced inflammation biomarkers (CRP, cytokines, WBC) | ≥ 2 qualifying sources | Threshold reduced from 3: domain scarcity + COI gate (max 1 COI source counts) + n≥30 quality gate |
| SC2 | Earthing associated with improved recovery markers (creatine kinase, VAS pain, DOMS) | ≥ 2 qualifying sources | Same rationale as SC1 |
| SC3 | Earthing associated with improved sleep quality (PSQI, ISI, sleep duration) | ≥ 2 qualifying sources | Same rationale; only 1 qualifying source found |
| SC4 | Associations established by RCT-level evidence (randomized, placebo-controlled) | ≥ 2 qualifying RCTs | Threshold=2 per domain scarcity; blinding imperfect |

**"Measurably"** is interpreted as requiring objective biomarker or validated-instrument evidence (not solely self-report) from studies with n≥30 participants.

**COI constraint:** The dominant earthing research group (Chevalier, Oschman, Sinatra) holds equity in EarthFx Inc. and runs the Earthing Institute. No more than 1 COI-affiliated source counts toward any sub-claim threshold.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|---------|
| B1 | SC1: Chevalier 2015 PMC review — earthing and inflammation biomarkers (COI source) | Partial (fragment match, 50% coverage — PMC inline reference markers inject noise) |
| B2 | SC1: Post-surgical earthing RCT 2025 (n=42) — CRP reduction | Yes |
| B3 | SC2: Post-surgical earthing RCT 2025 (n=42) — creatine kinase and pain recovery | Yes |
| B4 | SC2: Bodyworkers grounding RCT 2018 — pain and physical function (COI source) | Partial (fragment match, 54.5% coverage) |
| B5 | SC3: Earthing mat sleep quality RCT 2025 (n=60) — PSQI/ISI indices | No (HTTP 403 — ScienceDirect paywall) |
| B6 | SC4 causation: Post-surgical RCT 2025 (n=42) — RCT design evidence | Yes |
| B7 | SC4 causation: Sleep quality RCT 2025 (n=60) — RCT design evidence | No (HTTP 403 — ScienceDirect paywall) |
| A1 | SC1 qualifying source count (verified+partial) | Computed: 2 qualifying sources confirmed |
| A2 | SC2 qualifying source count (verified+partial) | Computed: 2 qualifying sources confirmed |
| A3 | SC3 qualifying source count (verified+partial) | Computed: 0 qualifying sources confirmed (fetch failed) |
| A4 | SC4 qualifying RCT count (verified+partial) | Computed: 1 qualifying RCT confirmed (1 fetch failed) |

*Source: proof.py JSON summary*

---

## Proof Logic

### SC1: Inflammation Association

The Chevalier et al. 2015 PMC review (B1) provides a broad synthesis stating that earthing produces "measurable differences in the concentrations of white blood cells, cytokines, and other molecules involved in the inflammatory response." This source has a partial citation match (50% coverage) due to inline HTML reference markers on the PMC page disrupting string matching — the key claim is still present. This is the 1 allowed COI source (Chevalier and Oschman hold equity in EarthFx Inc.).

The post-surgical RCT 2025 (B2, n=42) provides the required non-COI qualifying source. The study states that "Earthing after spinal surgery seems to promote recovery by reducing inflammation and pain, and accelerating general healing" — confirmed with full quote verification. This is a PMC-hosted open-access publication.

With 2 qualifying sources confirmed (1 COI + 1 non-COI), SC1 meets its threshold of 2.

### SC2: Recovery Association

The same post-surgical RCT (B3, same paper as B2) is used here to confirm recovery-specific outcomes. The paper reports creatine kinase reduction and VAS pain score improvement alongside CRP reduction — the same source provides independent evidence for both the inflammation outcome (SC1) and the recovery outcome (SC2), since these are distinct clinical endpoints. Quote verified.

The bodyworkers RCT 2018 (B4), which found "consistent beneficial effects of grounding in pain, physical function, and mood," provides the 1 allowed COI source for SC2 (lead author Chevalier, Earthing Institute). Citation is partial at 54.5% coverage.

With 2 qualifying sources confirmed (1 COI + 1 non-COI), SC2 meets its threshold of 2.

### SC3: Sleep Association — FAILS

The qualifying evidence rests solely on the 2025 sleep RCT (B5, n=60, ScienceDirect), which reported that "total sleep time was significantly increased compared to controls." However, this URL returned HTTP 403 (ScienceDirect paywall restriction on automated fetch), so the citation could not be verified. Wayback Machine fallback was attempted but unavailable.

Even if the URL were accessible, SC3 would fail: the threshold requires ≥2 qualifying sources, but only one qualifying sleep study (n≥30, non-COI, independent of the COI group) was found in the literature. The Ghaly and Teplitz 2004 study (n=12) was excluded for failing the n≥30 quality gate.

### SC4: Causation — FAILS

SC4 requires ≥2 verified RCTs to establish causal attribution beyond mere association. The post-surgical RCT (B6) is verified (full quote confirmed). The sleep quality RCT (B7) returned HTTP 403, leaving only 1 of 2 required RCTs verified.

Moreover, serious concerns constrain SC4 even if both RCTs had been verifiable: (a) a 2015 replication study found no significant differences where the 2010 DOMS study found benefits; (b) a systematic review (PCOM) found that "the few studies with robust methodologies found no evidence of health benefits"; (c) blinding is imperfect in grounding studies, as participants may detect skin sensations. SC4 cannot be established under current evidence regardless of the verification outcome.

---

## Counter-Evidence Search

Five adversarial searches were conducted:

1. **2015 replication failure (DOMS):** Confirmed. Africa Check documented that a 2015 study failed to replicate the 2010 DOMS earthing findings. This applies to the Chevalier study line specifically, not directly to the newer 2025 RCTs, but raises broader reproducibility concerns.

2. **Physics-based critique:** Confirmed. Science-Based Medicine argues that "from the perspective of basic physics, earthing makes no sense" — electrons are fungible, and Earth electrons are not biologically unique. This challenges the proposed mechanism but does not directly override RCT findings, which could reflect placebo effects or unknown mechanisms.

3. **Pervasive COI:** Confirmed. Four of five major earthing studies share authors with financial ties to EarthFx Inc. (Chevalier, Oschman, Sinatra). This is the most structurally significant weakness of the evidence base. The proof's COI gate limits this by requiring at least 1 non-COI source per sub-claim.

4. **Systematic review — negative for robust studies:** Confirmed. A PCOM systematic review found that methodologically robust studies found no health benefits from grounding. This predates the 2025 RCTs but establishes a concerning pattern: improved methodology tends to reduce observed effects.

5. **No large-scale independent RCTs:** Confirmed. No RCT with n>100 from a group unaffiliated with the earthing industry was found. The entire evidence base consists of small-to-medium studies.

None of the adversarial findings forced an UNDETERMINED verdict on their own, but collectively they substantially limit the confidence that SC4 (causation) can be established, even beyond the verification failure.

---

## Conclusion

**Verdict: PARTIALLY VERIFIED**

**Sub-claims that HOLD:** SC1 (inflammation association) and SC2 (recovery association) each met the threshold of 2 qualifying confirmed sources (1 COI + 1 non-COI per sub-claim). The post-surgical RCT 2025 (n=42, PMC) is the pivotal non-COI source for both.

**Sub-claims that FAIL:**

- **SC3 (sleep)** — failed for two independent reasons: (1) the sole qualifying source (ScienceDirect sleep RCT 2025, n=60) could not be fetched due to HTTP 403 (paywall), and (2) no second qualifying sleep source (n≥30, non-COI) was found in the literature. Even with the ScienceDirect paper verified, SC3 would still fail the threshold of 2.

- **SC4 (causation)** — failed because only 1 of 2 required qualifying RCTs was verified (the sleep RCT returned HTTP 403). Additionally, independent of the verification failure, the causation claim is materially undermined by: (a) a confirmed 2015 replication failure of earlier earthing findings, (b) a systematic review finding no benefit in methodologically robust studies, and (c) imperfect blinding in all earthing RCTs.

**What would be needed to change this verdict:**
- SC3: A second qualifying sleep study (n≥30, from authors without commercial ties to earthing companies) would be needed, plus successful verification of the 2025 sleep RCT.
- SC4: ≥2 independently verified, high-quality RCTs (n≥30, non-COI) showing consistent effects across different laboratories and study designs, addressing the replication failure and systematic review concerns.

Note: B5 and B7 (ScienceDirect, Tier 4/academic) could not be fetched due to paywall restrictions. B1 and B4 received partial citation matches (50% and 54.5% coverage respectively), consistent with the academic HTML noise pattern on PMC and PubMed abstract pages.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
