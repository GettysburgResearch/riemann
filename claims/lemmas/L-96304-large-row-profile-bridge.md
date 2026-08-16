# L-96304 — Growing component rows converge to a positive Volterra transform of the universal density

Claim ID: `L-96304`  
Status: **PROPOSED COMPLETE UNIFORM ASYMPTOTIC — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: the exact canonical row formula; elementary Euler--Maclaurin on compact ratio intervals  
RH status: **not assumed**

Fix `R>1`. Uniformly for `1<=y<=R`,

\[
\boxed{
 j^{3/2}Q_{jy}(j)
 =\phi(y)+O_R(j^{-1}),
}
\tag{L-96304.1}
\]

where

\[
\boxed{
\phi(y)=8\sqrt y-7-\frac32\log y.
}
\tag{L-96304.2}
\]

The proof expands the two edge coefficients to first order and applies one Euler--Maclaurin step to the positive tail:

\[
2\int_1^y t^{-1/2}\log(y/t)\,dt
=8\sqrt y-8-4\log y.
\]

The edge contribution is

\[
1+\frac52\log y+O_R(j^{-1}),
\]

which gives (L-96304.2).

For the full Möbius row, define

\[
\mathscr C(y)
=
\sum_{d\le y}\frac{\mu(d)}{\sqrt d}\phi(y/d).
\tag{L-96304.3}
\]

Then uniformly on compact `y` intervals,

\[
\boxed{
 j^{3/2}c_{jy}(j)
 =\mathscr C(y)+O_R(j^{-1}).
}
\tag{L-96304.4}
\]

Finite Fubini or Mellin comparison gives the exact bridge

\[
\boxed{
\mathscr C(y)
=
\mathscr L(y)
+\frac32\int_1^y\frac{\mathscr L(u)}u\,du.
}
\tag{L-96304.5}
\]

Its Mellin transform is

\[
\boxed{
\int_1^\infty\mathscr C(y)y^{-s-1}\,dy
=
\frac{(2s+1)(2s+3)}
{2s^2(2s-1)\zeta(s+1/2)}.
}
\tag{L-96304.6}
\]

Thus the universal Volterra density is not merely analogous to the fixed-row route: it is the exact growing-row scaling limit after one positive logarithmic integration.
