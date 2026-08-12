# L-91306 — Moving-unitary completion turns gamma/pole motion into a covariant Hardy connection

Claim ID: `L-91306`  
Status: **PROVED ABSTRACT COVARIANT-COLLIGATION THEOREM; COMPLETED SOURCE DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91035`, `L-91301`, `L-91305`, `L-91309`  
RH status: **unproved**

## 1. Purpose

`L-91305` proves tangent data processing when the observation map is fixed.
Suzuki's completed amplitude factorisation naturally has a moving unitary
archimedean factor. Treating that motion as an uncontrolled error is too
coarse: it is an exact skew connection.

This lemma gives the correct covariant version and applies it to

\[
 \Theta_a=\Gamma_a Z_a,
 \qquad
 Z_a(x)=\frac{\zeta(a+1/2+ix)}{\zeta(a+1/2-ix)}.
\]

It identifies the ordinary-prime tangent block as a literal Hankel operator and
places the gamma/pole term in the connection. No sign conclusion is inferred.

## 2. Abstract moving-unitary theorem

Let `H0`, `S`, and `H` be Hilbert spaces. Let

\[
 V_\tau:H_0\to S
\]

be a strongly differentiable family of isometries, and let

\[
 C_\tau:S\to H
\]

be a strongly differentiable family of unitaries. Put

\[
 M_\tau=C_\tau V_\tau,
 \qquad
 R_\tau=V_\tau V_\tau^*,
 \qquad
 Q_\tau=M_\tau M_\tau^*.
\]

Define the skew connection

\[
 \boxed{
 A_\tau=C_\tau^*\dot C_\tau,
 \qquad A_\tau^*=-A_\tau,
 }
 \tag{L-91306.1}
\]

and the covariant derivative

\[
 \boxed{
 \nabla_\tau V_\tau=\dot V_\tau+A_\tau V_\tau.
 }
 \tag{L-91306.2}
\]

Then

\[
 \boxed{
 \dot M_\tau=C_\tau\nabla_\tau V_\tau.
 }
 \tag{L-91306.3}
\]

Since `Q_tau=C_tau R_tau C_tau*`,

\[
 \boxed{
 (I-Q_\tau)\dot M_\tau
 =C_\tau(I-R_\tau)\nabla_\tau V_\tau.
 }
 \tag{L-91306.4}
\]

Thus the output-normal tangent and source covariant-normal tangent are
unitarily equivalent. In particular,

\[
 \boxed{
 \dot M_\tau^*(I-Q_\tau)\dot M_\tau
 =
 (\nabla_\tau V_\tau)^*(I-R_\tau)\nabla_\tau V_\tau
 \succeq0.
 }
 \tag{L-91306.5}
\]

Equation (L-91306.5) is equality, not only data processing. A positive
auxiliary defect enters only when the source is subsequently observed through
a genuine contraction.

### Proof

Differentiate `M_tau=C_tau V_tau` and use
`dot C_tau=C_tau A_tau`. Equation (L-91306.3) follows. The projection identity
`Q_tau=C_tau R_tau C_tau*` gives

\[
 I-Q_\tau=C_\tau(I-R_\tau)C_\tau^*.
\]

Substitution proves (L-91306.4); taking adjoints gives (L-91306.5). `square`

## 3. Safe completed-zeta factorisation

Fix `a>1/2`, put

\[
 c_a=a+\frac12,
\]

and define on the real boundary

\[
 \boxed{
 Z_a(x)=\frac{\zeta(c_a+ix)}{\zeta(c_a-ix)}.
 }
 \tag{L-91306.6}
\]

Both zeta values are in the absolute half-plane and are nonzero, so
`|Z_a(x)|=1`. Let `Theta_a` be Suzuki's completed inner multiplier and put

\[
 \boxed{
 \Gamma_a(x)=\Theta_a(x)Z_a(x)^{-1}.
 }
 \tag{L-91306.7}
\]

Then `|Gamma_a(x)|=1`; it is the explicit gamma/pole boundary factor.

On `L2(R)` let

\[
 V_a=M_{Z_a}\iota_+ :H^2_+\to L^2(\mathbb R),
 \qquad
 C_a=M_{\Gamma_a},
 \qquad
 M_a=M_{\Theta_a}\iota_+.
 \tag{L-91306.8}
\]

Here `iota_+` is the standard inclusion of `H2_+` into `L2`. Then

\[
 \boxed{M_a=C_aV_a}
 \tag{L-91306.9}
\]

with `V_a` isometric and `C_a` unitary.

Use logarithmic radius `tau=log a` and define the pure-imaginary boundary
connections

\[
 \chi_a^{\rm p}=Z_a^{-1}a\partial_a Z_a,
 \qquad
 \chi_a^{\infty}=\Gamma_a^{-1}a\partial_a\Gamma_a,
 \qquad
 \chi_a=\chi_a^{\rm p}+\chi_a^{\infty}.
 \tag{L-91306.10}
\]

The covariant derivative is

\[
 \boxed{
 \nabla_\tau V_a
 =M_{Z_a}M_{\chi_a}\iota_+.
 }
 \tag{L-91306.11}
\]

Thus gamma and pole motion is not a signed source remainder: it is exactly the
skew connection of the moving unitary `C_a`.

## 4. Hardy Hankel normal form

Let

\[
 R_a=M_{Z_a}P_+M_{\overline{Z_a}}.
\]

Conjugating the source-normal tangent in (L-91306.4) by `M_(overline Z_a)`
gives

\[
 \boxed{
 M_{\overline{Z_a}}(I-R_a)\nabla_\tau V_a
 =P_-M_{\chi_a}P_+.
 }
 \tag{L-91306.12}
\]

Therefore Suzuki's completed model-space shape is, up to the canonical Hardy
reflection and the factor `sqrt(2)` of `L-91301`, the Hankel block

\[
 \boxed{
 H_{\chi_a}=P_-M_{\chi_a}P_+.
 }
 \tag{L-91306.13}
\]

Its ordinary-prime part is `P_-M_(chi_a^p)P_+`; the gamma/pole contribution is
`P_-M_(chi_a^infinity)P_+`. Every cross term in
`H_(chi_a)^*H_(chi_a)` is retained automatically. Splitting the two blocks
after taking norms would lose completed interference and is not permitted.

## 5. Relation to the requested embedding

`L-91307` gives a positive-metric Julia dilation for the prime Hankel block
from its exact atomic first-chaos measure. Equation (L-91306.4) places that
output inside Suzuki's completed two-sided Hardy geometry, with
`chi_a^infinity` acting as the covariant gamma/pole connection.

This closes the operator-theoretic placement of the prime tangent:

```text
ordinary-prime first chaos
 -> explicit causal Hankel output plus positive Julia environment
 -> gamma/pole covariant connection
 -> Suzuki completed two-sided Hardy normal tangent.
```

It does not prove that the positive completed source Fisher curvature of
`L-91309` dominates the squared total normal tangent. That is the RH-bearing
inequality in corrected `T-91008`.

## 6. Exact boundary

```text
moving-unitary covariant tangent identity            EXACT
source/output normal tangents unitarily equivalent   EXACT
gamma/pole motion as skew connection                 EXACT
safe zeta phase as source isometry                   EXACT
completed Suzuki shape as one Hankel block           EXACT
prime Hankel Julia dilation                          CLOSED BY L-91307
completed Fisher curvature >= total shape            OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
