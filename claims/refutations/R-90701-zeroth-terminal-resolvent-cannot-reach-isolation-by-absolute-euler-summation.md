# R-90701 — Zeroth terminal resolvents cannot reach isolation through absolute Euler summation

Claim ID: `R-90701`  
Status: **PROPOSED COMPLETE EXACT SCOPE FIREWALL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: PR #375 heat kernel  
RH status: unproved

## Statement

For `0<y<1/2`, Laplace-transform the terminal heat kernel with damping
`e^(-alpha tau)`.

The target residue grows at rate `3y^2`, so the target Abel transform requires

\[
 \alpha>3y^2.
\]

After prime/continuum separation, the slow prime kernel decays at rate

\[
 \sqrt{\alpha+y^2}-y.
\]

At critical normalization, absolute Euler/Stieltjes interchange requires

\[
 \sqrt{\alpha+y^2}-y>\frac12,
\]

equivalently

\[
 \alpha>y+\frac14.
\]

The two boundaries differ by

\[
\boxed{
 y+\frac14-3y^2
 =3\left(\frac12-y\right)\left(y+\frac16\right)>0.
}
\]

Therefore no zeroth-order Laplace/Abel argument can both:

1. approach the terminal isolation boundary `alpha downarrow 3y^2`; and
2. justify termwise absolute Euler summation.

This is exactly the phase-blind saddle exponent found on PR #367.

## Surviving route

The firewall does not apply to high Laplace moments.  Freeze `alpha=1` in the
safe Euler region and insert `tau^k`.  The normalized moment concentrates at
heat time

\[
 \tau\asymp\frac{k}{1-3y^2},
\]

so terminal isolation is recovered through `k->infinity` without moving the
Euler sample points.  This is the construction of `T-90701`.

## Scope

This refutes only a zeroth-order absolute-Fubini closure.  It does not refute
completed-Chebyshev cancellation, high derivative order, conditional contour
continuation, the terminal heat criterion, or RH.
