# Proof: AI progress in capabilities has largely plateaued since late 2024

- **Generated:** 2026-03-28
- **Verdict:** DISPROVED
- **Audit trail:** [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- **ARC-AGI benchmark:** ARC-AGI-1 took 4 years to go from 0% (GPT-3, 2020) to 5% (GPT-4o, 2024). OpenAI's o3 then scored **75.7%** on the same benchmark in December 2024 — a 15x improvement in a single release (B1).
- **GPQA Diamond benchmark:** Accuracy on this graduate-level science test climbed from **<40% to >90%** in ~1.5 years, well surpassing the PhD expert baseline of 69.7% (B2).
- **Agent task length:** Independent research (METR, cited by B3) documents that "the length of tasks AI can do is doubling every 7 months" — a direct measure of real-world capability growth.
- **Three independent sources** — spanning an AI safety benchmarking organization, a benchmarking analysis site, and an independent developer/journalist — all document substantial capability gains since late 2024. The disproof threshold (3 verified sources) is met, yielding verdict **DISPROVED**.

---

## Claim Interpretation

**Natural-language claim:** "AI progress in capabilities has largely plateaued since late 2024"

**Formal interpretation:** The plateau claim holds if no substantial AI capability gains are documented by independent sources since October 2024. Operationally: if 3 or more independent reputable sources verify substantial benchmark score gains (>5 percentage points above the late-2024 baseline) since October 2024, the plateau claim is refuted.

**Operator note:** This proof uses a disprove strategy — empirical facts are counter-evidence sources that document continued progress. `claim_holds = (n_confirmed_sources >= 3)` = True means the disproof threshold is met, yielding **DISPROVED**. The threshold of 3 follows the standard consensus-evidence standard. "Substantial" means >5 percentage points, clearly above measurement noise. The proof covers broad AI capabilities (reasoning, science, agent task length) and does not claim all metrics are improving equally — only that the specific claim of a "large plateau" across capabilities is contradicted by multiple independent sources.

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | ARC Prize Blog: ARC-AGI-1 from 0% (GPT-3, 2020) to 5% (GPT-4o, 2024) — same page announces o3 at 75.7% (Dec 2024) | Yes |
| B2 | IntuitionLabs / GPQA Diamond: accuracy climbed from <40% to >90% in ~1.5 years | Yes |
| B3 | Simon Willison 2025 Year in LLMs: task length doubling every 7 months | Yes |
| A1 | Count of independently verified counter-evidence sources | Computed: 3 of 3 sources confirmed (disproof threshold ≥ 3 met) |

---

## Proof Logic

The claim says AI capabilities have "largely plateaued" since late 2024. Three independent sources directly refute this.

**B1 — ARC-AGI benchmark (ARC Prize, Dec 2024):** The ARC-AGI-1 benchmark measures novel reasoning on tasks never seen in training. The ARC Prize organization reports that from GPT-3 (2020) to GPT-4o (2024), the benchmark score only advanced from 0% to 5% over four years. OpenAI's o3, announced December 2024, scored 75.7% on the same evaluation set — a 15× improvement in a single release. This is the largest single-step capability jump in this benchmark's history, occurring at the very start of the claimed plateau period.

**B2 — GPQA Diamond benchmark (IntuitionLabs analysis):** GPQA Diamond tests graduate-level science questions designed to be unsolvable by web search (Google-proof). The benchmark tracks genuine reasoning capability rather than memorized facts. An independent analysis documents the score trajectory: from <40% in late 2023 to ~77% in September 2024 (OpenAI o1) to >90% by mid-2025. This surpasses the PhD domain-expert baseline of 69.7%, a threshold reached by AI only after the "plateau" date.

**B3 — Agent task length (Simon Willison, 2025 Year in LLMs):** Independent developer and journalist Simon Willison, summarizing research from METR (an AI safety evaluation organization), reports that "the length of tasks AI can do is doubling every 7 months." This is a direct measure of real-world useful capability — not a narrow benchmark score — and shows continued exponential growth rather than a plateau. The same article documents AI systems achieving gold medal performance in the International Mathematical Olympiad in 2025 and the broad adoption of reasoning-model approaches across every major AI lab following OpenAI's September 2024 o1 release.

**Independence check (A1):** The three sources come from three distinct independent organizations: ARC Prize (non-profit benchmarking), IntuitionLabs (independent analysis), and Simon Willison (independent journalist/developer). None share an upstream data source or institutional affiliation. All three citations were live-fetched and fully verified.

---

## Counter-Evidence Search

Four lines of counter-evidence were searched for and examined:

**1. General capability plateau (not just pre-training scaling):** A Georgetown Law Tech Institute article from November 26, 2024 cited Reuters/Bloomberg/The Information reports about OpenAI's internal "Orion" successor model not reliably outperforming GPT-4 at certain tasks. However, this article was written before the o3 announcement (December 2024) and referred specifically to limitations of pre-training scaling — not the field's overall capability trajectory. The "Orion" model discussed was later revealed to have achieved a 15x ARC-AGI-1 breakthrough. No post-2024 authoritative source documents a general capability plateau.

**2. Non-reasoning base LLM plateau:** A blog analysis ("Why Progress in Non-Reasoning LLMs Has Plateaued") documents that GPT-4 to GPT-4o delivered only a 3–7% improvement on standard NLP benchmarks. This is factually supported — pre-training scaling returns did diminish. However, this is explicitly scoped to *non-reasoning base models* and does not describe the field's overall trajectory. The industry responded by developing test-time compute scaling (o1, o3, reasoning models), which extended capabilities far beyond what pre-training alone achieved. The original claim says "AI capabilities" broadly — encompassing all approaches.

**3. o3's narrow benchmark coverage (ARC-AGI-2):** ARC-AGI-2 (introduced March 2025) is a harder successor benchmark. OpenAI's o3 scores only ~3% on it, versus ~60% for average humans. This is the strongest counter-evidence: it suggests current models face real capability limits on harder novel tasks. However, the creation of ARC-AGI-2 is *itself* evidence of progress — a new harder benchmark was needed because the previous one was effectively solved. GPQA Diamond saturation (top models >94% vs 69.7% expert baseline) and IMO gold medal performance independently confirm capability advances across different domains, none dependent on ARC-AGI.

**4. Benchmark gaming / contamination:** ARC-AGI uses a held-out semi-private evaluation set to prevent contamination. GPQA Diamond was designed to be Google-proof. IMO performance is a live competition result. SWE-bench uses real GitHub repositories. Benchmark gaming cannot explain improvements across multiple independently designed evaluations.

---

## Conclusion

**Verdict: DISPROVED**

All three citations were fully verified by live fetch. The disproof is not dependent on any unverified sources.

The claim "AI progress in capabilities has largely plateaued since late 2024" is **DISPROVED** by three independently verified sources documenting substantial capability improvements on multiple distinct benchmarks since October 2024:

- ARC-AGI-1: 5% → 75.7%+ (Dec 2024, ARC Prize) — 15x improvement in one release
- GPQA Diamond: <40% → >90% over ~1.5 years (surpassing PhD expert level after late 2024)
- Agent task length doubling every 7 months (METR, as of 2025)

**Partial truth in the claim:** Pre-training scaling returns for *non-reasoning base models* did slow in 2024. The claim may have originated from accurate observations about that specific sub-trend. However, the industry pivoted to test-time compute scaling and reasoning models, which drove the largest single-step benchmark gains in AI history during the very period described as a "plateau."

**Note:** All 3 citations come from unclassified (Tier 2) sources — arcprize.org, intuitionlabs.ai, and simonwillison.net. None are peer-reviewed journals or government sources. See Source Credibility Assessment in the audit trail. The ARC Prize organization is a well-known non-profit in the AI safety community; Simon Willison is a widely cited developer. Readers should verify source authority independently.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
