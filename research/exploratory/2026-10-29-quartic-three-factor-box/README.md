# Three-factor quartic boxes and the limits of the current minimax

**Status.** A source-qualified conditional calculation, extending the [optimized two-factor box](../2026-10-29-optimized-cyclic-quartic/README.md). It uses the general-order conjugate-pair sieve replay, Goldmakher–Louvel's quadratic Hecke sieve, the buffered detector and common-profile/height replay, and classical class field theory. Those inputs have not been independently established here. The resulting family statements are density-one relative-quotient rectangles, not individual zero-free regions; no exhaustive priority claim is made.

Fix K=Q(i) and the source's good S. For fixed exponents `a,b,c≥0` with `a+b+c=1`, let

    g=A B² C³,   NA≈X^a, NB≈X^b, NC≈X^c,                    (1)

where A,B,C are squarefree, good and pairwise coprime. Put `u=min(a,c)`, `v=max(a,c)`, so `u+v=1−b` and `0≤u≤v`. For q squarefree and a common coefficient vector λ_q, the two source sieves give

    Σ_(A,B,C) |Σ_q λ_q χ_q(g)|²
       ≪ X^ε [X + min{ X^(1−b)Q,
             max(X^c₀ Q, X^d₀ Q^(1/2)) }] Σ_q |λ_q|²,        (2)

where

    c₀=1/4+3b/4+u/2,   d₀=3/4+b/4−u/2.                       (3)

All fixed constants, dyads and finite ray classes are absorbed by ε. For the first bound freeze B, replace λ_q by the **common** vector `λ_q χ_q(B)²`, apply the quartic conjugate-pair sieve to A,C, and sum over the ≪X^(b+ε) possible B. For the second freeze A,C, replace λ_q by the common vector `λ_q χ_q(A C³)`, apply the quadratic Hecke sieve in B to `χ_q(B)²`, then sum over A,C. Each multiplier has modulus ≤1 with its original zero masks. Coprimality restrictions on the outer variables can be discarded only after enlarging their nonnegative sum; they are not removed from the characters. Finite reciprocity sectors are fixed before applying either sieve. These arguments give the two bounds independently, so taking their minimum is legitimate.

Writing Q=X^x gives the common inverse-block exponent

    E(x)=max{1, min{1−b+x, max(c₀+x,d₀+x/2)}}.                (4)

The ordinary block has the same exponent as an upper bound by the standard `q=q₁v²` squarefree-kernel decomposition, original row multiplier `χ_g(v²)`, Minkowski and divisor/small-power bounds. For the buffered detector take δ=2σ−1=3/5 and `f(x)=E(x)−δx`. If its source-qualified witnesses have `r+m≥t`, `m≤1/2`, `0≤r≤t` up to arbitrarily small losses, the exponent supplied by these moments is

    F(t)=sup_(max(0,t−1/2)≤r≤t) min{f(r), f(t−r)}.            (5)

The second moment must first be reduced to a common row-independent coefficient vector by the fixed-dimensional Sobolev/profile replay; t, bin, dyadic and polynomial-height losses are chosen before τ. Equation (5) is a **relaxed upper-bound optimization**: it does not claim that its extreme witnesses occur for an actual zero.

## A continuum of three-factor boxes

For every fixed `0≤b≤1/20`, choose

    u=1/30−b/6,  v=29/30−5b/6,  t=31/30−2b/3.

Then `a=u,c=v` is admissible, `1≤t≤31/30`, and the same endpoint argument used below gives the exact relaxed scalar value

    F(t)=17/25+2b/5.                                          (6)

Indeed the three inverse faces are `1−3r/5`, `(4/15+2b/3)+2r/5`, and `(11/15+b/3)−r/10`; the first and third meet (6) at r=t−1/2, and the second meets it at r=t. The ordinary witness has f(1/2)=7/10 and f(0)=1, so the endpoint lower bounds agree with the upper bound. The quadratic-core exponent is `13/25+12b/25`, which is smaller throughout this b-range. For fixed b>0, taking A,B,C prime gives a genuinely different local ramification type from B=1, at the cost of the displayed exponent and one logarithm in this elementary family lower bound. The associated discriminant exceptional exponent `(17/25+2b/5)/(3−b)` is strictly increasing in b, even though the family-size exponent `1/(3−b)` increases as well.

More precisely, for each fixed `0<b≤1/20`, prime A,B,C in fixed positive-width boxes provide `≫X/(log X)³` distinct cyclic quartic fields after the at-most-two-character fiber, with `N f(χ_g)≈X` and `N f(χ_g²)≈X^(1−b)`. At any sufficiently small fixed power height the relative-quotient exception count is `O(X^(17/25+2b/5+ε))`. Their absolute discriminants are ≍X^(3−b), so the cumulative discriminant exception exponent is `(17/25+2b/5)/(3−b)` and the elementary field-count exponent is `1/(3−b)`, each with the same small-dyad height split used below. At b=0 take B=(1): this returns the two-prime family and its `≫X/(log X)²` lower count. Constants and the permitted height power can depend on the chosen b.

At the upper endpoint b=1/20, one has `(a,b,c)=(1/40,1/20,37/40)`, `t=1`, order-four exception exponent `7/10`, quadratic-core exponent `68/125`, and `|D_L|≈X^(59/20)`. The discriminant-order bound is therefore `O(Y^(14/59+ε))`, against `≫Y^(20/59)/(log Y)³` distinct fields. The order-four and quadratic detector height powers are both required; take the common power below the order-four power and 19/20 times the quadratic-core power.

## A three-prime example

Choose

    b=1/100,  u=19/600,  v=23/24,  t=77/75.                  (7)

For instance set `a=u,c=v`. Then `c₀=41/150`, `d₀=221/300`, and every allowed r lies in `[79/150,77/75]`. In this range the pair bound in (4) is at most the quadratic bound, so

    f(r)=max{1−(3/5)r, 41/150+(2/5)r,
                         221/300−r/10} ≤ 171/250.             (8)

The first and third faces decrease and equal 171/250 at the left endpoint; the second increases and equals it at the right endpoint. Thus the inverse witness alone gives a conditional zero-density exponent 171/250=0.684, with arbitrarily small fixed losses and sufficiently small X-power height. The dual ordinary-block moment (4) remains available, but cannot lower this particular relaxed scalar maximum: at the two endpoints it has f(1/2)=7/10 and f(0)=1 respectively.

For the quadratic core, on good q,

    χ_g(q)² = χ_(AC)(q)² · 1_((q,B)=1).                        (9)

The B factor deletes good Euler factors, which are nonzero in Re s>0; the primitive core is therefore χ_(AC)², with good conductor AC and `N f(χ_g²)≈X^(1−b)`. For prime A,C, a core's good conductor determines their unordered product, and the unequal norm scales determine their order. Each core has at most `X^(b+ε)` choices of B. The fixed-field quadratic sieve and detector exponent 13/25 at σ=4/5 consequently give a core-exception exponent

    b+(1−b)·13/25 = 328/625 = 0.5248 < 171/250.              (10)

The possible power height for χ_g² is measured at conductor X^(1−b): choose the common height exponent strictly below (1−b) times its admissible power and below the order-four one. The χ_g³ factor has the same symmetric zero count as χ_g.

Taking A,B,C to be prime ideals in fixed positive-width boxes produces `≫X/(log X)³` distinct source characters: their good tame exponents 1,2,3 distinguish their labels. Their cyclic quartic class fields have fibers at most 2, so the same lower order holds for distinct fields. Under the stated inputs, at most `O(X^(171/250+ε))` fields have a zero of `ζ_L/ζ_K` in `Re s≥4/5` and a sufficiently short polynomial-height window. Their bad conductors are uniformly bounded, and the conductor–discriminant formula gives

    |D_L|=|D_K|⁴ [N f(χ_g)]² N f(χ_g²) ≍ X^(299/100).        (11)

The corresponding discriminant-order exceptional exponent is `(171/250)/(299/100)=342/1495≈0.22876`, against family-size exponent `100/299≈0.33445`. As in the two-prime note, first count in fixed boxes; for cumulative discriminant ordering, use a trivial label count on sufficiently small X dyads and choose the Y-height power small enough for all larger dyads. These fields have an order-two local factor at B, so their good ramification types differ from the two-factor AB³ family. Combining the two gives a strictly enlarged union, although the fixed three-prime subfamily has an extra logarithm in the elementary lower count.

## No improvement over 17/25 from these scalar bounds

The following is a lower bound for the **relaxed minimax supplied by (4) and the 13/25 core estimate**, not a lower bound on true zero counts or a no-go theorem for other inputs. It applies at σ=4/5, allowing every `a,b,c` and every detector cutoff t≤3/2.

If `b>1/3`, the displayed core-count exponent `(13+12b)/25` already exceeds 17/25. For `0≤b≤1/3`, (3) and `u≤(1−b)/2` imply `c₀≤1−b` and `d₀≤1−b+1/4`. Hence for x≥1/2 the quadratic alternative in (4) does not reduce either quartic face: `E(x)=max{1,c₀+x,d₀+x/2}`.

If t≤1, the feasible witness `r=m=t/2` has `f(r)≥1−3t/10≥7/10`, already above 17/25. If t≥1 and F(t)<17/25, take the two feasible relaxed witnesses `(r,m)=(t,0)` and `(t−1/2,1/2)`. Since f(0)=1 and f(1/2)≥7/10, the first yields `c₀+(2/5)t<17/25`, and the second yields both

    1−(3/5)(t−1/2)<17/25,
    d₀−(1/10)(t−1/2)<17/25.

The first inequality forces `t>31/30`; the order-four increasing face then forces `u<1/30−3b/2`. Comparing the upper bound on t from that face with the lower bound from the d₀ face instead gives `u>1/30+7b/6`. These cannot both hold for b≥0. The two-factor choice b=0, u=1/30, t=31/30 attains 17/25, so it is the exact optimum of these relaxed upper-bound formulas. For b>0 the same argument is strict until b=1/3, and the core face is strict above it. Therefore varying B does not improve the two-prime 17/25 conductor exponent using just these two sieves, this detector, and the stated quadratic-core bound. Since 3−b≤3, it also cannot improve the 17/75 discriminant exponent by optimizing these formulas.

No inference about optimal true zero counts follows. In particular, a joint mixed moment, additional structure in the cores, or a sharper quadratic-family input could alter the comparison.

For one explicit prior comparator on the three-prime box (7), conjugation replaces the natural label by `A³ B² C`, of norm ≍X^(161/150). De Faveri's stated quartic natural-index exponent 15/22 at σ=4/5 therefore gives `X^(161/220+ε)` for the order-four factor before its height loss, larger than 171/250. The quadratic factor still requires its own estimate. This comparison is conditional on the cited source theorem and is not an exhaustive literature survey.

[check_scalars.py](check_scalars.py) verifies the example and the exact scalar contradiction. An independent source-qualified review checked the common-vector sieve applications, squarefree-kernel decomposition, core and field fibers, discriminant arithmetic and relaxed-minimax proof; it did not establish the imported analytic inputs.
