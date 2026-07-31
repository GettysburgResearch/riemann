# L-15420 — Exact Blaschke-pair Hankel singular value

Claim ID: `L-15420`  
Title: One off-line zero pair has an exact Hankel pressure `omega/delta` and an exact Toeplitz coercivity collapse  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: elementary Hardy-space reproducing kernels; `L-15418`, `L-15419` for the zeta-scattering interpretation  
Scope: the uniform strict-contraction target for Suzuki's scattering symbols  
Related counterexample candidates: none

## Half-plane notation

Let `H^2(C_+)` be the Hardy space of the upper half-plane, with boundary
projection `P_+`, complementary projection `P_-`, and normalized reproducing
kernel `k_p` at `p in C_+`.

For `p in C_+`, put

\[
 b_p(z)=\frac{z-p}{z-\overline p}.
 \tag{L-15420.1}
\]

The boundary function `b_p` is inner.  Its one-dimensional model space is

\[
 K_{b_p}=H^2\ominus b_pH^2=\operatorname{span}\{k_p\}.
 \tag{L-15420.2}
\]

For a bounded boundary symbol `phi`, write

\[
 \mathsf H_\phi=P_-M_\phi|_{H^2},
 \qquad
 T_\phi=P_+M_\phi|_{H^2}.
 \tag{L-15420.3}
\]

## Exact two-point theorem

Let

\[
 p=x+iy_-,\qquad q=x+iy_+,
 \qquad 0<y_-<y_+,
 \tag{L-15420.4}
\]

and define the unimodular boundary symbol

\[
 \phi_{p,q}=\overline{b_p}\,b_q.
 \tag{L-15420.5}
\]

Then `mathsf H_(phi_(p,q))` has rank one and

\[
 \boxed{
 \mathsf H_{\phi_{p,q}}^*\mathsf H_{\phi_{p,q}}
 =|b_q(p)|^2P_{K_{b_p}}.}
 \tag{L-15420.6}
\]

Consequently,

\[
 \boxed{
 \|\mathsf H_{\phi_{p,q}}\|
 =|b_q(p)|
 =\frac{y_+-y_-}{y_++y_-}.}
 \tag{L-15420.7}
\]

Since multiplication by a unimodular symbol is unitary on `L^2`,

\[
 T_{\phi_{p,q}}^*T_{\phi_{p,q}}
 =I-\mathsf H_{\phi_{p,q}}^*\mathsf H_{\phi_{p,q}}.
 \tag{L-15420.8}
\]

Therefore the exact lower Toeplitz modulus is

\[
 \boxed{
 \inf_{\|f\|=1}\|T_{\phi_{p,q}}f\|^2
 =1-|b_q(p)|^2
 =\frac{4y_-y_+}{(y_-+y_+)^2}.}
 \tag{L-15420.9}
\]

### Proof

For inner `b_p`, the standard orthogonal decomposition gives

\[
 \mathsf H_{\overline{b_p}}^*
 \mathsf H_{\overline{b_p}}
 =P_{K_{b_p}}.
 \tag{L-15420.10}
\]

Since `b_qf in H^2` for `f in H^2`,

\[
 \mathsf H_{\phi_{p,q}}f
 =\mathsf H_{\overline{b_p}}(b_qf).
 \tag{L-15420.11}
\]

Evaluation by the normalized kernel gives

\[
 \langle b_qf,k_p\rangle
 =b_q(p)\langle f,k_p\rangle.
 \tag{L-15420.12}
\]

Thus

\[
 \|\mathsf H_{\phi_{p,q}}f\|^2
 =|b_q(p)|^2|\langle f,k_p\rangle|^2,
 \]

which proves (L-15420.6).  For the common-real-part geometry,

\[
 |b_q(p)|
 =\left|\frac{p-q}{p-\overline q}\right|
 =\frac{y_+-y_-}{y_++y_-}.
 \]

Equations (L-15420.8)--(L-15420.9) follow from the Toeplitz--Hankel defect
identity. QED.

## Zeta off-line-pair specialization

Let

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad 0<\delta<\frac12,
 \tag{L-15420.13}
\]

be a nontrivial zero.  For `0<omega<delta`, the corresponding local numerator
and denominator points of Suzuki's boundary scattering ratio are

\[
 p_\omega=-\gamma+i(\delta-\omega),
 \qquad
 q_\omega=-\gamma+i(\delta+\omega).
 \tag{L-15420.14}
\]

The isolated pair factor therefore satisfies

\[
 \boxed{
 \|\mathsf H_{\overline{b_{p_\omega}}b_{q_\omega}}\|
 =\frac{\omega}{\delta},}
 \tag{L-15420.15}
\]

and

\[
 \boxed{
 \inf_{\|f\|=1}
 \|T_{\overline{b_{p_\omega}}b_{q_\omega}}f\|^2
 =1-\frac{\omega^2}{\delta^2}
 =\frac{\delta^2-\omega^2}{\delta^2}.}
 \tag{L-15420.16}
\]

As `omega upward delta`,

\[
 \|\mathsf H\|\uparrow1,
 \qquad
 m(T):=\inf_{\|f\|=1}\|Tf\|
 \sim\sqrt{\frac{2(\delta-\omega)}{\delta}}.
 \tag{L-15420.17}
\]

This is the exact local singular-value mechanism behind `L-15419`.

## Full scattering symbol

After grouping all zeros at ordinate `gamma` and canceling only exact common
factors, write locally

\[
 \Theta_\omega
 =\overline{b_{p_\omega}}^{\,m}
  b_{q_\omega}^{\,m}\Phi_\omega,
 \tag{L-15420.18}
\]

where `Phi_omega` is unimodular on the boundary and regular and nonzero on the
shrinking Poisson scale centered at `-gamma`.  Normalized reproducing kernels
at `p_omega` localize on that scale. Hence the regular factor becomes a
unimodular constant in the limit and

\[
 \boxed{
 \limsup_{\omega\uparrow\delta}
 \|\mathsf H_{\Theta_\omega}\|=1.}
 \tag{L-15420.19}
\]

Equation (L-15420.19) is an asymptotic localization statement; the exact finite
formula (L-15420.15) belongs to the isolated pair factor.

## Consequence for a uniform moat

For every unimodular symbol,

\[
 \|\mathsf H_\Theta\|\le1.
 \]

Thus a false-RH zero forces the universal upper value to be approached:

\[
 \mathrm{RH\ false}
 \quad\Longrightarrow\quad
 \sup_{0<\omega<1/2}
 \|\mathsf H_{\Theta_\omega}\|=1.
 \tag{L-15420.20}
\]

Combined with Suzuki innerness under RH, the requested strict moat is not an
auxiliary estimate: it is an RH-equivalent spectral-gap formulation.

## Gap audit

- Formula (L-15420.7) is exact for the isolated pair symbol.
- Passing from the isolated pair to (L-15420.19) requires the same-ordinate
  grouping and regular-factor localization declared in `L-15419`.
- A bound at finitely many offsets cannot control an unknown crossing offset.
- Pointwise or local-`Lp` convergence of the symbols does not control Hankel
  norm; `R-15403` records the explicit failure.
- This lemma quantifies the obstruction. It does not prove that no off-line zero
  exists and therefore does not prove the requested uniform moat.
