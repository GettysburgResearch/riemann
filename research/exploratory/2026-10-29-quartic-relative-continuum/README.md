# Quartic relative-zeta families across a real-part interval

**Status.** A source-qualified family-density consequence of the [fourth-witness box calculation](../2026-10-29-fourth-moment-cyclic-box/README.md), the fixed-field buffered-detector replay, the fixed-field quadratic Hecke large sieve and detector, and classical class field theory. The general-order rectangular sieve, detector/profile/height transfers and recent source theorems are not independently established here. This is not an individual zero-free region or a complete priority comparison.

Fix K=Q(i), the good set S, and the source quartic FHL family. Let `3/4<σ<1` and `δ=2σ−1`. Define

    a(δ) = (2δ−1)/6,                         1/2<δ≤4/5,
           0,                                4/5≤δ<1;
    R₄(δ) = 7/6−5δ/6,                        1/2<δ≤4/5,
            (8−7δ)/[4(2−δ)],                 4/5≤δ<1.       (1)

At δ=4/5 the two displayed exponents both equal 1/2; the two different boxes are both admissible. For the first branch take all good coprime squarefree ideals A,B in fixed positive-width boxes `NA≈X^a`, `NB≈X^(1−a)` and let χ be the primitive character induced by `χ_(AB³)`. For the second branch take A=1 and B good squarefree with `NB≈X`, and let χ be induced by `χ_(B³)`. In either case χ has order four and cuts out a cyclic quartic extension L/K.

Subject to the listed inputs, for each ε>0 there is τ>0 such that at most

    O(X^(R₄(δ)+ε))                                             (2)

of these distinct fields have a zero of `ζ_L/ζ_K` in `Re s≥σ`, `|Im s|≤X^τ`. The [squarefree-box count](../2026-10-29-squarefree-box-count/README.md) gives `≫X` fields in either branch. Their absolute discriminants satisfy `|D_L|≈X³`. For one top-scale box `X≈Y^(1/3)` with suitably small fixed constants and a sufficiently small τ′, (2) becomes

    O(Y^(R₄(δ)/3+ε)) exceptional fields,                        (3)

against `≫Y^(1/3)` fields, in the analogous Y-power-height rectangle. Constants and the permitted height may depend on fixed σ and ε. A cumulative union of smaller boxes requires the standard small-scale/height split; it is not asserted by the top-box estimate alone. These are relative-quotient statements, and zeros of the fixed base ζ_K remain in ζ_L.

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

The relative quotient has the three entire factors `L(χ)L(χ²)L(χ³)`, with χ³=barχ and identical symmetric zero counts. In the first branch the quadratic core χ² agrees with `χ_(AB)²` on every good ideal including zero masks; in the second it agrees with `χ_B²`. Each has good conductor AB or B respectively. In the two-variable box a given core has at most `τ_K(AB)≪X^ε` factorizations into A,B; in the one-variable box its good conductor determines B. This subpower multiplicity is absorbed into the final loss.

The fixed-field quadratic sieve and the source-qualified detector give the core exponent

    Q(δ)=1−δ/2−δ²/2.                                            (7)

It is strictly less than R₄ throughout the interval:

    R₄−Q = (1−2δ+3δ²)/6                       (1/2<δ≤4/5),
           δ(1+2δ−2δ²)/[4(2−δ)]               (4/5≤δ<1).    (8)

Choose the common height power below both the quartic and quadratic powers. Each coprime squarefree-pair label gives a distinct primitive order-four character by its good local exponents, while each cyclic quartic field has two generators; hence the field fiber is at most two. The character and its square have conductor norms ≍X, so the conductor–discriminant formula gives the X³ scaling used above. A union bound over the three nontrivial factors proves (2) under the stated inputs.

## Direct comparisons and limitations

In the balanced branch, conjugation replaces AB³ by A³B, whose natural-label norm is `X^[2(1+δ)/3]`. Applying de Faveri Corollary 1.5 to that label gives the X-exponent `[2(1+δ)/3]D₄(σ)`, before its explicit height loss. This direct comparator is strictly larger than R₄ on `1/2<δ<4/5`. In the middle source interval `1/2≤δ≤3/4`, the difference is

    (2δ−1)(40δ²−43δ+9) / [6(8δ²−12δ+3)] > 0;              (9)

in `3/4≤δ≤4/5`, it is `(2δ−1)(11δ−9)/[6(2δ−3)]>0`. These are comparisons with one named natural-index source, not an exhaustive novelty claim.

For the high branch a=0, de Faveri's source **is stronger**: the squarefree label B gives `D₄=3(1−δ)/(3−2δ)`, and

    R₄−D₄ = δ(2δ−1)/[4(2−δ)(3−2δ)] > 0.                       (10)

The source's D₄ is also above the quadratic-core Q in (7), so under the same quadratic input it gives the stronger relative-quotient exponent D₄. The high branch is retained as a check of the fourth-witness mechanism, not as a density record.

Hu's [Theorem 1.2](https://hexagonmath.org/2610.00216v1) claims an all-height zero-free half-plane `Re s>7/8` for every unitary Hecke character of every number field. If that preprint is accepted, it supersedes positive exception bounds whenever σ>7/8; its open half-plane does not by itself exclude a zero exactly at σ=7/8. Hu's analytic transfer is not independently verified here. Thus the source-qualified nontrivial comparison (9) should not be interpreted as a stronger result than every claimed all-height zero-free theorem.

**Independent review.** Other_families checked both scalar branches and their full detector ranges, the quadratic-core comparison, the conjugate natural-index comparison and its signs, field fibers and discriminant/height conversion. The cited analytic inputs and their replays remain conditional.

## Conditional full Dedekind-zeta consequence

There is a separate route from the relative quotient to **full** ζ_L for this particular base. The isolated retune packet reports a locally compiled and freshly replayed `Candidate.bound` for every Dirichlet character with θ=`4369347/5000000=0.8738694`, subject to tracker admission and the semantic/source qualification in [its packet](../2026-10-29-return-retune-8738694/README.md). Its printed signature has the same quantifiers and pole exception as the [reviewed conventional Dirichlet bridge](../2026-10-29-dirichlet-conventional-bridge/README.md), which audited the earlier candidate with the same interface; the latter is not an independent audit of the retune's imported analytic chain.

Assume that conventional interpretation and admission of the retuned statement. Since

    ζ_Q(i)(s)=ζ(s)L(s,χ₋₄),                                   (11)

ζ_K has no zero at any height in `Re s>θ`, with its usual simple pole at 1. Thus, for every fixed σ>θ, each field whose relative quotient is zero-free in (2)'s rectangle has **full ζ_L zero-free in that same rectangle**, with the pole at s=1 excluded. This uses only the Dirichlet candidate and (11), not an E-Hecke corollary. It remains conditional on (2)'s independent source replays as well as the formal candidate's stated qualifications.

For a concrete point below Hu's claimed open 7/8 boundary, take

    σ=437/500,  δ=187/250,  a=31/375,
    R₄=163/300,  Q=43281/125000.                              (12)

The full Dedekind-zeta exception count is then `O(X^(163/300+ε))`, or `O(Y^(163/900+ε))` in the top discriminant box, versus `≫Y^(1/3)` fields. The same-box de Faveri natural-index comparator for the order-four factor is `179303/305700`, before its explicit height loss. The broader fixed-height Hecke-family bound of [Khale et al.](https://arxiv.org/abs/2008.09677v3), under its stated hypotheses, gives the tighter named comparator `252/437`, still larger than `163/300`; sufficiently small power height preserves the strict gaps. The target σ=437/500 is **below** 7/8, so Hu's claimed `Re s>7/8` theorem does not itself give this rectangle; it does cover the narrower open strip if accepted. The relative-quotient density and the base Dirichlet nonvanishing are distinct inputs.

**Independent review.** Other_families checked the retune signature and conventional-base implication, all fractions in (12), the pole exception, height conversion, and the strict comparison with the named sources. The retune's tracker and imported-chain qualifications remain unchanged.
