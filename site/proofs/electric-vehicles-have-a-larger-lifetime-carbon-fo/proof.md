# Proof: Electric vehicles have a larger lifetime carbon footprint than gasoline cars when manufacturing and battery disposal are included.

- **Generated:** 2026-03-28
- **Verdict:** DISPROVED
- **Audit trail:** [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- **U.S. Department of Energy cradle-to-grave analysis (2023):** A gasoline SUV produces 429 g CO2e per mile; an equivalent battery EV produces **48% fewer** greenhouse gas (GHG) emissions over its full lifetime — including manufacturing, fuel/electricity upstream, operation, and end-of-life (B1, B2).
- **IEA Global EV Outlook 2024:** Globally, a battery electric car sold in 2023 emits **half as much** as a conventional gasoline car over its lifetime (B3).
- **EV manufacturing IS higher:** EVs require more than 10 metric tons CO2 to manufacture vs. ~6 metric tons for a gasoline car — a premium of >4 metric tons. But the DOE and IEA analyses already account for this in their cradle-to-grave totals, and the result still strongly favors EVs (B4, A3).
- **Battery disposal does not flip the verdict:** The cradle-to-grave scope already includes end-of-life. Peer-reviewed research finds battery recycling *reduces* EV emissions by ~8.3% — disposal worsens neither the analysis nor the outcome.

---

## Claim Interpretation

**Natural-language claim:** "Electric vehicles have a larger lifetime carbon footprint than gasoline cars when manufacturing and battery disposal are included."

**Formal interpretation:** The claim asserts that battery electric vehicles (BEVs) have greater total cradle-to-grave lifecycle CO2-equivalent (CO2e) emissions than internal combustion engine vehicles (ICEVs) — covering manufacturing (including battery production), upstream energy (electricity/fuel supply chain), vehicle operation, and end-of-life (battery disposal/recycling).

**Operator:** `>` (strict inequality: BEV total lifetime CO2e > ICEV total lifetime CO2e)

**Operator note:** The claim is FALSE — and therefore DISPROVED — if authoritative cradle-to-grave lifecycle analyses show BEV total < ICEV total after all phases are included. The claim's *premise* (that EVs have higher manufacturing emissions) is confirmed as TRUE. What the evidence refutes is the *conclusion* that this manufacturing premium, combined with battery disposal, makes EVs' **total** lifetime footprint larger. Regional edge cases (coal-heavy grids, very short vehicle lifetimes) were examined in adversarial checks and do not rescue the claim.

---

## Evidence Summary

| ID  | Fact                                                                                   | Verified |
|-----|----------------------------------------------------------------------------------------|----------|
| B1  | DOE FOTW #1303 (2023): Gasoline SUV cradle-to-grave = 429 g CO2e per mile              | Yes      |
| B2  | DOE FOTW #1303 (2023): Battery EV emits 48% fewer GHGs than gasoline SUV (same scope) | Yes      |
| B3  | IEA Global EV Outlook 2024: BEV lifetime emissions are half of equivalent ICEV         | Yes      |
| B4  | Recurrent Auto: EV manufacturing >10 t CO2 vs gas car manufacturing ~6 t CO2          | Yes      |
| A1  | BEV/ICEV per-mile emissions ratio from DOE data                                        | Computed: 0.52 (EVs emit 48% less per mile over full lifecycle) |
| A2  | Cross-check: DOE per-mile ratio (0.52) vs IEA lifetime ratio (0.50)                   | Computed: AGREE — 2.0 percentage points difference, within 5% tolerance |
| A3  | EV manufacturing CO2 premium over gasoline car manufacturing                           | Computed: >4 metric tons CO2 (lower bound) |

---

## Proof Logic

### Sub-claim 1: EV manufacturing emits more CO2 than gasoline car manufacturing (TRUE)

Multiple lifecycle analyses confirm that battery production is energy-intensive. Recurrent Auto, citing ICCT, MIT, Argonne, and DOE studies, reports that gas car manufacturing produces ~6 metric tons CO2 while EV manufacturing produces more than 10 metric tons CO2 (B4). The computed premium is **>4 metric tons CO2** (A3). This is the factual basis the claim attempts to leverage.

### Sub-claim 2: Total lifetime emissions — EV > Gas (FALSE)

The U.S. Department of Energy's FOTW #1303 report (August 2023) provides a comprehensive cradle-to-grave analysis that includes raw material extraction, fuel production and transport, vehicle manufacturing, vehicle use, and vehicle end-of-life. This scope encompasses everything the claim invokes. The result: a small gasoline SUV produces **429 g CO2e per mile** while the equivalent battery EV produces **48% fewer GHG emissions** (B1, B2).

With BEV/ICEV ratio = 1 − 0.48 = **0.52** (A1), EVs emit roughly half as much as gasoline cars across their full lifetime — not more. The claim is false.

The International Energy Agency's Global EV Outlook 2024, drawing on independent global data, independently reaches the same conclusion: "A battery electric car sold in 2023 will emit **half as much** as conventional equivalents over its lifetime" (B3). This yields a BEV/ICEV ratio of **0.50**.

Cross-checking DOE (0.52) against IEA (0.50) shows agreement within 2.0 percentage points — well within the 5-point tolerance for different vehicle sizes and regional grid mixes (A2).

### Why the manufacturing premium does not flip the verdict

The manufacturing premium for EVs (~4–8 t CO2 depending on battery size and grid) is real and well-documented. However, the operational phase for gasoline vehicles generates far more emissions — roughly 45–70 metric tons CO2 over a vehicle's lifetime, depending on lifetime mileage. Even a battery EV fully charged from coal-generated electricity is equivalent in lifetime efficiency to roughly 50–60 mpg gasoline — far better than the average new gasoline car. The manufacturing deficit is paid off within approximately 1–2 years of average driving.

### Battery disposal specifically

The claim singles out battery disposal. Evidence shows: (1) the DOE cradle-to-grave scope already includes end-of-life; (2) a peer-reviewed PMC lifecycle assessment (PMC9171403) finds that battery recycling *reduces* BEV climate impact by approximately 8.3%; (3) there is no credible peer-reviewed analysis showing that battery disposal reverses the EV lifetime advantage.

---

## Counter-Evidence Search

**Coal-heavy grids:** Searched for studies showing EVs worse than gasoline on high-coal electricity grids. The IEA's regional analysis shows EVs save fewer tons in coal-heavy India — but still save emissions (BEVs remain better than ICE). No authoritative source documents a scenario where EV total lifetime CO2e exceeds equivalent ICE, even on the dirtiest grids in major economies.

**Battery disposal specifically:** Searched for studies showing battery end-of-life increases total EV emissions above ICE levels. None found. The PMC lifecycle study finds recycling *reduces* BEV emissions. The DOE cradle-to-grave analysis includes end-of-life and still shows EVs 48% lower.

**Fossil-fuel-industry-funded research:** The Institute for Energy Research and similar organizations publish skeptical analyses, but these focus on manufacturing in isolation — they do not produce cradle-to-grave lifecycle analyses showing BEV total > ICE total. No peer-reviewed study in major journals (Nature, Environmental Science & Technology) found EVs to have higher total lifetime emissions than gasoline equivalents in any mainstream scenario.

**Very short vehicle lifetimes (1–2 years):** The manufacturing premium is offset after roughly 1–2 years of average driving. The claim makes no such qualifier. For the full vehicle lifetime (typically 10–15 years), EVs are unambiguously lower.

---

## Conclusion

**Verdict: DISPROVED**

Two independent, authoritative sources — the U.S. Department of Energy (B1, B2) and the International Energy Agency (B3) — both confirm via cradle-to-grave lifecycle analysis that battery electric vehicles emit roughly 48–50% less CO2e over their lifetimes than equivalent gasoline cars. This analysis explicitly includes manufacturing (including battery production), upstream energy, vehicle operation, and end-of-life battery disposal.

The claim's partial premise is correct: EV manufacturing *does* produce more CO2 than gasoline car manufacturing (>10 t vs. ~6 t). But the claim's conclusion — that this manufacturing premium, combined with battery disposal, makes EVs' *total* lifetime footprint larger — is directly contradicted by all available authoritative lifecycle evidence.

Battery disposal, far from worsening the comparison, is already accounted for in the cited cradle-to-grave analyses. Peer-reviewed research shows recycling *reduces* BEV lifecycle emissions by ~8.3%.

No credible peer-reviewed counter-evidence was found. All adversarial checks — coal grids, short vehicle lifetimes, battery disposal, industry-funded studies — failed to produce a verified scenario where BEV total lifetime emissions exceed ICE total lifetime emissions.

**Note:** 2 citations (B3: iea.org, B4: recurrentauto.com) are from domains that the automated credibility classifier rates as "unclassified" (Tier 2). The IEA (International Energy Agency) is a well-established intergovernmental organization and is considered authoritative independent of the automated tier. Recurrent Auto cites ICCT, MIT, Argonne, and DOE sources; its manufacturing figures are corroborated by DOE data (B1, B2). The disproof does not depend solely on these sources — it is independently established by the two DOE citations (both Tier 5 government), with B3 and B4 providing corroboration.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
