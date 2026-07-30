# T-15102 — Reduced positive RH criterion from exact radical leakage

Claim ID: `T-15102`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Dependencies: `L-15101`, `L-15102`, `T-15101`, the finite CCM simple-even real-zero theorem, the CCM Fourier--Mellin normalization, and Hurwitz's theorem  
Scope: one continuum asymptotic estimate sufficient for RH  
Related counterexample candidates: none

## Statement

Let `k=E(h)` be the exact global Weil-radical target of `L-15101`, so that

\[
 \widehat k=\Xi.
\]

Let

\[
 \lambda_j\to\infty,
 \qquad
 0<\tau_j<\frac12,
 \qquad
 \tau_j\nearrow\frac12.
 \tag{T-15102.1}
\]

For each `j`, choose a smooth inversion-even localization `chi_j` supported in
`[lambda_j^-1,lambda_j]` and set

\[
 p_j=\chi_jk,
 \qquad
 t_j=(1-\chi_j)k.
 \tag{T-15102.2}
\]

Assume the following exact interfaces.

### A. Global/local form compatibility

The global Weil form `QW` and the localized form `q_j` share a form domain on
which

\[
 QW(k,f)=0,
 \qquad
 q_j(p_j,w)=QW(p_j,w)=-QW(t_j,w)
 \tag{T-15102.3}
\]

for every local form-domain vector `w`.

### B. Continuum localized spectral gates

The localized form is closed, lower bounded, parity invariant, and represented
by a compact-resolvent operator `A_j`. The target `p_j` is even and nonzero.
Put

\[
 \mu_j=\frac{q_j(p_j,p_j)}{\|p_j\|^2}.
\]

There are numbers

\[
 U_j\ge\mu_j,
 \qquad
 h_j>0,
 \qquad
 g_{j,-}>0
 \tag{T-15102.4}
\]

such that

\[
 q_j(w,w)-U_j\|w\|^2
 \ge h_j\|w\|_{\lambda_j,\tau_j}^2
 \tag{T-15102.5}
\]

for every even local `w perpendicular p_j`, and

\[
 q_j(w,w)-U_j\|w\|^2
 \ge g_{j,-}\|w\|^2
 \tag{T-15102.6}
\]

for every odd local `w`.

Define the exact Hardy-dual leakage

\[
 \ell_j
 =\sup_{\substack{0\ne w\ {m even}\\w\perp p_j}}
   \frac{|QW(t_j,w)|}
        {\|w\|_{\lambda_j,\tau_j}}.
 \tag{T-15102.7}
\]

Assume

\[
 \boxed{
 \|t_j\|_{\tau_j}+\frac{\ell_j}{h_j}
 \longrightarrow0.}
 \tag{T-15102.8}
\]

### C. Finite form-core interface

For every fixed `j`, the CCM Fourier spaces

\[
 E_N(\lambda_j)
\]

are nested parity-invariant form cores for `q_j`, and the imported CCM theorem
applies whenever their exact finite ground eigenvalue is simple and even.

Then the Riemann hypothesis is true.

## Proof

### 1. Continuum ground states approach the exact target

By `L-15102`, the gates (T-15102.5)--(T-15102.6) certify that the continuum
localized ground eigenvalue is simple and its normalized eigenvector `xi_j` is
even. For a suitable nonzero real scalar `c_j`,

\[
 \|c_j\xi_j-p_j\|_{\lambda_j,\tau_j}
 \le\frac{\ell_j}{h_j}.
 \tag{T-15102.9}
\]

Since `k=p_j+t_j`,

\[
 \boxed{
 \|c_j\xi_j-k\|_{\tau_j}
 \le\|t_j\|_{\tau_j}+\frac{\ell_j}{h_j}
 \longrightarrow0.}
 \tag{T-15102.10}
\]

### 2. Finite ground states may be chosen diagonally

For fixed `j`, `T-15101` applies to the form-core sequence. Thus all sufficiently
large finite truncations have a simple even ground vector `xi_(j,N)`, and these
ground lines converge to the continuum line in ordinary and form norm.

The Hardy norm is bounded by the ordinary norm on the fixed compact support.
Therefore choose `N_j` large enough that, after consistent real normalization,

\[
 \|c_j\xi_{j,N_j}-c_j\xi_j\|_{\lambda_j,\tau_j}
 \le 2^{-j}.
 \tag{T-15102.11}
\]

The cutoffs `N_j` may also be chosen strictly increasing.

Combining with (T-15102.10),

\[
 \|c_j\xi_{j,N_j}-k\|_{\tau_j}\longrightarrow0.
 \tag{T-15102.12}
\]

### 3. Hardy convergence gives local-uniform transform convergence

Fix a compact set `K` in `|Im z|<1/2`. Choose

\[
 \max_{z\in K}|\operatorname{Im}z|<\sigma<\tau<\frac12.
\]

Eventually `tau_j>=tau`, and monotonicity of the Hardy weights gives convergence
in the fixed `tau` norm. The exact transform estimate of `T-14301` yields

\[
 \sup_{z\in K}
 |\widehat{c_j\xi_{j,N_j}}(z)-\Xi(z)|\longrightarrow0.
 \tag{T-15102.13}
\]

### 4. Hurwitz forces all Xi zeros to be real

Every finite ground transform in (T-15102.13) is entire and has only real zeros
by the imported CCM simple-even theorem. On any disk compactly contained in the
open strip and disjoint from the real axis, all approximants are nonvanishing.
Hurwitz's theorem therefore prevents `Xi` from having a zero in that disk.

Every nontrivial zeta zero corresponds to a point strictly inside this centered
strip, and that point is real exactly when the zero has real part `1/2`.
Therefore every nontrivial zero lies on the critical line. RH follows. QED.

## Explicit sufficient asymptotic form

Suppose one proves a form-continuity estimate

\[
 |QW(t_j,w)|
 \le C_j\|t_j\|_{X_j}
          \|w\|_{\lambda_j,\tau_j}.
 \tag{T-15102.14}
\]

Then

\[
 \ell_j\le C_j\|t_j\|_{X_j},
\]

and (T-15102.8) follows from

\[
 \boxed{
 \|t_j\|_{\tau_j}	o0,
 \qquad
 \frac{C_j}{h_j}\|t_j\|_{X_j}\to0.}
 \tag{T-15102.15}
\]

The first condition is already explicit and super-Gaussian in `L-15101`.
Therefore an estimate of the shape

\[
 \|t_j\|_{X_j}\le A\lambda_j^m e^{-c\lambda_j^2},
 \qquad
 \frac{C_j}{h_j}\le e^{c'\lambda_j^2},
 \qquad c'<c,
 \tag{T-15102.16}
\]

would close the theorem. This formulation shows exactly how much continuum gap
collapse the Gaussian radical tail can tolerate.

## Improvement over T-14301

`T-14301` requires a diagonal family of finite ground states to approach an
explicit prolate target. The present theorem removes two independent burdens:

1. the target is already an exact global Weil-radical vector with transform
   `Xi`, so there is no ambient prolate eigen-defect;
2. finite cutoff simplicity, parity, and convergence follow from the continuum
   spectral gates by `T-15101`.

The sole structural estimate is now

\[
 \boxed{
 \text{localized radical-tail leakage}
 \ /
 \text{continuum even-complement coercivity}
 \longrightarrow0.}
\]

## Proof boundary

This is a complete implication, not a completed proof of RH. The following
remain unproved:

- exact global/local Weil form compatibility for the chosen smooth multiplier;
- a usable unconditional continuity bound `C_j` for the leakage form;
- continuum simple-even coercivity and a lower estimate for `h_j` as support
  grows;
- the final asymptotic comparison in (T-15102.15).

No finite collection of positive matrices establishes these conditions.
