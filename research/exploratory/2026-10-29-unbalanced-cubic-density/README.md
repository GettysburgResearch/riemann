# Conditional density in unbalanced cubic conductor boxes

**Status:** Source-conditional fixed-box refinement of the [short-detector density argument](../2026-10-29-short-cubic-conductor-detector/README.md). It imports the cited cubic rectangular sieve, its common-profile/height uniformity, and the fixed-field buffered detector with the short-cutoff and lowered-floor replays. No individual zero-free region or priority claim is made; these analytic inputs have not been independently proved here.

Fix K containing μ₃, the source's fixed good ideal set S and cubic family, and a fixed unitary Hecke character ν with finite conductor supported on S. Let `0≤a≤1/2`, `1/2<σ<1`, and ε>0 be fixed. Put

    δ = 2σ−1,
    t_a = min{ 1, 2(2−a)/(3(2−δ)), 2(1+a)/(4−3δ) },
    R_a = 1−δ t_a/2.                                                 (1)

Under the inputs above, there is τ>0 such that, for fixed-comparability boxes `NA≍X^a`, `NB≍X^(1−a)`, with A,B good squarefree and coprime,

    Σ_(A,B in box) N(σ,X^τ; νχ_(A B²)) ≪ X^(R_a+ε).                 (2)

Primitive zeros are counted with multiplicity. Fixed box constants and the conductor of ν affect only implied constants. At good primes dividing AB, ν is unramified and χ_(AB²) is ramified; the bounded bad part of the source conductor gives `N cond(νχ_(AB²))≍N(AB)≍X`. Thus the scale X is comparable to conductor throughout these boxes. The one possible pole-bearing presentation is treated separately, as in the detector note.

For 0<a≤1/2, choose fixed subboxes of the stated scales and take both A and B to be prime ideals, distinct when needed. The prime ideal theorem gives ≫X/(log X)² such pairs. At a=0, in a nonempty box fix one admissible squarefree good ideal A₀ and take prime B coprime to A₀, obtaining ≫X/log X labels; a box containing the unit ideal permits A₀=(1). Tame local ramification distinguishes these primitive characters, so each such subfamily has ≫X/(log X)² distinct members. Since R_a<1, (2) yields density-one zero-free rectangles in the box. This is an asymptotic statement about each fixed a and chosen box, not a uniform zero-free rectangle for an individual character.

At σ=4/5, the full-family short-detector exponent is 11/14. Formula (1) gives 8/11 for a=0 and 3/4 for a=1/4; the best balance at this σ is a=1/32, with exponent 23/32. In the special subfamily A=(1), the squarefree-index result of Blomer–Goldmakher–Louvel also gives 8/11 at this σ: χ_(B²) is the conjugate of χ_B, and the height window is symmetric. For a general bounded A, comparing with that source requires a separate fixed-twist transfer. For every fixed 0≤a<1/2 and 0<δ<1, (1) is strictly smaller than the full-family exponent: both unbalanced candidates for t_a exceed the balanced value `1/(2−δ)`, as does 1. This comparison does not assert novelty over all prior box-specific results.

## Moment and detector inputs

For the fixed A,B box, the cubic Proposition 8.1 supplies the normalized squarefree-column inverse moment

    Σ |M_r|² ≪ X^(E_a(r)+ε),
    E_a(r)=max{1, (1+a)/3+r, (2−a)/3+2r/3}.                        (3)

Here `min(NA,NB)≍X^a` and `max(NA,NB)≍X^(1−a)`; endpoint factors and O(log X) dyads are absorbed in ε. Original masks and fixed reciprocity phases are retained, and the source bounds arbitrary common squarefree-column coefficients. The same squarefree decomposition of the ordinary block as in the linked note gives

    Σ |S_m|² ≪ X^(1+O(η)+ε),     m≤1/2+O(η),                        (4)

because for m≤1/2 both nontrivial terms of E_a(m) are at most 1. For a column j=qv², q squarefree, drop |χ_g(v²)|≤1 outside the q-sum, use the coefficient mass `≪(Nv)^−2`, and sum row L² norms over v. Fixed-order Sobolev control of rowwise real parts and heights is an additional assumption, with all polynomial height factors absorbed by selecting τ sufficiently small.

Take the detector parameter `t=t_a`. The fixed-family buffered detector supplies, after binning and arbitrary small fixed losses η,e, simultaneous inverse and plain witnesses with

    r≤t+O(η),  m≤1/2+O(η),  r+m≥t−O(η),
    |M_r|²≥X^((2b−1)r−η),  |S_m|²≥X^((2b−1)m−η),

where the bin endpoint b is at least σ−e. Here the same row character and common separated frequency are used, and the common-coefficient Sobolev step is needed before applying (3)–(4). Choose e and η first, then the fixed profile/height orders, and finally τ. Dyads, bins, the small m-overflow in (4), and the standard individual zero-count factor are absorbed in the final ε. Thus (2) follows from the scalar maximization below.

## Exact scalar minimax

Set `c=(1+a)/3`, `d=(2−a)/3` and define

    I(r)=max{1−δr, c+(1−δ)r, d+(2/3−δ)r},
    P(m)=1−δm.

For `1/2≤t≤1`, feasibility is `r∈[t−1/2,t]` and `m≥t−r`. The worst m is t−r, so the count exponent is `F(t)=sup_r min{I(r),1−δ(t−r)}`. Since min distributes over a finite max, optimize the three inverse faces separately.

The first face peaks at r=t/2 with value `A(t)=1−δt/2`. The second face is nondecreasing in r, so its maximum is at most `c+(1−δ)t`; it is ≤A(t) whenever `t≤2(2−a)/[3(2−δ)]`. If δ≤2/3, the third face is also nondecreasing and is at most `d+(2/3−δ)t`; it is ≤A(t) whenever `t≤2(1+a)/(4−3δ)`. If δ≥2/3, its min with P is always ≤A(t): for r≤t/2 use P≤A(t), and for r≥t/2 use

    d+(2/3−δ)r ≤ d+(2/3−δ)t/2 ≤ 1−δt/2,

because `d+t/3≤1` for a≥0 and t≤1. In this regime the third candidate in (1) is at least 1. Consequently F(t_a)≤A(t_a)=R_a.

Conversely, if t≤t_a, the feasible point r=m=t/2 gives F(t)≥A(t)≥R_a. If t≥t_a and t_a<1, the active candidate in (1) is one of the nondecreasing second or third faces, and the feasible point r=t,m=0 gives F(t)≥R_a. If t_a=1 the first case already covers the interval. Hence the minimax on [1/2,1] is exactly R_a. The exhibited r,m values are feasible witnesses of the scalar relaxation; they are not claims about actual rows. □

## General fixed order: restricted conjugate-exponent boxes

For fixed n≥3 and K containing μ_n, consider only `g=A B^(n−1)` with A,B good squarefree and coprime, in the same box `NA≍X^a`, `NB≍X^(1−a)` for fixed 0≤a≤1/2. Under the detector, Sobolev and height assumptions above, additionally assume the [general-order rectangular-sieve replay](../2026-10-29-conjugate-conductor-sieve/README.md). Then (2) holds for these labels with R_a replaced by the following `R_(n,a)`.

Set

    c = 1/n + a(1−2/n),    d = 1−c,    δ=2σ−1,
    t_(n,a) = min{1, 2d/(2−δ), 2c/(4/n−δ)}   if δ<2/n,
    t_(n,a) = min{1, 2d/(2−δ)}                 if δ≥2/n,
    R_(n,a) = 1−δ t_(n,a)/2.                                       (5)

The reciprocal and ordinary moments use the source-conditional exponent

    E_(n,a)(r) = max{1, c+r, d+2r/n}.                                (6)

It comes directly from the two off-diagonal terms of the general-n rectangular bound with smaller row factor X^a and larger row factor X^(1−a). A plain block up to length X^(1/2+O(η)) again has moment X^(1+O(η)+ε), because `c+1/2≤1` and `d+1/n≤1`; the unique decomposition j=qv² and Minkowski argument are independent of n. The tame primitive conductor of χ_g has each good p|AB exactly once, with bounded fixed bad part, so it is comparable to X; the prime-pair argument above supplies ≫X/(log X)² distinct primitive characters in a nonempty fixed box, with the a=0 qualification already stated. This yields density-one rectangles for each such family.

The exact optimization repeats the cubic proof. The first face gives `1−δt/2`; the second nondecreasing face is ≤ it when `t≤2d/(2−δ)`. If δ<2/n, the third nondecreasing face is ≤ it when `t≤2c/(4/n−δ)`. If δ≥2/n, the third face is nonincreasing and its min with the plain bound is always ≤`1−δt/2`: for r≥t/2, use `d+(2/n−δ)r≤d+(2/n−δ)t/2≤1−δt/2` because `d+t/n≤1`. The lower-bound witnesses from the cubic optimization prove exactness. Each formula in (5) is at least 1/2, and the selected t is at most 1, within the short-detector range. For every a<1/2 it is strictly larger than the balanced value `1/(2−δ)`, hence improves the corresponding full restricted-family exponent.

For example, n=4, a=0 and σ=4/5 give t=1 and exponent 7/10. This remains an estimate for the ±1-exponent label subfamily, not all n-th-power-free labels, and no claim is made that it improves every prior squarefree-index theorem.

## Further improvement from t>1

The preceding formulas give the exact minimax only on `1/2≤t≤1`. The detector's original stated interval also permits `1≤t≤3/2`, and on very unbalanced boxes this can improve the exponent. In the general-n notation of (5), when `δ>2c` put

    t_long = max{ d+δ/2, (1−2c−1/n+δ/2)/(1−2/n) },
    R_long = c+(1−δ)t_long.                                          (7)

Then `1<t_long<3/2`, and the same conditional density statement holds with exponent R_long. This is the exact minimax on the full interval `[1/2,3/2]`; when `δ≤2c`, the short-range R_(n,a) in (5) is already the full-interval optimum. For instance, in the cubic family with a=0 and σ=9/10, one has δ=4/5, `t_long=6/5` and `R_long=43/75`, compared with 3/5 from restricting t≤1. For n=4, a=0 and σ=4/5, `t_long=11/10` and `R_long=69/100`, compared with 7/10 at t=1.

To prove (7), note that `δ>2c≥2/n`. For t≥1 the feasible interval is `t−1/2≤r≤t`, and minimizing m for a worst-case upper bound gives m=t−r. The first inverse face decreases in r and is ≤P throughout this interval; its maximum is therefore

    A_long(t)=1−δ(t−1/2).

The second inverse face and P are nondecreasing, so its maximum is `min{1,c+(1−δ)t}`. The third inverse face decreases; at r=t−1/2 it lies below P because `d+1/n≤1`, and hence its maximum is

    C_long(t)=d+(2/n−δ)(t−1/2).

Both A_long and C_long decrease with t, while the second-face maximum increases. Their crossings with its uncapped affine part occur at the two values inside the max in (7). Both crossings are at most 3/2: the first follows from d≤1−1/n and δ<1, and the second from c≥1/n and δ<1. At least the first exceeds 1 when δ>2c. The uncapped second face is <1 at the larger crossing, since there it equals one of the other two faces. Therefore their larger crossing is the exact long-range optimum and gives (7).

When δ≤2c, the second face at t=1 is already at least the first, and it increases thereafter; the short-range optimizer has exponent at most its t=1 value. Thus t>1 cannot improve it. All equalities are statements about the scalar relaxation and the cited moment majorants; no claim is made that the endpoint witness pairs are actually realized by zeros. □
