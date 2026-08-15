# L-93250 — A mean-zero Bernoulli projection of the centered Q4 field is one zero-safe cubic Riesz sum

Claim ID: `L-93250`  
Status: **PROPOSED COMPLETE EXACT FINITE/ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Frozen sources: PR #483 at `87bd7ad2127f98b6141b4c03355556f2b95f6404`; PR #474 at `0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b` for comparison only  
Scope: the complete actual compact-Q4 endpoint source and one fixed centered linear projection; no prime-correlation estimate and no RH conclusion in this lemma

## 1. Complete actual endpoint field

Retain the compact-Q4 coefficient

\[
 c_\circ(m)
 =\Lambda(m)
 -4\mathbf 1_{4\mid m}\Lambda(m/4)
 +3(\log4)\sum_{r\ge1}\mathbf 1_{m=4^r},
\tag{L-93250.1}
\]

its prefix

\[
 C_\circ(x)=\sum_{m\le x}c_\circ(m),
 \qquad C_\circ(0)=0,
\tag{L-93250.2}
\]

and, for an integer endpoint \(N\ge2\), the piecewise-constant field

\[
 Q_{\circ,N}(\theta)
 =C_\circ(N)
  -C_\circ(\lfloor N\theta\rfloor)
  -C_\circ(\lfloor N(1-\theta)\rfloor),
 \qquad 0<\theta<1.
\tag{L-93250.3}
\]

On the open cell \(j/N<\theta<(j+1)/N\),

\[
 Q_{\circ,N}(\theta)=R_N(j)
 =C_\circ(N)-C_\circ(j)-C_\circ(N-j-1).
\tag{L-93250.4}
\]

The predecessor \(N-j-1\), rather than \(N-j\), is load bearing.

Put

\[
 M_N=\int_0^1Q_{\circ,N}(\theta)\,d\theta
     ={1\over N}\sum_{j=0}^{N-1}R_N(j)
\tag{L-93250.5}
\]

and define the centered endpoint energy

\[
 \boxed{
 \mathscr V_\circ(N)
 ={1\over N}\int_0^1
   |Q_{\circ,N}(\theta)-M_N|^2\,d\theta
 ={1\over N^2}\sum_{j=0}^{N-1}|R_N(j)-M_N|^2.
 }
\tag{L-93250.6}
\]

This is the variance component of the complete endpoint PIG, with the same normalization as PR #483.

## 2. The fixed Bernoulli weight

Let

\[
 w(\theta)=\theta(1-\theta)-{1\over6}.
\tag{L-93250.7}
\]

Then exactly

\[
 w(1-\theta)=w(\theta),
 \qquad
 \int_0^1w(\theta)\,d\theta=0,
 \qquad
 \int_0^1w(\theta)^2\,d\theta={1\over180}.
\tag{L-93250.8}
\]

Equivalently, \(w=-B_2\) on \([0,1]\), where \(B_2(x)=x^2-x+1/6\) is the second Bernoulli polynomial. Its periodic Fourier series is

\[
 w(\theta)
 =-{1\over\pi^2}\sum_{a\ge1}{\cos(2\pi a\theta)\over a^2}.
\tag{L-93250.9}
\]

Thus this is one fixed inverse-circle-Laplacian projection using no zero frequency.

Define

\[
 \mathcal A_\circ(N)
 =\int_0^1w(\theta)Q_{\circ,N}(\theta)\,d\theta.
\tag{L-93250.10}
\]

Because \(w\) has mean zero,

\[
 \mathcal A_\circ(N)
 =\int_0^1w(\theta)
   [Q_{\circ,N}(\theta)-M_N]d\theta.
\tag{L-93250.11}
\]

Cauchy--Schwarz and (L-93250.8) give the exact normalization bridge

\[
 \boxed{
 |\mathcal A_\circ(N)|^2
 \le {N\over180}\,\mathscr V_\circ(N).
 }
\tag{L-93250.12}
\]

No endpoint mean, global block recurrence, QIDR measure, or factor-67 object occurs in this inequality.

## 3. Exact cubic Riesz kernel

Put

\[
 K(x)=2\int_0^xw(u)\,du
 ={x(1-x)(2x-1)\over3}.
\tag{L-93250.13}
\]

Then

\[
 K(0)=K(1)=0,
 \qquad
 K(1-x)=-K(x),
 \qquad
 K'(x)=2w(x).
\tag{L-93250.14}
\]

The exact extrema are

\[
 \max_{0\le x\le1}|K(x)|={\sqrt3\over54},
 \qquad
 \max_{0\le x\le1}K(x)^2={1\over972}.
\tag{L-93250.15}
\]

Indeed, with \(y=2x-1\) and \(t=y^2\),

\[
 K(x)={y(1-y^2)\over12},
 \qquad
 4-27t(1-t)^2=(3t-1)^2(4-3t)\ge0
\]

for \(0\le t\le1\), with equality at \(t=1/3\).

The projection (L-93250.10) is exactly the finite Riesz sum

\[
 \boxed{
 \mathcal A_\circ(N)
 =\sum_{m\le N}c_\circ(m)K(m/N).
 }
\tag{L-93250.16}
\]

The endpoint term \(m=N\) vanishes because \(K(1)=0\).

### Proof

The constant prefix \(C_\circ(N)\) disappears against \(\int w=0\). Symmetry of \(w\) makes the two moving-prefix integrals equal, so

\[
 \mathcal A_\circ(N)
 =-2\int_0^1w(\theta)
      C_\circ(\lfloor N\theta\rfloor)d\theta.
\]

Reverse the finite prefix sum:

\[
 C_\circ(\lfloor N\theta\rfloor)
 =\sum_{m<N}c_\circ(m)\mathbf1_{\theta\ge m/N}.
\]

Since \(\int_0^1w=0\),

\[
 -2\int_{m/N}^1w(\theta)d\theta
 =2\int_0^{m/N}w(\theta)d\theta
 =K(m/N).
\]

This proves (L-93250.16). \(\square\)

## 4. Mellin multiplier

For \(\Re s>-1\),

\[
 \boxed{
 \widehat K(s)
 :=\int_0^1K(x)x^{s-1}dx
 ={s-1\over3(s+1)(s+2)(s+3)}.
 }
\tag{L-93250.17}
\]

In particular, \(\widehat K\) has no zero in the open critical strip.

For real \(X\ge1\), define

\[
 \mathcal A_\circ(X)
 =\sum_{m\le X}c_\circ(m)K(m/X).
\tag{L-93250.18}
\]

For \(\Re s>1\), absolute convergence and the substitution \(x=m/X\) give

\[
 \boxed{
 \begin{aligned}
 \int_1^\infty
 \mathcal A_\circ(X)X^{-s-1}dX
 ={}&{s-1\over3(s+1)(s+2)(s+3)}\\
 &\times\left[
 (1-4^{1-s})\left(-{\zeta'\over\zeta}(s)\right)
 +3(\log4){4^{-s}\over1-4^{-s}}
 \right].
 \end{aligned}
 }
\tag{L-93250.19}
\]

At every nontrivial zero \(\rho\) with \(0<\Re\rho<1\), all of

\[
 \rho-1,
 \quad
 1-4^{1-\rho},
 \quad
 1-4^{-\rho},
 \quad
 (\rho+1)(\rho+2)(\rho+3)
\]

are nonzero. The four-adic term is holomorphic there, while
\(-\zeta'/\zeta\) has a nonremovable pole. Thus every open-strip zeta zero survives in (L-93250.19).

## 5. Integer-to-real interpolation

The elementary Chebyshev estimate implies

\[
 \sum_{m\le N}m|c_\circ(m)|\le C_0N^2
\tag{L-93250.20}
\]

for one absolute constant. Since

\[
 \max_{0\le x\le1}|K'(x)|\le{1\over3},
\tag{L-93250.21}
\]

if \(N\le X<N+1\), then

\[
 \boxed{
 |\mathcal A_\circ(X)-\mathcal A_\circ(N)|\le C_1
 }
\tag{L-93250.22}
\]

with one absolute constant. Indeed each kernel value moves by at most
\(m|X-N|/(3N^2)\), and the possible new endpoint is already covered by
\(K(1)=0\) and the same derivative bound.

Therefore every integer endpoint power or power-log estimate for
\(\mathcal A_\circ(N)\) extends to all real \(X\) with the same exponent.

## 6. Heat/resolvent interpretation

The weight \(w=-B_2\) is the mean-zero inverse-Laplacian Green profile on the circle. If

\[
 H_t(\theta)=1+2\sum_{a\ge1}
 e^{-4\pi^2a^2t}\cos(2\pi a\theta)
\]

is the periodic heat kernel, then

\[
 w(\theta)
 =-2\int_0^\infty[H_t(\theta)-1]dt.
\tag{L-93250.23}
\]

Thus the Q4 field has one canonical **integrated heat projection** whose arithmetic side is the cubic Riesz sum (L-93250.16). This is the exact structural bridge to the First-Hermite heat programme: both routes can be phrased as one-dimensional prime-block coherence after a heat/resolvent normalization, although their arithmetic windows remain different.

## 7. Proof boundary

Established natively:

1. the mean-zero symmetric Bernoulli weight and its exact norm;
2. the centered-energy Cauchy bridge;
3. the exact cubic Riesz kernel;
4. the zero-safe rational Mellin multiplier;
5. the complete compact-Q4 Mellin transform;
6. endpoint interpolation;
7. the inverse-Laplacian / integrated-heat interpretation.

Not established here:

1. a square-root bound for \(\mathcal A_\circ\);
2. a polylogarithmic bound for centered Q4 energy;
3. deterministic prime-block decorrelation;
4. RH.
