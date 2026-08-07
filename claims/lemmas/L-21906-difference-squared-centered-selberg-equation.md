# L-21906 — Difference-squared centered Selberg equation

Claim ID: `L-21906`  
Title: One first difference of the centered prime measure has a closed nonlinear equation whose quadratic term is its own positive convolution square  
Status: **PROPOSED — COMPLETE DISTRIBUTIONAL AND LAPLACE ALGEBRA**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: the centered Selberg equation of `L-21503/L-21905`; elementary translation-convolution algebra  
Scope: corrected nonlinear starting point after the `R-21903` positive-Hankel barrier

## 1. Translation convention

Let `tau_h` denote right translation of a measure by `h>0`:

\[
 \int f(y)\,d(\tau_h\mu)(y)
 =\int f(y+h)\,d\mu(y).
 \tag{L-21906.1}
\]

Put

\[
 \Delta_h=I-\tau_h.
 \tag{L-21906.2}
\]

Translations commute with additive convolution and

\[
 (\Delta_h\nu)*(\Delta_h\nu)
 =\Delta_h^2(\nu*\nu).
 \tag{L-21906.3}
\]

The centered prime measure satisfies

\[
 \boxed{
 \mathscr L\nu+\nu*\nu=R,
 }
 \tag{L-21906.4}
\]

where

\[
 \mathscr L\nu=y\,d\nu+2dP_0*d\nu,
 \qquad
 dP_0(y)=e^{y/2}{\bf1}_{y\ge0}dy.
 \tag{L-21906.5}
\]

## 2. Exact commutator

Multiplication by `y` obeys

\[
 y\,d(\tau_h\mu)
 =\tau_h(y\,d\mu)+h\,d(\tau_h\mu),
 \tag{L-21906.6}
\]

while convolution by `P_0` commutes with translation.  Hence

\[
 \boxed{
 \mathscr L\tau_h
 =\tau_h\mathscr L+h\tau_h.
 }
 \tag{L-21906.7}
\]

Equivalently,

\[
 \boxed{
 \Delta_h\mathscr L
 =\mathscr L\Delta_h+h\tau_h.
 }
 \tag{L-21906.8}
\]

Applying this identity twice gives

\[
 \boxed{
 \Delta_h^2\mathscr L\nu
 =\mathscr L\Delta_h^2\nu
  +2h\tau_h\Delta_h\nu.
 }
 \tag{L-21906.9}
\]

## 3. Closed equation for the first difference

Define

\[
 \boxed{
 \mu_h=\Delta_h\nu.
 }
 \tag{L-21906.10}
\]

Then `Delta_h^2 nu=Delta_h mu_h`.  Applying `Delta_h^2` to
(L-21906.4), and using (L-21906.3) and (L-21906.9), yields

\[
 \boxed{
 \mathscr L_h\mu_h+\mu_h*\mu_h
 =\Delta_h^2R,
 }
 \tag{L-21906.11}
\]

where the new linear operator is

\[
 \boxed{
 \mathscr L_h
 =\mathscr L\Delta_h+2h\tau_h.
 }
 \tag{L-21906.12}
\]

This equation is closed in `mu_h`.  No undifferenced copy of `nu` remains.
Most importantly, the nonlinear term is the literal self-convolution of the
same differenced measure.

The difference has the formal mass cancellation

\[
 \langle\mu_h,1\rangle=0
 \tag{L-21906.13}
\]

whenever the pairing is interpreted by compact truncation or by its Laplace
transform.  Thus conditionally positive kernels become a legitimate additional
possibility, provided their exact moment hypotheses are stated.

## 4. Adjoint operator

The translation adjoint is

\[
 (\tau_h^*f)(y)=f(y+h).
 \tag{L-21906.14}
\]

Therefore

\[
 \boxed{
 \mathscr L_h^*f
 =(I-\tau_h^*)\mathscr L^*f
  +2h\tau_h^*f.
 }
 \tag{L-21906.15}
\]

Explicitly,

\[
 \boxed{
 (\mathscr L_h^*f)(y)
 =(\mathscr L^*f)(y)
 -(\mathscr L^*f)(y+h)
 +2h f(y+h).
 }
 \tag{L-21906.16}
\]

For every positive-Hankel test `f`, pairing (L-21906.11) gives

\[
 \boxed{
 \langle\mu_h,\mathscr L_h^*f\rangle
 +\iint f(x+y)d\mu_h(x)d\mu_h(y)
 =\langle\Delta_h^2R,f\rangle,
 }
 \tag{L-21906.17}
\]

with a nonnegative quadratic term.

## 5. Laplace form

Let

\[
 H(z)=\langle\nu,e^{-z\,\cdot}\rangle,
 \qquad
 M_h(z)=(1-e^{-hz})H(z),
 \tag{L-21906.18}
\]

and let

\[
 \mathcal R(z)=\langle R,e^{-z\,\cdot}\rangle.
 \]

The original Riccati equation is

\[
 -H'(z)+{2\over z-1/2}H(z)+H(z)^2=\mathcal R(z).
 \tag{L-21906.19}
\]

Put

\[
 a_h(z)=1-e^{-hz}.
 \]

Substituting `M_h=a_hH` into (L-21906.19) gives exactly

\[
 \boxed{
 -a_h M_h'
 +\left[
   he^{-hz}+{2a_h\over z-1/2}
  \right]M_h
 +M_h^2
 =a_h^2\mathcal R.
 }
 \tag{L-21906.20}
\]

This is the Laplace transform of (L-21906.11).

## 6. Relation to the prime-only and Haar routes

The boundary difference in `T-21502` is precisely multiplication by
`1-e^{-z}`.  The second difference appearing in the nonlinear equation is
therefore not an artificial regularizer: it is the exact operation which turns
Selberg's quadratic prime term into the square of the prime-only centered
measure.

Likewise, the Haar/dilation constructions use finite differences to remove the
long ramp and the pole model before asking for a sign.  Equation
(L-21906.11) is the common nonlinear identity behind those routes.

## 7. What this repairs

`R-21903` shows that the undifferenced positive-Hankel adjoint cone cannot absorb
the long constant-coordinate stop-loss kernel.  The differenced equation makes
two changes simultaneously:

1. it annihilates the polynomial/ramp moments responsible for the decay
   mismatch;
2. it retains the complete quadratic arithmetic channel as a nonnegative
   self-square.

A complete proof still requires a positive or conditionally positive adjoint
for the **actual differenced target kernel** and a cofinal bound for the
explicit forcing `Delta_h^2R`.  Those are arithmetic obligations, not automatic
consequences of (L-21906.11).

## 8. Proof boundary

- The translation commutator, closed measure equation, adjoint, and Laplace
  equation are exact.
- No RH assumption enters.
- The equation does not itself prove the prime-only Hardy energy bound or the
  dyadic knot inequalities.
- It replaces the structurally impossible undifferenced local-residual plan by
  the correct square-preserving nonlinear starting point.
