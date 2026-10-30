# Independent review: retaining all four large-sieve terms

De Faveri's Θₙ has n-free rows and columns in the orientation used here. With rows bounded by X and columns by Xˣ, its four monomials give the exponent

    E(x) = max{1, 1−1/n+2x/n}                    (0≤x≤1),
    E(x) = 2/n+(1−1/n)x                         (1≤x≤3/2).

The second identity uses `2/n+(1−1/n)x≥x` for x≤2. The inverse columns are squarefree, and the ordinary fourth-moment columns can be decomposed as `a=a₁v²`; the fixed-v row factors are contractions and Minkowski sums their coefficient-mass losses. As in the underlying note, the uniform detector, simultaneous witnesses and common-profile/Sobolev transfer are assumed analytic inputs.

For `2/n<δ<1−1/n`, let

    t=3(n−3)/(n(3−δ)−7),    L=2t/3,
    R=2/n+(1−1/n−δ)t.

Then `1<t<3/2` and `2/3<L<1`. On `[L,1]`, both faces of `E(x)−δx` decrease; the second dominates the first because their difference is `(2x−1)/n`. On `[1,t]` the remaining face increases. Direct substitution gives `E(L)−δL=E(t)−δt=R`. If the inverse witness r satisfies `r≥L`, its exponent is at most R. Otherwise, `r+m≥t` and `m≤1/2` imply `L≤2m≤1`, and the ordinary fourth witness gives the same bound, up to the fixed detector losses. The limits are strict, so sufficiently small fixed losses can be absorbed in ε.

At `θ=4369347/5000000`, the source's middle Corollary 1.5 branch applies for every n≥4, since `1/2+1/n<θ<1−1/(2n)`. Exact algebra yields

    R=(1891959n²−1914571n−12500000)/[7n(804379n−2500000)]

and the source exponent minus R equals

    (630653n−2500000)(1869347n−5000000)
      (1869347n²−9977388n+12500000)
    / [7n(804379n−2500000)
      (5852276793591n²−21846735000000n+12500000000000)].

All factors are positive for n≥4: writing n=z+4, the numerator quadratic is `1869347z²+4977388z+2500000` and the denominator quadratic is `5852276793591z²+24971479348728z+18749488697456`. For n=4, R=`842755/1674204≈0.50337653`, versus approximately `0.50374832` in the printed source. The gap is small, so a comparison with growing heights requires choosing the positive height power sufficiently small.

This review verifies the source orientation and scalar deduction, not the imported detector, profile transfer, or analytic interpretation of the Lean candidate. It is a density bound, not an individual zero-free theorem or a priority claim.
