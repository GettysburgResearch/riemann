# A fourth-moment extension reduced to one signed arithmetic estimate

18 November 2026. The director read the two independent pure-arm reductions, the third contour adjudication, and both independent reviews of its new smooth saddle lemma. The full fourth moment remains unresolved. The result here is a precise conditional reduction, with a proved asymmetric continuous estimate and a proved smooth contour/saddle replacement. The source's sharp arithmetic saddle replacement is not extended by this argument, and is not needed in the smooth route.

## Exact target and what is already covered

Assume RH and the usual symmetric strict derivative-square tail. Fix 0<a<b with 1/8<b<1/6. Set `D(s)=sum_(Y^a<p≤Y^b)p^−s`, W=Re D(rho), H0=log(b/a), d=b−a and m_j=(b^j−a^j)/j. The exact algebra is

```text
E_Y W^4=(1/8)Re E_Y D^4+(1/2)Re E_Y D³ conjugate(D)+(3/8)E_Y|D|^4.
```

The 3+1 and 2+2 arms have longest Dirichlet side Y^(3b)<sqrt(Y). Their fixed factorial coefficient envelopes, divisor-closed padding, real polarization and strict-tail transfer fit the established HLZ theorem. Only the 4+0 pure arm has excessive length y=Y^(4b), between sqrt(Y) and Y^(2/3).

Let P(z)=(1−d z)^4+2m3 z(1−d z). The verified signed source extraction for the mixed arms gives

```text
E_Y W^4−4![z^4] exp(H0 z+H0 z²/4)P(z)
 =(1/8)[Re E_Y D^4−m4_pure]+o(1),
m4_pure=4![z^4] exp(H0 z)[P(z)+3m2² z²].
```

Equivalently

```text
m4_pure=H0^4+4(−4d+2m3)H0³
        +6(12d²−4d m3+6m2²)H0²−96d³H0+24d^4.
```

For four distinct primes the signed residue kernel is the known cosine kernel plus `6 sum_(i<j) epsilon_i epsilon_j x_i² x_j²`. It has been extracted independently from the actual J and I formulas, including every sign pattern, not merely inferred from RMT. Only opposite-sign repeated prime pairs survive in mixed arms; repeats in a pure arm have a p^−2 lcm weight and vanish in its formal main term. The intrinsic CUE window includes 4b<1, but supplies no missing arithmetic asymptotic.

The same established input on |D³|² gives a uniform sixth absolute moment because 3b<1/2. Thus a proved pure fourth target would yield the fourth cosine target and its correct passage to weak subsequential limits. This is an incremental statistic, not a full band law or a proof of RH.

## One-sided continuous moments do not impose the half-power barrier

For bounded fixed coefficients Q(s)=sum_(h≤y)a_h h^−s against the constant second arm, the direct product AFE proof gives, for fixed y≤T^theta, theta<1, and |alpha|,|beta|≤c/logT,

```text
integral_1^T zeta(1/2+it+alpha) zeta(1/2−it+beta) Q(1/2+it)dt
 =sum_(h≤y)(a_h/h) integral_1^T [h^(−beta)zeta(1+alpha+beta)
    +h^alpha (t/(2π))^(−alpha−beta)zeta(1−alpha−beta)]dt
  +O_epsilon(T^epsilon[(yT)^(1/2)+y^(1/4)T^(3/4)]).
```

The two poles cancel at alpha+beta=0. The log(t/(2π)) weight is obtained with the same power bound after partial integration and log absorption. This is unconditional; constants depend on the fixed coefficient bound, theta and shift radius.

In an AFE product shell uv≤R, the frequencies are K1=hu and K2=v. Comparable ones are at most sqrt(2yR), so integration by parts and the harmonic integer-gap estimate cost T^epsilon sqrt(yR). Noncomparable ones have bounded inverse logarithm and the same absolute scale. The diagonal v=hu costs `T^(3/4)sum |a_h|h^(−3/4)`, giving y^(1/4)T^(3/4). This sharper asymmetric accounting replaces the balanced bound y sqrt(T). Uniform microscopic shifts and diagonal cancellation use the previously audited direct sharp interface. No general long quadratic-polynomial theorem is being assumed.

The source's principal discrete terms also retain their calculation: the Perron cutoffs lie between constant multiples of T/y and Ty, whose logarithms stay comparable to logT for theta<1. The classical zero-free and short-interval arguments still give arbitrary fixed logarithmic savings, and the relevant outer harmonic divisor sums are bounded for D^4. The obstruction is on the reflected nonprincipal side.

## A smooth contour formulation closes the saddle error

Take a compact comparable-height piece T approximately Y and a real cutoff w_T(t), supported between fixed positive multiples of T, with exactly two transition regions of width `H=T^kappa`. It can be formed by averaging both upper and lower endpoints. For theta=4b choose

```text
(1+theta)/2 < kappa < 1.
```

The conservative original proof also works under kappa>(2+theta)/3. The sharper threshold above uses the localized derivative norms for a two-transition cutoff and was independently checked by both reviewers.

Wide horizontal contours can be averaged rather than bounded pointwise at every ordinate. Integrating the absolute logarithmic derivative across the fixed real strip turns each zero singularity into a logarithm of its ordinate distance. Its square is integrable; the local multiplicity-counting zero bound gives O(H log²T) on a transition interval. Strip Sobolev and the Dirichlet mean-value theorem give a mean-square bound O(H y log^O(1)T) for the supremum of |D^4| across that strip. Convexity for the two shifted zeta factors and Cauchy–Schwarz then bound the averaged horizontal and microscopic connector errors by `T^(1/2+epsilon)sqrt(y)=o(T)`. The cutoff is real; no fictitious holomorphic extension of it is used.

The reflected phase uses chi(1−s+beta) under the source's convention zeta(s)=chi(s)zeta(1−s). After absorbing beta into the integration variable, the real saddle is t0=2πm/k and the leading normalized phase is e(−m/k). The intermediate cutoff w_T(t0+Im beta) is replaced by w_T(t0), with error O(1/(H logT)), **before Cauchy differentiation**. The original shifted integral and the resulting unshifted-cutoff main sum are holomorphic; the error bound can be proved on the shift circles without claiming that the intermediate translated cutoff is holomorphic.

For x=m/k comparable to T, Stirling and the exact signed-square-root change of phase give a quadratic Fresnel integral with a smooth compact amplitude A and scale delta=H/T. Factoring the leading normalization, Fourier inversion bounds the saddle error by

```text
T^−1 integral_R |xi|² |Ahat(xi)| dxi.
```

The general bounds ||A||_1=O(1), ||A^(4)||_1=O(delta^−4) give O(T²/H³). For the prescribed two transitions, ||A'||_1=O(1) and ||A^(4)||_1=O(delta^−3). Splitting at |xi|=delta^−1 and using the first derivative on the low-frequency part gives integral |xi|²|Ahat|=O(delta^−2), hence the sharper **O(T/H²)** per term. These estimates are uniform for the saddle outside the cutoff's support but in the same larger compact range. Far saddles are removed by repeated integration by parts. Absolute convergence is checked using the original real-line exponents after the complex shift, so no infinite-series boundary is discarded.

The comparable terms have total absolute coefficient mass O(T^(1+epsilon)y). Their aggregate errors are bounded by

```text
T^epsilon [T² y/H² + y + T y/H],
```

each a power saving under the stated kappa. The far terms save arbitrary fixed powers. Principal residue terms commute with the endpoint averaging. This proves the smooth saddle replacement, not a sharper estimate for the original hard arithmetic cutoff in Lemma 7.

Restore sharp **zero-sum** endpoints after differentiation. Under RH, zeta'(rho) is at most T^epsilon on a comparable-height window. A local Sobolev sampling estimate for D² and its known continuous mean-square norm bounds the absolute weighted mass over a transition by `T^epsilon(H+Y^(2b))=o(T)`. This holds also at exact ordinate endpoints. Thus sharp zero boundaries can be recovered without recovering the unproved sharp saddle transition. The distinction resolves the initial apparent disagreement between the two contour reviews.

## The single unresolved smoothly cut sum

Let c_k be the coefficient of D(s)^4 and

```text
B_(alpha,beta,eta)(m)=[m^−s] zeta(s+eta)zeta(s+alpha)zeta(s−beta)/zeta(s).
```

In the reflected arm the sufficient missing estimate is `o(T logT)`, uniformly on the three fixed separated microscopic shift circles, for

```text
E_w(alpha,beta,eta;T)
 =sum_(k≤y) c_k/k^(1−beta)
   sum_(m≥1) B_(alpha,beta,eta)(m)m^(−beta) w_T(2πm/k)
      [e(−m/k)−mu(k/gcd(m,k))/phi(k/gcd(m,k))].
```

An estimate only after the actual three derivatives, of real size o(T log^4T), is weaker and also suffices. Setting eta=0 prematurely loses the auxiliary derivative and is not an argument. The subtraction is exactly the principal unit-character average, including reduced modulus one. The unreflected arm has denominator one and no nonprincipal remainder.

Every nonprincipal conductor dividing k exceeds the smallest band prime Y^a on T approximately Y. This removes the polylogarithmic small-conductor problem here, but leaves the large-conductor blocks. Even squarefree k have a conductor-k primitive block with signed weights tau(conjugate(psi))psi(−1). Taking absolute values before the character average loses their phase. The source's hybrid-large-sieve bounds retain a Q² term and produce y sqrt(T), y^(4/3)T^(1/3), and y^(1/3)T^(5/6), all reaching T at y=sqrt(T). None of the new contour estimates supplies cancellation in E_w.

Compact comparable-height estimates are sufficient. The established positive |D|^4 prefix bound controls the normalized strict-tail mass beyond RY by O(R^−1(1+log^4R)). First let Y increase at fixed R, then let R increase. Main time factors vary by O(1/logY) under this compact rescaling. Consequently the stated missing estimate would prove the pure fourth limit and the fourth cosine extension through the displayed exact reduction. Until it is proved, those two conclusions remain open.

## A fixed sequence replaces the shifted family

The director subsequently checked the two independent fixed-sequence derivations and a third independent adjudication. The three differentiated shifts can be eliminated. This strengthens the reduction above; it does not prove the remaining estimate. Write E_B for the same complex signed sum, with coefficient sequence B(m), exterior factor c_k/k, and the same cutoff and original-modulus subtraction. All statements in this section are uniform for the stated two-transition cutoffs and fixed positive margin kappa−(1+theta)/2.

The exact mixed derivative at zero is E_A plus the signed sum with coefficient `log(k/m) [m^−s]zeta'(s)^2`, where

```text
A(m)=[m^−s](−zeta'(s)^3/zeta(s))
    =(d_2 * Lambda * Lambda * Lambda)(m).
```

There is no derivative on the cutoff or the Ramanujan subtraction. The external logarithm comes from differentiating `(k/m)^beta`. The subtraction is the average of e(−um/k) over ALL unit numerators u modulo k. Reduction to q=k/gcd(m,k) is valid also for noncoprime m: the unit-group map onto the units modulo q is surjective with equal fibers. For k=1 the signed difference is identically zero.

For every fixed polynomial in log d, log e and log k, the signed sum over m=de decays faster than every fixed power of T. Two different proofs check the necessary uniformity. A smooth hyperbola partition restricts the outer factor to d≪sqrt(kT). Poisson summation in the other factor has frequency distance at least 1/k unless k divides d. In the resonant case its value is independent of the unit numerator and cancels exactly. Otherwise H/d≫T^delta gives arbitrary saving by integration by parts. The two halves of the partition must be retained with their interchanged logarithmic weights. Independently, the exact finite Hurwitz representation of the shifted divisor series gives a functional equation whose complete bilinear class sum has size k, not k². All polar parts are independent of the unit numerator, including when the two shifted poles coincide. Mellin inversion on Re s=−B bounds the nonprincipal difference by

```text
O_B((log T)^C k (T/H)^2 (kT/H^2)^B).
```

Since k≤T^theta and H²≫T^(1+theta+delta), summing over k and taking any fixed number of shift derivatives preserves arbitrary power saving. This proves that the external-logarithm divisor term is negligible. It gives no analogous estimate for the Mangoldt convolution.

There is a further exact simplification. Put L=zeta'/zeta and

```text
C_*(m)=(d_2 * (Lambda log^2))(m),
sum C_*(m)m^−s=−zeta(s)^2 L''(s),  Re s>1.
```

The logarithmic derivative identities give, coefficientwise,

```text
−zeta'^3/zeta = (1/2)[−zeta^2 L'' + zeta zeta''' −3 zeta' zeta''].
```

Both remaining products are shifted-divisor derivatives, already covered by the uniform estimate. Consequently

```text
E_A=(1/2)E_C_*+O_M(T^−M)  for every fixed M.
```

This rapid decay applies to the discarded divisor products. The contour and saddle errors in the preceding section retain their separate, previously proved power savings. The sufficient open problem is now the single real estimate

```text
Re sum_(k≤y) (c_k/k) sum_(m≥1) C_*(m) w_T(2πm/k)
     [e(−m/k)−mu(k/gcd(m,k))/phi(k/gcd(m,k))]
   =o(T log^4 T).
```

The sequence C_* is nonnegative, but the bracket is signed; positivity supplies no cancellation estimate. The desired estimate remains open in this archive. It would yield the pure fourth target and the fourth cosine extension for 1/8<b<1/6 through the proved reductions. It is a sufficient condition, not a claim that every proof must establish this particular sum. No Dirichlet GRH, generic moment conjecture, or individual character cancellation has been silently assumed.

[Fixed-sequence derivation](prime98_fixed_arithmetic_sequence.md) · [Independent Mellin proof and coefficient identity](weighted98_fixed_sequence_review.md) · [Third independent adjudication](uniform99_fixed_sequence_adjudication.md)

[First reduction](prime90_pure_fourth_bottleneck.md) · [Independent reduction](weighted90_pure_fourth_review.md) · [Contour and smoothing construction](analytic95_pure_fourth_adjudication.md) · [Independent saddle review](prime96_smooth_saddle_review.md) · [Separate saddle and endpoint review](weighted96_smooth_saddle_review.md) · [Primary HLZ source](../../sources/classical63_derivative_moments/hlz2022print.pdf)
