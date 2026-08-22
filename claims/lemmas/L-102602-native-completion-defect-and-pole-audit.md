# L-102602 — The native-completion defect is the sole detector-bearing residue

Claim ID: `L-102602`  
Status: **PROVED EXACT MELLIN AND SOURCE REDUCTION**  
Created: 2026-08-22  
Depends on: PR #715 `L-102504--L-102505`; `L-102600`  
RH status: **unproved**

Let \(z=s+\tfrac12\).  The duplicate-\(67\) native Euler source has Dirichlet
multiplier

\[
\boxed{
B_{\rm nat}(z)
=
\frac{1-67^{-z}}{\zeta(z)}.
}
\tag{L-102602.1}
\]

Complete every labelled Euler factor by its positive partner.  The resulting
squared source has multiplier

\[
\boxed{
B_{\rm sq}(z)
=
\frac{1-67^{-2z}}{\zeta(2z)}.
}
\tag{L-102602.2}
\]

The extra labelled \(67\) is essential: its two factors combine to
\(1-67^{-2z}\).

Define the completion defect

\[
B_{\rm def}(z)=B_{\rm nat}(z)-B_{\rm sq}(z).
\]

For the fixed common mother of PR #715, put

\[
H_{\rm nat}(X)
=
\sum_n\frac{\beta(n)}{\sqrt n}\Phi_*(X/n),
\]

and let \(H_{\rm sq}\) and \(H_{\rm def}=H_{\rm nat}-H_{\rm sq}\) denote the
corresponding squared and defect fields.  Then

\[
\boxed{
\mathcal M H_{\rm def}(s)
=
m_\Phi(s)
\left[
\frac{1-67^{-z}}{\zeta(z)}
-
\frac{1-67^{-2z}}{\zeta(2z)}
\right].
}
\tag{L-102602.3}
\]

## 1. Pole audit

When \(\Re s>0\), one has \(\Re(2z)>1\).  Hence the squared term is holomorphic
throughout the complete Landau half-plane.  Every hypothetical zeta zero

\[
\rho,\qquad \Re\rho>\frac12,
\]

produces the same pole at \(s=\rho-\tfrac12\) in \(H_{\rm def}\) as in
\(H_{\rm nat}\).  The squared completion cancels none of those poles.

Thus all detector-bearing difficulty is concentrated in the completion defect.

## 2. Polylogarithmic squared component

On the horizon \(1\le X\le Y\), only squared shifts \(p^2\le16Y\) can meet the
support of \(\Phi_*\).  Applying PR #715 `L-102505` with
\(Z=4\sqrt Y\) gives

\[
\|H_{\rm sq}\|_{L^2(dX/X)}
\ll
\log(2Y).
\]

Consequently

\[
\int_1^Y|H_{\rm sq}(X)|\frac{dX}{X}
\ll
(\log(2Y))^{3/2}.
\tag{L-102602.4}
\]

Because \(x\mapsto x_-\) is one-Lipschitz,

\[
\boxed{
\left|
\int_1^Y(H_{\rm nat})_-\frac{dX}{X}
-
\int_1^Y(H_{\rm def})_-\frac{dX}{X}
\right|
\ll
(\log(2Y))^{3/2}.
}
\tag{L-102602.5}
\]

Therefore the native and defect negative-mass criteria are equivalent at
subpower scale.

## Boundary

Completion has not proved RH.  It has separated an analytically harmless,
polylogarithmic squared component from one fixed defect carrying every possible
off-line pole.
