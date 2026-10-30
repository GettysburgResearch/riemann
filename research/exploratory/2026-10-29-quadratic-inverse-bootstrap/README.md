# A density-assisted quadratic inverse bootstrap and its fixed point

**Status:** A source-qualified conditional reduction, not an independent zero-free region. It assumes a uniform zero-free half-plane for *all Dirichlet L-functions*, the cited quadratic zero-density theorem, the quadratic large sieve, and the local reciprocal-L estimate stated below. Source-to-detector implications are not asserted. The numerical candidate `θ₀=4369351/5000000` can be used only if the tracker's theorem and its semantics are independently established.

Let W be a fixed smooth compact-annular function, and define

    M_u(D)=D^(−1/2) Σ_(a odd) μ(a) (u/a) W(a/D),
    A(Y,D)=Σ_(1≤u≤Y) |M_u(D)|²,

with the zero-extended quadratic symbol. Assume all primitive Dirichlet L-functions are zero-free in `Re s>θ₀`, with `1/2<θ₀<1`. Use the following standard local analytic input: for any fixed η>0, after excluding the zeros of `L(s,χ)` with `|Im s|≤2T` to the left of a chosen line `Re s=σ≥1/2`, Mellin inversion and reciprocal-L control give the corresponding smoothed inverse bound `≪(qT)^η D^(σ−1/2+η)`, with a margin η; the contribution from `|Im s|>T` is negligible after taking a sufficiently high fixed seminorm of W. The reciprocal of the principal L-function is holomorphic at its pole. Fixed and variable zero masks contribute at most `(Y D)^η`. These uniform local strip, height and mask estimates must be supplied, not inferred from the scalar calculation.

For a fixed margin, the `q^η` reciprocal control is stronger than the elementary `q^C` estimate and needs justification. On zero-free discs centered at `2+it`, Borel–Carathéodory bounds `|log L|` by O(log(q(|t|+3))) on an outer disc; on a fixed inner disc the absolutely convergent Euler series bounds `|log L|` by O(1). Hadamard three-circles, with positive separation from the zeros, bounds `|log L|` by a fixed power `<1` of `log(q(|t|+3))`; exponentiating yields `(q(|t|+3))^η`. A zero-free box of height 2T suffices for the discs needed below height T, for large T. This is the standard local logarithmic-control input; the contour boundaries, source masks and fixed loss order still require the stated uniformity.

As a zero-count input, [Corrigan–Zhao, Theorem 1.4](https://arxiv.org/abs/2211.00260), gives for primitive quadratic characters of conductor at most Q and height at most T a first-branch bound of shape

    (QT)^ε Q^H(σ) T^[4(1−σ)/(2−σ)],
    H(σ)=3(1−σ)/(2−σ).                                       (1)

Take `D=Y^r` with fixed `1/2<r≤4/5`. Choose the allowed loss first, then the strip margins, bin widths and their fixed polynomial-height growth orders. Next choose `T=Y^τ` with τ sufficiently small relative to those orders, and only then the external Mellin-tail differentiation order. Under the analytic inputs above,

    A(Y,D) ≪_ε (Y + sqrt(Y) D^(2θ₀−1))(YD)^ε.               (2)

In particular this has size `Y^(1+ε)` for

    r ≤ 1/[2(2θ₀−1)]                                         (3)

when that range lies in `(1/2,4/5]`. For `θ₀=4369351/5000000≈0.8738702`, the endpoint is exactly `1250000/1869351≈0.6686812696`.

## Derivation

Write `u=d k²` with d squarefree, and set `K=Y/D`. For `k≤K`, apply the quadratic large sieve to the d-family, preserving the coprimality mask from k as a bounded source coefficient. Summing gives

    Σ_(k≤K) Σ_(d≤Y/k²)|M_(dk²)(D)|²
       ≪_ε (Y+DK)(YD)^ε ≪ Y^(1+ε).                         (4)

For k>K, split into dyadic k ranges and the squarefree d rows into finitely many zero-location bins. For a bin with effective rightmost zero real part ≤σ, the local inverse bound is `D^(2σ−1+ε)` after squaring. The number of relevant d with a zero at least the lower endpoint of the bin is at most `(Y/k²)^{H(σ)+ε}` times the harmless height factor in (1). A baseline bin at σ=1/2 is bounded by the trivial row count and the same local inverse estimate. Split d by parity and residues modulo 4; the even case is a fixed χ₂ twist of the odd squarefree family. The primitive discriminant has size ≤4d, and these finitely many classes change only constants. If (1) omits the principal character d=1, add its one row separately to each k-block; since Q=Y/k²≥1, this additive 1 is dominated by Q^H. Summing k for a fixed bin gives, up to logarithms and small power losses,

    D^(2σ−1) Y^H Σ_(K<k≤sqrt Y) k^(−2H).                    (5)

For `σ≤4/5`, H≥1/2. If H>1/2 this is at most `D^(2σ−1)Y^H K^(1−2H)`; H=1/2 costs a logarithm. With `D=Y^r` and `K=Y^(1−r)`, its exponent is at most 1 whenever

    r ≤ H/[2(σ−1+H)] = 3/[2(1+σ)].                           (6)

The right side is at least 5/6 on `1/2≤σ≤4/5`, so it covers the stated r range. For `σ>4/5`, H<1/2 and the sum in (5) is `≪sqrt(Y)` up to a logarithm. The global strip puts every such σ below `θ₀` after an arbitrarily small boundary loss, yielding the second term in (2). Finitely many bin widths, the T factor in (1), the inverse margins, and divisor masks are absorbed in ε by the indicated choice order.

This step needs the local inverse estimate above uniformly across the row family; an estimate only on average, a coefficient-dependent bound, or an uncontrolled height loss is insufficient. In particular the scalar exponent calculation alone does not verify (2).

## Why this bootstrap cannot improve its own zero-free input

For the single squarefree label d=1, the rows are the squares `u=k²`. The [exact square-sector spectral identity](../2026-10-29-power-row-spectral-boundary/README.md) shows that an all-row estimate of size `Y^(1+ε)` at `D=Y^r` already forces

    Θ_ζ ≤ 1/2 + 1/(4r).                                       (7)

At the threshold (3), this returns exactly θ₀. Any proof of the same all-row inverse moment beyond (3) would itself yield a stronger ζ zero-free half-plane; density averaging alone cannot make the square rows disappear. Formula (2) is therefore a fixed-point mechanism, not a bootstrap to a better boundary.

For comparison, the simpler split using a pointwise inverse bound derived from the global strip gives `Y+sqrt(Y)D^θ₀`, reaching O(Y) only at `r≤1/(2θ₀)≈0.57216735`; (7) then returns only `1/2+θ₀/2≈0.9369351`. The zero-density input improves this inverse-moment range up to the square-sector fixed point, subject to the stated uniformity conditions, but does not cross it.

**Independent review:** [High_match](INDEPENDENT-REVIEW.md) and Families checked the simple split, the need for logarithmic interpolation to obtain q^ε, and the density-assisted binning and finite-height contour mechanism, conditional on the stated local reciprocal and source zero-count estimates.
