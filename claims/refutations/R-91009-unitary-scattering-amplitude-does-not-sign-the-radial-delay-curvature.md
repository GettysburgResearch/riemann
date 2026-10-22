# R-91009 — Unitary scattering amplitude does not sign the radial delay curvature

Claim ID: `R-91009`  
Status: **EXACT AMPLITUDE/TANGENT FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91035`; main `L-91023`; PR #398 safe-Jordan/Pick controls  
RH status: **unproved**

## 1. The distinction

`L-91035` gives an explicit positive-metric unitary scattering operator whose
boundary multiplier is the completed ratio `Theta_a`.  The Cauchy soft count is
not the modulus of that multiplier.  It is a scale derivative of its
Wigner--Smith delay.

For a differentiable scalar all-pass family put

\[
 q_a(x)=-i\Theta_a(x)^{-1}\partial_x\Theta_a(x)
 \tag{R-91009.1}
\]

and define the normalized radial delay curvature

\[
 \boxed{
 \mathcal N_a(x)
 =\frac14\left[a q_a(x)-a^2\partial_aq_a(x)\right]
 =-\frac{a^3}{4}
  \partial_a\left[\frac{q_a(x)}a\right].
 }
 \tag{R-91009.2}
\]

For the completed xi family this is the resident Cauchy soft count, up to the
fixed convention already recorded in main `L-91023`.

## 2. Exact scalar inner control

Consider

\[
 \boxed{
 \Theta_a^{\rm ctl}(z)=e^{ia^2z}.
 }
 \tag{R-91009.3}
\]

For every `a>0`, this is inner in the upper half-plane and unimodular on the
real line.  Multiplication by `Theta_a^ctl` is an explicit unitary scattering
amplitude on the boundary.

Its Wigner--Smith delay is positive:

\[
 \boxed{q_a^{\rm ctl}(x)=a^2.}
 \tag{R-91009.4}
\]

Nevertheless

\[
 \boxed{
 \mathcal N_a^{\rm ctl}(x)
 =\frac14(a^3-2a^3)
 =-\frac{a^3}{4}<0.
 }
 \tag{R-91009.5}
\]

Thus even the conjunction

```text
analytic inner multiplier at every scale;
positive boundary phase delay at every scale;
explicit positive-metric unitary scattering realization;
```

has no implication for the radial delay-curvature sign.

## 3. General unitary-family statement

Let `U_a` be any differentiable unitary family on a Hilbert space.  Its tangent
generator

\[
 A_a=-iU_a^*\partial_aU_a
 \tag{R-91009.6}
\]

is self-adjoint, but has no sign constraint.  Conversely, for any bounded
self-adjoint `B`,

\[
 U_a=e^{iaB}
\]

has tangent generator `B`.  Differentiating an isometry therefore moves the
problem from norm conservation to a self-adjoint tangent operator; it does not
create positivity.

A second radial derivative introduces the second fundamental form of the
unitary path.  That form can have either sign even when every amplitude map is
unitary.

## 4. Stronger existing control

The exact control on PR #398 retains substantially more zeta-like structure:

```text
functional-equation symmetry;
boundary unitarity;
exact horizontal cocycle;
positive safe Jordan/one-Green data.
```

Its target two-point Pick determinant is nevertheless strictly negative.  The
current firewall is the infinitesimal/tangent version of that same obstruction.

## 5. Consequence for the requested embedding

Suzuki's completed Hankel operator closes the amplitude-level embedding, but a
claim that it also proves CJHI merely by differentiation is invalid.  A valid
proof must construct an additional positive tangent lift and verify the exact
kernel identity after differentiation, including:

```text
the normalized radial first-chaos source of L-91037;
the gamma and pole derivative channels;
the delayed causal/anti-causal output core of L-91034;
all cross-carrier polarizations;
no signed second-fundamental-form remainder.
```

That tangent lift is the corrected final component in `T-91008`.

## 6. Exact boundary

```text
completed scattering amplitude isometry             CLOSED by Suzuki
amplitude unitarity -> delay-curvature sign           FALSE
positive phase delay -> radial curvature sign         FALSE
safe Jordan/cocycle -> target Pick sign               FALSE by PR #398
completed positive tangent lift                       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
