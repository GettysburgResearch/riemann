# Growing archimedean analytic conductor for one common twist

**Status.** This is a source-qualified per-X extension of [the moving common-twist argument](README.md), assuming the standard conductor-uniform Hecke functional equation, gamma-ratio/strip estimates and the printed FHL/Θₙ inputs used there. Those external inputs and their fully uniform constants are not independently proved here. It is a polynomial-height family-density statement, not an individual zero-free half-plane. No counting or union bound over a continuum of twists follows from it.

Fix K, n and FHL data as in the companion note. For each X, let ν=ν_X be **one common unitary Hecke character**, with

    Nf_ν≤X^κ,        C∞(ν)≤X^λ,       κ,λ≥0 fixed.             (1)

Use the primitive finite ideal presentation of ν, extended by zero only at its conductor primes. Here C∞ is the full archimedean analytic conductor at height zero, defined from every real/complex gamma parameter with the corresponding local degree. For example, it is comparable, up to K-dependent constants, to a product of `(1+|t_v|+|m_v|)^{d_v}` over archimedean places, where d_v=1 at a real place and 2 at a complex place. This is stronger and more precise than bounding just one angular parameter. Put

    q=κ+λ.                                                     (2)

The primitive inducing character of νχ_u has finite conductor norm `≪X^(1+κ)` and the same archimedean parameters as ν (up to the FHL family's fixed finite set of types). The standard analytic-conductor inequality

    C∞(ν,it) ≪_K C∞(ν)(1+|t|)^[K:Q]                           (3)

makes the total analytic conductor `≪X^(1+q)(1+|t|)^[K:Q]`. Uniform gamma-ratio estimates and the Hecke functional equation therefore give the reflected-line exponent `(1+q)(a−1/2)` in place of `(1+κ)(a−1/2)`, plus the same small buffer losses and a fixed polynomial height cost. The finite deleted Euler factors still have radical norm `≪X^(1+κ)` and cost `X^ε` on fixed positive-real-part lines; cancellation of local primitive conductors does not remove the original zeros. Euler-log anchoring, Borel–Carathéodory and three-circles then give the conductor-uniform reciprocal estimate needed by the buffered detector. Their constants must be uniform in all ν satisfying (1).

Fix the finite detector ranges and loss parameters first, take τ>0 sufficiently small after the resulting gamma/profile orders are known, and only then choose the external Mellin/Fourier tail orders. The source Γ-convolution and the same single common height budget yield simultaneous witnesses, up to arbitrarily small fixed losses,

    r≤t,   m≤(1+q)/2,   r+m≥t,                                (4)

with the same squared thresholds `X^(δr)` and `X^(δm)`. The Θₙ source sees ν only as a common column multiplier of modulus ≤1, and fixed powers S^j use the same divisor bounds and fixed-v row contractions. Thus every endpoint formula proved in [EXPANDED-KAPPA.md](EXPANDED-KAPPA.md) remains valid after replacing κ there by q=κ+λ. In particular:

* In the middle interval `2/n<δ<1−1/n`, the original exponent is unchanged when `q<(nδ−2)/[n(3−δ)−7]`; for larger fixed q the bound is `max{R,f(1+q)}` with all four source faces retained.
* In the high interval `1−1/n<δ<1`, every fixed integer k≥2 satisfying `k+5nh≥4` gives

      E_k(q)=h·max{2(k+1)/(k+nh), k(1+q)/2},  h=1−δ.         (5)

The ordinary 2k-th moment is formed by expanding S^k; k and its finite profile orders are fixed before τ.

A possible pole-bearing inducing character is a pure norm character `|·|^{it_ν}`. Exact good-prime tame-inertia injectivity shows there is at most one such n-free label for each common ν. Its norm parameter can now be polynomially large, so a global zero count `N_K(|t_ν|+X^τ)` is too crude. Use instead the **local** fixed-field bound for zeros in an interval of length `O(X^τ)` centered at −t_ν:

    N_K(T+H)−N_K(T−H) ≪_K (H+1) log(T+H+3),                  (6)

with the usual interpretation near T=0. Since `|t_ν|` is polynomially bounded by (1), this is `O(X^τ log X)` and is absorbed by choosing τ sufficiently small. A pole itself is not a zero. This local zero-count input is essential to uniformity as the norm shift grows.

## Example and scope

For n=4, σ=4/5, take κ=1/20 and λ=1/10. Their sum is `q=3/20<2/13=t−1`, so the source-qualified uniform family exponent remains

    R=35/52.                                                   (7)

The implied constant and one sufficiently small τ are uniform over every common ν satisfying (1) with these fixed exponents and K. The character ν may change as X changes; this is not a statement about one fixed infinite family. Since archimedean unitary parameters contain continuous norm-shift directions, one cannot count all such ν by a finite conductor-ball ray-class argument. The finite-order simultaneous-twist consequences in the companion note remain separate.

**Independent review.** Families checked the gamma analytic-conductor inequality, reflected-line exponent, one-height-budget choice, local zero count around a growing pure-norm shift, the q=κ+λ witness bounds and the fixed-k endpoint formula, under the stated standard Hecke and source assumptions. No count of the continuous twist set was inferred.

High_match independently checked the full local-degree gamma conductor, fixed-power common coefficients, shifted pure-norm local count and the numerical example under the same stated inputs.
