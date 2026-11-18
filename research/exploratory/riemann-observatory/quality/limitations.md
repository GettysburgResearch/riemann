# Limitations

```text
Status: QUALITY RECORD
Scope: the whole archive as delivered on 2026-11-17
Exact sources or dependencies: quality/coverage_report.md, quality/evidence_audit.md
What was actually run: n/a (self-assessment)
Smallest remaining gap: the items listed below
```

## What this archive is not

* **Not a proof or disproof of RH**, and not evidence for or against RH beyond the cited literature. Finite computations here (zeros to height 74,920, detection-horizon experiments, countermodel computations) carry no global implication.
* **Not a refereeing service.** "No error found" in an audit means no error was found in the inspected portion by AI agents. The OpenAI quasi-RH 11/12 audit, the Alpöge–Furman and Landau–Siegel audits are serious but not equivalent to expert referee reports.
* **Not complete.** The 1,000-work corpus is a curated selection from a 20,166-work pool; important works will be missing (see below).

## Coverage limits

1. **Full-text access.** 78 of 232 Level-1 targets had no legitimate open full text (mostly paywalled journals before ~1995). No paywalls were circumvented. MathSciNet, JSTOR and publisher platforms were not used.
2. **Indexes.** OpenAlex and Semantic Scholar were rate-limited and not used; zbMATH and arXiv dominate the pool, so works indexed only elsewhere (some engineering/physics venues, non-indexed proceedings, theses) are under-represented. Works before 1868 are missing from zbMATH/JFM and enter only via expert seeds.
3. **Languages.** Non-English works were included when indexed (French 52, German 49, Russian 7, Swedish 3 among the selected), but Russian, Japanese and Chinese literature is certainly under-covered.
4. **Depth.** Only 154 works were read (full or partial); 846 selected works have index-level records only. Theorem-level reconstruction exists for those 154; 12 works received targeted Level-2 audits.
5. **Families G and H** are the thinnest (48 and 64 works), by design for G (crank cap) and by harvest bias for H.
6. **Citation centrality** uses zbMATH-resolved references, which are sparse before ~2000; centrality of older works is underestimated relative to newer ones (partly corrected by within-stratum normalization).

## Verification limits

1. **Lean replays not done.** The OpenAI quasi-RH 7/8 and Landau–Siegel formalizations, Alpöge–Furman's and Knausgård's Lean claims were not compiled or replayed (building third-party code was blocked by the session safety policy). Static inspection only.
2. **The OpenAI 7/8 manuscript** (199 pp.) was read for structure, not audited.
3. **Imported deep inputs** of the 2026 manuscripts (Patterson/Kubota metaplectic theory, Dunn–Radziwiłł, large-sieve inputs, Montgomery–Taylor window theory) were checked against their statements, not re-proved.
4. **Correlated agents.** All producers and verifiers are AI agents of related model families.
5. **Text extraction errors** (fractions, bars, OCR) can corrupt Level-1 statements; prefer the original source for anything load-bearing.

## Process limits worth knowing

* Several sub-agent report files were refused by the harness and were rendered from the agents' structured returns (`tools/materialize_results.py`); content is the agents', formatting is scripted.
* Triage used a lighter model than audits; triage decisions on borderline works are the least reliable part of the corpus.
* Curator overrides (12 works) and stratum floors are explicit human-like editorial choices made by the orchestrating agent; they are listed in `corpus/selection_decisions.csv` and `methodology.md` Addendum A.

## How to extend

All harvest, selection and record scripts are idempotent (`tools/`). To update: rerun the harvesters with a new cutoff, rebuild the pool, triage only new candidates, rerun `select_corpus.py` and `make_records.py`; existing PAPER ids are stable if the selection order file is preserved (see `methodology.md` §10).
