# Exact minimax for the two separate witness moments

**Status:** Elementary scalar optimization. It assumes the inverse and plain moment bounds and the saturated-witness length constraints of [the companion note](README.md), including a short detector for t<1. It neither proves that detector nor gives a lower bound for any actual row count. No priority claim is made.

Fix `0<δ<1`. For a detector parameter `0<t≤3/2`, suppose the only retained length information is

    r,m≥0,   r≤t,   m≤1/2,   r+m≥t,

and the only count inputs are the separate moment upper exponents

    I(r)=max(1,1/2+r)−δr,    P(m)=1−δm.

The count bound for a given witness is the better of these, `min(I(r),P(m))`. Let `F_δ(t)` be the worst such exponent over all witness pairs consistent with the displayed constraints. Then exactly

    F_δ(t) = 1−δt/2,                                0<t≤1/2;
    F_δ(t) = max{1−δt/2, min{1,1/2+(1−δ)t}},       1/2≤t≤1;
    F_δ(t) = min{1,1/2+(1−δ)t},                     1≤t≤3/2.  (1)

The unique minimizing parameter and value are

    t*=1/(2−δ),    F_δ(t*)=(4−3δ)/(4−2δ).              (2)

At t=t*, both witness pairs

    (r,m)=(t*/2,t*/2),      (r,m)=(t*,0)                (3)

are feasible and attain the same exponent. Thus (2) is the **exact** minimax for this relaxed moment-only mechanism. Both optimal witnesses are hypothetical allowed pairs, not claims that an actual zero produces either pair.

## Proof

For each r, the smallest feasible m is `max(0,t−r)`. Since P decreases in m, replacing m by this value can only increase `min(I,P)`; hence it gives the worst case. The feasible interval is `max(0,t−1/2)≤r≤t`.

If t≤1/2, all r≤1/2, so `I=1−δr` and `P=1−δ(t−r)`. Their minimum is `1−δ max(r,t−r)`, maximized at r=t/2. This proves the first line of (1).

If 1/2≤t≤1, the portion r≤1/2 still has its maximum at r=t/2, namely `1−δt/2`. On the portion r≥1/2, `I=1/2+(1−δ)r` and `P=1−δ(t−r)` are both increasing in r. Their minimum is therefore maximized at r=t,m=0, and equals `min(1,1/2+(1−δ)t)`. Taking the larger of the two portions gives the second line.

If 1≤t≤3/2, every feasible r is at least t−1/2≥1/2. The same monotonicity gives the maximum at r=t,m=0, proving the last line.

On (0,1], put `A(t)=1−δt/2` and `B(t)=1/2+(1−δ)t`. A strictly decreases and B strictly increases. Their unique intersection is `t*=1/(2−δ)∈(1/2,1)`, and there `A(t*)=B(t*)<1`, so the cap in (1) is inactive. Every smaller t has F≥A(t)>F(t*), and every larger t≤1 has F≥min(1,B(t))>F(t*). For t≥1 the last line of (1) is nondecreasing and starts above F(t*). This proves (2), and the two maximizers (3) follow from the branch calculations. □

With `δ=2σ−1`, the value is `(7−6σ)/(6−4σ)`. For example σ=4/5 gives δ=3/5, `t*=5/7`, exponent `11/14`, and the two saturating relaxed witness pairs `(5/14,5/14)` and `(5/7,0)`. Fixed bin, dyadic and height losses perturb these equalities by O(κ); they are chosen before X grows and are not part of the exact scalar statement.

At δ=0 the value is 1 and minimizers are not unique; at δ=1 the value is 1/2 and all t∈[1,3/2] also minimize. These endpoints are irrelevant to fixed `1/2<σ<1` but explain why strict uniqueness was stated only for 0<δ<1. Improving (2) needs a stronger moment, an estimate combining the two words, or genuinely additional information excluding one of the relaxed witness configurations.

**Independent review:** A second researcher checked the piecewise maxima and shared endpoints, intersection and cap, uniqueness, extremizing witness pairs and σ=4/5 arithmetic. The review does not establish the assumed moments or short detector.
