# L-5503 — Smooth-background and gap-aware first-cell bounds

Claim ID: L-5503  
Title: Frozen-vector background motion is Lipschitz in `1/log(c)`, and eigenvector rotation is second order across a spectral gap  
Status: PROPOSED  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; finite-dimensional spectral theorem  
Scope: exclusion and promotion bounds for threshold-directed carrier searches  
Related counterexample candidates: none

## Statement A — frozen-vector smooth background

Fix a vector `v`, set `c_K=0`, and define

\[
 D_v=\max_{0\le d<K}
 \left(
  |\operatorname{Re}(c_{d+1}-c_d)|
  +|\operatorname{Im}(c_{d+1}-c_d)|
 \right).
\]

Let `L_0<L_1`, and suppose no new prime power other than a separately treated
event is admitted in the interval. For the old prime-power set `Q_0`, put

\[
 W_0=\sum_{q\in Q_0}
 \frac{\Lambda(q)}{\pi\sqrt q}\log q.
\]

Then for every `L in [L_0,L_1]`, the old frozen-vector prime background obeys

\[
 \boxed{
 |P_{v,\mathrm{old}}(L)-P_{v,\mathrm{old}}(L_0)|
 \le K D_v W_0
 \left|\frac1L-\frac1{L_0}\right|.
 }
\]

This remains valid when terms cross deposition knots.

If a newly entering event has an upper harmful contribution `E_q^+(L)` and a
directed lower bound `m_0` for the leading margin at `L_0+`, then

\[
 \boxed{
 M_v(L)\ge
 m_0-KD_vW_0\left(\frac1{L_0}-\frac1L\right)-E_q^+(L).
 }
\]

A positive lower endpoint after subtracting the nonprime gate certifies the
whole first microcell for the frozen vector.

## Statement B — gap-aware eigenvalue motion

Let `A` be Hermitian with a unit top eigenvector `v`, top eigenvalue `lambda_1`,
and second eigenvalue `lambda_2`. Let `E` be Hermitian and set

\[
 \mu=v^*(A+E)v,
 \qquad
 r=\|(I-vv^*)Ev\|,
 \qquad
 \beta=\lambda_2+\|E\|_2.
\]

If `mu>beta`, then

\[
 \boxed{
 \mu\le\lambda_{\max}(A+E)
 \le\mu+\frac{r^2}{\mu-\beta}.
 }
\]

Thus, once a spectral gap survives the perturbation, the error made by following
a frozen leading vector is quadratic in the off-eigenspace residual rather than
linear in the full perturbation norm.

For a leading screen `Q=alpha I-S`, this gives the lower bound

\[
 \lambda_{\min}(Q)
 \ge\alpha-\mu-\frac{r^2}{\mu-\beta}.
\]

## Proof of Statement A

As a function of

\[
 r=\frac{K\log q}{L},
\]

the piecewise-linear autocorrelation interpolant joins consecutive values
`c_d`. On each segment its real and imaginary slopes are the corresponding
coordinate differences, and crossing knots does not change the global
coordinatewise Lipschitz constant `D_v`. Therefore

\[
 |\operatorname{Re}(u_q(\rho_q(L)-\rho_q(L_0)))|
 \le D_v K\log q\left|\frac1L-\frac1{L_0}\right|
\]

for every unit phase `u_q`. Multiply by the nonnegative prime amplitude and sum.
The margin inequality follows because the prime value is subtracted from the
leading scalar. ∎

## Proof of Statement B

Decompose the space as `span(v) plus v^perp`. In this decomposition

\[
 A+E=\begin{pmatrix}\mu&b^*\\b&C\end{pmatrix},
 \qquad\|b\|=r,
 \qquad\lambda_{\max}(C)\le\beta.
\]

For a unit vector with component magnitudes `x,y`, its Rayleigh quotient is at
most

\[
 \mu x^2+2rxy+\beta y^2.
\]

The largest value is the top eigenvalue of the scalar matrix

\[
 \begin{pmatrix}\mu&r\\r&\beta\end{pmatrix},
\]

namely

\[
 \frac{\mu+\beta+\sqrt{(\mu-\beta)^2+4r^2}}2.
\]

For `d=mu-beta>0`,

\[
 \sqrt{d^2+4r^2}\le d+\frac{2r^2}{d},
\]

which proves the upper bound. The lower bound is the Rayleigh quotient at `v`.
∎

## Motivation

Statement A is a cheap fail-safe for very short microcells. L-5502 is sharper
when every knot is explicitly processed. Statement B explains when a frozen
vector is enough to control the moving extremal eigenvalue and gives a
proof-oriented alternative to repeated interval eigensolves.

## Analytic domain audit

Statement A uses finite prime sums and real positive logarithms. Statement B is
pure finite-dimensional Hermitian linear algebra.

## Dependency audit

D-0801/L-0801 supply the autocorrelation interpolation. The spectral statement
uses only the min-max principle and an elementary two-by-two eigenvalue formula.

## Gap audit

- Statement A requires a complete old-prime set and separately accounts for
  every newly admitted event.
- `D_v` must be computed from the exact frozen vector, not a floating proxy.
- The coarse bound may be far weaker than the exact knot mesh.
- In Statement B, `beta` must be a rigorous upper bound and `mu>beta` must be
  interval-separated.
- A large midpoint spectral gap is not a certified gap.

## Adversarial tests

1. Use a vector with alternating correlations to force the coordinatewise
   `L1` bound to be nearly sharp.
2. Cross several deposition knots and compare with direct endpoint values.
3. Test the two-by-two matrix where the spectral bound is exact before the final
   rational relaxation.
4. Let `mu` approach `beta`; the certificate must become unresolved.
5. Compare against Weyl's coarser `||E||` bound.

## Remaining uncertainty

No proof gap is known. Practical use of Statement B requires exported gap and
residual enclosures that the current production branch does not yet provide.

## Suggested next attack

For each nominated threshold, accumulate a directed fixed-vector value,
background norm, corner residual, and complement bound in one stream. Use the
quadratic correction only when it is materially sharper than Weyl.
