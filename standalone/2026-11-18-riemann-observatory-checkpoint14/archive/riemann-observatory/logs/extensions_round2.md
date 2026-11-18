# Extension-interlacing research log / checkpoint

Task from director: source-read Dancis–Davis1987 and/or arXiv2311.06701, then determine whether unbounded boundary couplings sharing a finite-defect symmetric restriction obey the same3d three-height model-cost bound without semiboundedness.

Date:2026-11-17. Cutoff:2026-11-17. No literature novelty or classical-RH theorem claimed.

## Primary access and scope

1. Dancis–Davis, *An interlacing theorem for eigenvalues of self-adjoint operators*, LAA88–89(1987),117–122, DOI10.1016/0024-3795(87)90106-6. Publisher/Crossref/author bibliography ground identity. Publisher labels open archive. Publisher PDF returned403; both an Elsevier PDF API route and the exact Crossref-provided text/plain mining route were blocked with403. Metadata and the exact failed text URL are saved under `sources/extensions_round2`. **Full text not accessed; no substantive reading or mathematical audit.** PAPER-D202 is deferred/not selected.
2. Berkolaiko–Cox–Latushkin–Sukhtaiev, arXiv2311.06701v4, revision2025-09-11. Current primary arXiv landing page records JST16(2026),1–49, DOI10.4171/jst/590. The v4 PDF was downloaded; SHA256 `52ef994bb33f9cf7fb22fd1581563d59b059065d515ecb6f9df0b55c6500eca5`,779610bytes. The PDF header/history confirmv4; its internal date15Sep2025 is recorded separately rather than replacing the archive revision date. Publisher DOI was unavailable through the web tool, so no comparison with journal typeset numbering was performed.
3. Actual targeted reading: main setting and Theorems1.1–1.3, pp2–5; §5 Proposition5.3 and proofs1.1–1.2,p19; §6 Theorem6.2, Lemma6.3, resolvent proof,pp22–24; selected §7 examples and boundary table. The entire35-page preprint and all index-theoretic foundations were **not** read/audited; PAPER-D201 stays whole-paperL0 with targeted technical reading.

Private copies and primary metadata are under `sources/extensions_round2`; `source_manifest.jsonl` documents the source/version. Source PDFs and extracted full text are excluded from the distributable archive by default.

## Findings and independent reconstruction

- SourceTheorem1.1 explicitly assumes S bounded below. Its fixed shift range has length n−dim(L1∩L2)≤n. No direct attribution of a two-sided-spectrum theorem to that source is made.
- Independent proposition: compact-resolvent selfadjoint H0,H1 on the same Hilbert space, finite-rank real-anchor resolvent difference of inertia(p,m), have one anchored relative count ξ(x)∈[−m,p] over **both** sides of the anchor. Hence oscillation≤r=p+m, and|Δ1−Δ0|≤3r.
- Common closed densely defined symmetric restriction with deficiency(d,d) gives r≤d. At i, resolvent difference maps into ker(S*−i). The exact resolvent transport identity moves this finite rank to any real common anchor. No semiboundedness or real-defect-space shortcut is needed.
- Endpoint conventions were retained: above anchor use resolvent tail[t,∞), below anchor use(−∞,t) and reverse sign. This is what yields the same range, not two unrelated length-d ranges and a spurious factor2.
- A real differential extension example saturates3d: S=−i d/dx on H0¹(0,2π), phasesθ1=3/20,θ0=2/5,K=3/10. Counts(1,1,2) versus(0,1,1), curvature1 versus−2. Direct sums give every finite d. Both spectra are unbounded in both directions.
- Applicability requires one fixed selfadjoint realization on the full space and a common S. An arbitrary unitary S(k) is not sufficient. If auxiliary states are present they remain in the full-space reference; no automatic identification d=M is asserted.
- Conditional bookkeeping: reference A⊕D with dimD=M gives|Δ_H1−Δ_A|≤3d+2M, because each finite D-level contributes0,−2 or1. This needs the same full-space common-extension hypothesis.

The parent independently checked reciprocal signs, half-open conventions, fixed range length,3r cancellation and the rank≤d strategy through real defect spaces. The alternative transport-identity proof and sharp differential example were then communicated separately. No separate third reconstruction is claimed in this checkpoint.

## Artifacts

- `audits/extension_interlacing_round2.md`: complete self-contained proof, exact source restrictions, sharpness and model consequences.
- `papers/PAPER-D201.md`, `PAPER-D202.md`, `papers/spectral_extension_round2_records.jsonl`: two bibliographic records, one accessed targeted source, zero completed full-paper substantive readings in this task.
- `theorems/spectral_extension_round2.jsonl`: seven nodes, separating source theorems from independently reconstructed propositions and conditional model consequences.
- `connections/spectral_extension_round2.jsonl`: one explicit hypothesis-compatible source-to-model connection.
- `experiments/code/extension_interlacing_round2.py`: standard-library exact Fraction arithmetic, including actual eigenvalue endpoints, both reciprocal branches and finite-window additivity.
- `experiments/results/extension_interlacing_round2.json`: successful reproduction and exact sharpness witness.
- `scripts/spectral_extension_round2_records.py`: record builder; requires the private source for its hash.

All JSONL parses and both Python files pass syntax checks. The exact experiment passes. Finite computations supplement the infinite-dimensional proof, not establish it.

## Continuation tasks

1. Obtain a separate third reconstruction of the abstract theorem, including the resolvent transport factor order and inclusive/strict tail conventions.
2. Obtain Dancis–Davis full text before auditing its precise interval/equality cases or asserting prior-work equivalence.
3. For one actual singular boundary/auxiliary proposal, exhibit the full operator domain and dense common S, calculate deficiency and effective resolvent rank, and prove compactness. Do not infer this from a formula S(k) alone.
4. Check source/journal version differences and any later correction history if relying on Duistermaat-index formulas beyond the small mechanism used here.
5. If relaxing compact resolvent, state which essential-spectrum gap contains all compared endpoints and whether a compatible shift normalization across disconnected gaps exists. No such extension was proved here.
