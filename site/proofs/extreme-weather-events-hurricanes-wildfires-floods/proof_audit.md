# Audit: Extreme weather events (hurricanes, wildfires, floods) have become dramatically more frequent and intense solely because of climate change.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Extreme weather events (hurricanes, wildfires, floods) |
| Property | Causal attribution of increased frequency and intensity |
| Operator | >= |
| Threshold | 3 (independent sources confirming non-climate drivers) |
| Proof direction | disprove |
| Operator note | The claim is a conjunction of SC1 (frequency increased), SC2 (intensity increased), SC3 (change is dramatic), SC4 (climate change is the sole cause). A conjunction is false when any conjunct is false. SC4 is the decisive falsifier. "Solely" is interpreted as "exclusively" per standard English (Merriam-Webster). Threshold 3 means 3 independent authoritative sources documenting non-climate drivers suffice to disprove SC4. SC1 is also only partially true: global hurricane frequency has not clearly increased (NOAA GFDL). |

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_gfdl | NOAA GFDL: Atlantic hurricane frequency partly driven by aerosol changes, not solely greenhouse gases |
| B2 | source_usgs | USGS: urbanization independently increases the size and frequency of floods |
| B3 | source_pnasnexus | PNAS Nexus: wildfire risk is a confluence of climate change AND development (WUI expansion) |
| B4 | source_ipcc | IPCC AR6 Ch.11: attribution cites greenhouse gases, aerosol emissions, AND land-use changes as separate human influences |
| A1 | (computed) | Count of independent sources confirming non-climate drivers of extreme weather |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Count of independent sources confirming non-climate drivers | count(citations with status in ('verified', 'partial')) = 4 | 4 |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | NOAA GFDL: hurricane frequency + aerosols | NOAA Geophysical Fluid Dynamics Laboratory (GFDL) | https://www.gfdl.noaa.gov/global-warming-and-hurricanes/ | "the increase in tropical storm frequency in the Atlantic basin since the 1970s has been at least partly driven by decreases in aerosols from human activity and volcanic forcing." | verified | full_quote | Tier 5 (government) |
| B2 | USGS: urbanization + flood frequency | U.S. Geological Survey (USGS) Fact Sheet FS-076-03 | https://pubs.usgs.gov/fs/fs07603/ | "Urbanization generally increases the size and frequency of floods and may expose communities to increasing flood hazards." | verified | full_quote | Tier 5 (government) |
| B3 | PNAS Nexus: wildfire + WUI confluence | PNAS Nexus — Wildfire risk management in the era of climate change (2024) | https://academic.oup.com/pnasnexus/article/3/5/pgae151/7665998 | "Wildfire risk lies in the confluence of climate change and development in the WUI" | verified | full_quote | Tier 4 (academic) |
| B4 | IPCC AR6: multiple human influences | IPCC AR6 Working Group I — Chapter 11 | https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-11/ | "Evidence of observed changes in extremes and their attribution to human influence (including greenhouse gas and aerosol emissions and land-use changes) has strengthened since AR5" | verified | full_quote | Tier 5 (government/intergovernmental) |

---

## Citation Verification Details

**B1 — NOAA GFDL**
- Status: `verified`
- Method: `full_quote`
- Fetch mode: `live`
- Coverage: N/A (full match)

**B2 — USGS**
- Status: `verified`
- Method: `full_quote`
- Fetch mode: `live`
- Coverage: N/A (full match)

**B3 — PNAS Nexus**
- Status: `verified`
- Method: `full_quote`
- Fetch mode: `wayback` (live Oxford Academic page returned access restrictions; Wayback Machine copy retrieved and verified)
- Coverage: N/A (full match)

**B4 — IPCC AR6**
- Status: `verified`
- Method: `full_quote`
- Fetch mode: `live`
- Coverage: N/A (full match)

All four citations are fully verified. No citations require "with unverified citations" qualifier in the verdict.

---

## Computation Traces

```
[✓] source_gfdl: Full quote verified for source_gfdl (source: tier 5/government)
[✓] source_usgs: Full quote verified for source_usgs (source: tier 5/government)
[✓] source_pnasnexus [wayback]: Full quote verified for source_pnasnexus (source: tier 4/academic)
[✓] source_ipcc: Full quote verified for source_ipcc (source: tier 5/government)
  Confirmed sources (non-climate drivers documented): 4 / 4
  SC4 disproof: verified sources confirming non-climate drivers >= 3: 4 >= 3 = True
```

---

## Independent Source Agreement (Rule 6)

| Check | Details |
|-------|---------|
| Sources consulted | 4 |
| Sources verified | 4 |
| Independence basis | Four distinct institutions: NOAA (federal agency), USGS (federal agency), PNAS Nexus (peer-reviewed journal, Oxford University Press), IPCC (intergovernmental scientific body). Each addresses a different event type (hurricanes, floods, wildfires, general attribution). The finding is not institution-specific. |
| source_gfdl | verified |
| source_usgs | verified |
| source_pnasnexus | verified |
| source_ipcc | verified |

**Independence note:** Two sources are US federal agencies (NOAA, USGS), which trace to the same government but are distinct agencies covering different domains. PNAS Nexus and IPCC are independent of both and of each other. The convergence across these four institutions is robust.

---

## Adversarial Checks (Rule 5)

**Check 1:** Does any mainstream scientific organization claim climate change is the *sole* cause?
- Searched: IPCC AR6 Chapter 11, NOAA, NASA, WMO statements for "solely", "only", "exclusively" attributing extreme weather to climate change
- Finding: No. All authoritative sources identify multiple drivers. IPCC AR6 explicitly lists greenhouse gases, aerosol emissions, AND land-use changes. No "solely" language found.
- Breaks proof: **No**

**Check 2:** Is SC1 (frequency increase) fully true for all three event types?
- Searched: NOAA GFDL global tropical cyclone frequency data
- Finding: Global hurricane COUNT has NOT clearly increased. NOAA GFDL: "global tropical cyclone frequency timeseries do not show evidence for significant rising trends." This is an additional independent reason the claim fails.
- Breaks proof: **No** (it further supports disproof, not the original claim)

**Check 3:** Could "solely" be charitably interpreted as "primarily"?
- Analysis: Merriam-Webster defines "solely" as "without another; only". Standard English gives no room for reinterpretation. "Primarily because of X" is a different and weaker claim.
- Finding: No charitable interpretation rescues the "solely" qualifier.
- Breaks proof: **No**

**Check 4:** Could aerosol forcing and land-use changes be indirect effects of climate change?
- Analysis: Aerosol reductions result from clean air legislation (independent policy choice). Urbanization is driven by population growth and economic development. WUI expansion results from residential development decisions. NOAA GFDL lists "aerosols from human activity" as a separate forcing category distinct from greenhouse gases.
- Finding: These are genuinely independent causal factors, not downstream consequences of greenhouse gas warming.
- Breaks proof: **No**

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | noaa.gov | government | 5 | NOAA Geophysical Fluid Dynamics Laboratory — leading U.S. hurricane-climate research center |
| B2 | usgs.gov | government | 5 | U.S. Geological Survey — authoritative federal source for hydrological data |
| B3 | oup.com | academic | 4 | Oxford University Press / PNAS Nexus — peer-reviewed scientific journal |
| B4 | ipcc.ch | government/intergovernmental | 5 | IPCC — the definitive intergovernmental scientific consensus body on climate |

All citations are Tier 4 or higher. No low-credibility sources were used.

---

## Extraction Records

For qualitative proofs, extractions record citation verification status rather than numeric values.

| ID | Extracted Value | Found in Quote | Quote Snippet |
|----|----------------|---------------|---------------|
| B1 | verified | Yes | "the increase in tropical storm frequency in the Atlantic basin since the 1970s h..." |
| B2 | verified | Yes | "Urbanization generally increases the size and frequency of floods and may expose..." |
| B3 | verified | Yes | "Wildfire risk lies in the confluence of climate change and development in the WU..." |
| B4 | verified | Yes | "Evidence of observed changes in extremes and their attribution to human influenc..." |

---

## Hardening Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Rule 1: Values parsed from quotes, not hand-typed | ✓ Pass | Qualitative proof — no numeric values extracted; citation verification status is computed, not hand-typed |
| Rule 2: Citations verified by fetching | ✓ Pass | All 4 citations verified via `verify_all_citations()` with `wayback_fallback=True` |
| Rule 3: System time anchored | ✓ Pass | `date.today()` used |
| Rule 4: Claim interpretation explicit | ✓ Pass | `CLAIM_FORMAL` with `operator_note` documents the conjunction structure and "solely" interpretation |
| Rule 5: Adversarial checks are independent | ✓ Pass | 4 adversarial checks covering: institutional language search, hurricane frequency data, linguistic analysis, indirect-causation argument |
| Rule 6: Cross-checks use independent inputs | ✓ Pass | 4 sources from 3 distinct institutional types (federal agency ×2, peer-reviewed journal, intergovernmental body), each covering a different event type |
| Rule 7: No hard-coded constants or formulas | ✓ Pass | `compare()` from `computations.py` used; no inline formulas |
| validate_proof.py | ✓ **PASS** | 15/15 checks passed, 0 issues, 0 warnings |

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
