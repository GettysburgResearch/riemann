# T-15409 — Cumulative Weyl energy and one endpoint branch inequality imply exact Toeplitz coercivity

Claim ID: `T-15409`  
Title: A direct canonical flow replaces the missing KLM/de Branges intertwiner  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15421`, `L-15422`, `L-15423`; exact quotient-to-original Weyl identification  
Scope: positive completion theorem for Issue #180  
Related counterexample candidates: none

## Hypotheses

For every `0<omega<1/2`, assume:

1. the original Riemann coordinate Weyl form `mathcal K_omega^W` is identified exactly with the normalized Volterra derivative form `mathcal Q_omega` on a common closed form core and its completion;
2. the endpoint Volterra branches satisfy
   \[
    \boxed{
    \|M_{-,\omega}f\|_2
    \le
    \|M_{+,\omega}f\|_2
    \quad\text{for every }f;}
    \tag{T-15409.1}
   \]
3. the Fourier convention is the one in `L-15421`.

## Cumulative positivity

By `L-15422`,

\[
 \int_0^\omega
 \langle f,\mathcal K_u^W f\rangle\,du
 =\frac12\left(
 \|M_{+,\omega}f\|_2^2
 -\|M_{-,\omega}f\|_2^2
 \right)
 \ge0.
 \tag{T-15409.2}
\]

Thus

\[
 \boxed{
 \int_0^\omega\mathcal K_u^W\,du\succeq0.}
 \tag{T-15409.3}
\]

`L-15421` gives the exact de Branges kernel identity

\[
 \widetilde{\mathcal D}_\omega
 ={4\over\pi}
 \int_0^\omega\mathcal K_u^W\,du.
 \tag{T-15409.4}
\]

Therefore

\[
 \boxed{
 \widetilde{\mathcal D}_\omega\succeq0.}
 \tag{T-15409.5}
\]

## Exact coercivity

Kernel positivity implies that

\[
 \Theta_\omega=E_\omega^\#/E_\omega
 \tag{T-15409.6}
\]

is a Schur function in the upper half-plane. Its boundary values are unimodular by the functional equations. Hence `Theta_omega` is inner and multiplication maps `H^2_+` isometrically into itself.

For the Toeplitz/Hankel decomposition,

\[
 T_\omega=P_+M_{\Theta_\omega}|_{H^2_+},
 \qquad
 \mathsf H_\omega=P_-M_{\Theta_\omega}|_{H^2_+},
 \tag{T-15409.7}
\]

one obtains

\[
 \mathsf H_\omega=0,
 \qquad
 \boxed{T_\omega^*T_\omega=I.}
 \tag{T-15409.8}
\]

Thus the requested uniform lower bound holds with

\[
 \boxed{\eta=1.}
 \tag{T-15409.9}
\]

## What has been removed

The theorem requires neither:

- pointwise Weyl positivity at every intermediate horizontal shift;
- a KLM coherent-state pullback;
- an explicit KLM-to-de Branges transmutation kernel;
- a separately proved compactness limit;
- a strict finite-stage Toeplitz moat.

The direct horizontal flow and endpoint primitive replace those steps.

## Exact remaining positive statement

The theorem reduces the full coercivity problem to one independent branch inequality in the physical Weyl metric:

\[
 \boxed{
 E_\omega^*
 \left(C^*C-K^*C^*CK\right)
 E_\omega\succeq0
 \qquad(0<\omega<1/2),}
 \tag{T-15409.10}
\]

where `K` is multiplication by

\[
 \kappa(s,u)={1-s-u\over1+s+u}.
 \tag{T-15409.11}
\]

By `L-15423`, (T-15409.10) is automatic in the quotient metric induced by `C`. The smallest concrete blocker is proving that this quotient metric is exactly the physical/original Weyl branch metric, or deriving the same inequality from the Jordan-divisor conditional expectation in `L-15424`.

## Proof boundary

- Equations (T-15409.2)--(T-15409.5) are direct consequences of the new exact flow and endpoint identities.
- The Schur/inner conclusion from positive de Branges kernel is standard Hardy/de Branges theory.
- The quotient-to-original Weyl identification and the physical endpoint branch domination are not proved here.
- The theorem is therefore a completed transfer theorem, not an unconditional proof of RH.
