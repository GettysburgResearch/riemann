# The first positive observed-hub repair already has too much variance

**Status: PROPOSED complete analytic and computer-assisted obstruction.**
This excludes a precise subclass of the growth-controlled infinite stars
in HARMONIC_STAR.md. It is a full-function obstruction using the tail
coefficient and the variance, not an unsuccessful finite moment fit.

Fix exactly `w_n=1/[2(n+a)]`, n>=0, a>0, without altering its weight head.
Give the fair hub a nonnegative observable weight B. Assume

\[
 J_n\ge h w_n,\quad J_n=h w_n+O(w_n^2),\qquad h=7/2. \tag{1}
\]

The natural repaired profile `J_n=(7/2)w_n+[37/(6 log2)]w_n^2` belongs
to this class. No model in (1) has the actual theta distribution.

## 1. The linear tail coefficient fixes the hub weight

The fair harmonic product has the more explicit coefficient

\[
 C_a=\tfrac12[\log(1/2)-\psi(a)+\gamma+\log(4/\pi)-1]. \tag{2}
\]

To derive it, split `sum tanh(u/(n+a))/(n+a)` at n+a<=u.
The harmonic portion is `log u-psi(a)+o(1)`, and the remaining Riemann
sum tends to

\[
 I=\int_0^\infty[\tanh v-1_{v\ge1}]\frac{dv}{v}
   =\gamma+\log(4/\pi). \tag{3}
\]

For a pinned evaluation of the last integral, integrate by parts to get
`I=- integral sech^2(v) log(v) dv`. The Mellin integral
`integral v^s sech^2(v)dv=2^(1-s) Gamma(s+1) eta(s)`, initially in a
region justified by its convergent exponential expansion and then by
analytic continuation to s=0, has logarithmic derivative
`log(pi/4)-gamma` there. Use eta(s)=(1-2^(1-s))zeta(s), zeta(0)=-1/2,
and zeta'(0)=-(log(2pi))/2. The special values are pinned in the
[NIST DLMF](https://dlmf.nist.gov/25.6#E11); no numerical approximation
to I is used in the proof.

The coupling perturbation in (1) does not change the linear coefficient.
An observed hub adds Bt. Comparing with the actual theta coefficient
`C_theta=-(1+log(2pi))/2` therefore forces the exact identity

\[
 \boxed{B=\frac{\psi(a)-\gamma-\log4}{2}\ge0.} \tag{4}
\]

If equality of the linear coefficients fails, the complete MGFs already
differ. The remainder of the proof assumes (4).

## 2. Monotonicity and elementary bounds

Write eta_n=tanh J_n, m=sum w_n eta_n, S_r=sum w_n^r. Directly from
conditional independence,

\[
 \operatorname{Var}X=B^2+S_2+2B\sum_nw_n\eta_n
                    +2\sum_{i<j}w_iw_j\eta_i\eta_j. \tag{5}
\]

Every term involving eta is coordinatewise nondecreasing for B>=0 and
eta>=0. Thus (1) bounds the variance below by the global h-tilted star.
Using `x-x^3/3<=tanh x<=x` for x>=0 gives

\[
 \operatorname{Var}X\ge S_2-h^2S_4
                +[B+hS_2-(h^3/3)S_4]^2, \tag{6}
\]

whenever the displayed bracket's lower bound is positive. For (6), first
use the baseline conditional mean `m_h>=hS_2-(h^3/3)S_4` and conditional
variance `sum w_n^2 sech^2(hw_n)>=S_2-h^2S_4`.

Convex trapezoidal comparison for x^(-2), and decreasing integral
comparison for x^(-4), imply

\[
 S_2\ge\frac1{4a}+\frac1{8a^2},\qquad
 S_4\le\frac1{48a^3}+\frac1{16a^4}. \tag{7}
\]

The needed digamma bounds, for a>1/2, are

\[
 \log(a-1/2)<\psi(a)<\log a-\frac1{2a}. \tag{8}
\]

For completeness these follow from the standard positive-argument
integral for psi minus the Frullani integral for log. The lower
difference is the integral of
`e^(-at)e^(t/2)[1/t-1/(2sinh(t/2))]>0`.
For the upper difference use
`1/(1-e^(-t))-1/t>1/2`, equivalent to coth(t/2)>2/t.
These inequalities follow from sinh x>x and tanh x<x, respectively.

## 3. An exact rational covering of the whole parameter range

certify_harmonic_observed_obstruction.py executes the following finite
inequalities with Fractions only:

- It proves `1.963<gamma+log4<1.964`. The Euler-constant enclosure is
  the harmonic-number Euler--Maclaurin formula at N=100 with remainder
  between -1/(120N^4) and0. Logarithms are enclosed by the atanh series
  after range reduction to [1,2], including its full geometric tail.
- It proves `log(7.6)-1/(15.2)<1.963`. Hence (4) and (8) require a>7.6.
  To include every a>0, first use
  `psi'(a)=sum_(n>=0)(n+a)^(-2)>0`: psi is increasing on the full
  positive half-line. Thus psi(a)<=psi(7.6) for every a<=7.6,
  including the range a<=1/2 outside the displayed lower bound's domain.
- It covers [7.6,12] by the44 closed intervals [k/10,(k+1)/10], k=76..119.
  On each interval it uses its upper endpoint in the lower S_2 bound,
  its lower endpoint in the upper S_4 bound, and
  `B>=max(0,[log(a_lower-1/2)-1.964]/2)`. Every whole-interval lower
  bound in (6) is strictly greater than .048.
- For a>=12, (4) and (8) give
  `B>=[log(11.5)-1.964]/2`, whose square alone is greater than .047.
- It reconstructs the original complete theta variance from all theta
  indices and the full time range, with the pinned320-bit directed
  backend and explicit Taylor/time/index tails, proving v_theta<.047.

The model variance is therefore larger than the actual theta variance
in every possible parameter range. No optimizer, sampled parameter,
special-function library, saved theta moment, or floating accept/reject
decision enters this conclusion.

## 4. Exact scope

This excludes all couplings above the global h w profile on the stated
unmodified harmonic weights, not just quadratic perturbations. It does
not exclude a profile that dips below h w at some indices, or a changed
finite weight head. Those changes affect the variance comparison or the
linear-coefficient identity. No larger class is claimed to be excluded.
