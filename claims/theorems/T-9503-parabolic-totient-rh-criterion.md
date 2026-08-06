# T-9503 — Minimal parabolic totient criterion for RH

Claim ID: `T-9503`  
Title: RH is equivalent to the critical error of one two-Green finite totient average  
Status: `PROPOSED — COMPLETE TRANSFER THEOREM; RH BOUND OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9510`; the classical Mertens-function equivalence to RH; Mellin inversion  
Scope: full Riemann Hypothesis  
Related counterexample candidates: none

## Criterion

For real `x>1`, define

\[
\boxed{
\mathcal P(x)=
\frac1x\sum_{1\le n<x}
 \frac{\varphi(n)}n
 \left(1-\frac{n^2}{x^2}\right).}
\tag{T-9503.1}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\mathcal P(x)=\frac4{\pi^2}
+O_\varepsilon(x^{-3/2+\varepsilon})
\quad\text{for every }\varepsilon>0.}
\tag{T-9503.2}
\]

This is the minimal polynomial smoothing in the new family: one quadratic
cutoff, one finite totient sum, and a two-factor rational Mellin kernel.

## Exact Mellin transform

The cutoff weight is

\[
w_1(u)=(1-u^2)\mathbf1_{0<u<1},
\]

with

\[
\boxed{
\widehat w_1(z)
=\int_0^1(1-u^2)u^{z-1}du
=\frac2{z(z+2)}.}
\tag{T-9503.3}
\]

Therefore, for `c>1`,

\[
\boxed{
\mathcal P(x)=
\frac1{2\pi i}\int_{(c)}
 \frac2{z(z+2)}
 \frac{\zeta(z)}{\zeta(z+1)}
 x^{z-1}dz.}
\tag{T-9503.4}
\]

The pole at `z=1` contributes

\[
\frac{2}{3\zeta(2)}
=\frac4{\pi^2}.
\tag{T-9503.5}
\]

The apparent kernel poles are canceled:

- at `z=0`, by the pole of `zeta(z+1)`;
- at `z=-2`, by the trivial zero of `zeta(z)`.

Every nontrivial zero `rho` gives a genuine pole

\[
\boxed{z=\rho-1.}
\tag{T-9503.6}
\]

because `zeta(rho-1)` is nonzero and the rational kernel has no zero.

## RH implies the estimate

RH is equivalent to the classical Mertens bound

\[
M(X)=\sum_{n\le X}\mu(n)
=O_\varepsilon(X^{1/2+\varepsilon})
\tag{T-9503.7}
\]

for every `epsilon>0`.

Applying `L-9510` with `beta=1/2` gives

\[
\mathcal P(x)-\frac4{\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon}).
\]

This direction uses no zero simplicity, no zero derivative, and no delicate
vertical contour estimate.

## The estimate implies RH

Let

\[
\mathcal E_1(x)=\mathcal P(x)-\frac4{\pi^2}.
\]

For `Re z>1`, direct Mellin integration gives

\[
\boxed{
\frac2{z(z+2)}
 \frac{\zeta(z)}{\zeta(z+1)}
-\frac{4/\pi^2}{z-1}
=\int_1^\infty\mathcal E_1(x)x^{-z}dx.}
\tag{T-9503.8}
\]

The critical estimate makes the right side analytic for

\[
\Re z>-\frac12.
\]

Any zero `rho` with `Re rho>1/2` would give the genuine pole `rho-1` in that
half-plane. Hence no such zero exists. The functional equation excludes the
reflected left-side zero, and RH follows.

## Exact rightmost-zero exponent

Put

\[
\beta_*=\sup_{\zeta(\rho)=0}\Re\rho,
\qquad
\Theta_\zeta=\beta_*-\frac12.
\tag{T-9503.9}
\]

Define

\[
\vartheta_1=\inf\left\{\theta\ge0:
 \mathcal E_1(x)
 =O_\varepsilon(x^{-3/2+\theta+\varepsilon})
 \text{ for every }\varepsilon>0
\right\}.
\tag{T-9503.10}
\]

Then

\[
\boxed{\vartheta_1=\Theta_\zeta.}
\tag{T-9503.11}
\]

The upper bound follows by combining the generalized Mertens estimate in every
zero-free half-plane with `L-9510`. The lower bound follows because a stronger
error exponent would analytically continue (T-9503.8) through a genuine pole
`rho-1`.

Therefore

\[
\boxed{
\vartheta_{\rm parabolic\ totient}
=\vartheta_{\rm quartic\ totient}
=\vartheta_{\rm square\ screw}
=\Theta_\zeta.}
\tag{T-9503.12}
\]

## Prime-dilation cascade

For finite prime sets, define the centered parabolic discrepancy exactly as in
`L-9509` with the new weight. Prime adjoining still gives

\[
D_{P\cup\{p\}}(x)=D_P(x)-p^{-2}D_P(x/p).
\tag{T-9503.13}
\]

At the critical normalization

\[
H_P(r)=e^{3r/2}D_P(e^r),
\]

this becomes

\[
\boxed{
H_{P\cup\{p\}}(r)
=H_P(r)-p^{-1/2}H_P(r-\log p).}
\tag{T-9503.14}
\]

The full RH criterion is therefore equivalent to subexponential growth of the
all-prime output of the same multiplicative wavelet cascade, now applied to the
minimal two-Green seed

\[
e^{-r}-e^{-3r}.
\]

## Exact finite arithmetic form

`L-9510` gives

\[
\begin{aligned}
\mathcal E_1(x)={}&
-\frac23\sum_{d\ge x}\frac{\mu(d)}{d^2}
-\frac1{2x}\sum_{d<x}\frac{\mu(d)}d\\
&-\frac1{x^2}\sum_{d<x}
 \mu(d)B_2(\{x/d\})\\
&+\frac1{3x^3}\sum_{d<x}
 \mu(d)d B_3(\{x/d\}).
\end{aligned}
\tag{T-9503.15}
\]

This is the smallest current proof-facing attack surface: two periodic
Bernoulli channels plus the two ordinary Mertens tails.

## Why this is stronger strategically than another finite matrix

Proving

\[
\boxed{
\mathcal P(x)-\frac4{\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon})}
\tag{T-9503.16}
\]

ends the full problem immediately. No packet exhaustion, support selection,
source right inverse, Schur complement, compactness theorem, or separate
finite-to-global transfer remains afterward.

The criterion is still RH-equivalent; the estimate is not proved here.

## Proof-producing interface

For rational `x`, the finite sum is rational. At integer `x`, a certificate
requires only exact totients and rational arithmetic; `pi^2` enters solely in
the main constant comparison.

A finite ladder cannot prove the asymptotic bound.

## Independent-review targets

1. Verify the rational Mellin kernel and residue.
2. Audit cancellation at `z=0,-2` and noncancellation at `rho-1`.
3. Reconstruct the Mertens transfer in `L-9510`.
4. Verify the exact rightmost-zero exponent.
5. Compare the two-Green seed with the terminal-prime and square-screw kernels.
