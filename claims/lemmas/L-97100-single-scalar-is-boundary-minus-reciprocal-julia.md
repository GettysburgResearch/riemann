# L-97100 — The unique 5:3 scalar is exactly a boundary term minus one reciprocal-Julia channel

Claim ID: `L-97100`  
Status: **PROVED EXACT DIRICHLET AND FINITE-COEFFICIENT IDENTITY**  
Created: 2026-08-17  
Depends on: the unique scalar algebra of PR #551/#557  
RH status: **not assumed**

Put
\[
G_\diamond(z)=
\frac{\zeta(z)}{(1-2^{-z})(1-2^{-z-1})},
\qquad
B_\diamond(z)=\frac1{G_\diamond(z)}.
\tag{L-97100.1}
\]
Write
\[
G_\diamond(z)=\sum_{n\ge1}\frac{g_\diamond(n)}{n^z},
\qquad
B_\diamond(z)=\sum_{n\ge1}\frac{b_\diamond(n)}{n^z}.
\]

For the unique scalar
\[
\mathcal R_X=5c_X(2)+3c_X(3),
\]
PR #551 gives, with `z=s+1/2`,
\[
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac6{s^2}
-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
\]
Since `2-2^(-z)=2(1-2^(-z-1))`,
\[
\boxed{
\int_1^\infty \mathcal R_X X^{-s-1}\,dX
=
\frac{6(1-B_\diamond(z))}{s^2}.
}
\tag{L-97100.2}
\]

Let `a_*(n)` be the scalar coefficient dictionary. Coefficient comparison gives
\[
\boxed{a_*=6(\delta_1-b_\diamond).}
\tag{L-97100.3}
\]
The dyadic local factor of `B_diamond` is
\[
(1-x)^2(1-x/2)=1-\frac52x+2x^2-\frac12x^3,
\qquad x=2^{-z}.
\]
Thus for odd squarefree `m`,
\[
\boxed{
\begin{array}{c|rrrr}
e&0&1&2&3\\ \hline
b_\diamond(2^em)/\mu(m)&1&-5/2&2&-1/2,
\end{array}}
\tag{L-97100.4}
\]
and all higher dyadic fibres vanish. Equation (L-97100.3) is exactly the PR #557 packet
\[
\mu(m)(-6,15,-12,3)
\]
for every nonunit odd squarefree core, with the already-recorded unit-core correction.

The scalar is therefore not an arbitrary combination of rows: it is six times the boundary defect of one normalized reciprocal Dirichlet state.
