# Proof: Current AI systems in 2026 have near-zero hallucinations and human-level reasoning across most domains.

- **Generated:** 2026-03-31
- **Verdict:** DISPROVED
- **Audit trail:** [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- **AI hallucination rates are far from near-zero:** The Vectara Hallucination Leaderboard (2025) shows Gemini-3-pro at 13.6% and all major frontier models (Claude Sonnet 4.5, GPT-5, GPT-OSS-120B, Grok-4, DeepSeek-R1) above 10% — more than an order of magnitude above any "near-zero" threshold.
- **AI falls dramatically short of human-level reasoning on rigorous benchmarks:** ARC-AGI-3 (launched March 26, 2026) shows every tested frontier model scoring below 1% against a human baseline of 100%; the best commercial AI scored 0.37%.
- **Expert-domain accuracy exposes the gap:** On Humanity's Last Exam (a 2,500-question test spanning 100+ academic disciplines), GPT-4o achieved 2.7% and o1 achieved only 8% — far below expert human performance.
- **Both sub-claims are independently disproved by 3 verified sources each:** 6 of 6 citations verified live with full-quote matching; no counter-evidence found that overturns either finding.

---

## Claim Interpretation

**Natural language claim:** "Current AI systems in 2026 have near-zero hallucinations and human-level reasoning across most domains."

This is a compound AND claim with two independently verifiable sub-claims:

**SC1 — Near-zero hallucinations:** Interpreted as: AI systems in 2026 have hallucination rates below ~1% across general-purpose tasks. This is a disproof — at least 2 independent sources must confirm rates are substantially higher. "Near-zero" is operationalized as the sub-1% threshold because that is the only region where some task-specific AI results cluster; general-purpose rates well above this constitute a clear refutation.

**SC2 — Human-level reasoning across most domains:** Interpreted as: AI reasoning capability reaches or exceeds human performance across the majority of knowledge and reasoning domains, not just narrow specialized tasks. Disproof requires at least 2 independent sources showing AI substantially below human-level on recognized multi-domain benchmarks. "Most domains" is given its natural reading — the unqualified claim cannot be satisfied by performance on a small subset of tasks.

Both sub-claims must be disproved for the compound verdict to be DISPROVED. The evidence disproves both.

*Source: proof.py JSON summary*

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | SC1 — Duke Univ. Libraries (Jan 2026): LLMs still hallucinate | Yes |
| B2 | SC1 — Vectara Hallucination Leaderboard (2025): top models >10% rate | Yes |
| B3 | SC1 — OpenAI SimpleQA paper (arXiv 2411.04368): benchmark for factual failures | Yes |
| B4 | SC2 — The Decoder (Mar 2026): ARC-AGI-3, all frontier models <1% | Yes |
| B5 | SC2 — ARC Prize 2025 results: best AI 37.6% vs 100% human baseline | Yes |
| B6 | SC2 — The Conversation (2025): Humanity's Last Exam, GPT-4o at 2.7% | Yes |
| A1 | SC1 verified source count (disproof of near-zero hallucinations) | Computed: 3 of 3 sources verified |
| A2 | SC2 verified source count (disproof of human-level reasoning claim) | Computed: 3 of 3 sources verified |

*Source: proof.py JSON summary*

---

## Proof Logic

### SC1: AI systems do NOT have near-zero hallucinations

The disproof of SC1 requires independent evidence that AI hallucination rates remain significantly above zero in 2026. Three independent sources confirm this.

Duke University Libraries published a January 2026 blog post reporting that "LLMs still make stuff up. When I talk to Duke students, many describe first-hand encounters with AI hallucinations – plausible sounding, but factually incorrect AI-generated info." (B1). This is qualitative confirmation that hallucinations remain a well-documented, first-hand-encountered problem in 2026.

The Vectara Hallucination Leaderboard (B2) provides the strongest quantitative evidence: as of 2025, Gemini-3-pro has a 13.6% hallucination rate, and Claude Sonnet 4.5, GPT-5, GPT-OSS-120B, Grok-4, and DeepSeek-R1 all exceed 10%. No major frontier model is near zero on general tasks.

OpenAI's SimpleQA benchmark paper (B3) — a benchmark specifically designed to measure whether models "know what they know" — states the authors hope it "will remain relevant for the next few generations of frontier models," explicitly anticipating that factual-accuracy failures will persist as an unsolved problem.

All three sources are from different institutions (Duke, Vectara, OpenAI), verified live, and report the same finding: AI hallucination rates remain substantial. SC1 is disproved by 3 confirmed sources against a threshold of 2.

### SC2: AI systems do NOT have human-level reasoning across most domains

The disproof of SC2 requires evidence of substantial AI-to-human performance gaps across multiple domains. Three independent benchmarks confirm this.

ARC-AGI-3 (launched March 26, 2026) is an interactive reasoning benchmark where untrained humans achieve 100% (by benchmark design). Every frontier model tested scored below 1%: Gemini 3.1 Pro Preview at 0.37%, GPT 5.4 at 0.26%, Opus 4.6 at 0.25%, Grok-4.20 at 0.00% (B4). This benchmark specifically tests novel abstract reasoning — the ability to face a new task and solve it independently — which is a core property of general intelligence.

ARC-AGI-2 (the 2025 competition) shows the same pattern at a slightly less extreme level. The best verified commercial model, Opus 4.5 (Thinking, 64k), achieved only 37.6% on ARC-AGI-2 at a cost of $2.20 per task (B5), against a human baseline of 100% established via a controlled study with 400+ participants.

Humanity's Last Exam (HLE), a 2,500-question test spanning 100+ academic disciplines, shows that when first released in early 2025, GPT-4o managed just 2.7% accuracy, Claude 3.5 Sonnet scored 4.1%, and OpenAI's most powerful model, o1, achieved only 8% (B6). By early 2026, top models had improved to 34–38% (Gemini 3 Pro, Claude Opus 4.6) — still far below the ~90% expert human baseline.

These three benchmarks cover distinct cognitive domains (novel abstract reasoning, interactive problem-solving, and breadth across 100+ academic fields) and all show the same large gap. SC2 is disproved by 3 confirmed sources against a threshold of 2.

*Source: author analysis*

---

## Counter-Evidence Search

**1. Do Vectara's sub-1% summarization rates support "near-zero hallucinations"?**

Investigated Vectara's Hallucination Leaderboard, which shows some top models achieving sub-1% rates on document summarization tasks specifically. Vectara explicitly labels these as "best-case scenario results" for a narrow task context. The same leaderboard shows the same frontier models at 10–14% hallucination on general tasks. Sub-1% rates are task-specific and cannot support a general claim of "near-zero hallucinations." This counter-evidence does not break the proof.

**2. Do saturated benchmarks (MMLU ~90%+, GSM8K ~97%) show human-level reasoning?**

AI achieves scores at or above average human performance on MMLU (~88–93% vs. ~89% human baseline) and GSM8K (~97% vs. ~90% human). However, MIT Technology Review (March 31, 2026) reports these benchmarks are saturated and compromised by training-data contamination — models that score 97% on GSM8K score substantially lower on novel GSM1K variants, suggesting partial memorization. ARC-AGI-3 (0.25–0.37% for all frontier models) and HLE (2.7–38% for top models vs. ~90% human) present the same models with challenges designed to prevent memorization, revealing the true gap. This counter-evidence does not break the proof.

**3. Could "most domains" be defined to include only AI's strongest areas?**

The claim specifies "most domains" without qualification. Even granting AI's best performance on coding competitions and standardized math tests, it clearly falls short in novel abstract reasoning (ARC-AGI-3 <1%), expert academic knowledge across 100+ disciplines (HLE 2.7–38%), legal reasoning (69–88% hallucination rate on court rulings), and medical reasoning (64% hallucination without mitigation). These domains collectively represent the majority of human cognitive domains. Narrow successes cannot satisfy "most." This counter-evidence does not break the proof.

*Source: proof.py JSON summary (adversarial_checks) and author analysis*

---

## Conclusion

**Verdict: DISPROVED**

Both sub-claims of the compound AND claim are individually disproved:

- **SC1 (near-zero hallucinations) DISPROVED:** 3 of 3 consulted sources confirmed live that AI hallucination rates in 2025–2026 remain far above zero. The Vectara Hallucination Leaderboard shows most frontier models above 10%; Duke University Libraries documents student encounters with hallucinations as recently as January 2026; and OpenAI's own SimpleQA benchmark was designed in anticipation that factual failures would persist across multiple future model generations.

- **SC2 (human-level reasoning across most domains) DISPROVED:** 3 of 3 consulted sources confirmed live that AI performance falls drastically below human-level on rigorous multi-domain benchmarks. ARC-AGI-3 (March 2026): all frontier models below 1% vs. 100% human. ARC-AGI-2 (2025): best AI 37.6% vs. 100% human. Humanity's Last Exam (2025): top initial models at 2.7–8%, best 2026 models at 34–38%, vs. ~90% expert human.

All 6 citations were verified live with full-quote matching; no citation failures. No counter-evidence found that overturns either finding.

Note: 3 citation(s) come from unclassified or low-credibility sources (B2 vectara.com, B4 the-decoder.com, B5 arcprize.org — all Tier 2). However, B2 is from the company that operates the Hallucination Leaderboard (primary source for its own data), B4 reports on a publicly verifiable benchmark result, and B5 is the official ARC Prize website reporting its own competition results. The disproof is independently supported by verified Tier 3–4 sources (B1 duke.edu, B3 arxiv.org, B6 theconversation.com), so the verdict does not depend solely on Tier-2 sources. See Source Credibility Assessment in the audit trail.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.3.1 on 2026-03-31.*
