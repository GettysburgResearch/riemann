# Formalization Reviewer A report

Base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`  
Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`  
Zeta23: `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e`

## Upstream theorem reused

- Mathlib `RiemannHypothesis`, `riemannZeta`, both completed-zeta normalizations and their functional equations.
- Mathlib `analyticOrderAt`, `meromorphicOrderAt`, reciprocal-order arithmetic, zero discreteness, Mellin convergence/change-of-variables/holomorphy APIs, and analytic arithmetic.
- Zeta23's exact nontrivial-zero convention, multiplicity convention, closed seam, finite zero windows, centered coordinate, reflected-zero and reflected-multiplicity theorems.
- Zeta23's literature-form Weil explicit formula and its Riemann-von Mangoldt package, the latter with an explicit `GammaFacts` argument.

## Theorem proved locally

- Project/Mathlib RH identity and normalization bridges with exceptional points stated.
- Centered-coordinate reconstruction.
- Mellin dilation, scalar multiplication, two-term finite linear combinations, compact power kernels, and power-bound strip analyticity adapters.
- Fixed holomorphic-defect transfer.
- Nonvanishing analytic multiplier preservation.
- Complete abstract fixed Mellin singularity transfer.
- Reciprocal-zeta meromorphic-order API.
- Functional-equation reflection closes RH once full admissible-zero reflection and right-half-plane exclusion are supplied.
- Mathlib-only comparator solution `Comparator.MellinAPI.fixedMellinConsumerSolution`.
- The default `RiemannFormal` target imports `Analysis.ComparatorSmoke`, so an ordinary `lake build` also elaborates the owned `MellinAPI` comparator solution and prints its axioms.

## Theorem proved conditionally

- Nonnegative Mellin boundary singularity, conditional on the exact proposition `MellinLandauBoundarySingularity`.
- Subpower negative-mass holomorphy, conditional on `SubpowerNegativeMassHolomorphy`.
- The resulting negative-mass singularity transfer.

The conditional propositions are definitions of `Prop`, not axioms. Every consumer accepts a proof term explicitly.

## Blocked on library infrastructure

Pinned Mathlib and Zeta23 do not expose the exact nonnegative locally integrable Mellin-density theorem saying that a finite abscissa of convergence is a boundary singularity. Zeta23 files containing `Landau` in their names prove different zero-count or explicit-formula estimates. The project therefore records the precise missing proposition and does not infer reuse by name.

The integration-by-parts theorem taking subpower logarithmic negative mass to a holomorphic negative-part Mellin transform on `re s > 0` is likewise not exposed at the pinned commits.

## Blocked on open mathematics

No arithmetic producer is formalized or assumed true here. In particular, fixed rows 2 and 3, the fixed 5:3 detector, zero-safe logarithmic-box positivity, and subpower negative mass remain conclusion-facing producer hypotheses exactly as in the reviewed registry. RH remains unproved.
