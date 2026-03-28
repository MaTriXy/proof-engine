# Proof: Current global warming is primarily driven by natural climate cycles rather than human CO2 emissions.

- **Generated:** 2026-03-28
- **Verdict:** DISPROVED
- **Audit trail:** [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- Three independent authoritative sources (NOAA ×2, NASA) — all tier-5 government agencies — explicitly state that human greenhouse gas (GHG) emissions, not natural cycles, are the primary driver of current global warming. All three citations were verified live against the source pages (B1, B2, B3).
- NOAA states: *"Virtually all climate scientists agree that this increase in heat-trapping gases is the **main reason** for the 1.8°F (1.0°C) rise in global average temperature since the late nineteenth century."* (B1)
- NOAA further rules out natural alternatives: *"no other known climate influences have changed enough to account for the observed warming trend"* (B2).
- NASA, addressing solar activity directly, concludes: *"It is therefore **extremely unlikely** that the Sun has caused the observed global temperature warming trend over the past half-century."* (B3)
- Adversarial searches found no major scientific institution, national academy, or peer-reviewed paper from a mainstream research body claiming natural cycles are the *primary* (>50%) driver of current warming.

---

## Claim Interpretation

**Natural language claim:** Current global warming is primarily driven by natural climate cycles rather than human CO2 emissions.

**Formal interpretation:** The claim asserts that natural climate cycles (solar variability, volcanic activity, internal oscillations such as AMO/PDO/ENSO) collectively account for more than human CO2/GHG emissions in driving current warming — i.e., natural factors are the dominant or primary driver contributing more than any other single factor.

**Operator choice:** The disproof threshold is `n_confirmed >= 3` authoritative sources explicitly rejecting natural-cycle primacy. This means: 3 or more independently verified sources from major scientific institutions must state that human emissions, not natural cycles, are the primary driver. Using `>=` rather than `>` means exactly 3 verified sources is sufficient — this is the standard consensus-proof threshold. Fewer than 3 would be UNDETERMINED; zero verified sources would yield UNDETERMINED, not PROVED.

**Proof direction:** Disproof. The `empirical_facts` contain sources that *reject* the claim. When 3+ are verified, `claim_holds = True` triggers verdict `DISPROVED`.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | NOAA Climate.gov: Are humans causing global warming? — scientific consensus statement | Yes |
| B2 | NOAA Climate.gov: What evidence exists that humans are the main cause? — ruling out natural factors | Yes |
| B3 | NASA Science FAQ: Is the Sun causing global warming? — solar vs human attribution | Yes |
| A1 | Count of verified sources rejecting natural-cycle-primacy claim | Computed: 3 of 3 sources verified — threshold (3) met, claim DISPROVED |

*Source: proof.py JSON summary*

---

## Proof Logic

This is a consensus disproof: the claim is rejected by showing that the established scientific consensus — as documented by independent authoritative institutions — is the direct opposite of the claim.

**Source independence:** NOAA (National Oceanic and Atmospheric Administration) and NASA (National Aeronautics and Space Administration) are separate U.S. federal agencies with independent research programs, budgets, satellite measurement systems, and scientific staff. Two NOAA pages (B1, B2) and one NASA page (B3) were used, yielding institutionally independent corroboration.

**B1 — Scientific consensus on primary cause (NOAA):** NOAA states that "virtually all climate scientists agree" that increased GHGs are "the main reason" for the observed 1.0°C warming since the late nineteenth century. "Main reason" is a direct rejection of any natural factor as the primary driver.

**B2 — Ruling out natural factors (NOAA):** NOAA states that "no other known climate influences have changed enough to account for the observed warming trend." This explicitly rules out solar variability, volcanic activity, and other natural factors as sufficient explanations, and attributes causation "squarely to human activities."

**B3 — Solar activity specifically ruled out (NASA):** The claim refers to "natural climate cycles," of which the Sun is the most commonly cited candidate. NASA, using its own satellite measurements (since 1978), states that solar energy reaching Earth has followed the Sun's 11-year cycle "with no net increase since the 1950s," while temperatures have risen markedly — making it "extremely unlikely that the Sun has caused the observed global temperature warming trend over the past half-century." This directly addresses the solar-cycle variant of the claim.

**Logical chain:** If the primary driver of current warming were natural climate cycles (not human CO2), then (a) the scientific consensus would not be nearly unanimous, (b) natural factors would show an upward trend matching observed warming, and (c) no other known influences would need to be ruled out. All three conditions are contradicted by the verified evidence above.

---

## Counter-Evidence Search

Three adversarial checks were performed before writing the proof code:

**1. Peer-reviewed support for natural-cycle primacy:**
Searched for papers arguing solar or natural cycles are the *primary* driver (>50% attribution) of recent warming. Found Connolly et al. (2023, ScienceDirect) arguing solar forcing may be larger than IPCC estimates, and Heritage Foundation (2023) questioning temperature record reliability. Neither paper claims natural cycles are the primary driver — Connolly et al. argue for a larger-but-still-secondary solar contribution, while Heritage Foundation is a political advocacy organization, not a scientific research institution. NASA states GHG forcing since 1750 is "over 270 times greater than the slight extra warming coming from the Sun itself." No major scientific institution paper credibly claims natural cycles account for >50% of post-1950 warming.

**2. Internal variability (AMO, PDO, ENSO) as alternative:**
IPCC AR6 quantifies the contribution of natural (solar + volcanic) drivers at −0.1°C to +0.1°C over the period 1850–1900 to 2010–2019, while human drivers contributed 0.8°C to 1.3°C (best estimate 1.07°C). Internal oscillations (Atlantic Multi-decadal Oscillation, Pacific Decadal Oscillation, El Niño–Southern Oscillation) produce multi-decadal fluctuations but are zero-sum over century-scale periods and cannot produce a sustained monotonic warming trend. Attribution studies consistently show these cannot account for the long-term trend.

**3. Scientific community consensus:**
Reviewed Cook et al. (2013), which found 97% of climate science papers endorsing the human-caused warming consensus; Lynas et al. (2021), which found 99.9% consensus. Reviewed positions of NASA, NOAA, IPCC, WMO, American Meteorological Society, American Geophysical Union, and the Royal Society — all attribute primary warming to human GHG emissions. No national academy of sciences, meteorological organization, or major climate research institution supports the natural-cycle-primacy claim.

None of these adversarial checks break the proof.

---

## Conclusion

**Verdict: DISPROVED**

All three citations are fully verified from live tier-5 government sources (NOAA and NASA). The disproof does not depend on any unverified citations.

The claim that current global warming is *primarily driven by natural climate cycles rather than human CO2 emissions* is directly contradicted by the documented position of independent government scientific agencies (NOAA, NASA) and the broader scientific consensus. IPCC AR6 quantifies human warming contribution at 0.8°C–1.3°C vs natural factors at −0.1°C to +0.1°C. Adversarial searches found no credible scientific institution or peer-reviewed majority position supporting the claim.

The scientific debate concerns the exact magnitude of various human and natural forcings (e.g., aerosol cooling, solar contribution magnitude, cloud feedback sensitivity) — not the fundamental attribution of primary causation to human GHG emissions.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
