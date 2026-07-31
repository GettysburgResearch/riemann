# T-18501 — Sacrificial count closes the harmonic visible floor

Claim ID: `T-18501`  
Title: A one-end or source-corrector frame replaces the cofinal integer count in the harmonic three-block theorem  
Status: `PROPOSED CONDITIONAL CLOSURE`  
Authoring agent: `gpt56-02-p`  
Created: 2026-07-31  
Dependencies: `L-18501`, `L-18502`; the harmonic-lift certified-zero transfer; the quadratic-rank Hermite tail theorem; the triangular three-block Schur theorem  
Scope: the final count displayed in the user request  
Related candidates: none

## 1. Harmonic setting

Let `U_lambda` be the complete finite low packet and let

\[
 J_\lambda u=(u,-C_\lambda^{-1}L_\lambda u)
\]

be the exact ambient-energy minimizing lift. Put

\[
 G_{C,\lambda}=J_\lambda^*G_\lambda J_\lambda,
 \qquad
 K_{T,\lambda}^C=J_\lambda^*K_{T,\lambda}J_\lambda.
 \tag{T-18501.1}
\]

Let `R_lambda subset U_lambda` be an exact localized radical packet and assume
its selected-zero evaluation Gram satisfies

\[
 \boxed{
 K_{T,\lambda}^C|_{R_\lambda}
 \preceq\epsilon_\lambda
 G_{C,\lambda}|_{R_\lambda}.}
 \tag{T-18501.2}
\]

Let `B_(T,lambda)` be the complete omitted-zero budget in the harmonic certified-
zero theorem.

## 2. Replacement for the integer gate

Assume there is a subspace `W_lambda subset U_lambda` with

\[
 \boxed{
 \operatorname{codim}_{U_\lambda}W_\lambda
 \le\dim R_\lambda}
 \tag{T-18501.3}
\]

and a proof-grade frame floor

\[
 \boxed{
 K_{T,\lambda}^C|_{W_\lambda}
 \succeq\sigma_\lambda^2
 G_{C,\lambda}|_{W_\lambda}.}
 \tag{T-18501.4}
\]

Choose `beta_lambda>0` so that

\[
 \boxed{
 B_{T,\lambda}+\beta_\lambda
 <\sigma_\lambda^2.}
 \tag{T-18501.5}
\]

Then `L-18501` gives directly

\[
 \boxed{
 N_{G_{C,\lambda}^{-1/2}K_{T,\lambda}^C
 G_{C,\lambda}^{-1/2}}
 \left(B_{T,\lambda}+\beta_\lambda\right)
 \le\dim R_\lambda.}
 \tag{T-18501.6}
\]

No principal angle between `R_lambda` and the selected-zero low eigenspace is
assumed. If additionally

\[
 \epsilon_\lambda<B_{T,\lambda}+\beta_\lambda,
\]

min--max gives equality in (T-18501.6), and the automatic angle estimate is

\[
 \boxed{
 \|P_{N_\lambda^\perp}P_{R_\lambda}\|^2
 \le
 \frac{\epsilon_\lambda}
 {B_{T,\lambda}+\beta_\lambda}.}
 \tag{T-18501.7}
\]

## 3. Visible Schur floor

The counted harmonic transfer therefore gives on

\[
 V_\lambda=R_\lambda^{\perp_{G_C}}\cap U_\lambda
\]

\[
 K_{T,\lambda}^C|_{V_\lambda}
 \succeq
 \left(B_{T,\lambda}+\beta_\lambda-\epsilon_\lambda\right)
 G_{V,\lambda}.
 \tag{T-18501.8}
\]

Combining with the certified-zero lower form gives

\[
 \boxed{
 B_{V,\lambda}
 -Z_\lambda^*C_\lambda^{-1}Z_\lambda
 \succeq
 (\beta_\lambda-\epsilon_\lambda)G_{V,\lambda}.}
 \tag{T-18501.9}
\]

If

\[
 \epsilon_\lambda\le\frac12\beta_\lambda,
 \tag{T-18501.10}
\]

then the visible Schur moat is at least `beta_lambda/2`.

## 4. Cofinal Gaussian schedule

Suppose the uniform radical-tail theorem gives

\[
 \epsilon_\lambda
 \le e^{-2c\lambda^2+o(\lambda^2)}
 \tag{T-18501.11}
\]

and the sacrificial frame has only sub-Gaussian loss,

\[
 \boxed{
 -\log\sigma_\lambda^2=o(\lambda^2).}
 \tag{T-18501.12}
\]

Choose

\[
 \beta_\lambda=e^{-\alpha\lambda^2},
 \qquad 0<\alpha<2c.
 \tag{T-18501.13}
\]

For each fixed support and finite packet, increase the proof-grade zero cutoff
until

\[
 B_{T,\lambda}\le\frac12\beta_\lambda.
 \tag{T-18501.14}
\]

Then, eventually,

\[
 B_{T,\lambda}+\beta_\lambda
 \le\frac32e^{-\alpha\lambda^2}
 <\sigma_\lambda^2,
 \tag{T-18501.15}
\]

and

\[
 \epsilon_\lambda\le\frac12\beta_\lambda.
 \tag{T-18501.16}
\]

Thus the sharp count and the positive visible Schur floor hold cofinally.

## 5. Two concrete sacrificial packets

### A. One-end packet

If the complete harmonic low packet contains a same-end profile packet
`W_lambda` whose codimension is at most `dim R_lambda`, then the opposite-end
terminal-prime Hankel matrix is absent from the witness restriction. It is
enough to prove a selected-real-zero frame on one end. The count is insensitive
to every cross term outside that restriction.

This is a strictly weaker target than bounding the complete terminal-prime
matrix in operator norm.

### B. External source corrector

If the packet is the localized/harmonic image of

\[
 U^{src}_\lambda=P_\lambda\oplus\operatorname{Ran}Q,
\]

with repaired radical block

\[
 R^{src}_\lambda=(I-Q\ell)P_\lambda,
\]

then

\[
 \operatorname{codim}R^{src}_\lambda=\operatorname{rank}\ell.
\]

Use the fixed-dimensional harmonic image of `Ran Q` as `W_lambda`. In the
self-dual Hermite sector the quotient is one-dimensional. `L-18502` shows that
the unlifted corrector frame is at scale `e^(-2 tau log lambda)`, while the
radical evaluations are at scale `e^(-2c lambda^2)`. The production obligation
is reduced to one harmonic-lift survival inequality and one metric-inflation
bound.

## 6. Completion of the three rates

Under the harmonic visible floor above, the quadratic-rank Gaussian radical-tail
theorem gives

\[
 e_\lambda\to0,
 \qquad
 \kappa_\lambda\to0,
\]

for any `alpha<2c` after the displayed subexponential metric losses. The directed
assembly diagonal gives `delta_lambda->0`. Therefore the triangular Schur theorem
yields

\[
 \boxed{
 \lambda_{\min}(\mathcal H_\lambda,\mathcal G_\lambda)
 \ge-\left(e_\lambda+\kappa_\lambda+\delta_\lambda\right)
 \longrightarrow0^-.}
 \tag{T-18501.17}
\]

The existing cofinal lower-envelope theorem then implies RH.

## 7. Exact remaining gates

The theorem replaces the large generalized-eigenvalue count by one of two
smaller proof objects:

1. a one-end selected-zero frame plus the exact codimension inequality; or
2. a fixed-dimensional external-corrector frame plus packet-containment.

Neither packet-containment nor harmonic-lift survival may be inferred from
source dimension alone. A complete proof must bind them to the exact harmonic
packet and metric.

## 8. Nonclaim

The min--max replacement and the Gaussian scale composition are exact. No current
production artifact has yet supplied the required one-end/corrector frame in the
exact harmonic metric for a complete cofinal Suzuki packet. Consequently this
theorem is a conditional closure and does not by itself prove RH.
