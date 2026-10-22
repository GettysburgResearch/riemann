# T-9504 — The positive critical-energy exponent equals the rightmost-zero displacement

Claim ID: `T-9504`  
Title: The integrated totient-discrepancy energy measures the rightmost zeta zero exactly  
Status: `PROPOSED — COMPLETE TRANSFER THEOREM; ZERO EXPONENT NOT SHOWN TO VANISH`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9511`, `L-9512`; standard Mellin abscissa transfer  
Scope: full Riemann Hypothesis  
Related counterexample candidates: none

## Setup

Let

\[
\beta_*=\sup_{\zeta(\rho)=0}\Re\rho,
\qquad
\Theta_\zeta=\beta_*-\frac12.
\tag{T-9504.1}
\]

Let `mathfrak A(x)` be the positive energy from `L-9511`. By `L-9512`, for
`x>=1`,

\[
\mathfrak A(x)
=x^{-4}|E^{\rm AN}(x)|^2
+x^{-5}\left[
\frac{c^2}{20}+\int_1^x|E^{\rm AN}(t)|^2dt
\right],
\qquad c=\frac6{\pi^2}.
\tag{T-9504.2}
\]

Define the energy growth exponent

\[
\boxed{
\Theta_{\rm en}
=\frac12\limsup_{x\to\infty}
\frac{\log(1+x^3\mathfrak A(x))}{\log x}.}
\tag{T-9504.3}
\]

## Exact exponent theorem

One has

\[
\boxed{\Theta_{\rm en}=\Theta_\zeta.}
\tag{T-9504.4}
\]

Consequently,

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak A(x)=O_\varepsilon(x^{-3+\varepsilon})
\quad\text{for every }\varepsilon>0.}
\tag{T-9504.5}
\]

More quantitatively, if RH is false, then for every
`0<=theta<Theta_zeta`,

\[
\boxed{
\sup_{x>=X}
 x^{3-2\theta}\mathfrak A(x)=\infty
\quad\text{for every }X>1.}
\tag{T-9504.6}
\]

Thus an off-line zero cannot be hidden by phase cancellation in the positive
energy: its horizontal displacement appears with twice the exponent.

## Upper bound

Fix `epsilon>0`. Standard Mellin/zero-free-half-plane transfer applied to
(L-9512.11) gives

\[
E^{\rm AN}(x)
=O_\varepsilon(x^{\beta_*+\varepsilon}).
\tag{T-9504.7}
\]

This may be obtained either by contour shifting in every fixed half-plane to
the right of all poles or from the generalized Mertens estimate in the same
zero-free half-plane.

Insert (T-9504.7) into (T-9504.2). Then

\[
\begin{aligned}
x^3\mathfrak A(x)
&\ll_\varepsilon
 x^{-1}x^{2\beta_*+2\varepsilon}
 +x^{-2}\int_1^x t^{2\beta_*+2\varepsilon}dt
 +x^{-2}\\
&\ll_\varepsilon
 x^{2\beta_*-1+2\varepsilon}.
\end{aligned}
\tag{T-9504.8}
\]

Therefore

\[
\Theta_{\rm en}\le\beta_*-\frac12=\Theta_\zeta.
\tag{T-9504.9}
\]

## Lower bound

The endpoint square in (T-9504.2) gives the exact pointwise domination

\[
\boxed{
x^3\mathfrak A(x)
\ge\frac{|E^{\rm AN}(x)|^2}{x}.}
\tag{T-9504.10}
\]

Suppose for contradiction that `Theta_en<theta<Theta_zeta`. Then by the
definition of the limsup, for some `eta>0`,

\[
\mathfrak A(x)=O(x^{-3+2\theta-\eta}).
\tag{T-9504.11}
\]

Equation (T-9504.10) gives

\[
E^{\rm AN}(x)=O(x^{1/2+\theta-\eta/2}).
\tag{T-9504.12}
\]

The Mellin integral in (L-9512.11) would then extend holomorphically to

\[
\Re s>\frac12+\theta-\frac\eta2.
\tag{T-9504.13}
\]

Choose a nontrivial zero `rho` with

\[
\Re\rho>rac12+\theta-rac\eta2.
\]

The right side of (L-9512.11) has a genuine pole at `s=rho`, because
`zeta(rho-1)` and the rational prefactor are nonzero. This contradicts
(T-9504.13). Hence

\[
\Theta_{\rm en}\ge\Theta_\zeta.
\tag{T-9504.14}
\]

Together with (T-9504.9), this proves (T-9504.4).

The same argument proves the tail-unboundedness statement (T-9504.6).

## Logarithmic state form

Put

\[
H(r)=e^{-r/2}\widetilde E^{\rm AN}(e^r),
\tag{T-9504.15}
\]

where `widetilde E^AN` is the complete positive-half-line extension from
`L-9512`. Then `L-9511` gives

\[
\boxed{
e^{3r}\mathfrak A(e^r)
=|H(r)|^2
+\int_0^\infty e^{-2u}|H(r-u)|^2du.}
\tag{T-9504.16}
\]

Thus `Theta_en` is the exponential growth bound of one endpoint-plus-memory
state norm. The Mellin transform of `H` has genuine poles at

\[
z=\rho-\frac12.
\tag{T-9504.17}
\]

The state energy therefore converts the rightmost-zero problem into a positive
Lyapunov-exponent problem.

## Why this is stronger than a scalar phase statement

A scalar explicit formula can be anomalously small at isolated phases. The
energy contains both the current value and a positive exponentially weighted
history. Nevertheless, because the endpoint square is retained, no regularity,
zero simplicity, residue lower bound, or phase recurrence theorem is needed to
recover the exact exponent.

This also identifies a hard proof boundary:

\[
\boxed{
\mathfrak A(x)=O_\varepsilon(x^{-3+\varepsilon})}
\]

is not an auxiliary estimate that can be established by phase-blind positivity.
It is exactly the assertion `Theta_zeta=0`.

## Relation to other repository exponents

Combining this theorem with `T-9503` and `T-19801` gives

\[
\boxed{
\Theta_{\rm en}
=\vartheta_{\rm parabolic\ totient}
=\vartheta_{\rm square\ screw}
=\Theta_\zeta.}
\tag{T-9504.18}
\]

The positive RKHS energy, finite totient scalar, and finite prime-power screw
therefore encode the same full zero spectrum with, respectively, squared,
linear, and prime-side observables.

## Proof boundary

- The exponent identity is complete modulo standard Mellin abscissa transfer.
- It does not show that `Theta_en=0`.
- Hence it does not prove the critical energy bound or RH.
- Any claimed unconditional proof of the critical energy estimate must contain
  genuinely new information excluding the poles in (T-9504.17); positivity of
  the energy alone is insufficient.
