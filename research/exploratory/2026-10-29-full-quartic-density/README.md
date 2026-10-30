# A conditional conductor-density bound for the full quartic family

**Status:** Source-dependent density theorem. It combines the [general-order squarefree-column rectangular-sieve replay](../2026-10-29-conjugate-conductor-sieve/README.md), the Goldmakher–Louvel quadratic Hecke large sieve over a fixed number field, and the [fixed-field short-detector proof replay](../2026-10-29-cubic-short-detector-proof/README.md). The quartic-to-quadratic source normalization has been independently matched in [the powered-family source review](../2026-10-29-full-order-density/POWERED-FAMILY-INDEPENDENT-REVIEW.md); the preprint theorems and proof replays have not been independently validated. It is a density-one statement, not an individual zero-free region, and no priority claim is made.

Fix K containing μ₄, S and the source quartic character family χ_g, and a fixed unitary Hecke character ν with finite conductor supported on S. Let g range over **all good fourth-power-free** ideals, written uniquely as

    g=a b² c³,   a,b,c squarefree and pairwise coprime.

At each good p dividing abc the corresponding local character is nontrivial, including the order-two character at p|b. Its primitive conductor has p to exponent one, and fixed bad-place conductors are uniformly bounded. Thus `N cond(νχ_g)≤X` implies `N(abc)≪X`, with both primitive conductor and original deleted radical `O(X)`.

The relevant source normalization is supplied by Goldmakher–Louvel §2, Remark 3 and Corollary 1.2: the n/2-th powers of the same FHL family satisfy the fixed-field **quadratic Hecke large sieve**, and for good squarefree q,b the primitive characters and de Faveri's original presentations agree, including the zero mask at `(q,b)>1`. Under these cited source inputs, for each fixed `2/3<σ<1` and ε>0 there exists τ>0 such that

    Σ_{g good fourth-free, N cond(νχ_g)≤X}
       N(σ,X^τ;νχ_g) ≪_{K,S,ν,σ,ε} X^{R(σ)+ε},               (1)

where zeros of the primitive inducing L-function are counted with multiplicity and

    δ=2σ−1,
    R(σ) = 7/6−δ/2                        (1/3<δ≤2/3),
           1−δ/[3(2−δ)]                   (2/3≤δ<1).              (2)

For example σ=4/5 gives `R=13/15`. Good prime labels have distinct primitive characters with conductor `O(Np)`, so there are ≫X/log X distinct family characters of conductor at most X and the exceptional proportion tends to zero. This includes the exponent-two labels excluded from the ±1-exponent subfamily.

## A mixed quartic/quadratic rectangular moment

Let a,b,c have dyadic norm scales A,B,C and ABC≪X; let q be good squarefree with `Nq≈Q` and λ be any common coefficient vector of squared mass 1. Partition the finite reciprocity class of g and absorb its q-phase into λ. The original character zero masks give

    χ_q(a b² c³)=χ_q(a c³) χ_q(b)².                            (3)

For fixed b, the factor χ_q(b)² is a common q-coefficient of modulus ≤1. The n=4 rectangular-sieve replay applied to a,c and then summed over b gives

    ≪ X^ε B [AC+M^(3/4)N^(1/4)Q+M^(1/4)N^(3/4)Q^(1/2)],      (4)

where M=min(A,C), N=max(A,C). Remove pairwise coprimality only after enlarging the nonnegative outer sum; original column-character zeros stay in (3).

For fixed a,c, the factor χ_q(a c³) is a common q-coefficient of modulus ≤1. The local square of a quartic residue character is the quadratic residue character at every good prime; finite reciprocity phases are fixed by ray-class partitions. Goldmakher–Louvel's quadratic Hecke sieve applies to the same FHL data, giving after summing over squarefree b and then over a,c

    ≪ X^ε AC(B+Q).                                              (5)

The two bounds are alternatives for the **same box**, not additive estimates with different coefficients. If `B≥X^(1/3)`, (5) is `≪X^ε[X+X^(2/3)Q]`. If `B≤X^(1/3)`, (4)'s Q coefficient is at most `B(AC)^(1/2)≤X^(1/2)B^(1/2)≤X^(2/3)`. Its square-root coefficient is at most `B(AC)^(3/4)≤X^(3/4)B^(1/4)≤X^(5/6)`, so

    X^(5/6)Q^(1/2) ≤ [X+X^(2/3)Q]/2.

Thus in either case the box contributes `≪X^ε[X+X^(2/3)Q]`. O(log³X) dyadic boxes and the finite ray classes cost a subpower. The proof also works when ABC is merely bounded above by a fixed multiple of X.

For normalized squarefree inverse blocks of length Q=X^r, coefficient mass is O(1), giving

    Σ_g |M_r(g)|² ≪ X^{E(r)+ε},   E(x)=max(1,2/3+x).            (6)

For a normalized ordinary block of length N=X^m, write each ideal j=qv² with q squarefree, factor off the row multiplier χ_g(v²) of modulus at most one, and apply the same squarefree sieve to the q sum. Its coefficient mass is `≪(Nv)^−2`; Minkowski and the ideal harmonic sum yield

    Σ_g |S_m(g)|² ≪ X^{E(m)+ε}.                                (7)

Both statements retain zero masks. The [Sobolev parameter lemma](../2026-10-29-detector-profile-sobolev/README.md) handles the finitely many rowwise zero real parts and heights using differentiated **common** coefficient vectors, at a fixed polynomial height cost.

## Saturated detector and minimax

The fixed-field replay, including the extension to any fixed t>1/2 and fixed floor above 1/2, gives for every row with a zero as in (1), after finite bin and dyadic grouping,

    r≤t+O(η), m≤1/2+O(η), r+m≥t−O(η),
    |M_r|²≥X^{δ_g r−η}, |S_m|²≥X^{δ_g m−η},  δ_g≥δ−O(e).

A pure norm presentation can occur only at g=1, and is counted separately. Choose e,η first, then the finite profile/height orders, and τ small enough to absorb Sobolev and the standard individual zero-count factor into ε. From (6)–(7), the exponent for any witness pair is at most

    min{f(r), f(m)},   f(x)=max(1,2/3+x)−δx.                   (8)

For `1/3<δ≤2/3`, choose t just above 1/2. At t=1/2 the function satisfies `f(x)≤R₀=7/6−δ/2` for `x∈[1/3,1/2]`. If x<1/3 and `f(x)>R₀`, then `x<1/2−1/(6δ)≤1/4`. Thus both f(r),f(m)>R₀ would contradict r+m≥1/2. Choosing t>1/2 and taking account of O(η) changes the bound by an arbitrarily small fixed loss.

For `2/3<δ<1`, choose `t=2/[3(2−δ)]∈(1/2,2/3)` and `R=1−δt/2=2/3+(1−δ)t`. On the feasible ranges r,m≤t, if `f(x)>R` then x<t/2: the upper affine face is at most R, and the lower face exceeds R only below t/2. Hence both f(r),f(m)>R would contradict r+m≥t. This proves (1)–(2) under the source inputs. At δ=2/3 use the first branch or a limiting t>1/2.

The same scalar relaxation shows why these exponents cannot be improved by changing only t while retaining (6)–(7): for t≤1, `r=m=1/2` is feasible and gives the first-branch lower bound. When δ>2/3, the feasible points `r=m=t/2` (for t≤2/3) and `r=t,m=0` enforce the second-branch balance. For t≥1, `r=t,m=0` gives a bound no smaller than the displayed optimum. These are feasible points of the relaxed inequalities, not asserted actual zeros.

## Comparison and scope

At σ=4/5, [de Faveri Corollary 1.5](https://arxiv.org/abs/2610.04045v1) gives fourth-free **index-ordered** exponent 15/22. Conjugate conductor reordering gives the generic conductor exponent 15/11, which is weaker than (1)'s 13/15. This comparison imports the source theorem and does not establish a priority claim.

For fixed Galois K and finite-order background, [Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3), controls all primitive finite-order Hecke characters and at fixed or polylogarithmic height gives conductor exponent `2 min(3/(2−σ),2/σ)(1−σ)`. For K=Q(i), this gives exponent 1 at σ=4/5, versus 13/15 here; the strict gap remains for a sufficiently small fixed height power after accounting for that source's T factor. For σ∈[4/5,5/6], its second branch is smaller than (2) precisely when `σ>(17−√145)/6≈0.8264009`, and it dominates throughout σ≥5/6. Applying that comparator to arbitrary fixed infinite-type ν requires the exact fixed angular-mode identification in the source; the comparison above is stated for finite-order ν. No exhaustive literature or priority search is claimed.
