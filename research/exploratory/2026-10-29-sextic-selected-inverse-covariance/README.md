# A selected single-inverse estimate from Hecke covariance

**Status:** A proposed source-qualified count for one common inverse and one prime slot; no global detector or zero-free return is proved. The Hecke subconvex input, finite-sector reciprocity and sixth-order large sieve are stated explicitly below. Row-dependent inverse coefficients or detector-selected profiles require a separate common-profile/Sobolev argument. No priority claim is made.

Let K=Q(ω), S be a fixed good-prime exclusion set containing the primes over 6, and let F be any subset of sixth-power-free good ideal rows `g` in a fixed ray sector with `Ng≈Y`. All original sextic zero masks and finite ray factors are retained. For fixed profiles and common row-independent coefficients, put

    M_D(g)=D^(−1/2) Σ_(a,S)=1 μ(a)ν(a)χ_a(g) W(Na/D),
    Q_P(g)=Σ_(p good prime, Np≈P) λ_p χ_p(g),
    Σ_p|λ_p|²≪1,    |λ_p|≪P^(−1/2).

Here ν is any fixed finite ray twist and W is a fixed smooth annular function. Fixed common norm twists are absorbed in the coefficients and do not change their absolute bounds. Let `D=Y^r`, `P=Y^z`, with fixed

    0≤r<min(z,1/2),  z>0.                                   (1)

Suppose on F that `|M_D(g)|²≥D^δ` and `|Q_P(g)|²≥P^σ` for fixed `δ,σ≥0`. Under the fixed-field sixth-order large sieve and the source-qualified Wu bound on finite-order Hecke characters, for every ε>0,

    #F ≪_ε Y^ε [Y^(1−δr−σz)
          +Y^(1/2+(359/256)(r+z)−δr−σz)].                   (2)

The inequality also holds for a nonnegative fixed smooth row weight V with `V≥1` on F's annulus. No row-existence, zero-location, or detector claim is made by (2).

## Proof

Let V be a fixed nonnegative smooth majorant for the row annulus. The unrestricted-row sextic large sieve, with the inverse's squarefree coefficients of squared mass `≪D^ε`, gives

    E_M=Σ_g V(Ng/Y)|M_D(g)|² ≪_ε Y^(1+ε),                    (3)

because `D≤Y^(1/2)` makes every term in the standard bound `Y+D Y^(1/6)+Y^(5/6)D^(1/3)+Y^(1/3)D^(5/6)` at most Y. The fixed finite ray/unit classes are partitioned before applying the source theorem.

Expand `Σ_g V|M_D Q_P|²`. Its p=q part is at most `(Σ_p|λ_p|²)E_M≪Y^(1+ε)`. For p≠q, the four source factors contain χ_p(g)barχ_q(g)χ_a(g)barχ_b(g). The annular inverse support has `Na,Nb≪D`, so `P≫D` makes the distinct slot ideals p,q coprime to both a and b. Thus the good local character at p is the nontrivial sextic slot character; finite fixed-ray projections cannot cancel it. The inducing Hecke character is nonprincipal, with conductor norm `Q≪P²D²`; any shared-prime zero masks at inverse indices are retained as Euler deletions.

For all good ideal rows the Euler product is `L(s,ξ)`, with fixed sector and source-mask factors. If one chooses to work directly with the sixth-free subfamily, its Euler product is `L(s,ξ)/L(6s,ξ^6)`. Mellin inversion at `Re s=1/2+η`, the absolutely convergent reciprocal of `L(6s,ξ^6)`, and [Wu's GL(1) subconvexity](../2026-10-29-hecke-gram-subconvex.md) with conductor exponent `103/512` give

    |Σ_(g good) V(Ng/Y) ξ(g) masks|
        ≪_ε Y^(1/2+ε) Q^(103/512+ε).                        (4)

The q-height factor is polynomial and is absorbed by the rapid decay of V's Mellin transform. Deleted-prime factors cost a small power of the radical. The inverse and prime coefficient ℓ¹ masses are respectively `≪D^(1/2+ε)` and `≪P^(1/2)`. Therefore the p≠q part is at most

    ≪_ε Y^(1/2+ε) (PD) · (P²D²)^(103/512+ε)
     = Y^(1/2+ε)(PD)^(359/256+ε).                           (5)

Positivity then gives `#F·D^δ P^σ≤Σ V|M_DQ_P|²`, and (2) follows. The identical proof with Hecke convexity exponent 1/4 has `3/2` in place of `359/256`. □

## Scalar comparison with PR94

Take the natural detector identification `σ=2δp`, `0≤δ≤1` and `0≤p≤1/2`, assuming the chosen slot and witness really have this normalization. Even optimistically ignoring all physical slot-cap and witness-length restrictions, optimize the maximum of the two exponents in (2). For fixed `r+z`, the minimum occurs near r=z because σ≤δ; balancing the terms forces `r+z=128/359`. The best relaxed infimum is

    1 − (64/359)(δ+σ) = 1 − (64/359)δ(1+2p).                 (6)

The strict condition r<z is approached from below. At the PR94 bottleneck `δ=223/500`, `p=1/2`, this gives `37739/44875≈0.84098050`. The existing count at that point is approximately `0.60937106`, so this single-inverse covariance estimate is far weaker there. Imposing the optimistic slot-width cap `z≤619/10000` and r<z raises even the first term to at least `1−2δ(619/10000)≈0.9447852`; the actual physical conductor capacity is no larger. Thus this calculation supplies no improvement to that fixed PR94 bottleneck or its zero-free return. The comparison uses the stated σ identification; matching it and all detector ranges to the source remains a separate obligation.

The method is still a different kind of selected estimate: the unrestricted moment input is only (3), and (2) can give a power saving from a large common prime slot without using the marked-inverse theorem. It is not asserted to beat all existing detector bounds, and the example is not a new zero-free region.

## Finitely many disjoint slots

The same estimate holds for a fixed number J of pairwise disjoint prime supports, with scales `P_j=Y^{z_j}`, normalized slot sums `Q_j`, and `r<min_j z_j`. Put `z=Σ_j z_j` and suppose `|Q_j(g)|²≥P_j^{σ_j}` on F. Expanding the product by prime tuples, identical tuples contribute at most `(∏_j Σ_p|λ_{j,p}|²)E_M`. In any unequal pair of tuples, some prime in a differing slot occurs neither in the other tuple nor in an inverse index: supports are disjoint and each P_j≫D. Its sextic local exponent is nonzero, so the row character is nonprincipal. The product tuple coefficient masses satisfy `ℓ¹≪(∏P_j)^(1/2)` and `ℓ²≪1`, while the conductor is at most a fixed factor times `(D∏P_j)²`. The same argument gives

    #F ≪_ε Y^(ε−δr−Σ_j σ_j z_j)
               · [Y+Y^(1/2+(359/256)(r+Σ_j z_j))].           (7)

For the source-style bounds `σ_j≤δ`, put z=Σz_j. The constraints give `r≤z/J`, so `δr+Σσ_j z_j≤δ z(1+1/J)≤2δz`. Thus multiple slots do not improve the optimistic single-slot comparison above when total prime width is capped. At `δ=223/500`, `p=1/2` and z≤619/10000, the first term is still at least `Y^0.9447852`, far above the existing 0.609371 count exponent. This assumes the source slot amplitudes match these individual lower bounds; actual aggregate selection and common-coefficient transport remain to be checked.

**Detector limitation and independent review:** High_match checked the all-row and sixth-free Hecke series, slot/inverse nonprincipality, finite masks, conductor and Wu exponent, tuple expansion and scalar comparison. The amplified simultaneous-witness branch cited in the source uses inverse length `r≥3/5−o(1)` at row base, whereas this estimate requires `r<1/2` and `r<min_j z_j`. Thus it does not apply to that branch; a separately established short-detector branch would still require full profile, height and witness matching.

Families independently checked the all-row covariance and multi-slot expansion, including the disjoint support and conductor conditions. The scalar minimax specifically uses `δ≤1`, as stated above.
