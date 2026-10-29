# Exact auxiliary-projector diagonal cancellation

**Status:** Elementary algebraic identity within the [second-Poisson aggregation](2026-10-29-second-poisson-aggregate.md). It explains the leading positive-diagonal cost but does not bound the remaining off-diagonal and does not prove an inverse moment or zero-free region. Source-to-physical phase, sector and profile identifications are those imported in the linked notes.

Let the residual columns r₁,r₂ be good squarefree ideals in an annulus `Nr_i ≍ P/D₀`, and insert the exact auxiliary Möbius projector

    1_((r₁,r₂)=1) = Σ_(g | r₁, g | r₂) μ(g).                  (1)

For each original gcd d and divisor k, every common finite ray sector and every fixed pair of row/column profiles, choose one **g-independent formal extension** A(r₁,r₂;v) of the physical coprime-pair summand to all pairs before expanding (1). The primitive conductor and root formulas that identify the physical summand are justified only when `(r₁,r₂)=1`; no assertion that they continue to represent a primitive character off that support is made. The chosen formal extension may retain the original zero masks and smooth factors, but it must be the same for every divisor g. The diagonal part of this exact projector expansion is

    Σ_r A(r,r;v) Σ_(g|r) μ(g) = A((1),(1);v),                (2)

because the coefficient multiplying the projector is independent of its representation r=gn. In the long residual-column range `D₀≤Y^(7/10)` with `P=Y^(6/5)`, the annulus has `Nr≫Y^(1/2)` up to harmless fixed scales, so the unit column is absent and (2) is exactly zero. In particular this statement does not require the summand to have a sign, a Gauss-moment bound, or a model for the diagonal coefficient.

One may first decompose the g sum into a finite smooth dyadic partition, but cancellation is recovered only after retaining the actual signed weights and recombining all dyads: for each r the partition sum must equal 1 on every divisor g|r. Replacing μ(g) by its absolute value, applying Cauchy separately to each g, dropping masks, or estimating each square positively destroys (2). The `K G H` theta-diagonal majorant in the second-Poisson aggregate is therefore a genuine artifact of that positive estimate, not the original coprime diagonal. Its physical contribution is the leading `Y^(6/5−d)` in the small-d regime.

The identity removes the diagonal *formally*. The signed off-diagonal, the common dual row v and the varying g,k phase still have to be controlled jointly. In particular, it does not follow that the three separate positive terms in the aggregate can simply be subtracted from their upper bound, nor that their cancellation is uniform under independently chosen row-dependent profiles. A new signed estimate preserving (1) and the original common profiles remains necessary.

An independent review checked (2) and the caveat that the off-coprime expression is a single formal extension, not a primitive-conductor identity. Its relation to any transformed estimate still depends on preserving that extension, the sector factors and the profiles exactly.
