# Audit: Electric vehicles have a larger lifetime carbon footprint than gasoline cars when manufacturing and battery disposal are included.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field           | Value |
|----------------|-------|
| Subject         | Battery electric vehicles (BEVs) vs. internal combustion engine vehicles (ICEVs) |
| Property        | Total cradle-to-grave lifecycle CO2e: manufacturing + upstream energy + vehicle operation + end-of-life |
| Operator        | `>` |
| Operator note   | Claim holds only if BEV total lifetime CO2e strictly exceeds ICEV total. DISPROVED if authoritative cradle-to-grave analyses show BEV < ICEV. Manufacturing premium (BEV > ICE) is evaluated as TRUE (premise). The conclusion — that total lifetime footprint is larger — is what is tested. |
| Threshold       | ICEV total lifetime CO2e (the claim asserts BEV exceeds this) |

---

## Fact Registry

| ID  | Key                    | Label |
|-----|------------------------|-------|
| B1  | source_doe_gas         | DOE FOTW #1303 (2023): Gasoline SUV cradle-to-grave = 429 g CO2e per mile |
| B2  | source_doe_ev          | DOE FOTW #1303 (2023): Battery EV emits 48% fewer GHGs than gasoline SUV (same cradle-to-grave scope) |
| B3  | source_iea             | IEA Global EV Outlook 2024: BEV lifetime emissions are half of equivalent ICEV globally |
| B4  | source_recurrent_mfg   | Recurrent Auto (citing multiple LCA studies): EV manufacturing >10 t CO2 vs gas car manufacturing ~6 t CO2 |
| A1  | —                      | BEV-to-ICEV per-mile emissions ratio derived from DOE data |
| A2  | —                      | Cross-check: DOE per-mile ratio vs IEA 'half as much' ratio |
| A3  | —                      | EV manufacturing CO2 premium over gasoline car manufacturing (metric tons) |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID  | Fact | Method | Result |
|-----|------|--------|--------|
| A1  | BEV/ICEV per-mile emissions ratio (DOE data) | `explain_calc: 1 - ev_reduction_pct / 100` | 0.52 |
| A2  | Cross-check: DOE ratio vs IEA ratio | `cross_check(0.52, 0.50, tolerance=0.05, mode='absolute')` | True (AGREE, diff = 0.020) |
| A3  | EV manufacturing CO2 premium (lower bound) | `explain_calc: ev_mfg_lower_bound - gas_mfg_tons` | 4.0 metric tons CO2 |

### Type B (Empirical) Facts

| ID  | Fact | Source | URL | Quote | Status | Method | Credibility |
|-----|------|--------|-----|-------|--------|--------|-------------|
| B1  | Gasoline SUV cradle-to-grave = 429 g CO2e/mile | U.S. DOE FOTW #1303 (Aug 14, 2023) | https://www.energy.gov/eere/vehicles/articles/fotw-1303-august-14-2023-cradle-grave-electric-vehicles-have-fewer | "Cradle-to-grave greenhouse gas (GHG) emissions for a small gasoline SUV in 2020 were estimated to be 429 grams of carbon dioxide equivalent (CO2e) per mile" | Yes | full_quote | Tier 5 (government) |
| B2  | Battery EV emits 48% fewer GHGs than gasoline SUV | U.S. DOE FOTW #1303 (Aug 14, 2023) | https://www.energy.gov/eere/vehicles/articles/fotw-1303-august-14-2023-cradle-grave-electric-vehicles-have-fewer | "the same size EV with 300 miles of range had 48% fewer GHG emissions" | Yes | full_quote | Tier 5 (government) |
| B3  | BEV lifetime = half of ICEV globally | IEA Global EV Outlook 2024 | https://www.iea.org/reports/global-ev-outlook-2024/outlook-for-emissions-reductions | "A battery electric car sold in 2023 will emit half as much as conventional equivalents over its lifetime" | Yes | full_quote | Tier 2 (unclassified; IEA is authoritative intergovernmental body) |
| B4  | EV manufacturing >10 t CO2 vs gas car ~6 t CO2 | Recurrent Auto (citing ICCT, MIT, Argonne, DOE LCAs) | https://www.recurrentauto.com/research/just-how-dirty-is-your-ev | "Manufacturing an average gas powered sedan creates about six metric tons of carbon dioxide emissions, but manufacturing an electric vehicle of the same size creates more than 10 metric tons of carbon dioxide emissions" | Yes | full_quote | Tier 2 (unclassified; values corroborated by DOE data) |

---

## Citation Verification Details

**B1 — source_doe_gas**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B2 — source_doe_ev**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B3 — source_iea**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B4 — source_recurrent_mfg**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

---

## Computation Traces

```
=== Computations ===
  A1: BEV/ICEV lifetime emissions ratio (DOE cradle-to-grave per-mile): 1 - ev_reduction_pct / 100 = 1 - 48.0 / 100 = 0.5200
  A3: EV manufacturing CO2 premium over gas car (metric tons, lower bound): ev_mfg_lower_bound - gas_mfg_tons = 10.0 - 6.0 = 4.0000

=== Cross-Check (Rule 6) ===
  A2: DOE per-mile ratio vs IEA lifetime ratio (BEV/ICEV): 0.52 vs 0.5, diff=0.020, tolerance=0.05 -> AGREE

=== Claim Evaluation ===
  Claim check: BEV/ICEV lifetime ratio > 1.0 (claim holds only if TRUE): 0.52 > 1.0 = False

BEV/ICEV ratio (DOE): 0.52 — EVs emit 48% LESS than gasoline cars lifetime
BEV/ICEV ratio (IEA): 0.50 — EVs emit 50% LESS than gasoline cars lifetime
EV manufacturing premium: >4 metric tons CO2 (higher than gas, but offset by operational savings)
```

---

## Independent Source Agreement (Rule 6)

**Cross-check A2: DOE per-mile ratio vs IEA lifetime ratio**

| Property | DOE FOTW #1303 | IEA Global EV Outlook 2024 |
|----------|---------------|---------------------------|
| Source type | U.S. Government agency | Intergovernmental energy body |
| Methodology | Per-mile cradle-to-grave LCA (Argonne GREET model) | Comprehensive lifecycle model across multiple regions |
| BEV/ICEV ratio | 0.52 (from 48% fewer emissions) | 0.50 ("half as much over lifetime") |
| Difference | — | 0.020 (2.0 percentage points) |
| Tolerance | 0.05 | — |
| Agreement | **PASS** | — |

Independence rationale: DOE uses the Argonne National Laboratory GREET model for the US context; IEA uses its own global fleet model incorporating multiple national electricity grids and vehicle classes. Different primary data, different analytical frameworks, different institutions — these are genuinely independent measurements reaching consistent conclusions.

---

## Adversarial Checks (Rule 5)

**Check 1: Coal-heavy electricity grids**
- Question: Is there any scenario where EV lifetime emissions exceed gasoline cars?
- Search performed: "electric vehicles larger carbon footprint coal grid lifetime analysis 2023 2024"; reviewed IEA Global EV Outlook 2024 regional breakdown.
- Finding: IEA reports EVs save "less than 10 tonnes of CO2-eq over lifetime" even in India (highest coal-heavy scenario). MIT: "even coal-grid EVs have fuel economy equivalent of ~50–60 mpg." No authoritative source documents EV total > ICE total in any major economy.
- Breaks proof: **No**

**Check 2: Battery disposal**
- Question: Does battery end-of-life increase EV emissions enough to flip the verdict?
- Search performed: "EV battery disposal recycling lifecycle CO2 emissions end of life"; reviewed PMC9171403 peer-reviewed LCA study.
- Finding: Battery recycling *reduces* BEV climate impact by ~8.3% (PMC9171403). DOE scope already includes end-of-life. No evidence battery disposal increases total emissions.
- Breaks proof: **No**

**Check 3: Fossil-fuel-industry-funded counter-research**
- Question: Do industry-funded studies reach different conclusions using full lifecycle analysis?
- Search performed: "peer reviewed study electric vehicles worse lifetime carbon footprint gasoline 2023 2024"; "EV lifecycle emissions higher than ICE study".
- Finding: Institute for Energy Research and similar organizations focus on manufacturing phase in isolation, not full lifecycle. No peer-reviewed major-journal study found BEV total > ICE total in mainstream scenarios. EU Parliament commissioned independent LCA found >60% CO2 savings for BEVs.
- Breaks proof: **No**

**Check 4: Short vehicle lifetimes**
- Question: Does a short lifetime (1–2 years) mean EV never repays its manufacturing premium?
- Search performed: "EV break-even point carbon emissions manufacturing years".
- Finding: Break-even is ~1–2 years of average driving. Claim makes no short-lifetime qualifier. For full vehicle lifetimes (10–15 years), EVs are unambiguously lower.
- Breaks proof: **No**

---

## Source Credibility Assessment

| ID  | Domain              | Tier | Type        | Notes |
|-----|---------------------|------|-------------|-------|
| B1  | energy.gov          | 5    | Government  | U.S. federal government domain (.gov) |
| B2  | energy.gov          | 5    | Government  | U.S. federal government domain (.gov) |
| B3  | iea.org             | 2    | Unclassified | Automated classifier does not recognize domain; IEA is the International Energy Agency, an intergovernmental body founded under the OECD — highly authoritative for energy statistics and analysis |
| B4  | recurrentauto.com   | 2    | Unclassified | Commercial EV data company; article synthesizes ICCT, MIT, Argonne, and DOE LCA studies; manufacturing figures corroborated by B1/B2 (DOE Tier 5) |

**Impact:** The disproof is independently established by B1 and B2 alone (both Tier 5, government). B3 and B4 provide corroboration from additional independent sources. Removing B3 and B4 from consideration does not change the verdict.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
