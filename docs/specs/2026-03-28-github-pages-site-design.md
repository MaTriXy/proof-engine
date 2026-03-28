# Proof Engine — GitHub Pages Site

**Date:** 2026-03-28
**Status:** Draft

## Goal

Publish proof-engine proofs on a GitHub Pages site that serves three purposes:
1. **Save time** — visitors can read verified proofs without re-running them
2. **Machine-readable facts** — AI agents can fetch credible, validatable facts via JSON without re-running research
3. **Promote the project** — showcase what proof-engine does through real examples

## Audiences

Equal weight between **humans** (researchers, journalists, curious visitors) and **AI agents** (fetching structured proof data). The site must serve both well: a human-friendly UI with machine-readable structured data.

## Architecture

### Build System

A single Python build script (`tools/build-site.py`) that:
- Walks `site/proofs/` for proof triplets (proof.py, proof.md, proof_audit.md)
- Parses the JSON summary block from each proof.py
- Renders markdown to HTML via Python-Markdown
- Applies keyword-based auto-tagging (with optional meta.yaml override)
- Generates all pages from Jinja2 templates
- Outputs to `_site/` for GitHub Pages

**Dependencies:** Jinja2, Python-Markdown, PyYAML. No framework.

### Source Directory Structure

```
site/
├── proofs/
│   └── {slug}/
│       ├── proof.py
│       ├── proof.md
│       ├── proof_audit.md
│       └── meta.yaml          # optional: tags, featured, author overrides
├── templates/
│   ├── base.html
│   ├── landing.html
│   ├── catalog.html
│   ├── tag.html
│   ├── proof.html
│   ├── methodology.html
│   └── submit.html
├── static/
│   ├── style.css
│   └── catalog.js             # client-side filtering
└── content/
    ├── methodology.md         # rendered from DESIGN.md + hardening-rules.md
    └── submit.md              # PR-based contribution guide
```

### Output Structure

```
_site/
├── index.html                 # landing page
├── index.json                 # global catalog (all proofs with metadata)
├── catalog/index.html         # filterable catalog page
├── methodology/index.html     # how proofs work, why trustworthy
├── submit/index.html          # PR-based contribution guide
├── tags/
│   └── {tag}/index.html       # paginated list (50/page) per tag
├── proofs/
│   └── {slug}/
│       ├── index.html         # proof detail page
│       ├── proof.json         # machine-readable proof summary
│       └── proof.py           # downloadable source
└── static/
    ├── style.css
    └── catalog.js
```

## Page Types (7)

### 1. Landing Page (`/`)

Hero section with project description, aggregate stats (total proofs, verification rate, domains covered), featured/curated proofs, and CTAs to browse the catalog or install the skill.

### 2. Catalog Page (`/catalog/`)

Lists all proofs as cards showing: claim text, verdict badge, tags, generation date. Client-side filtering via `index.json` — filter by tag, verdict, or free-text search. Scales to several thousand proofs without architectural change.

### 3. Tag Pages (`/tags/{tag}/`)

All proofs with a given tag. Paginated at 50 per page. One set of pages per tag. Proofs can appear under multiple tags.

### 4. Proof Detail Page (`/proofs/{slug}/`)

The core page. Top to bottom:

1. **Breadcrumb** — with tag links
2. **Verdict banner** — color-coded (green=proved, red=disproved, yellow=undetermined), verification summary (citation count, hardening rule pass rate)
3. **Trust context bar** — one-line explanation of Proof Engine, links to: Methodology, GitHub repo, Re-run instructions, Submit your own
4. **Claim as title** — with tags and generation date
5. **Key Findings** — 3-4 bullet points from proof.md
6. **Evidence Summary** — fact table (ID, fact description, verified/computed status)
7. **Proof Logic** — narrative reasoning section from proof.md
8. **Expandable Audit Trail** — collapsible panels pulling from proof_audit.md:
   - Citation Verification Details (per-citation status, method, fetch mode)
   - Computation Traces (explain_calc/compare output)
   - Adversarial Checks (counter-queries and findings)
   - Hardening Checklist (7/7 rule results)
   - Source Credibility (domain tier assessments)
9. **Downloads** — proof.py download, View on GitHub link, proof.json link

### 5. Methodology Page (`/methodology/`)

Static page rendered from DESIGN.md and hardening-rules.md content. Explains:
- What proof-engine is and the problem it solves
- The three-artifact proof structure
- The 7 hardening rules and why each exists
- How citation verification works
- How to re-run a proof locally

### 6. Submit Page (`/submit/`)

PR-based contribution guide:
- Prerequisites: valid proof triplet, validate_proof.py passes, all 7 rules pass
- Steps: fork, add proof to `site/proofs/{slug}/`, validate locally, open PR
- Optional meta.yaml format (tags, author, featured flag)
- CI validates automatically on PR; maintainer reviews and merges

### 7. JSON Layer (Machine-Readable)

**Global catalog (`/index.json`):**
```json
{
  "generated": "2026-03-28T12:00:00Z",
  "proof_engine_version": "0.9.0",
  "total": 95,
  "proofs": [
    {
      "slug": "us-dollar-purchasing-power",
      "claim": "The US dollar has lost more than 95% of its purchasing power since 1913",
      "verdict": "PROVED",
      "tags": ["economics", "inflation", "federal-reserve"],
      "date": "2025-01-15",
      "url": "/proofs/us-dollar-purchasing-power/",
      "json_url": "/proofs/us-dollar-purchasing-power/proof.json"
    }
  ]
}
```

**Per-proof (`/proofs/{slug}/proof.json`):**
Extracted directly from proof.py's `=== PROOF SUMMARY (JSON) ===` block. Contains: `fact_registry`, `claim_formal`, `verdict`, `key_results`, `citations`, `cross_checks`, `adversarial_checks`, `extractions`.

**JSON-LD in HTML:**
Every proof detail page embeds Schema.org `ClaimReview` markup in the `<head>` for search engine and agent discoverability.

## Tagging System

**Keyword-based auto-tagger** assigns tags from the claim text using a maintained keyword-to-tag mapping:
- `"GDP"`, `"inflation"`, `"CPI"` → `economics`
- `"neuron"`, `"brain"`, `"cortex"` → `neuroscience`
- `"founded"`, `"war"`, `"treaty"` → `history`
- etc.

**Author override:** `meta.yaml` in the proof directory can specify exact tags. If present, these replace auto-assigned tags entirely.

**New tags** emerge organically — no predefined taxonomy required. Tag pages are generated for every tag that has at least one proof.

## Deployment

**GitHub Actions workflow** (`deploy-site.yml`):
1. Triggered on push to `main` when files in `site/` change
2. Installs Python dependencies (Jinja2, Python-Markdown, PyYAML)
3. Runs `tools/build-site.py`
4. Deploys `_site/` to GitHub Pages via `actions/deploy-pages`

**CI validation for proof submissions:**
The existing `validate.yml` workflow is extended to also run `validate_proof.py` on any new proofs added to `site/proofs/` in PRs.

## Content Sources

### Initial corpus
- 2 example proofs from `docs/examples/` (purchasing-power-decline, cortical-plasticity)
- Eval results from `eval-results/` (90+ proofs) — only proofs with `.success` markers are candidates. The build script runs `validate_proof.py` on each and skips any that fail. No manual review gate for eval imports; validation is the quality gate.

### Ongoing
- Curated proofs added by maintainers
- Community submissions via PR

## Design Decisions

**Why Python build script, not a framework:**
The project is Python-native. A custom script gives full control over the JSON-LD generation, the expandable audit sections, and the proof.py JSON extraction. The page types are few and well-defined — a framework would add complexity without proportional benefit.

**Why tagging over fixed domains:**
Proofs often span multiple domains. Tags are an array in JSON (easy for agents), grow organically with community submissions, and don't require taxonomy curation.

**Why PR-based submissions over a form:**
Zero infrastructure to build. The audience (proof-engine users) is already comfortable with git. CI validates automatically. A form or CLI tool can be added later if submission volume justifies it.

**Why expandable audit sections over tabs:**
The summary is what most readers want. Keeping the audit trail on the same page (collapsible) reinforces transparency — one scroll away, not a navigation step away.

## Scalability

- **Individual proof pages** are static HTML — scales to any number
- **Catalog page** uses client-side filtering over `index.json` — works well to ~5K proofs
- **Tag pages** are paginated at 50/page — scales indefinitely
- **Beyond ~5K proofs:** shard `index.json` by first letter or add server-side search. Not needed initially.

## Out of Scope (v1)

- Server-side search or API
- User accounts or authentication
- Automated proof re-running on the site
- Form-based or CLI-based submission
- Comments or discussion on proofs
- RSS/Atom feed (easy to add later)
- Dark/light theme toggle (ship dark only, matching GitHub aesthetic)
