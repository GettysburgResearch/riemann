# L-91405 — The beta-binomial Hahn shadow has exact spectrum and an exact score-edge identity

Claim ID: `L-91405`  
Status: **EXACT FINITE REVERSIBLE-CHAIN THEOREM**  
Created: 2026-08-12  
Depends on: the beta-binomial/Jacobi shadow setup of `L-91403`  
RH status: **unproved**

## 1. The finite shadow law

For an integer `N>=1`, put

\[
 \pi_N(k)=
 \frac{6(k+1)(N-k+1)}{(N+1)(N+2)(N+3)},
 \qquad 0\le k\le N,
\]

and

\[
 \lambda_k=(k+2)(N-k),
 \qquad
 \mu_k=k(N-k+2).
\]

The normalization follows from

\[
 \sum_{k=0}^N(k+1)(N-k+1)
 =\frac{(N+1)(N+2)(N+3)}6.
\]

Moreover

\[
 \boxed{
 \pi_N(k)\lambda_k
 =\pi_N(k+1)\mu_{k+1}
 }
 \tag{L-91405.1}
\]

for `0<=k<N`.

Define the birth-death generator

\[
 (\mathcal L_Nf)(k)=\frac14\left[
 \lambda_k(f(k+1)-f(k))
 +\mu_k(f(k-1)-f(k))
 \right],
 \tag{L-91405.2}
\]

with missing boundary terms set to zero. Detailed balance gives

\[
 \boxed{
 -\langle f,\mathcal L_Nf\rangle_{\pi_N}
 =\frac14\sum_{k=0}^{N-1}
 \pi_N(k)\lambda_k|f(k+1)-f(k)|^2.
 }
 \tag{L-91405.3}
\]

## 2. Exact spectrum

The polynomial flag

\[
 \mathcal P_0\subset\mathcal P_1\subset\cdots\subset\mathcal P_N
\]

is invariant under `mathcal L_N`. On the monomial `k^j`, the coefficient of the leading term is

\[
 -\frac{j(j+3)}4k^j.
\]

Indeed, using

\[
 (k+1)^j-k^j
 =jk^{j-1}+\frac{j(j-1)}2k^{j-2}+O(k^{j-3}),
\]

\[
 (k-1)^j-k^j
 =-jk^{j-1}+\frac{j(j-1)}2k^{j-2}+O(k^{j-3}),
\]

and

\[
 \lambda_k=-k^2+(N-2)k+2N,
 \qquad
 \mu_k=-k^2+(N+2)k,
\]

the degree-`j+1` terms cancel and the degree-`j` coefficient is

\[
 \frac14[-4j-j(j-1)]
 =-\frac{j(j+3)}4.
\]

The triangular diagonal entries are distinct. Since `mathcal L_N` is self-adjoint in an `(N+1)`-dimensional space,

\[
 \boxed{
 \operatorname{spec}(-\mathcal L_N)
 =\left\{\frac{j(j+3)}4:0\le j\le N\right\}.
 }
 \tag{L-91405.4}
\]

In particular the spectral gap is exactly one:

\[
 \boxed{
 \operatorname{Var}_{\pi_N}(f)
 \le-\langle f,\mathcal L_Nf\rangle_{\pi_N}.
 }
 \tag{L-91405.5}
\]

The constant is sharp on the centered linear coordinate.

## 3. The score coordinate is an exact eigenfunction

Put

\[
 V_N(k)=\frac{2k-N}{N}.
\]

Since

\[
 \lambda_k-\mu_k=2N-4k=-2NV_N(k),
\]

one has

\[
 \boxed{-\mathcal L_NV_N=V_N.}
 \tag{L-91405.6}
\]

Thus the Poisson solution for the beta-coordinate score is not implicit: it is the score itself.

## 4. Product score-edge identity

Let `(K_1,K_2)` have law `pi_N tensor pi_N`, put

\[
 S_N=V_N(K_1)+V_N(K_2),
\]

and let

\[
 \mathcal L_N^{(2)}
 =\mathcal L_N\otimes I+I\otimes\mathcal L_N.
\]

Then

\[
 -\mathcal L_N^{(2)}S_N=S_N.
\]

For every complex function `H` on the product grid,

\[
 \boxed{
 \operatorname{Cov}(H,S_N)
 =\mathcal E_N^{(2)}(H,S_N),
 }
 \tag{L-91405.7}
\]

where the covariance uses the centered real score and the right side is the polarized Dirichlet form. Because every score increment is `2/N`, this is the explicit edge formula

\[
 \boxed{
 \begin{aligned}
 \operatorname{Cov}(H,S_N)
 =\frac1{2N}\sum_{i,j=0}^N\pi_N(i)\pi_N(j)
 \big[&\lambda_i(H(i+1,j)-H(i,j))\\
      &+\lambda_j(H(i,j+1)-H(i,j))\big],
 \end{aligned}
 }
 \tag{L-91405.8}
\]

with absent boundary edges omitted.

Consequently, if the real part of `H` is coordinatewise nondecreasing, then

\[
 \boxed{\operatorname{Re}\operatorname{Cov}(H,S_N)\ge0.}
 \tag{L-91405.9}
\]

This is the exact finite Hahn analogue of the monotone Brownian reflection theorem on PR #401.

## 5. General Poisson solution

For every centered `g`, define

\[
 h=(-\mathcal L_N)^{-1}g
\]

on the orthogonal complement of the constants. Then

\[
 \boxed{
 \operatorname{Cov}(H,g)=\mathcal E_N(H,h)
 }
 \tag{L-91405.10}
\]

and the unit spectral gap gives

\[
 \boxed{
 \langle g,(-\mathcal L_N)^{-1}g\rangle_{\pi_N}
 \le\operatorname{Var}_{\pi_N}(g).
 }
 \tag{L-91405.11}
\]

Thus the finite score-Poisson problem is completely solved and uniformly coercive.

## 6. Scope

Equations (L-91405.7)--(L-91405.9) prove the full monotone sector and provide an exact finite edge representation for every phase pattern. They do **not** make the arbitrary complex edge increments nonnegative. The remaining Brownian/theta theorem is source-specific:

> identify the completed Xi two-copy reflection observable, after the exact half-size tilt and Gamma reservoir are retained, with the limit of the positive Hahn edge energy plus an explicit nonnegative boundary square.

The unit gap ensures that such an identification would be stable under the finite-to-Jacobi limit; it does not supply the identification itself.

```text
beta-binomial reversibility                 EXACT
complete Hahn spectrum                      EXACT
uniform spectral gap one                    EXACT
score Poisson solution h=score              EXACT
product covariance = explicit edge pairing  EXACT
monotone sector positivity                  EXACT
arbitrary-phase edge-square identity        OPEN / RH-BEARING
theta DtN identification                    OPEN
Riemann Hypothesis                          UNPROVED
```
