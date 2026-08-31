# R-107300 — Residue aggregation alone forgets energy even on native rank-one rectangles

Claim ID: `R-107300`  
Status: **PROVED EXACT RANK-ONE COUNTEREXAMPLE**  
Created: 2026-08-30  
RH/GRH status: **not assumed**

The arbitrary-coefficient firewall on PR #765 does not disappear merely by
restricting to rank-one native vectors.

Consider one physical cell and two-by-two rectangular panels.

First take

\[
a=(1,1),\qquad b=(1,1).
\]

Then

\[
\left(\sum_i\overline{a_i}\right)\left(\sum_jb_j\right)=4,
\qquad
\|a\|^2\|b\|^2=4.
\]

Now take

\[
a'=(2,0),\qquad b'=(1,1).
\]

The residue aggregate is still

\[
\left(\sum_i\overline{a_i'}\right)\left(\sum_jb_j'\right)=4,
\]

but

\[
\|a'\|^2\|b'\|^2=8.
\]

Thus the two native rank-one coefficient panels have the same physical
aggregate and different literal diagonal energy.  Their single-cell Wick
values differ by

\[
4d_{\ell,\rho}.
\]

Hence a universal native adapter retaining only the residue aggregate is
still insufficient.

`L-107300` gives the sharp repair: retain the two one-sided quadratic
responses and the two one-sided norms.  No full arbitrary coefficient vector
or faithful rank-\(|\Omega|\) module is needed at scalar scope.
