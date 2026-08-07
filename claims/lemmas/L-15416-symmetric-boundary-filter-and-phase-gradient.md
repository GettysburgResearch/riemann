# L-15416 — A symmetric boundary filter turns the Hardy energy into a phase-gradient energy

Claim ID: `L-15416`  
Title: A compact two-boundary filter preserves every off-line zero and exposes the exact Suzuki scattering-phase Dirichlet energy  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: the functional equations of `xi`; elementary bilateral Laplace transforms; `T-15406` for the prime-window motivation  
Scope: the uniform Hardy/reflection defect in Issue #180  
Related counterexample candidates: none

## Centered completed logarithmic derivative

Put

\[
 \Xi(z)=\xi\!\left(\frac12+z\right),
 \qquad
 L(z)=\frac{\Xi'(z)}{\Xi(z)}.
 \tag{L-15416.1}
\]

The completed functional equations give

\[
 \Xi(-z)=\Xi(z),
 \qquad
 \Xi(\bar z)=\overline{\Xi(z)},
 \tag{L-15416.2}
\]

and hence

\[
 \boxed{L(-z)=-L(z),
 \qquad L(\bar z)=\overline{L(z)}.}
 \tag{L-15416.3}
\]

## A finite symmetric filter

Fix `h>0` and define, with removable value at zero,

\[
 B_h(z)=\frac{2\sinh(hz/2)}{hz},
 \tag{L-15416.4}
\]

\[
 P_h(z)=\cosh(hz)-\cosh(h/2),
 \tag{L-15416.5}
\]

and

\[
 \boxed{\Omega_h(z)=B_h(z)^2P_h(z).}
 \tag{L-15416.6}
\]

Then `Omega_h` is a real even entire function. Its zeros are contained in the
three boundary families

\[
 z=\frac{2\pi i k}{h}\quad(k\ne0),
 \tag{L-15416.7}
\]

and

\[
 z=\pm\frac12+\frac{2\pi i k}{h}\quad(k\in\mathbb Z).
 \tag{L-15416.8}
\]

Consequently

\[
 \boxed{\Omega_h(z)\ne0
 \qquad(0<|\operatorname{Re}z|<1/2).}
 \tag{L-15416.9}
\]

On every fixed vertical strip,

\[
 \Omega_h(\sigma+it)=O_h((1+|t|)^{-2}),
 \qquad
 \Omega_h'(\sigma+it)=O_h((1+|t|)^{-2}).
 \tag{L-15416.10}
\]

### Exact compact inverse profile

Let

\[
 b_h^{\rm sym}(u)=h^{-1}\mathbf1_{[-h/2,h/2]}(u),
 \qquad
 \tau_h=b_h^{\rm sym}*b_h^{\rm sym}.
 \tag{L-15416.11}
\]

The bilateral Laplace transform of `tau_h` is `B_h^2`. Therefore `Omega_h` is
the bilateral Laplace transform of the explicit compact signed profile

\[
 \boxed{
 \omega_h(u)=
 \frac12\tau_h(u+h)+\frac12\tau_h(u-h)
 -\cosh(h/2)\tau_h(u),}
 \tag{L-15416.12}
\]

supported in `[-2h,2h]`. Thus the symmetric filter has only three translated
triangular pieces; no infinite product or fitted profile enters its definition.

## Exact two-line modulus identity

Define

\[
 F_h(z)=\Omega_h(z)L(z).
 \tag{L-15416.13}
\]

Both factors have real Taylor coefficients, `Omega_h` is even, and `L` is odd.
Hence

\[
 F_h(-z)=-F_h(z),
 \qquad
 F_h(\bar z)=\overline{F_h(z)}.
 \tag{L-15416.14}
\]

For `z=sigma+it`,

\[
 F_h(-\bar z)=-\overline{F_h(z)}.
 \]

Therefore

\[
 \boxed{
 |F_h(\sigma+it)|^2
 =-F_h(\sigma+it)F_h(-\sigma+it).}
 \tag{L-15416.15}
\]

The positive Hardy energy may be written exactly as a same-height reflected
bilinear energy:

\[
 \boxed{
 \mathcal H_h(\sigma)
 :=\frac{\sigma}{2\pi}\int_{\mathbb R}
 |F_h(\sigma+it)|^2dt
 =-\frac{\sigma}{2\pi}\int_{\mathbb R}
 F_h(\sigma+it)F_h(-\sigma+it)dt.}
 \tag{L-15416.16}
\]

This identity does **not** permit the two vertical lines to be collapsed without
recording every pole crossed between them.

## Suzuki scattering phase

For `omega>0` and real `t`, define

\[
 \Theta_\omega(t)
 =\frac{\xi(\frac12-\omega-it)}
        {\xi(\frac12+\omega-it)}.
 \tag{L-15416.17}
\]

The functional equations imply

\[
 |\Theta_\omega(t)|=1
 \tag{L-15416.18}
\]

whenever the denominator is nonzero. Let

\[
 L_+(\omega,t)
 =\frac{\xi'}{\xi}\!\left(\frac12+\omega-it\right).
 \tag{L-15416.19}
\]

Since

\[
 \frac{\xi'}{\xi}\!\left(\frac12-\omega-it\right)
 =-\overline{L_+(\omega,t)},
 \tag{L-15416.20}
\]

direct differentiation gives

\[
 \boxed{
 \partial_t\log\Theta_\omega(t)
 =2i\operatorname{Re}L_+(\omega,t),}
 \tag{L-15416.21}
\]

and

\[
 \boxed{
 \partial_\omega\log\Theta_\omega(t)
 =-2i\operatorname{Im}L_+(\omega,t).}
 \tag{L-15416.22}
\]

Consequently

\[
 \boxed{
 |L_+(\omega,t)|^2
 =\frac14\left(
 |\partial_t\log\Theta_\omega(t)|^2
 +|\partial_\omega\log\Theta_\omega(t)|^2
 \right).}
 \tag{L-15416.23}
\]

Thus the uniform Hardy target is a weighted Dirichlet-energy bound for the
unimodular scattering phase `Theta_omega`.

## Local zero trichotomy

Let

\[
 \rho=\frac12+\delta+i\gamma
 \tag{L-15416.24}
\]

be a zero of multiplicity `m`, and put `a=delta+i gamma`. Since
`Omega_h(a)` is nonzero for `0<delta<1/2`, near `(omega,t)=(delta,-gamma)`
(or the corresponding sign convention for `t`) the filtered logarithmic
derivative has a genuine simple pole. Its local Hardy contribution behaves as

\[
 \boxed{
 \mathcal H_h(\omega)
 \sim
 \frac{\omega m^2|\Omega_h(a)|^2}
      {2|\omega-\delta|}.}
 \tag{L-15416.25}
\]

Hence:

- a left-half-plane centered zero gives a stable decaying mode;
- a critical-line zero gives a finite Abel boundary mass;
- an off-line right zero gives an interior phase vortex and unbounded Hardy
  energy.

The exact finite-rank form of this statement is proved in `T-15407`.

## Model-space interpretation

Suzuki studies the meromorphic function

\[
 \Theta_\omega(z)
 =\frac{\xi(\frac12-\omega-iz)}
        {\xi(\frac12+\omega-iz)}.
 \tag{L-15416.26}
\]

Its boundary values are unimodular unconditionally. The nontrivial question is
whether it is analytic and inner in the upper half-plane. The poles preventing
innerness are exactly the same off-line zeros producing (L-15416.25).

Therefore the Hardy/reflection defect, failure of Suzuki innerness, and the
anti-causal component of the corresponding Hankel/model-space operator are
three representations of one obstruction.

## Consequences for the positive route

1. The reflected line is not a heuristic replacement for the Hardy norm;
   equation (L-15416.15) is exact.
2. The only difference between a safe contour reflection and a circular one is
   the complete pole ledger.
3. A successful positive proof may equivalently establish finite phase-gradient
   energy for every `omega>0`, innerness of every `Theta_omega`, or vanishing of
   the anti-Hardy Hankel component.
4. Estimating the two vertical lines separately destroys the reflection
   cancellation and cannot reach the critical bound.

## Gap audit

- `Theta_omega` is unimodular on the boundary even when it is not inner.
  Boundary modulus one alone proves nothing about RH.
- The logarithm in (L-15416.21)--(L-15416.22) is local; its derivatives are
  single-valued away from zeros.
- Every contour displacement must retain multiplicities and both members of
  every functional-equation/conjugation orbit.
- The symmetric filter has a compact profile, but the completed logarithmic
  derivative also contains gamma-factor terms on the arithmetic side.
- This lemma identifies the exact phase energy. It does not prove that the
  interior vortex set is empty.
