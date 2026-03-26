# Environment and Source Handling

Read this when facing fetch failures, paywalled sources, or sandboxed environments.

## Environment-Specific Notes

- **Claude Code:** Has outbound HTTP from Python, so live fetch is the primary path. `verify_all_citations()` fetches URLs directly. WebFetch/WebSearch tools return processed summaries, NOT raw page text — do not use them to populate `snapshot` fields. Keep web research (Step 2) in the main conversation thread; subagents may not have web access.
- **ChatGPT:** Python sandbox has no outbound HTTP. Use the browsing capability during Step 2 to fetch each source page and include raw page text as the `snapshot` field in `empirical_facts`.
- **Other sandboxed environments:** If Python cannot fetch URLs, use the snapshot workflow — pre-fetch page text by any available means and embed it in `empirical_facts`.

## Verification Fallback Chain

1. **Live fetch** — try to fetch the URL directly. If successful, verify against live page.
2. **Snapshot** — if live fetch fails and a `snapshot` field is present, verify against the pre-fetched text. This is deterministic and user-provided.
3. **Wayback Machine** — if live and snapshot both fail and `wayback_fallback=True`, try the Wayback Machine archive. This is opt-in to avoid silently changing existing proof behavior.

## Fetch Result Statuses

- `verified` — quote found (full match or >=80% fragment coverage)
- `partial` — only a fragment matched (degraded verification)
- `not_found` — page fetched but quote not there (wrong quote or URL)
- `fetch_failed` — could not obtain page text by any method

## PDF Citations

When a URL returns a PDF, `verify_citation()` extracts text using `pdfplumber` or `PyPDF2` (optional dependencies). Install with `pip install pdfplumber` for PDF support.

## Handling Paywalled Sources

Many scientific papers and reports are behind paywalls. When a key source returns 403 or requires authentication:

1. **Try the abstract URL** — PubMed (pubmed.ncbi.nlm.nih.gov), DOI resolver (doi.org), or Google Scholar often have abstracts with key findings. Cite the abstract URL instead.
2. **Check for open-access versions** — many papers have preprints on arXiv, bioRxiv, medRxiv, or the author's institutional page.
3. **Cite the abstract quote** — if the abstract contains the key finding, that's a valid citation. Note "cited from abstract; full text behind paywall" in the audit doc.
4. **Find alternative sources** — if the claim is well-established, there are usually multiple sources. Prefer open-access ones.
5. **Last resort** — if the paywalled source is essential and no alternative exists, cite it with whatever quote is publicly visible and mark as "Not verified (paywall)" in the audit doc. This does not invalidate the proof if other verified sources support the same finding.

## Government Statistics Sites (.gov)

BLS, FRED, Federal Reserve, Census, and similar .gov sites systematically return 403 to automated fetching. This is the norm, not the exception. For government statistics:
- **Preferred:** Use reliable aggregators as citation URLs: rateinflation.com, inflationdata.com (for CPI); measuringworth.com, officialdata.org (for historical data); fred.stlouisfed.org (for FRED series). These are tier 3 (established reference) in credibility scoring.
- **Fallback:** Use the snapshot workflow — fetch via browser during Step 2, embed as `snapshot` in `empirical_facts`
- Note in the audit doc that aggregator sources republish data from the primary authority (e.g., "sourced from BLS via rateinflation.com")
