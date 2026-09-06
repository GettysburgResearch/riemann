# Sharp all-scale Jordan Green positivity

Status: **PROPOSED THEOREMS WITH COMPLETE NATIVE PROOFS; INDEPENDENT REVIEW PENDING**.
Scope: the literal generalized-Jordan arithmetic source, all real scales and
all nonnegative times; safe-half-plane Laplace kernels of every finite rank.
This manuscript does not prove RH, critical Xi innerness, or a source-to-Weil
isometry. No finite experiment supplies an unbounded quantifier below.
Author: Astra, returning to research after the Reviewer D audit.
Date: 2026-09-06.
Claim namespace: `JGC26` within this exact path.

The open density in PR #396, L-91026, has coefficient sqrt(275/14).
We prove it with an explicit positive margin, and prove the sharp universal
coefficient is actually 2. The input missed by the earlier transport estimates
is the elementary factorial identity for the von Mangoldt harmonic sum.
Sources and exact predecessor versions are listed in SOURCES.tsv.

## 1. Definitions and main theorem

For real s>0 let

\[
 F_s(n)=\prod_{p\mid n}(1-p^{-s}),\quad F_s(1)=1,
 \qquad c_s=\zeta(1+s)^{-1},\qquad r_s=c_s/s.
\]

All prime products use ordinary primes. Define, for t>=0,

\[
 E_{s,0}(t)=\sum_{n\le e^t}\frac{F_s(n)}n-c_st,
 \quad
 E_{s,1}(t)=\int_0^t E_{s,0}(v)\,dv.
\tag{1.1}
\]

E_0 is right-continuous, including the unit atom at t=0. Left limits at
positive activation knots are allowed in every lower bound below.
E_1 is continuous and locally absolutely continuous. For real kappa set

\[
 B_{s,\kappa}(t)=-c_s+\frac{\kappa s}{2}E_{s,0}(t)
                         +s^2E_{s,1}(t).
\tag{1.2}
\]

**Theorem JGC26.T1 (sharp universal threshold).**

\[
 [B_{s,\kappa}(t)\ge0\ \text{for every }s>0,t\ge0]
 \quad\Longleftrightarrow\quad\kappa\ge2.
\tag{1.3}
\]

For kappa>=2 the inequalities are in fact strict. No lower cutoff on s or
upper cutoff on t is imposed. The following nonoptimal quantitative bounds
hold at the sharp coefficient. With

\[
 e(y)=E_{s,0}(y/s),\quad I(y)=sE_{s,1}(y/s)=\int_0^y e(v)dv,
 \quad b_2(y)=\frac2s B_{s,2}(y/s)=2(e(y)+I(y)-r_s),
\]

one has, uniformly for all y>=0,

\[
 b_2(y)\ge
 \begin{cases}
 47s/1280,&0<s\le1/2,\\
 1/256,&1/2\le s\le2/3,\\
 203/3750,&s\ge2/3.
 \end{cases}
\tag{1.4}
\]

The overlapping endpoint estimates are compatible; any applicable bound may
be used. In particular every displayed lower bound is positive.

**Corollary JGC26.C1 (the repository's full density gate).** Put
kappa_* = sqrt(275/14), s=2a. Then

\[
 \boxed{\mathcal B_{2a,a}(t)=B_{2a,\kappa_*}(t)>\frac{8a}{45}
                  \quad(a>0,\ t\ge0).}
\tag{1.5}
\]

This closes the *arithmetic density* gap, not the separate critical-boundary
intertwiner. The stronger sharpness assertion (1.3) concerns the continuous
density, not a claimed classification of arbitrary completed L-functions.

## 2. Three elementary source bounds

### 2.1 Zeta normalization

A decreasing integral comparison and a strictly convex trapezoidal comparison
for x^(-1-s) on [1,infinity) give

\[
 \frac1s+\frac12<\zeta(1+s)<\frac1s+1.
\]

Consequently

\[
 \frac1{1+s}<r_s<\frac2{2+s},\qquad
 c_s>\frac{s}{1+s}.
\tag{2.1}
\]

For the trapezoidal comparison, sum
int_n^(n+1) f < (f(n)+f(n+1))/2 and let the upper endpoint increase.
There is no analytic continuation input in (2.1).

### 2.2 Product association, proved at the needed scope

For the finite prime set consisting of all primes <=N, let independent exponents
have law P(E_p=k)=(1-1/p)p^(-k), and put M=prod p^(E_p).
Both F_s(M) and 1_(M<=N) are coordinatewise nonincreasing. For one random
variable X and two same-direction monotone bounded functions f,g,

\[
 \operatorname{Cov}(f(X),g(X))
 =\tfrac12\mathbb E[(f(X)-f(X'))(g(X)-g(X'))]\ge0,
\]

where X' is an independent copy. Conditioning on the last variable and
inducting proves association for a finite product. The same proof works with
a nonnegative decreasing bounded h(M) in place of the indicator.
The normalization of the geometric law cancels, giving

\[
 \sum_{n\le N}\frac{F_s(n)}n h(n)
 \ge \prod_{p\le N}(1-p^{-1-s})\sum_{n\le N}\frac{h(n)}n.
\tag{2.2}
\]

The finite product is strictly larger than c_s. For h not identically zero
on {1,...,N}, this yields a strict lower comparison with c_s times the sum.
The h=0 case is equality, not a strict inequality.

Write delta=1-log 2. The sequence H_N-log(N+1) is increasing from delta,
because 1/(N+1)>log(1+1/(N+1)). For N=floor(e^t), (2.2) implies

\[
 \boxed{E_{s,0}(t)>c_s\delta>0.}
\tag{2.3}
\]

At t=log n- take N=n-1; the same conclusion holds. The unit atom separately
implies

\[
 e(y)\ge1-r_sy,\qquad I(y)\ge y-r_sy^2/2.
\tag{2.4}
\]

We use only the elementary enclosures

\[
 2/3<\log2<25/36<7/10.
\tag{2.5}
\]

Indeed log2=2 sum_(j>=0) 3^(-2j-1)/(2j+1); bound all denominators in the tail
by 3 to get the stated upper bound. In particular delta>3/10.

### 2.3 Factorial to prime-power lower bound

Let A(x)=sum_(n<=x) Lambda(n)/n. The elementary identity

\[
 \log N!=\sum_{d\le N}\Lambda(d)\lfloor N/d\rfloor\le N A(N)
\]

and int_1^N log x dx <= log N! show

\[
 A(N)\ge\log N-1+1/N\ge\log(N+1)-1.
\]

The last inequality uses log(1+1/N)<=1/N. For every real x>=1,

\[
 \boxed{A(x)\ge\log x-1.}
\tag{2.6}
\]

For n=p^k the finite geometric inequality gives

\[
 F_s(n)=1-p^{-s}\ge(1-p^{-ks})/k
             =(1-n^{-s})\frac{\Lambda(n)}{\log n}.
\tag{2.7}
\]

For other n>1 the right side is zero and the same inequality holds. Thus it
is legitimate to retain the complete prime-power subsource and discard the
other nonnegative coefficients.

Set f_s(u)=(1-e^(-su))/u for u>0, extended by f_s(0)=s.
It is positive and decreasing: (1+su)e^(-su)<=1. Stieltjes integration by
parts, including the lower endpoint, gives

\[
 \begin{aligned}
 J_s(t)&=\sum_{2\le n\le e^t}\frac{\Lambda(n)}{n\log n}(1-n^{-s})\\
 &= f_s(t)A(e^t)-\int_0^t A(e^u)f_s'(u)du\\
 &\ge f_s(t)(t-1)-\int_0^t(u-1)f_s'(u)du\\
 &=\int_0^t f_s(u)du-s.
 \end{aligned}
\tag{2.8}
\]

There is no atom at u=0 in A(e^u). The right side is allowed to be negative;
that does not invalidate this lower bound. Define

\[
 \operatorname{Ein}(y)=\int_0^y\frac{1-e^{-v}}v\,dv.
\]

Combining (2.7), (2.8), and the unit atom yields the key new bound

\[
 \boxed{e(y)\ge1-s-r_sy+\operatorname{Ein}(y).}
\tag{2.9}
\]

This uses no PNT, verified zero prefix, stochastic independence of zeta zeros,
or conjectural prime correlation. It is uniform in s and y.

## 3. A finite polynomial lower envelope, used analytically

Taylor's formula with integral remainder gives, for every v>=0,

\[
 e^{-v}\le1-v+v^2/2-v^3/6+v^4/24.
\]

Therefore Ein(y)>=p(y), where

\[
 p(y)=y-y^2/4+y^3/18-y^4/96,
\quad
 j(y)=\int_0^y p(v)dv=y^2/2-y^3/12+y^4/72-y^5/480.
\tag{3.1}
\]

This is a polynomial inequality on a continuum, not interpolation of sampled
values. Integrate (2.9) to obtain

\[
 e(y)\ge1-s-r_sy+p(y),\quad
 I(y)\ge(1-s)y-r_sy^2/2+j(y).
\tag{3.2}
\]

Let

\[
 L_{s,r}(y)=2(1-s-ry+p(y))
       +2((1-s)y-ry^2/2+j(y))-2r.
\tag{3.3}
\]

Then b_2>=L_(s,r_s). The useful exact identities are

\[
 p(2)=23/18,\quad j(2)=67/45,\quad
 p''(y)=-5/18-(y-4/3)^2/8,
\]

\[
 p'(y)+p''(y)=1/2-y(y^2-y+4)/24\le1/2\quad(y\ge0).
\tag{3.4}
\]

Thus L''<=1-2r<0 whenever r>1/2. In particular it is strictly concave
in the whole range s<=2/3, by (2.1).
L decreases in r. Put barL_s=L_(s,2/(s+2)). For 0<=y<=2,

\[
 \partial_s\bar L_s(y)
 =-2(1+y)+\frac{2(y^2+2y+2)}{(s+2)^2}<0.
\tag{3.5}
\]

To see the sign without a numerical grid, note
3(y^2+2y+2)<=10(1+y), since (2-y)(3y+2)>=0, and (s+2)^2>=4.

## 4. Proof at the sharp coefficient 2

### 4.1 Small scales: 0<s<=1/2

For 0<=y<=s, (2.4) gives

\[
 b_2(y)\ge U_r(y):=2-2r+2(1-r)y-ry^2.
\]

U_r is concave. At both y=0 and y=s, replacement of r by 2/(s+2)
gives a lower bound 2s/(s+2)>=4s/5. Hence this holds on the entire interval.

For s<=y<=2, use the concavity of L_(s,r_s). At the left endpoint,

\[
 \bar L_s(s)=
 \frac{s(1440-2160s-1160s^2-30s^3-s^4-3s^5)}{720(s+2)}
 \ge\frac{47s}{1280}.
\tag{4.1}
\]

The numerator's bracket is decreasing and its value at 1/2 is 2115/32;
the denominator is at most 1800. At the right endpoint,

\[
 \bar L_s(2)=-\frac{90s^2+7s-46}{15(s+2)}\ge8/15,
\tag{4.2}
\]

by (3.5) and its exact value at s=1/2. These bound every interior point.

For y>=2, use e>0 and the monotonicity of I. From (3.2),

\[
 I(2)-r\ge157/45-2s-3r
 >157/45-2s-6/(s+2)\ge4/45.
\tag{4.3}
\]

The last expression decreases on [0,1/2]. Hence b_2(y)>8/45 there.
These three regions imply the first line of (1.4).

### 4.2 The connecting interval: 1/2<=s<=2/3

Now r<4/5 and e>c_s delta>1/10. On 0<=y<=19/20, use U_r and concavity.
Its endpoint bounds at r=4/5 are 2/5 and 29/500.

On 19/20<=y<=2, use L and (3.5). The exact worst endpoint values are

\[
 \bar L_{2/3}(19/20)=1068867/256000000>1/256,
 \qquad \bar L_{2/3}(2)=1/30.
\tag{4.4}
\]

Concavity controls the interval between them. For y>=2, use e>1/10 and (3.2):

\[
 b_2(y)>1/5+2(I(2)-r)
 >323/45-4s-12/(s+2)\ge1/90.
\tag{4.5}
\]

Again the last function decreases and its endpoint value at s=2/3 is 1/90.
All three regions have lower bound 1/256, proving the middle line of (1.4).

### 4.3 All larger scales: s>=2/3

Here r<3/4, c_s>2/5, and hence e>d=3/25 by (2.3). Retain both lower bounds

\[
 e(y)\ge\max(1-ry,d).
\]

Put y_*=(1-d)/r. For y<=y_* the integrated unit bound gives U_r(y);
its minimum is at an endpoint. At y=0 it exceeds 1/2. At y=y_* it equals

\[
 2d+(1-d^2)/r-2r
 >2(3/25)+(616/625)(4/3)-3/2
 =203/3750.
\tag{4.6}
\]

For y>=y_*, the integral of max(1-ry,d) increases linearly with slope d,
so its lower bound for b_2 increases. This proves the last line of (1.4).

### 4.4 Sharpness and the original margin

For kappa>=2,

\[
 b_\kappa=b_2+(\kappa-2)e\ge b_2>0.
\]

Conversely B_(s,kappa)(0)/s=kappa/2-r_s, and (2.1) squeezes r_s to 1 as
s decreases to zero. For kappa<2 this is negative for sufficiently small s;
continuity within the first open activation cell also gives negative t>0.
This proves (1.3).

For the stronger bound at kappa_*=sqrt(275/14), first suppose s<=1/2.
On 0<=y<=2 the lower envelope 1-s-ry+p(y) is concave. Its values at 0 and
2, using r<2/(s+2), are at least 1/2 and 8/45 respectively: the second
lower bound 1-s-4/(s+2)+23/18 decreases on [0,1/2]. Thus e>=8/45
throughout this interval. Therefore

\[
 B_{s,\kappa_*}(y/s)> (s/2)(\kappa_*-2)(8/45)>4s/45,
\]

since kappa_*>3. For y>=2, (4.3) and e>0 give B>4s/45.
For s>=1/2, use e>1/10 and b_2>0:

\[
 B_{s,\kappa_*}(t)>(\kappa_*-2)s/20>4s/45,
\]

because kappa_*>34/9. This proves (1.5), since s=2a.
Every radical comparison here is an elementary rational-square comparison.

## 5. Exact Laplace measure and polarized safe kernels

For Re q>0, absolute Euler products give

\[
 Z_s(q)=\frac{\zeta(1+q)}{\zeta(1+s+q)}
       =\sum_{n\ge1}\frac{F_s(n)}{n^{1+q}}.
\]

Define

\[
 \mathcal F_{s,\kappa}(q)=
 \frac{q^2+(\kappa s/2)q+s^2}{q^2}
 \left(Z_s(q)-\frac{c_s}{q}\right).
\tag{5.1}
\]

For E_2(t)=int_0^t(t-v)E_0(v)dv, the endpoint values are
E_2(0)=E_2'(0)=0 and E_2''(0+)=1. On the OPEN half-line,

\[
 E_2'''=-c_sdt+\sum_{n\ge2}(F_s(n)/n)\delta_{\log n}.
\]

Laplace integration by parts, or separate finite Fubini in each source term,
therefore gives

\[
 \boxed{\mathcal F_{s,\kappa}(q)
 =1+\sum_{n\ge2}\frac{F_s(n)}n n^{-q}
       +\int_0^\infty e^{-qt}B_{s,\kappa}(t)dt.}
\tag{5.2}
\]

The constant 1 is the unit contact, not an omitted integration constant.
Since F_s<=1, the density has at most quadratic growth, ensuring convergence
and differentiation at every Re q>0. In fact the positivity and harmonic
upper bound suffice for all polynomially weighted Laplace integrals.

**Theorem JGC26.T2.** For s>0 and kappa>=2, (5.2) is a positive Laplace
representation. Thus all derivatives have alternating signs on q>0 and
for every finite complex packet Re z_i>0,

\[
 [\mathcal F_{s,\kappa}(z_i+\overline{z_j})]_{i,j}\succeq0.
\]

For kappa=kappa_* one has the fully polarized quantitative comparison

\[
 [\mathcal F_{s,\kappa_*}(z_i+\overline{z_j})]
 \succeq\frac{4s}{45}[1/(z_i+\overline{z_j})].
\tag{5.3}
\]

It follows by integrating |sum c_i exp(-z_i t)|^2 against the complete positive
measure. Distinct exponentials are linearly independent, so distinct nodes
give positive definite matrices. The same integral proves the confluent
jet versions with polynomial-exponential test functions. This conclusion is
in the safe Laplace half-plane, not the critical Xi Pick cone.

## 6. A corrected all-scale positive gamma completion

The repository's separate rational factor

\[
 R_s(q)=\frac{q+1}{(q+s)(q+s+1)}
\]

need not be completely monotone for s>1: its inverse density is
exp(-st)(1-s+s exp(-t)), which is eventually negative. Accordingly we do
NOT multiply two individually asserted positive factors outside their range.
Instead group it with the gamma ratio BEFORE taking the inverse transform.
The gamma recurrence gives exactly

\[
 A_s(q):=R_s(q)\pi^{s/2}
 \frac{\Gamma((q+1)/2)}{\Gamma((q+s+1)/2)}
 =\frac{\pi^{s/2}}{q+s}
 \frac{\Gamma((q+3)/2)}{\Gamma((q+s+3)/2)}.
\tag{6.1}
\]

Euler's beta integral represents the last gamma quotient by the positive
locally integrable density

\[
 \beta_s(t)=\frac{2\pi^{s/2}}{\Gamma(s/2)}
 e^{-3t}(1-e^{-2t})^{s/2-1},\qquad t>0.
\tag{6.2}
\]

Thus A_s is the Laplace transform of exp(-s t)*beta_s, for EVERY s>0.
Both factors are integrable. This elementary regrouping is necessary for the
all-scale claim; at s=2 the product reduces to 2pi/((q+2)(q+3)).

Let s=2a and

\[
 g_a=(te^{-at})*(te^{-2at})*(te^{-4at}),\quad
 d\omega_a=\delta_0+\sum_{n\ge2}(F_{2a}(n)/n)\delta_{\log n}
                         +B_{2a,\kappa_*}(t)dt.
\]

**Corollary JGC26.C2.** The exact transfer of old L-91031 is now an explicitly
positive Laplace transform at every a>0:

\[
 \mathcal S_a(q)=
 \frac{A_{2a}(q)\mathcal F_{2a,\kappa_*}(q)}
 {(q+a)^2(q+2a)^2(q+4a)^2}
 =\int_0^\infty e^{-qt}d\mu_a(t),
\]

\[
 \mu_a=(e^{-2at}dt)*\beta_{2a}(t)dt*g_a(t)dt*\omega_a\ge0.
\tag{6.3}
\]

Products mean convolution of measures/densities as indicated, not products of
pointwise values. Every finite-rank safe kernel of S_a is PSD. The full
critical-boundary identification is not a consequence of (6.3).

## 7. Proof and execution boundary

Sections 2--4 are the new unbounded proof. The exact checker verifies the
polynomial reductions, rational margins, finite divisor identities and
synthetic controls; it does not extrapolate from samples. Section 6 uses the
classical gamma recurrence and Euler beta integral, with their positive
real-part hypotheses explicit. See REAL_AXIS.md for a separate resolution
of the mean inequality in PR #440, and RH_ATTEMPT.md for the attempted
end-to-end transfer and its unresolved step. No literature-priority claim or
independent referee acceptance is made.
