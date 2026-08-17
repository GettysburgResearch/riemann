# R-97402 — PR #566's reserve injection does not imply its current-scalar domination

Claim ID: `R-97402`  
Status: **EXACT STATEMENT-TO-USE REFUTATION OF THE PROOF OF `L-96651(iv)`**  
Created: 2026-08-18  
Frozen target: PR #566 at `2407b4ffe5024a2e3898922cf0b722d5cf69e496`  
RH status: **unproved**

`L-96651` proposes a decomposition
\[
\mathcal G_v=
\mathcal H_v\oplus
\bigoplus_w\mathcal R_{v\to w}.
\tag{R-97402.1}
\]
It defines
\[
g_v=\operatorname{scalar}(\mathcal H_v),
\]
and constructs injections
\[
\alpha_{v,w}\mathcal G_w\hookrightarrow\mathcal R_{v\to w}.
\tag{R-97402.2}
\]
From (R-97402.2) one may conclude
\[
\operatorname{scalar}(\mathcal R_{v\to w})
\ge\alpha_{v,w}\operatorname{scalar}(\mathcal G_w).
\tag{R-97402.3}
\]
It gives no inequality comparing the **Hall complement**
`scalar(H_v)=g_v` with the reserve scalar.  Nevertheless the proof concludes
\[
\boxed{g_v\ge\sum_w\alpha_{v,w}g_w.}
\tag{R-97402.4}
\]

An exact one-parent/one-child model isolates the failure.  Take
\[
\alpha=\frac1{10},
\quad
\operatorname{scalar}(\mathcal G_w)=10,
\quad
\operatorname{scalar}(\mathcal R_{v\to w})=1,
\quad
\operatorname{scalar}(\mathcal H_v)=\frac12.
\]
All objects are positive, the reserve is disjoint, and the injection is scalar
exact:
\[
1=\alpha\cdot10.
\]
But
\[
\frac12<1=\alpha\operatorname{scalar}(\mathcal G_w),
\]
so (R-97402.4) fails.

The abstract `M`-matrix lemma `L-96652` is correct if `g>=Tg` is supplied.  The
error is the derivation of that premise.  Redefining `g_v` as the scalar of the
whole parent `G_v` makes (R-97402.3) useful, but then the recursion right side is
not the Hall current and the reserve is counted in both `g` and the recursive
child.  A new one-use source identity is required.
