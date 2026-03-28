# Audit: Detox diets and juice cleanses actually remove toxins from the body.

- **Generated:** 2026-03-28
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| subject | Detox diets and juice cleanses |
| property | actually remove toxins from the body beyond what normal organ function achieves |
| operator | >= |
| threshold | 3 |
| proof_direction | disprove |
| operator_note | The claim asserts that commercial detox diets and juice cleanses have a real, measurable effect on removing toxins — beyond what the liver, kidneys, and other organs already do. We disprove this by showing that 3 or more independent authoritative medical/scientific sources explicitly state there is no clinical evidence for this mechanism. threshold=3 applies the standard consensus bar: three independently verified sources from different institutions must confirm the disproof. |

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | urmc | URMC: detoxing through diet is a myth |
| B2 | pubmed_review | PubMed review: no compelling clinical evidence for detox diet toxin elimination |
| B3 | harvard_health | Harvard Health: cannot cleanse body through diet, per scientific reality |
| B4 | cleveland_clinic | Cleveland Clinic: no scientific research proving cleanses offer claimed health benefits |
| A1 | — | Verified source count |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Verified source count | count(verified citations) = 4 | 4 independent sources confirmed |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | URMC: detoxing through diet is a myth | University of Rochester Medical Center — Do Juice Cleanses Detox the Body? | https://www.urmc.rochester.edu/news/publications/health-matters/do-juice-cleanses-detox-the-body | "No. The concept of detoxing by eating or drinking certain diets is a myth." | verified | full_quote | Tier 4 (academic) |
| B2 | PubMed review: no compelling clinical evidence | PubMed — Detox diets for toxin elimination and weight management: a critical review of the evidence (2015) | https://pubmed.ncbi.nlm.nih.gov/25522674/ | "there is very little clinical evidence to support the use of these diets" | verified | full_quote | Tier 5 (government) |
| B3 | Harvard Health: medical literature yields no high-quality evidence | Harvard Health — Harvard Health Ad Watch: What's being cleansed in a detox cleanse? | https://www.health.harvard.edu/blog/harvard-health-ad-watch-whats-being-cleansed-in-a-detox-cleanse-2020032519294 | "Searching the medical literature for \"detox diets\" or \"cleanse diets\" yields almost no relevant, high-quality medical evidence demonstrating health benefits." | verified | full_quote | Tier 4 (academic) |
| B4 | Cleveland Clinic: research doesn't support detox claims | Cleveland Clinic — Detox or Cleanse? What To Know Before You Start | https://health.clevelandclinic.org/detox-cleanse | "Research doesn't support many health claims linked to detoxification programs" | verified | full_quote | Tier 3 (reference) |

---

## Citation Verification Details

**B1 — URMC**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Impact: N/A — verified

**B2 — PubMed systematic review (NIH)**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Impact: N/A — verified

**B3 — Harvard Health**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Impact: N/A — verified

**B4 — Cleveland Clinic**
- Status: verified
- Method: full_quote
- Fetch mode: live
- Impact: N/A — verified

---

## Computation Traces

```
  Confirmed sources: 4 / 4
  verified source count vs threshold: 4 >= 3 = True
```

---

## Independent Source Agreement (Rule 6)

| Description | n consulted | n verified | Agreement |
|-------------|------------|------------|-----------|
| Multiple independent sources from different institutions consulted | 4 | 4 | All agree |

**Sources:**
- urmc: verified
- pubmed_review: verified
- harvard_health: verified
- cleveland_clinic: verified

**Independence note:** Sources are from four different institutions: University of Rochester Medical Center, PubMed/academic peer review (NIH-indexed journal), Harvard Medical School, and Cleveland Clinic — all independently rejecting the claim.

---

## Adversarial Checks (Rule 5)

**Check 1:** Are there any clinical studies showing detox diets effectively remove toxins?

- Verification performed: Searched PubMed and Google Scholar for clinical studies showing that commercial detox diets or juice cleanses measurably remove toxins. The 2015 systematic review (B2) acknowledged that "a handful of clinical studies have shown that commercial detox diets enhance liver detoxification and eliminate persistent organic pollutants from the body," but explicitly concluded these studies are "hampered by flawed methodologies and small sample sizes" and that "no randomised controlled trials have been conducted to assess the effectiveness of commercial detox diets in humans." No high-quality RCT evidence was found.
- Finding: A small number of low-quality studies with positive results exist, but the peer-reviewed consensus (B2) is that these are methodologically flawed and no RCTs have been conducted. The existence of weak, flawed studies does not constitute credible clinical evidence and does not break the disproof.
- Breaks proof: No

**Check 2:** Could "detox" refer to a clinically recognized process that some diets support?

- Verification performed: Searched for medical definitions of "detoxification" in the context of diet. URMC (B1) states "The liver and kidneys remove toxins and waste. If we were holding onto toxins, we wouldn't be alive." Cleveland Clinic (B4) states the body's digestive tract, liver, kidneys, and skin break down toxins daily without special cleanses. Harvard Health (B3) notes "it's not even clear what toxin or toxins a cleanse is supposed to remove." The term "toxins" in detox marketing is consistently found to be undefined and unverifiable.
- Finding: Medical authorities confirm the body performs toxin elimination via liver/kidneys continuously. The term "toxins" in commercial detox marketing is undefined and no specific toxin has been shown to be measurably reduced by detox diets. Does not break the disproof.
- Breaks proof: No

---

## Source Credibility Assessment

| Fact ID | Domain | Type | Tier | Note |
|---------|--------|------|------|------|
| B1 | rochester.edu | academic | 4 | Academic domain (.edu) |
| B2 | nih.gov | government | 5 | Government domain (.gov) — NIH/PubMed |
| B3 | harvard.edu | academic | 4 | Academic domain (.edu) |
| B4 | clevelandclinic.org | reference | 3 | Established reference source |

All sources are tier 3 or above. No low-credibility sources cited.

---

## Extraction Records

For qualitative/consensus proofs, extractions record citation verification status per source rather than extracted numeric values.

| Fact ID | Value (status) | Countable | Quote snippet |
|---------|---------------|-----------|---------------|
| B1 | verified | Yes | "No. The concept of detoxing by eating or drinking certain diets is a myth." |
| B2 | verified | Yes | "there is very little clinical evidence to support the use of these diets" |
| B3 | verified | Yes | "Searching the medical literature for \"detox diets\" or \"cleanse diets\" yields alm..." |
| B4 | verified | Yes | "Research doesn't support many health claims linked to detoxification programs" |

**Extraction method:** For qualitative consensus proofs, no numeric values are parsed. Each source's evidence is the citation verification status itself — a source is counted toward the disproof threshold only if its quote was confirmed present on the live page (status = "verified" or "partial").

---

## Hardening Checklist

| Rule | Status |
|------|--------|
| Rule 1: Every empirical value parsed from quote text, not hand-typed | N/A — qualitative proof; no numeric values extracted from quotes |
| Rule 2: Every citation URL fetched and quote checked | PASS — all 4 citations verified live (full_quote method) |
| Rule 3: System time used for date-dependent logic | PASS — `date.today()` used for `generated_at` |
| Rule 4: Claim interpretation explicit with operator rationale | PASS — CLAIM_FORMAL with operator_note present |
| Rule 5: Adversarial checks searched for independent counter-evidence | PASS — 2 adversarial checks; both found non-breaking evidence |
| Rule 6: Cross-checks used independently sourced inputs | PASS — 4 sources from 4 different institutions |
| Rule 7: Constants and formulas imported from computations.py, not hand-coded | PASS — `compare()` imported from scripts.computations |
| validate_proof.py result | PASS — 15/15 checks, 0 issues, 0 warnings |

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v1.0.0 on 2026-03-28.*
