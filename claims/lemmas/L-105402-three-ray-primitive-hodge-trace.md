# L-105402 — The three filtered SHARP rays are one exact primitive Hodge trace

Claim ID: `L-105402`  
Status: **PROVED EXACT PRIMITIVE REALIZATION AND OPTIMAL TRACE INEQUALITY**  
Created: 2026-08-23  
Depends on: PR #719 `L-102728`; `L-105401`  
RH status: **not assumed**

Retain the three nonnegative, source-faithful rays of PR #719:

\[
P_-=JP_2Q_{\tau,-3/2},\qquad
P_0=JP_2Q_{\tau,-1},\qquad
P_+=JP_2Q_{\tau,-1/2}.
\]

Write

\[
A=2(P_-+P_+-2P_0),
\qquad
G=A+\frac12(P_+-P_-).
\]

The conclusion-facing current is

\[
L=5A-G
=\frac{17}{2}P_- -16P_0+\frac{15}{2}P_+.
\tag{L-105402.1}
\]

## 1. Primitive toric realization

Use

\[
B^\bullet
=
\mathbb R[y_-,y_0,y_+]/(y_-^2,y_0^2,y_+^2),
\qquad
\omega=y_-+y_0+y_+.
\]

Define

\[
c=\frac{17}{2}y_- -16y_0+\frac{15}{2}y_+,
\qquad
\beta=P_-y_-+P_0y_0+P_+y_+.
\]

The coefficients of \(c\) sum to zero, so \(c\) is primitive. Direct
intersection gives

\[
\boxed{
\deg(c\beta\omega)=-L.
}
\tag{L-105402.2}
\]

Thus the physical Lorentz current is literally a mixed intersection of one
fixed primitive class with the source-valued ray divisor.

## 2. Exact primitive energy

Put

\[
\bar P=\frac{P_-+P_0+P_+}{3},
\qquad
\beta^\circ=\sum_{\sigma\in\{-,0,+\}}
(P_\sigma-\bar P)y_\sigma.
\]

Then

\[
\boxed{
-\deg((\beta^\circ)^2\omega)
=
\sum_\sigma(P_\sigma-\bar P)^2
=
\frac13\sum_{\sigma<\sigma'}
(P_\sigma-P_{\sigma'})^2.
}
\tag{L-105402.3}
\]

Using the exact reconstruction formulas,

\[
\boxed{
\mathcal H(A,G)
:=
-\deg((\beta^\circ)^2\omega)
=
\frac{49A^2-96AG+48G^2}{24}.
}
\tag{L-105402.4}
\]

The matrix is positive definite; its determinant is \(1/12\).

## 3. Optimal Hodge trace inequality

The primitive norm of \(c\) is

\[
-\deg(c^2\omega)
=
\left(\frac{17}{2}\right)^2+16^2+
\left(\frac{15}{2}\right)^2
=
\frac{769}{2}.
\]

Therefore Hodge–Cauchy gives

\[
\boxed{
|5A-G|^2
\le
\frac{769}{2}\,\mathcal H(A,G).
}
\tag{L-105402.5}
\]

The constant is optimal. More precisely,

\[
\boxed{
\frac{769}{2}\mathcal H(A,G)-(5A-G)^2
=
\frac{(191A-192G)^2}{48}.
}
\tag{L-105402.6}
\]

The second primitive coordinate is

\[
191A-192G=94P_-+4P_0-98P_+,
\]

whose coefficients also sum to zero.

## 4. Root-free character

Every pairwise ray difference cancels the common deterministic carrier before
squaring:

\[
P_--P_0=\frac54A-G,
\]

\[
P_+-P_0=G-\frac34A,
\]

\[
P_+-P_-=2(G-A).
\]

Hence \(\mathcal H\) is a sum of three carrier-free, same-source squares. It is
not a root-containing positive square.

## Consequence

If

\[
\int_T^{T+1}\int_0^1
\sqrt{\mathcal H(A_{\tau},G_{\tau})}\,d\tau\,dT
=
e^{o(T)},
\tag{F1PE105403}
\]

then the centered three-ray fluctuation has subpower logarithmic negative mass.
Through PR #719's exact composition, this implies the fixed-detector criterion
and RH.

The implication is proved here; `F1PE105403` is not proved here.
