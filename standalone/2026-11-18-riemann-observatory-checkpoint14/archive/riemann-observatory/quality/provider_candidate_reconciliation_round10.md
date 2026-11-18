# Provider candidate identity and relevance review

18 November 2026. This review covers the existing 5,203 provider rows and their fixed discovery snapshots. The canonical bibliography used for the crosswalk contains 481 works. The crosswalk records identities and source locators without changing source-reading status, whole-work audit levels, canonical records, or earlier discovery and triage decisions.

## Crosswalk

| Measure | Count |
| --- | ---: |
| Provider candidates and matched originating OpenAlex cache records | 5,203 |
| Provisional work identity keys, including unresolved singletons | 5,162 |
| Provider rows linked by exact references to selected canonical records | 172 |
| Distinct selected canonical work IDs reached | 169 |
| Rows in additional exact provider-metadata clusters | 59 |
| Rows assigned provider-only identity keys | 4,972 |

Exact canonical links use an explicit candidate ID already recorded by the archive, exact DOI or arXiv base, or an exact stable source locator. The match records the canonical field that supplied the anchor. This identifies an existing record and its documented manifestation metadata. The access status shown for a canonical record belongs to that record. A linked provider row may refer to another edition, version or translation, so reading and proof scope still come from the canonical evidence.

Provider clusters use shared DOI/arXiv identifiers, recorded arXiv locations, registrant-issued version or identity relationships, recognized version suffixes, or exact journal serial identifiers with matching volume, first and last pages, title and author list. An exact normalized title and author list on its own stays as a review lead. Related-article, supplement, part-of and reference relations stay outside merger rules. The work keys use the canonical ID where available and an OpenAlex-based key anchored to a candidate in provisional clusters. If later evidence joins two provisional clusters, retain their former keys as aliases when recording that revision. [Crosswalk](../corpus/provider_candidate_work_crosswalk_round10.jsonl) · [Counts and input digests](../corpus/provider_candidate_reconciliation_round10.json)

## The 124 historical flags

| Review outcome | Groups | Rows |
| --- | ---: | ---: |
| Exact provider-metadata work or version group | 14 | 42 |
| Retained as distinct publication units | 7 | 15 |
| Version or duplicate identity remains unresolved | 32 | 67 |
| Total | 53 | 124 |

All 124 original flagged rows have a disposition and retain their original IDs and evidence references. The 67 unresolved rows are the remaining version-review backlog in this flagged subset. They remain individually represented in the provisional identity count. Consequently, 5,162 is a conservative count of assigned keys, rather than a certified count of distinct mathematical works or relevant papers. This also leaves arbitrary near-title matches outside the initial flags open to subsequent review.

For example, the DataCite concept DOI unifies the twelve “Number Arrow” provider rows as a version series, and the Figshare registration explicitly identifies arXiv:2609.38240. The Zhang records share a version root across two different title strings. In contrast, Carlitz–Chowla and Mordell have different bylines and publication locators. The Lubkin same-title records have disjoint starting pages. The Broughan and Goldfeld–Hundley same-title books have distinct volume identifiers. Matching titles on separate Zenodo concept DOIs remain unresolved without a registered link or a source comparison. [Flag review ledger](../corpus/provider_duplicate_flag_reviews_round10.jsonl)

The registry evidence contains one bounded request for each of 117 distinct flagged DOI strings. Seventy returned records were captured with their response hashes and relation fields. Four DataCite lookups returned 404 and 43 Crossref lookups were throttled. Those outcomes are request observations. The raw provider snapshots were independently checked against the discovery index before parsing their publication coordinates. [Registry observations](../corpus/provider_duplicate_registry_evidence_round10.jsonl) · [Discovery index](../corpus/raw_discovery_index.jsonl)

## Next source triage

The 42 new decisions use existing provider IDs and are disjoint from the older curated decisions and lexical exclusions. They comprise 35 priority metadata reviews, four explicit deferrals and three scope exclusions. Thirty-one have at least one provider-reported citing work that maps to a selected canonical record. Citation coverage is incomplete and the links are provider evidence for triage, not independent verification of a cited proof dependency.

Priorities emphasize known gaps in the historical chain and exact analytic inputs. They include Hadamard's 1893 entire-function memoir, Hutchinson and Lehmer's numerical records, the Selberg critical-line and Igusa correspondence routes, Bercovici–Foias's real-variable criterion, and mean square, mollifier, pair-correlation and zero-counting inputs. Every decision includes its own scope reason. Metadata review labels are separate from the earlier publisher-checked priority label. The old 56 lexical exclusions stay in their original file. [New decisions](../corpus/curated_candidate_decisions_round10.jsonl)

Rebuild the crosswalk from a stable archive working copy with the original raw provider snapshots available.

```bash
python scripts/reconcile_provider_candidates.py
```

The script reuses the saved registry observations and makes no network requests. It writes only the crosswalk, flag reviews and reconciliation summary. The sealed distribution can inspect those outputs without including raw discovery payloads. The manually scoped triage file remains separate from generated identity matches.
