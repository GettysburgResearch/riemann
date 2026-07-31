# T-15408 — The uniform Hankel moat is equivalent to RH

Claim ID: `T-15408`  
Title: A uniform Toeplitz coercivity reserve, a strict Hankel contraction, and RH are the same statement for the xi scattering family  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15418`, `L-15419`, `L-15420`; Suzuki's inner-function criterion for the xi scattering ratio  
Scope: final positive target in Issue #180  
Related counterexample candidates: none

## Scattering family

For `0<omega<1/2`, let

\[
 \Theta_\omega(t)=
 \frac{\xi(\frac12-\omega-it)}
      {\xi(\frac12+\omega-it)}
 \tag{T-15408.1}
\]

with removable common zeros canceled. Its boundary modulus is one almost
everywhere. On the Hardy decomposition

\[
 L^2(\mathbb R)=H^2_+\oplus H^2_-,
 \]

define

\[
 T_\omega=P_+M_{\Theta_\omega}|_{H^2_+},
 \qquad
 \mathsf H_\omega=P_-M_{\Theta_\omega}|_{H^2_+}.
 \tag{T-15408.2}
\]

## Exact Toeplitz--Hankel equivalence

Unitarity of boundary multiplication gives

\[
 \boxed{
 T_\omega^*T_\omega
 +\mathsf H_\omega^*\mathsf H_\omega=I.}
 \tag{T-15408.3}
\]

Consequently, for a fixed `kappa in [0,1)`, the following are equivalent:

1. `||mathsf H_omega||<=kappa`;
2. 
   \[
    T_\omega^*T_\omega\succeq(1-\kappa^2)I;
    \tag{T-15408.4}
   \]
3. 
   \[
    \|T_\omega f\|
    \ge\sqrt{1-\kappa^2}\,\|f\|
    \qquad(f\in H^2_+).
    \tag{T-15408.5}
   \]

Thus the requested uniform Hankel moat is exactly a uniform lower singular-value
bound for the complete Toeplitz family.

## Main theorem

Subject to the declared Suzuki normalization and the local factorization audit
in `L-15419/L-15420`, the following are equivalent:

1. the Riemann Hypothesis;
2. 
   \[
    \boxed{
    \exists\,\kappa<1:\quad
    \|\mathsf H_\omega\|\le\kappa
    \quad(0<\omega<1/2);}
    \tag{T-15408.6}
   \]
3. 
   \[
    \boxed{
    \exists\,\eta>0:\quad
    T_\omega^*T_\omega\succeq\eta I
    \quad(0<\omega<1/2).}
    \tag{T-15408.7}
   \]
4. 
   \[
    \boxed{
    \inf_{0<\omega<1/2}
    \inf_{\|f\|=1}\|T_\omega f\|>0.}
    \tag{T-15408.8}
   \]

The parameters are related by

\[
 \eta=1-\kappa^2.
 \tag{T-15408.9}
\]

### Proof

If RH holds, Suzuki's criterion makes every `Theta_omega` inner. Multiplication
then maps `H^2_+` into itself, so

\[
 \mathsf H_\omega=0
 \]

for every `omega`. Thus (T-15408.6) holds with `kappa=0`, and
(T-15408.7)--(T-15408.8) hold with `eta=1`.

Conversely, suppose RH is false. Choose a zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad0<\delta<\frac12.
 \]

`L-15420` identifies the exact local Blaschke-pair singular value

\[
 \frac{\omega}{\delta}
 \]

and the reproducing-kernel localization in the complete scattering symbol gives

\[
 \limsup_{\omega\uparrow\delta}
 \|\mathsf H_\omega\|=1.
 \]

Therefore no `kappa<1` can satisfy (T-15408.6). By (T-15408.3), the lower
singular value of `T_omega` tends to zero along the same offsets, so neither
(T-15408.7) nor (T-15408.8) can hold. This proves the equivalence. QED.

## Quantitative off-line pressure

For the isolated pair factor of an off-line zero,

\[
 \|\mathsf H_\omega\|=\frac\omega\delta,
 \qquad
 m(T_\omega)^2=1-\frac{\omega^2}{\delta^2}.
 \tag{T-15408.10}
\]

Hence near the crossing offset,

\[
 m(T_\omega)
 \sim\sqrt{\frac{2(\delta-\omega)}\delta}.
 \tag{T-15408.11}
\]

A positive proof of (T-15408.7) must therefore prevent this exact square-root
coercivity collapse uniformly at every unknown ordinate and horizontal
displacement.

## What this theorem changes

The target (T-15408.6) is a genuine weakening of exact innerness at each finite
stage, but it is **not** a theorem available below RH. It is another exact
formulation of RH.

This prevents two kinds of circularity:

1. inserting an RH-conditional zero expansion to estimate the Hankel norm;
2. treating a pointwise strict bound `||H_omega||<1` as if compactness supplied
   one uniform moat.

A successful new proof must establish the Toeplitz LMI (T-15408.7) from an
independent arithmetic, canonical-system, or operator inequality.

## Proof-producing interface

A candidate uniform certificate should provide one of:

1. a symbolic Schur-test weight proving a row/column product `<1` for every
   `omega`;
2. a canonical-system transfer inequality giving (T-15408.7) directly;
3. a matrix-valued von Mangoldt-chain dilation with a uniform spectral gap;
4. a complete finite packet plus an ambient tail norm whose sum is `<1`, with a
   symbolic covering of all offsets.

A finite offset grid, pointwise convergence, or a moat deteriorating as
`omega` approaches an unknown crossing is insufficient.

## Gap audit

- The abstract Toeplitz--Hankel equivalence is exact.
- The RH equivalence imports Suzuki's exact innerness normalization.
- The false-RH direction imports the same-ordinate factorization and
  reproducing-kernel localization of `L-15419/L-15420`.
- This theorem proves that the requested bound is RH-equivalent. It does not
  establish the bound unconditionally and therefore does not prove RH.
