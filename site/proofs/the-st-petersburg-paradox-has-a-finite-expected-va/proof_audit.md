# Audit: The St. Petersburg paradox has a finite expected value that a rational person should be willing to pay.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | St. Petersburg game |
| Property | expected monetary value (SC1) and rational certainty equivalent (SC2) |
| Operator | AND |
| Operator note | The claim makes two assertions: (SC1) the expected monetary value E[X] is finite, AND (SC2) a rational person should pay only a finite amount. SC1 requires the series sum_{n>=1} (1/2^n)*2^n to converge. SC2 requires decision theory (expected utility) to yield a finite certainty equivalent. The overall claim is DISPROVED because SC1 is false: the EV series diverges to infinity. SC2 is true — under Bernoulli's (1738) log utility, the certainty equivalent = $4 (initial wealth assumed zero) — but this does not save the compound claim because the correct resolution involves expected *utility*, not expected *value*. |

---

## Fact Registry

| ID | Key / Description |
|----|-------------------|
| A1 | SC1: EV term (1/2)^n * 2^n = 1 for every n; series = sum of infinitely many 1s |
| A2 | SC1 cross-check: partial sums grow as N (unbounded), confirming divergence |
| A3 | SC2: E[ln(2^N)] = ln(2) * sum(n*(1/2)^n) = ln(2)*2 = 2*ln(2) (finite) |
| A4 | SC2 cross-check: generating function confirms sum(n*(1/2)^n) = 2 |
| B1 | source_wiki — Wikipedia: St. Petersburg paradox |
| B2 | source_sep — Stanford Encyclopedia of Philosophy: St. Petersburg Paradox |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | SC1: EV term (1/2)^n * 2^n = 1 for every n; series = sum of infinitely many 1s | algebraic: (1/2)^n * 2^n = 1^n = 1 for all n >= 1 | All terms = 1.0 (verified n=1..20); series = sum of infinity 1s |
| A2 | SC1 cross-check: partial sums grow as N (unbounded), confirming divergence | partial sum: sum_{k=1}^{N} 1 = N (unbounded) | 10-term sum=10.0, 20-term sum=20.0 (grows as N) |
| A3 | SC2: E[ln(2^N)] = ln(2) * sum(n*(1/2)^n) = ln(2)*2 = 2*ln(2) (finite) | E[ln(2^N)] = ln(2) * sum(n*(1/2)^n) = ln(2) * 2 = 2*ln(2) | E[U] = 1.386294 = 2*ln(2); CE = exp(E[U]) = $4.000000 |
| A4 | SC2 cross-check: generating function confirms sum(n*(1/2)^n) = 2 | generating function: sum(n*x^n) = x/(1-x)^2 at x=1/2 | sum(n*(1/2)^n) = 2.0 (confirms = 2) |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | Wikipedia: St. Petersburg paradox — game rules and infinite EV | Wikipedia: St. Petersburg paradox | https://en.wikipedia.org/wiki/St._Petersburg_paradox | "The expected payoff of the lottery game is infinite" | Yes | full_quote | Tier 3 (reference) |
| B2 | SEP — Bernoulli utility resolution | Stanford Encyclopedia of Philosophy: St. Petersburg Paradox | https://plato.stanford.edu/entries/paradox-stpetersburg/ | "the logarithm of the monetary amount, which entails that improbable but large monetary prizes will contribute less to the expected utility of the game than more probable but smaller monetary amounts" | Yes | full_quote | Tier 4 (academic) |

---

## Citation Verification Details

**B1 — Wikipedia: St. Petersburg paradox**
- Status: verified
- Method: full_quote
- Fetch mode: live

**B2 — Stanford Encyclopedia of Philosophy: St. Petersburg Paradox**
- Status: verified
- Method: full_quote
- Fetch mode: live

---

## Computation Traces

```
── SC1: Term verification (1/2)^n * 2^n for n = 1..20 ──
First 5 terms: [1.0, 1.0, 1.0, 1.0, 1.0]
All 20 terms equal 1.0: True
  SC1: Every term (1/2)^n * 2^n = 1.0 (verified n=1..20): True == True = True

Spot-check n=5:
  (0.5**5) * (2.0**5): (0.5**5) * (2.0**5) = 0.5 ** 5 * 2.0 ** 5 = 1.0000

── SC1 cross-check: Partial sums ──
  partial_sum_10: partial_sum_10 = 10.0 = 10.0000
  partial_sum_20: partial_sum_20 = 20.0 = 20.0000
  SC1 cross-check: 10-term partial sum = 10.0 (unbounded growth): 0.0 < 1e-09 = True
  SC1 cross-check: 20-term partial sum = 20.0 (N-term sum = N): 0.0 < 1e-09 = True
  SC1: EV series converges? Terms 11-20 contribute <0.001? (False = diverges): 10.0 < 0.001 = False

── SC2: Bernoulli expected utility ──
  x / (1 - x)**2: x / (1 - x)**2 = 0.5 / (1 - 0.5) ** 2 = 2.0000
  SC2/A4: sum(n*(1/2)^n) = x/(1-x)^2 at x=0.5 = 2.0 (generating function): 0.0 < 1e-14 = True

Expected utility computation:
  math.log(2) * generating_fn: math.log(2) * generating_fn = math.log(2) * 2.0 = 1.3863
  SC2/A3: E[ln(2^N)] = ln(2) * 2 = 2*ln(2) ≈ 1.3863 (finite): 0.0 < 1e-12 = True

Certainty equivalent:
  math.exp(analytical_eu): math.exp(analytical_eu) = math.exp(1.3862943611198906) = 4.0000
  SC2: Certainty equivalent = exp(2*ln(2)) = $4.00 (rational WTP, finite): 0.0 < 1e-10 = True

── SC2 cross-check: numerical convergence ──
  abs(eu_numerical - analytical_eu): abs(eu_numerical - analytical_eu) = abs(1.3862943611198906 - 1.3862943611198906) = 0.0000
  SC2 cross-check: 10000-term numerical EU matches 2*ln(2) within 0.001: 0.0 < 0.001 = True
  SC2: Certainty equivalent is finite (< 1e15, i.e., a real finite dollar amount): 4.0 < 1000000000000000.0 = True
  Overall: compound claim holds only if SC1=True AND SC2=True: 1 == 2 = False
```

---

## Adversarial Checks (Rule 5)

**1. Is there a mathematical framework where the standard St. Petersburg EV is finite?**
- Searched: "St. Petersburg paradox finite expected value" and "St. Petersburg standard game EV convergent"
- Finding: No peer-reviewed source claims the standard game has finite EV. The divergence is mathematical consensus. Bounded-payoff and finite-wealth-cap variants are different games.
- Breaks proof: No

**2. Could "expected value" in the claim mean "expected utility" or "certainty equivalent"?**
- Analyzed: The claim language uses "expected value" — a precisely defined technical term in standard probability/economics. Searched for alternative readings; found none in standard literature.
- Finding: Even under the most charitable reading, the correct term for the $4 quantity is *certainty equivalent* or *expected utility*. The claim's terminology is wrong.
- Breaks proof: No

**3. Does Menger's (1934) super-St.-Petersburg paradox undermine SC2?**
- Searched: "Menger 1934 super St. Petersburg paradox log utility unbounded"
- Finding: Menger's result applies to a different game (payoff exp(2^n)). For the *standard* game (payoff 2^n), log utility gives CE = $4. Menger's result does not break SC2.
- Breaks proof: No

**4. Is log utility the only framework giving finite willingness to pay?**
- Searched: "St. Petersburg paradox CRRA utility solution" and "risk aversion St. Petersburg finite certainty equivalent"
- Finding: Any risk-averse utility (CRRA with γ > 0) gives a finite CE for the standard game. This strengthens SC2. Only the exact $4 value is specific to Bernoulli's log utility with zero initial wealth.
- Breaks proof: No

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | wikipedia.org | reference | 3 | Established reference source |
| B2 | stanford.edu | academic | 4 | Academic domain (.edu) — Stanford Encyclopedia of Philosophy |

---

## Hardening Checklist

- **Rule 1:** N/A — pure computation, no empirical values extracted from quotes
- **Rule 2:** Both citations fetched and verified live: B1 (full_quote), B2 (full_quote)
- **Rule 3:** `date.today()` present; not time-dependent (pure math), no date drift risk
- **Rule 4:** CLAIM_FORMAL with detailed `operator_note` documenting compound SC1/SC2 decomposition and why compound claim fails
- **Rule 5:** Four independent adversarial checks performed; no counter-evidence found that breaks the proof
- **Rule 6:** N/A — pure computation, no empirical cross-sources; independence for A-type facts established via mathematically distinct methods (algebraic term analysis vs. partial sum growth; generating function vs. numerical convergence)
- **Rule 7:** All constants and formulas use `math.log()`, `math.exp()` from Python stdlib; no hand-coded formulas or magic numbers
- **validate_proof.py result:** 16/16 checks PASS, 0 warnings

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
