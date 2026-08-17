# T-96500 - The global parity-Hall producer reduces the corrected full-recursion route to two rows and RH

Claim ID: `T-96500`
Status: **PROVED CONDITIONAL REDUCTION; GLOBAL PRODUCER OPEN**
Created: 2026-08-17
Depends on: `L-96500--L-96503`, `R-96500--R-96501`, the fixed-row Mellin transform, rows-2/3 noncancellation
RH status: **unproved**

Let `GPHT23` denote the statement that, after fully expanding the finite
rough-prime source at every sufficiently large endpoint and incorporating the
cumulative parity of every history, the exact common-source system
`L-96503.1--2` is feasible with `K=R_+^2` for rows two and three.

By `L-96501`, the expansion preserves every row activation and coefficient
magnitude. By `L-96500`, the parity-correct atom classes give the exact root
marginal. Applying `L-96503` once globally gives

\[
c_X(2)\ge0,\qquad c_X(3)\ge0
\]

for every sufficiently large `X`.

For fixed row `r`, the exact Mellin transform is

\[
\int_1^\infty c_X(r)X^{-s-1}\,dX
=\frac{C_r}{s^2}+
\frac{P_r(s+1/2)}{s^2\zeta(s+1/2)}.
\]

For `x=2^{-z}`, `y=3^{-z}`,

\[
P_2=2x-1-y,
\qquad
3P_3=5y-x-1-3x^2.
\]

Simultaneous vanishing implies

\[
-3(x-1)(x-2)=0,
\]

impossible for `0<Re z<1` because `1/2<|x|<1`. Landau's theorem for a
nonnegative Mellin density excludes every zeta zero with real part greater than
one half; the functional equation gives RH.

Thus

\[
\boxed{\mathrm{GPHT}_{2,3}\Longrightarrow\mathrm{RH}.}
\]

`GPHT23` is not proved here. The leafwise producer of PR #550 is invalid by
`R-96500`, and the fixed-depth two-level repair is false by `R-96501`. The
remaining producer is necessarily global, variable-depth, or non-scalar.
