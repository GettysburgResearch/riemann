# R-21901 — Finite Hermite–Vandermonde interpolation does not preserve the prolate tail hierarchy

Claim ID: `R-21901`  
Title: A finite Xi-polynomial interpolation frame leaves an exact high-Fourier corrected tail that dominates the fixed-mode prolate defects  
Status: **PROPOSED — EXACT FOURIER IDENTITY AND CONDITIONAL SAFE-SUPPORT SEPARATION; SCOPE CORRECTION, NOT AN RH CLAIM**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15101`; `L-16213`; `L-19820`; the standard local minimum-modulus bound for zeta on a zero-avoiding grid  
Scope: the differential-Hermite finite interpolation idea developed on PR #219

## 1. Exact differential-Hermite ladder

Let

\[
\mathcal D=x\partial_x+\frac12
\]

and let `h` be the exact self-Fourier two-cancellation Gaussian source of
`L-15101`.  Put

\[
h_m=(-\mathcal D^2)^m h,
\qquad
K_m(t)=E(h_m)(e^t).
\]

The source constraints are preserved:

\[
h_m(0)=0,
\qquad
\int_{\mathbb R}h_m=0.
\]

Moreover

\[
E(\mathcal D f)(e^t)=\partial_t E(f)(e^t),
\]

so, in the centered Fourier–Mellin convention,

\[
\boxed{
\widehat K_m(z)=z^{2m}\Xi(z).
}
\tag{R-21901.1}
\]

Consequently every polynomial `P` gives an exact global radical image

\[
K_P=P(-\partial_t^2)K,
\qquad
\widehat K_P(z)=P(z^2)\Xi(z).
\tag{R-21901.2}
\]

## 2. Exact finite Vandermonde interpolation

Fix the centered interval `[-ell,ell]` and frequencies

\[
\omega_k=\frac{\pi k}{\ell}.
\]

For the periodization of `K_P`, Poisson summation gives the exact Fourier
coefficient

\[
\boxed{
\langle\Sigma_{2\ell}K_P,\phi_k\rangle
=(2\ell)^{-1/2}\Xi(\omega_k)P(\omega_k^2).
}
\tag{R-21901.3}
\]

If `Xi(omega_k) != 0` for `0<=k<=N`, the squared nodes are distinct and the
polynomial map in (R-21901.3) is an isomorphism onto the finite even Fourier
space.  Its inverse is the ordinary Lagrange–Vandermonde inverse.  This closes
the algebraic finite-frame problem, but only at the retained nodes.

## 3. The omitted high-Fourier term is exact

Let `Pi_N` denote projection onto `|k|<=N`.  The finite corrected tail of
`L-19820` contains the discarded periodic Fourier part

\[
e_{P,\ell,N}=(I-\Pi_N)\Sigma_{2\ell}K_P.
\]

Parseval gives the immutable identity

\[
\boxed{
\|e_{P,\ell,N}\|_2^2
=\frac1{2\ell}
 \sum_{|k|>N}
 |\Xi(\omega_k)|^2|P(\omega_k^2)|^2.
}
\tag{R-21901.4}
\]

This term is absent only for an all-grid cardinal source.  Finite interpolation
at `0,...,N` does not control it.

Writing the complete corrected tail as

\[
W_{P,\ell,N}
=t_{P,\ell}
-\iota\mathfrak F_{2\ell}t_{P,\ell}
+\iota e_{P,\ell,N},
\]

where `t=(I-P_ell)K_P`, orthogonality of the exterior and interior pieces gives

\[
\boxed{
\|W_{P,\ell,N}\|_2^2
\ge
\bigl(
 \|e_{P,\ell,N}\|_2
 -\|\mathfrak F_{2\ell}t_{P,\ell}\|_2
\bigr)_+^2.
}
\tag{R-21901.5}
\]

## 4. The target column already violates the prolate scale

Take `P=1`, so the global image is the Xi source itself.  The Gaussian estimate
of `L-15101` and its translated copies imply

\[
\|t_{1,\ell}\|_2+
\|\mathfrak F_{2\ell}t_{1,\ell}\|_2
\le
\exp\{-\pi e^{2\ell}+O(\ell)\}.
\tag{R-21901.6}
\]

On a zeta-safe support for which the first omitted grid point
`omega_(N+1)` stays at inverse-polynomial distance from every nearby critical
ordinate, the standard local product bound and Stirling give

\[
|\Xi(\omega_{N+1})|
\ge
\exp\left\{-\frac\pi4\omega_{N+1}-o(\ell)\right\}.
\tag{R-21901.7}
\]

For the quadratic-log cutoff

\[
N=\lceil c\ell^2\rceil,
\qquad c>0,
\]

one has

\[
\omega_{N+1}=\pi c\ell+O(\ell^{-1}),
\]

and therefore (R-21901.4)--(R-21901.7) imply

\[
\boxed{
\|W_{1,\ell,N}\|_2^2
\ge
\exp\left\{-\left(\frac{\pi^2c}{2}+o(1)\right)\ell\right\}.
}
\tag{R-21901.8}
\]

By contrast, every fixed-mode prolate defect used in the positive hierarchy
has the Fuchs scale

\[
d_n(\lambda)
=
\exp\{-4\pi\lambda^2+O_n(\log\lambda)\},
\qquad
\lambda=e^\ell.
\tag{R-21901.9}
\]

Hence

\[
\boxed{
\frac{\|W_{1,\ell,N}\|_2^2}{d_4(e^\ell)}
\longrightarrow\infty.
}
\tag{R-21901.10}
\]

The separation is double-exponential on the logarithmic support scale.

## 5. Consequence

The finite Hermite–Vandermonde frame is an exact algebraic frame, but it cannot
be inserted into the prolate theorem with the assertion

\[
\mu_D=O(d_4).
\]

Its first column already carries the much larger high-Fourier projection tail
(R-21901.8).  Thus the algebraic completion and the prolate concentration
hierarchy are not interchangeable.

This does not refute the all-grid differential cardinal construction of
`L-15631`: there

\[
\widehat q_k(\omega_j)=\delta_{kj}
\quad\text{for every integer }j,
\]

so the discarded periodic Fourier term is exactly zero.  Any viable complete
source frame must either use such an all-grid cardinal or include
(R-21901.4) in its declared tail metric.

## 6. Proof boundary

- Equations (R-21901.1)--(R-21901.5) are exact.
- The Gaussian fold estimate follows from the explicit source of `L-15101`.
- The quantitative lower bound (R-21901.7) is asserted only on a declared
  zero-avoiding support and imports the standard local minimum-modulus estimate.
- The claim is a scope correction for one proposed frame; it does not reject
  the prolate route, prove RH, or disprove RH.
