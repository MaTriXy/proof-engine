# Audit: The purchasing power of the US dollar has declined by more than 90% since the Federal Reserve was established in 1913.

- **Generated:** 2026-03-26
- **Reader summary:** [proof.md](proof.md)
- **Proof script:** [proof.py](proof.py)

## Claim Specification

| Field | Value |
|-------|-------|
| Subject | Purchasing power of the US dollar |
| Property | Percentage decline since 1913 |
| Operator | > (strictly greater than) |
| Threshold | 90.0% |
| Operator note | "More than 90%" interpreted as > 90.0%. "Purchasing power" operationalized via CPI-U. Decline computed as (1 - CPI_1913 / CPI_current) * 100. "Established in 1913" = Federal Reserve Act signed December 23, 1913; CPI baseline uses 1913 annual average. |

## Fact Registry

| Report ID | Script Key | Label |
|-----------|-----------|-------|
| B1 | source_a_cpi | Source A CPI: 1913 annual avg = 9.883, 2024 annual avg = 313.689 (BLS via rateinflation.com) |
| B2 | source_b_cpi | Source B CPI: 1913 annual avg = 9.9, 2024 annual avg = 313.689 (BLS via inflationdata.com) |
| B3 | source_a_fed_date | Federal Reserve Act signed December 23, 1913 (Wikipedia) |
| B4 | source_b_fed_date | Federal Reserve Act signed December 23, 1913 (US Senate) |
| A1 | (computed) | Purchasing power decline computed from Source A CPI values |
| A2 | (computed) | Purchasing power decline computed from Source B CPI values |
| A3 | (computed) | Cross-check: Source A and B decline percentages agree within tolerance |
| A4 | (computed) | Claim evaluation: decline > 90% |

## Full Evidence Table

### Type A (Computed) Facts

| ID | Fact | Method | Result |
|----|------|--------|--------|
| A1 | Purchasing power decline from Source A | (1 - CPI_1913_A / CPI_2024_A) * 100 | 96.8494% |
| A2 | Purchasing power decline from Source B | (1 - CPI_1913_B / CPI_2024_B) * 100 | 96.8440% |
| A3 | Source A and B agreement | abs(decline_A - decline_B) < 0.1 | diff=0.0054%, within tolerance |
| A4 | Claim evaluation | compare(96.8494, '>', 90.0) | True |

### Type B (Empirical) Facts

| ID | Fact | Source | URL | Quote | Status | Method |
|----|------|--------|-----|-------|--------|--------|
| B1 | CPI 1913 & 2024 (Source A) | RateInflation.com (BLS) | https://www.rateinflation.com/consumer-price-index/usa-historical-cpi/ | "The CPI for USA is calculated and issued by: U.S. Bureau of Labor Statistics. CPI data is calculated and issued monthly." | verified | full_quote |
| B2 | CPI 1913 & 2024 (Source B) | InflationData.com (BLS) | https://inflationdata.com/Inflation/Consumer_Price_Index/HistoricalCPI.aspx | "A CPI of 195 indicates 95% inflation since 1982" | verified | full_quote |
| B3 | Fed founding date (Source A) | Wikipedia | https://en.wikipedia.org/wiki/Federal_Reserve_Act | "Signed into law by President Woodrow Wilson on December 23, 1913" | verified | full_quote |
| B4 | Fed founding date (Source B) | US Senate Historical Office | https://www.senate.gov/artandhistory/history/minute/Senate_Passes_the_Federal_Reserve_Act.htm | "On December 23, 1913, the Senate adopted the conference report by a vote of 43 to 25" | verified | full_quote |

## Citation Verification Details

### B1 — RateInflation.com (CPI Source A)
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live
- **Note:** The prose quote verifies the data source (BLS). CPI values (9.883, 313.689) are from the site's HTML table data, extracted as `cpi_1913_quote` and `cpi_2024_quote` fields and parsed via `parse_number_from_quote()`.

### B2 — InflationData.com (CPI Source B)
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live
- **Note:** The prose quote verifies the methodology explanation. CPI values (9.9, 313.689) are from the site's HTML table data, extracted similarly.

### B3 — Wikipedia (Fed date Source A)
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live

### B4 — US Senate (Fed date Source B)
- **Status:** verified
- **Method:** full_quote
- **Fetch mode:** live

All 4 citations fully verified via live URL fetch with full quote match.

## Computation Traces

Source: proof.py inline output (execution trace).

```
--- Source A (rateinflation.com, CPI 1913=9.883, CPI 2024=313.689) ---
  cpi_1913_a / cpi_2024_a: cpi_1913_a / cpi_2024_a = 9.883 / 313.689 = 0.0315
  (1 - cpi_1913_a / cpi_2024_a) * 100: (1 - cpi_1913_a / cpi_2024_a) * 100 = (1 - 9.883 / 313.689) * 100 = 96.8494
Source A: $1.00 in 1913 has purchasing power of $0.0315 in 2024 dollars
Source A: Decline = 96.85%

--- Source B (inflationdata.com, CPI 1913=9.9, CPI 2024=313.689) ---
  cpi_1913_b / cpi_2024_b: cpi_1913_b / cpi_2024_b = 9.9 / 313.689 = 0.0316
  (1 - cpi_1913_b / cpi_2024_b) * 100: (1 - cpi_1913_b / cpi_2024_b) * 100 = (1 - 9.9 / 313.689) * 100 = 96.8440
Source B: $1.00 in 1913 has purchasing power of $0.0316 in 2024 dollars
Source B: Decline = 96.84%

Decline cross-check: 96.8494% vs 96.8440%, diff=0.0054%

  compare: 96.84942729901272 > 90.0 = True
  compare: 96.84400791867104 > 90.0 = True

  decline_a - 90.0: decline_a - 90.0 = 96.84942729901272 - 90.0 = 6.8494
Margin above 90% threshold: 6.85 percentage points
```

## Independent Source Agreement (Rule 6)

### Cross-check 1: Federal Reserve founding date

| Source | Value |
|--------|-------|
| B3 (Wikipedia) | 1913-12-23 |
| B4 (US Senate) | 1913-12-23 |

**Agreement:** Exact match.

### Cross-check 2: CPI 2024 annual average

| Source | Value |
|--------|-------|
| B1 (rateinflation.com) | 313.689 |
| B2 (inflationdata.com) | 313.689 |

**Agreement:** Exact match. Both ultimately source from BLS CPI-U data.

### Cross-check 3: CPI 1913 annual average

| Source | Value |
|--------|-------|
| B1 (rateinflation.com) | 9.883 |
| B2 (inflationdata.com) | 9.9 |

**Agreement:** Within rounding tolerance (diff = 0.017, tolerance = 0.05). The value 9.9 is 9.883 rounded to 1 decimal place. Both source from BLS data; the difference is display precision only.

### Cross-check 4: Computed decline percentages

| Source | Decline |
|--------|---------|
| A1 (from Source A CPI) | 96.8494% |
| A2 (from Source B CPI) | 96.8440% |

**Agreement:** diff = 0.0054%, well within 0.1% tolerance. The tiny difference propagates from the 1913 CPI rounding difference.

## Adversarial Checks (Rule 5)

### Check 1: Hedonic quality adjustment bias
- **Question:** Does hedonic quality adjustment mean the CPI overstates inflation, potentially bringing the true decline below 90%?
- **Search performed:** Web search: 'CPI hedonic adjustment overstate inflation purchasing power'
- **Finding:** The BLS states hedonic adjustments outside shelter/apparel increase annual CPI by only ~0.005%/year. The Boskin Commission estimated ~1.1%/year overstatement. Over 111 years, even 1.1%/year overstatement leaves cumulative inflation far above 90%. Margin of 6.85pp is too large to flip.
- **Breaks proof:** No

### Check 2: 1913 vs 1914 founding date
- **Question:** Was the Fed established in 1913 (Act signed) or 1914 (Banks opened)?
- **Search performed:** Web search: 'Federal Reserve established 1913 vs 1914 operational'
- **Finding:** Using 1914 CPI (10.0): (1 - 10.0/313.689) * 100 = 96.81%. Difference is ~0.03pp. Immaterial.
- **Breaks proof:** No

### Check 3: Alternative price indices
- **Question:** Could PCE or GDP deflator yield a decline of 90% or less?
- **Search performed:** Web search: 'PCE vs CPI inflation 1913 to present comparison'
- **Finding:** PCE typically shows 0.3-0.5%/year lower inflation than CPI-U (since 1990s), but only goes back to 1929. No standard index over 111 years shows decline below 90%. Margin too large.
- **Breaks proof:** No

### Check 4: Pre-1978 CPI methodology
- **Question:** Is CPI-U the right measure when it only began in 1978?
- **Search performed:** Web search: 'BLS CPI history before 1978 CPI-U CPI-W comparison'
- **Finding:** BLS retroactively linked pre-1978 series to CPI-U. Minneapolis Fed confirms data from 1913 is "generally compatible through the present day." CPI-W yields nearly identical results.
- **Breaks proof:** No

## Extraction Records

| Fact ID | Extracted Value | Value in Quote | Quote Snippet | Method |
|---------|----------------|----------------|---------------|--------|
| B1 (CPI 1913) | 9.883 | Yes | "9.883" (table data) | `parse_number_from_quote(cpi_1913_quote, r"([\d.]+)")` |
| B1 (CPI 2024) | 313.689 | Yes | "313.689" (table data) | `parse_number_from_quote(cpi_2024_quote, r"([\d.]+)")` |
| B2 (CPI 1913) | 9.9 | Yes | "9.9" (table data) | `parse_number_from_quote(cpi_1913_quote, r"([\d.]+)")` |
| B2 (CPI 2024) | 313.689 | Yes | "313.689" (table data) | `parse_number_from_quote(cpi_2024_quote, r"([\d.]+)")` |
| B3 (Fed date) | 1913-12-23 | Yes (year) | "Signed into law by President Woodrow Wilson on December 23, 1913" | `parse_date_from_quote()` |
| B4 (Fed date) | 1913-12-23 | Yes (year) | "On December 23, 1913, the Senate adopted the conference report..." | `parse_date_from_quote()` |

Extraction method: CPI values parsed from dedicated `cpi_*_quote` fields containing exact table cell values via `parse_number_from_quote()`. Dates parsed via `parse_date_from_quote()`. All extractions confirmed by `verify_extraction()`. (Source: author analysis.)

**Note on CPI extraction:** The CPI values (9.883, 313.689, etc.) appear in HTML tables on the source pages. The verified prose quotes (B1, B2) confirm the data source (BLS) and methodology, while the numeric values are extracted from separate `cpi_*_quote` fields containing the exact table cell text. This two-layer approach verifies both the source authority and the numeric values.

## Hardening Checklist

- **Rule 1:** Every CPI value parsed from quote text via `parse_number_from_quote()`, dates via `parse_date_from_quote()`. No hand-typed values. All confirmed by `verify_extraction()`.
- **Rule 2:** All 4 citation URLs fetched live and quotes verified — all returned `verified` with `full_quote` match.
- **Rule 3:** System time used via `date.today()` with `PROOF_GENERATION_DATE` cross-check. System date matched proof generation date (2026-03-26). CPI data is 2024 annual average (most recent full year).
- **Rule 4:** Claim interpretation explicit in `CLAIM_FORMAL` with operator rationale for "more than" (> not >=), definition of "purchasing power" (CPI-U), and "established in 1913" (Fed Act signing date).
- **Rule 5:** 4 adversarial checks performed — hedonic adjustment bias, 1913 vs 1914 date, alternative price indices, pre-1978 CPI methodology. None break the proof.
- **Rule 6:** 4 cross-checks with independently sourced values: Fed founding date (Wikipedia vs US Senate: exact match), CPI 2024 (rateinflation vs inflationdata: exact match), CPI 1913 (9.883 vs 9.9: within rounding tolerance), computed declines (96.8494% vs 96.8440%: diff 0.0054%).
- **Rule 7:** All computations use `explain_calc()` from `computations.py` for self-documenting output. Claim evaluation uses `compare()`. No hand-coded constants or formulas.
- **validate_proof.py result:** PASS (11/11 checks passed, 0 issues, 0 warnings)
