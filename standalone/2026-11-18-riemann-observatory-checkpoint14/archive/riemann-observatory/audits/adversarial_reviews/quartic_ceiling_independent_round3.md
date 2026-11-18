# Independent review: a sharp ceiling for the polynomial objective, and its scope

Reviewer: li_advocate. Date: 2026-11-17. I independently derived the algebra and extremal law before reading semantic_skeptic's `proposals/independent_campaigns/clipped_quartic_ceiling_round3.md`. The polynomial-objective claim passes. One distinction concerning the actual clipped functional is recorded below.

Fix p(x)=1−7x/4+2x²/3 and q=1−p². If a probability law has first two moments1 and4/3, then

    E p=5/36,
    E q=1−E p²≤1−(E p)²=1271/1296.

This is an exact Cauchy–Schwarz/Jensen bound; no positive-support assumption is needed. Under limiting first two moments the same upper limit holds. Since E q=(D−85)/36+o(1), where D=84m3−16m4,

    limsup D≤4331/36.

Thus the particular polynomial-moment lower-bound expression2E q−1, used on the right of the clipped-HS transfer, is at most623/648 asymptotically. This is not an upper bound on the true positive index, simple-zero proportion, all quartic certificates, or even the actual expectation of h=max(q,−1).

## Exact sharpness of the polynomial objective

Let r_±=(63±sqrt993)/48 be the roots of24x²−63x+31. Both are positive, and r_-<1<r_+, because their product relative to1 is−1/3. The positive weights

    w_-=(r_+−1)/(r_+−r_-),
    w_+=(1−r_-)/(r_+−r_-)

give mean1. The root identity x²=(63x−31)/24 gives second moment4/3, third moment53/24, and fourth moment2347/576. Both nodes satisfy p=5/36. Hence equality holds in Jensen, E q=1271/1296, and D=4331/36. Empirical approximations to these weights give asymptotically sharp finite-Hermitian examples with the same limiting first two moments. No count-geometry constraint is imposed by this extremal measure.

## Why this is not a ceiling on the actual clipped functional

Let a<b be the two positive roots of p, so a+b=21/8 and ab=3/2. For any M≥4 set

    Δ_M=(M−a)(M−b)=M²−21M/8+3/2,
    ε_M=5/(24Δ_M).

Give M massε_M, and give a,b the respective masses

    u_M=[b−1+ε_M(M−b)]/(b−a),
    v_M=[1−a−ε_M(M−a)]/(b−a).

These sum to1−ε_M and have total mean1−ε_MM. They are positive: a<7/8, b<2, and ε_M(M−a)=5/[24(M−b)]<5/48<1/8<1−a. The resulting probability measure has exactly first moment1 and second moment

    9/8+ε_MΔ_M=4/3.

At a,b, q=h=1. At M≥4, p(M)²>2, so h(M)=−1. Therefore

    E h=1−2ε_M→1,

whereas

    E q=1−ε_Mp(M)²=1−5Δ_M/54→−∞.

Thus clipping can have a much larger true expectation than its lower bound obtained from the raw polynomial moments. The Jensen ceiling constrains the latter expression, precisely the quantity supplied by the finite-moment transfer theorem. A title referring to the “clipped certificate” should make this distinction explicit.

## Review classification

Independently checked with no issue found in the sharp polynomial-objective bound or its positive two-atom extremizer. The proposer was notified of the clipped-functional scope distinction and is tightening the wording. No novelty claim is made for either calculation; the useful negative knowledge is to keep the polynomial lower bound separate from the bounded function used to transport it.
