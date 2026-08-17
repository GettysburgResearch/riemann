# L-97243 - The 5:3 scalar has an exact parity-covariant positive Julia lift

Claim ID: `L-97243`  
Status: **PROVED EXACT MATRIX THEOREM**  
Created: 2026-08-17  
Inputs: exact scalar dictionary `L-97240`; dyadic Julia state of PR #562  
RH status: **not assumed**

Let
\[
g_2(n)=v_2(n)+1,
\qquad
h_*(n)=6g_2(n)+3\mathbf1_{2\mid n}g_2(n/2),
\]
and define
\[
\mathcal J_*(n)=
\begin{pmatrix}h_*(n)&a_*(n)\\a_*(n)&h_*(n)\end{pmatrix}.
\]
For every odd squarefree core `d>1`, the four nonzero dyadic levels satisfy
\[
\begin{array}{c|rrrr}
n&d&2d&4d&8d\\\hline
|a_*(n)|&6&15&12&3\\
h_*(n)&6&15&24&33.
\end{array}
\]
All other nonunit arithmetic cases have `a_*(n)=0`; the unit core is checked
separately. Hence
\[
\boxed{h_*(n)\ge|a_*(n)|,\qquad \mathcal J_*(n)\succeq0.}
\tag{L-97243.1}
\]

Put `D=diag(1,-1)`. For a rough history `h`,
\[
\boxed{D^{|h|}\mathcal J_*(n)D^{|h|}\succeq0}
\tag{L-97243.2}
\]
and its off-diagonal entry is `(-1)^{|h|}a_*(n)`. Thus cumulative parity is
implemented by positive conjugation rather than erased at terminalization.
