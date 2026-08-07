# L-20813 — Triangular retained-power convolution

Claim ID: `L-20813`  
Title: The finite Euler cutoff defect is paid exactly by the local collision square, leaving a wholly positive retained-power convolution  
Status: `PROPOSED — COMPLETE POSITIVE RECOMBINATION OF L-20812`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Dependencies: `L-20812`  
Scope: remove the apparent negative channel from the shrinking-strip Euler flow  
Related counterexample candidates: none

## 1. Exact triangular identity

Retain the notation

\[
 a=\log p,
 \qquad r=p^{-(1/2+u)},
 \qquad
 P_{p,K}=a\sum_{k=1}^Kr^k,
 \tag{L-20813.1}
\]

and the cutoff defect `E_(p,K)` of `L-20812`. Then

\[
 \boxed{
 P_{p,K}^2-E_{p,K}
 =a^2\sum_{\ell=2}^K(\ell-1)r^\ell
 \ge0.}
 \tag{L-20813.2}
\]

Equivalently,

\[
 \boxed{
 P_{p,K}^2-E_{p,K}
 =a^2\sum_{\substack{m,n\ge1\\m+n\le K}}r^{m+n}.}
 \tag{L-20813.3}
\]

### Proof

The square expands as

\[
 P_{p,K}^2
 =a^2\sum_{m=1}^K\sum_{n=1}^Kr^{m+n}.
 \tag{L-20813.4}
\]

For a fixed total exponent `ell<=K`, there are exactly `ell-1` ordered pairs
`(m,n)` with `m,n>=1` and `m+n=ell`. The complementary pairs satisfy
`m+n>K`. Their total is

\[
 a^2\sum_{\substack{1\le m,n\le K\\m+n>K}}r^{m+n}.
 \tag{L-20813.5}
\]

Summing first in `n` shows that (L-20813.5) is exactly

\[
 a^2r^{K+1}\sum_{m=0}^{K-1}(K-m)r^m
 =E_{p,K}.
 \tag{L-20813.6}
\]

Subtracting proves (L-20813.2)--(L-20813.3). QED.

Thus `E_(p,K)` is not an uncontrolled negative remainder. It is precisely the
part of the local collision square whose product exponent falls beyond the
physical cutoff.

## 2. Positive local derivative identity

Combining (L-20813.2) with `L-20812.4` gives

\[
 \boxed{
 -\partial_uP_{p,K}(u)
 =aP_{p,K}(u)
  +a^2\sum_{\ell=2}^K(\ell-1)
    p^{-\ell(1/2+u)}.}
 \tag{L-20813.7}
\]

Both channels are positive. The first is the base-prime logarithmic drift. The
second is the triangular retained-power convolution.

For `K=1`, the second channel vanishes and

\[
 E_{p,1}=P_{p,1}^2.
 \tag{L-20813.8}
\]

So completing a prime-only factor creates a collision square that is entirely
outside the finite prefix. This is the exact reason the completed-Euler shortcut
produces a false positive reserve.

## 3. Global positive strip flow

At cutoff `X=q_j`, define

\[
 \mathcal B_j(u)
 =\sum_{p\le X}(\log p)P_{p,K_p(X)}(u),
 \tag{L-20813.9}
\]

and

\[
 \boxed{
 \mathcal C_j(u)
 =\sum_{p\le X}(\log p)^2
  \sum_{\ell=2}^{K_p(X)}(\ell-1)
  p^{-\ell(1/2+u)}.}
 \tag{L-20813.10}
\]

Then

\[
 \boxed{
 -\mathcal P_j'(u)
 =\mathcal B_j(u)+\mathcal C_j(u),
 \qquad
 \mathcal B_j,\mathcal C_j\ge0.}
 \tag{L-20813.11}
\]

Consequently the shifted statistic of `T-20803` has the wholly positive
representation

\[
 \boxed{
 \mathcal L_j(\omega)
 ={P_j\over\omega}\int_0^\omega
 {\mathcal B_j(u)+\mathcal C_j(u)
  \over\mathcal P_j(u)}du.}
 \tag{L-20813.12}
\]

There is no negative arithmetic term left inside the strip flow.

## 4. Diagonal Selberg interpretation

For a prime power `p^ell`,

\[
 (\Lambda*\Lambda)(p^\ell)
 =(\ell-1)(\log p)^2.
 \tag{L-20813.13}
\]

Hence

\[
 \boxed{
 \mathcal C_j(u)
 =\sum_{\substack{p^\ell\le X\\\ell\ge2}}
 { (\Lambda*\Lambda)(p^\ell)
  \over p^{\ell(1/2+u)}}.}
 \tag{L-20813.14}
\]

This is exactly the same-base-prime, or diagonal, part of the positive Selberg
convolution stream. Cross-prime products are not inserted artificially.

The full theorem is therefore reduced to comparing

```text
positive base-prime drift
+ positive diagonal Selberg convolution
```

with the explicit archimedean Fenchel barrier.

## 5. Higher-power asymptotic

At `u=0`, the diagonal channel is

\[
 \mathcal C_j(0)
 =\sum_{\ell\ge2}(\ell-1)
  \sum_{p\le X^{1/\ell}}
  { (\log p)^2\over p^{\ell/2}}.
 \tag{L-20813.15}
\]

The square layer supplies the only divergent term. Partial summation and the
prime number theorem give

\[
 \sum_{p\le\sqrt X}{(\log p)^2\over p}
 ={1\over8}\log^2X+C_2+o(1),
 \tag{L-20813.16}
\]

while every layer `ell>=3` converges absolutely as `X` tends to infinity.
Therefore there is an explicit convergent prime-power constant `C_diag` such
that

\[
 \boxed{
 \mathcal C_j(0)
 ={1\over8}\log^2X+C_{\rm diag}+o(1).}
 \tag{L-20813.17}
\]

One convenient definition is

\[
\begin{aligned}
 C_{\rm diag}={}&
 \lim_{y\to\infty}
 \left[
  \sum_{p\le y}{(\log p)^2\over p}
  -{1\over2}\log^2y
 \right]\\
 &+\sum_{\ell=3}^\infty(\ell-1)
   \sum_p{(\log p)^2\over p^{\ell/2}}.
\end{aligned}
 \tag{L-20813.18}
\]

The second line is absolutely convergent. Equation (L-20813.17) shows that the
complete higher-power channel can be centered to `o(1)` unconditionally. The
remaining RH-sensitive term is the coupling of the base-prime drift with the
nonlinear barrier through the actual endpoint mass `P_j`.

## 6. Corrected completion target

The apparent task proposed immediately after `L-20812`—dominate the cutoff
defect by the collision square—is already closed exactly by (L-20813.2). The
real theorem is now

\[
 \boxed{
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\mathcal B_j(u)+\mathcal C_j(u)
  \over\mathcal P_j(u)}du
 \ge
 A_+^*(P_j)-\eta_j.}
 \tag{L-20813.19}
\]

A promising next normalization is:

1. subtract the explicit square-layer asymptotic (L-20813.17) from both the
   diagonal channel and the expansion of `A_+^*(P_j)`;
2. retain the base-prime drift and endpoint mass in one correlated expression;
3. seek a Selberg/reflection square for the resulting `o(1)`-centered remainder.

## 7. Proof boundary

- The triangular recombination and positive strip-flow identity are exact.
- The asymptotic centering of the diagonal channel follows from the PNT and
  absolute convergence of the higher layers.
- Positivity of the arithmetic channels alone does not imply that they dominate
  the Fenchel barrier.
- The remaining comparison (L-20813.19) is still RH-bearing.
- No RH proof is claimed.