# L-99300 — Positive Mellin witnesses only need holomorphic fixed-row error

Claim ID: `L-99300`  
Status: **PROVED ANALYTIC TRANSFER THEOREM**  
Created: 2026-08-19  
RH status: not assumed

Fix `j>=2`. Suppose the canonical component row has Mellin transform on its initial half-plane

\[
\mathcal C_j(s)=\frac{A_j}{s^2}+\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
\]

Assume that for every hypothetical zero `rho` of `zeta` with `Re rho>1/2`, there exists a sufficiently large fixed `j` for which `P_j(rho) != 0`. Let `D_X(j)>=0` and put `E_X(j)=c_X(j)-D_X(j)`.

Assume

\[
\int_1^\infty |E_X(j)|X^{-\sigma-1}\,dX<\infty
\]

for every `sigma>0`. Then

\[
\mathcal E_j(s)=\int_1^\infty E_X(j)X^{-s-1}\,dX
\]

is holomorphic throughout `Re s>0` by locally uniform dominated convergence. Consequently

\[
\mathcal D_j(s)=\mathcal C_j(s)-\mathcal E_j(s)
\]

has exactly the same nonreal poles in `Re s>0` as `\mathcal C_j`, except at points where `P_j` vanishes.

Now suppose `rho=1/2+delta+i gamma`, `delta>0`, is a zeta zero and choose fixed `j` with `P_j(rho)!=0`. Then `\mathcal D_j` has a nonreal pole at

\[
s_0=rho-1/2=delta+i gamma.
\]

Because `D_X(j)>=0`, Landau's theorem for Mellin/Laplace transforms of eventually nonnegative functions forces a singularity at the real abscissa of convergence whenever that abscissa is finite. The displayed continuation of `\mathcal D_j` is holomorphic on the positive real axis: `zeta(s+1/2)` has no zeros for real `s>0`, and the remaining terms are holomorphic there. This is incompatible with the nonreal pole at `s_0`.

Thus a nonnegative fixed-row surrogate modulo a Mellin-holomorphic error class is sufficient for the fixed-row Landau consumer. Exact equality `D_X(j)=c_X(j)`, global score closure, ordinary/detail capacity closure and positivity of each Volterra boundary coefficient are not needed by this transfer theorem.
