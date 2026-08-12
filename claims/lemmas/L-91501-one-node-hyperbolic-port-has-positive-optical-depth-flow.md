# L-91501 — The one-node hyperbolic port has a positive optical-depth flow

Claim ID: `L-91501`  
Status: **EXACT MODEL-SPACE DEPTH-FLOW THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91034`, `L-91038`, `L-91334`  
RH status: **unproved**

## 1. Setup

Work in the right half-plane

\[
\mathbb H=\{z:\Re z>0\}.
\]

Fix one real interior node

\[
\eta>\frac12.
\]

At horizontal scale `a>0`, a right-side xi zero

\[
\rho=\frac12+d+i\gamma,
\qquad 0<d<\frac12,
\]

produces the crossed pole

\[
p_{\rho,a}=d-a+i\gamma
\]

exactly when `d>a`.  After cancelling common numerator/denominator factors,
let `B_a` be the resulting crossed-pole Blaschke product.  The hyperbolic-port
diagonal is

\[
\mathcal K_a^{\rm hyp}(\eta,\eta)
=\frac{1-|B_a(\eta)|^2}
       {2\eta|B_a(\eta)|^2}.
\tag{L-91501.1}
\]

Define its logarithmic optical depth by

\[
\boxed{
\mathfrak L_a(\eta)
:=\log\!\left(1+2\eta\mathcal K_a^{\rm hyp}(\eta,\eta)\right)
=-2\log|B_a(\eta)|.
}
\tag{L-91501.2}
\]

## 2. Exact additive zero ledger

For a simple pole `p=delta+i gamma`, where

\[
\delta=d-a>0,
\]

one has

\[
|b_p(\eta)|^2
=\frac{(\eta-\delta)^2+\gamma^2}
       {(\eta+\delta)^2+\gamma^2}.
\tag{L-91501.3}
\]

Consequently, away from the countable collision/cancellation scales,

\[
\boxed{
\mathfrak L_a(\eta)
=\sum_{\rho:\,d>a}m_\rho
\log\frac{(\eta+d-a)^2+\gamma^2}
          {(\eta-d+a)^2+\gamma^2}.
}
\tag{L-91501.4}
\]

The sum converges normally on compact scale intervals avoiding collisions.  It
extends continuously across a birth scale `a=d`, because the newborn summand
vanishes at `d-a=0`.

## 3. Positive radial current

For

\[
\ell_{\eta,\gamma}(\delta)
=\log\frac{(\eta+\delta)^2+\gamma^2}
          {(\eta-\delta)^2+\gamma^2},
\]

direct differentiation gives

\[
\boxed{
\ell_{\eta,\gamma}'(\delta)
=\frac{4\eta(\eta^2+\gamma^2-\delta^2)}
 {[(\eta+\delta)^2+\gamma^2]
  [(\eta-\delta)^2+\gamma^2]}.
}
\tag{L-91501.5}
\]

Since

\[
0<\delta<\frac12<\eta,
\]

every factor in (L-91501.5) is strictly positive.  Therefore

\[
\boxed{
-\partial_a\mathfrak L_a(\eta)
=\mathfrak J_a(\eta)>0
}
\tag{L-91501.6}
\]

whenever at least one crossed pole is present, where

\[
\boxed{
\mathfrak J_a(\eta)
=\sum_{\rho:\,d>a}m_\rho
\frac{4\eta[\eta^2+\gamma^2-(d-a)^2]}
 {[(\eta+d-a)^2+\gamma^2]
  [(\eta-d+a)^2+\gamma^2]}.
}
\tag{L-91501.7}
\]

No Dirac birth term appears at `a=d`, because the optical depth of a newborn
factor is zero.  Thus the identity also holds distributionally in `a`.

## 4. Exact transport representation

There are no crossed poles for `a>=1/2`.  Integrating (L-91501.6) gives

\[
\boxed{
\mathfrak L_a(\eta)
=\int_a^{1/2}\mathfrak J_b(\eta)\,db.
}
\tag{L-91501.8}
\]

Hence one interior node sees the complete crossed-zero sector as a positive,
additive depth flow.  Distinct zero ports cannot cancel one another in this
coordinate.

The following are equivalent at a fixed generic scale:

\[
\boxed{
\begin{aligned}
\mathcal K_a^{\rm hyp}(\eta,\eta)=0
&\iff \mathfrak L_a(\eta)=0\\
&\iff \mathfrak J_b(\eta)=0
     \text{ for almost every }b\in(a,1/2)\\
&\iff B_a\text{ is constant}.
\end{aligned}}
\tag{L-91501.9}
\]

## 5. Consequence for the one-node source programme

The remaining arithmetic theorem cannot rely on cancellation between crossed
zero coordinates: the target defect is the positive scalar current
`mathfrak J_a(eta)` integrated over scale.  A source-ordered one-node proof may
therefore be organized as either

```text
instantaneous form:
    identify the completed arithmetic tangent current with J_a(eta)
    and prove it vanishes;

integrated form:
    identify the arithmetic norm defect with L_a(eta)
    and prove exact exhaustion.
```

The theorem does not prove either source identification.  It proves that once
such an identification is constructed, there is no hidden cancellation or
infinite-height escape in the zero-port sector.

## 6. Exact boundary

```text
one-node hyperbolic optical-depth sum              EXACT
positive radial birth/current formula              EXACT
all crossed ports add without cancellation         EXACT
one-node defect as positive scale transport         EXACT
arithmetic tangent current = optical current        OPEN
arithmetic proof that the current vanishes          OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
