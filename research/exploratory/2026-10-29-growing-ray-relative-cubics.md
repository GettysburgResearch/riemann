# Cyclic-cubic relative zeta functions over growing abelian fields

**Status.** This is a source-qualified polynomial-height family result, conditional on the cubic moving-common-twist estimate and its sieve/detector/profile interfaces in [the companion note](2026-10-29-moving-unitary-twist-density/README.md). It is not an individual zero-free region or an exhaustive priority claim. Unlike a statement about the full ζ-function, it requires no Dirichlet zero-free input for the base field.

Let `K=Q(ζ₁₂)`, `θ=4369347/5000000`, and let χ_u be the primitive cubic FHL character attached to a good cube-free ideal u. For every ε>0 the cited moving-density inputs give a single τ>0 such that, for all but

    O(X^(74957259/118919590+ε))                               (1)

labels `Nu≤X`, the following holds simultaneously for every finite abelian H/K with conductor ideal norm ≤`X^(1/20)`. If χ_u is nontrivial, let `L_u/K` be its cyclic cubic class field. Then

    ζ_{L_uH}(s)/ζ_H(s)                                         (2)

has no zero in `Re s≥θ`, `|Im s|≤X^τ`. The trivial label is omitted, and `L_u⊂H` gives quotient 1. No disjointness condition is imposed.

For every such H the good squarefree labels provide at least `≫X^(19/20)` distinct composita `L_uH`, of which at most (1) are exceptional. As `74957259/118919590<19/20`, their exceptional proportion tends to zero for sufficiently small ε. The same exceptional-label set works for all H simultaneously; this is a specified family rather than a count of all cubic extensions of H.

## Proof

The moving cubic estimate in the cited note has

    R=6306530/11891959,  κ=1/20<608041/11891959,
    R+2κ=74957259/118919590.                                   (3)

It applies uniformly to every common finite-order unitary ν with conductor norm ≤`X^κ`, with a single height power and constants depending on the fixed field and losses. There are `O(X^(2κ+ε))` such characters, by summing ray-class group sizes over conductor ideals. The union bound gives (1) for `L(s,(νχ_u)^*)`. It also controls `χ_u²=conjugate(χ_u)` with the same label, since ν ranges over a set closed under conjugation and the height interval is symmetric. All primitive and S-good presentations have the same zeros for `Re s>0`, because omitted Euler factors are nonvanishing there. The source estimate counts any pure-norm exceptional rows in its stated scope.

For `M=L_uH`, put `G=Gal(M/K)` and let A be the characters inflated from `Gal(H/K)`. Primitive Artin factorization gives `ζ_M/ζ_H=∏_{ψ∈Ĝ∖A}L_K(s,ψ)`. The group G is the fibre product of `Gal(L_u/K)` and `Gal(H/K)` over their common quotient. Every character of G extends to the finite abelian direct product, so each ψ is a restriction of `χ_u^jν`, with `j∈{0,1,2}` and ν a character of H. A factor outside A is nontrivial on `Gal(M/H)`, hence has j≠0. Every ν of H has conductor dividing the conductor of H and is included in the union bound. This argument includes both possible intersections of a cubic field with H, namely K and L_u.

There are ≫X good squarefree labels with `Nu≤X`. Their good tame conductors distinguish them, and each cyclic cubic field has at most two generators among these characters. For a fixed H, `[M:K]≤3[H:K]≪X^(1/20)`, by the ray-class group bound. A finite abelian G has at most |G| characters of order dividing three, so a fixed M contains `O(X^(1/20))` cyclic cubic subfields and therefore accounts for `O(X^(1/20))` such squarefree labels. This proves the lower count. Every exceptional M is represented by an exceptional label, and (1) completes the proof.

## Larger conductor ball via a sixth moment

The same source-qualified moving-detector and fixed-power profile inputs give another conclusion for the larger conductor ball `Nf_H≤X^(1/10)`: all but

    O(X^(34618079/46959795+ε))                                (4)

labels have the simultaneous relative-zero-free property (2), with one sufficiently small height power. For each H in this ball the squarefree labels give ≫X^(9/10) distinct composita, and the number of exceptional composita is bounded by (4). Since `34618079/46959795<9/10`, the exceptional proportion again tends to zero. This is a separate conductor-versus-exponent tradeoff, not an improvement of the smaller-ball exponent in (1).

To see the altered scalar step, put `h=630653/2500000`, `δ=1−h`, and choose

    t=8/(3+3h)=20000000/9391959,
    L=3t/4=5000000/3130653,
    E=8h/(3+3h)=5045224/9391959.                              (5)

The cubic sieve's threshold-divided envelope is `f(x)=max{1−δx,hx,2/3+(2/3−δ)x}`. Its decreasing mixed face at L and increasing face at t both equal E, and the remaining face is smaller on `[L,t]`. If the inverse witness has `r≥L`, use its second moment. Otherwise the true detector constraints give `3m≥3(t−r)>L` and `3m≤3(1+κ)/2=33/20<t`, so expand the ordinary block to its fixed third power and use its sixth moment. The same squarefree-column decomposition, row contractions, divisor bounds and fixed-order Sobolev separation used for the fourth/eighth moments apply to this fixed power. The common twist is a common bounded coefficient multiplier. This requires the moving-conductor detector and polynomial-height uniformity stated in the companion note, including its original masks and local cancellation handling.

The per-ν exceptional exponent is E; the conductor-ball count costs `2κ=1/5`, giving exactly `E+1/5=34618079/46959795`. The fibre-product and field-count proofs above then apply with κ=1/10. All fixed detector and mesh losses are absorbed by ε before choosing a single height power τ.

For elementary abelian 2-extensions H the characters ν are quadratic or trivial. Over this fixed K their conductor ball has only `O(Q^(1+ε))` such characters: the tame quadratic inertia character is unique at each prime outside the fixed primes above 2, and characters with the same tame data differ by one of finitely many quadratic characters unramified outside those fixed primes. Thus, for this restricted H class, take the larger ball `Nf_H≤X^(1/5)`. The same k=3 argument still works because `3(1+1/5)/2=9/5<t`; its per-ν exponent remains E and the union costs only `1/5`. Hence (4) also applies simultaneously to this elementary-2 ball. For each such H the field count is ≫X^(4/5); as `34618079/46959795<4/5`, the exceptional proportion tends to zero. The same source and uniformity qualifications apply.

This elementary-2 exponent is **not** the strongest named-source bound. For ψ=χ_u^jν with j=1 or 2 and ν²=1, one has `ψ³=ν`, so ψ determines ν and then χ_u^j, and the tame exponent data distinguish the good labels. The primitive conductor of ψ is `≪X^(6/5)`. [Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677), applied over the fixed Galois field K, gives the fixed-height conductor exponent `4h/(2−h)=2522612/4369347`; after conductor conversion its exponent is

    (6/5)·2522612/4369347 = 5045224/7282245 ≈ 0.692812,     (5a)

which is smaller than (4). Its height loss can be absorbed into ε by shrinking τ. Thus the elementary-2 case also follows with (5a) from that named density input and the same character/field algebra; the moving-moment argument above is recorded as a separate derivation, not as an improvement over that comparator.

The same named conductor theorem also improves (4) for the general `X^(1/10)` twist ball after accounting for collisions. Fix a primitive ψ and an exact conductor ideal f of ν. Outside f the inertia of ψ determines each good local exponent of u; at each good prime in f there are at most three choices. The number of good labels per f is therefore `≪(Nf)^ε`, with fixed bad sectors absorbed into the constant. Summing over `Nf≤Q` gives `≪Q^(1+ε)` labels for each ψ. Since `Nf_ψ≪XQ`, the named bound yields exponent

    κ+(1+κ)·2522612/4369347,
    κ=1/10: 32118079/43693470≈0.735077,                      (5b)

strictly smaller than (4), again after absorbing height and divisor losses. At κ=1/20 this comparator is `19114733/29128980≈0.656210`, larger than the moving-moment exponent in (1), so it does not subsume that smaller-ball result. This is a comparison against the named general finite-order bound, not an exhaustive literature search.

There is also a per-H version for **all** finite abelian H/K with `Nf_H≤X^(1/5)`, without imposing exponent 2. For one H its character group has cardinality `[H:K]≪X^(1/5)`, so the union over its characters gives the same exception bound (4), uniformly in H. The ≫X^(4/5) distinct-compositum count still applies. The exceptional labels in this per-H conclusion may depend on H; the smaller exception set simultaneously valid for every H was proved only for the conductor balls stated above. The constants and τ remain uniform in H, so H may vary with X.

The per-H range extends to `Nf_H≤X` if the degree is controlled. Put `d=[H:K]`, `h=630653/2500000`, and choose the ordinary fourth-moment cutoff

    t=6/(2+3h)=15000000/6891959,
    L=2t/3,   E₂=6h/(2+3h)=3783918/6891959.                 (6)

Here `2<t<5/2`. On `[L,t]` the cubic envelope f has maximum E₂, achieved by its mixed face at L and its increasing face at t. The moving-twist detector with conductor parameter κ=1 gives `m≤1` up to small losses: if `r<L`, then `2m≥2(t−r)>L` and `2m≤2<t`, so use the ordinary fourth moment; otherwise use the inverse second moment. The same common-profile and fixed-mask source qualifications apply, including the uniform pure-norm treatment. Thus, for each H and one τ independent of H,

    exceptional labels ≪ d X^(E₂+ε),
    distinct squarefree-label composita ≫ X/d.                (7)

Consequently their exceptional proportion is `≪d² X^(E₂−1+ε)`. This tends to zero uniformly for bounded-degree H, and more generally when `d≤X^α` for fixed `α<(1−E₂)/2=3108041/13783918`, with ε chosen below the gap. The exceptional set may depend on H. The full-zeta implication in the next paragraph applies to these H when they are also abelian over Q and the Dirichlet candidate is admitted.

One can allow the still larger conductor ball `Nf_H≤X³` with a weaker exponent using only ordinary **second** moments. Now the moving conductor parameter is κ=3 and `m≤2`; choose

    t=4/(1+3h)=10000000/4391959,
    L=t/2,    E₁=4h/(1+3h)=2522612/4391959.                 (8)

Again `2<t<5/2`, and f≤E₁ on `[L,t]`: the decreasing mixed face at L and increasing face at t agree. For `r<L`, the detector gives `m≥t−r>L` and `m≤2<t`, so the ordinary second moment suffices; otherwise use the inverse second moment. Hence the per-H exception count is `≪d X^(E₁+ε)` and the squarefree-label compositum count is `≫X/d`. The proportion tends to zero uniformly for bounded d, or for `d≤X^α` with any fixed `α<(1−E₁)/2=1869347/8783918`. This version has a larger conductor range and a weaker exponent than (7), and it still requires the same uniform moving-detector/source inputs.

For comparison, applying the named Khale et al. all-character conductor bound separately to each fixed ν gives the X-exponents `2·2522612/4369347=5045224/4369347≈1.154686` at κ=1 and `4·2522612/4369347=10090448/4369347≈2.309372` at κ=3, before the same d factor and height losses. Both are weaker than the displayed E₂ and E₁, and can be worse than trivial row counting. De Faveri's original untwisted family theorem is not automatically uniform for these moving ν. This is a comparison with named bounds from a targeted, nonexhaustive search, conditional on the source matching and moving-detector replay above.

## Base-changed Hecke L-functions

For each H/K and u, Artin induction and class field theory give the primitive all-place identity

    L_H(s,χ_u∘N_{H/K})=∏_{ν∈Gal(H/K)^} L_K(s,χ_uν).        (9)

If `L_u∩H=K`, the pullback `χ_u∘N_{H/K}` has order three and every factor on the right occurs in the relative quotient (2). The per-H results above therefore also show that this base-changed Hecke L-function is zero-free in their stated closed rectangles for all but the same exceptional labels. The displayed identity uses primitive Hecke characters and includes all local places; omitting S-good Euler factors does not change zeros for `Re s>0`.

For the degree-sensitive `Nf_H≤X³` result, restrict to squarefree u. At most O(d) such labels have `L_u⊂H`, because H has at most d characters and good conductors distinguish the labels; for the allowed `d≤X^α` this leaves ≫X labels disjoint from H. Two such χ_u can have the same pullback only if their quotient is a character of H/K, so at most d labels give the same pulled-back character. Thus there are ≫X/d distinct order-three Hecke characters of H in this family, and at most `≪dX^(E₁+ε)` of their character-labelled L-functions are exceptional. Their exceptional proportion is controlled by the same `d²X^(E₁−1+ε)` bound. This counts characters, without claiming that all their L-functions are different as complex functions. If `L_u⊂H`, the pullback is instead trivial and the left side of (9) is `ζ_H`; no relative-quotient argument alone controls its zeros.

## Conditional full-zeta consequence

Assume in addition that the separately staged Dirichlet candidate has been admitted and has its conventional interpretation: every primitive Dirichlet L-function is zero-free in the open half-plane `Re s>θ`, away from the principal pole. For any H in the `X^(1/10)` conductor ball which is also abelian over Q, `ζ_H` is a finite product of primitive Dirichlet L-functions, so it has no zeros in that open half-plane at any height. Combining this with (4) yields the same exceptional-label and per-H compositum bounds for **full** `ζ_{L_uH}` in `Re s>θ`, `|Im s|≤X^τ`, excluding the pole at 1. The conclusion is simultaneous over all such H. It does not assert nonvanishing on `Re s=θ`. The analogous full-zeta consequence holds simultaneously for the elementary-2 conductor ball `X^(1/5)` when H is additionally abelian over Q, and separately for each H/Q abelian in the general `X^(1/5)`, `X`, and `X³` balls, with the respective uniform bounds but H-dependent exceptional sets.

**Independent review.** Families checked the fibre-product character extension and intersection cases, conductor-ball counts, small common height, distinct-compositum fibers, and both k=3 scalar examples under the named source and detector inputs. The extra Dirichlet candidate interpretation is an additional stated assumption.
