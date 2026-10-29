# Quartic relative-zeta families across a real-part interval

**Status.** A source-qualified family-density consequence of the [fourth-witness box calculation](../2026-10-29-fourth-moment-cyclic-box/README.md), the fixed-field buffered-detector replay, the fixed-field quadratic Hecke large sieve and detector, and classical class field theory. The general-order rectangular sieve, detector/profile/height transfers and recent source theorems are not independently established here. This is not an individual zero-free region or a complete priority comparison.

Fix K=Q(i), the good set S, and the source quartic FHL family. Let `3/4<σ<1` and `δ=2σ−1`. Define

    a(δ) = (2δ−1)/6,                         1/2<δ≤4/5,
           0,                                4/5≤δ<1;
    R₄(δ) = 7/6−5δ/6,                        1/2<δ≤4/5,
            (8−7δ)/[4(2−δ)],                 4/5≤δ<1.       (1)

At δ=4/5 the two displayed exponents both equal 1/2; the two different boxes are both admissible. For the first branch take good distinct prime ideals A,B in fixed positive-width boxes `NA≈X^a`, `NB≈X^(1−a)` and let χ be the primitive character induced by `χ_(AB³)`. For the second branch take A=1 and B good prime with `NB≈X`, and let χ be induced by `χ_(B³)`. In either case χ has order four and cuts out a cyclic quartic extension L/K.

Subject to the listed inputs, for each ε>0 there is τ>0 such that at most

    O(X^(R₄(δ)+ε))                                             (2)

of these distinct fields have a zero of `ζ_L/ζ_K` in `Re s≥σ`, `|Im s|≤X^τ`. There are `≫X/(log X)²` fields in the first box and `≫X/log X` in the second. Their absolute discriminants satisfy `|D_L|≈X³`. For one top-scale box `X≈Y^(1/3)` with suitably small fixed constants and a sufficiently small τ′, (2) becomes

    O(Y^(R₄(δ)/3+ε)) exceptional fields,                        (3)

against `≫Y^(1/3)/(log Y)²` or `≫Y^(1/3)/log Y` fields respectively, in the analogous Y-power-height rectangle. Constants and the permitted height may depend on fixed σ and ε. A cumulative union of smaller boxes requires the standard small-scale/height split; it is not asserted by the top-box estimate alone. These are relative-quotient statements, and zeros of the fixed base ζ_K remain in ζ_L.

## Fourth-witness bounds

For a general quartic conjugate box write

    c=(1+2a)/4,    E(x)=max{1,c+x,1−c+x/2},
    f(x)=E(x)−δx.                                               (4)

The inverse second moment gives count exponent f(r), and the common-profile ordinary fourth moment gives f(2m). The latter is obtained by squaring the ordinary block, writing q=q₁v², using χ_g(v²) as a row contraction only after fixing v, and applying the squarefree-column sieve to common q₁ coefficients. Divisor-bounded convolution coefficients and Minkowski cost only small powers. The buffered detector supplies simultaneous witnesses with `r≤t+O(η)`, `r+m≥t−O(η)`, `m≤1/2+O(η)`; η and the bin and profile losses are fixed before choosing the height exponent.

For `1/2<δ<4/5`, put

    c=(1+δ)/6,   L=2/3,   t=1.                               (5)

Then `a=(2δ−1)/6`, and all three faces of f are at most `R₄=(7−5δ)/6` on `[L,1]`: the third equals R₄ at L, the second equals R₄ at 1, and the first at L is strictly smaller. If r≥L, then r≤t=1 and the inverse witness applies. If r<L, then `2m≥2(t−r)>L` and `2m≤1`, so the ordinary fourth witness applies. This uses the printed t≥1 range and still requires the source-qualified simultaneous-witness and common-profile transfer. No equality `m=t−r` is assumed.

For `4/5≤δ<1`, use c=1/4, a=0 and

    L=1/(2−δ),   t=3/[2(2−δ)].                                (6)

Now `1<t<3/2` and f is at most `R₄=(8−7δ)/[4(2−δ)]` on `[L,t]`: its third face at L and its second face at t both equal R₄, while the first at L is no larger. If r<L then `2m≥L` and `2m≤1<t`; otherwise use r≥L. This branch lies in the printed t range but still requires the simultaneous-witness and common-profile transfer. Arbitrarily small fixed losses extend both compact-interval checks to the actual detector inequalities.

## Quadratic factor and field fibers

The relative quotient has the three entire factors `L(χ)L(χ²)L(χ³)`, with χ³=barχ and identical symmetric zero counts. In the first branch the quadratic core χ² agrees with `χ_(AB)²` on every good ideal including zero masks; in the second it agrees with `χ_B²`. Each has good conductor AB or B respectively. Distinct prime pairs have distinct quadratic cores because their good conductor support determines the pair and the two norm scales determine its order; in the one-prime box the good conductor B determines the core.

The fixed-field quadratic sieve and the source-qualified detector give the core exponent

    Q(δ)=1−δ/2−δ²/2.                                            (7)

It is strictly less than R₄ throughout the interval:

    R₄−Q = (1−2δ+3δ²)/6                       (1/2<δ≤4/5),
           δ(1+2δ−2δ²)/[4(2−δ)]               (4/5≤δ<1).    (8)

Choose the common height power below both the quartic and quadratic powers. Each prime-pair label gives a distinct primitive order-four character by good local exponents, while each cyclic quartic field has two generators; hence the field fiber is at most two. The character and its square have conductor norms ≍X, so the conductor–discriminant formula gives the X³ scaling used above. A union bound over the three nontrivial factors proves (2) under the stated inputs.

## Direct comparisons and limitations

In the balanced branch, conjugation replaces AB³ by A³B, whose natural-label norm is `X^[2(1+δ)/3]`. Applying de Faveri Corollary 1.5 to that label gives the X-exponent `[2(1+δ)/3]D₄(σ)`, before its explicit height loss. This direct comparator is strictly larger than R₄ on `1/2<δ<4/5`. In the middle source interval `1/2≤δ≤3/4`, the difference is

    (2δ−1)(40δ²−43δ+9) / [6(8δ²−12δ+3)] > 0;              (9)

in `3/4≤δ≤4/5`, it is `(2δ−1)(11δ−9)/[6(2δ−3)]>0`. These are comparisons with one named natural-index source, not an exhaustive novelty claim.

For the high branch a=0, de Faveri's source **is stronger**: the squarefree label B gives `D₄=3(1−δ)/(3−2δ)`, and

    R₄−D₄ = δ(2δ−1)/[4(2−δ)(3−2δ)] > 0.                       (10)

The source's D₄ is also above the quadratic-core Q in (7), so under the same quadratic input it gives the stronger relative-quotient exponent D₄. The high branch is retained as a check of the fourth-witness mechanism, not as a density record.

Hu's [Theorem 1.2](https://hexagonmath.org/2610.00216v1) claims an all-height zero-free half-plane `Re s>7/8` for every unitary Hecke character of every number field. If that preprint is accepted, it supersedes positive exception bounds whenever σ>7/8; its open half-plane does not by itself exclude a zero exactly at σ=7/8. Hu's analytic transfer is not independently verified here. Thus the source-qualified nontrivial comparison (9) should not be interpreted as a stronger result than every claimed all-height zero-free theorem.

**Independent review.** Other_families checked both scalar branches and their full detector ranges, the quadratic-core comparison, the conjugate natural-index comparison and its signs, field fibers and discriminant/height conversion. The cited analytic inputs and their replays remain conditional.
