# L-97702 — Exact theorem-level maps among NCBI67, CPSL67 and completed parity

Claim ID: `L-97702`  
Status: **PROVED EXACT MAP AND NON-EQUIVALENCE THEOREM**  
Created: 2026-08-18  
Depends on: `L-97500--L-97502`, `L-97601`, `L-97603`, `L-97700`  
RH status: **unproved**

At a node `v`, let `P_v` be the literal paired source and

\[
f_v=D_{P_v}^+(0)=R_E(P_v)-R_O(P_v)
\tag{L-97702.1}
\]

its actual signed `5:3` scalar. The source-faithful contracted identity is

\[
P_v=C_v\oplus\bigoplus_wt_{vw}\mathsf SP_w.
\tag{L-97702.2}
\]

With `c_v=D_{C_v}^+(0)`, this gives

\[
\boxed{f+Tf=c.}
\tag{L-97702.3}
\]

`NCBI67` is \(c\ge Tc\). Since the finite rough-history operator is nilpotent,

\[
c-Tc=(I-T^2)f,
\]

and therefore

\[
\boxed{\mathrm{NCBI}_{67}\iff(I-T^2)f\ge0\Longrightarrow f\ge0.}
\tag{L-97702.4}
\]

The last implication uses \((I-T^2)^{-1}=\sum_{j\ge0}T^{2j}\ge0\).

By `L-97700`, `CPSL67` is exactly

\[
\boxed{D_{P_v}^+(\lambda)\ge0\quad\text{for every node }v\text{ and real }\lambda.}
\tag{L-97702.5}
\]

At zero this implies \(f\ge0\). Thus both producer statements imply the same scalar sign, but by different sufficient mechanisms.

They are not equivalent.

**NCBI without CPSL.** Take one node with `T=0`; even atom `(a,t,r)=(1,1,1)` and odd atom `(1,2,0)`. Then `f=c=1`, so NCBI holds, but target capacity fails and \(D^+(-10)=-9\).

**CPSL without NCBI.** On a three-node chain let \((Tx)_0=x_1,(Tx)_1=x_2,(Tx)_2=0\), and take \(f=(0,0,1)\). Give each node an even-only source with target one and scalar `f_v`; CPSL holds at every node. But

\[
c=(I+T)f=(0,1,1),\qquad Tc=(1,1,0),
\]

so NCBI fails at the root.

Hence

\[
\boxed{\mathrm{NCBI}_{67}\not\equiv\mathrm{CPSL}_{67}}
\tag{L-97702.6}
\]

as theorem statements. On the literal arithmetic family, neither missing implication has been proved.

For the full Lorenz lift, let `G_v^+(lambda)` be the current slack and define

\[
\mathfrak B_v(\lambda)=G_v^+(\lambda)-\sum_wt_{vw}D_w^+(\lambda).
\]

Then `L-97700` gives

\[
D_v^+(\lambda)=\mathfrak B_v(\lambda)+\sum_wt_{vw}(D_w^+(\lambda)+D_w^-(\lambda)).
\tag{L-97702.7}
\]

Thus \(\mathfrak B_v\ge0\) for every node and `lambda` implies CPSL67. At zero, \(\mathfrak B_v(0)=c_v-(Tf)_v=f_v\). This is the exact source-faithful Lorenz lift. It depends on complete child source slack, not a replacement by child current.

The valid implication graph is

\[
\mathrm{LBP}_{67}\Longrightarrow\mathrm{CPSL}_{67}\Longrightarrow f\ge0,
\qquad
\mathrm{NCBI}_{67}\Longrightarrow f\ge0.
\]

No additional arrow is asserted.