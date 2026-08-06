# T-9502 — Quartic totient criterion and exact rightmost-zero exponent

Claim ID: `T-9502`  
Title: RH is equivalent to one quartic-smoothed finite totient error at exponent `-3/2`  
Status: `PROPOSED — COMPLETE TRANSFER THEOREM; RH BOUND OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9508`; the classical Mertens-function equivalence to RH; Mellin inversion  
Scope: full Riemann Hypothesis  
Related counterexample candidates: none

## Finite criterion

For real `x>1`, define

\[
\boxed{
\mathcal Q(x)=
\frac1x\sum_{1\le n<x}
 \frac{\varphi(n)}n
 \left(1-\frac{n^2}{x^2}\right)^2.}
\tag{T-9502.1}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff
\mathcal Q(x)=\frac{16}{5\pi^2}
+O_\varepsilon(x^{-3/2+\varepsilon})
\quad\text{for every }\varepsilon>0.}
\tag{T-9502.2}
\]

The observable is finite, uses exact totients and a polynomial weight, and has
no zero list, infinite prime tail, special function, or numerical eigenspace.

## Elementary Mellin kernel

Let

\[
w(u)=(1-u^2)^2\mathbf1_{(0,1)}(u).
\tag{T-9502.3}
\]

Its Mellin transform is the rational function

\[
\boxed{
\widehat w(z)
=\int_0^1(1-u^2)^2u^{z-1}\,du
=\frac1z-\frac2{z+2}+\frac1{z+4}
=\frac8{z(z+2)(z+4)}.}
\tag{T-9502.4}
\]

For `Re z>1`,

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^{z+1}}
=\frac{\zeta(z)}{\zeta(z+1)}.
\tag{T-9502.5}
\]

Therefore

\[
\boxed{
\mathcal Q(x)=
\frac1{2\pi i}\int_{(c)}
 \frac8{z(z+2)(z+4)}
 \frac{\zeta(z)}{\zeta(z+1)}
 x^{z-1}\,dz,
\qquad c>1.}
\tag{T-9502.6}
\]

The pole at `z=1` contributes

\[
\frac{8}{15\zeta(2)}
=\frac{16}{5\pi^2}.
\tag{T-9502.7}
\]

The apparent kernel poles at `z=0,-2,-4` are canceled by the pole of
`zeta(z+1)` at `z=0` and the trivial zeros of `zeta(z)` at `z=-2,-4`.

Every nontrivial zero `rho` creates a genuine pole

\[
\boxed{z=\rho-1.}
\tag{T-9502.8}
\]

There is no cancellation:

1. `zeta(rho-1)` is nonzero because `rho-1` is nonreal with real part in
   `(-1,0)`;
2. the rational kernel has zeros nowhere.

## RH implies the estimate

The classical Littlewood equivalence gives

\[
\mathrm{RH}
\quad\Longrightarrow\quad
M(X)=\sum_{n\le X}\mu(n)
=O_\varepsilon(X^{1/2+\varepsilon})
\tag{T-9502.9}
\]

for every `epsilon>0`.

Applying `L-9508` with `beta=1/2` yields directly

\[
\mathcal Q(x)-\frac{16}{5\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon}).
\]

No contour estimate on `1/zeta` and no simplicity assumption on the zeros is
needed for this direction.

## The estimate implies RH

Put

\[
\mathcal E_2(x)=
\mathcal Q(x)-\frac{16}{5\pi^2}.
\]

For `Re z>1`, direct Mellin integration gives

\[
\boxed{
\frac8{z(z+2)(z+4)}
 \frac{\zeta(z)}{\zeta(z+1)}
-\frac{16/(5\pi^2)}{z-1}
=\int_1^\infty\mathcal E_2(x)x^{-z}\,dx.}
\tag{T-9502.10}
\]

If the estimate in (T-9502.2) holds for every `epsilon>0`, the right side is
analytic in

\[
\Re z>-\frac12.
\]

A zero `rho` with `Re rho>1/2` would produce the uncanceled pole `rho-1` in
that half-plane, contradiction. The functional equation excludes the reflected
left-half counterpart. Hence RH holds.

## Exact rightmost-zero exponent

Let

\[
\beta_*=\sup_{\zeta(\rho)=0}\Re\rho,
\qquad
\Theta_\zeta=\beta_*-\frac12.
\tag{T-9502.11}
\]

Define

\[
\vartheta_2=
\inf\left\{\theta\ge0:
 \mathcal E_2(x)
 =O_\varepsilon(x^{-3/2+\theta+\varepsilon})
 \text{ for every }\varepsilon>0
\right\}.
\tag{T-9502.12}
\]

Then

\[
\boxed{\vartheta_2=\Theta_\zeta.}
\tag{T-9502.13}
\]

### Upper bound

The classical generalized Mertens transfer says that absence of zeros in

\[
\Re s>\beta
\]

implies

\[
M(X)=O_\varepsilon(X^{\beta+\varepsilon}).
\]

Apply `L-9508` to obtain

\[
\mathcal E_2(x)=O_\varepsilon(x^{\beta-2+\varepsilon}).
\]

Letting `beta` decrease to `beta_*` gives

\[
\vartheta_2\le\beta_*-\frac12.
\]

### Lower bound

Any stronger exponent would make the Mellin transform in (T-9502.10) analytic
to the right of one of the genuine poles `rho-1`. Therefore

\[
\vartheta_2\ge\beta_*-\frac12.
\]

Together these prove (T-9502.13).

## Relation to the square-screw criterion

`T-19801`--`T-19802` encode the same quantity `Theta_zeta` through the positive
excess of a logarithmic von-Mangoldt Riesz mean. `T-9502` encodes it through a
quartic-smoothed totient error.

Thus

\[
\boxed{
\vartheta_{\rm square\ screw}
=\vartheta_{\rm quartic\ totient}
=\Theta_\zeta.}
\tag{T-9502.14}
\]

This is an exact duality between a prime-power explicit-formula observable and
a Möbius/totient visible-lattice observable.

## Why the quartic weight is load-bearing

The square-root semicircle endpoint of `T-9501` is the natural kernel inherited
from the Jordan/Volterra program, but its Mellin transform decays only like
`|t|^-3/2`.

The quartic weight has rational Mellin decay `|t|^-3` and, more importantly,
its discrete cell sum collapses exactly to bounded Bernoulli polynomials. This
makes the RH implication an elementary consequence of the Mertens estimate and
removes the delicate oscillatory contour step.

## Proof-producing interface

At one exact rational or integer `x`, a proof object requires:

1. exact `phi(n)` for every `n<x`;
2. exact rational evaluation of `(1-(n/x)^2)^2`;
3. exact rational summation of `Q(x)`;
4. a directed interval for `pi^2` only when comparing to the main constant.

For rational `x`, the entire finite sum is rational. An equivalent certificate
may use the exact Bernoulli–Möbius decomposition `L-9508.10`.

A finite ladder does not prove the asymptotic estimate.

## SERIOUS RESOLUTION PATH

The full RH problem has now been reduced to the single direct arithmetic bound

\[
\boxed{
\mathcal Q(x)-\frac{16}{5\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon}).}
\tag{T-9502.15}
\]

There is no remaining packet exhaustion, operator compactness, Schur complement,
source conditioning, zero census, or finite-to-global bridge after this bound.

The exact finite decomposition `L-9508.10` exposes five coupled Mertens channels
that must be controlled. Proving (T-9502.15) is a full resolution of RH; it is
not proved here.

## Independent-review targets

1. Verify the rational Mellin transform and main residue.
2. Check cancellation at `z=0,-2,-4`.
3. Audit noncancellation at every `rho-1`.
4. Reconstruct the exact Mertens transfer from `L-9508`.
5. Verify the Mellin-transform converse and exponent equality.
