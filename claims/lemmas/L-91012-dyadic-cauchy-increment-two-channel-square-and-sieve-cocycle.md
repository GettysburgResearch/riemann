# L-91012 — The dyadic Cauchy-count increment is a two-channel square aligned with a positive sieve cocycle

Claim ID: `L-91012`  
Status: **EXACT SPECTRAL/ARITHMETIC LEMMA**  
Created: 2026-08-11  
Depends on: `L-91008`, `L-91011`  
RH status: **unproved**

## 1. Exact two-channel square

For one critical-line coordinate \(u\), put

\[
 n_a(u)=\frac{a^4}{(a^2+u^2)^2}.
\]

The dyadic increment has the exact factorization

\[
\boxed{
\begin{aligned}
 n_{2a}(u)-n_a(u)
 &={3a^4u^2(8a^2+5u^2)
 \over (a^2+u^2)^2(4a^2+u^2)^2}\\
 &=|g_{1,a}(u)|^2+|g_{2,a}(u)|^2,
\end{aligned}}
\tag{L-91012.1}
\]

where

\[
\boxed{
 g_{1,a}(u)
 ={2\sqrt6\,a^3u
 \over(a^2+u^2)(4a^2+u^2)},
 \qquad
 g_{2,a}(u)
 ={\sqrt{15}\,a^2u^2
 \over(a^2+u^2)(4a^2+u^2)}.
}
\tag{L-91012.2}
\]

Thus the dyadic increment of the soft zero count is a literal two-channel
spectral square on the critical line. The channels are rational Cauchy filters
with poles only at \(\pm ia,\pm2ia\).

Under RH,

\[
 \mathcal N_x(2a)-\mathcal N_x(a)
 =
 \sum_\gamma m_\gamma
 \left(
 |g_{1,a}(\gamma-x)|^2
 +|g_{2,a}(\gamma-x)|^2
 \right)\ge0.
 \tag{L-91012.3}
\]

For a reflected pair the same two channels are evaluated at the complex
centred coordinate and form the corresponding indefinite hyperbolic block.

## 2. Normalized positive sieve flow

Shift the generalized-Jordan ratio of `L-91011` to define

\[
 \boxed{
 Q_a(s)
 =\mathcal J_a(s+a)
 =\frac{\zeta(s)}{\zeta(s+2a)}.
 }
 \tag{L-91012.4}
\]

For \(\Re s>1\),

\[
 \boxed{
 Q_a(s)
 =\sum_{n\ge1}{q_a(n)\over n^s},
 \qquad
 q_a(n)=\prod_{p\mid n}(1-p^{-2a})\in(0,1].
 }
 \tag{L-91012.5}
\]

This family satisfies the positive cocycle

\[
 \boxed{
 Q_{a+b}(s)=Q_a(s)Q_b(s+2a),
 }
 \tag{L-91012.6}
\]

and therefore

\[
 \boxed{
 q_{a+b}(n)
 =\sum_{de=n}q_a(d)q_b(e)e^{-2a}.
 }
 \tag{L-91012.7}
\]

Every term is nonnegative. At \(a=1/2\),

\[
 q_{1/2}(n)={\varphi(n)\over n}.
 \tag{L-91012.8}
\]

## 3. The soft count is the logarithmic curvature of the sieve flow

Let

\[
 F_x(\alpha)=\Re\log Q_\alpha(s_x),
\]

under analytic continuation from the absolute half-plane. The zeta part of

\[
 p_x(a)=\Re{\xi'\over\xi}(s_x+a)
\]

satisfies

\[
 p_{x,\zeta}(a)
 =-\frac12F_x'(a/2).
 \tag{L-91012.9}
\]

Consequently its contribution to the soft count is

\[
 \boxed{
 \mathcal N_{x,\zeta}(a)
 =-{a\over4}F_x'(a/2)
 +{a^2\over8}F_x''(a/2).
 }
 \tag{L-91012.10}
\]

The pole and gamma factors in `L-91011.8` supply the explicit archimedean
completion.

Thus the dyadic Cauchy gate compares logarithmic curvatures of the positive
sieve flow at the two adjacent parameters \(a/2\) and \(a\). The cocycle
(L-91012.6) is precisely adapted to the dilation \(a\mapsto2a\).

## 4. Frontier

The two-channel square closes the zero-side geometry and the positive sieve
cocycle closes the source typing. What remains open is the continuation of the
resulting Hermitian inequality from \(\Re s>1\) to the completed critical
boundary.

No coefficientwise or scalar absolute-value estimate is asserted to perform
that continuation.
