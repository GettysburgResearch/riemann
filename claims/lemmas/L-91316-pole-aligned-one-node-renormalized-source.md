# L-91316 — The one-node detector can be aligned with the renormalized Jordan pole state

Claim ID: `L-91316`  
Status: **EXACT POLE CANCELLATION AND FINITE-PART FORMULAS; COMPLETED TANGENT ISOMETRY OPEN**  
Created: 2026-08-12  
Depends on: main `L-91014/L-91015/L-91023`, `L-91313`  
RH status: **unproved**

## 1. Pole-aligned node

For `a>0`, take

\[
 \boxed{
 \eta_a^{\rm pole}=\frac12+a.
 }
 \tag{L-91316.1}
\]

In the right-half-plane coordinate

\[
 \Theta_a(z)
 =\frac{\xi(\frac12-a+z)}
        {\xi(\frac12+a+z)},
 \tag{L-91316.2}
\]

this gives

\[
 \frac12-a+\eta_a^{\rm pole}=1,
 \qquad
 \frac12+a+\eta_a^{\rm pole}=1+2a.
 \tag{L-91316.3}
\]

Hence

\[
 \boxed{
 \Theta_a(\eta_a^{\rm pole})
 =\frac{\xi(1)}{\xi(1+2a)}
 =\frac1{2\xi(1+2a)}.
 }
 \tag{L-91316.4}
\]

This is a finite positive safe value despite the pole of `zeta` at `1`.

## 2. Exact cancellation of the Euler pole

Write

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)},
 \qquad
 \kappa_a=\frac1{\zeta(1+2a)}.
 \tag{L-91316.5}
\]

Then

\[
 Q_a(s)=\frac{\kappa_a}{s-1}+H_a(s),
 \tag{L-91316.6}
\]

where `H_a` is holomorphic at `1`. The completed factor

\[
 \Gamma_a(s)
 =\pi^a
 \frac{s(s-1)}{(s+2a)(s+2a-1)}
 \frac{\Gamma(s/2)}{\Gamma((s+2a)/2)}
 \tag{L-91316.7}
\]

has a simple zero at `s=1`. Its leading coefficient is

\[
 \boxed{
 \Gamma_a(s)
 =(s-1)\,g_a+O_a((s-1)^2),
 }
 \tag{L-91316.8}
\]

with

\[
 \boxed{
 g_a
 =\pi^a
 \frac{\Gamma(1/2)}
      {2a(1+2a)\Gamma(1/2+a)}.
 }
 \tag{L-91316.9}
\]

Therefore

\[
 \Theta_a(\eta_a^{\rm pole})
 =g_a\kappa_a,
 \tag{L-91316.10}
\]

which is exactly (L-91316.4) after substituting the definition of `xi`.
The universal divergent Euler state and the completed archimedean zero cancel
with coefficient one.

## 3. Explicit pole-subtracted finite part

Using

\[
 \zeta(1+\varepsilon)
 =\frac1\varepsilon+\gamma+O(\varepsilon),
 \tag{L-91316.11}
\]

and expanding `1/zeta(1+2a+epsilon)`, one obtains

\[
 \boxed{
 H_a(1)
 =\kappa_a
 \left[
 \gamma-\frac{\zeta'}{\zeta}(1+2a)
 \right].
 }
 \tag{L-91316.12}
\]

Thus the pole-normalized finite part is

\[
 \boxed{
 \widetilde H_a(1)
 :=\frac{H_a(1)}{\kappa_a}
 =\gamma-\frac{\zeta'}{\zeta}(1+2a)>0.
 }
 \tag{L-91316.13}
\]

Every quantity is an absolutely convergent Euler value. Higher pole-subtracted
jets are explicit universal polynomials in the Stieltjes constants and the
safe derivatives of `log zeta` at `1+2a`.

## 4. Exact dyadic returned-state orientation

The normalized recurrence of main `L-91015` is

\[
 \widetilde H_{2a}(s)
 =\widetilde H_a(s)
  \frac{Q_a(s+2a)}{Q_a(1+2a)}
 +\frac1{Q_a(1+2a)}
  \frac{Q_a(s+2a)-Q_a(1+2a)}{s-1}.
 \tag{L-91316.14}
\]

At `s=1`, the inherited multiplier is exactly one:

\[
 \frac{Q_a(1+2a)}{Q_a(1+2a)}=1.
 \tag{L-91316.15}
\]

The second term has the finite value

\[
 \frac{Q_a'(1+2a)}{Q_a(1+2a)},
 \tag{L-91316.16}
\]

and its negative is a positive logarithmic moment of the tail measure in
`L-91015`. Thus the pole-aligned node is the exact coefficient-one state of the
source recurrence.

## 5. Zero-port detection at the pole-aligned node

The exact model-space port satisfies

\[
 \mathcal K_a^{\rm hyp}
 (\eta_a^{\rm pole},\eta_a^{\rm pole})
 =\frac{1-|B_a(\eta_a^{\rm pole})|^2}
        {2\eta_a^{\rm pole}|B_a(\eta_a^{\rm pole})|^2}.
 \tag{L-91316.17}
\]

It vanishes exactly when there is no zero of depth greater than `a`.
Therefore the arithmetic first-chaos/tangent map may be required at the
renormalized pole state rather than at an arbitrary safe point.

## 6. Pole-Aligned Arithmetic Exhaustion

> **`PAAE_a`.**  
> Construct the completed source-to-model tangent map on the coefficient-one
> pole state and its finite fluctuation jets (L-91316.12)--(L-91316.16), and
> prove exact norm exhaustion by the critical and deterministic stable model
> outputs at `z=eta_a^(pole)`.

No infinite source norm remains after the declared pole subtraction. The map
must include the gamma/pole zero `g_a`, the positive Jordan tail, the coupled
Brownian/theta reserve, and the local `p=2` boundary port.

`PAAE_a` forces (L-91316.17) to vanish. A sequence `a_j downarrow0` proves RH.

## 7. Three exact node normalizations

```text
pole-aligned:      eta_a=1/2+a
  coefficient-one pole state and finite fluctuation jets;

anchor-aligned:    eta_a=1/2+3a
  canonical finite Jordan anchor;

cocycle-aligned:   eta_a=1/2+a+q_0
  one fixed Green test through every dyadic generation.
```

They are not competing criteria. They are three coordinate charts for the
same one-node arithmetic exhaustion theorem.
