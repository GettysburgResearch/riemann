# M-9502 — Global centered-spectrum attack through the minimal parabolic totient criterion

Claim ID: `M-9502`  
Title: Replace shrinking finite positivity gates by one full RH-scale two-Green arithmetic problem  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Last updated: 2026-08-07  
Dependencies: `L-9506`, `L-9510`, `T-9503`; comparison with `T-9502`, `T-19801`--`T-19802`, and `L-15428`--`L-15432`  
Scope: repository-wide full-problem attack plan  
Related counterexample candidates: none

## Strategic reset

The repository contains many correct finite positivity, Schur, packet, and
certificate interfaces. Their repeated final obstruction is an escaping global
mode. Enlarging another finite packet only changes the coordinate in which that
mode appears.

The new attack centers the arithmetic transform **before** optimization and
attacks the complete shifted-zero spectrum through one finite scalar:

\[
\boxed{
\mathcal E_1(x)=
\frac1x\sum_{n<x}\frac{\varphi(n)}n
 \left(1-\frac{n^2}{x^2}\right)
-\frac4{\pi^2}.}
\tag{M-9502.1}
\]

`T-9503` proves, at `PROPOSED` transfer-theorem status,

\[
\boxed{
\mathrm{RH}
\iff
\mathcal E_1(x)=O_\varepsilon(x^{-3/2+\varepsilon})}
\tag{M-9502.2}
\]

and the best excess exponent is exactly the horizontal displacement of the
rightmost zeta zero.

There is no finite-to-global bridge after this estimate.

## Why this is the minimal proof-facing kernel

The weight

\[
1-u^2
\]

has Mellin transform

\[
\boxed{
\frac2{z(z+2)}.}
\tag{M-9502.3}
\]

This is the smallest polynomial Green depth that:

1. retains every shifted-zero pole `z=rho-1` without cancellation;
2. has sufficient vertical decay for the standard RH/Mertens transfer;
3. yields an exact finite Bernoulli decomposition;
4. reduces to only two periodic channels.

The semicircle weight is the exact Jordan/Volterra endpoint but its first
absolute-contour proof shortcut was incomplete; see `R-9502`. The quartic
criterion `T-9502` remains a more strongly smoothed cross-check. `T-9503` is the
minimal primary target.

## Exact full-problem decomposition

`L-9510` proves

\[
\boxed{
\begin{aligned}
\mathcal E_1(x)={}&
-\frac23\sum_{d\ge x}\frac{\mu(d)}{d^2}
-\frac1{2x}\sum_{d<x}\frac{\mu(d)}d\\
&-\frac1{x^2}\sum_{d<x}
 \mu(d)B_2(\{x/d\})\\
&+\frac1{3x^3}\sum_{d<x}
 \mu(d)d B_3(\{x/d\}).
\end{aligned}}
\tag{M-9502.4}
\]

The two periodic Bernoulli channels and the two ordinary Mertens tails all have
the same critical exponent. A proof must retain their reciprocal-cell
cancellation; replacing them by four unrelated absolute estimates obscures the
structure.

## Repository-wide synthesis

### Square-screw program

`T-19801`--`T-19802` encode the rightmost-zero displacement in a logarithmic
von-Mangoldt Riesz excess. `T-9503` encodes it in a parabolic totient error:

\[
\boxed{
\vartheta_{\rm screw}
=\vartheta_{\rm parabolic\ totient}
=\Theta_\zeta.}
\tag{M-9502.5}
\]

This is an exact duality between prime-power and Möbius/totient transforms.

### Jordan/Volterra/de Branges program

`L-9506` proves that the uncentered one-Green completed ratio is positive
unconditionally. Its endpoint subtraction is the first RH-bearing channel.
The semicircle observable `T-9501` realizes that endpoint exactly; applying the
minimal additional polynomial Green smoothing gives `T-9503`.

Thus the operator's escaping centered mode becomes a concrete two-Green
visible-lattice error.

### Xi-logarithmic-derivative and Pick/Stieltjes routes

The Mellin transform

\[
\frac2{z(z+2)}\frac{\zeta(z)}{\zeta(z+1)}
-\frac{4/\pi^2}{z-1}
\]

has genuine poles precisely at `z=rho-1`. The local `xi'/xi`, Pick, and
Stieltjes witnesses are local resolvent probes of the same pole set; the
parabolic observable compresses them into one real arithmetic function.

## Prime-scale wavelet form

For finite prime sets, centered prime adjoining obeys

\[
D_{P\cup\{p\}}(x)=D_P(x)-p^{-2}D_P(x/p).
\tag{M-9502.6}
\]

At the critical normalization

\[
H_P(r)=e^{3r/2}D_P(e^r),
\]

this becomes

\[
\boxed{
H_{P\cup\{p\}}(r)
=H_P(r)-p^{-1/2}H_P(r-\log p).}
\tag{M-9502.7}
\]

The complete RH error is therefore a multiplicative wavelet cascade generated
by

\[
I-p^{-1/2}T_{\log p}
\]

acting on the two-Green causal seed `e^-r-e^-3r`.

A false-RH zero produces one exponentially growing generalized mode of this
cascade.

## Four attack fronts

### A. Reciprocal-cell energy

Group (M-9502.4) by

\[
\left\lfloor x/d\right\rfloor=m.
\]

Seek a shared energy or contraction identity for the Mertens increments and the
exact Bernoulli endpoint corrections. The target is a cellwise quadratic form,
not separate triangle inequalities.

### B. Multiplicative Littlewood--Paley estimate

Prove a causal seed-specific frame estimate for the prime-dilation cascade:

\[
\left\|
 \prod_{p\le y}(I-p^{-1/2}T_{\log p})H_0
\right\|_{L^\infty([0,\log y])}
\le y^{o(1)},
\tag{M-9502.8}
\]

plus a complete tail bound. A false pointwise bound on
`1/zeta(1/2+it)` is neither true nor required.

### C. Dual-transform transference

Construct a norm-controlled transform between the square-screw von-Mangoldt
excess and `E_1`. Since both exponents equal `Theta_zeta`, a sharp one-way
transference theorem would let progress in either representation close the
other.

### D. Modular/visible-lattice spectrum

Interpret the totient coefficients as primitive residues and the parabolic
cutoff as a smooth radial visible-lattice weight. Seek a trace, Eisenstein,
horocycle, or transfer-operator energy estimate for its centered scattering
component.

This is a global resonance-line problem, not another bounded-height
calculation.

## Exact computation layer

`X-9505` verifies the cell formula and the direct/Möbius identity with exact
fractions for every integer `2<=x<=100`. Its proof-object SHA-256 is

```text
dd484b080dde97f31881a86af9c1031bb13548309d32b0ce9c042848b3d873b1
```

A larger exact experiment should preserve both Bernoulli channels, reciprocal
cell partitions, prime-cascade stages, and matched square-screw values. Its
purpose is theorem discovery; no finite ladder proves (M-9502.2).

## Literature connection

Recent smoothed-totient work develops Riesz typical means and shows how
smoothing removes the arithmetic error that obstructs the raw summatory
totient function. Recent generalized-totient work likewise encodes zeta zeros
as poles of totient Dirichlet series. The current contribution isolates the
minimal rational Mellin kernel and an exact two-channel Bernoulli form.

No literature-priority claim is made pending a dedicated source audit.

## Closed shortcuts

The following do not suffice:

1. positivity of the uncentered safe one-Green kernel;
2. a finite exact table;
3. four independent absolute estimates that lose reciprocal-cell cancellation;
4. a floating `x^-3/2` fit;
5. finite-height zero verification;
6. increasing an unrelated packet dimension;
7. pointwise control of a truncated Euler product on the critical line.

## SERIOUS RESOLUTION PATH

A serious full-resolution path is present:

\[
\boxed{
\text{prove }
\mathcal E_1(x)=O_\varepsilon(x^{-3/2+\varepsilon})
\text{ through reciprocal cells, the prime cascade, or visible-lattice spectrum}.}
\tag{M-9502.9}
\]

This one theorem proves RH directly by `T-9503`. No operator limit, packet
exhaustion, Schur complement, source conditioning, or finite-versus-global gate
remains behind it.

The estimate itself is not proved.
