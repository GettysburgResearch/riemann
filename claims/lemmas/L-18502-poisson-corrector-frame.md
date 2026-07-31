# L-18502 — Poisson source defect gives a sub-Gaussian corrector frame

Claim ID: `L-18502`  
Title: The external self-dual Hermite corrector has an explicit boundary channel whose fixed-zero Rayleigh quotient decays only exponentially in logarithmic support  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: Poisson summation; elementary Gaussian tails; `L-18501`; the external Hermite repair of `L-15611`  
Scope: the one-dimensional source-corrector quotient of the harmonic count  
Related candidates: none

## 1. Exact Poisson defect

Use the additive Fourier convention

\[
 \widehat f(y)=\int_{\mathbb R}f(x)e^{2\pi ixy}\,dx
\]

and

\[
 \mathcal E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu).
\]

For every even Schwartz source,

\[
 \boxed{
 \mathcal E(f)(u)
 =\mathcal E(\widehat f)(u^{-1})
 +\frac12\left[
 u^{-1/2}\int_{\mathbb R}f
 -u^{1/2}f(0)
 \right].}
 \tag{L-18502.1}
\]

Let `h_0` be the normalized self-Fourier Gaussian Hermite function, and put

\[
 q=h_0(0)=\int_{\mathbb R}h_0\ne0.
 \tag{L-18502.2}
\]

Write

\[
 R_0(x)=\mathcal E(h_0)(e^x).
 \tag{L-18502.3}
\]

Self-Fourier invariance gives the exact relation

\[
 \boxed{
 R_0(x)=R_0(-x)+\frac q2
 \left(e^{-x/2}-e^{x/2}\right).}
 \tag{L-18502.4}
\]

The source-valid repaired combinations

\[
 h_{4j}-\frac{h_{4j}(0)}{h_0(0)}h_0
\]

cancel this boundary channel exactly. It is therefore the natural quotient
coordinate left by the self-dual source constraint.

## 2. One-sided asymptotic

The Gaussian decay of `h_0` implies that, as `x->+infinity`,

\[
 |R_0(x)|\le C e^{Ax}e^{-\pi e^{2x}}
 \tag{L-18502.5}
\]

for fixed constants `A,C`. Inserting this into (L-18502.4) gives, as
`x->-infinity`,

\[
 \boxed{
 R_0(x)=\frac q2e^{-x/2}-\frac q2e^{x/2}
 +O\!\left(e^{-Ax}e^{-\pi e^{-2x}}\right).}
 \tag{L-18502.6}
\]

For `L>1`, let

\[
 k_L(x)=1_{[-L,L]}(x)R_0(x),
 \qquad
 \mathcal F_{\log}k_L(\gamma)
 =\int_{-L}^Lk_L(x)e^{-i\gamma x}\,dx.
 \tag{L-18502.7}
\]

For every fixed real `gamma`, (L-18502.5)--(L-18502.6) give

\[
 \boxed{
 \mathcal F_{\log}k_L(\gamma)
 =\frac{q}{2(1/2+i\gamma)}
   e^{(1/2+i\gamma)L}
 +O_\gamma(1).}
 \tag{L-18502.8}
\]

### Proof

On `[-L,-1]`, integrate the leading term `q e^{-x/2}/2` explicitly. Its lower
endpoint contributes the displayed exponential. The integral of
`e^{x/2}` is bounded independently of `L`; the double-Gaussian remainder is
integrable after the change of variables `v=e^{-x}`. On `[-1,L]`, the source
sum and the remaining elementary term are integrable uniformly in `L`. QED.

In particular, for every fixed certified real zero ordinate `gamma`, there are
constants `c_gamma>0` and `L_gamma` such that

\[
 \boxed{
 |\mathcal F_{\log}k_L(\gamma)|^2
 \ge c_\gamma e^L
 \qquad(L\ge L_\gamma).}
 \tag{L-18502.9}
\]

There is no oscillatory loss in the magnitude: the growing tail occurs at only
one logarithmic endpoint.

## 3. Hardy metric scale

For fixed `0<=tau<1/2`, put

\[
 \|f\|_{L,\tau}^2
 =\int_{-L}^L|f(x)|^2\,2\cosh(2\tau x)\,dx.
 \tag{L-18502.10}
\]

Equations (L-18502.5)--(L-18502.6) imply

\[
 \boxed{
 \|k_L\|_{L,\tau}^2
 \le C_\tau e^{(1+2\tau)L}.}
 \tag{L-18502.11}
\]

Consequently the one-zero generalized frame quotient obeys

\[
 \boxed{
 \frac{|\mathcal F_{\log}k_L(\gamma)|^2}
      {\|k_L\|_{L,\tau}^2}
 \ge c_{\gamma,\tau}e^{-2\tau L}.}
 \tag{L-18502.12}
\]

Thus the quotient frame loses at most ordinary exponential scale in the
logarithmic support. It does not inherit the Gaussian scale of the repaired
radical tails.

## 4. Harmonic-lift survival adapter

Let `J_L` be the exact ambient-energy minimizing lift used by the harmonic
three-block architecture. Let `G_C` be its metric and let `V_gamma` be the
selected-zero evaluation functional. Suppose the lifted corrector satisfies
proof-grade bounds

\[
 \boxed{
 |V_\gamma J_Lk_L|
 \ge(1-\theta_L)
 |\mathcal F_{\log}k_L(\gamma)|,
 \qquad 0\le\theta_L<1,}
 \tag{L-18502.13}
\]

and

\[
 \boxed{
 \|J_Lk_L\|_{G_C}^2
 \le M_L\|k_L\|_{L,\tau}^2.}
 \tag{L-18502.14}
\]

Then the one-dimensional corrector subspace has the directed frame floor

\[
 \boxed{
 \frac{|V_\gamma J_Lk_L|^2}
      {\|J_Lk_L\|_{G_C}^2}
 \ge
 c_{\gamma,\tau}
 \frac{(1-\theta_L)^2}{M_L}
 e^{-2\tau L}.}
 \tag{L-18502.15}
\]

The two quantities in (L-18502.13)--(L-18502.14) are finite harmonic-solve
certificates. They are much smaller proof obligations than the complete
generalized eigenvalue count.

## 5. Separation from the radical scale

Let the multiplicative support parameter be `lambda=e^L`. Suppose the uniformly
repaired Hermite radical packet has selected-zero Gram endpoint

\[
 \epsilon_\lambda
 \le e^{-2c\lambda^2+o(\lambda^2)}
 \tag{L-18502.16}
\]

and the harmonic corrector losses satisfy

\[
 \log M_L=o(\lambda^2),
 \qquad
 -\log(1-\theta_L)=o(\lambda^2).
 \tag{L-18502.17}
\]

Then the corrector frame floor in (L-18502.15) is

\[
 \boxed{\sigma_\lambda^2=e^{-o(\lambda^2)},}
 \tag{L-18502.18}
\]

while the radical evaluation scale is Gaussian. For any fixed
`0<alpha<2c`,

\[
 \beta_\lambda=e^{-\alpha\lambda^2}
 \tag{L-18502.19}
\]

satisfies eventually

\[
 \epsilon_\lambda\le\frac12\beta_\lambda,
 \qquad
 2\beta_\lambda<\sigma_\lambda^2.
 \tag{L-18502.20}
\]

After choosing the finite zero cutoff so that `B_(T,lambda)<=beta_lambda`, the
sacrificial-subspace theorem `L-18501` proves the sharp harmonic count whenever
the corrector channel has the required codimension.

## 6. Multiple source constraints

For `q` external correctors, replace the scalar in (L-18502.13) by the `q x q`
selected-zero evaluation matrix. If its smallest generalized singular value has
logarithm `o(lambda^2)`, the same Gaussian separation proves the count. Since
`q` is the fixed source codimension in the general Connes--Consani source
space, this remains a finite proof object independent of the growing radical
rank.

## 7. Proof boundary

- The Poisson identity and the unlifted corrector asymptotics are exact.
- Harmonic lifting may alter selected-zero evaluations; the survival and metric
  bounds in (L-18502.13)--(L-18502.14) must be certified rather than assumed.
- The theorem closes the scale separation once those finite bounds and the
  source-corrector codimension model are part of the production packet.
- It does not show that an arbitrary symbol-selected low packet has only the
  source-corrector quotient.
- No RH conclusion is claimed without the complete packet-containment gate.
