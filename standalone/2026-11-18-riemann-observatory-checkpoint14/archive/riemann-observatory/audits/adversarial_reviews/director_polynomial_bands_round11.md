# Cumulative Gaussian limits and non-Gaussian prime bands

18 November 2026. The director read the primary HLZ Theorem5 and equations(5),(24), the independent cutoff/variance/cubic calculations, and the original HKO density derivation on pp.2614–2615. The coefficient extraction, support restrictions, repeated-prime terms and moment bounds were reconstructed independently. Symbolic and interval programs have separate director replay receipts. The statements below are conditional on RH and the matched published shifted-moment input. Publication priority remains unestablished. A full arithmetic limiting distribution of a fixed polynomial band is not proved. A joint third-moment tensor has not been calculated.

## Sampling law and the aggregate interface

Use the normalized symmetric strict tail on |gamma|>Y with weights |zeta'(1/2+i gamma)|^2/(1/4+gamma^2). This is one derivative-weighted ordinate, not ordinary zero sampling or adjacent-zero statistics. For D(s)=sum_(p in a prescribed prime set)p^(-s), the coefficients of D^j are bounded by j!, independently of the largest prime. The divisor closures of finitely many such supports can be padded by a fixed positive baseline so that four signed arrays satisfy the source's coefficient envelope and submultiplicative condition. Polarization extracts the required bilinear forms before any main-term expansion.

This order is essential: HLZ's O_A(T log^(-A)T) remainder is used ONCE for the full polynomial, rather than once per character and then multiplied by an exponential number of absolute coefficients. Every fixed degree fits a fixed declared length y=T^delta<sqrt(T) in the ranges stated below. The main local quotient retains its lcm weight. Its relative change is O(log(mn/gcd(m,n)^2)/log T), and the sum against positive model coefficients is controlled by the corresponding raw moment.

The full-paper audit separately scrutinizes the source's continuous sharp-interval interface. Independent direct product-AFE calculations supply the required uniform replacement for bounded padded arrays, with error O_epsilon(T^epsilon[y sqrt(T)+sqrt(y)T^(3/4)]) for |alpha|,|beta|<=c/log T, fixed small c. Both weights1 and log(t/(2pi)) are covered. The sharp estimate is not obtained by silently shrinking the smoothing in Pratt–Robles beyond its stated derivative class. Theorem5-only consequences do not use the distinct Lemma6 smoothing reduction, whose parameter signs are being audited separately.

All transfers use the inclusive prefix in the subtracted Stieltjes boundary for the strict tail. Primes and coefficients are fixed at height Y throughout the prefix variable T>=Y. Bounded polynomials in log p/log T can be frozen at T=Y with error O(log(T/Y)/log Y), integrable against the normalized t^-2 log^4t tail profile.

## Larger cumulative cutoffs

Set H_P=sum_(p<=P)1/p, V_P=(1/2)sum_(p<=P)(1/p-1/p^2), W_P=sum_(p<=P)cos(gamma log p)/sqrt p. If P(Y) tends to infinity and log P=o(log Y), every fixed moment of (W_P-H_P)/sqrt(V_P) tends to its standard Gaussian value. In particular this covers exp((log Y)^a) for every fixed0<a<1.

For P=Y^theta, every fixed0<theta<1/2 gives weak Gaussian convergence with that same centering and normalization. Moments through order2k also converge when k theta<1/2. The proof does not assert all moment orders at a fixed positive theta or the endpoint theta=1/2.

For the near-power reduction choose P*=exp(L exp(-(log L)^(1/3))), L=log Y. Below P* the direct local error decays faster than the fixed powers of the harmonic mean introduced by centering. The discarded band up to Y^theta has harmonic mass O((log L)^(1/3)) while V_P is comparable to log L. Bound its2k-th power by |D_band^k|^2 plus its mean term. Its polynomial length P^k fits the source when k theta<1/2. Dividing by V_P^k makes the band negligible, even using the conservative raw moment bound. For k=1 this proves weak convergence for every theta<1/2 by Slutsky; for subpower P all fixed k fit. This avoids falsely extending a fixed finite list of moment estimates to all orders.

The effective conductor deletion can be tracked separately. It is not required to change a qualitative published theorem into the conditional deductions above. No practical numerical onset is claimed. Arbitrary normalized joint arrays do not automatically inherit the bounded Dirichlet-coefficient envelope: converting their phase coefficients to Dirichlet coefficients multiplies by sqrt(p). Their larger-cutoff extension has a separate scope.

## Fixed polynomial bands retain a different law

For0<a<b<1/4 set Delta_j=b^j-a^j and

```text
W= sum_(Y^a<p<=Y^b) cos(gamma log p)/sqrt p,
S= sum_(Y^a<p<=Y^b) sin(gamma log p)/sqrt p.
```

Their limiting moments are

```text
E W -> log(b/a)-4Delta_1+(2/3)Delta_3,
Var W -> (1/2)log(b/a)-4Delta_1^2+4Delta_1 Delta_3-(4/9)Delta_3^2,
E S = 0,
Var S -> (1/2)log(b/a)-(3/2)Delta_2^2,
Cov(W,S) = 0.
```

The exact zero statements follow from the symmetric sampling law, not a one-sided imaginary-character estimate. Both variances are strictly below the independent Poisson-circle value. The cumulative normalized Gaussian theorem and these band formulas are compatible: a bounded band correction disappears when divided by the cumulative standard deviation, which diverges.

The leading one-prime factor is F(x)=1-4x+2x^3, x=log p/log Y. For distinct primes at x,y, the ratio and product kernels are

```text
Kratio = F(x)+F(y)-1+12xy-2xy(x^2+y^2)-6x^2y^2,
Kproduct = F(x)+F(y)-1+12xy-2xy(x^2+y^2)+6x^2y^2.
```

The cosine covariance correction is C(x,y)=-4xy+6x^3y+6xy^3-4x^3y^3. It has rank at most2 as a form on test functions in L2(dx/x). The sine correction is the rank-one kernel-6x^2y^2. The cosine diagonal is exactly(1/2)sum1/p; the repeated p^2 oscillatory contribution vanishes on these moving bands. Integrating C against dx/x dy/y gives the displayed variance. Product frequencies require support Y^(2b), hence the strict b<1/4 condition.

The covariance is genuinely positive: C=-g tensor g+5x^3 tensor x^3, g=2x-3x^3, and integral_0^(1/4) g^2 dx/x=931/8192<1/2. Thus the full cosine form is bounded below by(1/2-931/8192) times the L2 norm on any such band. This is a consistency check stronger than the variance of one test alone.

## A rigorous Gaussian obstruction

For0<a<b<1/6 the limiting centered third moment of W is

```text
kappa3 = -8Delta_1^3+24Delta_1^2 Delta_3
         -8Delta_1 Delta_3^2+(16/27)Delta_3^3 < 0.
```

On[a,b]=[1/20,1/10] it is exactly-818904257/864000000000. The distinct-prime cubic coefficient comes from degree3 in the J exponent and degree4 in I before the auxiliary derivative. Its centered integrand against ordinary dx dy dz is

```text
-8+24(x^2+y^2+z^2)-24(x^2y^2+y^2z^2+z^2x^2)+16x^2y^2z^2.
```

It is bounded above by-8+72b^2+16b^6<0. The support D^3 requires3b<1/2. Terms with exactly two equal primes contribute(3/2)H E W to the raw third moment; they cancel the corresponding second-moment diagonal on centering. All-equal terms and the remaining prime-square lcm sums vanish. Omitting this coincidence analysis would not prove the formula.

Uniform fourth moments follow from |Re D|^4<=|D^2|^2, using length Y^(2b), the bounded local multipliers and the positive comparison moment. This proves uniform integrability of cubic powers. Hence no subsequence of the correctly centered band can converge weakly to a Gaussian: its mean would be zero and third moment zero, contradicting the strictly negative limit. This is stronger than showing a different model mean. It does not identify the full non-Gaussian band distribution.

## An exact random-matrix moment connection

Hughes–Keating–O'Connell's rooted derivative-square ensemble normalizes the joint Haar matrix and uniform root label by the derivative-square weight. It is different from keeping an unweighted Haar matrix and normalizing labels separately within each matrix. After rotation to the selected root1, the remaining N-1 eigenvalues have density Vandermonde-squared times product|1-z|^4, directly from HKO(2.2)–(2.8).

This is the projection DPP on polynomials of degree<=N with both value and derivative zero at1. Its projection is E-Q, with Q spanned by the normalized constant coefficient vector and the centered linear vector j-N/2. The continuum rank-two kernel is q(s,t)=1+12(s-1/2)(t-1/2). Its shift trace is2-4x+2x^3; including the deterministic root and taking the NEGATIVE cosine Fourier-band observable gives F(x). Exact projection trace formulas give the same rank-two cosine and rank-one sine corrections, and the same centered cubic in both frequency chambers. Riemann sums use dx/x, matching the prime reciprocal measure by Mertens. The director checked the primary HKO density and the independent symbolic identities.

These are proved band-mean/covariance and centered-cosine-third-moment matches in their stated ranges, with arithmetic conditional on RH. They are not a theorem transferring the complete random-matrix law to zeta zeros. The next precise problem is to characterize the limiting fixed-band law, or identify the additional uniform high-order/characteristic-function estimate that would establish this candidate DPP law. A separate, easier crossover occurs when the positive exponent band itself shrinks to zero; the established small-logarithmic-scale Gaussian model then becomes relevant again.

[Cutoff proofs](prime70_hlz_cutoff_extension.md) · [Independent cutoff audit](weighted70_hlz_cutoff_review.md) · [Variance and RMT derivation](prime71_hlz_band_covariance.md) · [Independent covariance](weighted71_hlz_band_second_moment.md) · [Third moment](prime72_hlz_band_third_cumulant.md) · [Independent rooted-CUE check](weighted73_rooted_cue_band_match.md) · [Third source reconstruction](geometry71_hlz_band_independent.md)
