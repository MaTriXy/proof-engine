# Audit: You must eat animal protein to meet daily protein needs effectively.

- Generated: 2026-03-28
- Reader summary: [proof.md](proof.md)
- Proof script: [proof.py](proof.py)

---

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Animal protein |
| Property | Necessity for meeting daily protein needs |
| Operator | >= |
| Threshold | 3 (minimum confirmed independent sources) |
| Proof direction | disprove |
| Operator note | The claim asserts an absolute requirement ('must'): that animal protein is necessary and cannot be substituted to meet daily protein needs. Interpretation: no well-planned plant-based diet can adequately provide all protein needs without animal sources. Proof direction: DISPROVE. We show that >= 3 independent authoritative sources confirm plant-based diets CAN meet daily protein needs without animal protein, which directly negates the absolute 'must' claim. A single verified exception (a well-planned plant-based diet meeting protein needs) is logically sufficient to disprove any 'must' claim — the source threshold of 3 establishes consensus, not merely a single outlier observation. |

---

## Fact Registry

| ID | Key | Label |
|----|-----|-------|
| B1 | source_and | Academy of Nutrition and Dietetics 2016 Position Paper on Vegetarian Diets (PubMed PMID 27886704) |
| B2 | source_pmc_review | Peer-reviewed review: Dietary Protein and Amino Acids in Vegetarian Diets (PMC6893534, Nutrients 2019) |
| B3 | source_cleveland | Cleveland Clinic: Do I Need to Worry About Eating Complete Proteins? |
| A1 | — | Count of authoritative sources confirmed by citation verification |

---

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Count of authoritative sources confirmed by citation verification | count(citation_results[key]['status'] in ('verified', 'partial')) | 3 of 3 sources confirmed |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method | Credibility |
|----|------|--------|-----|-------|--------|--------|-------------|
| B1 | Academy of Nutrition and Dietetics 2016 Position Paper | Journal of the Academy of Nutrition and Dietetics, Melina et al. 2016 (PMID 27886704) | https://pubmed.ncbi.nlm.nih.gov/27886704/ | "It is the position of the Academy of Nutrition and Dietetics that appropriately planned vegetarian, including vegan, diets are healthful, nutritionally adequate, and may provide health benefits for the prevention and treatment of certain diseases. These diets are appropriate for all stages of the life cycle, including pregnancy, lactation, infancy, childhood, adolescence, older adulthood, and for athletes." | verified | full_quote | Tier 5 (government) |
| B2 | Peer-reviewed review: Dietary Protein and Amino Acids in Vegetarian Diets | Nutrients 2019: Dietary Protein and Amino Acids in Vegetarian Diets — A Review (PMC6893534) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6893534/ | "there is no evidence of protein deficiency in vegetarian populations in western countries" | verified | full_quote | Tier 5 (government) |
| B3 | Cleveland Clinic: Complete Proteins | Cleveland Clinic Health Essentials: Complete Proteins | https://health.clevelandclinic.org/do-i-need-to-worry-about-eating-complete-proteins | "mixing and matching those protein sources can get you all the amino acids your body needs" | verified | full_quote | Tier 3 (reference) |

---

## Citation Verification Details

### B1 — Academy of Nutrition and Dietetics (PubMed)
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live
- **Credibility:** Tier 5 (government — nih.gov)

### B2 — PMC6893534 Systematic Review
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live
- **Credibility:** Tier 5 (government — nih.gov)

### B3 — Cleveland Clinic
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live
- **Credibility:** Tier 3 (reference — clevelandclinic.org)

---

## Computation Traces

```
Verifying citations...
  [✓] source_and: Full quote verified for source_and (source: tier 5/government)
  [✓] source_pmc_review: Full quote verified for source_pmc_review (source: tier 5/government)
  [✓] source_cleveland: Full quote verified for source_cleveland (source: tier 3/reference)
  Confirmed sources: 3 / 3
  verified source count vs threshold (proof_direction=disprove): 3 >= 3 = True
```

---

## Independent Source Agreement (Rule 6)

| Description | Sources Consulted | Sources Verified | Agreement |
|-------------|-------------------|-----------------|-----------|
| Multiple independent authoritative sources consulted | 3 | 3 | Yes — all 3 confirm plant-based protein adequacy |

**Independence note:** Sources are from three independent institutions:
1. Academy of Nutrition and Dietetics (professional dietetics body — Melina et al. 2016 position paper, published in the Journal of the Academy of Nutrition and Dietetics)
2. An independent peer-reviewed journal review (Nutrients/PMC — Mariotti & Gardner 2019, a systematic literature review)
3. Cleveland Clinic (major academic medical center — clinical guidance authored by a registered dietitian)

These represent independent research and expert consensus. They are not a single institution cited multiple times, and they draw on different bodies of literature.

---

## Adversarial Checks (Rule 5)

### Check 1
- **Question:** Does any meta-analysis or systematic review conclude that plant protein CANNOT meet protein needs, or that animal protein is physiologically required?
- **Search performed:** Searched PubMed and Google Scholar for 'animal protein required necessary protein deficiency vegan vegetarian meta-analysis systematic review'. Reviewed PMC7926405 (meta-analysis on animal vs plant protein for lean mass, 2021) and Nutrition Reviews 2025 (plant protein and muscle). No study concludes that protein needs cannot be met on plant-based diets. PMC7926405 found animal protein has a modest lean mass advantage in younger adults but states the result 'does not significantly impact gains in lean mass or muscle strength following resistance type exercise training' overall.
- **Finding:** No peer-reviewed meta-analysis or systematic review claims plant-based diets cannot meet protein needs. Studies note animal protein has higher bioavailability and leucine content, but none conclude plant protein is insufficient if adequate variety and quantity is consumed.
- **Breaks proof:** No

### Check 2
- **Question:** Is there scientific evidence that athletes or specific populations CANNOT meet protein needs on plant-only diets?
- **Search performed:** Searched for 'vegan athlete protein deficiency impossible' and 'plant-based diet protein inadequacy athletes systematic review'. The Gatorade Sports Science Institute review found: 'Muscle conditioning in athletes does not need to be compromised when adopting a plant-based diet as long as sufficient protein is consumed from a large variety of different plant-based protein sources.' The Academy of Nutrition and Dietetics explicitly states plant-based diets are appropriate 'for athletes'.
- **Finding:** Athletes can meet protein needs on plant-based diets. Sports science literature confirms adequacy with sufficient quantity and variety, negating any claim that animal protein is required even for high-demand populations.
- **Breaks proof:** No

### Check 3
- **Question:** Does the claim have merit if interpreted narrowly — e.g., does animal protein have bioavailability or amino acid score (DIAAS) advantages that make plant protein 'ineffective' for meeting needs?
- **Search performed:** Searched for 'DIAAS plant protein inadequate protein needs'. Animal proteins do generally score higher on the Digestible Indispensable Amino Acid Score (DIAAS). However, the Academy of Nutrition and Dietetics notes: 'Protein from a variety of plant foods, eaten during the course of a day, supplies enough of all indispensable (essential) amino acids when caloric requirements are met.' The terms 'complete' and 'incomplete' protein are described as 'misleading' in this context. The PMC6893534 review found lysine intakes in vegetarians were '58 and 43 mg/kg, respectively, largely higher than the 30 mg/kg estimated average requirement.'
- **Finding:** Animal protein has higher DIAAS scores, but plant proteins consumed in adequate variety and quantity meet all amino acid requirements in practice. Bioavailability differences do not render plant protein 'ineffective' for meeting daily protein needs — they may require slightly larger total intake. The 'must' framing remains false: plant protein can effectively meet protein needs.
- **Breaks proof:** No

---

## Source Credibility Assessment

| Source | Domain | Tier | Type | Notes |
|--------|--------|------|------|-------|
| B1 — PubMed/PMID 27886704 | nih.gov | 5 | Government | U.S. National Institutes of Health database; publishes peer-reviewed journal abstracts |
| B2 — PMC6893534 | nih.gov | 5 | Government | PubMed Central — NIH full-text archive of peer-reviewed biomedical literature |
| B3 — Cleveland Clinic | clevelandclinic.org | 3 | Reference | Major U.S. academic medical center; clinically reviewed health content |

No citations come from unclassified or low-credibility (tier ≤ 2) sources.

---

*Generated by [proof-engine](https://github.com/yaniv-golan/proof-engine) v0.10.0 on 2026-03-28.*
