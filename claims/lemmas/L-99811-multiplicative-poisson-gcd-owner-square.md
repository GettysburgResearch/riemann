# L-99811 — Prime-torus Poisson evaluation gives an exact positive divisor-GCD owner square

Claim ID: `L-99811`  
Status: **PROVED EXACT MULTIPLICATIVE HARDY IDENTITY**  
Created: 2026-08-20  
RH status: **not assumed**

Let `(c_n)` be finitely supported and let `tau>0`. Let `\mathcal P` be the
finite set of primes dividing the support. For

\[
 n=\prod_{p\in\mathcal P}p^{v_p(n)},
\]

define the polynomial

\[
 F_\tau(z)=\sum_nc_n n^\tau
 \prod_{p\in\mathcal P}z_p^{v_p(n)}.
\tag{L-99811.1}
\]

Put `r_p=p^{-tau}`. Then

\[
 F_\tau((r_p)_p)=\sum_nc_n.
\tag{L-99811.2}
\]

## 1. Product-Poisson inequality

Apply the one-variable Poisson inequality successively in every prime
coordinate. On the boundary torus, the product Poisson kernel has Fourier
coefficient

\[
 \prod_pr_p^{|v_p(m)-v_p(n)|}
 =\left(\frac{\gcd(m,n)^2}{mn}\right)^\tau.
\]

The factors `m^tau n^tau` in (L-99811.1) therefore leave
`gcd(m,n)^(2 tau)`. Hence

\[
\boxed{
 \left|\sum_nc_n\right|^2
 \le
 \mathcal G_\tau(c)
 :=\sum_{m,n}c_m\overline{c_n}\gcd(m,n)^{2\tau}.
}
\tag{L-99811.3}
\]

This is a multiplicative alternative to the one-parameter Cauchy packet.

## 2. Exact Jordan-square factorization

For `alpha>0`, put

\[
 J_\alpha(d)=d^\alpha\prod_{p\mid d}(1-p^{-\alpha})\ge0.
\]

The generalized Jordan identity is

\[
 x^\alpha=\sum_{d\mid x}J_\alpha(d).
\tag{L-99811.4}
\]

Taking `alpha=2 tau` in (L-99811.3) and switching finite sums gives

\[
\boxed{
 \mathcal G_\tau(c)
 =\sum_{d\ge1}J_{2\tau}(d)
   \left|\sum_{d\mid n}c_n\right|^2.
}
\tag{L-99811.5}
\]

Thus the multiplicative point-evaluation cost is exactly a positive square of
all divisor tails. It retains the native divisor ownership and introduces no
unknown sign, absolute Möbius replacement or post-hoc Gram.

## 3. Canonical scalar application

For the PR #659 coefficients `c_(L,y)(n)`, define

\[
 \mathcal G_L(y)
 =\sum_dJ_{2\tau_L}(d)
 \left|
  \sum_{d\mid n}
  \frac{\beta_{67}(n)}{\sqrt n}
  (\mathcal F_LT)(y/n)
 \right|^2.
\]

Then

\[
 |f_L(y)|^2\le\mathcal G_L(y).
\]

Consequently a subpower block estimate for the inverse-weighted integrals of
`sqrt(mathcal G_L)` is independently conclusion-complete. This divisor-square
route may exploit multiplicativity and the exact owner laws even when a direct
frequency large sieve cannot see the signs.

The theorem proves the positive normal form. It does not prove its required
subpower packing estimate.