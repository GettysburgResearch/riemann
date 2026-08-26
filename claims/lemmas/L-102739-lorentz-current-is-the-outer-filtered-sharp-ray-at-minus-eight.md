# L-102739 — The filtered Lorentz current is the outer SHARP ray at \(w=-8\)

Claim ID: `L-102739`  
Status: **PROVED EXACT EXTREMAL-COORDINATE THEOREM**  
Created: 2026-08-22  
Depends on: `L-102728`, `L-102731`, `L-102738`  
RH status: **not assumed**

Let

\[
P(w)=C+2Bw+Aw^2
\]

be the real restriction of the filtered SHARP disk polynomial, with

\[
P_-=P(-1/2),
\qquad
P_0=P(0),
\qquad
P_+=P(1/2).
\]

For the filtered activation/current coordinates of PR #719,

\[
A=P_2a_\tau,
\qquad
B=G_\tau-A.
\]

Therefore the conclusion-facing Lorentz coordinate is

\[
5P_2a_\tau-G_\tau=4A-B.
\tag{L-102739.1}
\]

## 1. Outer-ray identity

Evaluation at the fixed outer point `w=-8` gives

\[
P(-8)=C-16B+64A.
\]

Hence

\[
\boxed{
4A-B=\frac{P(-8)-P(0)}{16}.
}
\tag{L-102739.2}
\]

Thus the final filtered Lorentz current is not an unknown matrix coordinate.
It is the increment from the center of the filtered SHARP disk to one fixed
outer ray.

## 2. Exact three-ray extrapolation

Quadratic interpolation from the three positive inner rays gives

\[
\boxed{
P(-8)=136P_-+120P_+-255P_0.
}
\tag{L-102739.3}
\]

Subtracting `P_0` and dividing by `16` recovers

\[
\boxed{
4A-B
=
\frac{17}{2}P_-+rac{15}{2}P_+-16P_0,
}
\tag{L-102739.4}
\]

which is exactly the barycentric formula of `L-102728`.

The constants `136`, `120`, and `255` are therefore not bookkeeping
artifacts.  They are the exact degree-two Lagrange extrapolation coefficients
from `{-1/2,0,1/2}` to `-8`.

## 3. The radial gauge contains the sharp outer ray

In the dual of `L-102738`, choose

\[
Z_*
=
\begin{pmatrix}
4&-1/2\\
-1/2&1/16
\end{pmatrix}
=
\begin{pmatrix}2\\-1/4\end{pmatrix}
\begin{pmatrix}2&-1/4\end{pmatrix}.
\]

It is feasible and saturates both upper constraints.  The corresponding dual
functional is

\[
-4A+B=-(4A-B).
\]

Equivalently, it is the rank-one ray `t=-8`, `theta=1/16` in
(L-102738.6).  Therefore

\[
\boxed{
(4A-B)_-\le\mathfrak R(A,B,C).
}
\tag{L-102739.5}
\]

This gives the exact extremal explanation for the radial-gauge constants

\[
\frac{255}{64},
\qquad
\frac1{16}.
\]

## 4. Source and carrier scope

All three inner rays and the outer increment have the same affine physical
carrier.  Equation (L-102739.2) removes that carrier before any absolute value.
After the exact source-region and owner recombination of PR #719, the remaining
arithmetic theorem can be stated in the equivalent outer-ray form

```text
OER102780:
  the carrier-recombined outer-ray increment
  [P(-8)-P(0)]/16 has subpower logarithmic negative mass.
```

`OER102780`, `TRF102750`, and the Lorentz part of `OERSC102770` are the same
fixed scalar in three exact coordinate systems.  This theorem creates no new
RH assumption; it removes the last matrix-coordinate ambiguity.