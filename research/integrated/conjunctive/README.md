# Conjunctive APIs

## Integrated scope

**Strongest reviewed result:** Perron, Schur, matched-transfer, root/excess, staircase identities.

**First open arrow:** Literal native simultaneous premises.

**Relationship to RH:** open nodes: OPEN.ARITH.CFBB, OPEN.ARITH.BPOE, OPEN.CONJ.REGIONAL_ROW, OPEN.CONJ.REGIONAL_COLUMN, OPEN.CONJ.QMT, OPEN.CONJ.AMT, OPEN.CONJ.SORR, OPEN.CONJ.RFCP, OPEN.CONJ.PERRON_CV_ROW, OPEN.CONJ.PERRON_XD_ROW

**Family state:** `live`

This packet contains 18 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `API.PERRON.ABSORPTION` | `VERIFIED` | A fixed nonnegative subcritical matrix absorbs coupled negative masses. | finite fixed channel system | None | PR #697 `e878c3717cd8` `claims/lemmas/L-101100-positive-completion-negative-mass-absorption.md` |
| `API.CONJUNCTIVE.SPARSITY_ENERGY` | `VERIFIED_WITH_FIXES` | Bad-set length and derivative energy jointly bound negative mass by a Poincare inequality. | locally absolutely continuous log-scale scalar | Do not call subpower log-length an independent key; require power-saving or deep-excursion occupancy for genuine leverage. | PR #698 `a10d6a401051` `claims/lemmas/L-101103-bad-set-sparsity-times-derivative-energy.md` |
| `API.CONJUNCTIVE.REGIONAL_SCHUR` | `VERIFIED_WITH_FIXES` | Source-owned regional row and column Schur masses pair losslessly when partitioned before observation. | finite or subpower source-owned partition | Require literal native row/column marginals and a compatible partition. | PR #698 `a10d6a401051` `claims/lemmas/L-101105-regionwise-two-sided-schur-cover.md` |
| `API.CONJUNCTIVE.MATCHED_TRANSFER` | `VERIFIED` | One common transfer gives an exact infimal negative-part decomposition. | pointwise/measurable common transfer | None | PR #704 `66f755df4321` `claims/lemmas/L-101500-matched-transfer-negative-part.md` |
| `API.CONJUNCTIVE.ROOT_EXCESS` | `VERIFIED` | Strict source-owned root return plus root-free packing controls detector negative mass. | dyadic blocks with strict theta<1 | None | PR #706 `44828a27c63b` `claims/lemmas/L-104101-two-key-root-excess-absorption.md` |
| `REFUTATION.ROOT_EXCESS_ONLY` | `REFUTED_MECHANISM` | Positive excess alone does not control the unknown root in Q=\|g\|^2+E. | all Hilbert triples | None | PR #706 `44828a27c63b` `claims/lemmas/L-104100-root-containing-square-firewall.md` |
| `ARITH.STAIRCASE.VECTOR_REDUCTION` | `VERIFIED_WITH_FIXES` | The survival-weighted mixed coboundary, one common carrier-free filter, and vector Vaughan identity reduce two channels to one balanced source packet. | finite monotone staircases and identical cutoffs | Use the identical source, cutoff, and zero-safe compact filter in both coordinates. | PR #703 `0a46dba5c74e` `claims/lemmas/L-102100-survival-weighted-mixed-coboundary-and-staircase-telescope.md\|claims/lemmas/L-102103-carrier-free-filter-for-the-quadratic-wavelet-bridge.md\|claims/lemmas/L-102105-vector-vaughan-reduction.md` |
| `OPEN.ARITH.CFBB` | `OPEN_SUFFICIENT_FOR_RH` | A source-faithful subcritical 2x2 Perron matrix controls the carrier-free balanced vector packet. | global dyadic blocks | None | PR #703 `0a46dba5c74e` `claims/theorems/T-102100-carrier-free-staircase-perron-frontier.md` |
| `ARITH.PHASE.CUBIC_AMPLITUDE` | `VERIFIED` | Carrier-normalized phase homotopy, cubic B-spline autocorrelation, and half-divisor source square root close the source/phase amplitude layer. | finite labelled source and fixed compactifier | None | PR #707 `7bf3308d40ac` `claims/lemmas/L-103300-critical-carrier-normalized-balanced-homotopy.md\|claims/lemmas/L-103303-centered-cubic-bspline-autocorrelation.md\|claims/lemmas/L-103304-half-divisor-field-is-source-square-root.md` |
| `OPEN.ARITH.BPOE` | `OPEN_SUFFICIENT_FOR_RH` | Physical observation embeds the source/phase energy into one multiplicative shell at subpower cost. | dyadic shell operators on one occurrence | None | PR #707 `7bf3308d40ac` `claims/theorems/T-103300-balanced-phase-amplitude-and-physical-occupancy-frontier.md` |
| `OPEN.CONJ.REGIONAL_ROW` | `OPEN_SUFFICIENT_FOR_RH` | Literal native regional row marginals satisfy the subpower Schur bound. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.REGIONAL_COLUMN` | `OPEN_SUFFICIENT_FOR_RH` | Compatible literal native regional column marginals satisfy the subpower Schur bound. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.QMT` | `OPEN_SUFFICIENT_FOR_RH` | The first matched-transfer arithmetic estimate holds on the common transfer. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.AMT` | `OPEN_SUFFICIENT_FOR_RH` | The second matched-transfer arithmetic estimate holds on the common transfer. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.SORR` | `OPEN_SUFFICIENT_FOR_RH` | Strict source-owned root return holds with contraction theta<1. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.RFCP` | `OPEN_SUFFICIENT_FOR_RH` | Root-free excess packing is subpower on the same source ledger. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.PERRON_CV_ROW` | `OPEN_SUFFICIENT_FOR_RH` | The source-faithful critical-variation row of the joint Perron matrix is subcritical. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.CONJ.PERRON_XD_ROW` | `OPEN_SUFFICIENT_FOR_RH` | The source-faithful cross-dispersion row of the joint Perron matrix is subcritical. | global literal source | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
