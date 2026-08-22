# L-102728 — Three filtered SHARP rays reconstruct the compact activation/current coordinates

Claim ID: `L-102728`  
Status: **PROVED EXACT FILTERED COORDINATE THEOREM**  
Created: 2026-08-22  
Depends on: `L-102725--L-102727`  
RH status: **not assumed**

Add the third fixed shift

\[
z_-=-\frac32.
\]

It belongs to the audited SHARP disk.

## 1. Positive filtered carrier and prime budget

Writing `x=sqrt(y)`, its filtered carrier is

\[
K_{-3/2}(y)=
\begin{cases}
(8x-9)^2/4,&1\le y<2,\\
-[32\sqrt2x^2-144\sqrt2x+81(1+\sqrt2)]/4,&2\le y<4,\\
[16x^2-72x+81\sqrt2]/4,&4\le y<8,\\
2(2-\sqrt2)x^2,&y\ge8,\\
0,&0<y<1.
\end{cases}
\tag{L-102728.1}
\]

The middle-cell derivatives have their unique extrema at `x=9/4`; endpoint
values are strictly positive. Hence `K_-3/2(y)>=0`.

The same finite-cell/analytic-tail method as `L-102726` gives

\[
\boxed{
\sup_y\mathfrak b_{-3/2}(y)<0.920011.
}
\tag{L-102728.2}
\]

The retained certificate checks `633` cells and `6` interior stationary
points; the maximum occurs at the boundary `y=8`.

Therefore

\[
P_2Q_{\tau,-3/2}\ge0,
\qquad
JP_2Q_{\tau,-3/2}\ge0.
\tag{L-102728.3}
\]

## 2. Three positive ray coordinates

Put

\[
P_-:=JP_2Q_{\tau,-3/2},
\qquad
P_0:=JP_2Q_{\tau,-1},
\qquad
P_+:=JP_2Q_{\tau,-1/2}.
\]

All three are nonnegative. Write

\[
A=P_2a_\tau,
\qquad
G=G_\tau,
\qquad
Q=P_2Q_\tau.
\]

Using `L-102727.5`,

\[
P_-=Q-6G+\frac54A,
\]

\[
P_0=Q-5G,
\]

\[
P_+=Q-4G-\frac34A.
\tag{L-102728.4}
\]

These three values reconstruct the filtered coordinates exactly:

\[
\boxed{
A=2(P_-+P_+-2P_0),
}
\tag{L-102728.5}
\]

\[
\boxed{
G=A+\frac12(P_+-P_-),
}
\tag{L-102728.6}
\]

and `Q=P_0+5G`.

In particular the conclusion-facing Lorentz coordinate is

\[
\boxed{
5A-G
=\frac{17}{2}P_-+\frac{15}{2}P_+-16P_0.
}
\tag{L-102728.7}
\]

Thus the signed compact current is no longer hidden inside an unknown matrix:
it is one explicit barycentric combination of three nonnegative,
source-faithful filtered SHARP rays.

## 3. Exact remaining cancellation

Equation (L-102728.7) shows that the sole adverse coefficient is the center ray
`P_0`. The three rays have the same linear `X` carrier, and the coefficients in
(L-102728.7) sum to zero. Therefore that deterministic carrier cancels only in
the complete barycentric combination.

Taking an absolute value of `P_0` or estimating it before recombination would
reintroduce a power-sized term. The remaining theorem is a carrier-preserving
control of the centered three-ray fluctuation, not a fourth source identity.