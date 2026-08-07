# L-21901 — All-grid differential cardinals eliminate the finite-projection tail exactly

Claim ID: `L-21901`  
Title: The smooth all-grid Mellin cardinal is the correct complete-frame replacement for finite Xi-polynomial interpolation  
Status: **PROPOSED — COMPLETE ALGEBRAIC AND ZERO-SIDE BRIDGE; COFINAL PROFILE LMI SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15631`; `L-19820`; `L-21504`; `L-21505`; `L-21506`; the centered CCM basis adapter  
Scope: exact source-frame interface for the whole-matrix and prolate positive routes

## 1. Smooth differential cardinal

Fix a period length `L` and frequencies

\[
\omega_k=\frac{2\pi k}{L}.
\]

Let

\[
\chi_L=L^{-1}{\bf1}_{[-L/2,L/2]}*\eta,
\qquad
\eta\in C_c^\infty,
\quad
\int\eta=1,
\]

and define

\[
q_{k,L}(t)
=
\frac{(\partial_t+1/2)
      [\chi_L(t)e^{i\omega_kt}]}
     {i\omega_k+1/2}.
\tag{L-21901.1}
\]

Then

\[
\boxed{
\widehat q_{k,L}(\omega_j)=\delta_{kj}
\quad(j\in\mathbb Z),
\qquad
\widehat q_{k,L}(i/2)=0.
}
\tag{L-21901.2}
\]

The first identity holds on the **entire** Fourier lattice, not merely on a
finite retained set.

Let `f_(k,L)` be the corresponding even multiplicative source.  It is smooth,
vanishes at zero, and has integral zero.  Its arithmetic image

\[
h_{k,L}(t)=E(f_{k,L})(e^t)
\]

is logarithmically Schwartz by `L-21504`.

## 2. Exact periodized image

The arithmetic Mellin multiplier gives

\[
\widehat h_{k,L}(\omega_j)
=
\zeta(1/2-i\omega_j)\delta_{kj}.
\tag{L-21901.3}
\]

Consequently the complete periodization has exactly one Fourier mode:

\[
\boxed{
\Sigma_Lh_{k,L}
=
\zeta(1/2-i\omega_k)e_k.
}
\tag{L-21901.4}
\]

For every finite cutoff `N`, therefore,

\[
\boxed{
(I-\Pi_N)\Sigma_Lh_{k,L}=0
\qquad(|k|\le N).
}
\tag{L-21901.5}
\]

Thus the high-Fourier term isolated in `R-21901` is identically absent.

## 3. Complete raw frame

Let

\[
Z_L=
\operatorname{diag}
\left(
 \zeta(1/2-i\omega_k)
ight)_{|k|\le N}.
\]

In raw source coordinates, the projected periodized map is exactly `Z_L`.
At any support for which no selected diagonal entry vanishes, the source map

\[
F_{L,N}=\operatorname{span}\{f_{k,L}:|k|\le N\}
\longrightarrow E_N(L)
\]

is an isomorphism, and its inverse is the diagonal congruence `Z_L^-1`.
No generic-density argument, fitted source solve, or finite Vandermonde inverse
is needed.

The zero-avoidance theorem `L-21506` permits the support average to be performed
on the raw columns first and the diagonal inverse to be applied only after a
support has been selected.  Relative Loewner inequalities are then transferred
without condition-number loss:

\[
A_{\rm Fourier}=Z_L^{-*}A_{\rm raw}Z_L^{-1},
\qquad
D_{\rm Fourier}=Z_L^{-*}D_{\rm raw}Z_L^{-1}.
\tag{L-21901.6}
\]

## 4. Exact corrected tail

Because (L-21901.5) removes the projection term, the corrected tail is simply

\[
\boxed{
W_{k,L}
=(I-P_L)h_{k,L}
-
\iota_L\mathfrak F_L(I-P_L)h_{k,L}.
}
\tag{L-21901.7}
\]

Every fold converges in `C^infinity` and in the zero-side form domain by
`L-21504/L-21505`.  For coefficient vectors `c,d`, one has the exact identity

\[
\boxed{
Q_W(y_c,y_d)=Q_W(W_c,W_d),
}
\tag{L-21901.8}
\]

where

\[
y_c=\sum_{|k|\le N}c_k
 \zeta(1/2-i\omega_k)e_k.
\]

Thus the complete finite CCM/Weil matrix is represented by one genuine
alias-corrected tail, with no missing Fourier sector.

## 5. What this closes

The all-grid cardinal frame closes the following former ambiguities:

1. algebraic surjectivity of the finite source map;
2. the distinction between finite interpolation and all-grid periodization;
3. convergence of every periodization fold;
4. the sharp finite-vector zero-side form domain;
5. the order of support averaging and zeta inversion.

The remaining positive theorem is no longer a source-existence statement.  It
is the cofinal matrix estimate for the explicit raw corrected-tail synthesis
`W_(L,N)`.

## 6. Exact remaining LMI

Put

\[
D_{L,N}=W_{L,N}^*W_{L,N}
\]

and let `A_(L,N)^line` be the positive matrix obtained by placing every zero at
its real ordinate.  A whole-matrix resolution follows from one common-metric
package

\[
A_{L,N}^{\rm line}
\succeq
[\log R-C-o(\log R)]D_{L,N}
-o(\log R)\tau_RG,
\tag{L-21901.9}
\]

\[
-\delta_R(D_{L,N}+\tau_RG)
\preceq
A_{L,N}-A_{L,N}^{\rm line}
\preceq
\delta_R(D_{L,N}+\tau_RG),
\tag{L-21901.10}
\]

with

\[
\delta_R=o(\log R),
\qquad
(\delta_R+o(\log R))\tau_R\to0.
\tag{L-21901.11}
\]

All objects in (L-21901.9)--(L-21901.11) are now attached to one explicit source
frame.  Proving those LMIs remains RH-bearing; the present lemma does not assume
them.

## 7. Proof boundary

- The lattice cardinality, exact periodization, absence of the projection tail,
  diagonal source congruence, and corrected-tail identity are exact.
- The exact CCM coordinate normalization still must be bound through the
  centered-basis adapter in a production artifact.
- No complete alias-profile floor, local-Weyl LMI, or horizontal-orbit error is
  proved here.
- This lemma repairs the source interface and does not prove RH.
