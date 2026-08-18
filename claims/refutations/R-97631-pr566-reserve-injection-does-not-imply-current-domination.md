# R-97631 — A reserve injection does not imply Hall-complement domination

Claim ID: `R-97631`  
Status: **EXACT STATEMENT-TO-USE COUNTEREXAMPLE**  
Frozen target: PR #566 at `2407b4ffe5024a2e3898922cf0b722d5cf69e496`  
RH status: **unproved**

PR #566 proposes
\[
\mathcal G_v=\mathcal H_v\oplus\bigoplus_w\mathcal R_{v\to w}
\]
and injections
\[
\alpha_{v,w}\mathcal G_w\hookrightarrow\mathcal R_{v\to w}.
\]
This controls the scalar of the reserve. The next stage consumes
\[
g_v\ge\sum_w\alpha_{v,w}g_w,
\]
where `g_v` is the scalar of the disjoint Hall complement `H_v`.

The implication is false. Take
\[
\alpha=\frac12,\qquad
\mathcal H_v=(1,0),\qquad
\mathcal R_{v\to w}=\left(\frac12,\frac12\right),\qquad
\mathcal G_w=(1,1),
\]
and observe with the second coordinate. The injection is exact and every
source coordinate is nonnegative, but
\[
g_v=0<\frac12=\alpha g_w.
\]
Thus PR #566 still requires an independent complement-versus-child theorem.
