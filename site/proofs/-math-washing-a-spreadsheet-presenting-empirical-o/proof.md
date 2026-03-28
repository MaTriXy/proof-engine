# Proof: "Math washing" a spreadsheet (presenting empirical observations as universal theorems) is valid scientific practice.

- Generated: 2026-03-28
- Verdict: **DISPROVED**
- Audit trail: [proof_audit.md](proof_audit.md) | [proof.py](proof.py)

---

## Key Findings

- **3 out of 3** independent authoritative sources — Encyclopaedia Britannica, Stanford Encyclopedia of Philosophy, and the Catalog of Bias — confirm that presenting empirical observations as universal theorems (without falsifiability, hypothesis testing, and replication) violates core standards of scientific validity. (A1)
- **Popper's falsifiability criterion** (Britannica, B1): a theory is only genuinely scientific if it is possible to establish that it is false — ruling out patterns that were never exposed to disconfirmation.
- **The scientific method** (Stanford Encyclopedia, B2): valid science requires systematic reasoning that goes *beyond* what observation alone can establish — not just cataloging data.
- **Data-dredging** (Catalog of Bias, B3): presenting the results of unplanned statistical tests *as if* they were a prespecified analysis is a recognized methodological distortion that generates false positives.
- All three adversarial hypotheses — Baconian inductivism, Exploratory Data Analysis, and domain-limited empiricism — were searched and found not to support the claim.

---

## Claim Interpretation

**Natural language claim:** "Math washing" a spreadsheet (presenting empirical observations as universal theorems) is valid scientific practice.

**Formal interpretation:**

| Field | Value |
|-------|-------|
| Subject | Math washing (presenting empirical spreadsheet observations as universal theorems) |
| Property | Constitutes valid scientific practice |
| Operator | ≥ |
| Threshold | 3 independent authoritative sources confirming this practice violates scientific standards |
| Proof direction | Disprove |

**Operator rationale:** "Valid scientific practice" is interpreted as methodology meeting the standards recognized by the scientific community: specifically, the hypothetico-deductive model requiring hypothesis formation, falsifiability, and controlled testing. The disproof threshold requires 3 independent authoritative sources confirming that presenting empirical observations alone as universal theorems violates these standards. "Universal theorem" is interpreted in the strict sense: a claim that holds without exception for all instances, not merely a statistical regularity or empirical generalization. A threshold of 3 ensures broad expert consensus rather than relying on a single contrary voice.

*Source: proof.py JSON summary*

---

## Evidence Summary

| ID | Fact | Verified |
|----|------|----------|
| B1 | Britannica: Popper's falsifiability criterion — scientific validity requires falsifiability | Yes |
| B2 | Stanford Encyclopedia of Philosophy: scientific method requires reasoning beyond observation | Yes |
| B3 | Catalog of Bias: data-dredging is a recognized methodological distortion in science | Yes |
| A1 | Count of authoritative sources confirming math-washing is not valid scientific practice | Computed: 3 sources confirmed (threshold: 3) |

*Source: proof.py JSON summary*

---

## Proof Logic

The claim asserts that "math washing" — taking patterns observed in a spreadsheet and presenting them as universal theorems — constitutes valid scientific practice.

To disprove this, the proof establishes that this methodology violates the foundational standards of scientific validity as articulated by three independent authoritative sources:

**Falsifiability failure (B1):** Encyclopaedia Britannica states that "a theory is genuinely scientific only if it is possible in principle to establish that it is false." Patterns extracted from a spreadsheet and declared universal theorems have typically not been subjected to attempts at falsification. A claim derived solely by inspecting what a dataset shows has not been tested for what it forbids — it cannot predict what observations would contradict it. This directly fails Popper's demarcation criterion for science.

**Insufficiency of observation alone (B2):** The Stanford Encyclopedia of Philosophy states that "scientific method requires a logic as a system of reasoning for properly arranging, but also inferring beyond, what is known by observation." Observation is necessary but not sufficient. Valid scientific inference requires the superstructure of hypothesis formation, theoretical grounding, and systematic testing — all absent from raw pattern presentation.

**Data-dredging distortion (B3):** The Catalog of Bias defines data-dredging as "a distortion that arises from presenting the results of unplanned statistical tests as if they were a fully prespecified course of analyses." Math washing is structurally identical to this distortion: patterns identified post-hoc in a dataset are reframed as if they were predicted theorems. This practice generates false positives and is explicitly cataloged as a methodological error.

Together, these three sources cover the three main failure modes of math washing: it lacks falsifiability (B1), it over-extends what observation can establish (B2), and it misrepresents the analytical process as theory-driven when it is pattern-driven (B3). All three citations were fully verified on their live source pages (A1: 3/3 confirmed ≥ threshold of 3).

*Source: author analysis*

---

## Counter-Evidence Search

Three adversarial hypotheses were investigated before writing this proof:

**1. Is there a scientific tradition that endorses inductive generalization from data as universal law?**
Baconian inductivism (Francis Bacon's model) is the strongest historical candidate. However, even Bacon's framework requires systematic observation, replication, and elimination of observer bias. Naive inductivism has been largely discredited in philosophy of science (Popper 1934; Hempel 1965). No form of inductivism endorses labeling data patterns as universal *theorems* (a term implying deductive necessity) rather than empirical generalizations.

**2. Does Exploratory Data Analysis (EDA) validate presenting spreadsheet patterns as scientific findings?**
Tukey's EDA framework (1977) is an explicitly hypothesis-*generating* practice, not hypothesis-confirming. EDA is designed to produce candidate hypotheses for subsequent rigorous testing — not universal theorems. The EDA literature itself draws this distinction, supporting the disproof.

**3. Could math washing be valid in limited domains (actuarial science, empirical economics, physics phenomenology)?**
Empirical economics explicitly distinguishes "stylized facts" (data regularities) from theorems. Kaldor (1961) introduced "stylized facts" precisely because observed patterns do NOT constitute universal theorems without theoretical grounding. In physics, empirical regularities like Kepler's laws were only accepted as scientific law after derivation from deeper theoretical principles (Newton's mechanics). No domain endorses raw pattern-to-theorem promotion.

None of these adversarial checks found evidence that breaks or qualifies the disproof.

*Source: author analysis*

---

## Conclusion

**Verdict: DISPROVED**

Three independent authoritative sources — Encyclopaedia Britannica (B1), Stanford Encyclopedia of Philosophy (B2), and the Catalog of Bias (B3) — all confirmed (3/3, threshold ≥ 3) that presenting empirical observations as universal theorems without falsifiability testing, hypothesis formation, and independent replication violates the foundational standards of scientific validity. All three citations were fully verified on live source pages.

No adversarial search found a scientific tradition, framework, or domain that endorses direct pattern-to-universal-theorem inference from spreadsheet data. The practice of math washing fails the scientific method on at least three independent grounds: it lacks falsifiability (Popper), it over-extends what observation alone can establish (SEP), and it constitutes the recognized methodological distortion of data-dredging (Catalog of Bias).

**Note:** Citation B3 (catalogofbias.org) is classified as credibility tier 2 (unclassified domain). This source is published by a project affiliated with the University of Oxford's Centre for Evidence-Based Medicine (CEBM). The conclusion does not depend solely on B3 — it is independently supported by the fully verified tier-3 (B1) and tier-4 (B2) sources.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
