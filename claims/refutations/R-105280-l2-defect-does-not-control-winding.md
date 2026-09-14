# R-105280 — Ordinary L2 control does not control companion winding

Claim ID: `R-105280`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24

For \(\varepsilon>0\), put

\[
B_\varepsilon(x)=\frac{x-i\varepsilon}{x+i\varepsilon}.
\]

This is circle-valued on the real line and has winding one on the compactified
line.  Nevertheless

\[
B_\varepsilon(x)-1
=
\frac{-2i\varepsilon}{x+i\varepsilon},
\]

so

\[
\boxed{
\int_{\mathbb R}|B_\varepsilon(x)-1|^2\,dx
=4\pi\varepsilon
\longrightarrow0.
}
\tag{1}
\]

Its half-derivative degree energy cannot vanish:

\[
\boxed{
1=\operatorname{wind}B_\varepsilon
\le\|B_\varepsilon\|_{\dot H^{1/2}}^2.
}
\tag{2}
\]

Thus a zero/pole phase slip approaching the real axis carries one full unit of
topological defect while becoming invisible to ordinary \(L^2\) comparison.

Consequences:

1. source-model trace/HS or ordinary mean-square control cannot by itself prove
   the adjacent all-pass winding estimate;
2. the missing `AHXFER105280` theorem must retain a half derivative, an
   equivalent Carleson/Dirichlet energy, or a source-specific near-line
   repulsion theorem;
3. any argument replacing the half-derivative energy in T-105280 by an
   unweighted \(L^2\) norm is false.
