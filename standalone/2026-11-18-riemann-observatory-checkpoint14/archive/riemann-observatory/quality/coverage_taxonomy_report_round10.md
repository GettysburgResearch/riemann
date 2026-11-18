# Coverage taxonomy and reading depth

Historical cutoff 2026-11-18. The export covers 1011 canonical paper IDs and 0 separately marked pending contributor IDs. The taxonomy summarizes evidence already recorded in the archive. The family assignments carry their actual field, reason and provenance.

Existing family tags are preserved in the original field. Title and topic mappings are metadata inferences, including when the record also reports a complete reading. A separate primary-scope label uses a documented passage or read scope specific to that family. The G table admits substantial failed research routes and documented withdrawals. Original G tags without that evidence are shown in the per-paper ledger as preserved, withheld from the G count. Local typos and theorem qualifications do not trigger G.

The historical bucket uses the exact archive year field, with separate before-1859, post-cutoff-year and undated categories. The year follows the record's work/version identity. Readings and accesses count from their independent fields. Family rows overlap. Historical rows are disjoint. Both tables use selected works.

[Per-paper taxonomy](coverage_taxonomy_round10.jsonl) · [Full cross-tabs](coverage_taxonomy_crosstabs_round10.csv) · [Input pins and summary](coverage_taxonomy_summary_round10.json) · [Exact area rules](coverage_taxonomy_rules_round10.json) · [Reviewed scope overrides](coverage_taxonomy_scope_overrides_round10.jsonl)

## Canonical input

| family | Selected | Full text | Primary excerpt | Whole read | Level 0 | Level 1 | Level 2 | Level 3 | Unknown level |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A · Classical analysis | 424 | 411 | 3 | 58 | 366 | 54 | 0 | 4 | 0 |
| B · Zeros and statistics | 317 | 311 | 1 | 50 | 267 | 48 | 0 | 2 | 0 |
| C · Equivalent criteria | 94 | 87 | 1 | 28 | 66 | 24 | 0 | 4 | 0 |
| D · Spectral and operator approaches | 132 | 117 | 9 | 20 | 112 | 18 | 0 | 2 | 0 |
| E · Geometry, arithmetic and L-functions | 216 | 210 | 2 | 23 | 193 | 21 | 0 | 2 | 0 |
| F · Dynamics and alternative analysis | 118 | 114 | 2 | 22 | 96 | 20 | 0 | 2 | 0 |
| G · Documented failed or disputed approaches | 3 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| H · Adjacent methods | 189 | 185 | 3 | 22 | 167 | 22 | 0 | 0 | 0 |
| unclassified | 12 | 8 | 0 | 0 | 12 | 0 | 0 | 0 | 0 |

| stratum | Selected | Full text | Primary excerpt | Whole read | Level 0 | Level 1 | Level 2 | Level 3 | Unknown level |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| before_1859 | 4 | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 |
| 1859–1900 | 11 | 11 | 0 | 5 | 6 | 4 | 0 | 1 | 0 |
| 1901–1950 | 52 | 40 | 1 | 12 | 40 | 12 | 0 | 0 | 0 |
| 1951–1980 | 81 | 70 | 5 | 16 | 65 | 16 | 0 | 0 | 0 |
| 1981–2000 | 82 | 75 | 2 | 15 | 67 | 13 | 0 | 2 | 0 |
| 2001–2015 | 296 | 288 | 1 | 32 | 264 | 29 | 0 | 3 | 0 |
| 2016–2023 | 286 | 280 | 4 | 25 | 261 | 23 | 0 | 2 | 0 |
| 2024–2026-11-18 | 198 | 197 | 0 | 26 | 172 | 25 | 0 | 1 | 0 |
| after_cutoff_year | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undated | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Gaps and next priorities

- In 1859–1900 the archive has 11 full texts and 5 complete readings among 11 selected works. In 1901–1950 it has 40 full texts and 12 complete readings among 52. Prioritize full original-language readings alongside missing source retrieval. The historical review identifies specific original locators, and the provider triage separates original contributions from compendia and translations. [Historical source notes](../papers/geometry64_historical_sources_notes.md) · [Source triage](../corpus/curated_candidate_decisions_round10.jsonl)
- The largest absolute gaps between full text and whole reading are A (411 full texts, 58 whole readings), B (311 full texts, 50 whole readings), E (210 full texts, 23 whole readings). Use the family-by-stratum cross-tabs and recorded source locators to choose new technical reconstructions. Keep scoped proof reviews and complete-work audit levels separate.

- Review unclassified and metadata-only assignments from the source title and indicated mathematical sections during the next reading pass. The G cases withheld from coverage need source-level justification for the failure or controversy. Previously documented local issues keep their findings scope.

The ledger contains 221 explicit-family evidence entries, 1498 metadata inferences, 168 primary-scope entries and 1 explicit publication-status entries. Pending multi-track identities held for the canonical builder: 0.

Rebuild after canonical integration with `python scripts/build_coverage_taxonomy.py`. Add `--preview-tracks` to include noncanonical contributor rows separately. The command writes only this taxonomy and its report and tabulation.
