# Proof: Nuclear power is the safest form of electricity generation with the lowest death rate per TWh produced.

- **Generated:** 2026-04-01
- **Verdict:** UNDETERMINED
- **Audit trail:** [proof_audit.md](proof_audit.md) · [proof.py](proof.py)

---

## Key Findings

- Nuclear is **not** the lowest death-rate electricity source by the OWID composite dataset: biofuels rank 1st at 0.0048 deaths/TWh; nuclear ranks 2nd at 0.0097 deaths/TWh (Sovacool et al. 2016).
- The primary reference (Our World in Data) **explicitly warns** that comparing nuclear, solar, and wind is "misguided" because "the uncertainties around these values are likely to overlap."
- Two independent nuclear mortality estimates differ by ~7.6×: Sovacool et al. (2016) gives 0.0097 deaths/TWh (accidents only); Markandya & Wilkinson (2007) gives 0.074 deaths/TWh (including some air-pollution effects). Under the M&W 2007 estimate, nuclear (0.074) is *less* safe than solar (0.019) and wind (0.035) on a point-estimate basis.
- **What is clear:** nuclear is dramatically safer than fossil fuels on all estimates. Coal (24.62 deaths/TWh) is ~2,538× more lethal than nuclear by the Sovacool 2016 estimate; gas (2.821/TWh) is ~291× more lethal.

---

## Claim Interpretation

**Natural language claim:** "Nuclear power is the safest form of electricity generation with the lowest death rate per TWh produced."

**Formal interpretation:** "Safest with the lowest death rate per TWh" is operationalized as nuclear holding **rank 1 (minimum death rate)** among all electricity generation sources — coal, oil, gas, nuclear, hydro, solar, wind, and biofuels.

The metric is deaths per terawatt-hour (TWh), counting deaths from accidents and air pollution (as used by Our World in Data). Data comes from Markandya & Wilkinson (2007) for fossil fuels and Sovacool et al. (2016) for low-carbon sources.

**Operator choice:** The claim requires nuclear to be strictly first (lowest), not merely low or comparable. Two independent nuclear estimates exist and differ substantially: there is no consensus on which estimate is "correct," and the primary source explicitly flags that the differences between nuclear, solar, and wind are within overlapping uncertainty ranges. Per proof-engine rules for superlative claims with source-acknowledged uncertainty, `uncertainty_override = True` and the verdict is UNDETERMINED.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | OWID 'What are the safest and cleanest sources of energy?' — uncertainty caveat: comparing nuclear/solar/wind is 'misguided' because uncertainties are likely to overlap | Yes (fragment, 81.2%) |
| B2 | Our World in Data via Wikimedia Commons — death rates per TWh for all electricity sources (Markandya & Wilkinson 2007 + Sovacool et al. 2016) | Yes |
| A1 | Nuclear rank by Sovacool 2016 death rate among all electricity sources (1 = lowest/safest) | Computed: Rank 2 of 8 (biofuels ranks 1st at 0.0048 deaths/TWh; nuclear is 0.0097 deaths/TWh) |
| A2 | Coal-to-nuclear death rate ratio (coal M&W 2007 / nuclear Sovacool 2016): shows nuclear is dramatically safer than fossil fuels even if it is not THE lowest | Computed: 2538.1× (coal is 2,538 times more lethal per TWh than nuclear by these estimates) |

*Note: B2 (wikimedia.org) has credibility tier 2 (unclassified domain). However, the content is the official Our World in Data dataset published on Wikimedia Commons — a standard OWID data publication channel. See Source Credibility Assessment in the audit trail.*

*Source: proof.py JSON summary*

---

## Proof Logic

The claim is a superlative: nuclear must rank **first** (lowest death rate per TWh) among all electricity generation sources.

**Step 1 — Construct the full ranking (B2, A1).**
Using the OWID composite dataset (Sovacool et al. 2016 for low-carbon; Markandya & Wilkinson 2007 for fossil fuels), all electricity sources rank as follows:

| Rank | Source | Deaths/TWh |
|------|--------|-----------|
| 1 | Biofuels | 0.0048 |
| 2 | Nuclear (Sovacool 2016) | 0.0097 |
| 3 | Solar | 0.019 |
| 4 | Hydro | 0.0235 |
| 5 | Wind | 0.035 |
| 6 | Gas | 2.821 |
| 7 | Oil | 18.43 |
| 8 | Coal | 24.62 |

By point estimates, biofuels (0.0048 deaths/TWh) ranks lower than nuclear (0.0097 deaths/TWh), so nuclear is **not** rank 1 (A1: rank 2 of 8).

**Step 2 — Methodological disagreement for the nuclear estimate (A2).**
A second independent estimate for nuclear — Markandya & Wilkinson (2007) — gives 0.074 deaths/TWh, approximately 7.6× higher than the Sovacool estimate. Under this estimate, nuclear (0.074) has a *higher* death rate than solar (0.019) and wind (0.035). The ratio of the two nuclear estimates (0.074 ÷ 0.0097 ≈ 7.6×) reflects genuine methodological disagreement, not rounding: M&W includes occupational deaths and some air-pollution mortality; Sovacool focuses on accident deaths. No consensus determines which is correct.

**Step 3 — Source-acknowledged uncertainty (B1).**
Our World in Data, the primary source for this comparison, explicitly states: "People often focus on the marginal differences at the bottom of the chart — between nuclear, solar, and wind. This comparison is misguided: the uncertainties around these values are likely to overlap." This directly invokes the proof-engine rule for superlative claims with source-acknowledged uncertainty: `uncertainty_override = True`.

**Step 4 — What is robustly established.**
Across both nuclear estimates (0.0097 and 0.074), nuclear is dramatically safer than fossil fuels. Coal (24.62 deaths/TWh) is roughly 2,538× more lethal than nuclear by Sovacool 2016 and ~332× more lethal by M&W 2007. Gas (2.821 deaths/TWh) is ~291× and ~38× more lethal respectively. This sub-result is not in dispute.

---

## Counter-Evidence Search

**Search 1 — Does biofuels exclusion change the result?**
Searched "biofuels electricity generation death rate OWID Sovacool" and reviewed OWID methodology. Finding: OWID's "death rates from energy production" comparison includes biofuels as an electricity generation source; biofuels in this context covers biogas and biomass power plants. Even if biofuels were excluded, the uncertainty_override still applies because OWID explicitly warns that comparing nuclear/solar/wind is "misguided." Result: does not break the UNDETERMINED verdict.

**Search 2 — Markandya & Wilkinson (2007) estimate for nuclear.**
Reviewed the OWID all-sources Wikimedia Commons dataset, which lists both nuclear estimates (0.074 M&W 2007 and 0.0097 Sovacool 2016). Under M&W 2007, nuclear (0.074 deaths/TWh) is less safe than solar (0.019) and wind (0.035) on a point-estimate basis. This directly contradicts the claim. The 7.6× discrepancy between estimates reflects genuine methodological disagreement. **This counter-evidence breaks the proof** (`breaks_proof: True`).

**Search 3 — Consensus source for nuclear as definitively lowest.**
Searched "nuclear lowest death rate electricity all sources 2024 definitive" and "safest energy source peer reviewed 2023." Finding: no authoritative source makes the unqualified claim that nuclear has the definitively lowest death rate per TWh across all electricity sources. Our World in Data — the most widely cited source on this topic — explicitly cautions against this ranking. Most sources describe nuclear as "among the safest" or "comparable to solar and wind."

---

## Conclusion

**Verdict: UNDETERMINED**

The claim that "nuclear power is the safest form of electricity generation with the lowest death rate per TWh" cannot be established for three independent reasons:

1. **Nuclear is not the point-estimate minimum.** By the OWID composite dataset, biofuels rank first (0.0048 deaths/TWh) while nuclear ranks second (0.0097 deaths/TWh) by the Sovacool 2016 estimate.

2. **Source-acknowledged uncertainty makes the comparison unresolvable.** Our World in Data (B1, verified) explicitly states the comparison between nuclear, solar, and wind is "misguided" because the uncertainty ranges are likely to overlap.

3. **Methodological counter-evidence.** The Markandya & Wilkinson (2007) nuclear estimate (0.074 deaths/TWh, B2, verified) places nuclear as *less* safe than solar and wind by point estimates — directly contradicting the claim.

**To resolve this claim, the following evidence would be needed:**
- A peer-reviewed consensus establishing which nuclear mortality methodology is correct (accident-deaths-only vs. including occupational/air-pollution deaths).
- Confidence intervals for all electricity sources from a single consistent methodology, demonstrating that nuclear's interval does not overlap with the next-safest source.
- A standardized decision on whether biofuels-for-electricity count as an electricity generation comparator.

**What this proof does establish:** Nuclear power is dramatically safer than fossil fuels (coal, oil, gas) by any available estimate. This sub-result is robust across methodologies. The ambiguity is limited to whether nuclear, solar, wind, and biofuels can be definitively ranked among themselves.

*Note: B2 (wikimedia.org) is classified as Tier 2 (unclassified domain) by the credibility assessor. This reflects the assessor's treatment of wikimedia.org rather than the source's actual authority: B2 is the official OWID dataset, published on Wikimedia Commons as a standard data-sharing channel. The OWID data is the primary reference for this topic and is widely cited in peer-reviewed literature.*

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-04-01.*
