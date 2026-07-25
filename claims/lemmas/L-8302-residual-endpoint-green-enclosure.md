# L-8302 — Residual enclosures for endpoint Green data

Claim ID: L-8302  
Title: Two residual-controlled linear solves enclose the complete endpoint Green matrix  
Status: PROPOSED  
Authoring agent: `gpt56-05-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: elementary operator-norm bounds  
Scope: proof-producing input for L-8301 without a full matrix inverse  
Related counterexample candidates: none

## Statement

Let `H` be Hermitian and suppose

\[
 H\succeq \mu I,\qquad \mu>0.
\]

Let `u,w` be unit vectors. Define

\[
 x_u=H^{-1}u,\qquad x_w=H^{-1}w
\]

and

\[
 a=u^*x_u,\qquad b=u^*x_w,\qquad d=w^*x_w.
\]

Let `y_u,y_w` be arbitrary approximate solves, with residuals

\[
 \rho_u=u-Hy_u,\qquad \rho_w=w-Hy_w.
\]

Put

\[
 \eta_u=\frac{\|\rho_u\|_2}{\mu},
 \qquad
 \eta_w=\frac{\|\rho_w\|_2}{\mu}.
\]

Then

\[
 \|x_u-y_u\|_2\le\eta_u,
 \qquad
 \|x_w-y_w\|_2\le\eta_w,
\]

and

\[
 \boxed{|a-\operatorname{Re}(u^*y_u)|\le\eta_u,}
\]

\[
 \boxed{|d-\operatorname{Re}(w^*y_w)|\le\eta_w.}
\]

With the symmetrized estimator

\[
 \widetilde b
 =\frac12\left(u^*y_w+\overline{w^*y_u}\right),
\]

one also has

\[
 \boxed{|b-\widetilde b|\le\frac{\eta_u+\eta_w}{2}.}
\]

Thus two approximate linear solves and one certified spectral floor enclose the
entire `2 x 2` matrix `G=U^*H^{-1}U` required by L-8301.

## Uncertain-matrix corollary

Suppose the exact matrix has the form

\[
 H=H_0+E,\qquad \|E\|_2\le\delta,
\]

and a rational or otherwise certified midpoint satisfies

\[
 H_0\succeq mI,\qquad m>\delta.
\]

Then

\[
 H\succeq\mu I,\qquad \mu=m-\delta.
\]

For an approximate solve `y`,

\[
 \|f-Hy\|_2
 \le\|f-H_0y\|_2+\delta\|y\|_2.
\]

Therefore L-8302 applies with the computable radius

\[
 \eta_f
 =\frac{\|f-H_0y\|_2+\delta\|y\|_2}{m-\delta}.
\]

This is the intended adapter for a rational midpoint plus operator-radius
certificate from a directed Toeplitz coefficient box.

## Enclosing the pressure

Let

\[
 a\in[a_-,a_+],\qquad d\in[d_-,d_+],
 \qquad b\in B(\widetilde b,\eta_b)
\]

be the resulting intervals and complex disc. For an exact or enclosed unit
phase `zeta`, interval arithmetic gives enclosures for

\[
 r=\operatorname{Re}(\overline\zeta b),
 \qquad
 D=ad-|b|^2.
\]

A certificate must prove `D_->0`. Directed square-root evaluation of `r^2+D`
then encloses

\[
 \lambda_+=r+\sqrt{r^2+D}.
\]

No entry of the full inverse is required. For exact rational data, a one-point
crossing can avoid a square root by checking the sign of

\[
 1-2r\tau-D\tau^2.
\]

For a quantitative background moat, outward rational lower and upper bounds on
`lambda_+` suffice.

## Proof

Since `H\succeq mu I`,

\[
 \|H^{-1}\|_2\le\frac1\mu.
\]

The first solve error satisfies

\[
 x_u-y_u=H^{-1}(u-Hy_u)=H^{-1}\rho_u,
\]

so

\[
 \|x_u-y_u\|_2\le\eta_u.
\]

The same proof gives the `w` estimate. Because `u,w` are unit vectors,
Cauchy--Schwarz gives the diagonal entry bounds.

Hermiticity of `H^{-1}` gives

\[
 b=u^*x_w=\overline{w^*x_u}.
\]

Hence

\[
 b-\widetilde b
 =\frac12\left(
 u^*(x_w-y_w)+\overline{w^*(x_u-y_u)}
 \right),
\]

and the triangle inequality gives the displayed radius.

For the uncertain-matrix corollary, Weyl's inequality yields

\[
 \lambda_{\min}(H)\ge\lambda_{\min}(H_0)-\|E\|_2\ge m-\delta.
\]

The residual inequality follows from

\[
 f-Hy=(f-H_0y)-Ey.
\]

The remaining statements are inclusion-monotone interval propagation. ∎

## Motivation

A direct inverse of a `1024 x 1024` interval Toeplitz matrix is unnecessary and
usually much wider than needed. The rank-two event sees only two endpoint
columns of the inverse. Krylov, conjugate-gradient, dense midpoint, or Toeplitz
solvers may nominate `y_u,y_w`; the final proof trusts only the spectral floor
and residual norms.

## Analytic domain audit

Pure finite-dimensional linear algebra. Every norm is Euclidean or induced
spectral norm.

## Dependency audit

No D-0801 formula is used. L-8301 consumes the resulting Green enclosure.
PR #79 supplies one possible midpoint/operator-radius source, but this lemma is
not logically tied to its implementation.

## Gap audit

1. The lower spectral floor `mu` must be rigorous and strictly positive.
2. Residuals must be evaluated against an enclosure of the intended exact
   matrix, not merely the discovery midpoint.
3. The complex off-diagonal estimator needs the displayed conjugation.
4. A disc for `b` must not be replaced by underestimated independent component
   radii.
5. Positivity of the inferred `D` must survive every uncertainty term.

## Adversarial tests

- Perturb exact endpoint solves and verify the exact Green entries remain in the
  residual enclosures.
- Inflate the midpoint radius until `m-delta<=0`; fail closed.
- Reverse the conjugation in the symmetrized `b` estimator and require a complex
  Hermitian control to fail.
- Use a nearly singular positive matrix to expose the necessary `1/mu` factor.

## Remaining uncertainty

No mathematical gap is known. Practical sharpness depends on the certified
spectral floor and residuals from the production Toeplitz midpoint.

## Suggested next attack

Once a complete coefficient box exists, certify a rational midpoint floor,
solve the two endpoint systems, and emit only the midpoint, operator radius, two
solution vectors, and exact residual ledgers. An independent checker can
reconstruct the pressure interval in `O(K^2)` time.
