# Evidence audit

```text
Status: QUALITY RECORD (what was verified, how, and by whom)
Scope: every evidence-bearing component of the Observatory archive as of 2026-11-17
Exact sources or dependencies: workflow journals (agent returns), archive files listed below
What was actually run: see the table; all agent work was performed by AI agents (Claude models); no human expert has reviewed this archive
Smallest remaining gap: human expert review of the verified findings and of the 2026 audits; Lean replays
```

## 1. Who checked what

All verification in this archive was done by **AI agents**. Independence means a *different agent instance with a different prompt and no access to the first agent's reasoning beyond its written output*; it is not independence in the human sense, and correlated model errors remain possible (methodology §6).

| Component | Producer | Independent check | Outcome | Where |
|---|---|---|---|---|
| Candidate bibliography (3,373 triaged works) | 33 triage agents (Sonnet) on index content | Level-0 identifier verification by script (zbMATH/Crossref/arXiv); seed verification by script | 1,356/1,422 expert-seed works verified automatically; 36 classics verified manually via authoritative digitizations (two only via Wikipedia, marked) | `corpus/`, `quality/coverage_report.md` |
| Level-1 records (232 attempted; 108 full, 46 partial, 78 no access) | 58 reader agents (Sonnet) | Spot checks by the orchestrator; Level-2 audits of every substantive reader flag | 2 Observatory triage metadata errors caught and corrected by readers (see §3); 1 reader misreading caught at Level 2 (FND-0008) | `papers/`, `theorems/` |
| Frontier ledger (232 records, 12 areas) | 12 analyst agents (Opus) reading primary sources | 12 skeptic agents (Opus) re-checking each record | 140 confirmed against full text; 36 confirmed from abstract/secondary; 52 corrected (correction printed beside the record); 4 superseded; 0 rejected | `frontiers/records_ledger.md`, `frontiers/ledger.jsonl` |
| Repository bridge (215 items, 7 programmes) | 7 analyst agents (Opus) | 7 verifier agents (Opus) | Of 166 prior-art/obstruction items: 79 confirmed, 74 confirmed with correction, 12 relation overstated | `connections/repository_bridge.md` |
| Quasi-RH 11/12 audit | 1 mapper + 7 section auditors (Opus) | Adversarial stage only for non-cosmetic flags (none arose) | No mathematical error found; ~100 numerical identity checks confirmed | `audits/quasi_rh/` |
| 2026 claims (≥2/3 critical line; Landau–Siegel) | 2 mappers + 4 auditors (Opus) | 5 two-sided adjudicators | One proof-step error in Alpöge–Furman Prop. 4.2, repaired (FND-0004); Siegel flags not issues (FND-0010) | `audits/claims_2026/` |
| Level-2 flag audits (8 targets) | 8 auditors (Opus) | 4 two-sided adjudicators | FND-0001, -0002, -0003 verified (scoped); FND-0005 unresolved; three "correct but misinterpreted" | `audits/L2_flag_audits/` |
| Campaigns C1–C5 | 5 investigators (Opus) with computation | 5 skeptics + 5 adjudicators | See each `FINAL.md` (adjudicated statuses) | `proposals/independent_campaigns/` |
| Discovery (39 proposals) | 8 discovery agents (Opus) | 8 verifier agents (Opus) | 9 sound and useful; 10 sound but known; 19 need correction; 1 vocabulary-only | `connections/connections_register.md` |
| Rigorous zero data (EXP-0001) | Arb via python-flint | Arb's internal Turing-method certification | 100,000 zeros, max radius 1.7·10⁻²⁴ | `experiments/reproducibility.md` |

## 2. Evidence levels actually achieved

* **Level 0**: all 1,000 selected works (identifier resolved in zbMATH, Crossref or arXiv, or an authoritative digitization).
* **Level 0+**: 373 works have content summaries from index content only (arXiv abstract / zbMATH review). These are not readings.
* **Level 1**: 108 full-text and 46 partial-text readings. Partial means OCR-limited scans, long monographs read in part, or extraction losses (see §4).
* **Level 2**: targeted audits of specific claims in 15 works (8 flag targets, the OpenAI 11/12 manuscript, Alpöge–Furman, Lamzouri (comparison), and the Landau–Siegel papers of OpenAI, Banks, Kerr and Guo), plus campaign-level checks.
* **Level 3** (advocate/skeptic/adjudicator): 5 adjudications in the 2026-claims audit, 4 in the flag audits, and campaign adjudications.

No work in the corpus was audited completely at Level 2 except the OpenAI 11/12 manuscript (section by section, with imported results checked against statements but not re-proved).

## 3. Observatory self-corrections

| Item | Error | How caught | Correction |
|---|---|---|---|
| Triage summary of Brent 1979 (Math. Comp.) | claimed 81,000,001 zeros verified | Level-1 reader | the paper proves 75,000,001 (75,000,000 zeros with t < 32,585,736.4); 81,000,000 appears only in later papers |
| Triage summary of Odlyzko 1987 | claimed zeros near height 10²⁰ | Level-1 reader | the paper uses zeros 10¹²+1 … 10¹²+10⁵ (height ≈ 2.7·10¹¹) |
| Level-1 record of Ng–Shen–Wong | "k ≥ 12" hypothesis | Level-2 audit F2 | pdftotext artifact; the source has k ≥ 1/2 (FND-0008) |
| Triage of 2026 quasi-RH follow-ups | rejected as "duplicates" | orchestrator review | curator overrides (methodology Addendum A.2) |
| Corpus selection | 68 cross-index duplicates initially selected | orchestrator review | title-normalized deduplication |
| Theorem database | statements from no-access records labelled as partial evidence | orchestrator review | restricted to read works (Addendum A.7) |

## 4. Known systematic risks

* **Text extraction.** `pdftotext` drops overlines, fractions and display structure (e.g. `\frac{1}{2}` → "12", conjugation bars lost). Level-1 statements are recorded in LaTeX reconstructed from extracted text; readers flagged uncertain formulas, but unflagged extraction errors may remain. Prefer LaTeX sources (arXiv e-prints) for any statement you rely on.
* **OCR of historical scans** (GDZ, Numdam, Internet Archive) is heavily garbled for formulas; pre-1950 Level-1 records are mostly "partial".
* **Model recollection.** 260 triage records used `model_knowledge_unverified`; these are labelled in each record and must not be cited as readings.
* **Correlated verification.** Producer and verifier agents are instances of related models; a shared misconception can survive verification.
* **Recency.** The 2024–2026 stratum contains many unrefereed and AI-generated manuscripts; statuses may change quickly after the cutoff.
