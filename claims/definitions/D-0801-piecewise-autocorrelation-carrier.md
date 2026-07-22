# D-0801 — Piecewise autocorrelation carrier family

Claim ID: D-0801  
Title: Compact-support autocorrelation carriers with piecewise-constant envelopes  
Status: PROPOSED  
Authoring agent: `gpt56-04-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: the Fourier convention and Guinand--Weil admissibility interface of D-0001/D-0701  
Scope: a high-dimensional carrier family for Issue #29  
Related counterexample candidates: none

## Definitions

Fix `L>0`, put

\[
 \Delta=\frac{L}{2\pi},\qquad I=[-\Delta/2,\Delta/2],
\]

and partition `I` into `K` half-open cells of equal length

\[
 h=\frac{\Delta}{K},\qquad
 I_j=[-\Delta/2+jh,-\Delta/2+(j+1)h)
 \quad(0\le j<K),
\]

with the harmless endpoint convention on the final cell understood.  For
`v=(v_0,...,v_{K-1}) in C^K`, define

\[
 w_v(x)=\sum_{j=0}^{K-1}v_j\mathbf 1_{I_j}(x),
 \qquad
 W_v(z)=\int_I w_v(x)e^{2\pi izx}\,dx.
\]

Let

\[
 W_v^\#(z)=\overline{W_v(\overline z)}.
\]

This is an entire function: the conjugation applies to the coefficients of the
entire power series, not to the variable after evaluation.  For a real carrier
`T`, put

\[
 A_{T,v}(z)=W_v(z-T)W_v^\#(z-T)
\]

and define the even symmetrization

\[
 g_{T,v}(z)=\frac12\{A_{T,v}(z)+A_{T,v}(-z)\}.
\]

## Statement

For every `v`:

1. `g_{T,v}` is even and entire;
2. its Fourier transform is supported in `[-Delta,Delta]`;
3. for every real `r`,
   \[
   g_{T,v}(r)=\frac12\{|W_v(r-T)|^2+|W_v(-r-T)|^2\}\ge0;
   \]
4. its value at Fourier frequency zero is
   \[
   \widehat g_{T,v}(0)=\int_I|w_v(x)|^2dx
   =h\sum_{j=0}^{K-1}|v_j|^2.
   \]

For real `xi`, define the compact autocorrelation

\[
 R_v(\xi)=\int_{\mathbb R}w_v(x)\overline{w_v(x-\xi)}\,dx.
\]

Then

\[
 \widehat g_{T,v}(\xi)
 =\operatorname{Re}\!\left(e^{-2\pi iT\xi}R_v(\xi)\right),
 \qquad |\xi|\le\Delta,
\]

and the transform is zero outside that interval.

## Proof of the elementary properties

Compact support makes `W_v` entire of exponential type.  The Schwarz-reflected
function `W_v^#` is entire, so both products in the definition of `g` are
entire.  Replacing `z` by `-z` exchanges the two products, proving evenness.
On the real axis, `W_v^#(r-T)=overline{W_v(r-T)}`, which proves the displayed
nonnegativity.

The Fourier transform of `W_v W_v^#` is the convolution of `w_v` with
`x -> overline{w_v(-x)}`, namely the autocorrelation `R_v`.  Translation by
`T` multiplies that transform by `exp(-2*pi*i*T*xi)`.  Averaging with the
reflected product takes the real part and makes the weight even.  The support
is the difference set `I-I=[-Delta,Delta]`.  At zero, the autocorrelation is
the `L^2` norm, and disjoint equal cells give the final identity.

## Motivation

The cosine-box family of D-0701 is low dimensional unless many Fourier modes
are retained.  D-0801 instead allows a 1,024-cell envelope while preserving a
finite prime-power side.  The autocorrelation representation removes the
small high-carrier `a+b` prime branch present in the squared-cosine formula:
the complete prime matrix is a single compact Hermitian Toeplitz operator.

Under the audited Guinand--Weil implication, a rigorously certified negative
value of the exact explicit formula for one `g_{T,v}` would disprove RH.

## Analytic domain audit

- `W_v`, `W_v^#`, and `g_{T,v}` are entire; no logarithmic branch occurs.
- The cell envelope is compactly supported and integrable.  Its jump
  discontinuities give `W_v(r)=O(1/|r|)` away from removable zero denominators,
  so `g_{T,v}(r)=O(1/r^2)` on the real axis.
- The exact admissibility hypotheses of the chosen Guinand--Weil theorem still
  require independent review.  If more smoothness is required, the cell family
  must be mollified with a proof that the decisive sign survives.
- Complex `v` is intentional.  Real-axis nonnegativity follows from the
  Schwarz product, not from squaring a complex value.

## Gap audit

1. Nonnegative ordinary floating output is not a proof of positivity.
2. A negative prime-only or high-carrier-leading value is not yet the exact
   `P+R+A` value.
3. The external explicit-formula normalization remains PROPOSED.
4. Phase reduction at carriers near `10^12` needs ball arithmetic before any
   candidate promotion.
5. Increasing `K` changes the finite family; convergence to a continuous
   envelope statement is not asserted.

## Remaining uncertainty

The Fourier/autocorrelation algebra is self-contained, but the precise
Guinand--Weil admissibility interface and exact archimedean normalization have
not been independently reconstructed for this piecewise family.

## Suggested next attack

Derive the exact cellwise archimedean and pole Toeplitz blocks, implement their
ball enclosures, and freeze the leading eigenvector whenever a complete prime
operator crosses zero.
