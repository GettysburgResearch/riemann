# A fixed-target obstruction to amplification by common twists

**Scope.** This is an elementary restriction on two proposed uses of the source-qualified moving-twist density bounds. It is not an impossibility theorem for other amplification methods, and it does not prove or disprove a zero-free strip. The input is the good tame-local FHL character identity and its original masks; the detector and recent large-sieve bounds are needed only for the comparisons below.

Fix K, a good set S and n≥2. Let χ_u be the FHL character at a good n-free label u, and assume at every good prime p the inertia character has exact order `n/gcd(n,v_p(u))`, while its primitive conductor norm is `≪_{K,S,n}Nrad(u)` including the bounded fixed-S part. Fix a unitary target character η with finite conductor. Write `Q=X^κ`.

## Faithful twists

Suppose the primitive characters satisfy

    (νχ_u)^* = η,       Nfν≤Q.                                  (1)

At every good p dividing u but not fη, the local χ_u is nontrivial on inertia, so ν must be ramified there. Thus

    Nrad(u) ≤ Nfη · Nrad(fν) ≤ Nfη · Q.                         (2)

For each squarefree ideal a there are at most `(n−1)^ω(a)` n-free ideals u with radical a. The fixed-field ideal divisor bound and ideal counting give, for every ε>0,

    #{u good, n-free : (1)} ≪_{K,n,η,ε} Q^(1+ε).              (3)

Hence if κ<1, representing a fixed target by twists with conductor ≤X^κ can populate only `O(X^(κ+ε))` labels among the O(X) natural labels. Conversely, when η is finite-order, for each good squarefree u with Nu≤c_η Q the finite-order character `ν=ηχ_u^(−1)` has conductor norm ≤Q for a fixed sufficiently small c_η. There are ≫Q such u. Thus the exponent κ is the correct scale up to subsidiary powers, not just an artifact of an overly loose upper bound.

For one fixed finite abelian extension H/K with conductor f_H, every ν factoring through H has conductor dividing f_H. The primes appearing in rad(u) are then contained in the fixed support of `fη f_H`, so the sharper count is

    #{u : η=νχ_u for some ν∈Ĥ} ≪_{K,n,η,ε} (Nf_H)^ε.          (4)

The implied constant in (4) is uniform as H varies. The same conclusion holds for a norm translate of η, since norm characters are trivial on finite inertia.

## Implication for the density-union approach

A fixed target zero in `Re s≥σ` eventually lies in every growing height window. It therefore marks every u satisfying (1) as exceptional for its corresponding ν. But the simultaneous conductor-ball estimate [in the moving-twist note](../2026-10-29-moving-unitary-twist-density/README.md) bounds all exceptional labels by `X^(E(κ)+2κ+ε)`, whereas the fixed target can account for only `X^(κ+o(1))` of them. The union bound by itself therefore cannot force that fixed zero to disappear; for fixed H the analogous possible replication in (4) is even smaller. For κ≥1 the elementary Q² twist-count loss is already at least X², so that same union-bound method does not give an o(X) exceptional set.

There is a precise reason why the alternative `ν_u=ηχ_u^(−1)` cannot simply be substituted in the existing large-sieve proof: ν_u then depends on the row, and the common character factor becomes

    ν_u(a)χ_u(a)=η(a)                                          (5)

at ideals coprime to the source presentations, with their respective zero masks retained elsewhere. The column vector is no longer common across rows after the separate original masks are included, and the displayed Θₙ operator estimate does not provide the moving-twist uniformity used for a fixed ν. In particular, if ν_u is given as the inverse of the source presentation with its same zero mask, every row polynomial is the same target polynomial with the u-dependent coprimality mask; it is not a new oscillating χ_u family. A bound for this diagonal row-dependent choice would require a genuinely new input and can have individual zero-free consequences.

## Nonfaithful powers and full zeta factors

For a power χ_u^j, let g=gcd(j,n) and q=n/g. At each good prime, `(χ_u^j)` depends on the valuation of u only modulo q. Given a fixed η and ν, the conditions `(νχ_u^j)^*=η` fix those residues, so u has a fixed q-free core v and can be written `u=v b^q`, where the good valuations of b are at most g−1 and may overlap those of v. Ideal counting yields at most `O(X^(1/q+ε))=O(X^(g/n+ε))` such labels up to X. In the quadratic-power case j=n/2 this is the familiar square-root multiplicity `u=w c²`; it explains why lifting a core count to all natural quartic/sextic labels can have an X^(1/2) floor. This observation is not a zero-free proof: powers with a repeated core do not form the same faithful Θₙ row family.

There is a converse amplification criterion for any target η actually represented by a fixed core: suppose `η=(νχ_v^j)^*`, with ν fixed, 1≤j<n, g=gcd(j,n)≥2, q=n/g, and a fixed q-free good v. For each squarefree good b coprime to v and the fixed bad set, put `u=v b^q`. Because q<n, these labels are n-free and number `≫X^(1/q)` for `Nu≤X`; the original source identity gives `χ_u^j=χ_v^j·1_{(·,b)=1}`, including the added zero mask. Therefore their primitive inducing twists are all η. If one proved a zero-density estimate for these powered factors over **all** such natural labels with exponent strictly less than `1/q` and a growing height window, it would exclude every fixed zero of η in the stated region. In particular, an exponent below 1/2 for the full natural quartic or sextic quadratic-power family would force zero-freeness for each fixed represented quadratic core. This is an exact implication, not an assertion that the currently available X^(1/2) power-family count can be improved. If a field formulation requires χ_u itself to have exact order n, choose v with an order-n local character; otherwise the statement concerns the full n-free label family. For faithful j, g=1 and q=n, the n-free condition forces b=1, so this replication mechanism is absent.

The alternative base-field route is genuine but needs a stronger source theorem. For every extension L/K, a zero of ζ_K is inherited by ζ_L whenever the complementary Artin factors are holomorphic there; for a cyclic extension these are nontrivial finite-order Hecke L-functions and are holomorphic. Thus a **full** ζ_L zero count that is o(the number of fields), uniform over a family of fields and with growing heights, would exclude each fixed base-field zero in the tested region. The relative quotient `ζ_L/ζ_K` cancels precisely this common factor and gives no such exclusion, while existing full-ζ applications in this workspace separately assume a base-field Dirichlet strip.

The difference is also visible in inverse coefficients. The explicit fixed-profile [quadratic full-inverse growth identity](../2026-10-29-riemann-quadratic-inverse-growth/README.md) relates a mean square containing `1/ζ(s)` to the supremum of real parts of ζ zeros; its lower/mean direction already shows that a sufficiently strong full-inverse moment would imply a zero-free statement. Likewise the [sixth-power-row boundary](../2026-10-29-power-row-spectral-boundary/README.md) records how principal power rows recover a fixed-field reciprocal zeta sum. Those source-qualified identities identify a real analytic hurdle, rather than ruling out a new structured estimate that overcomes it.

**Independent review.** High_match checked the faithful radical and finite-order converse, fixed-H support and divisor count, powered-core multiplicity and full-versus-relative zeta lifting. The FHL conductor bound and row-index/zero-mask identities remain explicit source inputs.
