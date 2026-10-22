# L-91301 — Suzuki model-space curvature is the canonical positive first-chaos tangent reserve

Claim ID: `L-91301`  
Status: **PROVED ABSTRACT HARDY/MODEL-SPACE THEOREM; ZETA CURVATURE DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91035`, `L-91036`, `L-91037`  
RH status: **unproved**

## 1. Purpose

`L-91035` closes the amplitude-level completed Jordan-to-Hardy transport by
Suzuki's inner multiplier

\[
 \Theta_a(z)=\frac{\xi(1/2-a-iz)}{\xi(1/2+a-iz)}
\]

at every safe scale `a>1/2`.  `L-91036` shows that any natural positive
source-linear tangent completion must live in first chaos.  The missing output
feature can therefore be searched for inside the differential geometry of the
Hardy model space itself.

This lemma identifies it exactly.  No arbitrary reserve or existential square
root is needed.

## 2. A differentiable inner family

Let `H^2=H^2(C_+)`.  Let `tau -> Theta_tau` be a `C^2` family of inner
functions in the sense that multiplication

\[
 M_\tau=M_{\Theta_\tau}:H^2\to H^2
\]

is an isometry and the multiplier family is twice strongly differentiable on a
common dense core.

Put

\[
 Q_\tau=M_\tau M_\tau^*,
 \qquad
 P_\tau=I-Q_\tau.
\]

Thus `P_tau` is the orthogonal projection onto the model space

\[
 K_{\Theta_\tau}=H^2\ominus\Theta_\tau H^2.
\]

Dots below denote `d/dtau`.

## 3. Exact off-diagonal tangent

Differentiating

\[
 P_\tau=I-M_\tau M_\tau^*
\]

gives

\[
 \dot P_\tau
 =-\dot M_\tau M_\tau^*-M_\tau\dot M_\tau^*.
\tag{L-91301.1}
\]

If `f in K_(Theta_tau)`, then `M_tau^* f=0`; hence

\[
 \boxed{
 \dot P_\tau f
 =-M_\tau\dot M_\tau^*f
 \in \Theta_\tau H^2.
 }
\tag{L-91301.2}
\]

Define the second-fundamental-form operator

\[
 \boxed{
 \mathcal B_\tau
 =(I-P_\tau)\dot P_\tau P_\tau
 =-M_\tau\dot M_\tau^*P_\tau.
 }
\tag{L-91301.3}
\]

Since `M_tau^*M_tau=I`,

\[
 \boxed{
 \mathcal B_\tau^*\mathcal B_\tau
 =P_\tau\dot M_\tau\dot M_\tau^*P_\tau
 \succeq0.
 }
\tag{L-91301.4}
\]

The output feature map is therefore explicit:

\[
 \boxed{
 \mathcal J_\tau
 =\sqrt2\,\dot M_\tau^*P_\tau:
 K_{\Theta_\tau}\longrightarrow H^2.
 }
\tag{L-91301.5}
\]

It is linear in the tangent multiplier `dot Theta_tau`; in particular it is a
first-chaos object rather than a nonlinear Fock correction.

## 4. Projection-curvature square

Every differentiable orthogonal projection satisfies

\[
 P\dot P P=0.
\tag{L-91301.6}
\]

Differentiate `P^2=P` twice:

\[
 \ddot P P+2\dot P^2+P\ddot P=\ddot P.
\]

Sandwiching by `P` gives

\[
 P\ddot P P+2P\dot P^2P=0.
\]

Since `dot P` is self-adjoint and off diagonal relative to
`Ran P direct-sum Ker P`,

\[
 P\dot P^2P=\mathcal B^*\mathcal B.
\]

Consequently

\[
 \boxed{
 -P_\tau\ddot P_\tau P_\tau
 =2\mathcal B_\tau^*\mathcal B_\tau
 =\mathcal J_\tau^*\mathcal J_\tau
 \succeq0.
 }
\tag{L-91301.7}
\]

This is an exact Gram factorization of the radial curvature of the moving model
space.

## 5. Logarithmic radial parameter

For the zeta scattering family it is natural to use

\[
 \tau=\log a.
\]

Then `partial_tau=a partial_a`.  Although

\[
 \partial_\tau^2P=a^2\partial_a^2P+a\partial_aP,
\]

the second term vanishes after sandwiching because `P partial_a P P=0`.
Therefore

\[
 \boxed{
 -P_a\partial_\tau^2P_aP_a
 =2a^2\mathcal B_a^*\mathcal B_a.
 }
\tag{L-91301.8}
\]

Thus normalization by logarithmic radius creates no extra signed connection
term on the model-space fibre.

## 6. Application to Suzuki's safe family

For every `a>1/2`, Suzuki's theorem makes `Theta_a` meromorphic inner in
`C_+`.  On any compact safe `a`-interval avoiding a parameter collision, the
preceding theorem applies to

\[
 P_a=P_{K_{\Theta_a}}.
\]

The canonical completed tangent reserve is

\[
 \boxed{
 \mathcal J_a
 =\sqrt2\,M_{a\partial_a\Theta_a}^*P_a.
 }
\tag{L-91301.9}
\]

The logarithmic derivative of `Theta_a` splits explicitly into:

```text
prime-power first chaos;
gamma first chaos;
pole/boundary finite channel.
```

Hence (L-91301.9) is source-linear in exactly the sense required by
`L-91036`.

## 7. The exact remaining domination

Let `C_a^src` denote the complete positive first-chaos curvature form obtained
by adjoining the Jordan source of `L-91037` to the explicit gamma/pole tangent
channels.  The only possible conservative tangent identity compatible with the
Suzuki amplitude and the standard Hardy splitting is

\[
 \boxed{
 C_a^{\rm src}
 =\mathcal J_a^*\mathcal J_a+K_a^{\rm screw}.
 }
\tag{L-91301.10}
\]

Thus a proof of

\[
 \boxed{
 C_a^{\rm src}\succeq\mathcal J_a^*\mathcal J_a
 }
\tag{L-91301.11}
\]

on the delayed form core of `L-91034` would produce the desired fixed-scale
screw Gram and prove RH through `T-91007`.

Equation (L-91301.11) is now an explicit domination between two resident
first-chaos operators.  It is not a request for an unspecified Fock embedding.

## 8. Uniqueness of the reserve

Suppose a differentiable conservative colligation uses the same amplitude
subspace `Theta_a H^2` and the same orthogonal Hardy splitting.  The derivative
of the output subspace has off-diagonal block

\[
 (I-P_a)\partial_\tau P_aP_a.
\]

Therefore every such colligation contains `mathcal B_a` up to an output
isometry.  Any extra positive reserve is orthogonal to this mandatory channel.
The map (L-91301.9) is consequently canonical, not one ansatz among many.

## 9. Proof boundary

```text
safe Suzuki amplitude innerness                 IMPORTED PROVED
model-space tangent operator                    EXACT
projection-curvature Gram square                 EXACT
log-radius normalization                        EXACT
canonical first-chaos output reserve             EXACT
source curvature >= tangent leakage              OPEN / RH-BEARING
fixed-scale screw Gram positivity                OPEN
Riemann Hypothesis                               UNPROVED
```
