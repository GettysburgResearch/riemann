# L-91010 — The Catalan Hankel background is exactly diagonal in shifted Chebyshev coordinates

Claim ID: `L-91010`  
Status: **EXACT ORTHOGONAL-POLYNOMIAL / CHRISTOFFEL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`, `T-91001`  
RH status: **unproved**

## 1. The universal background measure

The high-carrier limit from `L-91008` is

\[
 \Phi(w)=\sum_{k\ge0}c_k w^k
 =\int_0^1\frac{d\nu(\lambda)}{1-w\lambda},
 \qquad
 d\nu(\lambda)=\frac1\pi\sqrt{\lambda(1-\lambda)}\,d\lambda,
\]

with

\[
 c_k=\frac{C_{k+1}}{8\,4^k}.
\]

For a polynomial

\[
 p(\lambda)=\sum_{j=0}^n u_j\lambda^j
\]

define the Catalan Hankel quadratic form

\[
 Q_\nu[p]
 =\sum_{i,j=0}^n\overline{u_i}u_jc_{i+j}
 =\int_0^1|p(\lambda)|^2d\nu(\lambda).
\tag{L-91010.1}
\]

## 2. Exact shifted-Chebyshev orthogonality

Let `U_j` be the Chebyshev polynomial of the second kind and put

\[
 e_j(\lambda)=\sqrt8\,U_j(2\lambda-1).
\tag{L-91010.2}
\]

Then

\[
 \boxed{
 \int_0^1e_j(\lambda)e_k(\lambda)d\nu(\lambda)=\delta_{jk}.
 }
\tag{L-91010.3}
\]

Indeed, with `x=2lambda-1`,

\[
 d\nu(\lambda)=\frac1{4\pi}\sqrt{1-x^2}\,dx,
\]

and

\[
 \int_{-1}^1U_j(x)U_k(x)\sqrt{1-x^2}\,dx
 =\frac\pi2\delta_{jk}.
\]

Consequently the moment matrix

\[
 H_n^{(\nu)}=(c_{i+j})_{0\le i,j\le n}
\]

is congruent to the identity under the exact triangular change of basis from monomials to `e_0,...,e_n`.

Equivalently, if

\[
 p=\sum_{j=0}^nd_je_j,
\]

then

\[
 \boxed{Q_\nu[p]=\sum_{j=0}^n|d_j|^2.}
\tag{L-91010.4}
\]

This is the canonical preconditioner for the high-carrier Hankel hierarchy.

## 3. Exact Christoffel–Darboux amplifier

The degree-`n` reproducing kernel is

\[
 \boxed{
 K_n(\lambda,\mu)
 =\sum_{j=0}^ne_j(\lambda)e_j(\mu)
 =8\sum_{j=0}^nU_j(2\lambda-1)U_j(2\mu-1).
 }
\tag{L-91010.5}
\]

For every `lambda_*` outside `[0,1]`,

\[
 \boxed{
 \sup_{\deg p\le n,\ Q_\nu[p]=1}|p(\lambda_*)|^2
 =K_n(\lambda_*,\lambda_*).
 }
\tag{L-91010.6}
\]

The extremizer is

\[
 p_{n,\lambda_*}(\lambda)
 =\frac{K_n(\lambda,\lambda_*)}
 {\sqrt{K_n(\lambda_*,\lambda_*)}}.
\tag{L-91010.7}
\]

Thus `K_n` gives the exact best polynomial amplifier against the complete Catalan/Stieltjes background, not merely a convenient test vector.

## 4. Closed form at an off-line depth

For a possible off-line pair of depth

\[
 0<y<\frac12,
\]

put

\[
 w_y=1-y^2,
 \qquad
 \lambda_y=w_y^{-1},
 \qquad
 \alpha_y=2\operatorname{artanh}y.
\tag{L-91010.8}
\]

Then

\[
 2\lambda_y-1
 =\frac{1+y^2}{1-y^2}
 =\cosh\alpha_y
\]

and

\[
 U_j(2\lambda_y-1)
 =\frac{\sinh((j+1)\alpha_y)}{\sinh\alpha_y}.
\tag{L-91010.9}
\]

Therefore

\[
 \boxed{
 K_n(\lambda_y,\lambda_y)
 =\frac8{\sinh^2\alpha_y}
  \sum_{j=1}^{n+1}\sinh^2(j\alpha_y).
 }
\tag{L-91010.10}
\]

Equivalently,

\[
 \boxed{
 K_n(\lambda_y,\lambda_y)
 =\frac4{\sinh^2\alpha_y}
 \left[
  \frac{\sinh((n+1)\alpha_y)
        \cosh((n+2)\alpha_y)}{\sinh\alpha_y}
  -(n+1)
 \right].
 }
\tag{L-91010.11}
\]

In particular

\[
 \log K_n(\lambda_y,\lambda_y)
 =2n\alpha_y+O_y(1)
 =4n\operatorname{artanh}y+O_y(1).
\tag{L-91010.12}
\]

## 5. Exact rank-one form of one matching pair

At the matching centre of an off-line pair of multiplicity `m`, `R-91003` gives the moment contribution

\[
 a_k^{\rm pair}
 =-4my^2w_y^{-k-3}.
\]

Hence for every polynomial `p`,

\[
 \boxed{
 Q_{\rm pair}[p]
 =-4my^2w_y^{-3}|p(\lambda_y)|^2.
 }
\tag{L-91010.13}
\]

In the orthonormal Chebyshev basis this is one negative rank-one matrix

\[
 -4my^2w_y^{-3}
 v_n(\lambda_y)v_n(\lambda_y)^*,
 \qquad
 v_n(\lambda)=(e_0(\lambda),\ldots,e_n(\lambda))^T.
\tag{L-91010.14}
\]

Its unique nonzero eigenvalue is

\[
 \boxed{
 -4my^2w_y^{-3}K_n(\lambda_y,\lambda_y).
 }
\tag{L-91010.15}
\]

This is the exact finite-dimensional analogue of the hyperbolic pair block in Claude's Gabor compression, now after optimal nonlinear polynomial amplification.

## 6. Boundary

Exact here:

```text
Catalan moment matrix -> identity in shifted U_j basis;
exact Christoffel kernel and extremizer;
closed hyperbolic formula at lambda_y=1/(1-y^2);
one matching pair -> one negative rank-one Hankel perturbation;
optimal degree-n pair amplification.
```

Not established here:

```text
unconditional positivity of the full zeta Hankel matrix at all degrees;
control of all off-line nuisance blocks without a sign theorem;
Riemann Hypothesis.
```
