# L-91330 — The free Suzuki endpoint contains one explicit unstable pole bridge, canceled coefficient-one by the full Jordan channel

Claim ID: `L-91330`  
Status: **EXACT ASYMPTOTIC, MELLIN-POLE, AND HARD-RANGE THRESHOLD THEOREM**  
Created: 2026-08-12  
Depends on: Suzuki's explicit endpoint kernel; `L-91311/L-91329`; standard gamma identities and the prime number theorem  
RH status: **unproved**

## 1. Suzuki's endpoint kernel

For \(0<\omega<3/2\) and \(0<x<1\), write

\[
 g_\omega(x)
 =\frac{2\pi^\omega}{\Gamma(\omega)}
 \left[
 x^{2-\omega}(1-x^2)^{\omega-1}
 -\omega x^{\omega-1}
 \int_{x^2}^{1}t^{1/2-\omega}(1-t)^{\omega-1}dt
 \right].
 \tag{L-91330.1}
\]

Its Mellin transform is

\[
 \int_0^1g_\omega(x)x^s\frac{dx}{x}
 =G_\omega(s)
 :=\frac{\gamma(s-\omega)}{\gamma(s+\omega)},
 \tag{L-91330.2}
\]

with \(\gamma(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\).

## 2. Exact small-\(x\) expansion

The beta integral in (L-91330.1) gives, as \(x\downarrow0\),

\[
 \boxed{
 g_\omega(x)
 =C_{0,\omega}x^{\omega-1}
 +C_{1,\omega}x^{2-\omega}
 +O_\omega(x^{4-\omega}),
 }
 \tag{L-91330.3}
\]

where

\[
 \boxed{
 C_{0,\omega}
 =-4\omega\pi^{\omega-1/2}\Gamma(3/2-\omega),
 }
 \tag{L-91330.4}
\]

and

\[
 \boxed{
 C_{1,\omega}
 =\frac{6\pi^\omega}{(3-2\omega)\Gamma(\omega)}.
 }
 \tag{L-91330.5}
\]

Indeed,

\[
 \int_{x^2}^{1}t^{1/2-\omega}(1-t)^{\omega-1}dt
 =B(3/2-\omega,\omega)
 -\frac{x^{3-2\omega}}{3/2-\omega}
 +O_\omega(x^{5-2\omega}).
 \tag{L-91330.6}
\]

## 3. Free endpoint Green threshold

Put

\[
 F_\omega(y)=g_\omega(1/y),
 \qquad y\ge1,
 \tag{L-91330.7}
\]

and

\[
 V_\omega(x)=\mathcal JF_\omega(x)
 =\int_1^xF_\omega(y)\frac{dy}{y}.
 \tag{L-91330.8}
\]

For \(0<\omega<1\), (L-91330.3) gives

\[
 \boxed{
 V_\omega(x)
 =\frac{C_{0,\omega}}{1-\omega}x^{1-\omega}
 +C_\omega^{\rm fp}
 +O_\omega(x^{\omega-2}).
 }
 \tag{L-91330.9}
\]

Therefore the logarithmic free Green vector

\[
 v_\omega(t)=e^{-t/2}V_\omega(e^t)
 \tag{L-91330.10}
\]

obeys

\[
 v_\omega(t)
 =\frac{C_{0,\omega}}{1-\omega}
 e^{(1/2-\omega)t}
 +O_\omega(e^{-t/2}),
 \tag{L-91330.11}
\]

and hence

\[
 \boxed{
 v_\omega\in L^2(0,\infty)
 \iff
 \omega>\frac12.
 }
 \tag{L-91330.12}
\]

At the threshold \(\omega=1/2\),

\[
 C_{0,1/2}=-2,
 \qquad
 v_{1/2}(t)\longrightarrow-4.
 \tag{L-91330.13}
\]

Thus the all-detail inverse exposes, rather than cures, the hard-range instability.

## 4. One-dimensional pole bridge

Put

\[
 s_0=1-\omega.
 \tag{L-91330.14}
\]

Since \(\gamma(1)=0\) and \(\gamma'(1)=1/2\), (L-91330.2) has a simple pole at \(s_0\) with

\[
 \boxed{
 \operatorname*{Res}_{s=s_0}G_\omega(s)
 =2\gamma(1-2\omega)
 =C_{0,\omega}.
 }
 \tag{L-91330.15}
\]

The positive forward Jordan factor

\[
 C_\omega(s)=\frac{\zeta(s-\omega)}{\zeta(s+\omega)}
 \tag{L-91330.16}
\]

has the exact local expansion

\[
 \boxed{
 C_\omega(s)
 =\zeta(1-2\omega)(s-s_0)
 +O_\omega((s-s_0)^2).
 }
 \tag{L-91330.17}
\]

Hence the free pole and the arithmetic zero cancel with coefficient one in

\[
 C_\omega(s)G_\omega(s)
 =\frac{\xi(s-\omega)}{\xi(s+\omega)}.
 \tag{L-91330.18}
\]

This universal cancellation is independent of RH. It is the archimedean pole bridge that every source-to-Hardy construction must preserve before taking norms.

## 5. Pole-subtracted free vector

Define

\[
 F_\omega^\circ(y)
 =F_\omega(y)-C_{0,\omega}y^{1-\omega},
 \qquad y\ge1.
 \tag{L-91330.19}
\]

Then

\[
 e^{-t/2}\mathcal JF_\omega^\circ(e^t)
 \in L^2(0,\infty)
 \qquad(0<\omega<1/2).
 \tag{L-91330.20}
\]

The local singularity at \(y=1\) is integrable after the Green primitive, while at infinity the pole-subtracted forcing is \(O(y^{\omega-2})\) and its primitive tends to a finite constant.

Thus the hard-range free endpoint consists of exactly

```text
one explicit non-Hilbert pole bridge
+ one unconditional Hilbert remainder.
```

## 6. Finite Euler products amplify rather than cancel the bridge

For a finite prime cutoff \(P\), put

\[
 C_{\omega,P}(s)
 =\prod_{p\le P}
 \frac{1-p^{-(s+\omega)}}{1-p^{-(s-\omega)}}.
 \tag{L-91330.21}
\]

At \(s_0=1-\omega\),

\[
 C_{\omega,P}(s_0)
 =\prod_{p\le P}
 \frac{1-p^{-1}}{1-p^{-(1-2\omega)}}>1,
 \tag{L-91330.22}
\]

and the prime number theorem gives

\[
 \boxed{
 \log C_{\omega,P}(s_0)
 =\frac{P^{2\omega}}{2\omega\log P}
 (1+o(1)).
 }
 \tag{L-91330.23}
\]

Therefore every finite Euler product multiplies the free pole residue by a rapidly growing positive number. The zero in (L-91330.17) is not the limit of the finite Euler factors at \(s_0\); it is a genuinely global analytic-continuation effect.

## 7. Consequence

A cutoff-wise construction that first forms a finite Euler product, then removes the Julia normalizations, and finally appends an independent gamma/theta port cannot approximate the completed cancellation. The pole bridge and the all-prime tail must be mixed before Hilbert completion through a nonlocal, sector-changing renormalization.
