# L-15427 — The singular Jordan channel transmutes into an endpoint trace

Claim ID: `L-15427`  
Title: Exact Hardy Cauchy derivative identity for the zeta-pole/gamma-zero cancellation  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `R-15405`; elementary Hardy-space Laplace kernels  
Scope: singular part of the missing Mellin-boundary intertwiner  
Related counterexample candidates: none

## Polarized boundary coordinates

Let

\[
 u={s+\bar t\over2},
 \qquad
 u_0=1+\omega,
 \tag{L-15427.1}
\]

and put

\[
 z=s-u_0,
 \qquad
 w=t-u_0.
 \tag{L-15427.2}
\]

Then

\[
 u-u_0={z+\bar w\over2}.
 \tag{L-15427.3}
\]

The singular arithmetic kernel from `R-15405.3` is

\[
 \boxed{
 A_\omega(s,t)
 \sim {2\over\zeta(1+2\omega)}
 {1\over z+\bar w}.}
 \tag{L-15427.4}
\]

## Hardy Cauchy feature

For `Re z>0`, define

\[
 k_z(x)=e^{-zx},
 \qquad x>0.
 \tag{L-15427.5}
\]

In `L^2(0,infinity)` with inner product linear in the second variable,

\[
 \boxed{
 \langle k_w,k_z\rangle
 ={1\over z+\bar w}.}
 \tag{L-15427.6}
\]

Let

\[
 D=-{d\over dx}
 \tag{L-15427.7}
\]

on the exponential core. Since `Dk_z=zk_z`,

\[
\begin{aligned}
 \langle Dk_w,k_z\rangle
 +\langle k_w,Dk_z\rangle
 &={\bar w+z\over z+\bar w}\\
 &=1.
\end{aligned}
 \tag{L-15427.8}
\]

Equivalently, integration by parts gives

\[
 \boxed{
 \langle Dk_w,k_z\rangle
 +\langle k_w,Dk_z\rangle
 =k_z(0)\overline{k_w(0)}.}
 \tag{L-15427.9}
\]

Thus multiplication of the Cauchy pole by the linear zero `z+bar(w)` is exactly
an endpoint evaluation.

## Pole-zero transmutation constant

By `R-15405.8`, the polarized archimedean zero contributes

\[
 {B_0\over4\omega}(z+\bar w)
 \tag{L-15427.10}
\]

at leading order. Combining (L-15427.4), (L-15427.9), and
(L-15427.10) gives the finite rank-one boundary kernel

\[
 \boxed{
 {B_0\over2\omega\zeta(1+2\omega)}
 k_z(0)\overline{k_w(0)}.}
 \tag{L-15427.11}
\]

This is exactly the scalar limit in `R-15405.9`.

## Explicit singular intertwiner

Define the singular arithmetic lift

\[
 \mathcal J_{\omega}^{\rm sing}(z)
 =\sqrt{2/\zeta(1+2\omega)}\,k_z
 \tag{L-15427.12}
\]

and the boundary operator

\[
 \mathcal B_\omega f
 =\sqrt{B_0/(4\omega)}\,f(0).
 \tag{L-15427.13}
\]

Then the symmetrized derivative form satisfies

\[
 \boxed{
 \langle\mathcal B_\omega D
  \mathcal J_{\omega}^{\rm sing}(w),
  \mathcal B_\omega
  \mathcal J_{\omega}^{\rm sing}(z)\rangle
 +\text{adjoint term}
 ={B_0\over2\omega\zeta(1+2\omega)}.}
 \tag{L-15427.14}
\]

The singular local-place channel is therefore completely routed into one
endpoint trace. It is not part of the Volterra tail norm.

## Connection with the Mellin-boundary concomitant

The exact Mellin atom split in the current Volterra source separates each
incomplete-gamma atom into a moving Volterra tail and a boundary prefix. The
source identifies a new primitive endpoint functional `M_z` as the missing
concomitant. Equation (L-15427.9) shows the universal model of that channel:
the arithmetic Cauchy pole is converted by the gamma zero into a derivative
boundary trace.

An exact normalization match between (L-15427.13) and the full-`Phi` `M_z`
requires a source-level Mellin calculation. The singular mechanism and its
coefficient are already fixed by (L-15427.11).

## Remaining regular kernel

After removing the pole channel, define

\[
 A_\omega^{\rm reg}(u)
 ={\zeta(u-\omega)\over\zeta(u+\omega)}
 -{1\over\zeta(1+2\omega)(u-u_0)}.
 \tag{L-15427.15}
\]

The smallest remaining intertwining problem is to identify the coupled regular
kernel

\[
 A_\omega^{\rm reg}(u)\widehat g_\omega(u)
 \tag{L-15427.16}
\]

with the completed Volterra tail quotient in the augmented
`(endpoint trace) direct-sum (tail)` metric. Scalar Jordan Jensen cannot do
this. By `R-15405.14`, the regular arithmetic factor is the Laplace transform
of an explicit atomic-minus-Lebesgue signed measure; no alternate positive
measure representation is available.

## Gap audit

- The Cauchy/derivative/endpoint identity is exact.
- The leading pole and zero coefficients are exact.
- The full regularized Mellin kernel, not the singular channel, remains the
  unresolved metric identification.
- Any claimed positive intertwiner omitting the endpoint trace contradicts
  `R-15405`.
