# Quartic relative zeta functions over growing ray-class fields

**Status.** This is a source-qualified polynomial-height family consequence, conditional on the moving-common-twist quartic and quadratic estimates in [the companion note](2026-10-29-moving-unitary-twist-density/README.md), their de Faveri/FHL and quadratic large-sieve inputs, and the uniform detector/profile replay stated there. These recent inputs have not been independently established here. It is not an individual all-height zero-free region or an exhaustive priority claim.

Let `K=Q(i)` and let χ_u be the primitive quartic FHL character attached to a good fourth-free label u in a fixed source presentation. Fix `σ=4/5`. For every ε>0, assuming the named inputs, there is τ>0 such that all but

    O(X^(227/260+ε))                                          (1)

labels `Nu≤X` have the following **simultaneous** property. For every finite abelian extension H/K with conductor ideal of norm at most `X^(1/10)`, and for the cyclic quartic field `L_u/K` of an exact-order-four χ_u, the relative quotient

    ζ_{L_u H}(s)/ζ_H(s)                                       (2)

has no zeros in `Re s≥4/5`, `|Im s|≤X^τ`. The statement is only asserted for exact-order-four labels, and there are ≫X such labels already among good squarefree ideals. When `L_u⊂H` the quotient is 1. No restriction on `L_u∩H` is needed.

For each such H, the good squarefree labels give at least `≫X^(9/10)` distinct composita `L_uH`. At most the quantity in (1) of these have a zero in the rectangle. Thus their exceptional proportion tends to zero for ε<7/260. This bound is uniform in H and concerns the displayed family, not every extension of H of degree ≤4.

## Faithful twists and the quadratic core

Every character ν of such H is a finite-order K-Hecke character with conductor norm ≤`X^(1/10)`. The moving quartic estimate, with `κ=1/10<2/13`, gives `R₄=35/52` uniformly per ν. There are `O(X^(1/5+ε))` finite-order ν in the full conductor ball, by summing the sizes of ray class groups over conductor ideals. A union bound therefore gives (1) for the faithful factors χ_u and χ_u³: the latter is handled by the conjugate source embedding with the same u, or by conjugating both ν and χ_u and reflecting the two-sided height interval.

For χ_u², uniquely write the fourth-free label as `u=w c²`, where w is squarefree; w and c can share primes. On good ideals a the original zero extensions give

    χ_u²(a)=χ_w²(a) 1_((a,c)=1).                              (3)

After multiplication by ν, the deletion in (3) can only omit Euler factors nonvanishing for `Re s>0`, even if the factors have shared conductor primes or local cancellation. Thus zeros of the primitive inducing character are those of the primitive quadratic-core twist. Application of the quadratic moving estimate imports the powered-FHL-to-quadratic source matching, including any fixed finite ray-sector correction and original zeros; matching tame conductor supports alone would not suffice. There are `O((X/Nw)^(1/2+ε))` choices of c for each w.

Choose a fixed `a>2/5` arbitrarily close to 2/5. Discard all labels with `Nw≤X^a`: the ideal divisor bound gives `O(X^(1/2+a/2+ε))` labels, before any union over ν. For `Nw∼W≥X^a`, choose a fixed quadratic moving-twist parameter `κ₂<1/4` with `1/10<aκ₂`; then every twist in the global conductor ball satisfies `Nfν≤W^κ₂`. The quadratic moving estimate at 4/5 has exponent `R₂=1/2` uniformly in ν. A per-ν dyadic sum, weighted by the c multiplicity, is `O(X^(1/2+ε))`; summing over all ν gives `O(X^(7/10+ε))`. Choose a sufficiently close to 2/5, and subsequently choose the common height exponent below a times the local quadratic allowance. Both small- and large-core bounds are strictly smaller than `227/260`. The primitive pure-norm cases are already included in the moving-density input. Constants, fixed S-sectors, overlaps and dyadic sums are absorbed in the ε-loss.

## The compositum factorization

Put `M=L_uH`, `G=Gal(M/K)`, and let A be the subgroup of its character group consisting of characters inflated from `Gal(H/K)`. The finite abelian Artin factorization gives, using primitive all-place Hecke L-functions,

    ζ_M(s)/ζ_H(s)=∏_{ψ∈Ĝ∖A} L_K(s,ψ).                          (4)

Each character ψ in this product is nontrivial on `Gal(M/H)`. The Galois group G is the fibre product of `Gal(L_u/K)` and `Gal(H/K)` over their common quotient `Gal(L_u∩H/K)`. Every character of the subgroup G extends to a character of the finite abelian direct product: equivalently, every ψ is the restriction to G of a product `χ_u^j ν` with `j∈{0,1,2,3}` and ν a character of H. If ψ is nontrivial on `Gal(M/H)`, necessarily `j≠0`. Every such pair restricts to the fibre product; the representation need not be unique. Thus every factor in (4) is one of the primitive twists controlled above. No assertion that the two extensions are disjoint is used. When the source uses S-good zero-extended presentations, omitted Euler factors have no zeros in `Re s>0`.

## Counting distinct composita

The good squarefree labels supply ≫X distinct χ_u, since the good tame conductor of χ_u is u; at most two generate the same quartic L_u. Fix H as above. Every compositum M has `[M:K]≤4[H:K]≪X^(1/10)`, because the ray-class exact sequence bounds `[H:K]` by a fixed multiple of its conductor norm. As G is finite abelian, the number of its characters of order dividing four is at most |G|. Hence M contains `O(X^(1/10))` cyclic quartic K-subfields and accounts for `O(X^(1/10))` of the squarefree labels. This yields ≫X^(9/10) distinct composita for each H. Each exceptional M has an exceptional label, so (1) bounds the number of exceptional M. Since `9/10−227/260=7/260`, the displayed proportion tends to zero after taking ε smaller than this gap.

This counting is for fixed X and each H separately; the same exceptional-label set works simultaneously for all H in the conductor ball. No fixed-discriminant ordering or nonvanishing of ζ_H itself is implied.

## Elementary 2-extension improvement

If H/K is elementary abelian of exponent 2, all its characters ν are quadratic or trivial. For fixed K there are `O(Q^(1+ε))` such characters with conductor norm ≤Q: outside the finite set above 2, a quadratic local character has squarefree tame conductor and at most one nontrivial inertia character per prime; two characters with the same tame inertia data differ by a quadratic character unramified outside that finite set, of which there are finitely many. Counting possible tame conductor ideals gives the stated bound; the finitely many wild local choices are absorbed in the constant.

At `κ=1/10`, this reduces the faithful-factor union bound to

    X^(35/52+1/10+ε)=X^(201/260+ε).                           (5)

The small-core discard remains `X^(1/2+a/2+ε)` for any fixed a>2/5, and the large-core quadratic union is `X^(1/2+1/10+ε)`. Both are strictly smaller than (5) when a is sufficiently near 2/5. The same quotient, intersection and distinct-compositum argument therefore holds simultaneously for every elementary 2-extension H in the conductor ball, with (5) as its exception bound. More generally the same method gives exponent `35/52+κ` for each fixed `0<κ<2/13`, since the small-core cost approaches `1/2+2κ<35/52+κ`; the quadratic-twist margin still requires choosing `a>4κ` and a sufficiently small common height.

For one fixed H in the general abelian conductor ball, the same improved exponent `35/52+κ` follows without the elementary-2 assumption: H has only `[H:K]≪X^κ` characters. This per-H bound is uniform in H, but its exceptional-label set can depend on H. At κ=1/10 it gives (5) and ≫X^(9/10) distinct composita for every H separately. More generally `35/52+κ<1−κ` for `κ<2/13`, so the same distinct-compositum density conclusion holds throughout that range.

**Independent review.** Families checked the fibre-product extension, nontrivial intersections, both conductor-ball character counts, the quadratic small/large-core split, original masks, common height and distinct-compositum fibers under the named source and detector inputs.
