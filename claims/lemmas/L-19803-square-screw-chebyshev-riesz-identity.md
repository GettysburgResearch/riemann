# L-19803 — Square-screw Chebyshev–Riesz identity

Claim ID: `L-19803`  
Title: The finite square-cutoff screw scalar is an explicit positive-kernel Riesz mean of the Chebyshev error  
Status: `PROPOSED — COMPLETE ELEMENTARY IDENTITY`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `T-19801`; Stieltjes integration by parts

## 1. Chebyshev notation

Let

\[
\psi(x)=\sum_{m\le x}\Lambda(m)
\tag{L-19803.1}
\]

be the second Chebyshev function and put

\[
E(x)=\psi(x)-x.
\tag{L-19803.2}
\]

For an integer `N>=1`, define the positive kernel

\[
\boxed{
K_N(x)=x^{-3/2}
\left(1+\frac12\log\frac{N^2}{x}\right)
\mathbf1_{[1,N^2]}(x).}
\tag{L-19803.3}
\]

## 2. Exact prime-sum identity

The finite prime term in `T-19801` is

\[
P(N)=\sum_{m\le N^2}
 \frac{\Lambda(m)}{\sqrt m}
 \log\frac{N^2}{m}.
\tag{L-19803.4}
\]

Regard the sum as a Stieltjes integral:

\[
P(N)=\int_{1^-}^{N^2}
 x^{-1/2}\log\frac{N^2}{x}\,d\psi(x).
\tag{L-19803.5}
\]

The boundary term vanishes at both ends because `psi(1^-)=0` and the logarithm
vanishes at `x=N^2`. Since

\[
-\frac d{dx}
\left[x^{-1/2}\log\frac{N^2}{x}\right]
=K_N(x),
\tag{L-19803.6}
\]

Stieltjes integration by parts gives

\[
\boxed{
P(N)=\int_1^{N^2}\psi(x)K_N(x)\,dx.}
\tag{L-19803.7}
\]

Splitting `psi(x)=x+E(x)`, the elementary main integral is

\[
\begin{aligned}
\int_1^{N^2}xK_N(x)dx
&=\int_1^{N^2}x^{-1/2}
 \left(1+\frac12\log\frac{N^2}{x}\right)dx\\
&=4N-4-2\log N.
\end{aligned}
\tag{L-19803.8}
\]

Therefore

\[
\boxed{
P(N)=4N-4-2\log N
 +\int_1^{N^2}E(x)K_N(x)dx.}
\tag{L-19803.9}
\]

## 3. Exact screw decomposition

Insert (L-19803.9) into the finite formula for `mathscr S(N)`. Then

\[
\boxed{
\mathscr S(N)
 =\mathcal A(N)
 -\int_1^{N^2}E(x)K_N(x)dx,}
\tag{L-19803.10}
\]

where the completely explicit archimedean threshold is

\[
\boxed{
\begin{aligned}
\mathcal A(N)={}&\frac4N-4
 +(2+\psi(1/4)-\log\pi)\log N\\
&-\frac14\left[
 N^{-1}\Phi(N^{-4},2,1/4)
 -\Phi(1,2,1/4)
 \right].
\end{aligned}}
\tag{L-19803.11}
\]

Consequently

\[
\boxed{
\mathscr S(N)\ge0
\iff
\int_1^{N^2}(\psi(x)-x)K_N(x)dx
\le\mathcal A(N).}
\tag{L-19803.12}
\]

This is the exact arithmetic inequality remaining in the eventual-sign route.

## 4. Kernel normalization and limiting shape

The kernel has total mass

\[
\boxed{
\int_1^{N^2}K_N(x)dx=2\log N.}
\tag{L-19803.13}
\]

Indeed it is the integral of the derivative in (L-19803.6). Thus

\[
d\mu_N(x)=\frac{K_N(x)}{2\log N}dx
\tag{L-19803.14}
\]

is a probability measure on `[1,N^2]`.

For every fixed `x>=1`,

\[
\frac{K_N(x)}{2\log N}
\longrightarrow\frac12x^{-3/2}.
\tag{L-19803.15}
\]

The limiting density is itself a probability density on `[1,infinity)`.
Hence the square criterion is a logarithmically renormalized one-sided average
of the complete Chebyshev error against a fixed positive Mellin weight.

## 5. Archimedean asymptotic

Since

\[
\Phi(N^{-4},2,1/4)=16+O(N^{-4}),
\tag{L-19803.16}
\]

the `4/N` term cancels the leading Lerch endpoint exactly, giving

\[
\boxed{
\mathcal A(N)
 =C_0-\kappa_0\log N+O(N^{-5}),}
\tag{L-19803.17}
\]

where

\[
C_0=-4+\frac14\Phi(1,2,1/4),
\qquad
\kappa_0=-(2+\psi(1/4)-\log\pi)>0.
\tag{L-19803.18}
\]

Thus the exact RH-equivalent inequality is not a crude statement that the
smoothed prime error is small. It requires the specific negative logarithmic
bias supplied by the pole, gamma factor, and trivial-zero correction.

## 6. Growth-exponent form

Combining (L-19803.10) with `L-19802`,

\[
\boxed{
\Theta_\zeta
 =\limsup_{N\to\infty}
 \frac1{2\log N}
 \log\left(
 1+\left[
 \int_1^{N^2}E(x)K_N(x)dx-\mathcal A(N)
 \right]_+
 \right).}
\tag{L-19803.19}
\]

This expresses the rightmost zero displacement entirely through a one-sided
positive-kernel Riesz mean of the finite Chebyshev function.

## 7. Proof-facing consequence

A sufficient arithmetic theorem for RH is now the standalone estimate

\[
\boxed{
\left[
\int_1^{N^2}(\psi(x)-x)K_N(x)dx-\mathcal A(N)
\right]_+
=N^{o(1)}.}
\tag{L-19803.20}
\]

The stronger eventual inequality in (L-19803.12) is also sufficient.

This form is designed for comparison with Selberg symmetry, explicit PNT error
formulae, and one-sided Riesz-mean estimates. Any such comparison must preserve
the exact archimedean threshold `mathcal A(N)`; replacing it by an absolute
error bound loses the RH-scale cancellation.

## 8. Proof boundary

- The Stieltjes and elementary integral identities are exact.
- No estimate for the Chebyshev-error integral is proved here.
- Standard unconditional PNT error bounds are far larger than the
  subpolynomial excess required in (L-19803.20).
- The lemma is a structural arithmetic reduction, not a proof of RH.