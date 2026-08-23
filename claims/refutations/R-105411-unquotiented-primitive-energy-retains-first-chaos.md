# R-105411 — The unquotiented primitive Hodge energy retains a power-sized first chaos

Claim ID: `R-105411`

Status: **PROVED ASYMPTOTIC SEPARATOR / FORWARD CORRECTION**

Depends on: PR #719 `L-102732`, `L-102737`, `L-102741`; PR #730
`L-105404--L-105405`.

Let the centered filtered ray family be

\[
R_w=R_0+2w k_B+w^2k_A,
\qquad w\in\mathbb R,
\]

with

\[
\widehat k(1/2)=\int_0^\infty k(y)y^{-1/2}\frac{dy}{y}.
\]

PR #719 proves

\[
\widehat R_w(1/2)=M_0+2\kappa_0w,
\qquad
\kappa_0=4\log2\,(3-2\sqrt2)>0.
\]

Therefore

\[
\boxed{
\widehat{k_A}(1/2)=0,
\qquad
\widehat{k_B}(1/2)=\kappa_0.
}
\tag{R-105411.1}
\]

Put

\[
L=4A-B,
\qquad
J=A+192B.
\]

The corresponding kernels satisfy

\[
\boxed{
\widehat{k_L}(1/2)=-\kappa_0,
\qquad
\widehat{k_J}(1/2)=192\kappa_0.
}
\tag{R-105411.2}
\]

For the literal ordinary-prime singleton packet, with fixed orientation
`epsilon=+1` or `epsilon=-1`, the quantitative prime number theorem gives,
uniformly in the completion parameter,

\[
L^{[1]}_\tau(X)
=-\epsilon\kappa_0\frac{\sqrt X}{\log X}
+O\!\left(\frac{\sqrt X}{\log^2X}\right),
\]

\[
J^{[1]}_\tau(X)
=192\epsilon\kappa_0\frac{\sqrt X}{\log X}
+O\!\left(\frac{\sqrt X}{\log^2X}\right).
\tag{R-105411.3}
\]

The second labelled copy of `67` is a finite compact-support term and vanishes
from this tail.

The exact Hodge square is

\[
Q=\frac{769}{2}\mathcal H_{\rm prim}
=L^2+\frac{J^2}{48}.
\]

Consequently its isolated first-chaos sector satisfies

\[
\boxed{
Q^{[1]}_\tau(X)
=769\kappa_0^2\frac{X}{\log^2X}
\left(1+O\left(\frac1{\log X}\right)\right).
}
\tag{R-105411.4}
\]

On a unit logarithmic block this is power-sized. Its coefficient diagonal is
only polylogarithmic, so the positive part of the distinct-prime off-diagonal
is power-sized as well. Hence `F1ATO105405`, when read as subpower packing of
the unquotiented positive Hodge trace, is false.

This does not refute the finite Hodge identity or the signed total detector.
It proves that the source-owned first chaos must be moved before an absolute
value, square, radial gauge or regional positive part. PR #719
`L-102741--L-102742` provides the exact Wick quotient; `L-105412` transports it
through the F1 Hodge coordinates.
