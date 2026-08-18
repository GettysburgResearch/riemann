# R-98020 — Bounded-remainder Dickman domination stops at the critical saddle

Claim ID: `R-98020`  
Status: **PROVED METHODOLOGICAL NO-GO AT THE DECLARED INPUT SCOPE**  
Created: 2026-08-18  
Depends on: `L-98021`  
RH status: **unproved**

The proof of `L-98021` uses only two quantitative facts about the nonhomogeneous
`P_61` source:

1. `b(Y)-a_*sqrt(Y)` is bounded;
2. the unsigned rough count has size `O(Y/log z)`.

At that scope the resulting uncertainty is

\[
O\!\left(\frac{\sqrt Y}{\log z}\right).
\tag{R-98020.1}
\]

Let

\[
u=c\frac{\log\log Y}{\log\log\log Y}
\]

with fixed `c>1`. De Bruijn's asymptotic gives

\[
\rho(u)=(\log Y)^{-c+o(1)},
\tag{R-98020.2}
\]

whereas

\[
\frac1{\log z}
=\frac{u}{\log Y}
=(\log Y)^{-1+o(1)}.
\tag{R-98020.3}
\]

Thus

\[
\rho(u)=o(1/\log z)
\qquad(c>1).
\tag{R-98020.4}
\]

Therefore no argument that replaces the bounded source remainder by the
unsigned estimate (R-98020.1) can decide the sign beyond the critical saddle.
A continuation must exploit the actual Möbius correlation of

\[
\sum_m\frac{\mu(m)}{\sqrt m}e(Y/m),
\]

not merely its absolute size.

This is a mechanism no-go, not a counterexample to the native scalar. It shows
that `L-98021` reaches the natural endpoint of the homogeneous-Dickman plus
absolute-remainder method.
