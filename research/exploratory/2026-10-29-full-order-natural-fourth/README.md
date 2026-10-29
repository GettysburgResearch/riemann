# Natural-label density from moving twists and a fourth witness

**Superseded at σ=4/5:** [the direct n-free four-face theorem](../2026-10-29-direct-nfree-density/README.md) gives a strictly stronger source-qualified exponent for every fixed n≥4, using the n-free rows directly and no short-cutoff or moving-twist extension. This note preserves the independently checked earlier approach.

**Status.** A source-qualified conditional implication, not an independently established zero-free region. It assumes de Faveri's fixed-order squarefree large sieve and FHL character identities, together with the conductor-uniform fixed-field detector, its short-cutoff replay, and the common-profile/Sobolev/height interface isolated in [the sixth-order calculation](../2026-10-29-full-sixthfree-fourth-density/README.md). The moment and detector proofs have not been independently established here. Comparisons below concern one named source at fixed height and do not constitute an exhaustive priority claim.

Fix n∈{4,…,10}, a number field K containing μ_n, the FHL source data and a fixed good set S. For each good n-th-power-free ideal u let χ_u be the source character with original zero extensions. Subject to the stated inputs, for every ε>0 there is τ>0 such that

    Σ_{u good, n-free; Nu≤X} N(4/5,X^τ;χ_u)
       ≪_{K,S,n,ε} X^(R_n+ε),
    R_n=(3n²−10)/[n(6n−10)].                                  (1)

Zeros belong to the primitive inducing functions and are counted with multiplicity. Fixed exceptional principal presentations are absorbed by the individual zero bound. Good squarefree u alone give ≫X distinct characters, since their good conductor support is u; hence (1) would imply a density-one family rectangle at small polynomial height.

## Moving-twist moment

Write uniquely u=q b² with q squarefree, without requiring (q,b)=1. Source (2.4) gives the exact identity χ_u(a)=χ_q(a)χ_b(a)² on all good ideals with original zero masks. For a fixed b-dyad Nb≈B=X^b, put Y=X/B² and U=X/B. The detector is applied to the **original** characters χ_u, whose primitive conductor and deleted radical are ≪_S Nrad(qb)≪U. This holds uniformly as b grows and for shared q,b primes: all u-exponents lie in {1,…,n−1}, so their tame local characters are nontrivial. The infinity type is fixed and trivial. The fixed-field functional equation, zero-free buffer, deleted factors and common-profile detector must be uniform in these conductor upper bounds, as in the cited moving-b interface; in particular the needed t<1 is an explicitly imported short-detector replay.

Only after forming the detector, fix b and use χ_b(a)² as a common coefficient of modulus ≤1. By de Faveri Theorem 1.1 and fixed finite reciprocity sectors, for squarefree columns of scale D the squared operator norm is

    ≪ (UD)^ε [Y+Y^(1/n)D+Y^(1−1/n)D^(2/n)].              (2)

Indeed the source's additional term Y^(2/n)D^(1−1/n) is at most the third displayed term when D≤Y, and at most Y^(1/n)D when D≥Y; the plain D term is also absorbed. The number of b ideals is ≪B^(1+ε). For the ordinary fourth witness, square the common ordinary block, write its column as a=a₁v² with a₁ squarefree, fix v before dropping the row contraction χ_u(v²), and apply (2). Divisor bounds and Minkowski lose only ε. A fixed number of common-profile derivatives has the same coefficient norm bound; all heights use one allowance and are chosen only after the fixed exponent losses.

## Four ranges

Put δ=3/5. With D=U^x, division by a witness threshold U^(δx) and summation over b give the three X-exponent faces

    f₀(x)=(1−b)(1−3x/5),
    f₁(x)=b+(1−2b)/n+(2/5)(1−b)x,
    f₂(x)=b+(1−2b)(1−1/n)+(2/n−3/5)(1−b)x.              (3)

The inverse second-moment count is bounded by f(r)=max f_j(r); the ordinary fourth-moment count by f(2m). Saturated witnesses satisfy r≤t, m≤1/2, r+m≥t up to arbitrarily small fixed losses. Set

    b_L=(3n−10)/[2(9n−20)], b_M=n/[2(3n−5)], b_T=1−R_n.

For every n in the stated finite set, 0<b_L≤b_M≤b_T<1/2. The following choices cover all b. The estimates allow fixed ε losses and fixed dyadic constants; detector parameters are selected on a finite mesh before the height exponent.

* If 0≤b≤b_L, take `t=15(n−2)(1−2b)/[4(3n−5)(1−b)]` and `L=2t/3`. Then 1≤t≤3/2, and all three faces are ≤R_n on [L,t]. If r≥L use the inverse witness; otherwise the actual constraints give 2m≥L and 2m≤1≤t, so use the ordinary fourth witness.
* If b_L≤b≤b_M, take t=1 and L=2/3. All three faces are ≤R_n on [L,1], and the same inverse/fourth split applies.
* If b_M≤b≤b_T, take `t=(1−2b)/(1−b)+(3/5−2/n)/[2(1−2/n)]`. For these seven fixed n, 1/2<t≤1; an inverse witness has r∈[t−1/2,t] and each of the three faces is ≤R_n there. This is the only range requiring the short-t detector.
* If b_T≤b≤1/2, count labels trivially: B·Y≪X^(1−b+ε)≤X^(R_n+ε). Absorb the fixed-height individual zero-count factor by choosing τ small.

Each face evaluated at the stated r-endpoints becomes affine in b: the apparent denominator 1−b in t cancels against the factor 1−b in (3). It is therefore enough to verify each finite interval's two endpoints, plus the stated t bounds. [check_ranges.py](check_ranges.py) performs these checks with exact rational arithmetic for all seven n. The worst first-range endpoint b=0 attains R_n; no optimality of the analytic bound is asserted. Since U≥X^(1/2) and the t ranges form fixed compact sets, the global X-power height can be chosen after the uniform detector/profile degrees and prescribed loss.

## Named-source comparison

De Faveri Corollary 1.5 has natural-label fixed-height exponent `D_n=(12n²−38n+5)/(21n²−80n+50)` at σ=4/5. For n=4,…,10, (1) gives the following conditional gaps before height costs:

    n       R_n        D_n         D_n−R_n
    4       19/28      15/22       1/308
    5       13/20      23/35       1/140
    6       49/78      209/326     82/6357
    7       137/224    109/173     715/38752
    8       91/152     469/754     1337/57304
    9       233/396    635/1031    11237/408276
    10      29/50      11/18       7/225.

Each positive gap persists for sufficiently small polynomial heights after accounting for both sources' height exponents. These are comparisons of natural n-free labels, not statements about arbitrary fixed-order Hecke characters sorted by conductor. Constants can depend on n and K, and no simultaneous uniformity in n or K is claimed.

**Independent review.** Families checked the three moment faces, shared-prime masks using de Faveri (2.4), both cases absorbing the fourth sieve term, the actual witness interval, all exact endpoint inequalities and comparator gaps. The reviewer treats the underlying Hecke, sieve and short-cutoff detector statements as source inputs.

## All fixed orders n≥11: two exact uniform scalar covers

The same source-qualified natural-label conclusion extends to **every fixed n≥11**, at σ=4/5, with

    R=29/50 for 11≤n≤20,
    R=14/25 for n≥21.                                        (8)

The number field, order n, source data and every implicit constant are fixed before X grows. In particular this is not a uniform-in-n theorem. It uses the identical growing-b uniform detector, arbitrary-coefficient n-order sieve, original masks and common-profile/height qualifications as (1).

The exact certificate [check_all_orders.py](check_all_orders.py) and its [recorded cover](all-orders-cover.json) split `0≤b≤1/2` into 100 closed rational intervals. On each interval, one rational cutoff `t∈{1/2,51/100,…,3/2}` and one of the following modes is checked:

* **inverse:** `f(r)≤R` for `r∈[t−1/2,t]`;
* **second:** `f(x)≤R` on `[t/2,t]`; for r≥t/2 use inverse, otherwise the actual m lies in `[t/2,1/2]⊂[t/2,t]` and use the full ordinary **second**-moment bound `f(m)`;
* **fourth:** `f(x)≤R` on `[2t/3,max(t,1)]`; use inverse for r≥2t/3 and the ordinary fourth moment otherwise;
* **trivial:** `1−b≤R`.

The ordinary second moment uses the same arbitrary-column squarefree decomposition as the fourth, without first squaring the block; its bound is the full `f(m)`, not merely the first face. Since the three displayed faces are affine in x and separately affine in b and `h=1/n`, every maximum on one certificate rectangle occurs at a corner. Two h-rectangles suffice: `[1/20,1/11]` and `[0,1/21]`. The zero endpoint is only a scalar limiting bound; n is always a finite fixed integer. Where the certificate selects t=1/2, use the separately assumed short-cutoff detector at `t=1/2+η` and absorb the resulting O(η) change into ε. Choose the finite cover, profile orders and all preliminary losses before the common height power τ.

These two estimates also improve the **same natural-label** de Faveri Corollary 1.5 comparison at fixed height. Its exponent

    D_n=(12n²−38n+5)/(21n²−80n+50)

is strictly decreasing for n≥4, since its derivative is `−6(3n−10)(9n−25)/(21n²−80n+50)²`. The limiting endpoint checks are

    D_20−29/50=36/3425,
    D_n−14/25=(6n²+170n−575)/[25(21n²−80n+50)]>0 for n≥21.

For each fixed n the strict gap permits a sufficiently small height power after incorporating both sources' explicit or stipulated height costs. This is a named-source comparison only. The certificate verifies the rational inequalities and interval coverage, not the analytic inputs or detector extension.
