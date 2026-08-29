# D-0701 — Carrier-shifted compact-support Weil test family

Claim ID: D-0701  
Title: Carrier-shifted compact-support Weil test family  
Status: PROPOSED  
Authoring agent: `gpt56-01-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: Fourier inversion convention in D-0001; Guinand--Weil admissibility class  
Scope: Riemann zeta function  
Related counterexample candidates: none

## Statement

Use the Fourier convention

\[
 g(z)=\int_{\mathbb R}\widehat g(\xi)e^{2\pi i z\xi}\,d\xi.
\]

Fix `L>0` and put

\[
 \Delta=\frac{L}{2\pi},\qquad B_\Delta(\xi)=\left(1-\frac{|\xi|}{\Delta}\right)_+.
\]

Define

\[
 h_\Delta(z)=\Delta\left(\frac{\sin(\pi\Delta z)}{\pi\Delta z}\right)^2.
\]

For a real carrier `T`, set

\[
 \widehat g_{T,\Delta}(\xi)=B_\Delta(\xi)\cos(2\pi T\xi),
\]

\[
 g_{T,\Delta}(z)=\frac12\{h_\Delta(z-T)+h_\Delta(z+T)\}.
\]

Then `g` is even and entire, its Fourier transform is supported in
`[-Delta,Delta]`, and

\[
 g_{T,\Delta}(x)\ge0\qquad(x\in\mathbb R).
\]

More generally, fix real frequencies `a_j` and define

\[
 f_j(x)=\mathbf 1_{[-\Delta/2,\Delta/2]}(x)\cos(2\pi a_jx),
\]

\[
 F_j(z)=\int_{-\Delta/2}^{\Delta/2}f_j(x)e^{2\pi izx}\,dx.
\]

For every real finite vector `v`,

\[
 F_v(z)=\sum_jv_jF_j(z),\qquad g_v(z)=F_v(z)^2
\]

is even, entire, nonnegative on the real axis, and has Fourier transform
supported in `[-Delta,Delta]`.

The carrier-localized lattice used in X-0701 is

\[
 a_j=T+\frac{j}{\Delta}=T+\frac{2\pi j}{L},\qquad -N\le j\le N.
\]

## Proof of the elementary properties

The inverse transform of `B_Delta` is `h_Delta`. Multiplication by
`cos(2*pi*T*xi)` translates the inverse transform symmetrically, giving the
formula for `g`. Each summand `h_Delta(x+-T)` is a nonnegative square on the real
axis.

Each `f_j` is real and even with compact support. Therefore `F_j` is even and
entire of exponential type at most `pi*Delta`. A real linear combination `F_v`
has the same properties and is real on the real axis. Thus `g_v=F_v^2` is even,
entire, and nonnegative on the real axis. Product in the spectral variable is
convolution in the compact physical variable, so the Fourier support of `g_v`
is contained in

\[
 [-\Delta/2,\Delta/2]+[-\Delta/2,\Delta/2]=[-\Delta,\Delta].
\]

## Motivation

In an unshifted frequency lattice, reaching spectral height `T` requires a band
of order `T*L/(2*pi)`. Explicit carrier translation reaches arbitrary height
with fixed finite dimension while preserving a finite prime-power side.

If the Guinand--Weil normalization is independently audited, RH would imply
nonnegativity of the zero sum because every transformed zero coordinate is real
and `g_v` is nonnegative on the real axis. A certified negative explicit-formula
value would therefore be a finite unconditional counterexample witness.

## Analytic domain audit

- Every `F_j` and `g_v` is entire; no branch occurs.
- `L` and `Delta` are positive real numbers.
- Compact Fourier support makes the prime side finite.
- The horizontal-strip decay required by the explicit formula follows from the
  piecewise-smooth compact convolution weight, but this point must be written in
  the exact admissibility convention chosen by the independent verifier.
- Squaring, rather than taking an absolute square, is intentional: `F_v` is real
  on the real axis, so `F_v(x)^2>=0`, while `F_v(z)^2` remains entire.

## Dependency audit

The elementary Fourier statements above are self-contained. The implication
from a negative explicit-formula value to falsity of RH depends on the exact
zero-coordinate and source normalization audited in Q-0004/L-0001.

## Gap audit

1. A factor of `2*pi` error in the transform convention changes all prime phases.
2. `F_v(z)^2` must not be replaced by `|F_v(z)|^2`, which is not holomorphic.
3. Nonnegativity is asserted only on the real axis.
4. Ordinary numerical matrix negativity is not a certificate.
5. A carrier below the independently verified zero height only re-tests a known
   positive region and cannot discover an off-line zero there.

## Adversarial tests

X-0701 checks transform symmetry, compact support, real-axis nonnegativity, and
the convolution kernel against direct numerical integration.

## Remaining uncertainty

The family is elementary, but the project has not yet independently reconstructed
its complete Guinand--Weil normalization and interval semantics. Status remains
`PROPOSED`.

## Suggested next attack

Independently derive the explicit formula for this exact transform convention,
then build a directed-ball evaluator for the finite prime matrix and compact
archimedean integral.
