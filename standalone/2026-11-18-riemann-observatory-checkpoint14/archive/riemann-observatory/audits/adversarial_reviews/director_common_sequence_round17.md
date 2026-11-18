# A common positive sequence can defeat the two progression budgets

18 November 2026. The director reconstructed the finite Fourier proof and integerization, read the independent advocate and two skeptics, and checked the full four-prime coefficient extension. A common nonnegative sequence meets the displayed all-residue variance and maximum-error bounds yet has a large projection against the exact unit-centered phase. **The norm centering is P/k or the induced unit-row mean. The prime-model baseline P/phi(k), global prime support and a Mangoldt pointwise cap are additional hypotheses not supplied here.** This is a stronger common-sequence variant of the earlier abstract row obstruction, with those changed hypotheses made explicit. It gives no lower bound for actual primes or the full C_* sum.

Evidence: [construction and full-support extension](prime161_common_sequence_phase_campaign.md), [independent Fourier and occupancy review](analytic163_common_sequence_review.md), [independent skeptical proof and alternative rounding](geometry163_common_sequence_skeptic.md). All conclusions are finite algebra and inequalities or their stated asymptotic consequences; publication novelty has not been established.

## Exact statement

Fix 1/2<theta<2/3, K comparable to T^theta and an integer P comparable to KT. Let the prime band be [X,(1+eta)X], with K=X^4 and fixed small eta>0 such that (1+eta)^4<2. Its fourth polynomial has full coefficient support S contained in [K,2K), including repeated factors. If M is the number of band primes, then

```text
abs(S)=binom(M+3,4) comparable to K/log^4 K,
c_k=4!/product_(p|k) m_p! in [1,24].
```

The prime number theorem supplies only this support count. The moving data variable below is an integer index, not a prime restricted by that theorem.

There exists b(n)>=0 supported on J=[P,2P) intersect integers with total mass P. Write B_(k,u)=sum_(n≡u mod k)b(n). Then

```text
sum_(k≤2K) sum_(u mod k) abs(B_(k,u)−P/k)² <= C PK,
sum_(k≤2K) max_(u mod k) abs(B_(k,u)−P/k) <= C K sqrt(P).
```

The second is O_B(P/log^B T) for every fixed B, because K/sqrt(P) is a fixed negative power of T. On unit residues both bounds also hold if P/k is replaced by their actual unit mean. Nevertheless

```text
abs(sum_(k in S) (c_k/k) sum_((n,k)=1) b(n)
       [cos(2pi n/k)−mu(k)/phi(k)])
 >= c sqrt(P abs(S)) comparable to K sqrt(T)/log² T.
```

It exceeds T log^4 T by a divergent factor. The same conclusions can be realized by **integer-valued counts** with exact total mass P. No assertion that these counts are 0–1 or bounded by log P is made. Their complete residue arrays have exact common-divisor marginal compatibility because they are induced by the same sequence.

## Preserve the moving frequencies and suppress small denominators

Define the real mean-zero periodic kernels

```text
h_k(n)=1_((n,k)=1)[cos(2pi n/k)−mu(k)/phi(k)],
H(n)=sum_(k in S) (K c_k/k) h_k(n).
```

Take L=floor(K/100), and let psi be uniform on the integer interval [-L,L]. Its multiplier satisfies abs(psi_hat(a/q))<=C min(1,q/K) for every nonzero reduced fraction. At 1/k, k in S, it is bounded below positively: every cosine in the average has argument at most 2pi/100. This short positive averaging preserves the desired moving frequency and damps the small denominators that would otherwise repeat too often in the progression variance.

The Fourier coefficient of h_k at 1/k is

```text
[phi(k)+Ramanujan_k(2)]/(2k)
 −mu(k) Ramanujan_k(1)/[k phi(k)]
 =[phi(k)+mu(k)]/(2k)−mu(k)²/[k phi(k)].
```

Every k is odd and all its prime factors tend to infinity. The expression is uniformly bounded below. This identity also holds for nonsquarefree k, when mu(k)=0. A different k' in the same dyadic shell cannot supply the frequency 1/k: its reduced denominator would require k to divide k'. This proves the full-support extension, rather than discarding repeated-prime coefficients and leaving uncontrolled cancellation from them.

All frequencies have reduced denominators at most 2K and circular separation at least 1/(4K²). Summing exponentials over an interval of N integers gives a Gram matrix with diagonal N and absolute off-diagonal row sum O(K² log(2K)). Its quadratic form and adjoint therefore have N plus or minus that error. Since P is much larger than K² log K, for the interior interval I=[P+L,2P-L),

```text
F=(psi*H)1_I,     M_*=norm_2(F) >= c sqrt(P abs(S)).
```

The same elementary Gram bound will give the variance upper estimate; no unrecorded phase-independent conclusion from a prime-distribution theorem is being invoked.

## Positivity without a fourth moment or clipping assumption

Let F_plus and F_minus be its positive and negative parts, lambda=K/M_*, and center each part on I:

```text
a_plus/minus=lambda [F_plus/minus−mean_I(F_plus/minus)1_I],
b_plus/minus=1_J+psi*a_plus/minus.
```

Centering is an orthogonal projection, so norm_2(a_plus/minus)<=K. Cauchy–Schwarz gives a_plus/minus(n)>=-K/sqrt(abs(I)). This tends to zero, while the baseline is one. Positive convolution and I+[-L,L] contained in J therefore make both b nonnegative with exact mass P. This avoids assuming a fourth moment for H or controlling the height of all its positive peaks.

For a mean-zero perturbation g=psi*a, progression Parseval gives the variance at modulus k as (1/k)sum_(1≤r<k)abs(g_hat(r/k))². After reduction, a frequency a/q carries the multiplicity

```text
sum_(k≤2K, q|k) 1/k <= C log(e 2K/q)/q.
```

Multiplication by abs(psi_hat(a/q))² makes this entire weight at most C/K, uniformly for all 2<=q<=2K. The adjoint Gram bound and norm_2(a)<=K now give total variance at most C(P/K)K²=C PK. The uniform baseline contributes only O(K²). Cauchy–Schwarz over moduli gives the maximum-error estimate. Replacing a constant reference by the actual unit-row mean decreases the unit squared error and increases its maximum by at most a factor two.

By symmetry of psi, the difference of the two projections against H is

```text
lambda [M_*²−abs(I) mean_I(F)²].
```

Mean-zero periodicity bounds the sum of psi*H on I by O(K abs(S)). Thus the mean correction divided by M_*² is O(K² abs(S)/P²)=o(1). At least one b has absolute H projection at least c K M_*. Dividing by K proves the phase lower bound. The two candidates guarantee a large absolute real projection; no prescribed sign is asserted.

## Integer-valued realization with exact mass

Choose the successful real b, and make P independent draws on J with probabilities b(n)/P. Let C(n) be the resulting counts. Their total is exactly P and their expectation is b. At each modulus k, the expected summed squared residue noise is at most P, so its expectation over k<=2K is at most 2PK. Markov gives the required variance bound with fixed positive probability after combining it with the deterministic bound.

The phase test W=H/K has supremum O(abs(S)/K). Its occupancy projection has noise variance at most C P abs(S)²/K². The squared signal is at least c P abs(S); their ratio is O(abs(S)/K²), which tends to zero. Chebyshev and the preceding fixed-probability event intersect for large T. Some count realization therefore retains the lower bound and variance budget, and the maximum estimate follows again by Cauchy–Schwarz. This proves integer-valued existence, not a finite-height assertion about the primes.

## The remaining arithmetic distinction

All full residue rows of this example have matching marginals under reduction. Their **unit-only** rows use their induced masses, which can differ between moduli. A genuinely prime-supported measure at these long scales puts every sample on units of all the band moduli and has reference unit mean P/phi(k). That is a different variance requirement. Even modulus two separates an ordinary integer baseline from an all-unit prime baseline. The construction cannot be used to assert that both specifications have been met.

Accordingly the verified obstruction is to an inference from the two displayed centered norm budgets and full common-sequence compatibility alone. It improves on treating unrelated rows as independent possible data, but it does not exclude a method that uses the sieve profile, unit support, bounded prime weights or stronger arithmetic correlations. The full smooth C_* sum remains open, as do estimates for genuine primes in its moving Fourier mode.

The concrete next test is to impose the actual all-unit support and P/phi(k) centering, or a suitable sieve substitute, while preserving the variance budget and phase signal. Another useful test asks whether a Mangoldt-size pointwise bound changes the implication. These are explicit additional hypotheses to investigate, not assumptions silently appended to the counterexample. No publication-priority conclusion or advance in a zero-free exponent follows.
