# A lower global SHARP power threshold, with exact arithmetic

Status: **PROPOSED global theorem; arithmetic certificate independently checked
within this packet, external mathematical review still required.**

Scope: the literal beta source and SHARP boundary kernel, for every real
endpoint x>=1. This lowers a sufficient supercritical exponent. It does not
prove the critical exponent m=1, an RH conclusion, or novelty relative to
work outside the inspected repository.

Exact sources: reviewed definitions and the labelled Euler-removal argument
in `research/integrated/CURRENT_RESULTS.md`, section 2; frozen source
`fa081e81044a81e76f48cb9878a659d749e98427`, claim L-99613; the independently
resident analogous activation-zero proof in
`claims/lemmas/L-99930-activation-zero-supercritical-positivity.md`.
The empty-level correction in the current guide is retained explicitly.
The exact numerical enclosure below uses the Euler--Maclaurin formula and
the Fourier expansion of the periodic Bernoulli polynomial, with their
remainder contracts written below.

What was actually run: see `EXECUTION.json`, including normal and optimized
execution and independent controls. No ordinary floating-point value enters
the finite acceptance test.

Smallest remaining gap toward critical positivity: the elementary pairing
argument stops above 1.80206853772. A bound for the critical signed source
or an additional cancellation theorem is still needed.

## 1. The exact threshold of the retained pairing argument

Write

\[
 P(\alpha)=\sum_{p\ \mathrm{prime}}p^{-\alpha},\qquad
 V(\alpha)=P(\alpha)+67^{-\alpha},\qquad \alpha>1.
\]

The extra term is a second **labelled** copy of 67, not another distinct
prime. V is continuous and strictly decreasing. The certificate proves

\[
 V(1.40103426886)>1>V(1.40103426887).
 \tag{P1}
\]

Therefore exactly one alpha_* lies between these endpoints with
V(alpha_*)=1. Put m_*=2 alpha_*-1. The bracket is

\[
 1.80206853772<m_*<1.80206853774.
 \tag{P2}
\]

**Proposed theorem A-SP1.** For beta(n)=mu(n)-1_(67|n) mu(n/67),
T(y)=(4sqrt(y)-3)1_(y>=1), and every real m>=m_*,

\[
 H_m(x):=\sum_{n\le x}{\beta(n)\over\sqrt n}T(x/n)^m>0
 \quad\text{for every real }x\ge1.
 \tag{P3}
\]

In particular the explicit rational exponent **1.80206853774**, and the
simpler exponent **1.80207**, are valid sufficient lower thresholds.

### Full proof, including the threshold endpoint and empty levels

For a finite subset A of prime labels, including the two distinct labels
at 67, let n_A be their product and put

\[
 w_m(A)=n_A^{-1/2}T(x/n_A)^m\mathbf1_{n_A\le x},
 \qquad M_k=\sum_{|A|=k}w_m(A).
\]

Only finitely many labels and subsets can be active for fixed x. Projection
of the signs (-1)^|A| gives exactly beta(n), including the coefficients
(1,-2,1) on powers of 67.

If A is active and q is one of its labels, B=A\{q} is active. With y=x/n_A>=1,

\[
 T(qy)-\sqrt q T(y)=3(\sqrt q-1)>0,
\]

and hence

\[
 w_m(A)<q^{-(m+1)/2}w_m(B).
 \tag{P4}
\]

For k>=1, sum over the k possible removals from each active k-subset. A
fixed (k-1)-subset can be extended only by labels q<=x. Consequently

\[
 kM_k\le V_x(\alpha)M_{k-1},\quad
 V_x(\alpha):=\sum_{p\le x}p^{-\alpha}
                   +\mathbf1_{67\le x}67^{-\alpha},
 \quad\alpha=(m+1)/2.
 \tag{P5}
\]

The non-strict form is valid even when one or both levels are empty. Since
V_x(alpha)<V(alpha)<=1, (P5) gives M_(2j+1)<=M_(2j) for every j and gives
M_1<M_0, because M_0=T(x)^m>0. Pair the finite alternating sum, taking all
higher missing levels to be zero. Every pair is nonnegative and the first
is strictly positive. This proves (P3), including m=m_*. QED.

For m>m_* the same proof supplies a quantitative lower bound

\[
 H_m(x)\ge[1-V((m+1)/2)]T(x)^m.
 \tag{P6}
\]

At the exact threshold one instead has the positive finite-horizon bound
[1-V_x(alpha_*)]T(x)^m. A fixed positive lower coefficient independent of x
is not asserted at that endpoint.

## 2. The exact certificate's analytic contracts

The checker uses dyadic outward rounding at 180 bits. Every arithmetic
endpoint is a rational number, and negative rational endpoints are rounded
with floor/ceiling, never by truncation toward zero.

For 1<=v<=2 put z=(v-1)/(v+1)<=1/3. The logarithm series satisfies

\[
 0\le\log v-2\sum_{j=0}^{J-1}{z^{2j+1}\over2j+1}
 \le {2z^{2J+1}\over(2J+1)(1-z^2)}.
 \tag{P7}
\]

Binary reduction handles any positive rational. To bound exp(-t), divide
t>=0 by a power of two until it lies in [0,1/4]. The alternating Taylor
partial sum through an even order is an upper bound; adding the next
negative term is a lower bound. Directed interval squaring reverses the
range reduction. These contracts bound n^(-s) for every positive rational
s, without computing enormous-degree integer roots.

For real s>1 and integers N>=1, K>=1, Euler--Maclaurin gives

\[
 \zeta(s)=\sum_{n=1}^{N-1}n^{-s}
   +{N^{1-s}\over s-1}+\frac12N^{-s}
   +\sum_{k=1}^{K}{B_{2k}\over(2k)!}(s)_{2k-1}N^{-s-2k+1}+R_K,
\]

where (s)_j=s(s+1)...(s+j-1), and

\[
 |R_K|\le {|B_{2K}|\over(2K)!}(s)_{2K-1}N^{-s-2K+1}.
 \tag{P8}
\]

Indeed, the integral remainder contains B_(2K)({t})(s)_(2K)t^(-s-2K)/(2K)!.
The Fourier expansion of the even periodic Bernoulli polynomial gives
|B_(2K)({t})|<=|B_(2K)|. Integrating the positive majorant from N to infinity
cancels the last rising-factorial term s+2K-1 and proves (P8). Thus the
bound does not assume an unproved alternating property of the asymptotic
Euler--Maclaurin expansion. The checker uses N=64 and K=14.

Absolutely convergent Euler-product expansion and Möbius inversion give

\[
 P(s)=\sum_{k\ge1}{\mu(k)\over k}\log\zeta(ks),\qquad s>1.
 \tag{P9}
\]

For completeness, log zeta(ks)=sum_p sum_j p^(-kjs)/j. The coefficient of
p^(-rs) in the right side is (1/r) sum_(k|r) mu(k), which is one for r=1
and zero otherwise. Absolute convergence justifies regrouping.

After k=K0, the absolute omitted contribution is at most

\[
 {2^{-(K_0+1)s}\over K_0+1}
 {1+2/((K_0+1)s-1)\over1-2^{-s}}.
 \tag{P10}
\]

To prove this, use log zeta(t)<=zeta(t)-1 and the decreasing-integral bound
zeta(t)-1<=2^(-t)[1+2/(t-1)]. Replace 1/k and the bracket by their maxima
at k=K0+1, and sum the remaining powers geometrically. The checker uses
K0=80 and then adds the independently enclosed 67^(-s).

Equations (P7)--(P10), outward rational operations, and the two strict
comparisons in (P1) comprise the finite acceptance rule. A high-precision
decimal reconnaissance located the bracket, but is not part of acceptance.

## 3. Every fixed power above one is eventually positive, effectively

This observation complements the global threshold rather than extending it
to all endpoints near the critical power.

**Proposed lemma A-SP2.** Fix a real 1<m<2 and put a=(m+1)/2,

\[
 B(a)={1-67^{-a}\over\zeta(a)},\qquad
 E(m)={3m\over2-m}+2+{4\over m-1}.
\]

For every real x>=1,

\[
 H_m(x)\ge4^m\left[B(a)x^{m/2}-E(m)\sqrt x\right].
 \tag{P11}
\]

Thus H_m(x)>0 whenever

\[
 x>\left({E(m)\over B(a)}\right)^{2/(m-1)}.
 \tag{P12}
\]

An entirely explicit sufficient horizon, involving no evaluated zeta value,
is

\[
 x>\left[\frac{67(m+1)E(m)}{66(m-1)}\right]^{2/(m-1)}.
 \tag{P13}
\]

**Proof.** The absolutely convergent beta series at a has sum B(a). Write
T(x/n)^m=4^m(x/n)^(m/2)(1-3sqrt(n)/(4sqrt(x)))^m for n<=x.
For 0<=z<=3/4 and m>=1, Bernoulli's inequality gives
0<=1-(1-z)^m<=mz. Since |beta(n)|<=2, the difference between the truncated
weighted sum and its unmodified prefix is bounded by

\[
 {3m\over2\sqrt x}\sum_{n\le x}n^{-m/2}
 \le {3m\over2-m}x^{(1-m)/2}.
\]

Here sum_(n<=x) n^(-m/2)<=x^(1-m/2)/(1-m/2), by the decreasing-integral
bound. For noninteger x, the tail also satisfies the uniform safe bound

\[
 \sum_{n>x}n^{-a}\le x^{-a}+{x^{1-a}\over a-1}.
\]

Multiply the prefix and tail errors by 4^m x^(m/2). The tail's x^(-1/2)
term is at most sqrt(x), giving exactly E(m) in (P11). Finally
zeta(a)<=a/(a-1), while 1-67^(-a)>=66/67, so
B(a)>=(66/67)(m-1)/(m+1). This proves (P13). QED.

If delta=m-1 decreases to zero, the logarithm of the sufficient horizon
in (P13) is

\[
 \frac4\delta\log(1/\delta)+O(1/\delta).
 \tag{P14}
\]

The exploding horizon is the obstruction to taking the critical limit.
For any fixed x, H_m(x) is continuous in m, so a hypothetical negative
critical value would persist for m sufficiently close to one at that
fixed x. It is fully compatible with (P12), whose starting point escapes
to infinity. Fixed-m tail positivity is not a uniform critical-power proof.
