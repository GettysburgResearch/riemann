# A zero-free input for a separable auxiliary Möbius sum

**Status.** This is a conditional analytic observation and a limitation of applying it to the [long-dual small core](../2026-10-29-long-dual-frequency-localization/README.md). The stated uniform reciprocal control must be supplied by the finite-order Hecke zero-free input plus its standard uniform logarithmic-control argument; this note does not prove that source theorem or transfer the resulting scalar cancellation to the coupled physical kernel. No new zero-free region follows.

Fix K=Q(ω), the good set S, and a smooth annular `U∈C_c^∞((0,∞))`. Suppose that every primitive finite-order Hecke character χ in the relevant family has `L(s,χ)≠0` for Re s>θ₀, and suppose the standard uniform reciprocal consequence: for every η>0,

    |1/L^S(s,χ)| ≪_η [Q_χ(2+|Im s|)]^η
    whenever Re s≥θ₀+η,                                       (1)

with Qχ its finite conductor norm. The fixed S factors and additional good-prime deletions at a modulus D cost `(ND)^η` in this half-plane. The principal character is included: its L-function pole at 1 becomes a zero of the reciprocal. The norm-frequency in a common smooth profile is handled by the same polynomial height allowance. Uniformity in moving Qχ, D and t, with the η-margin fixed before the scales grow, is essential; mere nonvanishing without (1) is not a numerical bound.

For each fixed η>0, Mellin inversion and a contour shift to `Re z=θ₀−1+2η` give

    Σ_(g good) μ(g)χ(g)/(Ng) · U(Ng/G)
       ≪_{U,η} G^(θ₀−1+2η) Qχ^η,                           (2)

with `(ND)^η` for an additional coprimality mask and fixed polynomial profile/height factors. Indeed the Dirichlet series in the absolute half-plane is `1/L^S(1+z,χ)` with the original zero extension. It is holomorphic in the shifted strip, even for principal χ, and the Mellin transform of U decays faster than any fixed polynomial. For conductor, mask and height polynomially bounded in Y, (2) saves `G^(1−θ₀)` up to `Y^ε`.

This does **not** currently give the saving to the physical auxiliary-g sum. The source imposes coupled conditions such as `g²|t` in the second-Poisson fibre, `(v,g)=1`, `g|r₁,r₂`, and g-dependent smooth kernels, finite phases and secondary gcds. A restriction to divisors of a varying t is not a complete smooth g-sum, and cannot be discarded inside a signed estimate. In the elementary weighted model `Σ_(g²|t) μ(g)/Ng=∏_(p²|t)(1−1/Np)`, the sign gives no power cancellation and its mean is positive; this model is not asserted to equal the physical coefficient. Fixed finite-ray characters can be absorbed into χ, but growing arithmetic twists and unitary angular types require the uniform hypotheses just stated.

For scale, the cited second-Poisson endpoint bound in the unit original gcd/divisor case has nonprincipal error `Y^(7/6)G^(−5/6)`. If one had a **separate proved factorization** that applies (2) to this same g dyad while preserving every other factor, the hypothetical new bound would be `Y^(7/6)G^(−5/6−(1−θ₀))`. At θ₀=4369347/5000000, it would meet the `Y^(21/20)` target for

    g:=log G/log Y ≥ (7/60)/(5/6+1−θ₀)
                      = 1750000/14391959 ≈0.121596.          (3)

The existing bound reaches this target only at g≥7/50=0.14. This is an algebraic benchmark conditional on a presently unproved separability/correlation estimate, not a new bound for those physical dyads. The unit label g=1 remains feasible and gives no Möbius cancellation at all, so even the hypothetical separable saving cannot close the full core by itself.

**Independent review.** Literature checked the shifted Mellin line, fixed and moving finite-prime masks, the threshold (3), and the absence of a physical separability proof. Under a genuinely uniform finite-order Hecke zero-free half-plane, standard Euler-log, Borel–Carathéodory and three-circles arguments with uniform strip growth yield the reciprocal control (1); this note retains that consequence explicitly because it does not reproduce the uniform proof or the formal-to-conventional Hecke bridge.
