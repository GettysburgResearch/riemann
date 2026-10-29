# A fourth-moment detector in unbalanced cyclic boxes

**Status.** A source-qualified conditional density calculation. It assumes the [general-order conjugate-box rectangular sieve](../2026-10-29-conjugate-conductor-sieve/README.md), the fixed-field buffered detector with simultaneous witnesses, and the source's common-profile, Sobolev and height controls. Those analytical replays are not independently established here. It is a density statement in explicitly chosen families, not an individual zero-free region or an exhaustive priority claim.

Fix n≥4, a number field K containing μ_n, the source's good set S, and a fixed unitary finite-ray twist. At `σ=4/5` write `δ=2σ−1=3/5`. Consider `g=A B^(n−1)` with A,B good coprime squarefree ideals in boxes `NA≈X^a`, `NB≈X^(1−a)`, `0≤a≤1/2`. Define

    c=1/n+a(1−2/n),    d=1−c,
    E(x)=max{1,c+x,d+2x/n}.                                  (1)

The cited rectangular sieve bounds the squared norm of any normalized squarefree-column polynomial of length `X^x` by `X^(E(x)+ε)`. It applies equally to the inverse witness. The ordinary witness has the **fourth** moment

    Σ_g |S_m(g)|⁴ ≪ X^(E(2m)+ε),                             (2)

for `m≤1/2+O(η)` and the common profiles/heights allowed by the detector. Indeed, square the ordinary polynomial, whose normalized length is `X^(2m)`. Its convolution coefficients are divisor-bounded. Decompose each column ideal as `q=q₁ v²` with q₁ squarefree. For each fixed v the factor `χ_g(v²)` is a row-dependent contraction outside the q₁-sum, retaining all original zero masks. The normalized squared ℓ² mass of the q₁-coefficient vector is `≪X^ε/(Nv)²`. Applying the rectangular sieve at the shortened q₁ scale, using monotonicity of E, and then Minkowski over v costs `Σ_(Nv≪X^m)1/Nv≪X^ε`. The original coefficients are common to rows; rowwise frequencies require the stated Sobolev/height replay before this argument.

Use detector cutoff t=1. Its simultaneous inverse and ordinary witnesses satisfy, up to `O(η)` losses for an arbitrarily small fixed η chosen before X grows,

    0≤r≤1,   0≤m≤1/2,   r+m≥1,
    |M_r(g)|²≥X^(δr−O(η)),   |S_m(g)|²≥X^(δm−O(η)).       (3)

The full interval for m is essential; there is no asserted equality `r+m=1`. Markov using the second moment of M or the fourth moment (2), whichever is better, gives a count exponent at most

    min{E(r)−δr, E(2m)−2δm}.                                  (4)

For all feasible r,m this is at most

    R_n(c)=max{3/5,c+2/5,3/5−c+4/(3n)}.                     (5)

If `r≥2/3`, use the inverse bound. On `[2/3,1]` the three faces of `E(r)−δr` are bounded by the three terms in (5): the first and third decrease, since n≥4, and the second increases. If `r≤2/3`, use the ordinary fourth moment; then `2m∈[2/3,1]`, and the same three-face calculation applies uniformly throughout that entire interval. Small detector overflows are absorbed by choosing the detector loss before the final ε and height exponent.

The scalar relaxation (5) is exact for t=1: the feasible point `(r,m)=(1,1/2)` yields `c+2/5`, since c≥1/n, and `(2/3,1/3)` yields at least the remaining two terms. These are algebraic witnesses for the relaxation, not assertions that actual zeros realize them.

Minimizing (5) over admissible c gives

    n=4,5,6: c=1/10+2/(3n), a=(3n−10)/[30(n−2)],
              R=1/2+2/(3n);
    n≥7:     c=4/(3n), a=1/[3(n−2)], R=3/5.                 (6)

For each fixed n, the standard detector-to-zero-count and finite height-bin argument therefore gives, subject to the stated source inputs, `O(X^(R+ε))` zeros with `Re s≥4/5` and `|Im s|≤X^τ` for some τ>0 in these boxes. The factor n and all ray-sector/profile constants are fixed before τ. Tame local conductors on the good primes A,B are of exponent one, so the primitive conductor is ≍X, with bounded bad factors; prime ideal pairs give `≫X/(log X)²` distinct characters in fixed boxes. This shows a density-one rectangle in those families, not a uniform individual region.

For n=4,5,6,7,8,9 the new exponents and the prior conditional optimized-box exponents are respectively

    n       a         new R       prior R      improvement
    4      1/30        2/3         17/25          1/75
    5      1/18       19/30        23/35          1/42
    6      1/15       11/18        16/25         13/450
    7      1/15        3/5         47/75          2/75
    8      1/18        3/5         77/125         2/125
    9      1/21        3/5        167/275         2/275.

These compare different fixed boxes, as shown by their a values. At n=10 the new result ties the prior conditional `3/5`; for n≥11 that prior result is smaller, so there is no improvement from this fourth-moment t=1 argument. The individual-order-n statement for composite n does not by itself bound every power χ_g^j needed in a relative Dedekind-zeta product.

The above table concerns t=1 only. For n≥7 a better choice with t>1 is available, as proved below.

For prime p=5 or 7, each nontrivial j is invertible modulo p, and raising the source character family to j is the same FHL construction with a changed embedding, preserving original masks and the ±1 conjugate-pair box. Thus the same conditional bound applies to each of the p−1 factors of `ζ_L/ζ_K` for the cyclic degree-p extension L/K cut out by χ_g. A finite union gives a relative-zeta exceptional count `O(X^(R+ε))`, with `R=19/30` for p=5 and `R=31/52` for p=7 using the long-cutoff optimization below. Fixed character-to-field fibers have size ≤p−1; the conductor–discriminant formula gives `|D_L|≈X^(p−1)`. Accordingly, under the same source/height qualifications, the corresponding discriminant exponents are `19/120` for p=5 and `31/312` for p=7. For a cumulative bound over `|D_L|≤Y` with one height `Y^τ′`, split conductor X dyadically: choose `0<u<R/(p−1)`, count all fields trivially when `X≤Y^u`, and choose `τ′<uτ` on the remaining dyads. The fixed box constants are absorbed in the height margin, while prime ideals in a box near `X≈Y^(1/(p−1))` give at least `≫Y^(1/(p−1))/(log Y)²` distinct fields. Thus these relative-zeta rectangles have density one in the specified discriminant-ordered subfamilies under the stated assumptions. The fixed base ζ_K factor is not covered.


## Exact optimization over the full detector range for n≥7

No moments beyond the ordinary fourth are needed. For each fixed n≥7 choose

    c=5/(3n+5),    a=(2n−5)/[(3n+5)(n−2)],
    t=15n/[4(3n+5)],   L=2t/3=5n/[2(3n+5)],
    R=(3n+10)/(6n+10).                                      (7)

Here `1<t<5/4` and `1/n≤c≤1/2`, so the source detector and box constraints hold. Put `f(x)=E(x)−(3/5)x`. Its first and third faces decrease and its second increases. The choices in (7) give

    1−(3/5)L = 1−c+(2/n−3/5)L = c+(2/5)t = R.             (8)

Thus `f(x)≤R` for every `L≤x≤t`. If a feasible detector witness has r≥L, its inverse second moment gives the desired exponent. If r<L, then the *actual* m obeys `m≥t−r>t−L=L/2` and `m≤1/2`, so `2m∈[L,1]⊂[L,t]` and the ordinary fourth moment gives the same bound. This handles every permitted m, including cases with `r+m>t`, with small fixed detector losses absorbed into ε.

The value R is the exact minimax of this scalar relaxation over the full allowed `1/2≤t≤3/2` and all `1/n≤c≤1/2`. For any t, the feasible point `(r,m)=(t,0)` forces at least `min(1,c+(2/5)t)`. The feasible point `(r,m)=(2t/3,t/3)` makes both moment arguments equal `2t/3`, forcing at least

    max{1−(2/5)t, 1−c+[4/(3n)−2/5]t}.

If the relaxed bound is below 1, the latter face and `c+(2/5)t` together imply `R≥1/2+2t/(3n)`. Minimizing the maximum of this and `1−(2/5)t` gives exactly (7). These are lower witnesses for the scalar relaxation, not existence claims about detected zeros.

For example, n=7 gives `a=9/130`, `t=105/104`, `R=31/52`; n=8 gives `a=11/174`, `t=30/29`, `R=17/29`; n=9 gives `a=13/224`, `t=135/128`, `R=37/64`; and n=11 gives `a=17/342`, `t=165/152`, `R=43/76`. The prior optimized-box exponent minus (7) is

    3n(n+10)/[50(n+2)(3n+5)]                   for 7≤n≤10,
    (3n³+150n−500)/[50n(n−2)(3n+5)]           for n≥11,

which is strictly positive throughout those ranges. The comparison uses different explicit a-boxes. The n=4,5,6 results above remain the t=1 bounds; no assertion about their global optimum is needed for the stated theorem.

## A continuum of fourth-moment boxes

Let n≥5 and `σ∈(1/2+2/n,1)`, and put `δ=2σ−1`. Under the same fixed-order sieve, detector and common-profile inputs, choose

    L = 2n/[n(3−δ)+4],       t = 3L/2,
    c = 4/[n(3−δ)+4],
    a = [n(1+δ)−4]/[(n−2)(n(3−δ)+4)],
    R = 1−δL = [3n(1−σ)+2]/[n(2−σ)+2].                    (9)

The assumption δ>4/n implies `1<t<3/2` and `δ>2/n`; the displayed a lies in `[0,1/2]`. The three faces of `f(x)=E(x)−δx` are bounded by R on `[L,t]`: the first and third decrease and equal R at L, while the second increases and equals R at t. For any simultaneous witnesses, if r≥L the inverse second moment applies, and if r<L then `2m≥2(t−r)>L` and `2m≤1<t`, so the ordinary fourth moment applies. This gives the same conductor-X exceptional-count bound `O(X^(R+ε))` in the indicated n-order box, subject to the source/height hypotheses.

For example, n=7 and σ=9/10 give `a=43/485`, `t=105/97`, `R=41/97`. For n=5 and σ=19/20 they give `a=11/87`, `t=30/29`, `R=11/29`. These are valid source-qualified bounds, but this particular balanced fourth-moment choice is **not always better** than the prior long-cutoff optimization: at n=7, σ=9/10 the previous a=0 branch gives `R=363/875<41/97`. The exact general-σ scalar minimax, including the better high-σ a=0 branch, is proved next. For prime n the powered-family and relative-zeta consequences apply as before, with this R and the fixed base factor excluded.

### A better high-σ branch and exact scalar minimax

The continuum (9) is not always the best fourth-moment choice. Put `δ_c=3/5+4/(5n)`. When `δ≥δ_c` (still δ<1), take instead

    c=1/n,  a=0,  t=3(n−2)/[n(3−δ)−4],  L=2t/3,
    R=1/n+(1−δ)t.                                           (10)

This uses the squarefree-index subfamily `A=(1)`, `NB≈X`. In the present δ>4/n regime one has `1<t<3/2`, `L>1/2`, and δ>2/n. Hence the first and third faces of f decrease, the second increases, and

    f₂(L)=f₁(t)=R,   f₀(L)≤f₂(L).

The same inverse/ordinary-fourth split at L proves the bound for every feasible witness pair. At n=7, σ=9/10 this gives `t=25/19`, `R=54/133`, improving the prior a=0 exponent `363/875`; at n=5, σ=19/20 it gives `t=18/13`, `R=22/65`, improving `41/120`.

In fact the balanced branch (9) for `4/n<δ≤δ_c` and the a=0 branch (10) for `δ_c≤δ<1` are the exact scalar minimax over the full detector range, among these two moments and conjugate boxes. For general δ the feasible witnesses `(t,0)` and `(2t/3,t/3)` imply, whenever the relaxed exponent is <1,

    R ≥ max{ 1−(2δ/3)t,
             1/2+[1/2−5δ/6+2/(3n)]t,
             1/n+(1−δ)t }.                                  (11)

If `δ≤δ_c`, the middle line has nonnegative slope; intersecting it with the first gives the t and R in (9). If `δ≥δ_c`, the middle line has nonpositive slope while the last increases; their intersection gives (10). The upper bounds above attain these lower envelopes. Feasible witness points only certify the minimax of the scalar relaxation and need not occur for actual zeros. The endpoint δ=δ_c has a flat family of minimizing t and either branch gives R=1/2.

For `δ≥δ_c`, the older optimized long-detector calculation is minimized at `a=0` and its active cutoff is `t_old=(1−3/n+δ/2)/(1−2/n)`. Its exponent exceeds (10) by the positive exact amount

    n(1−δ)²(nδ−2) / [2(n−2)(n(3−δ)−4)].                       (12)

All comparisons retain the prior and new source replay assumptions. For composite n, this proves the statement for the order-n factor only unless the lower-order powered factors are separately controlled.

**Independent review.** High_match checked the high-σ branch, global scalar lower envelope, threshold `δ_c`, source-admissible cutoff and exact comparator (12). The zero-density result remains conditional on the named detector/sieve inputs.
