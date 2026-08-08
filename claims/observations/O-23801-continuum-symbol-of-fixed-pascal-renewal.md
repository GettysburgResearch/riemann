# O-23801 — Continuum symbol of a fixed Pascal renewal

Claim ID: `O-23801`  
Title: Every fixed self-similar balanced branching law retains the reciprocal-zeta channel in its continuum renewal symbol  
Status: **PROPOSED STRUCTURAL OBSERVATION — FINITE/CONTINUUM TRANSFER NOT CLAIMED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`, `L-23813`

## 1. Critical scaling profile

Write `n=Xe^{-t}` and consider the critical target

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

The multiple-Möbius coordinate has the formal scaling

\[
U_X(n)=X^{-1/2}u(t)+o(X^{-1/2}),
\]

where

\[
\boxed{
u(t)=e^{t/2}
\sum_{k\le e^t}\frac{\mu(k)}{\sqrt k}(t-\log k).}
\tag{O-23801.1}
\]

Initially for `Re(s)>1`, its Laplace transform is exactly

\[
\boxed{
\widehat u(s)=
\frac1{(s-\tfrac12)^2\zeta(s)}.}
\tag{O-23801.2}
\]

Indeed each `k`-term contributes

\[
\frac{\mu(k)}{k^s(s-\tfrac12)^2}.
\]

The discrete first difference scales as

\[
R_X(n)=X^{-3/2}r(t)+o(X^{-3/2}),
\qquad
r(t)=e^tu'(t),
\]

and therefore

\[
\boxed{
\widehat r(s)=
\frac{s-1}{(s-\tfrac32)^2\zeta(s-1)}.}
\tag{O-23801.3}
\]

## 2. Fixed self-similar branching

Let `pi` be a probability law on balanced ratios `alpha in [eta,1-eta]`.
The continuum parent-to-child renewal operator is

\[
(\mathcal T_\pi f)(t)=
\int\left[
\alpha^{-1}f(t+\log\alpha)
+(1-\alpha)^{-1}f(t+\log(1-\alpha))
\right]d\pi(\alpha),
\tag{O-23801.4}
\]

with `f(t)=0` for `t<0`. Its Laplace multiplier is

\[
\boxed{
M_\pi(s)=
\int[\alpha^{s-1}+(1-\alpha)^{s-1}]d\pi(\alpha).}
\tag{O-23801.5}
\]

The formal continuum descending renewal

\[
f=r+\mathcal T_\pi f
\]

therefore has transform

\[
\boxed{
\widehat f(s)=
\frac{s-1}
{(s-\tfrac32)^2\zeta(s-1)[1-M_\pi(s)]}.}
\tag{O-23801.6}
\]

At `s=2`, size conservation gives `M_pi(2)=1`; the pole of zeta at `s-1=1`
and the renewal zero cancel in the normalized main term.

## 3. The frozen mixed producer

For `L-23815`,

\[
\pi=\frac{31}{32}\delta_{1/3}
    +\frac1{32}\delta_{1/2},
\]

so

\[
\boxed{
M_\pi(s)=
\frac{31}{32}
\left[3^{1-s}+\left(\frac23\right)^{s-1}\right]
+\frac1{32}2^{2-s}.}
\tag{O-23801.7}

This denominator can alter the `2`--`3` renewal geometry and the size-conservation
pole, but it does not cancel generic zeros of `zeta(s-1)`.

## 4. Consequence for proof strategy

The large finite positivity of one fixed renewal is meaningful evidence, but its
continuum symbol remains strip sensitive. A proof of pointwise MPR cannot come
from a phase-blind absolute bound or from extrapolating finite scans; it must
preserve the complete Möbius sign or use another theorem strong enough to
exclude the corresponding off-line poles.

The weaker BTF theorem may exploit lattice cancellation not visible in the
pointwise continuum profile. Its proof still must be symbolic and cofinal.

## 5. Status boundary

The Laplace calculations above are exact for the declared continuum functions
in their initial half-planes. What is not asserted here is a uniform theorem
transferring the full finite descending recurrence to this limit across every
Möbius quotient knot.

This file diagnoses the strip sensitivity of fixed branching laws; it proves
neither MPR/BTF nor RH.
