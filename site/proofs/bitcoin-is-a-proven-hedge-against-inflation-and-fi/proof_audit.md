# Audit: Bitcoin is a proven hedge against inflation and fiat currency collapse.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Bitcoin |
| Property | proven (consistent, empirically reliable) hedge against both (SC1) ordinary consumer-price-index (CPI) inflation and (SC2) fiat currency collapse or hyperinflation |
| Operator | == |
| Threshold | True (both sub-claims proven) |
| Operator Note | 'Proven' is interpreted strictly: requires consistent, documented empirical performance under the claimed conditions with no verified counterexamples. The claim is a conjunction (SC1 AND SC2): both sub-claims must be proven. SC1 proof direction is FALSIFICATION — one verified counterexample (Bitcoin declining during a period of high CPI inflation) is sufficient to disprove the 'proven' designation for SC1. SC2 proof direction is CONSENSUS — requires >= 3 independent verified sources establishing Bitcoin reliably protects value during fiat collapse; having found only partial evidence (stablecoins preferred over Bitcoin in hyperinflationary economies), SC2 does not reach 'proven' status. The compound claim holds only if BOTH SC1 and SC2 are individually proven. |
| Sub-Claims | SC1: Bitcoin is a proven hedge against ordinary CPI inflation; SC2: Bitcoin is a proven hedge against fiat currency collapse / hyperinflation |

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | sc1_bedel | SC1 counter-evidence: Bitcoin returned -64.8% in 2022 — the worst inflation year since 1981 (Bedel Financial Advisors) |
| B2 | sc1_cpi | SC1 context: US CPI peaked at 9.1% in June 2022 — largest year-over-year increase since November 1981 (Bedel Financial Advisors) |
| B3 | sc1_smales | SC1 academic finding: cryptocurrencies are not a viable alternative to gold for inflation hedging (Smales 2024, Accounting & Finance) |
| B4 | sc2_venezuela | SC2 partial context: Venezuelan citizens use crypto amid hyperinflation and currency collapse (AINFP) |
| A1 | — | SC1 computation: count of verified counter-evidence sources for Bitcoin-as-inflation-hedge claim (any >=1 disproves 'proven') |
| A2 | — | SC2 computation: count of verified support sources versus 'proven' threshold of 3 |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1: count of verified counter-evidence sources | count verified SC1 counter-evidence sources in {sc1_bedel, sc1_cpi, sc1_smales} | 3 verified (>= 1 needed to disprove 'proven' status for SC1) |
| A2 | SC2: count of verified support sources vs threshold | count verified SC2 support sources vs threshold of 3 | 1 verified (< 3 = not proven for SC2) |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | SC1 counter-evidence: Bitcoin -64.8% in 2022 | Bedel Financial Advisors — Inflation Hedge in 2022: Bitcoin vs. Gold | https://www.bedelfinancial.com/inflation-hedge-in-2022-bitcoin-vs-gold | "bitcoin ended the year down an abysmal -64.8%, while gold ended the year relatively flat, down about -0.7%" | verified | full_quote | Tier 2 (unknown) |
| B2 | SC1 context: US CPI peaked at 9.1% June 2022 | Bedel Financial Advisors — Inflation Hedge in 2022: Bitcoin vs. Gold (CPI peak data) | https://www.bedelfinancial.com/inflation-hedge-in-2022-bitcoin-vs-gold | "By June, the 12-month CPI was up to 9.1%. This was the largest year-over-year increase since November 1981" | verified | full_quote | Tier 2 (unknown) |
| B3 | SC1 academic: cryptocurrencies not viable gold alternative for inflation hedging | IDEAS/RepEC — Smales (2024), Accounting & Finance | https://ideas.repec.org/a/bla/acctfi/v64y2024i2p1589-1611.html | "cryptocurrencies do not currently offer investors a viable alternative to gold for hedging inflation" | verified | full_quote | Tier 2 (unknown) |
| B4 | SC2 partial: Venezuelan crypto use during hyperinflation | AINFP — How Venezuelans Use Crypto Amid Hyperinflation | https://ainfp.org/how-venezuelans-use-crypto-amid-hyperinflation | "Annual inflation at 229% in May 2025 and the currency losing over 70% of its value since January" | verified | full_quote | Tier 2 (unknown) |

---

## Citation Verification Details

**B1 — Bedel Financial Advisors (Bitcoin return 2022)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B2 — Bedel Financial Advisors (CPI peak 2022)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B3 — IDEAS/RepEC, Smales (2024)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

**B4 — AINFP, Venezuela crypto**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Coverage: N/A (full match)

No unverified citations. All citations confirmed via live fetch.

---

## Computation Traces

```
SC1 (inflation hedge): zero verified counter-evidence sources (required for 'proven' status): 3 == 0 = False
SC2 (fiat collapse hedge): verified support sources >= proven threshold of 3: 1 >= 3 = False
Compound claim: SC1 (no counterexample) AND SC2 (proven) both hold: 0 == 2 = False
```

**Interpretation:**
- `3 == 0 = False`: Three counter-evidence sources confirmed SC1's failure. The condition "zero counterexamples" evaluates to False, meaning SC1 is disproved.
- `1 >= 3 = False`: Only one SC2 support source was found; the proven threshold of 3 is not reached.
- `0 == 2 = False`: The sum of passing sub-claims (0 out of 2) does not equal 2; the compound claim fails.

---

## Independent Source Agreement (Rule 6)

| Cross-check | Source A | Source B | Agreement |
|-------------|----------|----------|-----------|
| SC1 real-world vs academic | Bedel Financial (2022): Bitcoin -64.8% while CPI 9.1% | Smales (2024): cryptocurrencies not a viable gold alternative for hedging inflation | Yes |

**Independence rationale:** Source A (bedelfinancial.com) is a financial advisory firm reporting calendar-year 2022 market returns and BLS CPI data. Source B (Smales 2024, IDEAS/RepEC) is a peer-reviewed econometric analysis using a different methodology (regression analysis of cryptocurrency returns relative to inflation expectations). They are independently published, use different methodologies, and arrive at compatible conclusions through separate analytical paths. Independence is "independently published (different domains and methodologies)" — not independent measurements of the same underlying physical quantity.

---

## Adversarial Checks (Rule 5)

**Check 1:** Does any academic study confirm Bitcoin as a reliable, consistent inflation hedge?
- Search performed: Searched Google Scholar and PubMed Central for 'Bitcoin inflation hedge' peer-reviewed studies. Found Bouri et al. (2021) in Finance Research Letters (PMC/NCB PMC8995501) which concluded 'Bitcoin appreciates against inflation or inflation expectation shocks, confirming its inflation-hedging property claimed by investors.' Also reviewed MDPI Axioms 11/7/339 on high-adoption countries.
- Finding: Several studies using data primarily from 2010–2020 find some inflation-hedging signal in Bitcoin. However, Smales (2024) — using a longer, post-COVID series — finds the effect 'only significant for short-term inflation expectations' and 'only when inflation or market-implied inflation expectations are below 2%,' meaning Bitcoin hedges inflation precisely when no hedge is needed. The 2022 real-world test invalidated earlier positive findings: Bitcoin fell 65% during the worst US inflation in 40 years.
- Breaks proof: No

**Check 2:** Could Bitcoin's long-term appreciation (from <$1 in 2009 to >$10,000+) constitute an inflation hedge?
- Search performed: Searched for 'Bitcoin long-term inflation-adjusted returns' and 'inflation hedge definition finance'. Reviewed academic definitions of an inflation hedge: an asset whose returns co-move positively with inflation, providing purchasing power protection during inflationary episodes.
- Finding: Long-term appreciation does not establish an asset as an inflation hedge in the financial-economics sense. A hedge must reliably co-move with inflation during inflationary episodes. Bitcoin's 2022 performance (down 65% during peak inflation) demonstrates that its long-run appreciation coexists with sharp declines during the very periods a hedge would be needed. High-volatility assets with strong long-run trends (e.g., equities, real estate) are not classified as inflation hedges for the same reason.
- Breaks proof: No

**Check 3:** Does Bitcoin adoption in Argentina (276% inflation in 2024) support SC2 (fiat collapse hedge)?
- Search performed: Searched 'Argentina Bitcoin crypto adoption hyperinflation 2024' and reviewed Chainalysis 2023 Geography of Cryptocurrency report. Found Argentina among top global crypto adopters during its 2024 inflation crisis.
- Finding: Argentina and Venezuela both show elevated crypto adoption during fiat crises. However, the dominant instruments are dollar-pegged stablecoins (USDT, USDC) rather than Bitcoin itself. In Venezuela, 'USDT' is the everyday transaction currency ('Binance dollars') while Bitcoin plays a secondary role. In Argentina, stablecoins dominate daily transactions. Bitcoin's own extreme volatility (capable of -50% in a single month) makes it a poor store of value during economic crises where price stability is paramount. This weakens the 'Bitcoin specifically' component of SC2.
- Breaks proof: No

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | bedelfinancial.com | unknown | 2 | Unclassified domain — verify source authority manually. Manual note: Bedel Financial Advisors is a registered US investment advisory firm (Indianapolis, IN). CPI figures are sourced from the US Bureau of Labor Statistics. The Bitcoin return figure is consistent with widely reported market data. |
| B2 | bedelfinancial.com | unknown | 2 | Same source as B1. |
| B3 | repec.org | unknown | 2 | Unclassified domain — verify source authority manually. Manual note: IDEAS/RepEC is a major academic bibliography database for economics, maintained by the University of Connecticut and Federal Reserve. The Smales (2024) paper is published in *Accounting & Finance* (Wiley), a peer-reviewed journal. The effective credibility is Tier 4 (academic/peer-reviewed); the Tier 2 designation reflects the automated classifier's limitation. |
| B4 | ainfp.org | unknown | 2 | Unclassified domain — verify source authority manually. Manual note: AINFP (Association for Inflation-Fighting Programs) is a small advocacy/educational organization. The Venezuela statistics cited are consistent with widely reported IMF and Chainalysis data, but this source should be treated with appropriate caution for quantitative claims. |

No Tier 1 (flagged unreliable) sources. The proof's key falsification argument (SC1) relies on B1–B3; B3's underlying paper is peer-reviewed. B4 (AINFP) is used only for SC2's partial-evidence assessment, not for the definitive disproof.

---

## Extraction Records

For qualitative proofs, extraction records reflect citation verification status per source:

| Fact ID | Value | Value in Quote | Quote Snippet |
|---------|-------|----------------|---------------|
| B1 | verified | true | "bitcoin ended the year down an abysmal -64.8%, while gold ended the year relativ" |
| B2 | verified | true | "By June, the 12-month CPI was up to 9.1%. This was the largest year-over-year in" |
| B3 | verified | true | "cryptocurrencies do not currently offer investors a viable alternative to gold f" |
| B4 | verified | true | "Annual inflation at 229% in May 2025 and the currency losing over 70% of its val" |

No numeric extraction performed. This is a qualitative consensus/falsification proof; citation verification status counts as evidence, not extracted numeric values.

---

## Hardening Checklist

- **Rule 1 (No hand-typed values):** ✓ Auto-pass — no value-extraction patterns used (qualitative proof)
- **Rule 2 (Verify citations by fetching):** ✓ `verify_all_citations()` called; all 4 citations returned `status: verified` via live fetch
- **Rule 3 (Anchor to system time):** ✓ `date.today()` present in `generator.generated_at`; no time-dependent age calculations
- **Rule 4 (Explicit claim interpretation):** ✓ `CLAIM_FORMAL` with `operator_note` present; both sub-claims documented; "proven" interpreted with explicit threshold and falsification strategy
- **Rule 5 (Adversarial checks):** ✓ Three independent adversarial checks performed; searched for studies supporting Bitcoin as inflation hedge, assessed long-term appreciation argument, evaluated Argentina/Venezuela evidence — none breaks the proof
- **Rule 6 (Independent cross-checks):** ✓ SC1 conclusion corroborated by two independently published sources (bedelfinancial.com and repec.org/Smales 2024) using different methodologies
- **Rule 7 (No hard-coded constants):** ✓ Auto-pass — no arithmetic constants or formulas used (qualitative proof)
- **validate_proof.py result:** PASS — 14/14 checks passed, 0 issues, 0 warnings

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
