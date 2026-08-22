# L-102502 — Exact CV/XD channel Gram and a strict shell reserve

Claim ID: `L-102502`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
Depends on: `L-102500--L-102501`  
RH status: **not assumed**

Let `F` be either the labelled lift in
`L^2(R x T^L)` or its real physical collapse at `vartheta=0`. Define

\[
C=\partial_uF,\qquad
X=\frac12(\partial_u+\tfrac32)F.
\tag{L-102502.1}
\]

These are the common-smoothed critical-variation channel and corrected
same-`K1` cross-dispersion channel.

## 1. Exact orthogonality

For the labelled lift, torus characters are orthogonal and each mother
translate is real and compactly supported. For the physical collapse the whole
field is real and compactly supported. In both cases

\[
\boxed{\langle \partial_uF,F\rangle=0.}
\tag{L-102502.2}
\]

Consequently

\[
\boxed{\langle C,X\rangle=\frac12\|C\|^2,}
\tag{L-102502.3}
\]

\[
\boxed{\|X\|^2=\frac14\|C\|^2+\frac9{16}\|F\|^2.}
\tag{L-102502.4}
\]

Thus

\[
\boxed{
\det
\begin{pmatrix}
\|C\|^2&\langle C,X\rangle\\
\langle C,X\rangle&\|X\|^2
\end{pmatrix}
=\frac9{16}\|C\|^2\|F\|^2.
}
\tag{L-102502.5}
\]

This is the desired Pick-order-three-type determinant reserve, obtained here
as an elementary consequence of the common mother.

## 2. Source-shell localization

Suppose every labelled source product in `F` satisfies

\[
e^a\le n<e^{a+\delta}.
\]

Because `Phi_*` is supported in `[1,16]`, the field is supported in an interval
of logarithmic length

\[
L_\delta=\delta+\log16.
\]

It vanishes at both endpoints. The Dirichlet Poincare inequality gives

\[
\|F\|^2\le\frac{L_\delta^2}{\pi^2}\|C\|^2.
\tag{L-102502.6}
\]

Hence

\[
\boxed{
\|X\|^2\le\kappa_\delta\|C\|^2,
\qquad
\kappa_\delta=\frac14+\frac{9L_\delta^2}{16\pi^2}.
}
\tag{L-102502.7}
\]

For a one-octave source shell, `delta<=log 2`, so

\[
\boxed{
\kappa_\delta\le
\frac14+\frac{225(\log2)^2}{16\pi^2}
=0.9345634570\ldots<1.
}
\tag{L-102502.8}
\]

Thus the same-`K1` channel is a strict energy contraction of the common
smoothed-CV channel on every carrier-recombined one-octave source shell.

The determinant also satisfies

\[
\boxed{
\det G(C,X)\ge
\frac{9\pi^2}{16L_\delta^2}\|F\|^4.
}
\tag{L-102502.9}
\]

## Scope firewall

The theorem does not permit taking norms of arbitrary short/long regions before
their deterministic carriers are recombined. It applies after an exact
source-owned shell and carrier quotient have been formed.
