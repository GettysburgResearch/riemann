# Relative-zeta density for every fixed prime degree p≥7

**Status.** This is a source-qualified conditional family consequence of the [optimized fourth-witness box calculation](../2026-10-29-fourth-moment-cyclic-box/README.md), the general-order rectangular-sieve replay, the buffered detector/common-profile/height transfer, the powered FHL-family bridge, and classical class field theory. Those analytic replays and cited preprints have not been independently established here. This gives density-one rectangles for selected relative quotients, not an individual zero-free region or an exhaustive priority claim.

Fix a prime p≥7, K=Q(ζ_p), and the source good set S. At σ=4/5 put

    a_p=(2p−5)/[(3p+5)(p−2)],     R_p=(3p+10)/(6p+10).      (1)

Take all good coprime squarefree ideals A,B in fixed positive-width boxes `NA≈X^a_p`, `NB≈X^(1−a_p)`, and let χ be the primitive character induced by the FHL presentation `χ_(AB^(p−1))`. Its good conductor is AB and its bad conductor is supported on S with bounded norm; hence `Nf(χ)≈X`. Its local character has order p at every good prime dividing A or B, so χ cuts out a cyclic degree-p extension L/K.

Under the stated inputs, for every ε>0 there is τ>0 such that at most

    O_(p,ε,S)(X^(R_p+ε))                                      (2)

of these distinct fields have a zero of the relative quotient `ζ_L/ζ_K` in `Re s≥4/5`, `|Im s|≤X^τ`. Their number is `≫X`, so this is a density-one relative-zero-free rectangle within the indicated family.

For every `j=1,…,p−1`, the powered family `χ_a^(j)=χ_a^j` is again the source FHL family with a compatible changed root embedding. Original zero masks and finite ray data are retained, and

    χ_(AB^(p−1))^j = χ_A^(j) overline(χ_B^(j))                 (3)

on good ideals. Thus the same bound (2) applies to **each** χ^j, with its own fixed constants and permitted height; choose the finite minimum of those heights. This is the [reviewed powered-family bridge](../2026-10-29-full-order-density/POWERED-FAMILY-INDEPENDENT-REVIEW.md), not a mere comparison of conductors. All χ^j have identical local kernels and primitive conductors, including at S. Consequently

    ζ_L/ζ_K=∏_(j=1)^(p−1) L_K(s,χ^j),
    |D_L|=|D_K|^p [Nf(χ)]^(p−1) ≍ X^(p−1).                  (4)

All factors are entire. Distinct ordered coprime squarefree pairs give distinct primitive source characters because their good local inertia exponents 1 and p−1 identify A and B; each cyclic p-field has p−1 nontrivial character generators, so the field fiber is at most p−1. The [squarefree-box count](../2026-10-29-squarefree-box-count/README.md) gives ≫X pairs and proves the lower count; a union bound covers the finitely many factors.

For absolute discriminant Y use **one** top-scale box `X≈Y^(1/(p−1))`, rescaled by fixed constants to ensure `|D_L|≤Y`. With a common τ′<τ/(p−1), the number of exceptional fields in `Re s≥4/5`, `|Im s|≤Y^τ′` is

    O(Y^[R_p/(p−1)+ε]),  versus  ≫Y^[1/(p−1)] fields.       (5)

This one-box height transfer does not imply a cumulative union over smaller X without a separate small-scale split. The fixed ζ_K factor remains in ζ_L and is not controlled by (4).

## Detector parameters and prior comparison

For `δ=2(4/5)−1=3/5`, the source calculation takes

    t=15p/(12p+20),    c=5/(3p+5),
    L=2t/3,            R_p=1−δL=(3p+10)/(6p+10).            (6)

The three affine faces of `E(x)−δx`, with `E(x)=max{1,c+x,1−c+2x/p}`, are at most R_p for x∈[L,t]. For a detector inverse witness r≥L use its second moment. Otherwise the actual constraints give `2m≥2(t−r)>L` and `2m≤1<t`, so the ordinary fourth moment applies on the **whole** possible interval. Here `1<t<3/2`; the printed cutoff range suffices, but the fixed-field simultaneous-witness and common-profile/fourier-height replays remain necessary. Fixed bin and overflow losses are chosen before τ.

The bound for the fourth ordinary moment follows by squaring a common block, splitting q=q₁v² with q₁ squarefree, treating χ_g(v²) as a fixed-v row contraction, and applying the source sieve to the common q₁ coefficients. Their squared mass is `≪X^ε/(Nv)²` and Minkowski costs `Σ1/Nv≪X^ε`. This does not insert row-dependent coefficient vectors into a single sieve application.

For the **same** box, conjugation changes the natural label to `A^(p−1)B`, of norm `X^[5p/(3p+5)]`. De Faveri Corollary 1.5 gives at σ=4/5 natural-index exponent

    D_p=(12p²−38p+5)/(21p²−80p+50).

Before its explicit polynomial height factor, its X-exponent exceeds R_p by

    [57p³−350p²+700p−500] /
       [2(3p+5)(21p²−80p+50)]  > 0,                          (7)

for every p≥7. Choose the power height and losses below this fixed gap. This is a direct comparison with that named source on this box, not an exhaustive claim about all previous results. For example p=7 gives `a=9/130`, `R=31/52`, discriminant exception exponent `31/312`; p=11 gives `a=17/342`, `R=43/76`, exponent `43/760`.

As p→∞ the exponent in (5) is asymptotic to `1/(2p)`, while the elementary family-count exponent is asymptotic to `1/p`. This compares the individual formulas for a sequence of **fixed-p families**. The constants, fixed sectors, analytic input and height τ′ may depend on p; no uniformity as p grows is claimed.

## A general-real-part continuum

For fixed p≥7 and `σ∈(1/2+1/p,1)`, put δ=2σ−1 and `δ_c=3/5+4/(5p)`. The same two moment bounds and powered-family transfer give the following source-qualified alternative, at a sufficiently small power height:

* If `2/p<δ≤4/p`, take
  `a=(pδ−2)/[6(p−2)]` and `R=1−5δ/6+2/(3p)`, using t=1.
* If `4/p<δ≤δ_c`, take
  `a=[p(1+δ)−4]/[(p−2)(p(3−δ)+4)]` and
  `R=[3p(1−σ)+2]/[p(2−σ)+2]`.
* If `δ_c≤δ<1`, take `a=0` and
  `R=1/p+(1−δ)·3(p−2)/[p(3−δ)−4]`.

The first two branches use coprime squarefree pairs and the last uses all good squarefree B; each supplies `≫X` distinct fields by the linked counting argument. Their formulas agree at the shared boundaries. The detailed detector cutoffs, scalar minimax and all fixed-loss choices are in the cited box note. These formulas need not beat other known density theorems: in particular, the squarefree high-σ branch is dominated in examples by de Faveri's natural-index theorem. Hu's preprint claims all-height nonvanishing for `Re s>7/8`; if accepted it supersedes positive exception bounds for σ>7/8, but does not by itself exclude zeros on the closed σ=7/8 boundary. Its source transfer has not been independently verified here.

## Conditional full Dedekind-zeta rectangles

For K=Q(ζ_p), the reviewed conventional Dirichlet interpretation of the staged candidate gives a separate base-field input: assuming admission and the semantic/source qualifications of the [retuned θ=0.8738694 candidate](../2026-10-29-return-retune-8738694/README.md), its Dirichlet half-plane applies to ζ and each nontrivial character modulo p. The exact Artin/Dirichlet factorization is

    ζ_K(s)=ζ(s) ∏_(χ mod p, χ≠1) L(s,χ),                       (8)

where nontrivial characters are primitive. The trivial factor is **ζ**, including the ramified Euler factor at p; using the imprimitive principal L-function without restoring that factor would not give this exact identity. Consequently ζ_K has no zeros in `Re s>θ` at any height and has its usual simple pole at 1.

Combine this base input with any of the relative-quotient estimates above. For every fixed σ>θ in the applicable range, all but the stated number of L have **full** ζ_L zero-free in the same rectangle, excluding its pole at s=1. The relative density bound and the base Dirichlet candidate are separate assumptions; no conventional E-Hecke bridge is needed for (8). The formal candidate's fresh Lean replay is not a tracker admission or an independent verification of its imported analytic chain.

For example, at p=11 and σ=437/500=0.874, the high-σ fourth-witness branch has

    a=0,   R=2656/6347,   R/(p−1)=1328/31735.                (9)

Thus, under both inputs, all but `O(Y^(1328/31735+ε))` of a one-box family of `≫Y^(1/10)` cyclic degree-11 extensions have ζ_L zero-free in `Re s≥437/500`, `|Im s|≤Y^τ′`, apart from its pole at 1. De Faveri Corollary 1.5 on the **same** squarefree-index family gives X-exponent `2100479/4803751`, larger than `2656/6347`, before the two sources' height losses. This is a named-source comparison, not an exhaustive priority claim. Hu's claimed open `Re s>7/8` theorem does not by itself cover σ=437/500, which is strictly below 7/8.

**Independent review.** Amplified_opt checked the powered-family and good-conductor scope, finite field fibers, one-box height/discriminant conversion, symbolic same-box natural-index difference (7), fixed-p asymptotics and the σ=437/500 example, including the exact Dirichlet factorization of ζ_K. This is conditional on the stated analytical replays and candidate interpretation; it does not establish tracker admission or an individual region beyond those inputs.
