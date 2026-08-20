# L-101210 — The fixed ratio-536 detector is an exact three-state function on every unit cell

Claim ID: `L-101210`  
Status: **PROVED EXACT CELL CALCULUS**  
Created: 2026-08-21  
Depends on: PR #665, `L-99824`

Let

\[
G(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}\widetilde K(X/n)
\]

be the fixed zero-safe compact scalar of PR #665. Its kernel is supported on
`[1,536]` and has breakpoints

\[
r=(1,2,4,8,67,134,268,536).
\]

On the seven bands \([r_j,r_{j+1})\), write

\[
\widetilde K(y)=a_j\sqrt y+b_j\log y+c_j.
\]

The exact coefficient table is

\[
\begin{array}{c|c|c|c}
[r_j,r_{j+1})&a_j&b_j&c_j\\ \hline
[1,2)&8&-3&-8\\
[2,4)&0&3(\sqrt2-1)&8(\sqrt2-1)-3\sqrt2\log2\\
[4,8)&-4&3\sqrt2&8\sqrt2-6\log2-3\sqrt2\log2\\
[8,67)&0&0&6(\sqrt2-1)\log2\\
[67,134)&-8/\sqrt{67}&3&8+6(\sqrt2-1)\log2-3\log67\\
[134,268)&0&3(1-\sqrt2)&8(1-\sqrt2)+(9\sqrt2-6)\log2+3(\sqrt2-1)\log67\\
[268,536)&4/\sqrt{67}&-3\sqrt2&\sqrt2(-8+3\log536).
\end{array}
\tag{L-101210.1}
\]

Fix an integer `N>=1` and define

\[
I_j(N)=\left\{n:\left\lfloor\frac N{r_{j+1}}\right\rfloor<n\le
\left\lfloor\frac N{r_j}\right\rfloor\right\}.
\]

For every `X in (N,N+1)`, these seven integer sets are constant. Put

\[
A_N=\sum_j a_j\sum_{n\in I_j(N)}\frac{\beta(n)}n,
\]

\[
B_N=\sum_j b_j\sum_{n\in I_j(N)}\frac{\beta(n)}{\sqrt n},
\]

\[
C_N=\sum_j\sum_{n\in I_j(N)}
\frac{\beta(n)}{\sqrt n}(c_j-b_j\log n).
\]

Then exactly

\[
\boxed{G(X)=A_N\sqrt X+B_N\log X+C_N\qquad(N<X<N+1).}
\tag{L-101210.2}
\]

Moreover

\[
G'(X)=\frac{A_N}{2\sqrt X}+\frac{B_N}{X}.
\]

Thus each open unit cell has at most one critical point. A critical point can be
an interior minimum only when `A_N>0`, `B_N<0`, and

\[
X_N^*=\left(-\frac{2B_N}{A_N}\right)^2\in(N,N+1).
\]

Consequently the exact cell minimum is obtained from the two endpoint limits
and, only in that case, `G(X_N^*)`. No numerical minimization or hidden
activation subdivision remains.
