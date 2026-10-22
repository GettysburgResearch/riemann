# L-19811 — Causal/anti-causal prime projection identity

Claim ID: `L-19811`  
Title: The gap-one energy is exactly the anti-causal residue energy generated when the causal Euler source is continued across the strip  
Status: `PROPOSED — COMPLETE HARDY/PLANCHEREL IDENTITY; REFLECTION BOUND OPEN`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: `L-19810`; the absolutely convergent Euler logarithmic derivative for `Re s>1`; Hardy projections and contour displacement  
Scope: prime-side formulation of the exact minimum-phase inequality

## 1. Fourier and Hardy conventions

Use

\[
 \widehat f(u)=\int_{\mathbb R}f(t)e^{-itu}\,dt,
 \qquad
 f(t)={1\over2\pi}\int_{\mathbb R}\widehat f(u)e^{itu}\,du,
 \tag{L-19811.1}
\]

and let the Hilbert transform satisfy

\[
 \widehat{\mathcal Hf}(u)=-i\,\operatorname{sgn}(u)\widehat f(u).
 \tag{L-19811.2}
\]

Thus upper-half-plane Hardy boundary functions have Fourier support in
`[0,infinity)`. Write `P_+` and `P_-` for the positive- and negative-frequency
projections.

Fix

\[
 \sigma={1\over2}+\omega,
 \qquad 0<\omega<{1\over2},
 \tag{L-19811.3}
\]

and retain the pole-free damped transfer

\[
 G_{\sigma,M}(z)
 =(z+i)^{-M}(\sigma-iz-1)\zeta(\sigma-iz)
 \tag{L-19811.4}
\]

from `T-19805/L-19810`. Its boundary logarithmic derivative is

\[
 D_{\sigma,M}(t)={d\over dt}\log G_{\sigma,M}(t).
 \tag{L-19811.5}
\]

The damping exponent is chosen large enough that the regularized boundary
objects below are in `L2`; the final anti-causal quantity is independent of
`M`.

## 2. The high-line Euler source is exactly causal

Let `v>1-sigma`. On the horizontal line `z=t+iv`, one has

\[
 s=\sigma-iz=\sigma+v-it,
 \qquad \Re s>1.
\]

The Euler series is absolutely convergent and gives

\[
\boxed{
\begin{aligned}
D_{\sigma,M}(t+iv)
={}&-{i\over\sigma+v-1-it}\\
&+i\sum_{n\ge2}\Lambda(n)n^{-\sigma-v}e^{it\log n}\\
&-{M\over t+i(v+1)}.
\end{aligned}}
\tag{L-19811.6}
\]

Every term has nonnegative Fourier support. Indeed,

\[
 {1\over a-it}=\int_0^\infty e^{-au}e^{itu}\,du
 \qquad(a>0),
 \tag{L-19811.7}
\]

and the prime terms have frequencies `log n>0`. Consequently

\[
\boxed{
 P_-D_{\sigma,M}(\cdot+iv)=0
 \qquad(v>1-\sigma).}
\tag{L-19811.8}
\]

This is the exact causal prime-side starting point. No zero information appears
on the high line.

## 3. Lowering the line creates only zero residues

Let

\[
 \rho=\beta+i\gamma
 \tag{L-19811.9}
\]

be a nontrivial zeta zero of multiplicity `m_rho`. It becomes a zero of
`G_(sigma,M)` at

\[
 p_\rho=-\gamma+i(\beta-\sigma).
 \tag{L-19811.10}
\]

It lies in the upper half-plane exactly when `beta>sigma`. The logarithmic
derivative has principal part

\[
 {m_\rho\over z-p_\rho}.
 \tag{L-19811.11}
\]

For `u<0`, contour closure in the upper half-plane gives

\[
 \int_{\mathbb R}{e^{-itu}\over t-p_\rho}\,dt
 =2\pi i\,e^{-ip_\rho u}.
 \tag{L-19811.12}
\]

Lower the line from `Im z=v` to the boundary. The horizontal sides vanish after
the harmless damping, and the pole at `s=1` has already been removed in
(L-19811.4). Therefore, first for a finite rectangle and then by the standard
symmetric limiting procedure,

\[
\boxed{
 \widehat{P_-D_{\sigma,M}}(u)
 =2\pi i
 \sum_{\substack{\zeta(\rho)=0\\\beta>\sigma}}
 m_\rho e^{(\beta-\sigma)u}e^{i\gamma u},
 \qquad u<0.}
\tag{L-19811.13}
\]

If the right side does not define an `L2` function, all subsequent energies are
interpreted as `+infinity`. Formula (L-19811.13) is independent of `M`.

Thus analytic continuation from the Euler line to the critical strip is a
Wiener--Hopf reflection: the high-line source is causal, and every zero crossed
creates one anti-causal exponential.

## 4. Exact Plancherel formula for the Hilbert residual

Write

\[
 D_{\sigma,M}=A+iB,
 \qquad A,B\text{ real-valued},
 \tag{L-19811.14}
\]

and define

\[
 p_\omega=B-\mathcal HA
 \tag{L-19811.15}
\]

as in `L-19810`. For `u<0`, (L-19811.2) gives

\[
 \widehat p_\omega(u)
 =\widehat B(u)-i\widehat A(u)
 =-i\widehat D_{\sigma,M}(u).
 \tag{L-19811.16}
\]

Since `p_omega` is real, its positive- and negative-frequency energies agree.
Insert (L-19811.13) into Plancherel and put `u=-x`. This yields the exact identity

\[
\boxed{
 \int_{\mathbb R}p_\omega(t)^2\,dt
 =4\pi\int_0^\infty
 \left|
 \sum_{\substack{\zeta(\rho)=0\\\beta>\sigma}}
 m_\rho e^{-(\beta-\sigma)x}e^{-i\gamma x}
 \right|^2dx.}
\tag{L-19811.17}
\]

Hence the normalized gap-one energy is

\[
\boxed{
 \mathcal E_\omega
 =(1-2\omega)\int_0^\infty
 \left|
 \sum_{\substack{\zeta(\rho)=0\\\beta>1/2+\omega}}
 m_\rho e^{-(\beta-1/2-\omega)x}e^{-i\gamma x}
 \right|^2dx.}
\tag{L-19811.18}
\]

Equation (L-19811.18) is the time-domain form of `L-19810.12`. It is not a
phase-blind estimate: every cross term between right-of-line zeros is retained.

## 5. Prime-side reflection operator

Let `q_(sigma,v)` denote the explicit causal distribution supplied by the
right-hand side of (L-19811.6), viewed in positive-frequency coordinates. Let

\[
 \mathscr R_{\sigma,v}q_{\sigma,v}
 =\sum_{\beta>\sigma}
 m_\rho e^{-(\beta-\sigma)x}e^{-i\gamma x},
 \qquad x>0,
 \tag{L-19811.19}
\]

be the anti-causal residue output obtained by lowering the line. This defines the
exact Wiener--Hopf reflection map on the zeta source. The desired strict upper
bound is now

\[
\boxed{
 (1-2\omega)
 \|\mathscr R_{\sigma,v}q_{\sigma,v}\|_{L^2(0,\infty)}^2<1,
 \qquad\sigma={1\over2}+\omega.}
\tag{L-19811.20}
\]

Thus the missing theorem is not an estimate for the causal Euler coefficients
alone. It is a contraction estimate for the analytic-continuation reflection
map carrying those coefficients into the anti-causal channel.

## 6. Why the reversible Dirichlet form alone cannot give the bound

The reversible convolution of `L-19809` fixes the boundary amplitude and gives a
positive quadratic form for the self-adjoint causal transfer. In the Hardy
splitting, however,

\[
 P_+L^2\perp P_-L^2.
 \tag{L-19811.21}
\]

The high-line Euler source lies entirely in `P_+`, while the target in
(L-19811.20) lies entirely in `P_-`. Consequently an inequality involving only

\[
 \langle f,(I-K_\omega)f\rangle
 \tag{L-19811.22}
\]

or only the boundary modulus of the completed-zeta characteristic function does
not control (L-19811.20) without an additional theorem binding the causal and
anti-causal channels.

The required new input must therefore be one of:

1. a true minimum-phase theorem for the completed-zeta transfer;
2. a positive Weyl/de Branges kernel whose positivity forces the reflection to
   vanish;
3. a direct contractive estimate for `mathscr R_(sigma,v)` on this one arithmetic
   source.

The next lemma constructs the exact Weyl/de Branges bridge.

## 7. Proof boundary

- The high-line causal expansion is an absolutely convergent prime identity.
- The negative-frequency formula follows by contour displacement and residues;
  truncation and damping provide the standard rigorous limiting interface.
- The Plancherel constants are exact in convention (L-19811.1).
- This lemma identifies the prime-side operator that must be bounded, but does
  not prove its norm on the zeta source is below the gap-one threshold.
- No proof of RH is claimed.