# A θ-strip plus strong density does not close the inverse core

**Status.** This is an exact obstruction to a specified positive-input interpolation, not a lower bound for the physical signed dual sum and not a counterexample using actual Hecke characters. It deliberately grants stronger source inputs than have been established over E=Q(ω).

Let `θ=4369347/5000000`, `P=Y^(6/5)`, and consider the full-row Möbius inverse moment in [the 125/144 target](2026-10-29-target-125-144/README.md). Assume optimistically:

1. Every relevant primitive finite-order E-Hecke character has no zeros in Re s>θ and the standard uniform reciprocal contour bound holds, with all source zero masks and the fixed ray twists. This pointwise implication has its own analytic and candidate-semantic hypotheses.
2. The much stronger Liu sextic density rate, normally sourced only for fields containing μ₁₂ plus a family-identification bridge, also held for these E rows. At θ its exponent is `R=3795224/13141959≈0.28878678`. Assume the corresponding rates for nearby fixed real parts and sufficiently small polynomial height.
3. Liu's unmarked inverse mean `Σ|M_u(P)|²≪Y^(7/6+ε)` and ordinary fourth mean `Σ|S_u|⁴≪Y^(1+ε)` hold with the original source profiles.

The pointwise strip estimate supplies only

    |M_u(P)|² ≪ Y^[5608041/6250000+ε]
                   =Y^(0.89728656+ε).                           (1)

Even a top bin of `Y^(R+ε)` rows with zeros arbitrarily close to θ is allowed by the density input. Bounding that bin by (1) gives exponent

    R+5608041/6250000
       =97420794892319/82137243750000≈1.18607334,              (2)

which exceeds 7/6 by `1594010517319/82137243750000≈0.01940667`, and exceeds the strict-improvement threshold `19949123/18750000≈1.06395323` by `3209795/26283918≈0.12212011`. Thus this zero-location slicing, even with the optimistic transferred density, cannot improve the existing total inverse mean by simply applying the pointwise estimate to each bin.

The limitation is also visible as positive data: take `Y^R` abstract selected rows with

    |M|² = Y^(7/6−R),       |S|=1,

and let other M-values vanish. The inverse energy is Y^(7/6), the ordinary fourth energy is at most Y, and the selected-row cardinality is Y^R. Because `7/6−R < 5608041/6250000`, the pointwise θ cap is satisfied with strict room. Assigning their zero-location parameter just below θ is compatible with the optimistic top-bin density exponent after an arbitrarily small loss. Hence no application of Hölder, Cauchy, threshold slicing or positive sums using only these three asserted numerical inputs can force a power saving over Y^(7/6).

This model does not encode actual Möbius coefficients, Hecke phases, moving zero masks, or the signed g-projector, and it does not imply such rows exist. In particular it does not refute a source-specific mixed correlation estimate or [the localized signed-core target](2026-10-29-target-125-144/README.md). To improve the individual boundary one must use some arithmetic relation absent from these positive bounds—for example the coupled Möbius coefficients and signed masks in the reviewed Poisson expansion. The exact sixth-power sector itself shows why a moment exponent below `19949123/18750000` would imply a new ζ_E strip; the checked θ strip alone supplies no such strict margin.

**Independent review.** High_match verified the pointwise exponent, exact fractions, the optimistic E-family transfer qualification and the abstract model. The same review checked [the genuine principal-sector subrange](2026-10-29-known-strip-self-loop-barrier.md): with the staged ζ_E strip and original masks, sixth-power rows v⁶ with `Nv≤Y^b` contribute `O(Y^(21/20−c))` for every fixed `b<954459/6250000`; that statement does not control a localized signed dual block.
