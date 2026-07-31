# L-15419 — A uniform strict Hankel contraction moat implies RH

Claim ID: `L-15419`  
Title: An off-line zero forces Suzuki's anti-causal Hankel norm to approach one at its crossing offset  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15418`; normalized reproducing kernels in the half-plane; local Blaschke factorization  
Scope: a quantitatively weaker positive target than exact Hankel vanishing  
Related counterexample candidates: none

## Motivation

`L-15418` states RH as

\[
 \mathsf H_\omega=0
 \qquad(\omega>0).
 \]

Exact operator equality is difficult to certify. The present lemma shows that a
**uniform strict contraction moat** already suffices:

\[
 \boxed{
 \sup_{0<\omega<1/2}\|\mathsf H_\omega\|<1
 \quad\Longrightarrow\quad\mathrm{RH}.}
 \tag{L-15419.1}
\]

In fact, under the local factorization stated below, false RH forces the
supremum to equal one.

## The reciprocal Blaschke bubble

For a point

\[
 p=x+iy\in\mathbb C^+,
 \]

put

\[
 b_p(z)=\frac{z-p}{z-\bar p}.
 \tag{L-15419.2}
\]

The boundary function `b_p` is inner. Its reciprocal boundary symbol is
`overline{b_p}`. The corresponding Hankel operator satisfies

\[
 \boxed{
 \mathsf H_{\overline{b_p}}^*
 \mathsf H_{\overline{b_p}}
 =P_{K_{b_p}},}
 \tag{L-15419.3}
\]

where `K_(b_p)=H2 minus b_p H2` is one-dimensional. Consequently

\[
 \boxed{
 \|\mathsf H_{\overline{b_p}}\|=1}
 \tag{L-15419.4}
\]

for every `y>0`, even though

\[
 \overline{b_{x+iy}}(t)\longrightarrow1
 \tag{L-15419.5}
\]

pointwise for `t!=x` and in every finite local `Lp` norm as `y downarrow0`.
Thus a rank-one anti-causal bubble can be invisible to ordinary boundary
convergence while retaining unit operator norm.

## Local factor from an off-line zeta zero

Let

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
 \tag{L-15419.6}
\]

be a zero. For `0<omega<delta`, the denominator of

\[
 \Theta_\omega(z)=
 \frac{\xi(\frac12-\omega-iz)}
      {\xi(\frac12+\omega-iz)}
 \tag{L-15419.7}
\]

has a pole at

\[
 p_\omega=-\gamma+i(\delta-\omega).
 \tag{L-15419.8}
\]

The functional-equation partner in the numerator supplies the reflected lower
half-plane zero. After grouping every zero at the same ordinate and canceling
only exact common factors, the boundary symbol has a local factorization

\[
 \boxed{
 \Theta_\omega(t)
 =\overline{b_{p_\omega}(t)}^{\,m}
  \Phi_\omega(t),}
 \tag{L-15419.9}
\]

where `m>=1` is the uncanceled multiplicity and `Phi_omega` is unimodular and
has a regular nonzero boundary value at `t=-gamma` as `omega upward delta`.
All other zeros have positive distance from this shrinking boundary scale after
the same-ordinate finite packet is grouped.

## Reproducing-kernel localization

Let `k_p` be the normalized `H2` reproducing kernel at `p`. Its boundary mass is
the Poisson kernel centered at `x` with width `y`. Hence, for every bounded
symbol `Phi` with a Lebesgue value at `x`,

\[
 \|(\Phi-\Phi(x))k_{x+iy}\|_2\longrightarrow0
 \qquad(y\downarrow0).
 \tag{L-15419.10}
\]

Apply this with `Phi=Phi_omega` and `p=p_omega`. On the shrinking kernel scale,
`Theta_omega` is a constant unimodular multiple of the reciprocal Blaschke
bubble. Therefore

\[
 \boxed{
 \limsup_{\omega\uparrow\delta}
 \|\mathsf H_\omega\|=1.}
 \tag{L-15419.11}
\]

The upper bound `<=1` is automatic from

\[
 I-T_\omega^*T_\omega
 =\mathsf H_\omega^*\mathsf H_\omega\preceq I.
 \]

This proves equality in (L-15419.11).

## Strict-contraction criterion

Under RH, every `Theta_omega` is inner and

\[
 \mathsf H_\omega=0.
 \tag{L-15419.12}
\]

If RH is false, choose an off-line zero and use (L-15419.11). Hence

\[
 \boxed{
 \mathrm{RH}
 \iff
 \sup_{0<\omega<1/2}\|\mathsf H_\omega\|<1.}
 \tag{L-15419.13}
\]

The right side may be replaced by the existence of any explicit constant
`kappa<1` satisfying

\[
 \|\mathsf H_\omega\|\le\kappa
 \qquad(0<\omega<1/2).
 \tag{L-15419.14}
\]

Thus a positive proof does **not** need to prove exact causality at every finite
stage. A uniform operator moat below the universal value one is enough.

## Why this is a genuine weakening

Exact innerness asks for

\[
 \|\mathsf H_\omega\|=0
 \]

at every offset. The new target allows an arbitrary fixed amount of anti-causal
energy, provided it stays uniformly below one. The discrete pole-crossing index
then upgrades the strict moat to absence of every off-line zero.

This is analogous to proving a uniform spectral gap rather than exact equality
of two subspaces.

## Candidate sources of a moat

1. **Schur test on Suzuki's explicit kernel.** Find one positive weight giving
   an anti-causal integral-operator norm below one uniformly in `omega`.
2. **Canonical-system energy.** Prove the Hamiltonian transfer matrix has a
   uniform strict contractivity reserve.
3. **Von Mangoldt-chain dilation.** Realize `mathsf H_omega` as a compression of
   a Markov adjoint whose nontrivial singular values have a uniform gap.
4. **Filtered phase packet.** Combine a finite proof-grade phase block with a
   complete tail norm below `1-kappa`.
5. **Collective compactness plus index.** Prove every possible unit-norm bubble
   escapes a common compact frame, then rule out that escape arithmetically.

## Proof-producing interface

A finite moat certificate should contain:

- exact `omega` interval;
- rational or directed kernel boxes;
- a positive Schur weight;
- row and column integral bounds whose product is `<1`;
- a complete anti-causal tail budget;
- interval coverage of `(0,1/2)` or a symbolic monotonic continuation theorem.

A finite offset grid is insufficient because a reciprocal Blaschke bubble
localizes on a scale set by the unknown distance `delta-omega`.

## Gap audit

- The local regularity of `Phi_omega` in (L-15419.9) must be checked after
  grouping every zero at the same ordinate and all exact cancellations.
- Pointwise or `Lp` convergence of the symbol does not control Hankel norm;
  (L-15419.3)--(L-15419.5) are the explicit counterexample.
- A bound `||H_omega||<=1` is automatic and useless; strictness is
  load-bearing.
- A moat depending on `omega` and tending to one near an unknown crossing does
  not close RH.
- This lemma reduces the positive theorem to a uniform strict contraction. It
  does not prove such a moat.
