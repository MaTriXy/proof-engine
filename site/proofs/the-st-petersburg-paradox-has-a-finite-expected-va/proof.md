# Proof: The St. Petersburg paradox has a finite expected value that a rational person should be willing to pay.

- **Generated:** 2026-03-28
- **Verdict:** DISPROVED
- **Audit trail:** [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- The standard St. Petersburg game has an **infinite** expected monetary value, not finite: every term of the series equals 1, so E[X] = 1 + 1 + 1 + … = ∞.
- The claim's premise ("finite expected value") is **mathematically false** — this is precisely why it is called a paradox.
- Under Bernoulli's (1738) logarithmic utility, the expected *utility* is finite: E[ln(2^N)] = 2·ln(2) ≈ 1.3863, and the **certainty equivalent is exactly $4** — the most a rational risk-averse agent with log utility should pay.
- The compound claim fails because SC1 (finite EV) is false; SC2 (finite rational willingness to pay) is true but via expected *utility* theory, not expected *value*.

---

## Claim Interpretation

**Natural language:** "The St. Petersburg paradox has a finite expected value that a rational person should be willing to pay."

**Formal decomposition:**

- **SC1:** The expected monetary value E[X] is finite. This requires the series Σ (1/2)^n · 2^n to converge. *Verdict: DISPROVED — the series diverges.*
- **SC2:** A rational person should be willing to pay only a finite amount. This requires expected utility theory to produce a finite certainty equivalent. *Verdict: PROVED — under Bernoulli's log utility, CE = $4.*

**Why the compound claim is DISPROVED:** SC1 is false. The claim's framing — calling the resolution value a "finite expected value" — is terminologically wrong. The correct term is *certainty equivalent* (or *expected utility*). The compound claim ("SC1 AND SC2") fails because SC1 fails.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| A1 | SC1: (1/2)^n · 2^n = 1 for every n; series = sum of infinitely many 1s | Computed: all 20 terms verified = 1.0; series diverges |
| A2 | SC1 cross-check: partial sums grow as N (unbounded), confirming divergence | Computed: 10-term sum = 10.0, 20-term sum = 20.0 (N-term sum = N) |
| A3 | SC2: E[ln(2^N)] = ln(2)·sum(n·(1/2)^n) = ln(2)·2 = 2·ln(2) (finite) | Computed: E[U] = 1.386294 = 2·ln(2); certainty equivalent = $4.000000 |
| A4 | SC2 cross-check: generating function confirms sum(n·(1/2)^n) = 2 | Computed: x/(1-x)² at x=0.5 = 2.0 exactly |
| B1 | Wikipedia: St. Petersburg paradox — game rules and infinite expected value | Yes |
| B2 | Stanford Encyclopedia of Philosophy — Bernoulli utility resolution | Yes |

---

## Proof Logic

### SC1: The Expected Value is Infinite

The St. Petersburg game pays 2^n dollars if the first heads appears on flip n (probability (1/2)^n). The expected value is:

> E[X] = Σ_{n=1}^∞ P(heads on flip n) · payout(n) = Σ_{n=1}^∞ (1/2)^n · 2^n

**Key observation (A1):** Each term simplifies exactly:

> (1/2)^n · 2^n = (1/2 · 2)^n = 1^n = **1**

So E[X] = 1 + 1 + 1 + … = ∞. This is not an approximation — every term equals exactly 1.0 (verified computationally for n = 1 through 20).

Wikipedia confirms: "The expected payoff of the lottery game is infinite" (B1).

**Cross-check (A2):** The N-term partial sum equals N exactly. The 10-term sum is 10.0; the 20-term sum is 20.0. Partial sums grow linearly without bound — the series does not converge.

SC1 is **DISPROVED**: the claim of "finite expected value" is mathematically false.

### SC2: A Rational Person's Willingness to Pay is Finite ($4)

Bernoulli (1738) proposed that rational agents maximize *expected utility*, not expected monetary value. Under logarithmic utility U(w) = ln(w) (A3, B2):

> E[U] = E[ln(2^N)] = Σ_{n=1}^∞ (1/2)^n · n · ln(2) = ln(2) · Σ_{n=1}^∞ n · (1/2)^n

**Key computation (A4):** By the generating function identity Σ_{n=1}^∞ n·x^n = x/(1−x)², evaluated at x = 1/2:

> Σ_{n=1}^∞ n · (1/2)^n = (1/2) / (1/2)² = 0.5 / 0.25 = **2.0** (exactly)

Therefore (A3):

> E[U] = ln(2) · 2 = **2·ln(2) ≈ 1.3863** (finite)

The certainty equivalent — the amount w such that ln(w) = E[U] — is:

> CE = exp(2·ln(2)) = exp(ln(4)) = **$4.00** (exactly)

A rational agent with log utility should pay at most $4 to play the game. This is finite. SC2 is **PROVED**.

**Cross-check:** Numerical summation of 10,000 terms converges to 1.38629436, matching the analytical value 2·ln(2) = 1.38629436 exactly.

---

## Counter-Evidence Search

**1. Is there a framework where the standard St. Petersburg EV is finite?**
No peer-reviewed source claims the standard game (unlimited flips, payoff = 2^n) has finite expected value. Bounded-payoff and finite-wealth-cap variants are different games and do not apply here. The divergence is mathematical consensus.

**2. Could "expected value" in the claim mean "expected utility"?**
In standard probability and economics, "expected value" is a precisely defined technical term: E[X] = Σ p_i·x_i. Even under the most charitable reading, the correct term for the $4 quantity is *certainty equivalent* or *expected utility*. The claim's terminology is wrong regardless of interpretation.

**3. Does Menger's (1934) super-St.-Petersburg paradox undermine SC2?**
Menger showed that for any unbounded utility function (including log), a game with payoff exp(2^n) has infinite expected utility. This does not break SC2: SC2 applies only to the *standard* St. Petersburg game (payoff = 2^n). For that game, log utility gives a finite CE = $4. Menger's extended game is a separate paradox.

**4. Is log utility the only resolution?**
No. Any CRRA utility with risk-aversion coefficient γ > 0 gives a finite certainty equivalent for the standard game. This *strengthens* SC2 — the finiteness of rational willingness to pay is robust across frameworks. The exact $4 figure is specific to Bernoulli's log utility with zero initial wealth.

---

## Conclusion

**Verdict: DISPROVED.**

The claim that the St. Petersburg paradox "has a finite expected value" is mathematically false. The expected monetary value is infinite (E[X] = Σ 1 = ∞), which is precisely the source of the paradox. No credible source disputes this.

What *is* finite is the *expected utility* under Bernoulli's (1738) logarithmic utility model, and the resulting certainty equivalent of **$4.00** — the most a rational risk-averse agent should pay. But this is a statement about expected *utility*, not expected *value*. The claim's framing confuses these two distinct concepts, making it false as stated.

Both supporting citations (B1: Wikipedia, B2: Stanford Encyclopedia of Philosophy) were independently verified.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
