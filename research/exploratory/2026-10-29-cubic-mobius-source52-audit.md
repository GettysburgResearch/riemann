# What paper 52's cubic Möbius mean does and does not transfer

**Status.** This traces the stated result of [rStation paper 52 v5](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5); its source estimates and full proof are not independently verified. No new zero-free region is claimed. Use the notation of [the cubic power-row target](../2026-10-29-cubic-power-row-target/README.md), with row cutoff Y and normalized inverse length D.

Paper 52 Corollary 3.10 (N1), applied with one inverse factor, **principal** fixed finite character, a common smooth profile and common deletion, states for every D≥1

    Σ_(0<Nu≤Y) |D^(−1/2)Σ_n μ(n)χ_u(n)W(Nn/D)|²
       ≪_(ε) (YD)^ε [Y+Y^(1/3)D].                           (1)

The sum is over good primary **natural** rows, not just cube-free rows; χ_u(n) is the zero-extended cubic symbol. Cube rows, their principal inducing characters and all masks remain included. The source allows a fixed number of inverse factors, common norm-twist heights with fixed polynomial cost, common deletion of fixed-polynomial norm, and compact smooth profiles. It does not assert the same estimate with an arbitrary fixed noncubic finite character, row-dependent profiles, arbitrary coefficients, or a sextic row character. Cubic reciprocity and the fixed S/primary conventions must be matched before applying it to χ_n(u).

At `D=Y^(9/10)` (1) is `≪Y^(37/30+ε)`; the O(Y) target requires a further Y^(7/30) saving. The source bound alone, inserted in cube-row extraction, yields only the trivial Θ_(ζ_K)≤1. The squarefree arbitrary-coefficient operator upper/lower at the same scales is Y^(19/15±ε), and does not constrain the actual Möbius vector from below.

## Source mechanism and its scope

Section 3.8 derives its principal-twist cube-free inverse estimate from a reverse-Poisson identity, source cubic Gauss-series evaluations, and an averaged Type I/II estimate that preserves the cube-free product-row zero. It obtains the unnormalized bound `PY+P^(1/3)Y²`; central normalization gives `P+P^(1/3)Y` for inverse length Y≤P. This is coefficient-specific and keeps the actual μ. Section 3.9 extends to fixed products of inverse factors with common profiles via a common Mellin integral, not by multiplying independent moment bounds.

Section 3.10 then writes each natural row uniquely as `h=k q³` with cube-free k and retains the identity `χ_h(n)=χ_k(n)1_((n,q)=1)`. For fixed q it applies the cube-free mean with common deletion `rad(q)` and uses a generic cube-free bound for the short-core range. Summing q gives the term `Y^(1/3)D` in (1). This positive lifting includes principal k=1 and therefore cannot be treated as a signed cancellation. At the target scale, using the generic bound over short cores is exactly where the source pays the D term per cube root; this is a source-upper-bound diagnosis, not a lower bound on those rows.

## Cubic dual and sextic core

Proposition 3.8 (R3) in the same paper states a positive all-natural-row second moment for `μ(n)G(n) overlineχ_n(ch)`, G a normalized cubic Gauss sum, fixed common puncture and fixed nonzero c. The cubic-Poisson coefficient is the conjugate of μγ₂, up to the normalization fixed in [the cubic target note](../2026-10-29-cubic-power-row-target/README.md). The source's trace-additive G differs from γ₂ by the fixed cubic factor at λ=1+2ω; formally this is absorbed in the fixed row twist c=λ². The printed R3 statement permits fixed nonzero c, and the proof after (R5b) explicitly restores the prime above 3 and fixed numerator multipliers. Physical Fourier separations and masks must still be matched in an actual signed correlation. At schematic scales H=D²/Y=Y^(4/5), D=Y^(9/10), R3's dominant `(HD)^(2/3)` is Y^(17/15), and the physical prefactor Y/D gives Y^(37/30). This recovers the same exponent as (1), not the missing Y-bound. R3 is a **positive** mean: it does not evaluate the signed physical diagonal or justify cancellation among its gcd dyads.

For the sextic signed core, the first dual column is `α⁻¹γ₂(n)χ₆,n(v)` up to fixed phases, equivalently a μγ₋₁ coefficient. It is not the R3 μγ₂ coefficient. Moreover the row character is sextic rather than cubic. The identity `χ₆,n(v)=χ₆,n(v)^4χ₆,n(v)^3` leaves a moving quadratic factor tied to the same v; R3 permits a fixed cubic twist c and common column coefficients, not this row-dependent quadratic twist. Applying a quadratic sieve after treating the cubic part as common is therefore unjustified. Restricting to a special row subset does not bound the remaining sextic rows. The source provides no direct estimate for the full sextic physical correlation.

An arithmetic improvement could in principle retain the signed Fourier kernel and its diagonal cancellation, control the shared moving cubic/quadratic twist, or exploit μ in the residual small-core terms. None of those estimates is supplied by (1), (R3), or the paper's L-weighted mollifier precedents. They remain concrete gaps, not counterexamples to a possible stronger theorem.

**Independent review:** Families checked the exact principal-twist N1 hypotheses, natural-row cube masks and exponents, as well as the additive-character conversion `G(n)=overlineχ₃,n(λ)γ₂(n)`, fixed c=λ² in R3 and the Y^(17/15) dual bound. The full physical signed transfer and cited analytic inputs remain separate gates.
