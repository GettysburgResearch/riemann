# L-106414 — Superexponential Xi Fourier-tail control

Claim ID: `L-106414`  
Status: **PROVED UNCONDITIONALLY FOR FIXED DERIVATIVE ORDER AND FIXED STRIP HEIGHT**  
Created: 2026-08-24  
Depends on: the classical positive Xi theta kernel  
RH status: **not assumed**

Let

\[
\Xi(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\]

where \(\Phi\) is the classical positive even Xi Fourier density.  For
\(u\ge1\), its theta-series formula gives constants \(C,c>0\) such that

\[
\boxed{
0\le\Phi(u)\le C\exp(Cu-ce^{2u}).
}
\tag{L-106414.1}

Indeed, each theta term is a polynomial in \(n\) and \(e^u\) multiplied by
\(\exp(-\pi n^2e^{2u})\); the \(n=1\) exponential dominates the remaining
summable tail.  Evenness gives the corresponding estimate at \(-\infty\).

For \(L>1\), define

\[
\Xi_L(z)=\int_{-L}^{L}\Phi(u)e^{izu}\,du.
\]

Fix a derivative order \(0\le j\le3\) and a strip height \(H>0\).  Since

\[
\Xi^{(j)}(z)-\Xi_L^{(j)}(z)
=\int_{|u|>L}(iu)^j\Phi(u)e^{izu}\,du,
\]

one has, uniformly for \(|\operatorname{Im}z|\le H\),

\[
\boxed{
\left|\Xi^{(j)}(z)-\Xi_L^{(j)}(z)\right|
\le C_{j,H}\exp(-c_{j,H}e^{2L}).
}
\tag{L-106414.2

For \(L_T=\log T\), this becomes

\[
\boxed{
\sup_{|\operatorname{Im}z|\le H}
\left|\Xi^{(j)}(z)-\Xi_{L_T}^{(j)}(z)\right|
\ll_{A,j,H}T^{-A}
}
\tag{L-106414.3

for every fixed \(A>0\), once \(T\) is sufficiently large.

## Product and source-Gram consequences

Every endpoint product in `L-106400` is bilinear in derivatives of order at
most three.  The full and truncated derivatives are uniformly bounded on a
fixed-height strip by the absolutely convergent Fourier integral.  Therefore

\[
\boxed{
N_\Xi-N_{\Xi_L},\quad
D_\Xi-D_{\Xi_L},\quad
\mathcal T_\Xi-\mathcal T_{\Xi_L}
=O_A(T^{-A})
}
\tag{L-106414.4

uniformly on that strip when \(L=\log T\).

Consequently every predeclared finite Paley--Wiener source Gram of dimension
\(O(T\log T)\), formed by integrating these product errors against unit-norm
source functions on a fixed-height contour, receives total Hilbert--Schmidt or
trace error \(o(1)\), hence \(o(N(T))\).

## Topological firewall

Equation (L-106414.4) is an **additive source/contour estimate**.  It does not
by itself preserve zeros of a companion whose boundary value is arbitrarily
small, and it does not prove equality of the full and truncated all-pass
indices.  The cofinal model-space coverage/lower-frame theorem in `T-106420`
remains load bearing.
