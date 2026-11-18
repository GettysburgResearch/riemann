# PAPER-D201: The Duistermaat index and eigenvalue interlacing for self-adjoint extensions of a symmetric operator

Gregory Berkolaiko, Graham Cox, Yuri Latushkin, Selim Sukhtaiev. Journal of Spectral Theory 16 (2026), 1–49; inspected arXiv preprint v4. DOI10.4171/jst/590. [Source](https://arxiv.org/pdf/2311.06701v4).

**Audit level:** 0. Full text accessed: True. Completed substantive reading: False. Targeted primary-text reading: §1 main hypotheses/Theorems1.1–1.3 and discussion; §5 Proposition5.3 and proofs of1.1–1.2; §6 Theorem6.2, Lemma6.3 and resolvent proof; selected §7 examples. Whole35-page paper and every Duistermaat-index argument were not read/audited completely. The unbounded-both-directions auxiliary theorem is independently reconstructed separately, not attributed to sourceTheorem1.1.

**Access/version:** 35-page v4 PDF downloaded and text extracted; private research copy. Primary arXiv version history inspected: v1 2023-11-12, v2 2024-01-09, v3 2025-08-25, v4 2025-09-11; abstract comments report fixes/streamlining. No exhaustive later correction search.

## Source results

- Theorem1.1,pp2–3; equations1.11–1.14: S closed densely defined bounded below symmetric, finite equal deficiency(n,n), boundary triplet. For two selfadjoint extensions H1,H2, the global spectral shift below essential spectrum lies in a fixed interval[−σ−,σ+], with σ−+σ+=n−dim(L1∩L2)≤n; endpoints are Duistermaat indices relative to the Friedrichs extension.
- Theorem1.2,p4; proof§5,p19: Under the same hypotheses, for[a,b] disjoint from essential spectrum, N_H1((a,b])−N_H2((a,b]) equals the difference of endpoint Duistermaat indices. Unique continuation is not required for this relative count.
- Theorem6.2,pp22–24; equations6.21–6.31: At common real resolvent λ, the resolvent difference reduces to ker(S*−λ), has constant rank n−dim(L1∩L2), and its positive/negative inertia is expressed by Duistermaat indices. The source retains the setting of Theorem1.1.

## Proof architecture

- Boundary triplets identify selfadjoint domains with Lagrangian planes.
- Cauchy data spaces, Maslov-index monotonicity and the triple-index identity give relative interval counts.
- Common real eigenvalues missed without UCP cancel between the two extensions.
- An alternative proof places resolvent differences in finite-dimensional defect spaces, computes inertia, then anchors below both spectra and applies finite-rank Weyl interlacing.

## Limitations

- Semiboundedness is an explicit hypothesis; the main theorem cannot be directly cited for arbitrary two-sided spectra.
- Friedrichs anchoring and counts from−∞ are unavailable for an arbitrary unbounded-both-directions operator.
- No full-paper L1 audit; published typeset version not compared.
- No result about Riemann zeros or arbitrary energy-dependent unitary scattering matrices.

## Concrete next steps

- Independently review the two-sided compact-resolvent relative-count proof in audits/extension_interlacing_round2.md.
- For an actual unbounded boundary coupling identify the common closed symmetric restriction, finite defect, fixed domains and compactness.
- Determine the effective resolvent rank r rather than overcounting all boundary coordinates.

## Reuse and provenance

See `audits/extension_interlacing_round2.md` for the independently reconstructed compact-resolvent, finite-defect3d curvature bound. Its proof is separate from the source theorem and preserves the latter’s semiboundedness hypothesis. Exact examples are reproduced by `experiments/code/extension_interlacing_round2.py`. No literature novelty or classical-RH theorem is asserted.
