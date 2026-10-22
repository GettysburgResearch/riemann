# L-21503 — Selberg log-convolution Riccati identity

Claim ID: `L-21503`  
Title: The centered logarithmic prime measure satisfies one exact nonlinear Volterra equation whose filtered energy is the global RH obstruction  
Status: `PROPOSED — COMPLETE ARITHMETIC IDENTITY; DISSIPATIVE ESTIMATE OPEN`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Dependencies: Selberg's elementary convolution identity

## 1. Weighted logarithmic prime measure

On the additive logarithmic half-line define

\[
 dP(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \delta_{\log n}(dy).
 \tag{L-21503.1}
\]

Let convolution be additive convolution of measures on `[0,infinity)`. Define

\[
 dC(y)=\sum_{n\ge1}
 \frac{(\mu*\log^2)(n)}{\sqrt n}
 \delta_{\log n}(dy),
 \tag{L-21503.2}
\]

where

\[
 (\mu*\log^2)(n)
 =\sum_{d\mid n}\mu(d)\log^2(n/d).
\]

Selberg's exact coefficient identity is

\[
 \boxed{
 \Lambda(n)\log n+(\Lambda*\Lambda)(n)
 = (\mu*\log^2)(n).}
 \tag{L-21503.3}
\]

Dividing by `sqrt(n)` and using

\[
 \frac1{\sqrt a\sqrt b}=\frac1{\sqrt{ab}}
\]

turns it into the exact measure equation

\[
 \boxed{
 y\,dP+dP*dP=dC.}
 \tag{L-21503.4}
\]

No asymptotic prime theorem is used.

## 2. Center the zeta pole before estimating

Let

\[
 dP_0(y)=e^{y/2}\mathbf1_{y\ge0}\,dy
 \tag{L-21503.5}
\]

and define the centered measure

\[
 d\nu=dP-dP_0.
 \tag{L-21503.6}
\]

The model terms satisfy

\[
 y\,dP_0+dP_0*dP_0
 =2y e^{y/2}\,dy,
 \tag{L-21503.7}
\]

because

\[
 (dP_0*dP_0)(y)
 =\int_0^ye^{u/2}e^{(y-u)/2}du
 =y e^{y/2}.
\]

Consequently (L-21503.4) is exactly

\[
 \boxed{
 y\,d\nu
 +2dP_0*d\nu
 +d\nu*d\nu
 =dR,}
 \tag{L-21503.8}
\]

where the explicit signed forcing is

\[
 \boxed{
 dR=dC-2y e^{y/2}\,dy.}
 \tag{L-21503.9}
\]

This is a nonlinear Volterra/Riccati equation for the complete centered prime
discrepancy. The quadratic term must be retained; deleting it returns only a
phase-blind prime-number-theorem approximation and loses the RH-scale
coherence.

## 3. Laplace Riccati form

For `Re z>1/2`, put

\[
 P(z)=\int_0^\infty e^{-zy}dP(y)
 =-\frac{\zeta'}{\zeta}\!\left(z+\frac12\right),
 \tag{L-21503.10}
\]

\[
 P_0(z)=\frac1{z-1/2},
 \qquad
 H(z)=P(z)-P_0(z).
 \tag{L-21503.11}
\]

Taking Laplace transforms of (L-21503.8) gives

\[
 \boxed{
 -H'(z)+\frac{2}{z-1/2}H(z)+H(z)^2
 =\mathcal R(z),}
 \tag{L-21503.12}
\]

where

\[
 \mathcal R(z)
 =\frac{\zeta''}{\zeta}\!\left(z+\frac12\right)
  -\frac{2}{(z-1/2)^2}.
 \tag{L-21503.13}
\]

Equation (L-21503.12) is merely the arithmetic identity in transform
coordinates; it does not assume RH.

## 4. The safe filter removes the pole model exactly

For the window `G` of `L-21501`,

\[
 \widehat G(1/2)=0.
\]

For all sufficiently large `x`, compact support gives

\[
 \int_0^\infty e^{y/2}G(x-y)dy
 =e^{x/2}\widehat G(1/2)=0.
 \tag{L-21503.14}
\]

Hence

\[
 \boxed{
 Q_G(x)=G*dP(x)=G*d\nu(x)}
 \tag{L-21503.15}
\]

outside one fixed initial compact interval. That initial interval has no effect
on the Hardy-energy exponent of `T-21501`.

Thus the global RH criterion concerns the filtered solution of the centered
nonlinear equation (L-21503.8), not the exponentially large pole model.

## 5. New global attack suggested by the identity

Let `\mathcal L_0` denote the linear Volterra operator

\[
 \mathcal L_0\nu=y\nu+2P_0*\nu.
\]

The exact equation is

\[
 \mathcal L_0\nu+\nu*\nu=R.
 \tag{L-21503.16}
\]

The next proof target is an energy estimate for the safe filtered solution:

\[
 \boxed{
 \int_0^X|G*\nu(x)|^2dx=\exp(o(X)).}
 \tag{L-21503.17}
\]

A successful argument must exploit the quadratic convolution rather than bound
it absolutely. Candidate mechanisms include:

1. a positive-real or dissipative estimate for the Volterra resolvent of
   `L_0`;
2. a completion of `nu*nu` into the prime-pair Gram of `L-21502`;
3. a Selberg-dispersion identity in which the forcing `R` and the quadratic
   term share the same bilinear decomposition;
4. a scale-recursive inequality for unit-block energies of `G*nu`.

Any one of these would attack the full problem globally. Merely proving another
finite scalar sign or finite matrix floor would not establish (L-21503.17).

## 6. Proof boundary

Closed:

- the coefficient identity;
- the exact centered measure equation;
- the Riccati transform;
- exact cancellation of the continuous pole model by the safe window.

Open:

- a dissipative or one-sided energy estimate strong enough to prove
  (L-21503.17).

The open estimate is RH-equivalent by `T-21501`; the identity exposes its
nonlinear arithmetic structure without claiming it is automatically positive.
