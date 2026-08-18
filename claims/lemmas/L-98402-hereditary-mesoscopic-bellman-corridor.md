# L-98402 — The exact Bellman cone is hereditary in the Vinogradov–Korobov mesoscopic corridor

Claim ID: `L-98402`  
Status: **PROVED UNCONDITIONAL ANALYTIC THEOREM ON CLASSICAL INPUTS**  
Created: 2026-08-18  
Depends on: `L-98401`; classical Dickman/de Bruijn estimates; the classical Vinogradov–Korobov zero-free region  
RH status: **not assumed**

Let

\[
U(Y,z)=\int A_z(Y/x)\,dh(x),
\qquad
L=\log z,
\qquad
\nu=\frac{\log Y}{L}.
\]

The completed annular base has total Stieltjes mass \(a_*>0\) and exponentially
weighted finite variation.  Its continuous profile is

\[
\mathcal C_L(\nu)
=
\int
\rho\!\left(\nu-\frac{\log x}{L}\right)dh(x),
\tag{L-98402.1}
\]

where \(\rho\) is the Dickman function, extended by zero on the negative axis.
The classical ratio estimate and the finite variation give

\[
\mathcal C_L(\nu)
=a_*\rho(\nu)
\left(1+O\!\left(\frac{\log(\nu+2)}L\right)\right).
\tag{L-98402.2}
\]

Vinogradov--Korobov prime-reciprocal discrepancy gives

\[
|U(Y,z)-\mathcal C_L(\nu)|
\le
C\nu
\exp\!\left[-cL^{3/5}(\log L)^{-1/5}\right].
\tag{L-98402.3}
\]

Let \(p\) be the prime immediately below the threshold \(z=p^+\).  The exact
one-prime margin is

\[
\mathfrak D(Y,p)
=U(Y,p^+)-\frac1pU(Y/p,p^+).
\tag{L-98402.4}
\]

The continuous child has Dickman coordinate
\(\nu-\log p/\log p^+=\nu-1+O(1/L)\).  The de Bruijn ratio bound

\[
\frac{\rho(\nu-1)}{\rho(\nu)}
\ll \nu\log(\nu+2)
\tag{L-98402.5}
\]

therefore shows

\[
\frac1p\mathcal C_L\!\left(\nu-\frac{\log p}{L}\right)
=o(\rho(\nu))
\tag{L-98402.6}
\]

whenever \(p\gg\nu\log\nu\).

Put \(R=\log Y\).  There is an absolute \(c_0>0\) such that

\[
\boxed{
\nu\le
c_0R^{3/8}(\log R)^{-3/4}
}
\tag{L-98402.7}
\]

implies both

\[
\nu\log(\nu+2)
\le
c_1L^{3/5}(\log L)^{-1/5}
\]

and \(p\gg\nu\log\nu\).  Indeed
\(L=R/\nu\gg R^{5/8}(\log R)^{3/4}\), while the two sides of the first
inequality have the common critical scale
\(R^{3/8}(\log R)^{1/4}\); a sufficiently small \(c_0\) leaves a strict
margin.

Combining (L-98402.2)--(L-98402.6) yields, uniformly for sufficiently large
\(Y\),

\[
\boxed{
U(Y,p^+)>0,
\qquad
U(Y,p^+)\ge\frac1pU(Y/p,p^+),
}
\tag{L-98402.8}
\]

throughout (L-98402.7).

Thus the corridor is hereditary under the **exact** least-prime Bellman update,
not merely positive state by state.  Any failure must lie in the critical
saddle beyond this corridor.
