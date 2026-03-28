# Proof: The climate has always changed — today's warming is not unusual or alarming.

- **Generated:** 2026-03-28
- **Verdict:** PARTIALLY VERIFIED
- **Audit trail:** [proof_audit.md](proof_audit.md) · [proof.py](proof.py)

---

## Key Findings

- **SC1 — PROVED (with unverified citations):** Earth's climate has indeed changed throughout history. Natural glacial-interglacial cycles on roughly 100,000-year timescales are well-documented, driven by solar, volcanic, and orbital forcings (B1, B2).
- **SC2 — DISPROVED:** Today's warming is *not* within natural variability bounds. 4 independent authoritative sources (IPCC, NASA, NOAA — three separate organizations) confirm that current changes are unprecedented in thousands to hundreds of thousands of years (B3, B4, B5, B6).
- **CO2 is at 422.7 ppm** — higher than at any point in the 800,000-year ice-core record, which shows CO2 never exceeded 300 ppm during any prior interglacial (B5).
- **2024 global temperature** was 1.47°C above the 1850–1900 pre-industrial baseline (B4), and the warming rate over the last 50 years is described as "unprecedented" by NOAA (B6).

---

## Claim Interpretation

**Natural language claim:** "The climate has always changed — today's warming is not unusual or alarming."

This is a compound claim joined by "—" (used rhetorically to imply: *because* climate has always changed, today's warming is not unusual). The proof engine evaluates the two sub-claims independently:

| Sub-claim | Formal property | Direction | Threshold |
|-----------|----------------|-----------|-----------|
| SC1 | Earth's climate has undergone documented natural changes throughout geological history | Affirm | ≥ 2 verified sources |
| SC2 | Today's warming is not unusual or alarming (i.e., falls within natural variability) | Disprove | ≥ 3 sources contradicting it |

**SC1 operator note:** SC1 is universally accepted — natural climate variability is real and well-documented. True if at least 2 independent authoritative sources confirm natural climate cycles and forcings.

**SC2 operator note:** SC2 is the contentious part. A disproof requires at least 3 independent authoritative sources establishing that current warming *is* unprecedented — directly contradicting the "not unusual" assertion. Threshold of 3 chosen because three separate independent institutions (IPCC, NASA, NOAA) all publish authoritative data on this. If threshold is met, SC2 is DISPROVED.

**Compound logic:** Both sub-claims must hold for the compound claim to be PROVED. If SC1 is proved but SC2 is disproved, the verdict is PARTIALLY VERIFIED: the climate does indeed always change, but that historical variability does not imply today's warming is within natural bounds.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|---------|
| B1 | SC1: NOAA Climate.gov Q&A — natural glacial-interglacial cycles on 100,000-year timescales | Yes |
| B2 | SC1: NOAA NCEI — natural climate forcing mechanisms (solar and volcanic) | Partial (aggressive normalization — quote text present but required alphanumeric stripping) |
| B3 | SC2 disproof: IPCC AR6 (2021) — current changes unprecedented in thousands of years | Yes |
| B4 | SC2 disproof: NASA Earth Observatory — 2024 was 1.47°C above pre-industrial baseline | Yes |
| B5 | SC2 disproof: NOAA Climate.gov — atmospheric CO2 higher than any point in human history | Yes |
| B6 | SC2 disproof: NOAA NCEI — temperatures increased at unprecedented rate over 50 years | Yes |
| A1 | SC1: confirmed source count (natural variability) | Computed: 2 independent sources confirmed |
| A2 | SC2: confirmed disproof source count (warming IS unusual) | Computed: 4 independent sources confirmed warming IS unusual |

---

## Proof Logic

### SC1: Climate Has Always Changed

Earth has a 4.5-billion-year history of climate change. NOAA Climate.gov (B1) confirms that natural glacial-interglacial cycles have occurred "on roughly 100,000-year cycles for at least the last 1 million years," driven by Milankovitch orbital variations. NOAA NCEI (B2) confirms that natural forcings — including solar and volcanic activity — drive climate variability. Both sources are from the same upstream authority (NOAA), independently published. SC1 is **proved** (2/2 sources, threshold met).

### SC2: Is Today's Warming "Not Unusual or Alarming"?

The disproof draws on four converging lines of evidence from three independent institutions:

1. **Rate:** IPCC AR6 (B3) — the world's most comprehensive climate assessment, drawing on 14,000+ scientific papers by 234 scientists from 65 countries — states that "many of the changes observed in the climate are unprecedented in thousands, if not hundreds of thousands of years."

2. **Temperature magnitude:** NASA Earth Observatory (B4) documents that global temperature in 2024 was 1.47°C above the 1850–1900 pre-industrial average — the warmest year in the 145-year instrumental record, exceeding the 1.5°C Paris Agreement threshold for the first time on an annual basis.

3. **Atmospheric CO2:** NOAA (B5) documents that atmospheric CO2 is now at 422.7 ppm — higher than at any point in recorded human history. Ice-core records show CO2 never exceeded 300 ppm across 800,000 years of glacial-interglacial cycles; we are now 40%+ above that ceiling.

4. **Rate of warming:** NOAA NCEI (B6) states that "temperatures have increased over the last 50 years at an unprecedented rate" — faster than any comparable 50-year period in at least the last 2,000 years (IPCC AR6 high confidence).

All four sources confirmed on live page fetch. The SC2 disproof threshold of 3 is met (4/4 sources, all verified). SC2 — "today's warming is not unusual or alarming" — is **disproved**.

### Logical Structure of the Compound Claim

The rhetorical form of the claim is: "Because the climate has always changed naturally (premise), today's warming is not unusual (conclusion)." This argument form is a non sequitur. The existence of past natural climate change does not bound the magnitude or rate of current change. IPCC AR6 explicitly addresses this: the natural forcings responsible for past climate cycles (orbital, solar, volcanic) are well-understood and cannot account for post-industrial warming.

---

## Counter-Evidence Search

**Medieval Warm Period (MWP, ~900–1200 AD):** The MWP is sometimes cited as evidence that modern warming is within natural bounds. Paleoclimate reconstructions (including IPCC AR6 WG1) show the MWP was a real regional event (predominantly North Atlantic/Europe) but that its global temperature was lower than today's. IPCC AR6 concludes with high confidence that the "global nature and magnitude of current warmth is unprecedented in the context of the last 2000 years." The MWP does not establish that today's warming is within natural bounds globally.

**Minority scientific views:** A small minority of climate scientists (Spencer, Curry, Lindzen) argue that natural variability plays a larger role than IPCC consensus states. However, none claim current warming falls within Holocene natural variability ranges. Spencer's UAH satellite dataset — the most frequently cited skeptic dataset — itself shows a warming trend of ~0.15°C/decade since 1979. Warming is unambiguous even on the most conservative measurement.

**Urban heat island (UHI) bias:** UHI is sometimes argued to be an artifact inflating surface temperature records. Berkeley Earth's independent analysis (Rohde et al. 2013) found UHI explains less than 0.1°C of the ~1.5°C observed warming. Ocean temperatures (unaffected by UHI) show the same trend, confirming the warming is real.

**Logical structure of the original claim:** The claim implicitly commits a non sequitur: natural past change does not imply current change is natural or within natural bounds.

None of these lines of counter-evidence break the disproof of SC2.

---

## Conclusion

**Verdict: PARTIALLY VERIFIED**

The compound claim is only half-true:

- **SC1 — PROVED (with unverified citations):** Earth's climate has always changed. Natural glacial-interglacial cycles and climate forcings are thoroughly documented. SC1 is true. (Note: B2 verified via aggressive normalization rather than exact match; B1 provides independent full verification of the same point.)

- **SC2 — DISPROVED:** Today's warming is *not* within natural variability bounds. Four independently verified sources from three separate institutions (IPCC, NASA, NOAA) establish that current changes — in temperature magnitude, warming rate, and CO2 concentration — are unprecedented on timescales of thousands to hundreds of thousands of years.

The rhetorical move of invoking historical climate change to dismiss current warming is a logical fallacy: the existence of past natural variability does not imply that all future changes are natural or unremarkable. The scientific evidence is clear that the current warming episode is qualitatively different in both rate and driver from the natural cycles SC1 documents.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
