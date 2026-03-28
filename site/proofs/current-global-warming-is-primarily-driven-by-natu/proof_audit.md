# Audit: Current global warming is primarily driven by natural climate cycles rather than human CO2 emissions.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| subject | Current global warming |
| property | primary driver is natural climate cycles (not human CO2 emissions) |
| operator | >= |
| threshold | 3 |
| proof_direction | disprove |
| operator_note | The claim asserts natural climate cycles are the PRIMARY driver of current warming — meaning they account for more than 50% (or more than human CO2) of observed warming. This is the disproof variant: we collect authoritative scientific sources that explicitly state the opposite — that human greenhouse gas emissions, not natural cycles, are the dominant driver. Threshold = 3 independent authoritative sources confirming this counter-position. 'Primary' interpreted as dominant/main driver contributing more than any other single factor. Sources from two independent U.S. government agencies (NOAA, NASA) plus IPCC-aligned statements. |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_noaa_humans | NOAA Climate.gov: Are humans causing global warming? — scientific consensus statement |
| B2 | source_noaa_evidence | NOAA Climate.gov: What evidence exists that humans are the main cause? — ruling out natural factors |
| B3 | source_nasa_sun | NASA Science FAQ: Is the Sun causing global warming? — solar vs human attribution |
| A1 | *(computed)* | Count of verified sources rejecting natural-cycle-primacy claim |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Count of verified sources rejecting natural-cycle-primacy claim | count(verified citations) = 3 | 3 |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | NOAA: scientific consensus on primary cause | NOAA Climate.gov — Are humans causing or contributing to global warming? | https://www.climate.gov/news-features/climate-qa/are-humans-causing-or-contributing-global-warming | "Virtually all climate scientists agree that this increase in heat-trapping gases is the main reason for the 1.8°F (1.0°C) rise in global average temperature since the late nineteenth century." | verified | full_quote | Tier 5 (government) |
| B2 | NOAA: ruling out natural climate influences | NOAA Climate.gov — What evidence exists that Earth is warming and humans are the main cause? | https://www.climate.gov/news-features/climate-qa/what-evidence-exists-earth-warming-and-humans-are-main-cause | "no other known climate influences have changed enough to account for the observed warming trend" | verified | full_quote | Tier 5 (government) |
| B3 | NASA: solar activity cannot explain warming trend | NASA Science — Is the Sun causing global warming? | https://science.nasa.gov/climate-change/faq/is-the-sun-causing-global-warming/ | "It is therefore extremely unlikely that the Sun has caused the observed global temperature warming trend over the past half-century." | verified | full_quote | Tier 5 (government) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — NOAA: Are humans causing global warming?**
- Status: `verified`
- Method: `full_quote`
- Coverage: N/A (full match)
- Fetch mode: `live`

**B2 — NOAA: What evidence exists that humans are the main cause?**
- Status: `verified`
- Method: `full_quote`
- Coverage: N/A (full match)
- Fetch mode: `live`

**B3 — NASA: Is the Sun causing global warming?**
- Status: `verified`
- Method: `full_quote`
- Coverage: N/A (full match)
- Fetch mode: `live`

All three citations verified on live pages. No unverified citations. No impact analysis needed.

*Source: proof.py JSON summary*

---

## Computation Traces

```
Verifying citations...
  [✓] source_noaa_humans: Full quote verified for source_noaa_humans (source: tier 5/government)
  [✓] source_noaa_evidence: Full quote verified for source_noaa_evidence (source: tier 5/government)
  [✓] source_nasa_sun: Full quote verified for source_nasa_sun (source: tier 5/government)
  Confirmed sources: 3 / 3
    source_noaa_humans: verified
    source_noaa_evidence: verified
    source_nasa_sun: verified
  verified source count vs threshold: 3 >= 3 = True
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

| Description | Sources Consulted | Sources Verified | Agreement |
|-------------|-------------------|------------------|-----------|
| Two independent U.S. government agencies (NOAA and NASA) with separate research programs both explicitly reject natural-cycle primacy and attribute current warming to human emissions. | 3 | 3 | All verified |

**Source statuses:**
- source_noaa_humans: verified
- source_noaa_evidence: verified
- source_nasa_sun: verified

**Independence note:** NOAA (National Oceanic and Atmospheric Administration) and NASA (National Aeronautics and Space Administration) are independent agencies with separate research budgets, staff, and measurement programs. Both positions are independently consistent with IPCC AR6 findings.

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

**Check 1: Peer-reviewed support for natural-cycle primacy**

- **Question:** Do any credible peer-reviewed papers argue that solar or natural cycles are the PRIMARY driver of recent warming (>50% attribution)?
- **Verification performed:** Searched 'solar cycles primary cause global warming peer-reviewed 2020 2021 2022 2023' and 'natural climate cycles primary cause warming attribution science'. Found Connolly et al. (2023, ScienceDirect) arguing solar forcing may be underestimated and Heritage Foundation (2023) questioning temperature record reliability. Examined NASA, NOAA, IPCC, WMO, American Meteorological Society, and Royal Society positions.
- **Finding:** No peer-reviewed paper from a major scientific institution credibly claims natural cycles account for >50% of post-1950 warming. Connolly et al. (2023) argue for a larger-than-IPCC solar contribution but still treat it as a secondary factor; Heritage Foundation is a political advocacy organization, not a scientific institution. NASA states the greenhouse gas warming forcing is 'over 270 times greater than the slight extra warming coming from the Sun itself over that same time interval' (since 1750).
- **Breaks proof:** No

**Check 2: Internal variability as alternative**

- **Question:** Could internal variability (AMO, PDO, ENSO) account for most of the observed long-term warming trend?
- **Verification performed:** Searched IPCC AR6 attribution findings on internal variability and reviewed attribution literature. IPCC AR6 SPM quantifies: natural (solar + volcanic) drivers changed temperature by −0.1°C to +0.1°C from 1850–1900 to 2010–2019; human drivers caused 0.8°C to 1.3°C (best estimate 1.07°C). Reviewed literature on AMO, PDO, and multi-decadal variability as alternative explanations.
- **Finding:** IPCC AR6 attributes −0.1°C to +0.1°C to natural (solar + volcanic) drivers vs 0.8°C–1.3°C to human drivers over the industrial era. Internal oscillations (AMO, PDO) produce multi-decadal fluctuations but cannot produce a sustained, monotonically increasing century-scale warming trend — they are zero-sum over long periods. Attribution studies consistently show these cannot explain the long-term trend.
- **Breaks proof:** No

**Check 3: Scientific community consensus**

- **Question:** Is there disagreement within the scientific community about whether CO2 or natural cycles drive current warming, such that the claim could be considered contested?
- **Verification performed:** Reviewed consensus surveys: Cook et al. (2013) found 97% of climate scientists endorsing human-caused warming consensus; Lynas et al. (2021) found 99.9% consensus in a literature survey. Reviewed positions of all major scientific organizations worldwide. Searched for any national academy of sciences or major meteorological organization that disputes human-forcing primacy.
- **Finding:** Multiple independent surveys of the peer-reviewed literature find 97–99.9% consensus that human activities are the dominant cause of recent warming. No national academy of sciences, meteorological organization, or major climate research institution supports the natural-cycle-primacy claim. The scientific debate concerns quantification details (exact percentages, cloud feedbacks, aerosol forcing magnitudes), not the direction of attribution.
- **Breaks proof:** No

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | climate.gov | government | 5 | Government domain (.gov) |
| B2 | climate.gov | government | 5 | Government domain (.gov) |
| B3 | nasa.gov | government | 5 | Government domain (.gov) |

All sources are Tier 5 (government). No low-credibility sources used.

*Source: proof.py JSON summary*

---

## Extraction Records

This is a qualitative consensus proof. No numeric values were extracted from quotes. The `extractions` field records citation verification status per source:

| Fact ID | Value (citation status) | Countable | Quote Snippet (first 80 chars) |
|---------|------------------------|-----------|-------------------------------|
| B1 | verified | Yes | "Virtually all climate scientists agree that this increase in heat-trapping gases" |
| B2 | verified | Yes | "no other known climate influences have changed enough to account for the observe" |
| B3 | verified | Yes | "It is therefore extremely unlikely that the Sun has caused the observed global t" |

*Source: proof.py JSON summary*

---

## Hardening Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Rule 1: Values parsed from quotes, not hand-typed | N/A | Qualitative proof — no numeric extraction |
| Rule 2: All citation URLs fetched and quotes verified | PASS | All 3 citations verified live (full_quote method) |
| Rule 3: System time used for date-dependent logic | N/A | No time-dependent computation in this proof |
| Rule 4: Claim interpretation explicit with operator rationale | PASS | CLAIM_FORMAL includes operator_note explaining threshold and operator choice |
| Rule 5: Adversarial checks searched for independent counter-evidence | PASS | 3 adversarial checks performed via web search before writing proof code |
| Rule 6: Cross-checks used independently sourced inputs | PASS | NOAA and NASA are independent agencies; 2 different NOAA pages used |
| Rule 7: Constants and formulas imported from computations.py | PASS | Only `compare()` used; no hand-coded constants |
| validate_proof.py | PASS | 15/15 checks passed, 0 issues, 0 warnings |

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
