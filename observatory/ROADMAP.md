# Riemann Observatory roadmap

Programme: #897. v0.1 is a concrete instrument, not completion of the original programme. Milestones below are proposed deliverables and acceptance gates, not implemented functionality or time estimates.

## v0.1 — runnable local research desk (this contribution)

Six bounded workspaces; five analytic objects; exact-coordinate imported interval demo; honest sampled-data reduction; linked inspection and transient baseline overlay; portable requests/results and replay; agent-readable scene; killable processes; local API/CLI and setup. Read VALIDATION before interpreting “tested.” No public hosting is part of this release.

## v0.2 — connected experiments and trustworthy refinement

**Product outcome:** move from independent experiments to a small number of mathematically specified connected investigations, with real artifact persistence and better local navigation.

### 0.2-A: one genuine prime–zero desk

Choose ONE explicitly stated smoothed explicit formula and a declared test-function basis. Put Fourier/Mellin conventions, measures, endpoint conventions, main/pole/archimedean/trivial-zero terms, finite zero selection and tail status in its schema. Implement both sides independently where feasible. Selecting a spectral band shows its contribution under that exact kernel, not a mythical one-zero/one-prime correspondence.

Acceptance: reproduce a small checked reference experiment; visibly distinguish identity terms from numerical truncation; changing cutoff/precision/smoothing changes the actual producer; a missing tail remains explicitly missing. No RH-dependent estimate can silently be used to certify the RH route under examination.

### 0.2-B: precision/refinement and comparison

Add optional python-flint/Arb providers for a bounded set of point evaluations with genuine ball serialization. Separate arithmetic enclosure, function-domain assumptions and coverage. Re-evaluate selected grid cells/points rather than increasing the entire grid. Add logarithmic magnitude and phase contour modes with fixed legends and masks. Improve linked coordinate navigation and retain cross-panel viewport state. Add two-result comparison for explicitly compatible observables, with both source requests visible.

Acceptance: independent known-value and pole/underflow tests; scout vs ball labels cannot be confused; a sampled image is never labeled a certified whole-cell field; replay preserves comparisons and selected refinements.

### 0.2-C: durable experiments and provider contracts

Split Spec into discriminated per-provider schemas, with generated/validated client controls. Introduce immutable local content-addressed artifacts and a lightweight experiment index (SQLite is sufficient). Support offline inspection of validated saved artifacts without promoting their scientific status. Persist provider versions, code hashes, observations, event selections, comparisons and checks.

Acceptance: process restart does not lose saved investigations; corrupt hashes and schema mismatches are refused or visibly quarantined; prior experiments remain reproducible/migratable; a CLI/browser agent can reproduce the same experiment identity.

### 0.2-D: finish platform acceptance

Native-origin Playwright coverage in CI; Windows/macOS startup; network-clean install; PNG/JSON downloads and native localStorage; stale/cancel races; keyboard and screen-reader audit; no outside requests. Add a screenshot+scene pair export. Improve maintainability of app.js through components only where it advances these workflows.

**Do not put in 0.2:** public arbitrary compute, an unbounded expression language, all L-function families, or a costly frontend rewrite with no mathematical/interaction payoff.

## v0.3 — scalable stored data and family exploration

**Product outcome:** inspect large existing datasets smoothly and explore families without confusing data navigation with expensive fresh evaluation.

Build an event-table adapter with exact heights, source/version/coverage/licence metadata and import validation. Start with a small curated dataset and a complete importer test, not a screenshot of advertised global coverage. Expand Dirichlet characters to a bounded primitive/imprimitive family explorer with explicit conductor, parity, local-factor and normalization metadata.

Introduce multiresolution stored summaries, independent indexed events, viewport range queries, immutable chunk manifests and missing-data masks. Use columnar event tables; use chunked arrays for actual grid workloads. Choose Parquet/Arrow and Zarr only where measurements justify them; do not force both into every representation. The raw data and definition, not display vertices, determine statistics. Preserve irregular spacing and local anchors.

Acceptance: adversarial spikes, alternating signs, gaps at chunk boundaries, duplicate/uncertain events, extreme anchors and missing tiles survive navigation. Publish hardware/workload/latency/memory measurements for a declared dataset, with source I/O separated from rendering and fresh evaluation. Provide a useful normalized zero-statistics panel with window/census restrictions exposed. Larger-height evaluators remain distinct capability providers.

## v0.4 — operators, counterfactual worlds and discovery experiments

**Product outcome:** generate reproducible questions about mechanisms, rather than only draw more quantities.

Add one reviewed finite kernel/witness workflow from the repository with exact source SHA, primitive input status, conditioning, all finite blocks/couplings and omitted-sector status. A selected eigenvector opens the corresponding test function and its arithmetic decomposition. Add a small synthetic-control library: specified symmetric zero sets, exact polynomial/graph models, finite local-factor perturbations and clearly marked phase-randomized arithmetic.

Build a bounded disagreement search between independently specified constructions. Search on training windows; freeze a detector; test on withheld windows; record parameter choices and failures. Add the reciprocal/logarithmic hierarchy workspace from the #892 programme as a separate provider family, with source and analytic-domain distinctions retained.

Acceptance: a concrete investigation exports an observation, data, detector definition, controls, held-out results, uncertainty and one useful next experiment. A fitted model or finite PSD matrix is not elevated to a theorem. A deformation that is a nonvanishing analytic factor does not falsely animate existing zeros.

## v0.5 — public exhibits and private collaboration

**Product outcome:** share compelling reproducible investigations safely.

First deploy precomputed, read-only exhibits with all definitions, source status and manifests. Public visitors should not be able to submit unrestricted calculations. Add an authenticated private workbench separately: bounded job queues, permissions, quotas, cancellation, resource accounting, backups, observability, cost limits and environment isolation. Reuse experiment formats between local/private/public modes.

Acceptance: threat model, tenancy and access tests, restore drills, resource limits, crash/restart behavior, licensed data distribution and reproducible deploy/rollback. No public deployment until these exist. Specialized remote CPU/GPU workers are optional providers with benchmarks, not an automatic requirement to use the instrument.

## Coordination strategy

Keep the numerical contracts and mathematical formula review independent of UI implementation. A practical first split is: (A) formula/provider accuracy, (B) views/state/refinement, (C) artifacts/scaling, (D) native browser/platform tests. Each contribution carries executable examples and explicit numerical scope. Small vertically complete experiments are better acceptance units than a large inventory of disconnected controls.
