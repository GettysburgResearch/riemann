# The Riemann Observatory

```text
Status: EXPLORATORY / IMPORTED literature archive with audits, campaigns and verified registers; no RH claim
Scope: Riemann Hypothesis research literature 1737 – 2026-11-17 (search cutoff 2026-11-17)
Exact sources or dependencies: zbMATH Open, arXiv, Crossref, open digitizations, the OpenAI math release (read-only), primary full texts listed per record
What was actually run: see quality/evidence_audit.md and logs/RUN_LOG.md
Smallest remaining gap: human expert review; Lean replays of 2026 formal claims; deeper reading of the 846 index-level records
```

**RH remains open.** This archive is a structured, evidence-graded map of the literature and the current frontier, built by an autonomous multi-agent program inside the GettysburgResearch RH repository. It contains audits of the most consequential recent claims, research campaigns with computations, and verified registers of records, connections, obstructions and findings. Every statement carries its evidence level; read [`methodology.md`](methodology.md) before citing anything.

**Start here:** [`START_HERE.md`](START_HERE.md) (one-day guide) · [`executive_report.md`](executive_report.md) · [`final_synthesis/comprehensive_report.md`](final_synthesis/comprehensive_report.md).

## What is inside

| Directory | Contents |
|---|---|
| [`corpus/`](corpus/) | 1,000 selected works (`bibliography.csv/.jsonl`), selection decisions with reasons for all 3,373 triaged candidates, access/audit manifest, 2024–2026 scan, Crossref metadata and correction notices |
| [`papers/`](papers/) | one record per work, `PAPER-0001.md` … `PAPER-1000.md`; 108 full-text (L1), 46 partial (L1-partial), 373 index-content (L0+), 473 metadata-level (L0) |
| [`theorems/`](theorems/) | 1,635 statements (with locations) from the 154 works actually read; intra-paper proof dependencies; notation and normalization dictionary |
| [`frontiers/`](frontiers/) | records ledger (232 records, 12 areas, each independently verified), research programmes (8 frontier questions per area), missing lemmas, obstruction atlas, unsolved questions |
| [`audits/`](audits/) | findings register; verified and unresolved findings; quasi-RH 11/12 audit; 2026 critical-line and Landau–Siegel audits; Level-2 flag audits; Lean replay plan |
| [`connections/`](connections/) | 39 cross-paper proposals with verifier verdicts; strongest connections; cross-field opportunities; repository–literature bridge (215 items) |
| [`history/`](history/) | chronological timeline, evolution of methods, abandoned approaches, 2024–2026 developments |
| [`experiments/`](experiments/) | code, results and reproducibility register (incl. 100,000 Arb-certified zeta zeros) |
| [`proposals/`](proposals/) | ranked research directions, actionable conjectures, five adjudicated research campaigns |
| [`graphs/`](graphs/) | theorem-level knowledge graph (JSONL) and schema |
| [`quality/`](quality/) | coverage report, evidence audit, limitations |
| [`final_synthesis/`](final_synthesis/) | comprehensive report (answers the ten synthesis questions), top-100 insights, top-25 opportunities, open problems for future agents |
| [`tools/`](tools/) | harvesters, pool/candidate builders, seed verification, selection, record and graph generators |

## Headline facts (details and evidence in the linked files)

* **2026 changed the frontier.** Unrefereed claims of a zero-free half-plane for ζ and all Dirichlet L-functions (OpenAI: Re s > 11/12, human-edited; Re s > 7/8, Lean claimed), of ≥ 2/3 of zeta zeros simple and on the critical line (Alpöge–Furman; independent proof by Lamzouri), and of the non-existence of Landau–Siegel zeros (OpenAI; human re-proofs by Banks, Kerr, Guo). See [`history/recent_developments_2024_2026.md`](history/recent_developments_2024_2026.md).
* **Our audits found no error invalidating any of these main theorems** in the inspected portions: the 11/12 manuscript passed a section-by-section Level-2 audit; one proof step in Alpöge–Furman needed (and received) a short repair. These are AI-agent audits, not referee reports. See [`audits/verified_findings.md`](audits/verified_findings.md).
* **Verified findings elsewhere** include scoped errors in a 2024 Hilbert–Pólya Hamiltonian construction, in Farmer's 2022 Table 4.1, and in one table entry of the 2026 record zero-free-region preprint (whose main constant 4.896 we independently reproduced).
* **RH itself is untouched** by all of the above; see the method-limit analyses in [`audits/quasi_rh/DOSSIER.md`](audits/quasi_rh/DOSSIER.md) §4 and [`frontiers/known_obstructions.md`](frontiers/known_obstructions.md).

## Relation to the host repository

This archive lives in `research/exploratory/` and follows [`AGENTS.md`](../../../AGENTS.md): it proposes no change to integrated results. The bridge [`connections/repository_bridge.md`](connections/repository_bridge.md) records prior art and obstructions for each repository programme as literature pointers for the repository's own review.

## Licensing and sources

Original analysis: MIT (repository license). zbMATH Open data: CC BY-SA 4.0 (short attributed excerpts only). arXiv metadata: CC0. No copyrighted full texts are redistributed; records give links, identifiers and, for read works, SHA-256 hashes of the texts read where recorded.
