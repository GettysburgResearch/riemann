# An effective proper-source zero pair at every even weight k>=96

This analytic corollary makes the first coefficient depth effective.
It concerns the actual proper theta-source quotient S_k/ker([q]), taken
BEFORE Mellin observation. It is not the old period-side Schur quotient,
a one-dimensional restriction, or a numerical zero search.

## Exact accepted inputs

- Proper-source central criterion and zero implication:
  `0d1f90323c8d61abefee077b7bcaa4c024596a55`, independently reviewed at
  `31e5ca265cc3be43cff30962041d93a2be4d8ee2`;
  [TQ proof](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY.md), TQ1--TQ7.
- Actual coefficient Poincare kernel and its normalization:
  `14fa39a02267c043ac27cd68ef7157ef77afe83b`, independently reviewed at
  `3575c8274a887bc5de29aa41749cac37f49b73cd`;
  [HC proof](CUSP_FLAG_HECKE_SOURCE_CONCENTRATION.md), Section 7,
  especially the unfolding identity and HC20.

TQ imports the actual MP theta completion; that source and its Petersson
vacuum are unchanged. The effective argument below does NOT use a
non-effective cusp-norm asymptotic or its unknown onset.

## 1. Statement and exact quotient norm

**Theorem.** For EVERY even integer k>=96, the actual proper source quotient
L_(k,1) of TQ satisfies L_(k,1)(1/2)>0. It has a sign-changing real zero in
each of (0,1/2) and (1/2,1), with reflection preserving multiplicity.
The entire function s(s-1)L_(k,1)(s) retains both zeros.

The threshold96 is sufficient, not claimed optimal. This proves no
simplicity, uniqueness, individual ordinate, endpoint-scale location, or
statement at weight24. The higher fixed-depth TQ theorem remains
non-effective; this corollary is ONLY depth one.

Put nu=k-1>=95 and

    A_1 = Gamma(k-1)/(4*pi)^(k-1) = (nu-1)!/(4*pi)^nu.

Let P=P_(k,1) be HC's ordinary holomorphic coefficient Poincare series,
and p=[q]P. The exact normalization, with conjugate-linear first input, is

    G(P,f)=A_1 [q]f,        G(P,P)=A_1 p.                       (E1)

In particular p is real. The explicit bound below shows p>0.
For every f with [q]f=1, Cauchy--Schwarz in the ACTUAL Petersson form gives

    A_1^2 <= G(P,P)G(f,f)=A_1 p G(f,f).

Equality is attained at the genuine modular form f=P/p. Therefore the
quotient vacuum is EXACTLY

    G_Q=A_1/p.                                                (E2)

This is not an approximate norm and does not assume Hecke diagonalization
of the theta or period matrix. For k>=96 the native cusp dimension is
at least two, so ker([q]) is nonzero and the quotient is genuinely proper.

## 2. An all-weight lower bound for p

HC20, derived from the complete Kloosterman/Bessel expansion, gives

    |p-1| <= 4*pi*(2*pi)^nu/nu! * exp(4*pi^2/k).               (E3)

It retains the whole c>=1 series, using |S(1,1;c)|<=c,
sum c^(-nu)<=2, and the full defining Bessel-series bound.
No finite c-prefix or sampled Bessel function is substituted.

Use pi<22/7, hence 2*pi<7,4*pi<13 and
4*pi^2/k<1 for every k>=96. Also e<3. Thus

    |p-1| < 42*7^nu/nu!.

The exact integer comparison

    42*1000*7^95 < 95!                                       (E4)

and the consecutive ratio 7/(nu+1)<1 for nu>=95 prove

    |p-1|<1/1000,             p>999/1000                      (E5)

for ALL k>=96, not merely a finite tested range.
E4 is an integer inequality; no decimal special-function evaluation is used.

## 3. An all-weight lower bound for J/A_1

The source integral from TQ is

    J = integral_1^infinity y^(k-3/2) exp(-4*pi*y) dy.

Its full integral from zero is Gamma(nu+1/2)/(4*pi)^(nu+1/2).
Since the omitted integral is less than 1/(nu+1/2), we have

    J/A_1 >
      Gamma(nu+1/2)/[sqrt(4*pi)*Gamma(nu)]
      - 1/[(nu+1/2)A_1].                                    (E6)

First bound A_1 without a limiting statement. From 4*pi<13 and the exact
integer inequality

    1000*13^95 < 94!,                                        (E7)

we obtain A_1>1000 at nu=95. The consecutive ratio of
(nu-1)!/13^nu is nu/13>1, so A_1>1000 for every nu>=95.
Thus the final subtracted quantity in E6 is less than1/1000.

For x>0, integral Cauchy--Schwarz applied to Gamma(x+1) gives

    Gamma(x+1)^2 <= Gamma(x+1/2)Gamma(x+3/2)
                 = (x+1/2)Gamma(x+1/2)^2.

Using Gamma(x+1)=x Gamma(x), this yields the explicit bound

    Gamma(x+1/2)/Gamma(x) >= x/sqrt(x+1/2).                    (E8)

The function x^2/(x+1/2) is increasing for x>0. At nu=95, the following
is an EXACT rational inequality:

    95^2 / [(191/2)*(88/7)] > (137/50)^2.                     (E9)

Since 4*pi<88/7, E8--E9 show for every nu>=95 that

    Gamma(nu+1/2)/[sqrt(4*pi)*Gamma(nu)] >137/50.

Consequently E6 yields

    J/A_1 >137/50-1/1000 =2739/1000.                          (E10)

No Stirling error, numerical incomplete-Gamma value, or unknown
asymptotic threshold enters this estimate.

## 4. The strict central criterion and its zeros

By E2, the exact parameter in TQ is R=J/G_Q=pJ/A_1. Hence

    R > (999/1000)*(2739/1000)
      =2736261/1000000 >273/100 >e.                          (E11)

For completeness, the elementary last bound follows from the exponential
series and a geometric tail:

    e = sum_(n>=0) 1/n!
      <= sum_(n=0)^5 1/n! + (1/6!)/(1-1/7)
       =163/60+7/4320 <273/100.                              (E12)

The ratios after the n=6 term are at most1/7, so this bounds the complete
infinite tail. All comparisons in E4,E7,E9,E11,E12 are rational/integer
ones, with the uniform extensions proved above. The selection of96 was
post-result analysis, not a claim of preregistered or optimal discovery.

TQ's exact inequality, using the pointwise source quotient and its literal
vacuum, is

    L_(k,1)(1/2)/G_Q >=2R(log R-1),       R>1.

E11 makes this strictly positive. TQ/MP's residue +G_Q/2 at one makes
L_(k,1)(s) tend to negative infinity as s tends to1 from below.
There are no poles in (0,1); real analyticity and reflection therefore
give the asserted pair of sign-changing zeros. At least one in each
interval has odd multiplicity, but simplicity is not proved.

## 5. Verification boundary

This proof is an exact analytic and integer-inequality deduction from the
frozen parents. It introduces no computational producer, test module or
finite zero-location certificate, and does not change the37-module G
replay denominator. Independent review must check the complete infinite
Bessel bound, the Petersson normalization, the two integer base cases,
the all-weight monotonicity, the Gamma Cauchy--Schwarz bound and endpoint
signs; reproducing a few central-value samples would not suffice.

The result rules out a critical-line theorem based only on positive
theta-source completion for these particular native coefficient quotients.
It does not classify Hecke-compatible source operations or give an Euler
product, new automorphic representation, RH/GRH counterexample, complete
zero census, minimal weight, or uniform higher-depth threshold.
