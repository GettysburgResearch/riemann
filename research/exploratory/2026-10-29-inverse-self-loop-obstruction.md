# The inverse-moment self-loop at the long dual edge

**Status.** A source-qualified accounting and an exact obstruction to two formal decoupling arguments. It uses paper 5 v3 §§10.2–10.3 and its all-row inverse estimate (10.2), together with the [mask-preserving replay](2026-10-29-mask-preserving-second-poisson.md). It does not prove that the cited inputs or replay hold, rule out arithmetic cancellation, establish the target moment, or give a zero-free region.

Let P=Y^(6/5), fix d=k=g=(1), and consider a dual row dyad H≤H₀=P²/Y=Y^(7/5). The first Poisson contribution carries Y/P. After the second Poisson, the inverse row scale is T=P²/H and the normalized source prefactor is H/P. Thus a source-qualified nonprincipal **offdiagonal** dyad has schematic bound

    (Y/P)(H/P) I(T,P),       T=P²/H,                            (1)

up to the source's smooth/Fourier, finite-sector, ε and restoration factors. The physical theta diagonal must still be retained at fixed g: it cancels only after the original signed auxiliary-g projector is recombined, as in the [diagonal identity](2026-10-29-auxiliary-diagonal-cancellation.md). One must not subtract a diagonal from a positive norm bound and claim (1) controls a whole positive square.

The imported source input is

    I(T,P) ≪ (TP)^ε [T+T^(1/6)P^(5/6)].                        (2)

Substituting (2) into (1) gives `Y+Y(H/P)^(5/6)`. The nonprincipal dyads with H≤P are therefore controlled at Y^(1+ε); the potential excess occurs only in `P<H≤P²/Y`. At the maximal scale H=P²/Y, one has **exactly** T=Y and YH/P²=1, so the transformed inverse input is the original I(Y,P), with bound `Y+Y^(7/6)`. Repeating this same two-Poisson/positive-input maneuver at the long edge has no strict contraction in scale or normalization. This is a statement about this procedure and its available majorant, not a lower bound for the true arithmetic sum.

## An exact splitting and why second moments alone do not close it

For every fixed integer m≥2 and squarefree ideal n, put `f_m(a)=μ(a)m^(−ω(a))`. Then

    μ(n)=Σ_(a₁···a_m=n) f_m(a₁)···f_m(a_m).                  (3)

Each prime of n has m possible owners, so (3) is exact; the product is automatically pairwise coprime when n is squarefree. After a dyadic decomposition and common logarithmic Fourier separation, (3) writes a smooth Möbius column as a finite/logarithmic superposition of products of m character polynomials with their original coprime masks and scales whose product is ≍P. The splitting does not force each factor to be shorter: a unit factor leaves another at scale P. The coefficients are f_m, **not** the μ coefficients in (2), and their product has a common row variable. Dropping the masks or applying the μ-specific estimate (2) separately to these factors has no source justification.

The splitting alone cannot give a power saving by coefficient mass. On an annulus of scale A, fixed-field squarefree ideal counting and `m^(−2ω(a))≫_(m,ε) (Na)^(−ε)` imply

    Σ_(a sf, Na≈A) |f_m(a)|²/Na ≫_(m,ε) A^(−ε).              (4)

Thus an arbitrary-coefficient large sieve sees subpower-size mass even for a split factor; no fixed power of Y is saved merely from the m-way weights. Algebraically, for Re s>1 the Euler product `F_m(s)=∏_(p good)(1−(Np)^(−s)/m)` satisfies

    F_m(s)^m = ζ_(K,S)(s)^(−1) · H_m(s),
    H_m(s)=∏_(p good) (1−(Np)^(−s)/m)^m/(1−(Np)^(−s)),     (5)

where H_m is holomorphic and nonzero for Re s>1/2. This records precisely which new coefficient class arises; it is not a transfer of the μ-specific inverse moment.

There is also an abstract common-row obstruction. On N rows, let X_i=Z_i=√N for i=1 and 0 otherwise. Both normalized second moments `N^(−1)Σ|X_i|²` and `N^(−1)Σ|Z_i|²` equal 1, while `N^(−1)Σ|X_i Z_i|²=N`. Thus individual second-moment bounds cannot, on their own, bound a product's second moment; a uniform fourth/mixed moment, sign-sensitive bilinear input, or an explicit structural nonconcentration argument is required. This model does not assert that the actual character factors concentrate this way.

The self-loop pinpoints a concrete analytic target: either improve the source bound (2) for its actual inverse coefficients at the unequal scale T=Y, P=Y^(6/5), or prove an arithmetic joint estimate that preserves the signed auxiliary projector and rules out concentration in H>P. A shorter-factor identity and separate source-size second moments alone do neither.

## A weaker target that would still improve the boundary

An all-row exponent of 1 is not necessary to obtain a substantial conditional improvement. For the special fixed profile W and empty prime-slot product of the independently reviewed [sixth-power sector identity](2026-10-29-mobius-marked-boundary/README.md), an all-element-row bound

    Σ_(Nu≪Y) |P^(−1/2)Σ_n μ_K(n)χ_n(u)W(Nn/P)|²
       ≪_ε Y^(E+ε),        P=Y^(6/5),                         (6)

for every ε>0 forces the nontrivial-zero supremum Θ_K to satisfy

    Θ_K ≤ 1/2+(5/12)(E−1/6).                                  (7)

This follows directly from the sixth-power-row lower limsup `1/6+(12/5)(Θ_K−1/2)`, not from a detector implication. The estimate must include those original sixth-power rows and their nonunit zero masks; an estimate only for sixth-free or selected rows does not supply (7). Since ζ_K=ζ·L(χ_−3), (7) also excludes Riemann ζ zeros to the right of that bound.

For example, the unproved bound (6) at E=21/20 would imply `Θ_K≤125/144≈0.868056`, an improvement of about 0.00581 over the separate candidate θ₀=4369347/5000000=0.8738694, if the latter's own dependencies are discharged. An exponent `E<19949123/18750000≈1.06395323` already beats that candidate by this sixth-power extraction. None of those numerical implications proves (6).

In the [mask-preserving second-Poisson replay](2026-10-29-mask-preserving-second-poisson.md), the proposed offdiagonal bound for d,k,g exponents is `Y/K + Y^(7/6)/(K D₀^(5/6)G^(5/6))`. For E=21/20 it is at most Y^(E+ε) when

    5d+5g+6κ ≥ 7/10.                                          (8)

Thus that source-qualified partial calculation would leave only the smaller core `5d+5g+6κ<7/10`, plus its stated signed-kernel, fibre and tail gates, to be controlled at exponent 21/20. The diagonal cancellation must be performed across the signed g projector as described there. Even at d=κ=g=0 the available source offdiagonal estimate remains Y^(7/6), so the smaller core is not yet resolved.

An independent review checked the scale and coefficient identities, the m-way splitting and Euler product, the extraction arithmetic and (8), while retaining the source and offdiagonal-replay assumptions.
