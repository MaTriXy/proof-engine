# Audit: "Math washing" a spreadsheet (presenting empirical observations as universal theorems) is valid scientific practice.

- Generated: 2026-03-28
- Reader summary: [proof.md](proof.md)
- Proof script: [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Math washing (presenting empirical spreadsheet observations as universal theorems) |
| Property | Constitutes valid scientific practice |
| Operator | >= |
| Threshold | 3 |
| Proof direction | disprove |
| Operator note | 'Valid scientific practice' is interpreted as methodology meeting the standards recognized by the scientific community: specifically, the hypothetico-deductive model requiring hypothesis formation, falsifiability, and controlled testing. The DISPROOF threshold is 3 independent authoritative sources that confirm that presenting empirical observations alone as universal theorems—without hypothesis formation, testing for falsifiability, and independent replication—violates these standards. 'Universal theorem' is interpreted in the strict sense: a claim that holds without exception for all instances, not merely a statistical regularity or empirical generalization. A threshold of 3 is used to require broad expert consensus; a single contrary source would be insufficient. |

*Source: proof.py JSON summary*

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_britannica_popper | Britannica: Popper's falsifiability criterion — scientific validity requires falsifiability |
| B2 | source_sep_scientific_method | Stanford Encyclopedia of Philosophy: scientific method requires reasoning beyond observation |
| B3 | source_catalog_of_bias | Catalog of Bias: data-dredging is a recognized methodological distortion in science |
| A1 | — (computed) | Count of authoritative sources confirming math-washing is not valid scientific practice |

*Source: proof.py JSON summary*

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Count of authoritative sources confirming math-washing is not valid scientific practice | count(verified citations) = 3 | 3 sources confirmed (threshold: 3) |

*Source: proof.py JSON summary*

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | Popper's falsifiability criterion | Encyclopaedia Britannica — criterion of falsifiability | https://www.britannica.com/topic/criterion-of-falsifiability | "a theory is genuinely scientific only if it is possible in principle to establish that it is false." | verified | full_quote | Tier 3 (reference) |
| B2 | Scientific method requires reasoning beyond observation | Stanford Encyclopedia of Philosophy — scientific method | https://plato.stanford.edu/entries/scientific-method/ | "In addition to careful observation, then, scientific method requires a logic as a system of reasoning for properly arranging, but also inferring beyond, what is known by observation." | verified | full_quote | Tier 4 (academic) |
| B3 | Data-dredging is a methodological distortion | Catalog of Bias — data-dredging bias | https://catalogofbias.org/biases/data-dredging-bias/ | "A distortion that arises from presenting the results of unplanned statistical tests as if they were a fully prespecified course of analyses." | verified | full_quote | Tier 2 (unknown) |

*Source: proof.py JSON summary*

---

## Citation Verification Details

**B1 — Encyclopaedia Britannica:**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

**B2 — Stanford Encyclopedia of Philosophy:**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

**B3 — Catalog of Bias:**
- Status: verified
- Method: full_quote
- Coverage: N/A (full match)
- Fetch mode: live

*Source: proof.py JSON summary*

---

## Computation Traces

```
  Confirmed sources: 3 / 3
  verified source count vs disproof threshold: 3 >= 3 = True
```

*Source: proof.py inline output (execution trace)*

---

## Independent Source Agreement (Rule 6)

| Description | Sources consulted | Sources verified | Agreement |
|-------------|------------------|-----------------|-----------|
| Multiple independent authoritative sources consulted (Britannica, SEP, Catalog of Bias) | 3 | 3 | All verified |

**Independence note:** Sources are from different institutions and traditions: encyclopedic philosophy (Britannica), academic philosophy reference (Stanford Encyclopedia), and medical/scientific methodology catalog (Oxford-affiliated Catalog of Bias). Each addresses a distinct failure mode of math-washing: falsifiability failure (B1), insufficiency of observation alone (B2), and data-dredging distortion (B3).

*Source: proof.py JSON summary*

---

## Adversarial Checks (Rule 5)

**Check 1: Is there a scientific tradition that validates presenting inductive generalizations from data as universal laws without further testing?**
- Searched: "defense inductive reasoning empirical observations sufficient universal scientific laws" and "Bacon inductivism valid science pattern observation"
- Finding: Even Bacon's inductivism — the strongest defense of inductive science — requires systematic collection, replication, and elimination of observer bias before generalizing. Naive inductivism has been largely discredited in philosophy of science (Popper, 1934; Hempel, 1965). No form of inductivism endorses presenting patterns as universal 'theorems' (a term implying deductive necessity) rather than empirical generalizations.
- Breaks proof: No

**Check 2: Does Exploratory Data Analysis (EDA) validate presenting spreadsheet patterns as scientific findings?**
- Searched: "Tukey exploratory data analysis purpose hypothesis generation not confirmation"
- Finding: EDA (Tukey 1977) is an explicitly hypothesis-generating practice, not hypothesis-confirming. Tukey's framework is designed to produce candidate hypotheses for subsequent testing, not to generate universal theorems. This supports the disproof: the EDA literature itself distinguishes pattern-finding from universal claims.
- Breaks proof: No

**Check 3: Could 'math washing' be valid in limited empirical domains like actuarial science, empirical economics, or physics phenomenology?**
- Searched: "stylized facts empirical economics vs universal law", "actuarial science empirical observation universal theorem"
- Finding: Empirical economics explicitly distinguishes between 'stylized facts' (regularities observed in data) and 'economic laws' or theorems. Kaldor (1961) introduced 'stylized facts' precisely because observed patterns in data do NOT constitute universal theorems without theoretical grounding. Even in phenomenological physics, empirical regularities (e.g., Kepler's laws) were only elevated to scientific law status after being derived from deeper theoretical principles (Newton's mechanics). No domain endorses presenting data patterns as universal theorems directly.
- Breaks proof: No

*Source: proof.py JSON summary*

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | britannica.com | reference | 3 | Established reference source |
| B2 | stanford.edu | academic | 4 | Academic domain (.edu) |
| B3 | catalogofbias.org | unknown | 2 | Unclassified domain — verify source authority manually |

**Note on B3 (Tier 2):** catalogofbias.org is the online home of the Catalog of Bias project, affiliated with the University of Oxford's Centre for Evidence-Based Medicine (CEBM). The domain is unclassified by the automated credibility system, but the project is an established academic resource in evidence-based medicine. The conclusion does not depend solely on B3 — B1 (Tier 3) and B2 (Tier 4) independently support the disproof.

*Source: proof.py JSON summary; tier-2 note is author analysis*

---

## Extraction Records

For this qualitative proof, extractions record citation verification status rather than numeric values:

| ID | Value (status) | Countable (verified/partial) | Quote snippet |
|----|----------------|------------------------------|---------------|
| B1 | verified | Yes | "a theory is genuinely scientific only if it is possible in principle to establis..." |
| B2 | verified | Yes | "In addition to careful observation, then, scientific method requires a logic as ..." |
| B3 | verified | Yes | "A distortion that arises from presenting the results of unplanned statistical te..." |

*Source: proof.py JSON summary*

---

## Hardening Checklist

| Rule | Status | Notes |
|------|--------|-------|
| Rule 1: No hand-typed extracted values | N/A — qualitative proof, no numeric extraction | Citation verification status is machine-computed |
| Rule 2: Citations verified by fetching | PASS — all 3 citations verified live | verify_all_citations() run against live URLs |
| Rule 3: System time for date logic | N/A — no time-dependent computation | date.today() imported but not used for claims |
| Rule 4: Explicit claim interpretation | PASS | CLAIM_FORMAL with operator_note present |
| Rule 5: Adversarial checks independent | PASS | 3 adversarial hypotheses searched independently |
| Rule 6: Cross-checks from independent sources | PASS | 3 sources from different institutions and traditions |
| Rule 7: No hard-coded constants/formulas | PASS | compare() used; no inline formulas |
| validate_proof.py | PASS (14/15, 1 warning fixed) | Warning about missing else branch was resolved |

*Source: proof.py inline output (execution trace); author analysis*

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
