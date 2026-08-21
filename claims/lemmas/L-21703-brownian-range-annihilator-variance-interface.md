# L-21703 — Brownian-range representation of the annihilator variance defect

Claim ID: `L-21703`  
Title: The prime-annihilator defect is the excess logarithmic variance of a half-size-biased Brownian-bridge range  
Status: **PROVED REPRESENTATION PENDING INDEPENDENT REVIEW; VARIANCE SATURATION OPEN**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Dependencies: `T-21702`; Biane--Pitman--Yor's Mellin law for the Brownian-bridge range and their `Sigma_2` perpetuity characterization  
Scope: a positive probabilistic attack on the exact scalar endpoint

## 1. Brownian range law for `xi`

Let `(b_u,0<=u<=1)` be a standard Brownian bridge and put

\[
 Y=\sqrt{2/\pi}
 \left(\max_{0\le u\le1}b_u-\min_{0\le u\le1}b_u\right).
 \tag{L-21703.1}
\]

Biane--Pitman--Yor prove the entire Mellin identity

\[
 \boxed{\mathbb E[Y^s]=2\xi(s)\qquad(s\in\mathbb C).}
 \tag{L-21703.2}
\]

Define the half-size-biased law

\[
 \boxed{
 {d\mathbb P_{1/2}\over d\mathbb P}(Y)
 ={Y^{1/2}\over\mathbb E[Y^{1/2}]}.}
 \tag{L-21703.3}
\]

For

\[
 Z=\log Y
\]

under `P_(1/2)`, (L-21703.2) gives

\[
 \boxed{
 \mathbb E_{1/2}[e^{itZ}]
 ={\xi(1/2+it)\over\xi(1/2)}.}
 \tag{L-21703.4}
\]

The reciprocal size-bias identity

\[
 \mathbb E[g(1/Y)]=\mathbb E[Yg(Y)]
 \tag{L-21703.5}
\]

implies that the law of `Z` in (L-21703.4) is symmetric.  This is the Brownian
realization of Nakamura's centered completed-Riemann probability law.

## 2. Exact logarithmic variance

Since the centered functional equation gives `xi'(1/2)=0`, differentiating
(L-21703.4) at the origin yields

\[
 \boxed{
 \operatorname{Var}_{1/2}(\log Y)
 ={\xi''(1/2)\over\xi(1/2)}.}
 \tag{L-21703.6}
\]

Let `Gamma_L` be the distinct positive critical-line zero ordinates and retain
multiplicity `m_gamma`.  Combining (L-21703.6) with `T-21702` gives

\[
 \boxed{
 \begin{aligned}
 D_{\rm off}
 :={}&\operatorname{Var}_{1/2}(\log Y)
 -2\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}\\
 ={}&4\sum_{\substack{\rho=1/2+\delta+i\gamma\\
                      \delta>0,\ \gamma>0}}
 m_\rho{\gamma^2-\delta^2\over(\gamma^2+\delta^2)^2}
 \ge0.
 \end{aligned}}
 \tag{L-21703.7}
\]

Every summand on the final line is strictly positive.  Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \operatorname{Var}_{1/2}(\log Y)
 =2\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}.}
 \tag{L-21703.8}
\]

This is the exact Brownian form of the prime-annihilator endpoint.

## 3. Gamma-sum realization

Let

\[
 \Sigma_2={2\over\pi^2}
 \sum_{n\ge1}{\Gamma_{2,n}\over n^2},
 \tag{L-21703.9}
\]

where the `Gamma_(2,n)` are independent gamma variables with shape `2` and
unit rate.  Biane--Pitman--Yor prove

\[
 \boxed{\Sigma_2\overset d={2\over\pi}Y^2.}
 \tag{L-21703.10}
\]

Its Laplace transform is

\[
 \boxed{
 \phi(\lambda)=\mathbb E[e^{-\lambda\Sigma_2}]
 =\left({\sqrt{2\lambda}\over\sinh\sqrt{2\lambda}}\right)^2.}
 \tag{L-21703.11}
\]

Let `P_(1/4)^Sigma` denote the quarter-size-biased law

\[
 {d\mathbb P_{1/4}^{\Sigma}\over d\mathbb P}(x)
 ={x^{1/4}\over\mathbb E[\Sigma_2^{1/4}]}.}
 \tag{L-21703.12}
\]

Equation (L-21703.10) shows that an additive constant separates
`log Y` from `(1/2)log Sigma_2`; hence

\[
 \boxed{
 \operatorname{Var}_{1/4}^{\Sigma}(\log\Sigma_2)
 =4{\xi''(1/2)\over\xi(1/2)}.}
 \tag{L-21703.13}
\]

The endpoint is equivalently

\[
 \boxed{
 \mathrm{RH}
 \iff
 \operatorname{Var}_{1/4}^{\Sigma}(\log\Sigma_2)
 =8\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}.}
 \tag{L-21703.14}
\]

Thus the target concerns one explicit infinite gamma convolution, not an
abstract unknown probability law.

## 4. Size-biased perpetuity equation

For a nonnegative random variable `X`, write `X*` for its ordinary size-biased
law.  Biane--Pitman--Yor characterize `X=Sigma_2` by

\[
 \mathbb E[X]={2\over3},
 \qquad
 \boxed{X^*\overset d=X+HX^*,}
 \tag{L-21703.15}
\]

where the three variables on the right are independent and

\[
 \mathbb P(H\in dh)=(h^{-1/2}-1)\,dh,
 \qquad0<h<1.
 \tag{L-21703.16}
\]

If `phi(lambda)=E[e^{-lambda X}]`, then the size-biased transform is
`-phi'(lambda)/E[X]`.  Equation (L-21703.15) gives the exact nonlinear renewal
identity

\[
 \boxed{
 \phi'(\lambda)
 =\phi(\lambda)
 \int_0^1(h^{-1/2}-1)\phi'(\lambda h)\,dh.}
 \tag{L-21703.17}
\]

The hyperbolic expression (L-21703.11) is the unique normalized solution.
This gives a concrete probability/renewal operator from which a variance or
convex-order proof may be attempted.

## 5. The missing independent inequality

`T-21702` already proves the lower inequality

\[
 \operatorname{Var}_{1/2}(\log Y)
 \ge2\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}.
 \tag{L-21703.18}
\]

It is equality exactly under RH.  Therefore a Brownian proof need only establish
the reverse inequality

\[
 \boxed{
 \operatorname{Var}_{1/2}(\log Y)
 \le2\sum_{\gamma\in\Gamma_L}{m_\gamma\over\gamma^2}.}
 \tag{L-21703.19}
\]

A stronger sufficient target uses the laws `mu_C` and `mu_U` from `T-21702`:

\[
 \boxed{
 \mathcal L(Z)*\mu_C\preceq_{\rm cx}\mu_U.}
 \tag{L-21703.20}
\]

Convex order in (L-21703.20) implies the variance inequality; together with the
opposite exact defect (L-21703.7), it forces equality and RH.

The perpetuity equation (L-21703.15), the gamma-sum decomposition, or a
Brownian-path coupling are three noncircular mechanisms that could establish
(L-21703.19) or (L-21703.20).

## 6. What generic probability does not supply

The following properties alone do not prove the reverse inequality:

- positivity of the completed-Riemann density;
- symmetry from reciprocal size bias;
- infinite divisibility of the additive variable `Sigma_2`;
- log-concavity without an exact comparison operator;
- finite verification of critical-line zeros.

A symmetric characteristic function may have nonreal zeros, and additive gamma
infinite divisibility does not automatically make the logarithmic Mellin
transform a Pólya-frequency transform.  Any successful argument must use the
specific coefficients `n^{-2}`, the exact perpetuity kernel
`h^{-1/2}-1`, or Brownian bridge geometry.

## 7. Proof boundary

Equations (L-21703.2)--(L-21703.17) are exact imported probability identities
and elementary consequences.  Equation (L-21703.7) is the positive off-line
quartet decomposition of `T-21702`.

Neither (L-21703.19) nor (L-21703.20) is proved here.  They are the smallest
independent Brownian/probability inequalities that would prove the corrected
prime-annihilator endpoint.
