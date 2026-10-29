# A short-detector obstruction for the collapsed inverse face

**Status:** Exact scalar comparison, independently checked internally and conditional on the usual saturated-witness and moment interfaces. It is not a lower bound for actual row counts and does not rule out a different detector, a stronger moment, or a joint estimate. No priority claim. It explains why the new sixth-power-sieve inverse face does not by itself improve the existing Xu–Sang count by choosing a shorter detector parameter.

Normalize the row length to one. Assume a detector at a parameter t∈[0,2/3] yields nonnegative lengths r,m with r≤t, r+m≥t, m≤1/2 (up to small losses), and the separate spikes |M_r|²≥U^(δr−o(1)) and |S_m|²≥U^(δm−o(1)). Suppose prime selection of total relative width z gives gain 2qz in squared magnitude, with x=q/δ∈[0,1/2]. Put κ=3/4 and c=1/(3κ)=4/9. In addition to the ordinary inverse and plain moment capacities, grant the newly derived inverse face r+z≤1/2. Ignore any shortage of physical prime slots, so this grants the hypothetical count the strongest benefit available from these separate estimates.

Then the worst-case row-count exponent obtainable by taking the better of the separate inverse and plain estimates cannot be strictly smaller than the existing Xu–Sang exponent Rκ(δ,x), for 0<δ≤5/6. This is a limitation of this scalar optimization: an actual family may have more structure than these necessary witness constraints.

## Calculation

For 0≤r≤1, the maximum inverse width provided by the union of the old and new faces is

    z_M(r) = max{ min((1−r)/2, (3−2r)/8), max(0,1/2−r) }.

For 0≤m≤1/2, the plain width is z_P(m)=(1−2m)/(6κ). With q=δx, the separate Chebyshev exponents are

    A_I=1−δ[r+2x z_M(r)],
    A_P=1−δ[2m+2x z_P(m)].

The source count from Xu–Sang Proposition 4.1 is R=1−δH, where

    D=3−(1+2c)x,  P=(2−2cx)(1−x),
    H=1−(α−δ)P/{2[(α−δ)D+δP]},  α=5/6.

Here D,P>0 and H≥1−P/(2D)≥2/3, since 2D−3P=2x(2+c−3cx)≥0. A direct identity strengthens this to

    1−P/(2D) ≥ 2/3+cx/3,                              (1)

because the numerator after clearing the positive denominator is

    2D−3P−2cxD = 4x(1−c)(1−cx) ≥ 0.

If 0≤t≤1/3, consider the admissible witness pair r=t,m=0. For r≤1/6, the new width dominates and

    r+2x z_M(r) = x+(1−2x)r ≤ 1/6+2x/3 ≤ 1/2.

For 1/6≤r≤1/3, the old second face dominates and the same quantity is at most 1/3+7x/12≤5/8. The plain gain is at most 2x/(6κ)=cx≤2/9. Thus the better of A_I and A_P is at least 1−(2/3)δ≥R.

If 1/3≤t≤2/3, consider r=1/3,m=t−1/3. This pair satisfies all the witness length constraints and m≤1/3. The inverse gain is at most 1/3+7x/12≤5/8. The plain gain is increasing in m on [0,1/3] and is at most

    2/3 + x/(9κ) = 2/3+cx/3.

By (1) both gains are at most H, so the better of the two count exponents is at least R.

In the actual source optimization the estimates must hold for every possible admissible witness pair. Exhibiting one pair for each t with exponent at least R proves the stated worst-case barrier. Small fixed margins and the finite prime supply can only weaken these hypothetical estimates, and do not alter the conclusion after the loss tends to zero. □

The new inverse width exceeds the old one only for r<1/6. In the ordinary detector, r+m≥t and m≤1/2 therefore force t<2/3 to access that extra width. The scalar result above shows that the extra face cannot improve the current count within this class of separate-moment arguments, even if a shorter detector construction is proved. Sources: [Xu–Sang Proposition 4.1](https://arxiv.org/abs/2610.15291v2) and the conditional [general-field collapsed sieve](../2026-10-29-general-field-collapsed-sieve/README.md).

**Independent review:** A second researcher checked both hypothetical witness pairs, the union of inverse faces, the gain bounds, and the comparison with R. This is a worst-case scalar obstruction, not a lower bound on actual row counts.
