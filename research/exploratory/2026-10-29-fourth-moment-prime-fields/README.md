# Prime-degree relative zeta families from a fourth-moment witness

**Status.** A source-qualified conditional density consequence of the [fourth-moment cyclic-box calculation](../2026-10-29-fourth-moment-cyclic-box/README.md). It uses the general-order conjugate-pair rectangular-sieve replay, the buffered t=1 detector and common-profile/height replay, the powered FHL-family bridge, and classical class field theory. These analytic replays and their cited preprints have not been independently established here. The result is a family-density statement for a relative quotient, not an individual zero-free region or an exhaustive priority claim.

For each fixed n≥4, let K contain μ_n and use the source FHL characters and fixed good set S. For good coprime squarefree ideals A,B in boxes `NA≈X^a`, `NB≈X^(1−a)`, form `χ_(AB^(n−1))`. At σ=4/5 the cited fourth-moment calculation gives, subject to its inputs, the following zero-count bound in a sufficiently short polynomial-height window:

    Σ_(A,B) N(4/5,X^τ; χ_(AB^(n−1))) ≪ X^(R_n+ε),           (1)

where ε>0 is fixed first and

    n=4,5,6: a=(3n−10)/[30(n−2)],   R_n=1/2+2/(3n);
    n≥7:     a=1/[3(n−2)],          R_n=3/5.                 (2)

These are counts over labels, with multiplicity of zeros. Constants, finite sectors and τ may depend on n,K,S and ε. The source box moment is applied to the common coefficient vector and its good zero masks; the fixed-height profile and Sobolev transfer remain explicit inputs. For composite n, (1) alone does not bound all powers needed for a relative-zeta product.

In particular, p=5 gives `(a,R)=(1/18,19/30)` and p=7 gives `(a,R)=(1/15,3/5)`. Their proof can be checked directly. Set δ=3/5 and

    E_n(x)=max{1,c+x,1−c+2x/n},
    c=[1+(n−2)a]/n,
    f_n(x)=E_n(x)−δx.                                       (3)

The inverse second-moment count has exponent f_n(r), and the ordinary fourth-moment count has exponent f_n(2m). Squaring the ordinary polynomial creates divisor-bounded coefficients; writing q=q₁v² with q₁ squarefree makes χ_g(v²) a row contraction for each fixed v. The source sieve applies to the common q₁ coefficients, their squared mass is `≪X^ε/(Nv)²`, and Minkowski costs `Σ 1/Nv≪X^ε`. The detector at t=1 gives `r+m≥1−O(η)` and `m≤1/2+O(η)`, with arbitrarily small fixed η. Thus for `r≥2/3` use f_n(r), and for `r≤2/3` use f_n(2m): in the latter case the **actual** m range gives `2m∈[2/3,1]` up to O(η). With c=7/30 for p=5 all three faces of f₅ on `[2/3,1]` are at most 19/30; with c=4/21 for p=7 all three faces of f₇ there are at most 3/5. The elementary source does not assume `m=1−r`; bin, profile and height losses are selected before τ. The general-n minimax and exact rational values are in the linked calculation.

## Cyclic quintic and septic fields

Take `K=Q(ζ_p)` with p=5 or 7, and restrict A,B to distinct good prime ideals in the indicated positive-width boxes. Their primitive χ has order p and good conductor AB; bounded S-local conductor factors give `Nf(χ)≈X`. For each `1≤j≤p−1`, form the **entire** powered FHL family `χ_a^(j)=χ_a^j`. Since j is a unit modulo p, changing the fixed root embedding gives the same source construction with its finite ray phases and original good-prime zeros. Therefore (1) applies to each power, with a potentially different positive height exponent; choose τ smaller than their finite minimum. This is the source-family compatibility reviewed in the [powered-family bridge](../2026-10-29-full-order-density/POWERED-FAMILY-INDEPENDENT-REVIEW.md), not an appeal to conductor matching alone.

Class field theory attaches to χ a cyclic degree-p extension L/K. All χ^j have the same local kernel and primitive conductor at every place, including S, and

    ζ_L(s)/ζ_K(s)=∏_(j=1)^(p−1) L_K(s,χ^j),
    |D_L|=|D_K|^p [Nf(χ)]^(p−1) ≈ X^(p−1).                (4)

Each relative factor is entire. Taking a union of the finitely many power-family counts gives at most `O(X^(19/30+ε))` exceptional fields for p=5, and `O(X^(3/5+ε))` for p=7, in `Re s≥4/5`, `|Im s|≤X^τ`. Distinct prime pairs give distinct primitive source characters by their good local exponents, and a cyclic degree-p field has p−1 nontrivial characters, so its character-to-field fiber has size at most p−1. The prime ideal theorem supplies `≫X/(log X)²` distinct fields in each family.

For a discriminant parameter Y choose **one** top-scale box with X a fixed small multiple of `Y^(1/(p−1))`; its fixed constants put all fields under Y. If τ′<τ/(p−1), after accounting for fixed factors, the exceptional counts at `|Im s|≤Y^τ′` and the corresponding elementary lower counts are

    p=5:  O(Y^(19/120+ε)) exceptional;  ≫Y^(1/4)/(log Y)² fields;
    p=7:  O(Y^(1/10+ε)) exceptional;    ≫Y^(1/6)/(log Y)² fields.  (5)

These are density-one relative-quotient rectangles in the specified box-generated families. A cumulative union of smaller boxes would require the separate small-conductor/height split, not just the choice of τ′ above. Zeros of the fixed base ζ_K remain in ζ_L, so no full Dedekind-zeta conclusion follows.

For comparison, the earlier conditional optimized-box exponents were `23/35` and `47/75` in X, or `23/140` and `47/450` in discriminant; the reductions in (5) are `1/168` and `1/225` respectively. These are comparisons of different fixed boxes and rely on the cited fourth-moment source replay. The [targeted prior-art survey](../2026-10-29-optimized-cyclic-prior-art/README.md) records natural-index comparators; no complete literature or novelty claim is made.

For the **same new boxes**, conjugation reorders the natural label to `A^(p−1)B`. De Faveri's stated natural-index bound at σ=4/5 gives X-exponents `23/30` for p=5 and `436/519` for p=7, before their explicit height losses; the gaps from (1) are `2/15` and `623/2595`. The comparison applies to all p−1 factors via the same powered-family bridge, and is with this named source only.

**Independent review.** Other_families checked the scalar formulas, fourth-moment coefficient mass and actual detector range, powered FHL family and masks, conductor and field fibers, one-box height, and comparator arithmetic. The cited analytic inputs remain conditional. An [exact scalar check](../2026-10-29-quartic-fourth-detector/check_general.py) accompanies the general-n calculation.
