# L-98701 — The Tao semigroup port has an atomwise phase-ready Gram decomposition

Claim ID: `L-98701`  
Status: **PROVED EXACT ARITHMETIC THEOREM**  
Created: 2026-08-18  
Depends on: `T-98300`  
RH status: **not assumed**

For a finite prime set `P`, let `S_P` be its multiplicative semigroup and put

\[
A_P(x)=\sum_{\substack{n\le x\\n\in S_P}}\frac{\mu(n)}n,
\quad
N_P(x)=\#(S_P\cap[1,x]),
\quad
H_P(x)=\sum_{\substack{n\le x\\n\in S_P}}\frac1n.
\]

Let `N_(P^c)(x)` count integers at most `x` having no prime factor in `P`. The Tao completion matrix is

\[
K_P(x)=
\begin{pmatrix}C_P(x)&A_P(x)\\A_P(x)&C_P(x)\end{pmatrix},
\qquad
C_P(x)=\frac{N_P(x)+N_{P^c}(x)-H_P(x)}x.
\]

The following source decomposition is exact. For every complementary-semigroup integer `m<=x`, add the rank-one plus-channel atom

\[
\frac1x\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

For every `n in S_P`, add the diagonal atom

\[
\frac{1-1/n}{x}I_2.
\]

If `n` is squarefree, also add the trace-free atom

\[
\frac{\mu(n)\{x/n\}}x
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Because `x,n` are integers,

\[
0\le\{x/n\}\le1-1/n,
\]

so the sum of the diagonal and trace-free atoms at `n` is positive semidefinite. The off-diagonal sum is exactly `A_P(x)` by restricted Möbius inversion, and the diagonal sum is exactly `C_P(x)`.

This realizes every local port as a common labelled Gram before Stieltjes integration. It is stronger than an a posteriori square root of `K_P`: the labels survive prime adjoining and are suitable for a cross-scale Fock direct limit.
