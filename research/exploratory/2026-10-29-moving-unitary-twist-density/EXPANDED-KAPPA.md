# Larger common-twist conductors by retaining the endpoint face

**Status.** This is a proposed extension of [the common moving-twist theorem](README.md), with the same fixed-field Hecke/FHL/Θₙ inputs, original masks and compact archimedean parameter range. Its proof is the detector-face argument below; it is not an individual all-height zero-free result. A fixed κ may be arbitrarily large, but the estimate is useful only when its stated exponent beats the trivial family count or the intended comparator. The source inputs and this extension require independent review.

Fix one common ν_X with primitive finite conductor `Nf_ν≤X^κ` and archimedean parameters in a fixed compact set. The moving detector proof gives, uniformly in ν_X and up to arbitrarily small fixed losses,

    r≤t,   m≤(1+κ)/2,   r+m≥t.                               (1)

Let f be the maximum of the four threshold-divided Θₙ faces from the direct note. Since f is a maximum of affine functions, it is convex.

## Middle interval

For n≥4 and `2/n<δ<1−1/n`, retain

    t=3(n−3)/[n(3−δ)−7],   L=2t/3,
    R=2/n+(1−1/n−δ)t.                                        (2)

The inverse witness gives ≤R whenever r≥L. Otherwise the ordinary fourth witness satisfies `L≤2m≤1+κ`. By convexity, its count exponent is bounded by

    R_mid(κ)=max{R, f(1+κ)}.                                 (3)

Indeed f(L)=R; there is no need to require 1+κ<t. The endpoint has the explicit form

    f(1+κ)=2/n+(1−1/n−δ)(1+κ)   for 0≤κ≤1,
             (1−δ)(1+κ)          for κ≥1.                    (4)

For κ below the old strict cap t−1, (3) equals R. At or above the cap it retains the appropriate Θₙ endpoint rather than assuming the ordinary length is at most t.

## High interval

For n≥3 and `1−1/n<δ<1`, put h=1−δ and retain

    t=10/(4+nh),   L=4t/5,   R=ht.                           (5)

If r≥L, the inverse witness is bounded by R. Otherwise `L≤4m≤2(1+κ)`, and the ordinary eighth moment gives, again by convexity,

    R_high(κ)=max{R, 2h(1+κ)}.                               (6)

Here `2(1+κ)≥2`, and the increasing f_D face dominates all four faces for x≥2. The old strict cap `(1−nh)/(4+nh)=t/2−1` is exactly where the second term crosses R. Fixed profile orders, the bounded dyadic range (depending on the fixed κ), Γ-shift order and fixed losses are chosen before the global height power τ. The possible pure-norm inducing presentation is treated as in the moving theorem.

## Simultaneous finite-order twist example

At n=3, `σ=θ=4369347/5000000` and `κ=1/10`, we have `h=630653/2500000`, so the second face in (6) dominates and gives

    R_high(1/10)=6937183/12500000≈0.55497464.                 (7)

There are `O_K(X^(2κ))` finite-order Hecke characters of conductor norm ≤X^κ, so [the uniform union bound](../2026-10-29-simultaneous-finite-twists/README.md) would give at most

    X^[9437183/12500000+ε] ≈ X^(.75497464+ε)                 (8)

bad labels when requiring every such twist to have no zero in `Re(s)≥θ, |Im(s)|≤X^τ`. Restricting to quadratic twists uses only `O_K(X^κ)` characters and gives exponent `8187183/12500000≈.65497464`. Both are density-one conclusions for the n-free label family and use one uniform τ; they are not claims about a single fixed infinite family or all-height nonvanishing.

For finite-order twists in the fixed Galois-field scope of Khale et al., the product conductor is `≪X^(1+κ)`. Their broad-family fixed-height exponent at θ is `(1+κ)·2522612/4369347≈.635`, larger than (7), before choosing sufficiently small height powers. This named-source comparison does not automatically apply to arbitrary angular or norm-type twists; the recent P52 cubic bound has a different fixed-twist/field scope.

## Optimizing the ordinary moment order

In the high interval, any fixed integer k≥2 gives another explicit option, provided `k+5nh≥4` so that the following fixed detector cutoff satisfies t_k≤5/2:

    t_k=2(k+1)/(k+nh),   L_k=k t_k/(k+1),
    R_k=2h(k+1)/(k+nh),
    E_k(κ)=h·max{t_k, k(1+κ)/2}.                             (9)

Here `1<L_k<2<t_k≤5/2`, and `f₃(L_k)=f_D(t_k)=R_k`. If r≥L_k use the inverse; otherwise `km≥L_k` and `km≤k(1+κ)/2`, so the generic ordinary 2k-th moment and convexity give E_k. If the upper endpoint is below L_k, the ordinary branch is empty. If it lies between L_k and t_k, the face maximum is at most R_k; if it lies beyond t_k, the increasing f_D face equals h times that endpoint. This proves the simpler maximum in (9) without an unnecessary loss when the ordinary branch is empty. Expanding S^k uses fixed-order divisor bounds and the same squarefree-column extraction, row contractions and profile derivatives as the eighth-moment proof. Choose k and its finite profile orders before all loss and height choices. This is a family of explicit bounds; optimization over k is only over fixed integers.

For n=3 at θ, k=3 is allowed and gives

    t₃=20000000/9391959,
    R₃=5045224/9391959≈0.53718548.                            (10)

At both κ=1/10 and κ=19/100, the ordinary endpoint is below 2 and has f-value ≤R₃, so E₃=R₃. The all-finite-order simultaneous exception exponents R₃+2κ are respectively

    34618079/46959795≈0.73718548,
    430708421/469597950≈0.91718548.                          (11)

For quadratic twists, replace 2κ by κ, giving respectively `59844199/93919590≈0.63718548` and `682969621/939195900≈0.72718548`. The earlier k=4 bound (7) remains valid; for these two conductor ranges k=3 improves it. The same one uniform τ and source/field qualifications continue to apply.

At n=3 and θ, the k=3 exponent stays equal to R₃ for every `κ≤11824123/28175877≈.419654`. Therefore the all-finite-order union is density-one for every fixed `κ<4346735/18783918≈.231407`. For quadratic twists the endpoint becomes `3h(1+κ)/2` after that crossing, and density-one persists for every fixed `κ<3108041/6891959≈.450966`. These cutoffs concern the fixed-k bound (9) and its union counts; they are not asserted to be globally optimal over all moment choices.

For a simple concrete consequence, κ=1/5 for all finite-order twists, or κ=2/5 for quadratic twists, gives the same exceptional-label exponent `44010038/46959795≈0.93718548` at n=3, σ=θ. In either case every twist in the stated conductor range is handled simultaneously at one small polynomial height, for a density-one subset of the good cube-free label family.

**Independent review.** Families checked the general fixed-k witness split, profile and mask reductions, and sample fractions. High_match independently verified the simplified maximum, including the empty-ordinary-branch case, and all three exact θ conductor thresholds. The uniform detector and printed source estimates remain the stated inputs.
