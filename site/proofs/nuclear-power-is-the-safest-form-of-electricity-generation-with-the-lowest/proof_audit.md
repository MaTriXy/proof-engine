# Audit: Nuclear power is the safest form of electricity generation with the lowest death rate per TWh produced.

- **Generated:** 2026-04-01
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | nuclear power |
| Property | death rate per TWh (deaths from accidents and air pollution) — rank among all electricity generation sources (1 = lowest/safest) |
| Operator | == |
| Threshold | 1 (nuclear must achieve rank 1, i.e., the minimum death rate) |
| Operator note | 'Safest with the lowest death rate per TWh' is operationalized as nuclear holding rank 1 (minimum death rate) among all electricity generation sources — coal, oil, gas, nuclear, hydro, solar, wind, and biofuels. Data from Our World in Data (OWID) combining Markandya & Wilkinson (2007) for fossil fuels and Sovacool et al. (2016) for low-carbon sources. Two independent nuclear estimates differ by ~8×: 0.0097 (Sovacool 2016) and 0.074 (M&W 2007). OWID explicitly cautions the comparison between nuclear/solar/wind is 'misguided' due to overlapping uncertainty. uncertainty_override=True per proof-engine rules. |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | owid_safest | OWID 'What are the safest and cleanest sources of energy?' — uncertainty caveat: comparing nuclear/solar/wind is 'misguided' because uncertainties are likely to overlap |
| B2 | owid_data_table | Our World in Data via Wikimedia Commons — death rates per TWh for all electricity sources (Markandya & Wilkinson 2007 + Sovacool et al. 2016) |
| A1 | *(computed)* | Nuclear rank by Sovacool 2016 death rate among all electricity sources (1 = lowest/safest) |
| A2 | *(computed)* | Coal-to-nuclear death rate ratio (coal M&W 2007 / nuclear Sovacool 2016): shows nuclear is dramatically safer than fossil fuels even if it is not THE lowest |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Nuclear rank by Sovacool 2016 death rate among all electricity sources (1 = lowest/safest) | sort(all_sources by death_rate)[nuclear] → rank 2 | 2 |
| A2 | Coal-to-nuclear death rate ratio (coal M&W 2007 / nuclear Sovacool 2016) | coal / nuclear_sovacool | 2538.1× |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | OWID uncertainty caveat | Our World in Data — 'What are the safest and cleanest sources of energy?' (Hannah Ritchie, 2020; updated July 2022) | https://ourworldindata.org/safest-sources-of-energy | "People often focus on the marginal differences at the bottom of the chart — between nuclear, solar, and wind. This comparison is misguided: the uncertainties around these values are likely to overlap." | verified | fragment (81.2%) | Tier 3 (reference) |
| B2 | OWID all-sources data table | Our World in Data via Wikimedia Commons — deaths per TWh all sources (Markandya & Wilkinson 2007 + Sovacool et al. 2016) | https://commons.wikimedia.org/wiki/Data:Deaths_per_TWh_energy_production,_all_sources_(Markandya_and_Wilkinson;_Sovacool_et_al.)_(OWID_4888).tab | "Death rates from energy production is measured as the number of deaths by energy source per terawatt-hour (TWh) of production." | verified | full_quote | Tier 2 (unclassified) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — OWID safest sources page**
- Status: `verified`
- Method: `fragment` (coverage 81.2% — above the 80% threshold for verified)
- Fetch mode: `live`
- Note: OWID pages are partially JavaScript-rendered. The key quote was found at 81.2% fragment coverage in the live-fetched HTML, exceeding the 80% threshold for verified status.

**B2 — Wikimedia Commons OWID data table**
- Status: `verified`
- Method: `full_quote`
- Fetch mode: `live`
- Note: The Wikimedia Commons `.tab` page returns raw tab-separated data in the Data: namespace. The quote describing the dataset ("Death rates from energy production is measured...") was found verbatim. All nine data values (biofuels, nuclear_sovacool, nuclear_mw2007, solar, wind, hydro, coal, oil, gas) were independently verified via `verify_data_values()` — all found on the live page.

*Source: proof.py JSON summary*

---

## Computation Traces

Reproduced verbatim from proof.py execution:

```
--- Death rates per TWh, ranked lowest to highest ---
    (Sovacool 2016 for low-carbon sources; M&W 2007 for fossil fuels)
  Rank  1: biofuels     0.0048 deaths/TWh
  Rank  2: nuclear      0.0097 deaths/TWh  <-- NUCLEAR
  Rank  3: solar        0.0190 deaths/TWh
  Rank  4: hydro        0.0235 deaths/TWh
  Rank  5: wind         0.0350 deaths/TWh
  Rank  6: gas          2.8210 deaths/TWh
  Rank  7: oil          18.4300 deaths/TWh
  Rank  8: coal         24.6200 deaths/TWh

Nuclear rank (Sovacool 2016): 2 of 8
  Nuclear rank == 1 (lowest death rate across all electricity sources): 2 == 1 = False
  Biofuels (0.0048) < Nuclear/Sovacool (0.0097): biofuels has lower rate than nuclear: 0.0048 < 0.0097 = True
  A2: Coal / Nuclear (Sovacool 2016) death-rate ratio: coal / nuclear_sovacool = 24.62 / 0.0097 = 2538.1443
  Nuclear (M&W 2007) / Solar ratio [>1 means nuclear LESS safe than solar by M&W]: nuclear_mw2007 / solar = 0.074 / 0.019 = 3.8947
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

| Cross-check | Values Compared | Agreement | Note |
|-------------|-----------------|-----------|------|
| Two independent nuclear death-rate estimates (methodological cross-check) | Sovacool 2016: 0.0097; M&W 2007: 0.074 | **No** — differ by 7.6× | These are two methodologically distinct estimates, not two independent measurements of the same quantity. M&W 2007 includes occupational and air-pollution deaths; Sovacool 2016 focuses on accidents. The disagreement reflects genuine methodological controversy. |

**Data value verification (Rule 6 — confirming B2 numbers appear on source):**

All nine data values from B2 were found on the live Wikimedia Commons page:

| Key | Value | Found |
|-----|-------|-------|
| biofuels | 0.0048 | ✓ live |
| nuclear_sovacool | 0.0097 | ✓ live |
| nuclear_mw2007 | 0.074 | ✓ live |
| solar | 0.019 | ✓ live |
| wind | 0.035 | ✓ live |
| hydro | 0.0235 | ✓ live |
| coal | 24.62 | ✓ live |
| oil | 18.43 | ✓ live |
| gas | 2.821 | ✓ live |

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

**Check 1 — Does biofuels exclusion change the result?**
- Question: If biofuels are excluded from 'electricity generation' sources, does nuclear then have the lowest death rate?
- Search performed: Reviewed OWID methodology and Sovacool et al. 2016: 'biofuels' in the dataset covers biogas and biomass power plants used for electricity generation. OWID's 'death rates from energy production' chart includes biofuels as an electricity generation source. Searched 'biofuels electricity generation death rate OWID Sovacool' to confirm scope.
- Finding: Even if biofuels were excluded, the uncertainty_override=True verdict applies regardless: OWID explicitly warns that comparing nuclear, solar, and wind is 'misguided' because 'the uncertainties around these values are likely to overlap.' Nuclear (0.0097) < solar (0.019) and wind (0.035) by Sovacool 2016 point estimates, but OWID's caveat prevents a definitive superlative ranking.
- Breaks proof: **No**

**Check 2 — M&W 2007 nuclear estimate contradicts the claim**
- Question: Does the Markandya & Wilkinson (2007) nuclear estimate (0.074 deaths/TWh) contradict the claim that nuclear has the lowest death rate?
- Search performed: Reviewed the OWID all-sources Wikimedia Commons dataset: it contains two entries for nuclear — 0.074 (M&W 2007) and 0.0097 (Sovacool 2016). These differ by ~8×. M&W 2007 includes occupational deaths and some air-pollution effects; Sovacool 2016 focuses on accident deaths (Chernobyl, Fukushima, other accidents). Searched 'nuclear death rate Markandya Wilkinson 2007 vs Sovacool 2016 comparison' to confirm methodological basis of each estimate.
- Finding: The M&W 2007 nuclear estimate (0.074 deaths/TWh) directly contradicts the claim: nuclear would be LESS safe than solar (0.019) and wind (0.035) by point estimates. The 8× discrepancy reflects fundamental methodological disagreement about what death categories to include; no consensus exists on which is 'correct.' Under M&W 2007, nuclear is not only not the safest — it is less safe than two major renewable sources. This counter-evidence breaks the proof.
- Breaks proof: **Yes** → verdict forced to UNDETERMINED

**Check 3 — No consensus source establishes nuclear as definitively lowest**
- Question: Is there a consensus source that definitively establishes nuclear as having the single lowest death rate across all electricity generation sources?
- Search performed: Searched 'nuclear lowest death rate electricity all sources 2024 definitive', 'safest energy source peer reviewed 2023', and 'nuclear solar wind death rate definitive ranking'. Reviewed Our World in Data, Sovacool et al. 2016, Markandya & Wilkinson 2007, and WHO energy data.
- Finding: No authoritative source makes the unqualified claim that nuclear has the definitively lowest death rate per TWh across all electricity sources. OWID — the most widely cited source on this topic — explicitly cautions against making this comparison. Most sources describe nuclear as 'among the safest' or 'comparable to solar and wind,' not as definitively the lowest.
- Breaks proof: **No**

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | ourworldindata.org | reference | 3 | Established reference source — widely cited in peer-reviewed literature for energy safety statistics |
| B2 | wikimedia.org | unknown | 2 | Unclassified domain — the credibility assessor does not classify wikimedia.org specifically. However, B2 is the official Our World in Data dataset published on Wikimedia Commons (OWID's standard data-sharing channel). The underlying data is sourced from peer-reviewed studies (Markandya & Wilkinson 2007, Lancet; Sovacool et al. 2016, Journal of Cleaner Production). The proof does not depend solely on B2: the uncertainty caveat (B1, Tier 3) is independently verified from ourworldindata.org. |

*Source: proof.py JSON summary*

---

## Extraction Records

All values were parsed from `data_values` strings using `parse_number_from_quote()`, which extracts the floating-point value via regex. No `verify_extraction()` calls are needed for `data_values` (per template — they are verified via `verify_data_values()` instead).

| Fact ID | Extracted Value | Found in data_values | Snippet |
|---------|-----------------|----------------------|---------|
| B2_nuclear_sovacool | 0.0097 | Yes | data_values['nuclear_sovacool'] = '0.0097' |
| B2_nuclear_mw2007 | 0.074 | Yes | data_values['nuclear_mw2007'] = '0.074' |
| B2_biofuels | 0.0048 | Yes | data_values['biofuels'] = '0.0048' |
| B2_solar | 0.019 | Yes | data_values['solar'] = '0.019' |
| B2_wind | 0.035 | Yes | data_values['wind'] = '0.035' |
| B2_coal | 24.62 | Yes | data_values['coal'] = '24.62' |
| B2_gas | 2.821 | Yes | data_values['gas'] = '2.821' |

Extraction method: `parse_number_from_quote(data_values[key], r"([\d.]+)", fact_id)` — standard floating-point extraction, no Unicode normalization needed (all values are ASCII numerics).

*Source: proof.py JSON summary; extraction method: author analysis*

---

## Hardening Checklist

- **Rule 1** ✓ Every empirical value parsed from data_values strings via `parse_number_from_quote()`, not hand-typed in proof logic.
- **Rule 2** ✓ Both citation URLs fetched live; quotes verified: B1 fragment (81.2%), B2 full. All nine data_values confirmed via `verify_data_values()`.
- **Rule 3** ✓ `date.today()` used for `generated_at` field. Proof logic is not time-dependent (mortality data is from 2014 studies), so no date-dependent computation required.
- **Rule 4** ✓ `CLAIM_FORMAL` dict with explicit `operator_note` documenting the superlative interpretation, both nuclear estimates, the uncertainty caveat, and the basis for `uncertainty_override=True`.
- **Rule 5** ✓ Three adversarial checks performed via web search and source review, including one (`breaks_proof: True`) finding that the M&W 2007 nuclear estimate directly contradicts the claim. Each check is structurally independent from the ranking computation.
- **Rule 6** ✓ Two distinct sources in `empirical_facts` (B1: ourworldindata.org; B2: wikimedia.org). Data values verified against the live B2 page. Methodological cross-check documents the 7.6× discrepancy between the two nuclear estimates.
- **Rule 7** ✓ All computations use `compare()` and `explain_calc()` from `scripts/computations.py`. No hard-coded constants or inline formulas.
- **validate_proof.py result:** PASS — 15/15 checks passed, 0 issues, 0 warnings.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
