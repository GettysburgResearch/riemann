# L-32302 — A critical-mode-null dyadic source with positive inverse and compact factor-eight carry image

Claim ID: `L-32302`  
Title: Three dyadic zeros simultaneously remove the constant floor tail, the affine carry tail, and the real square-root critical mode without cancelling any off-line zeta zero  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: the affine Möbius carry contraction of PR #243/#246  
Scope: exact source/filter/carry algebra; no RH conclusion

## 1. The source polynomial

Put

\[
x=2^{-s}
\]

and define

\[
\boxed{
P_\dagger(x)=(1-x)(1-x/2)(1-\sqrt2\,x).
}
\tag{L-32302.1}
\]

Expanding,

\[
P_\dagger(x)
=1-\left({3\over2}+\sqrt2\right)x
 +\left({1\over2}+{3\sqrt2\over2}\right)x^2
 -{\sqrt2\over2}x^3.
\tag{L-32302.2}
\]

Define the Dirichlet source

\[
\boxed{
\omega_\dagger
=\mu-\left({3\over2}+\sqrt2\right)\delta_2*\mu
 +\left({1\over2}+{3\sqrt2\over2}\right)\delta_4*\mu
 -{\sqrt2\over2}\delta_8*\mu.
}
\tag{L-32302.3}
\]

Its Dirichlet series is

\[
\boxed{
\Omega_\dagger(s)
={P_\dagger(2^{-s})\over\zeta(s)}.
}
\tag{L-32302.4}
\]

The three roots have three distinct jobs:

```text
P_dagger(1)=0          constant floor-tail cancellation;
P_dagger(2)=0          affine carry-tail cancellation;
P_dagger(2^-1/2)=0     square-root critical-mode cancellation.
```

## 2. No off-line zeta zero is cancelled

The zeros of `P_dagger(2^-s)` occur only when

\[
2^{-s}\in\{1,2,2^{-1/2}\}.
\]

Their real parts are respectively

\[
0,-1,{1\over2}.
\]

Therefore

\[
\boxed{
P_\dagger(2^{-\rho})\ne0
\quad\text{for every }\rho\text{ with }\Re\rho>{1\over2}.
}
\tag{L-32302.5}
\]

Any hypothetical off-line zeta zero remains an uncancelled pole of `Omega_dagger`.

## 3. Strictly positive Dirichlet inverse

The inverse series is

\[
A_\dagger(s)
={\zeta(s)\over
 (1-2^{-s})(1-2^{-s-1})(1-\sqrt2\,2^{-s})}.
\tag{L-32302.6}
\]

Write

\[
{1\over(1-x)(1-x/2)(1-\sqrt2 x)}
=\sum_{r\ge0}d_r x^r.
\]

Every coefficient is strictly positive because

\[
d_r=\sum_{i+j+k=r}2^{-j}2^{k/2}>0.
\tag{L-32302.7}
\]

Convolution with `zeta` gives the explicit inverse coefficient

\[
\boxed{
a_\dagger(n)=\sum_{0\le r\le v_2(n)}d_r>0.
}
\tag{L-32302.8}
\]

Thus the exact inverse is coefficientwise positive.

## 4. Positive generalized-prime sequence

Logarithmic differentiation of (L-32302.6) gives

\[
\boxed{
\Lambda_\dagger(n)
=\Lambda(n)
 +(\log2)\left(1+2^{-r}+2^{r/2}\right)
 \mathbf1_{n=2^r},
\qquad r\ge1.
}
\tag{L-32302.9}
\]

Hence

\[
\Lambda_\dagger(n)\ge0.
\]

The generalized Selberg identity therefore has the same positive quadratic forcing orientation as the previously audited Euler-aligned sources:

\[
\omega_\dagger*(a_\dagger\log^2)
=\Lambda_\dagger\log
 +\Lambda_\dagger*\Lambda_\dagger.
\tag{L-32302.10}
\]

## 5. Compact pointwise carry wavelet

The elementary identity

\[
\sum_{k\le y}\mu(k)\left\lfloor{y\over k}\right\rfloor
=\mathbf1_{y\ge1}
\]

shows that the source-contracted floor primitive at scale `m` is

\[
\boxed{
 g_m(y)=
 \mathbf1_{m\le y<2m}
 -\left({1\over2}+\sqrt2\right)\mathbf1_{2m\le y<4m}
 +{\sqrt2\over2}\mathbf1_{4m\le y<8m}.
}
\tag{L-32302.11}
\]

It vanishes identically for `y>=8m`.

For the pointwise carry indicator,

\[
\boxed{
Z_{n,m}(j)
=\sum_{k\le n/m}\omega_\dagger(k)\chi_{n,mk}(j)
=g_m(n)-g_m(j)-g_m(n-j).
}
\tag{L-32302.12}
\]

Thus the complete source has a literal compact factor-eight carry image.  No tail is discarded.

## 6. Averaged carry image is supported only on rows 2 through 7

Use the exact affine Möbius contraction

\[
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
={2m-n-1\over n+1}.
\tag{L-32302.13}
\]

For `n>=8`, all four dyadic source taps are active.  Because

\[
P_\dagger(1)=0
\quad\text{and}\quad
P_\dagger(2)=0,
\]

both the `n` coefficient and the constant coefficient cancel, giving

\[
\boxed{
\sum_{q=2}^n\omega_\dagger(q)\beta_{nq}=0
\qquad(n\ge8).
}
\tag{L-32302.14}
\]

The complete nonzero table is

\[
\boxed{
\begin{array}{c|c}
n & \displaystyle\sum_{q=2}^n\omega_\dagger(q)\beta_{nq}\\ \hline
2 & -{5\over6}-{\sqrt2\over3}\\[1mm]
3 & -{1\over2}\\[1mm]
4 & {11\sqrt2\over10}\\[1mm]
5 & {5\sqrt2\over6}\\[1mm]
6 & {9\sqrt2\over14}\\[1mm]
7 & {\sqrt2\over2}\\[1mm]
n\ge8 & 0.
\end{array}}
\tag{L-32302.15}
\]

Every value follows by substituting `m=1,2,4,8` into (L-32302.13), retaining only active taps.

## 7. Interpretation

This source combines three features which had previously appeared on separate branches:

```text
positive Dirichlet inverse and generalized primes;
finite carry localization;
annihilation of the real square-root critical scaling mode.
```

The price is that the six surviving bottom rows have mixed sign.  No sign conclusion for their target pairing is asserted here.

## 8. Proof boundary

Closed exactly:

- source polynomial and transform;
- noncancellation of every off-line zeta zero;
- positive inverse coefficients;
- positive generalized-prime coefficients;
- generalized Selberg identity;
- compact factor-eight pointwise wavelet;
- exact six-row averaged carry table;
- vanishing of every averaged row `n>=8`.

Open:

- a one-sign or subpower estimate for the associated Riesz coordinate;
- a source-specific physical/carry reserve using this critical-null filter;
- RH.
