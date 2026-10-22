# L-91416 — Pointwise cutoff-minor positivity

Status: **PROVED EXACT**. RH remains unproved.

For cutoff `c>y`, define
\[
M_{j,c}(d)=K_R^{(j)}(d)K_S(c)-K_S(d)K_R^{(j)}(c).
\]
If `d<=y`, `L-91410` gives
\[
K_R^{(j)}(d)/K_S(d)\ge\phi_j(p)
\ge K_R^{(j)}(c)/K_S(c).
\]
If `y<d<c`, both ratios are outer and outer monotonicity gives the same inequality. Hence
\[
\boxed{M_{j,c}(d)\ge0\quad(d<c).}
\]
The prefix determinant from `L-91415` is
\[
\Pi_{j,c}=
\sum_{d<c,\ d\mid P_{61}}\mu(d)M_{j,c}(d).
\]
Thus every individual minor has the correct sign. The remaining issue is only the finite even/odd cancellation of this positive kernel.
