# T-18502 — Full-complement selected-zero count and harmonic Schur transfer

Claim ID: `T-18502`  
Title: Critical-line uniqueness closes the packet-capture theorem; one quantitative frame-to-tail moat remains  
Status: `PROPOSED CONDITIONAL COFINAL TRANSFER`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `L-18507`; harmonic certified-zero Schur lower form; quadratic-rank Hermite tail; triangular three-block theorem  
Scope: replacement of the packet-specific count on PR #186 by a count on the actual complete harmonic low packet  
Related candidates: none

## 1. Exact full packet theorem

At each support `lambda`, let

\[
 U_\lambda=R_\lambda\oplus_{G_{C,\lambda}}W_\lambda,
 \qquad
 W_\lambda=R_\lambda^{\perp_{G_C}}\cap U_\lambda.
\]

By `L-18507`, there is a finite proof-grade set of simple critical-line zeros
`Z_lambda` and a number `sigma_lambda^2>0` such that

\[
 K_{Z,\lambda}^C|_{W_\lambda}
 \succeq
 \sigma_\lambda^2G_{C,\lambda}|_{W_\lambda}.             \tag{T-18502.1}
\]

This uses the **actual complete low packet**. No equality between a constructed
cardinal packet and the dangerous low hierarchy is assumed.

Let `K_(T,lambda)^C>=K_(Z,lambda)^C` be the complete selected-zero Gram used by
the harmonic theorem. Suppose

\[
 K_{T,\lambda}^C|_{R_\lambda}
 \preceq
 \epsilon_\lambda G_{C,\lambda}|_{R_\lambda}.             \tag{T-18502.2}
\]

Choose `beta_lambda>0` so that

\[
 \boxed{
 \epsilon_\lambda
 <B_{T,\lambda}+\beta_\lambda
 <\sigma_\lambda^2.}                                     \tag{T-18502.3}
\]

Then

\[
 \boxed{
 N_{G_{C,\lambda}^{-1/2}K_{T,\lambda}^C
 G_{C,\lambda}^{-1/2}}
 (B_{T,\lambda}+\beta_\lambda)
 =\dim R_\lambda.}                                       \tag{T-18502.4}
\]

In particular the count inequality requested in the harmonic three-block route
holds.

## 2. Visible Schur floor

The counted harmonic transfer gives, on

\[
 V_\lambda=W_\lambda,
\]

\[
 K_{T,\lambda}^C|_{V_\lambda}
 \succeq
 (B_{T,\lambda}+\beta_\lambda-\epsilon_\lambda)
 G_{V,\lambda}.                                          \tag{T-18502.5}
\]

Combining with

\[
 S_{U,\lambda}
 \succeq K_{T,\lambda}^C-B_{T,\lambda}G_{C,\lambda}
\]

gives

\[
 \boxed{
 S_{U,\lambda}|_{V_\lambda}
 \succeq
 (\beta_\lambda-\epsilon_\lambda)G_{V,\lambda}.}         \tag{T-18502.6}
\]

Equivalently, in the original three-block coordinates,

\[
 \boxed{
 B_{V,\lambda}-Z_\lambda^*C_\lambda^{-1}Z_\lambda
 \succeq
 (\beta_\lambda-\epsilon_\lambda)G_{V,\lambda}.}         \tag{T-18502.7}
\]

If `epsilon_lambda<=beta_lambda/2`, the visible moat is at least
`beta_lambda/2`.

## 3. Cofinal rate composition

Assume the existing uniform Hermite-radical theorem and directed assembly
provide

\[
 e_\lambda\to0,
 \qquad
 \kappa_\lambda\to0,
 \qquad
 \delta_\lambda\to0,                                    \tag{T-18502.8}
\]

whenever the visible moat is `beta_lambda/2` and the declared metric losses are
inserted.

If there is an unbounded support sequence for which one can choose the finite
frames of `L-18507` and numbers `beta_lambda` satisfying

\[
 \boxed{
 \epsilon_\lambda\le\frac12\beta_\lambda,
 \qquad
 B_{T,\lambda}+\beta_\lambda<\sigma_\lambda^2,}           \tag{T-18502.9}
\]

then the triangular three-block theorem gives

\[
 \boxed{
 \lambda_{\min}(\mathcal H_\lambda,\mathcal G_\lambda)
 \ge-(e_\lambda+\kappa_\lambda+\delta_\lambda)
 \longrightarrow0^-.}                                   \tag{T-18502.10}
\]

The existing monotone cofinal lower-envelope theorem then implies RH.

## 4. What has been removed

The theorem eliminates the following former hypotheses:

- equality between a constructed cardinal--radical packet and the complete low
  packet;
- a principal-angle theorem;
- a dimension-only capacity comparison;
- a one-end or sacrificial packet containment assertion;
- any need to guess the low selected-zero eigenspace.

The full complement is simply `R_lambda^(perp_GC)`, and finitely many actual
simple line zeros frame it by Paley--Wiener uniqueness.

## 5. Exact remaining scalar

Define the best finite simple-line frame floor

\[
 \Sigma_\lambda
 =\sup_{Z\subset\mathcal Z_0^{\rm simp},\ |Z|<\infty}
 \lambda_{\min}
 \left(
 (G_C|_{W_\lambda})^{-1/2}
 K_{Z,\lambda}^C|_{W_\lambda}
 (G_C|_{W_\lambda})^{-1/2}
 \right).                                                \tag{T-18502.11}
\]

`L-18507` proves

\[
 \boxed{\Sigma_\lambda>0}                                \tag{T-18502.12}
\]

at every finite support.

The cofinal theorem is therefore reduced to the scalar separation

\[
 \boxed{
 \epsilon_\lambda<B_{T,\lambda}+\beta_\lambda
 <\Sigma_\lambda}                                        \tag{T-18502.13}
\]

with a `beta_lambda` compatible with the Gaussian radical-row schedule.

This is strictly narrower than packet capture. It compares one positive
critical-line sampling constant with one complete omitted-zero budget in the
same harmonic metric.

## 6. Why the scalar is genuinely RH-bearing

If RH is false, an off-line Xi-cardinal difference is a fixed negative Weil
direction invisible at every exact real zero before localization. Its supported
approximants acquire only tail-sized real-zero evaluations. Therefore the
finite frame constants in (T-18502.11) may collapse relative to the omitted-zero
budget on complete low packets.

Consequently no theorem proving (T-18502.13) cofinally may be inferred from
finite-dimensionality or qualitative uniqueness alone. It must use the
arithmetic form, a quantitative sampling theorem for the actual packet, or a
direct positive Schur estimate.

## 7. Proof boundary

- The finite full-complement construction and count are proved by `L-18507`.
- The harmonic Schur transfer is exact once (T-18502.3) is certified.
- No current result proves the cofinal frame-to-tail separation
  (T-18502.13).
- Hence the packet-capture issue is closed, but RH is not claimed proved.
