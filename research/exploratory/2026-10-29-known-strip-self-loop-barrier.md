# Known strip versus the long inverse self-loop

**Status.** This note gives a quantitative barrier to deriving a better individual boundary from the known strip and the source's positive inverse bound alone. It does not assert that the target fails, or that the model below represents the arithmetic sextic matrix. All recent input claims remain source-qualified.

Put `P=Y^(6/5)` and `θ=4369347/5000000`. The original target is an upper bound `Y^(E+ε)` for the all-element-row Möbius energy with the fixed zero-free Mellin profile, original sectors and moving zero masks. The independently reviewed sixth-power extraction gives the exact limsup contribution

    1/6+(12/5)(Θ_E−1/2)                                    (1)

on the logarithmic Y scale, where Θ_E is the rightmost nontrivial zero of `ζ_E` in the sense of a supremum. If a separately admitted conventional Dirichlet strip only supplies `Θ_E≤θ`, its sector exponent is allowed to reach

    1/6+(12/5)(θ−1/2)
      =19949123/18750000≈1.0639532267.                       (2)

Thus an upper bound with any fixed `E` below (2), applied to that actual sector, would itself imply `Θ_E<θ`; at E=21/20 it gives `Θ_E≤125/144`. The prior θ bound does not by itself rule out a hypothetical zero between the target boundary and θ. This is a conditional logical obstruction, not a claim such a zero exists. It also shows that a fixed analytic margin below (2) cannot be extracted merely by substituting the same boundary θ into a pointwise principal-sector estimate.

For the actual sixth-power row `u=v⁶`, the sextic character is the coprimality mask `1_(n,v)=1`. The known `ζ_E` strip and fixed-margin Mellin inversion give the smoothed unnormalized principal sum `≪P^(θ+η)(Nv)^η`; the variable factors are the reciprocal of the finite Euler factors at primes dividing v. Summing over `Nv≪Y^(1/6)` gives precisely exponent (2), up to a loss depending on η. This controls that sector at the old boundary but gives no strict improvement. The derivation needs no assertion about angular Hecke characters.

This does give a strict **physical-row subrange** at the stronger `E=21/20` target: for any fixed `b<954459/6250000≈0.15271344`, the contribution of sixth-power rows with `Nv≤Y^b` is `O(Y^(21/20−c))` for some c>0, after choosing a sufficiently small fixed Mellin/ε margin. Indeed it is `≪Y^[b+(6/5)(2θ−1)+η]`. This is genuine prime/composite cancellation supplied by the assumed E-zeta strip and the original moving coprimality mask. It covers only a sparse physical subfamily and does **not** bound a separately localized auxiliary-g or dual-frequency block; the signed Poisson decomposition need not preserve positivity under that restriction. Nor does it supply the full-row target.

One tempting extension would use the same pointwise exponent for every row `u=a v⁶`, where a is sixth-free. As a benchmark, **even if** one additionally assumed the uniform masked estimate `P^(θ+η)Y^η` for all associated sixth-order Hecke characters with `Na≤Y^b`, the elementary row count

    Σ_(Na≤Y^b) #{v: Nv≤(Y/Na)^(1/6)} ≪ Y^(1/6+5b/6+η)       (3)

would give at best `(2)+5b/6` by pointwise squaring and summation. On all O(Y) rows this same benchmark is

    1+(6/5)(2θ−1)=11858041/6250000≈1.89728656,              (4)

far weaker than the imported all-row inverse bound `Y^(7/6+ε)`. The hypothetical uniform estimate is **not** implied here by the Dirichlet strip: the nonprincipal characters indexed by a require their own zero-free and conductor-uniform reciprocal bounds. The comparison only demonstrates that pointwise use of such an estimate cannot replace cancellation across the full row family.

## Positive-input countermodel

The following finite matrix shows the logical limitation of combining a sector bound and a global second-moment upper bound. Let N be even, N≈Y^(6/5), and choose a balanced vector `m_j∈{±N^(−1/2)}` with Σ_j m_j=0. On roughly Y^(1/6) designated rows set every matrix entry to 1; their response is zero, matching an idealized strong sixth-power-sector constraint. On each of roughly Y other rows set `T_ij=sign(m_j) ξ_j`, where `ξ_j∈{±1}` is chosen so that `Σ_j ξ_j` is the nearest attainable integer to `Y^(1/12)√N`. This is possible for large Y. All entries have absolute value one, but each nondesignated response is `Y^(1/12)+o(1)`, so their energy is `Y^(7/6)(1+o(1))`.

Hence a sharp positive input at exponent 7/6 and even a vanishing designated sector leave the desired exponent below 1.063954 wholly unforced without a relation between the other rows and the designated sector. The model is deliberately abstract: its balanced signs are not asserted to be actual Möbius coefficients, its matrix does not satisfy sextic reciprocity or the source's ray-class correlations, and it does not localize the energy to the low- or high-frequency part of a Poisson transform. Its purpose is to isolate what must be added to the source inverse bound: a genuine signed or spectral coupling between physical rows, including the complete Möbius coefficient vector, sectors and original masks.

The more arithmetic self-loop calculation, with the source normalization and exact dual scales, is in [the inverse self-loop note](2026-10-29-inverse-self-loop-obstruction.md). The separately controlled high-gcd region and exact cancellation of the auxiliary diagonal do not by themselves supply such a coupling at the unit-gcd long-dual edge.

**Independent review.** Families checked the power-sector exponent, truncated-root threshold, variable Euler deletion and abstract matrix calculation. The review does not infer a bound for the signed auxiliary-g core.
