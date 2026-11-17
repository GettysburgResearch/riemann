# Coverage report

Search cutoff: **2026-11-17**. All counts are exact and generated from the archive data by script; categories are cumulative only where stated.

## Funnel: discovered → accessed → read → audited

| Stage | Count | Definition |
|---|---|---|
| zbMATH records harvested | 24876 (in 27 queries) | raw API records, with overlaps |
| arXiv records harvested | 5737 (in 30 queries) | raw API records, with overlaps |
| Candidate pool (deduplicated) | 20166 | unique works after zbMATH/arXiv merge and citation expansion |
| Expert seed works | 1422 listed, 1356 verified at Level 0 automatically | nine independent family lists; verification against pool, zbMATH, Crossref, arXiv |
| Candidate bibliography triaged | 3373 | every one has a decision and reason in corpus/selection_decisions.csv |
| Triage decisions | include 1453, borderline 696, reject 1224 | index-content triage (title, metadata, arXiv abstract, zbMATH review) |
| **Selected corpus** | **1000** | coverage floors per family and stratum (methodology §4) |
| Level 1 attempted | 231 | full-text reading attempted |
| Level 1 full text read | 108 | main statements and proof architecture extracted with locations |
| Level 1 partial text | 46 | partial text (OCR limits, chapters, abstracts of long works) |
| No legitimate open full text | 77 | record stays at L0/L0+ |
| Index-content records (L0+) | 373 | content from arXiv abstract / zbMATH review only |
| Metadata-level records (L0) | 473 | bibliographic record; any content is labelled title/metadata-only or unverified recollection |

Level-2/3 audits are listed separately in `quality/evidence_audit.md` and `audits/` (they target specific claims, not whole papers).

## Selected corpus by family (multi-label)

| Family | Works | of which L1 (full or partial) |
|---|---|---|
| A Classical analytic NT | 424 | 64 |
| B Zeros and statistics | 343 | 62 |
| C Equivalent formulations | 204 | 33 |
| D Spectral/operator | 114 | 21 |
| E Geometry/arithmetic/L-functions | 241 | 38 |
| F Dynamical/alternative | 121 | 15 |
| G Failed/controversial/corrections | 48 | 5 |
| H Adjacent mathematics | 64 | 3 |

## Selected corpus by historical stratum

| Stratum | Works | L1 (full or partial) |
|---|---|---|
| S0 pre-1859 antecedents | 4 | 0 |
| S1 1859–1900 | 16 | 6 |
| S2 1901–1950 | 139 | 21 |
| S3 1951–1980 | 134 | 11 |
| S4 1981–2000 | 207 | 17 |
| S5 2001–2015 | 217 | 43 |
| S6 2016–2023 | 182 | 43 |
| S7 2024–2026-11-17 | 101 | 13 |

## Work types and languages

Work types: original_paper 786, survey 53, monograph 53, preprint 45, computation_report 34, lecture_notes 6, correction_or_comment 5, thesis 5, textbook 4, collection 4, other 4, failed_or_withdrawn_attempt 1.

Languages (index metadata): English 731, unknown 158, French 52, German 49, Russian 7, Swedish 3.

## Identifiers

DOI: 728; arXiv: 376; zbMATH: 912; none: 50.

## Theorem database

1635 statements from 154 works (732 lemmas); 265 intra-paper dependency edges. Statement scope (main results): asymptotic 404, global 273, conditional 131, finite 52, computational 30, local 13.

## Rejected candidates

Reasons: peripheral_application 536, low_relevance 403, generic_reference 151, low_quality_claim 43, duplicate_or_translation 42, out_of_scope_other_zeta 20, insufficient_metadata 17, superseded_survey 12. Not-selected includes/borderlines are listed with the reason "below fill threshold" or "duplicate of …".

