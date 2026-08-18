# R-97701 — NCBI67 and CPSL67 are not equivalent theorem statements

Claim ID: `R-97701`  
Status: **PROVED EXACT FINITE COUNTERMODELS**  
Created: 2026-08-18  
RH status: **not assumed**

The two conditions share a downstream scalar consumer but are not logically equivalent producer statements.

**NCBI without CPSL.** At one node take no recursive child. Give the even source atom `(a,t,r)=(1,1,1)` and the odd source atom `(1,2,0)`. The scalar is positive and NCBI holds. Target capacity fails, and `D^+(-10)=-9`.

**CPSL without NCBI.** On a three-node chain let `T` be the forward shift and `f=(0,0,1)`. Give each node an even-only source with target one and scalar `f_v`; CPSL holds at every node. But `c=(I+T)f=(0,1,1)` and `Tc=(1,1,0)`, so NCBI fails at the root.

The exact valid map is

\[
\mathrm{NCBI}_{67}\Longrightarrow f\ge0,
\qquad
\mathrm{CPSL}_{67}\Longrightarrow f\ge0.
\]

No implication between the producer hypotheses is available without a new source-specific theorem. This refutes claims of abstract or formal equivalence; it does not decide whether both happen to hold on the literal arithmetic family.