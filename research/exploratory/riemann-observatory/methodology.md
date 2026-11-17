# Methodology

```text
Status: EXPLORATORY / IMPORTED (literature archive; no new RH claim)
Scope: literature corpus 1859 – 2026-11-17; theorem statements are IMPORTED from cited sources
Exact sources or dependencies: zbMATH Open API, arXiv API, Crossref API, primary full texts (listed per record)
What was actually run: see logs/RUN_LOG.md and quality/coverage_report.md
Smallest remaining gap: see quality/limitations.md
```

This document fixes how the Riemann Observatory corpus was built, how evidence is graded, and what each label means. It was written **before** the corpus was selected and is amended only by dated addenda at the end.

## 1. Literature search cutoff and sources

* Search cutoff: **2026-11-17** (UTC). Anything later is out of scope.
* Programmatic sources (all public, no credentials):
  * **zbMATH Open** REST API (`api.zbmath.org/v1`), including JFM records (1868–1942), MSC codes, reviewer texts and resolved reference lists. zbMATH data are CC BY-SA 4.0; reviews are quoted only briefly and attributed.
  * **arXiv** Atom API (`export.arxiv.org/api/query`); arXiv metadata are CC0. Full texts are fetched only to read them; PDFs are **not** redistributed in the archive (cache paths and SHA-256 hashes are recorded instead).
  * **Crossref** REST API for DOI resolution, venue metadata and update/correction relations.
  * Open digitisation portals when a classical work is freely available (e.g. GDZ Göttingen, Numdam, EuDML, the Wilkins transcription of Riemann 1859, Clay Mathematics Institute scans).
* OpenAlex and Semantic Scholar were rate-limited (HTTP 429, shared IP budget) at execution time and were **not** used.
* MathSciNet is not accessible from this environment and was not used.

## 2. Coverage taxonomy

Every work receives one or more **family tags** and exactly one **historical stratum**.

| Tag | Family | Typical content |
|---|---|---|
| A | Classical analytic number theory | memoir, continuation, functional equation, explicit formulas, PNT, zero-free regions, zero density, exponential sums, Dirichlet polynomials, mollifiers, moments, subconvexity, resonance, approximate functional equations |
| B | Zeros and their statistics | critical-line proportions, simplicity, pair/n-level correlation, spacing, universality, extreme values, RMT models, de Bruijn–Newman, numerical verification |
| C | Equivalent formulations | Weil positivity, Li, Nyman–Beurling/Báez-Duarte, Robin/Lagarias/Nicolas, Mertens/Riesz/Hardy–Littlewood, Hilbert-space and Mellin criteria |
| D | Spectral / operator | Hilbert–Pólya, trace formulas, scattering, de Branges spaces, canonical systems, spectral determinants, transfer operators, quantum chaos |
| E | Geometry, arithmetic, broader L-functions | function fields (Weil, Deligne), automorphic/Langlands, Selberg class, Dedekind/Hecke, Selberg zeta, Ihara, GRH, Siegel zeros, counterexample zetas |
| F | Dynamical and alternative | ergodic/horocycle, Laguerre–Pólya and Jensen polynomials, probability, Beurling primes, Fourier quasicrystals, Euler-product truncations, computation-led ideas, physical analogies with rigorous content |
| G | Failed and controversial | claimed proofs/disproofs, retractions, corrections, disproved conjectures, documented failure modes |
| H | Adjacent mathematics | decoupling, polynomial method, real-stable polynomials, total positivity, Pick/Loewner, prolate functions, GMC/log-correlated fields, SOS/SDP, Fourier extremal problems, logic/formalization |

Historical strata: `S1 1859–1900`, `S2 1901–1950`, `S3 1951–1980`, `S4 1981–2000`, `S5 2001–2015`, `S6 2016–2023`, `S7 2024–2026-11-17`.

## 3. Corpus construction (overlapping methods)

1. **MSC/keyword harvest (zbMATH)**: 27 queries (see `tools/harvest_zbmath.py`), e.g. `cc:11M26`, `cc:11M06`, `cc:11M50`, `cc:11N05`, `cc:11Y35`, `any:"Riemann hypothesis"`, and criterion/technique keywords (Li coefficients, Nyman, Robin, de Bruijn–Newman, Weil positivity, Hilbert–Pólya, Selberg class …).
2. **arXiv harvest**: 30 phrase queries (see `tools/harvest_arxiv.py`).
3. **Backward citation expansion**: zbMATH resolves references of harvested documents to zbMATH document ids. We count, for every referenced document, how many harvested documents cite it (*in-pool citation count*). Highly cited references are pulled into the candidate pool even if their MSC codes are outside the harvest (this is how adjacent-field works enter).
4. **Expert seed lists**: nine independent specialist agents (families A1, A2, B–H) list landmark works from expertise. Seeds are **not trusted**: each is matched programmatically against zbMATH/Crossref/arXiv (Level 0); unmatched seeds are kept only if a human-checkable source is found, otherwise rejected with reason `unverified_seed`.
5. **Forward/currency checks**: frontier analysts (see `frontiers/`) independently locate current records up to the cutoff, which adds recent works missing from the harvest.

## 4. Selection criteria (scored, then curated)

For each candidate a transparent score is computed (`tools/build_corpus.py`):

* `rel` — topical relevance (query membership weight: core RH MSC/keywords > zeta-general > adjacent).
* `cent` — dependency centrality: log(1 + in-pool citations), normalized **within stratum** (older works accumulate citations; recent works would otherwise be excluded).
* `seed` — named by at least one expert seed list (and verified).
* `type` — monograph/survey bonus for reference value; crank/withdrawn items are capped (family G gets ≤ ~5% of the corpus and must be instructive).
* `frontier` — cited as a current record by the frontier ledger.

Selection then applies **coverage floors** per family and per stratum so that the ~1,000 selected works span all eight families and seven strata. Every candidate that was considered and not selected receives a machine-readable exclusion reason in `corpus/selection_decisions.csv` (e.g. `low_relevance`, `duplicate_version`, `superseded_survey`, `peripheral_application`, `unverified_seed`, `crank_cap`, `out_of_scope_language_unavailable`).

The 1,000 target is a planning scale, not a quota: no entry is padded or invented.

## 5. Evidence levels (per record)

| Level | Name | Meaning (what was actually done) |
|---|---|---|
| L0 | Bibliographic verification | identity confirmed in at least one authoritative index (zbMATH id, DOI via Crossref, or arXiv id); versions/dates recorded |
| L0+ | Index-content record | content fields derived **only** from index content (arXiv abstract, zbMATH review); marked `basis: abstract/review`. This is **not** a reading of the paper |
| L1 | Substantive reading | full text opened; main results, hypotheses and proof architecture extracted with theorem/page locations |
| L2 | Detailed technical audit | central lemmas re-derived or checked; boundary cases, interchanges of limits, constants, uniformity checked; later corrections searched |
| L3 | Adversarial reconstruction | independent advocate and skeptic agents plus an adjudicator; computations or formal checks where feasible |

A record never claims a higher level than the work actually performed. `access_and_audit_manifest.csv` lists the level per work.

## 6. Finding classification (audits)

`verified_error` · `suspected_gap` · `unresolved_ambiguity` · `missing_hypothesis` · `correct_but_misinterpreted` · `valid_with_stronger_consequences` · `no_issue_found_in_inspected_portion`.

Rules: (i) an alleged error must have an explicit witness (counterexample, failing computation, or a precise invalid step with a corrected computation) produced independently of the agent that first raised it; (ii) agreement among agents that share a prompt is not independent evidence; (iii) published errata/corrections by the authors themselves are reported as such, distinct from Observatory findings; (iv) no author's result is publicly called erroneous on the basis of an unverified finding — such items stay in `audits/unresolved_findings.md`.

## 7. Connection and conjecture discipline

Each proposed connection records: exact source theorems; the explicit mathematical link; checked compatibility of domains/quantifiers/constants; what is proved; what is conjectural; next step; potential counterexamples; proposed tests; significance and difficulty. Shared vocabulary or analogous formulas do not count as a connection. Speculative edges in the knowledge graph carry `status: speculative`.

## 8. Computation discipline

Computations use `python-flint` (Arb ball arithmetic) when a claim is described as rigorous or certified; `mpmath` high precision is labelled **non-rigorous high precision**. Every experiment records code path, parameters, versions, runtime and output hashes (`experiments/reproducibility.md`). A finite computation is never presented as a proof of an infinite statement.

## 9. Relation to the host repository

The Observatory lives in `research/exploratory/` of the GettysburgResearch RH project and follows its exploration rules (AGENTS.md): it proposes no change to integrated results and does not recycle claim IDs. Where literature bears on a repository programme (`PROGRAMMES.md`), the link is recorded in `connections/repository_bridge.md` as an **IMPORTED** literature pointer; any resulting statement about repository results is a proposal requiring the repository's own review.

## 10. Incremental updates

All identifiers are stable (`PAPER-####`, `THM-PAPER-####-k`, `FND-####`, `CON-####`, `LED-<AREA>-k`). New works append new ids; removed works keep their ids with `status: withdrawn_from_corpus`. Harvest scripts are idempotent (`.done` markers); rerunning `tools/build_corpus.py` with a later cutoff produces a diff rather than a rebuild.

## Addendum A (2026-11-17, during execution)

1. **Stratum S0.** Four selected works predate Riemann's memoir (Euler 1737, Dirichlet 1837, Chebyshev 1852 ×2). They are labelled `S0 pre-1859 antecedents` rather than forced into S1.
2. **Curator overrides.** Twelve 2026 works were force-included with the documented reason "curator override: 2026 frontier claim/follow-up audited or tracked by the Observatory" (the OpenAI 11/12 quasi-RH manuscript, human follow-ups to the 7/8 claim, human re-proofs of Landau–Siegel exclusion, Knausgård's critical-line refinement, Bellotti–Trudgian–Yang 2026). The triage agent had wrongly rejected several as "duplicates". Overrides are listed in `corpus/selection_decisions.csv`.
3. **Deduplication.** Cross-index duplicates (zbMATH vs arXiv vs scan records of the same work) are removed by normalized title within a ±3-year window; 68 duplicates were removed and recorded as "duplicate of CAND-…".
4. **Model tiering.** Index-content triage and Level-1 reading used a lighter model (Sonnet); frontier analysis, verification, audits, campaigns and discovery used Opus. Level-1 records are extraction-level evidence; any finding that matters is re-checked at Level 2 by a different agent.
5. **Sub-agent outputs.** The execution harness sometimes refused sub-agents' writes of report files. Those agents' structured returns were rendered to the expected paths by `tools/materialize_results.py`; such files begin with a `materialized from workflow result` comment.
6. **Lean replay.** Building third-party Lean code (the OpenAI quasi-RH formalization) was blocked by the session's safety policy; see `audits/lean_replay/README.md`.
7. **Theorem database scope.** `theorems/theorems.jsonl` contains statements only from works whose text was actually read (full or partial). Records with no legitimate full-text access contribute no theorem nodes.
