# A local mixed-moment target for a strict density improvement

**Stronger sixth-order source:** for sextic rows over the specific Liu field range and assuming the indicated source matching, Liu’s claimed inverse moment already beats the generic Θ₆ baseline considered below. [The source-level minimax note](../2026-10-29-liu-source-minimax-barrier.md) gives the correspondingly stronger local target. This earlier general-n reduction remains applicable where no such stronger inverse input is available.

**Status.** This is a rigorous reduction conditional on the source-qualified [direct density and detector inputs](../2026-10-29-direct-nfree-density/README.md) and the additional mixed-moment hypothesis below. The mixed-moment hypothesis is **unproved** here. The conclusion is a stronger family density bound, not an individual zero-free region.

Fix n≥4, K, S and FHL data as in the direct note, and fix `1/2+1/n<σ<1−1/(2n)`. Put δ=2σ−1, and

    t*=3(n−3)/[n(3−δ)−7],   L=2t*/3,
    R=2/n+(1−1/n−δ)t*,   B(x)=2/n+(1−1/n)x.                (1)

Assume there are fixed positive numbers κ,c such that, uniformly for all dyadic r,m with `|r−L|≤c`, `|m−L/2|≤c`, all common β and frequency profiles required by the source detector and its fixed first derivatives, and the two fixed character orientations,

    Σ_{u good,n-free;Nu≤X} |M_r(u) S_m(u)|²
        ≪ X^[B(r+m)−κ+ε].                                    (2)

Here M is the normalized actual Möbius inverse block and S is the normalized actual ordinary block, with their original Hecke masks, as in the linked detector proof. The bound must hold after the common-profile Fourier and Sobolev reductions, with their fixed polynomial height dependence absorbed by taking a sufficiently small global height exponent. The constants may depend on the fixed data and profile orders; they must be uniform in the displayed neighborhood. For D=X^r, N=X^m the product has common coefficients

    c_a=(DN)^−1/2 Σ_{lk=a} μ_K(l) W₁(Nl/D)W₂(Nk/N),         (3)

with the actual smooth profiles, normalized powers and zero masks retained. In particular (2) concerns these structured restricted Möbius divisor sums, not all coefficient vectors. On the neighborhood, r+m>1, and B is exactly the fourth unnormalized face of de Faveri's generic Θ_n bound; (2) asks for a fixed power saving over that face.

Under (2), there are κ'>0 and τ>0 such that

    Σ_{u good,n-free;Nu≤X} N(σ,X^τ;χ_u) ≪ X^(R−κ'+ε).       (4)

## Proof of the localization

Write f(x) for the maximum of the four threshold-divided faces in the direct note, and let

    D_t={(r,m): 0≤r≤t, 0≤m≤1/2, r+m≥t}.

At t=t*, the direct inverse-second/ordinary-fourth count exponent is `min(f(r),f(2m))≤R`. Its equality locus in D_t* is exactly

    {(L,L/2)} ∪ {(t*,m): 0≤m≤L/2}.                            (5)

Indeed r≥t*−1/2>1/2. On `[1/2,1]`, f=f₂ is strictly decreasing, and on `[1,t*]`, f=f₃ is strictly increasing. Thus f(r)=R only at r=L or r=t*. On `[0,1]`, f(x)≤R precisely for x≥L, with equality at x=L; the admissible set excludes simultaneously r<L and 2m<L, since then r+m<t*. These facts give (5).

Choose a closed neighborhood U of (L,L/2) small enough that it lies inside the c-neighborhood in (2) and that `f₃(r+m)≤R+κ/4` on U. Set `t=t*−η>1` for a sufficiently small fixed η>0. By continuity and compactness, outside U and a small neighborhood of the vertical part of (5), the original `min(f(r),f(2m))` is at most R minus a fixed positive amount for all sufficiently small η. Inside that vertical neighborhood the cutoff r≤t*−η and the strictly increasing f₃ give a saving at least `(1−1/n−δ)η`, after shrinking the neighborhood so r>1. Thus there is a fixed γ>0 such that the original moments already give exponent ≤R−γ outside U.

Inside U, saturation gives `|M_r S_m|²≫X^[δ(r+m)−o(1)]`, so Markov's inequality and (2) give exponent `B(r+m)−δ(r+m)−κ+o(1)=f₃(r+m)−κ+o(1)≤R−3κ/4+o(1)`. A finite dyadic/profile partition and a sufficiently small height power preserve a positive fraction of both savings, proving (4). The detector inequalities have arbitrarily small fixed losses, which are chosen only after η, U and κ; they do not alter the compactness argument.

## Why the hypothesis is substantive

[The exact coefficient obstruction](../2026-10-29-mixed-witness-coefficient-obstruction.md) constructs prime-pair coefficients at D=N² whose squared ℓ² mass is ≫`1/(log D log N)`, uniformly under the stated fixed profiles and phases. Thus a power saving in (2) cannot come just from discarding the product coefficient norm or a general Cauchy–Schwarz estimate. It must exploit cancellation in the row correlations for the actual Möbius-supported coefficients, an additional detector restriction, or another input. The lower bound on coefficients does **not** give a lower bound for the row moment and does not refute (2).

A targeted source search did not locate (2). [rStation paper 52 v5](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5) Theorem 3.11 gives an inverse–ordinary mixed estimate for a principal-twist **cubic** Eisenstein family; it is not a sextic or general-order result. At the formal sextic target scales below, that theorem’s `X+X^(1/3)Y` face gives `172/111`, while generic cubic Θ₃ gives `164/111`; its separate nonprincipal one-ordinary-factor bound ties the latter exponent. These are only arithmetic comparisons across different families. [Liu, Theorem 11.2](https://arxiv.org/html/2610.26835v1#S11.Thmtheorem2) treats a sextic inverse times selected **prime sums** under `r+2z<1` and `2r+8z<3`, which do not cover even the formal balanced witness at n=6, σ=4/5: `r=30/37`, `m=15/37` give `r+2m=60/37>1` and `2r+8m=180/37>3`. The ordinary block in (2) is also broader than a prime sum. These recent sources have not been independently verified here, and this search is not exhaustive.

**Independent review.** High_match verified the exact equality locus, the cutoff and compactness argument, and the required common-profile, derivative and height quantifiers. This review does not prove the mixed-moment hypothesis.
