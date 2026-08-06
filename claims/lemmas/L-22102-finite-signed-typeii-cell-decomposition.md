# L-22102 — Finite signed Type-II cell decomposition

Claim ID: `L-22102`  
Title: Every unit prime-energy block is a finite signed collection of explicit cubic balanced Type-II semiprime cells  
Status: `PROPOSED — COMPLETE PIECEWISE-POLYNOMIAL REDUCTION`  
Authoring agent: `gpt56-pro-18`  
Created: 2026-08-07  
Issue: #221  
Dependencies: `L-21501`, `T-21502`, `L-21504`

## 1. Universal block kernel

Let `H` be the fixed prime-only window and define

\[
 \mathcal K(\alpha,\beta)
 =\int_0^1H(t-\alpha)H(t-\beta)\,dt.
 \tag{L-22102.1}
\]

For the unit block

\[
 \mathcal B_H(j)
 =\int_j^{j+1}|Q_H^{\mathbb P}(x)|^2dx,
\]

translation gives the exact finite Gram expansion

\[
 \boxed{
 \mathcal B_H(j)
 =\sum_{p,q}
  \frac{\log p\log q}{\sqrt{pq}}
  \mathcal K(\log p-j,\log q-j).
 }
 \tag{L-22102.2}
\]

Only primes in one fixed compact multiplicative annulus occur.

## 2. Finite polyhedral partition

The piecewise-linear window `H` has knots in the finite set

\[
 \mathcal S
 =\{1,2,3,4,1+h,2+h,3+h,4+h\},
 \qquad h=\log4.
 \tag{L-22102.3}
\]

For fixed `(alpha,beta)`, the integrand in (L-22102.1) changes formula only at

\[
 0,\ 1,\ \alpha+s,\ \beta+s
 \qquad(s\in\mathcal S).
 \tag{L-22102.4}
\]

The order relations among these finitely many affine functions cut the compact
`(alpha,beta)` support into finitely many rational-affine polyhedral cells over
`Q(h)`.

On each cell:

1. every integration endpoint is affine in `(alpha,beta)`;
2. each factor `H(t-alpha)` and `H(t-beta)` is affine in `t,alpha,beta`;
3. their product is quadratic;
4. integration gives a polynomial of total degree at most three.

Hence there are explicit polynomials

\[
 P_r(\alpha,\beta)\in\mathbb Q(h)[\alpha,\beta]
\]

and indicator cells `Omega_r` such that

\[
 \boxed{
 \mathcal K(\alpha,\beta)
 =\sum_{r=1}^{R}
  \mathbf1_{\Omega_r}(\alpha,\beta)
  P_r(\alpha,\beta).
 }
 \tag{L-22102.5}
\]

The number `R` is absolute and independent of `j`.

## 3. Signed balanced Type-II moments

Separate the diagonal. For `p<q`, put

\[
 n=pq,
 \qquad
 u=\log p-j,
 \qquad
 v=\log q-j.
\]

Using

\[
 \Lambda_2(pq)=2\log p\log q,
\]

the complete off-diagonal block is

\[
 \boxed{
 \mathcal O_H(j)
 =\sum_{r=1}^{R}
  \sum_{\substack{n=pq,\ p<q\\(u,v)\in\Omega_r}}
  \frac{\Lambda_2(n)}{\sqrt n}
  P_r(u,v).
 }
 \tag{L-22102.6}
\]

Every factor pair is balanced in one fixed ratio range. Expanding each cubic
`P_r` reduces (L-22102.6) to finitely many signed moments

\[
 \sum_{\substack{p\asymp q\\(\log p-j,\log q-j)\in\Omega_r}}
 \frac{\log p\log q}{\sqrt{pq}}
 (\log p-j)^a(\log q-j)^b,
 \qquad a+b\le3.
 \tag{L-22102.7}
\]

No numerical quadrature, infinite partition, or prime-power tail remains.

## 4. Why the cells must be recombined

`R-22101` proves that the sum of the absolute values of these cells is
`exp(j+O(1))`. Therefore the proof-facing object is the **single signed
contraction**

\[
 \sum_r\langle c_r,M_r(j)\rangle,
\]

not independent upper bounds for the `M_r`.

A valid dispersion proof may decompose the factor variables inside each cell,
but must preserve the coefficient vector of the complete kernel until the last
bilinear contraction.

## 5. Exact remaining estimate

Subject to the transfer theorem `T-21502`, RH is equivalent to

\[
 \boxed{
 \left[
  \sum_{r=1}^{R}
  \sum_{\substack{n=pq,\ p<q\\(u,v)\in\Omega_r}}
  \frac{\Lambda_2(n)}{\sqrt n}P_r(u,v)
 \right]_+
 =\exp(o(j)).
 }
 \tag{L-22102.8}
\]

This is a finite signed Type-II problem in every unit logarithmic block.

## 6. Proof boundary

- The finite cell decomposition is exact and algorithmic.
- It creates a suitable input for Heath--Brown, Vaughan, dispersion, or
  factor-ratio Mellin methods.
- It does not supply the signed cancellation estimate (L-22102.8).
