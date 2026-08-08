# Addendum — endpoint-scale kernel and exact Möbius weight state

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Branch:** `research/gpt56-pro-262-parabolic-scale-frame`  
**Parent report:** `2026-08-08-parabolic-endpoint-scale-frame-proposal.md`  
**Status:** **NEW EXACT TRANSFORM BRIDGE; POSITIVE FINITE-MINORANT THEOREM OPEN**

## Result

After the positive endpoint frame was constructed, its continuum response could
be diagonalized exactly.

Let

\[
F(\theta)=\sum_{k\le1/\theta}g(k\theta)
\]

be the continuum response of the complete parabolic seed.  Differentiating the
endpoint-scaled response gives one positive kernel

\[
k(u)=-\frac12F(u)-uF'(u).
\]

On the reciprocal cell `1/(N+1)<u<=1/N`, it is exactly

\[
\boxed{k(u)=2N-S_Nu^{-1/2}>0.}
\]

Moreover,

\[
\int_0^1k(u)du=2.
\]

Thus `k/2` is the fixed probability law governing the ratio between one
endpoint atom and the column scale it reaches.

## Endpoint-scale Volterra equation

For a nonnegative endpoint weight `lambda(s)`, the response is

\[
\mathcal R_\lambda(\theta)
=\int_\theta^1\lambda(s)s^{-3/2}k(\theta/s)ds.
\]

With

\[
\theta=e^{-t},
\qquad
L(t)=\lambda(e^{-t}),
\qquad
\varrho(v)=e^{-v/2}k(e^{-v}),
\]

this becomes

\[
e^{-t/2}\mathcal R_\lambda(e^{-t})=(L*\varrho)(t).
\]

Exact saturation of the critical target is therefore

\[
\boxed{L*\varrho=t.}
\]

The finite endpoint-scale greedy on PR #265 is a positive finite-horizon
minorant producer for this scalar equation.

## Exact symbols

The positive kernel has Laplace transform

\[
\boxed{
\widehat\varrho(z)
=\zeta(z+1/2)
 \frac{z-1/2}{z(z+1/2)}.}
\]

The exact equality weight consequently has transform

\[
\boxed{
\widehat L_*(z)
=\frac{z+1/2}
 {z(z-1/2)\zeta(z+1/2)}.}
\]

Its physical form is the simple Möbius–Riesz state

\[
\boxed{
L_*(t)
=\sum_{n\le e^t}\frac{\mu(n)}{\sqrt n}
 \left[2e^{(t-\log n)/2}-1\right].}
\]

The critical mass is

\[
\widehat L_*(1/2)=2,
\]

so the endpoint entropy is exactly

\[
2\widehat L_*(1/2)=4.
\]

Every hypothetical off-line zeta zero remains an uncancelled pole.  The exact
weight is not assumed positive.

## Bridge to DCRS and the canonical carry state

Let `mathfrak g` be PR #252's carry-resolvent state.  The transforms satisfy

\[
\widehat{\mathfrak g}(z)
=\frac{z+3/2}{z}\widehat L_*(z).
\]

Equivalently,

\[
\boxed{
\mathfrak g(t)
=L_*(t)+\frac32\int_0^tL_*(u)du,}
\]

and

\[
\boxed{
L_*(t)
=\mathfrak g(t)
-\frac32\int_0^t
 e^{-3(t-u)/2}\mathfrak g(u)du.}
\]

Thus the endpoint-scale equality state and the canonical carry-resolvent state
are mutually related by stable first-order causal filters.  They expose the
same zeta poles; the difference is the positive finite producer used to
approximate them.

## Consequence

The new frame is not an isolated positive-coordinate construction.  It is a
finite minorant programme for one exact reciprocal-zeta Volterra equation,
canonically equivalent at the transform level to DCRS and the Gamma/carry
route.

The remaining theorem is still finite:

```text
construct nonnegative endpoint weights
whose response lies below the target
and whose lost critical mass is X^o(1).
```

`ESBT/ESGS` is the blocker-coordinate version of that theorem.  No positivity
of the global equality state, no zero-free assumption, and no RH claim is made.
