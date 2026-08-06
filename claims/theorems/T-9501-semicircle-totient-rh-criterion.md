# T-9501 — Semicircle totient criterion and exact rightmost-zero exponent

Claim ID: `T-9501`  
Title: A semicircle-weighted finite totient sum has RH-scale error exactly when RH holds  
Status: `PROPOSED — COMPLETE TRANSFER THEOREM; RH-SCALE ESTIMATE OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: standard analytic continuation and zero-free half-plane of `zeta`; Mellin inversion; standard contour/abscissa transfer  
Scope: direct global equivalent criterion for RH  
Related counterexample candidates: none

## The finite arithmetic observable

For real `x>1`, define

\[
\boxed{
\mathcal V(x)
=\frac2x\sum_{1\le n<x}
 \frac{\varphi(n)}n
 \sqrt{1-\frac{n^2}{x^2}}.}
\tag{T-9501.1}
\]

Every level is a finite arithmetic sum. There is no zero list, prime tail,
contour count, or fitted spectral model in the definition.

Let

\[
\mathcal E(x)=\mathcal V(x)-\frac3\pi.
\tag{T-9501.2}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\mathcal E(x)=O_\varepsilon
\left(x^{-3/2+\varepsilon}\right)
\quad\text{for every }\varepsilon>0.}
\tag{T-9501.3}
\]

Thus RH is equivalent to square-root cancellation beyond the unconditional
`x^{-1}` prime-number-theorem scale in one geometrically elementary smoothed
totient sum.

## Exact Mellin transform

Put

\[
k(u)=2\sqrt{1-u^2}\,\mathbf1_{(0,1)}(u).
\tag{T-9501.4}
\]

Its Mellin transform is

\[
\boxed{
\widehat k(z)
=\int_0^1k(u)u^{z-1}\,du
=B(z/2,3/2)
=\frac{\Gamma(z/2)\Gamma(3/2)}
       {\Gamma((z+3)/2)}.}
\tag{T-9501.5}
\]

Since

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^{z+1}}
=\frac{\zeta(z)}{\zeta(z+1)}
\qquad(\Re z>1),
\tag{T-9501.6}
\]

Mellin inversion gives

\[
\boxed{
\mathcal V(x)
=\frac1{2\pi i}\int_{(c)}
 \widehat k(z)
 \frac{\zeta(z)}{\zeta(z+1)}
 x^{z-1}\,dz,
\qquad c>1.}
\tag{T-9501.7}
\]

The pole at `z=1` contributes

\[
\frac{\widehat k(1)}{\zeta(2)}
=\frac{\pi/2}{\pi^2/6}
=\frac3\pi.
\tag{T-9501.8}
\]

At `z=0`, the pole of `Gamma(z/2)` is canceled by the zero of
`1/zeta(z+1)`. The remaining poles relevant to the rightmost error exponent are

\[
z=\rho-1,
\tag{T-9501.9}
\]

where `rho` runs over nontrivial zeta zeros, with their multiplicities.

## No zero-pole cancellation

Every pole in (T-9501.9) is genuine.

- `zeta(rho-1)` is nonzero: `rho-1` is nonreal with real part in `(-1,0)`, so it is neither a nontrivial zero nor a negative even trivial zero.
- `widehat k(rho-1)` is nonzero: gamma has no zeros, and the zeros created by the denominator gamma factor occur only at negative odd real integers.

Thus the observable sees every nontrivial zero without a generic-parameter or
noncancellation hypothesis.

## Proof that RH implies the bound

Assume RH. Then every denominator-zero pole in (T-9501.9) lies on

\[
\Re z=-\frac12.
\]

For fixed `epsilon>0`, shift the Mellin contour from `Re z=c` to

\[
\Re z=-\frac12+\varepsilon.
\]

Only the main pole at `z=1` is crossed. Standard zeta bounds in the zero-free
half-plane `Re(z+1)>1/2`, together with

\[
\widehat k(\sigma+it)
=O_\sigma((1+|t|)^{-3/2}),
\tag{T-9501.10}
\]

control the shifted integral and the horizontal truncation sides. This yields

\[
\mathcal V(x)=\frac3\pi
+O_\varepsilon(x^{-3/2+\varepsilon}).
\]

Multiple zeros contribute powers of `log x`, which are absorbed by
`x^epsilon`.

## Proof of the converse

For `Re z>1`, direct Mellin integration gives

\[
\int_0^\infty \mathcal V(x)x^{-z}\,dx
=\widehat k(z)\frac{\zeta(z)}{\zeta(z+1)}.
\tag{T-9501.11}
\]

Since `V(x)=0` for `0<x<=1`, subtraction of the main constant gives

\[
\boxed{
\widehat k(z)\frac{\zeta(z)}{\zeta(z+1)}
-\frac{3/\pi}{z-1}
=\int_1^\infty \mathcal E(x)x^{-z}\,dx.}
\tag{T-9501.12}
\]

If the bound in (T-9501.3) holds for every `epsilon>0`, the integral on the
right is analytic throughout

\[
\Re z>-\frac12.
\]

But a zero `rho` with `Re rho>1/2` would create the uncanceled pole
`z=rho-1` in that half-plane, contradicting analyticity. Hence no zero lies to
the right of the critical line. The functional equation supplies the reflected
half, proving RH.

## Exact rightmost-zero exponent

Let

\[
\beta_*=\sup_{\zeta(\rho)=0}\Re\rho,
\qquad
\Theta_\zeta=\beta_*-\frac12.
\tag{T-9501.13}
\]

Define the arithmetic error exponent

\[
\vartheta_{\rm sc}
=\inf\left\{\theta\ge0:
 \mathcal E(x)=O_\varepsilon
 (x^{-3/2+\theta+\varepsilon})
 \text{ for every }\varepsilon>0
 \right\}.
\tag{T-9501.14}
\]

The Mellin pole set and the standard converse contour transfer give

\[
\boxed{
\vartheta_{\rm sc}=\Theta_\zeta.}
\tag{T-9501.15}
\]

Indeed the rightmost zero poles have real-part supremum `beta_*-1`, so the
inverse-Mellin error exponent is `beta_*-2=-3/2+Theta_zeta`. A stronger claimed
error would analytically continue (T-9501.12) through one of those poles.

Consequently the semicircle observable and the square-screw/Riesz observable of
`T-19801`--`T-19802` measure the same rightmost-zero displacement through two
different finite arithmetic transforms.

## Exact relation to the Jordan/Volterra density

The endpoint `s=1` of `L-9506` has

\[
F_1(n)=\frac{\varphi(n)}n,
\qquad
n_1(t)=2e^{-t}\sqrt{1-e^{-2t}},
\qquad
c_1=\frac6{\pi^2}.
\tag{T-9501.16}
\]

Therefore its centered density satisfies the exact identity

\[
\boxed{
Y_1(\log x)
=\mathcal V(x)
-\frac6{\pi^2}\left[
 \frac\pi2-\arcsin\frac1x
 -\frac1x\sqrt{1-\frac1{x^2}}
 \right].}
\tag{T-9501.17}
\]

The positive pole-density main term is

\[
A_1x^{-1}=\frac{12}{\pi^2x}.
\tag{T-9501.18}
\]

Thus

\[
\boxed{
\begin{aligned}
&Y_1(\log x)-\frac{12}{\pi^2x}\\
&\quad=\mathcal E(x)
+\frac6{\pi^2}\left[
 \arcsin\frac1x
 +\frac1x\sqrt{1-\frac1{x^2}}
 -\frac2x
 \right].
\end{aligned}}
\tag{T-9501.19}
\]

The bracket is `O(x^-3)`. Hence the centered Green-density error and the
semicircle totient error have exactly the same RH-bearing exponent.

This is the direct bridge between:

1. the terminal-prime/Jordan/Volterra program;
2. the square-screw/rightmost-zero program;
3. classical smoothed totient/Farey arithmetic.

## Proof-producing interface

At a fixed rational or integer `x>1`, a directed certificate requires only:

1. exact `phi(n)` for `1<=n<x`;
2. outward enclosures of `sqrt(1-(n/x)^2)`;
3. exact rational factors `phi(n)/n`;
4. a directed enclosure of the final finite sum and of `3/pi`.

A finite small value is not a proof of RH. The proof target is the uniform
asymptotic exponent in (T-9501.3).

## Honest frontier

The equivalence and exact exponent transfer are complete modulo standard
Mellin-contour growth details. The estimate

\[
\boxed{
\mathcal V(x)-\frac3\pi
=O_\varepsilon(x^{-3/2+\varepsilon})}
\tag{T-9501.20}
\]

is not proved. Establishing it is a full resolution of RH, not a finite
positivity check.

## Independent-review targets

1. Recompute the Mellin transform (T-9501.5).
2. Audit the factor `x^{-1}` and exponent `x^{z-1}` in (T-9501.7).
3. Verify the main residue `3/pi`.
4. Check cancellation at `z=0` and noncancellation at every `rho-1`.
5. Reconstruct the Mellin-transform converse (T-9501.12).
6. Check every coefficient in the exact Green-density bridge (T-9501.17)--(T-9501.19).
