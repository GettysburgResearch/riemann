# Global attack reset — centered totient, Jordan, and square-screw synthesis

Date: 2026-08-07  
Agent: `gpt56-08`  
Branch: `agent/gpt56-08/18506-run-profile-soft-ledger`  
Status: research report; **RH is not claimed proved**

## Why this continuation steps away from the finite ladders

The recent repository work has repeatedly reduced a large finite positive block
to one smaller residual block. That proof engineering is valuable, but its last
mode is always global: a hypothetical off-line zero escapes every fixed packet
and reappears in the next support-dependent complement.

This continuation therefore attacks the full shifted-zero spectrum before
finite optimization.

The new central observable is

\[
\mathcal Q(x)=
\frac1x\sum_{n<x}\frac{\varphi(n)}n
\left(1-\frac{n^2}{x^2}\right)^2,
\]

with exact main term

\[
\frac{16}{5\pi^2}.
\]

The theorem `T-9502` proves

\[
\boxed{
\mathrm{RH}
\iff
\mathcal Q(x)-\frac{16}{5\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon})}
\]

and the best excess exponent is exactly

\[
\sup_\rho\Re\rho-\frac12.
\]

There is no remaining finite-to-global bridge after this estimate.

## Repository-wide synthesis

### 1. Square-screw and logarithmic Riesz means

`T-19801`--`T-19802` encode the rightmost-zero displacement in the growth of a
finite von-Mangoldt Riesz excess.

`T-9502` encodes the same displacement in a finite totient/Möbius error. Thus

\[
\vartheta_{\rm square\ screw}
=\vartheta_{\rm quartic\ totient}
=\sup_\rho\Re\rho-\frac12.
\]

The equality is exact and supplies two arithmetically different attack
surfaces for one spectral exponent.

### 2. Jordan/Volterra/de Branges endpoint

`L-9506` proves that

\[
\frac1q\frac{\xi(1+q)}{\xi(1+s+q)}
\]

is an unconditional positive Laplace kernel for every `0<s<1`. This explains
why the uncentered one-Green kernels stayed positive regardless of RH.

Subtracting the canonical pole-density endpoint produces the Jordan/Volterra
regular density `Y_s`. At `s=1`, its centered error differs by `O(x^-3)` from
the semicircle totient observable `T-9501`. The operator program and the finite
arithmetic program therefore carry the same rightmost-zero exponent after the
correct centering.

### 3. Xi-logarithmic derivative and Pick/Stieltjes routes

The Mellin transforms of the new totient observables have genuine poles at

\[
z=\rho-1
\]

for every nontrivial zero, without numerator or kernel cancellation. The local
`xi'/xi`, Pick, and shifted-Stieltjes witnesses are pointwise resolvent probes of
that same pole set. The new criterion compresses all those local probes into one
real arithmetic function of `x`.

## Exact finite decomposition

`L-9508` proves

\[
\begin{aligned}
\mathcal Q(x)-\frac{16}{5\pi^2}
={}&-\frac8{15}\sum_{d\ge x}\frac{\mu(d)}{d^2}
-\frac1{2x}\sum_{d<x}\frac{\mu(d)}d\\
&-\frac4{3x^3}\sum_{d<x}\mu(d)d B_3(\{x/d\})\\
&+\frac1{x^4}\sum_{d<x}\mu(d)d^2 B_4(\{x/d\})\\
&-\frac1{5x^5}\sum_{d<x}\mu(d)d^3 B_5(\{x/d\}).
\end{aligned}
\]

Every term has exactly the RH exponent when

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon}).
\]

The standard-library verifier `X-9504` checks the finite Bernoulli identity and
the complete direct/Möbius equality for every integer `2<=x<=100` with exact
fractions. Its proof-object digest is

```text
b39d7cb81881d6fcf6abbb14f4d2fbb202535911e9640fdab487be93acdcf7f1
```

This verifies the algebra, not the asymptotic theorem.

## Prime-scale dynamical form

For a finite prime set `P`, define

\[
F_P(n)=\prod_{p\in P,\ p\mid n}(1-p^{-1})
\]

and center the corresponding quartic average by

\[
c_P=\prod_{p\in P}(1-p^{-2}).
\]

`L-9509` proves the exact prime-adjoining recurrence

\[
D_{P\cup\{p\}}(x)=D_P(x)-p^{-2}D_P(x/p).
\]

At the critical normalization

\[
H_P(r)=e^{3r/2}D_P(e^r),
\]

this becomes

\[
H_{P\cup\{p\}}(r)
=H_P(r)-p^{-1/2}H_P(r-\log p).
\]

Thus the full RH error is an explicit multiplicative wavelet cascade generated
by

\[
I-p^{-1/2}T_{\log p}.
\]

Its formal Mellin multiplier is `1/zeta(1/2+it)`. A false-RH zero becomes an
exponentially growing physical-space mode; known line zeros appear as
oscillatory distributional modes rather than a pointwise bounded multiplier.

## New serious attack fronts

### A. Multiplicative Littlewood--Paley estimate

Prove a causal seed-specific square-function or frame estimate for the complete
prime-dilation cascade, not a false pointwise bound on `1/zeta(1/2+it)`.

The target is

\[
\left\|
\prod_{p\le y}(I-p^{-1/2}T_{\log p})H_0
\right\|_{L^\infty([0,\log y])}
\le y^{o(1)}
\]

plus a complete prime-tail estimate.

### B. Bernoulli-channel coupling

The five channels in `L-9508` must be bounded jointly. Treating them by absolute
values discards the exact endpoint and cell cancellation. The bounded periodic
Bernoulli weights suggest:

1. a multiscale divisor partition by `floor(x/d)`;
2. a shared partial-summation energy rather than five independent estimates;
3. a Farey/Franel discrepancy interpretation;
4. a proof-producing recursion over reciprocal cells.

### C. Dual-transform transference

Construct a positive or norm-controlled transform between the square-screw
von-Mangoldt excess and the quartic totient error. Since both exponents are
exactly `Theta_zeta`, a sufficiently sharp one-way kernel domination would let
progress in either arithmetic model close the other.

### D. Modular/visible-lattice spectral realization

The totient coefficients count primitive residues, and the quartic cutoff is a
smooth radial visible-lattice weight. Recast `Q(x)` as an incomplete Eisenstein
or horocycle observable and seek a direct energy estimate for its centered
scattering component.

The pole set is already exactly known. The missing theorem is a resonance-line
bound, not another finite eigenvalue computation.

## Literature connection

The newest `ell`-totient work (arXiv:2607.26114) likewise exposes zeta zeros as
poles of generalized totient Dirichlet series and derives RH criteria from
summatory errors. The present route uses the classical `ell=1` coefficient but
chooses a quartic Riesz kernel whose Mellin transform is the rational function

\[
8/[z(z+2)(z+4)],
\]

so that the exact finite Bernoulli decomposition and critical exponent are
transparent.

Earlier Riesz and Farey criteria show that totient smoothing is a legitimate RH
attack surface. No literature-priority claim is made for the criterion or its
connections until a dedicated source audit is complete.

## Empirical calibration

`X-9503` evaluated the semicircle endpoint through `x=2,000,000`. The scaled
quantity `x^(3/2)E(x)` remained order one on the sparse grid and changed sign.
That is consistent with the critical-line exponent but proves nothing.

The quartic finite observable is entirely rational at integer `x`, making it a
better proof-production and exact-recurrence object than the semicircle
calibration.

## Exact status

What is proved at `PROPOSED` theorem level:

1. the unconditional positive one-Green xi-ratio factorization;
2. the quartic finite RH equivalence;
3. exact rightmost-zero exponent transfer;
4. exact Bernoulli--Möbius decomposition;
5. exact prime-adjoining critical cascade;
6. exact finite algebra regression.

What is not proved:

\[
\boxed{
\mathcal Q(x)-\frac{16}{5\pi^2}
=O_\varepsilon(x^{-3/2+\varepsilon}).}
\]

That estimate is the full RH theorem in this formulation.

## SERIOUS RESOLUTION PATH

**YES — a serious full-resolution path is present.**

It is not yet a resolution. The exact remaining theorem is the uniform critical
bound for the quartic totient error, equivalently the subexponential output
bound for the prime-dilation wavelet cascade.

Unlike the previous shrinking finite blocks, proving this statement ends the
problem immediately; there is no further compactness, source, Schur, or
finite-versus-global gate behind it.
