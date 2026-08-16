# L-96502 — Every terminal P61 difference has a nonnegative realization in rows two and three

Claim ID: `L-96502`  
Status: **PROPOSED COMPLETE SPECIALIZATION OF FROZEN DIRECTED AVLT/HALL INPUTS**  
Created: 2026-08-17  
Frozen sources: PR #550 `L-96300` and `L-96301` at
`20646a78c3e8843001cb49ea0c9741f6d0d446f7`

A terminal leaf has

\[
p\ge67,\qquad 1\le y<67,\qquad d\mid P_{61},\qquad\mu(d)\ne0,
\]

and signed row

\[
R_{p,y,d}(j)=
{\mu(d)\over\sqrt d}
\left[Q_{py/d}(j)-p^{-1/2}Q_{y/d}(j)\right].
\tag{L-96502.1}
\]

The frozen directed Target–Lorenz theorem supplies a lower-triangular Hall
transport from negative-demand colors to positive-supply colors. If `T_e` and
`T_o` are the positive and negative target masses, `t_{o,e}` the no-upward
flow, and

\[
r_e=T_e-\sum_o t_{o,e}\ge0,
\]

then demand conservation and the target-normalized row profile `rho_j` give

\[
\sum_eT_e\rho_j(e)-\sum_oT_o\rho_j(o)
 =\sum_er_e\rho_j(e)
 +\sum_{o,e}t_{o,e}[\rho_j(e)-\rho_j(o)].
\tag{L-96502.2}
\]

For `e<=o`, the frozen profile theorem gives

\[
\rho_j(e)\ge\rho_j(o)
\]

for every component row, hence in particular for `j=2,3`. Both terms on the
right of (L-96502.2) are nonnegative. The first is residual target-bearing
source; the second is a target-null current-only Hall row bonus. It is not a
new source and is not recursively copied.

For `67<=p<=191`, the finite head inequalities are exact. For `p>=193`, the
frozen 256-bit MPFR producer uses directed `RNDD/RNDU` square-root and logarithm
endpoints and verifies the complete tail. The two domains overlap at their
boundary, so all `p>=67` are covered.

The same directed certificate proves that the residual outer native row is
nonnegative on every real endpoint cell `1<=x<67`; its smallest frozen strict
lower bound is positive at endpoint 67, row 66.

Therefore every canonical current leaf and every outer leaf in the finite
stopping line has a positive physical realization whose rows two and three
match its signed marginal. Applying ordinary `q` and ordinary `4q` to the same
realization before differencing preserves the identity, although the present
consumer needs only the component rows.
