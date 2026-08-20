# L-99704 — Cross-source prime-exchange flow is the exact noncircular orientation problem

Claim ID: `L-99704`  
Status: **PROVED EXACT FINITE MAX-FLOW/MIN-CUT REDUCTION**  
Created: 2026-08-20  
Depends on: `L-99702`, `L-99703`  
RH status: **not assumed**

For fixed `X`, use the bounded box potential `Phi_X^Box` from `L-99703` and define two positive source measures on the integer vertices:

\[
m_X^\pm(n)
=\pi(n)\Phi_X^{\Box}(n)\frac{1\pm f(n)}2.
\tag{L-99704.1}
\]

Then

\[
\boxed{
\sum_nm_X^+(n)-\sum_nm_X^-(n)
=\frac{(\mathcal S_{67}h)(X)}{\sqrt X}.
}
\tag{L-99704.2}
\]

Thus every source coefficient, repeated-prime reserve, and factor-67 local square is present once in a positive two-channel ledger.

Construct a finite capacitated bipartite graph as follows.

* A left copy of every vertex carries demand `m_X^-(n)`.
* A right copy carries capacity `m_X^+(n)`.
* A left vertex may send flow to a right vertex only along a path of the reversible prime-birth/death graph of `L-99702`.
* Every path retains its complete prime-power labels and every intermediate source occurrence is used with capacity at most one.

For any admissible flow `J`, let `rho_X(J)` be its unmatched left mass. Then

\[
\boxed{
\bigl[-(\mathcal S_{67}h)(X)\bigr]_+
\le \sqrt X\,\rho_X(J).
}
\tag{L-99704.3}
\]

The optimal residual `rho_X^*` is characterized by the ordinary finite max-flow/min-cut theorem. In particular,

\[
\boxed{
\rho_X^*
=\sup_{S}
\left[
 m_X^-(S)-m_X^+(N(S))
\right]_+,
}
\tag{L-99704.4}
\]

where `S` ranges over left vertex sets and `N(S)` is their allowed prime-exchange neighborhood with the inherited occurrence capacities.

This is not a renaming of the desired sign:

* the graph and all capacities are explicit functions of `beta`, `g`, `T`, and `X`;
* the flow is restricted to exact prime-power source moves;
* arbitrary direct matching of total positive and negative masses is forbidden;
* the within-integer owner martingale of `L-99701` is only the downward part of this graph;
* `R-99700` proves why the downward part alone is insufficient.

The same construction may be integrated over logarithmic `X`-blocks. If an explicit family of flows satisfies

\[
\int_1^Y\sqrt X\,\rho_X(J_X)\frac{dX}{X}
\ll_\varepsilon Y^\varepsilon
\qquad(\varepsilon>0),
\tag{L-99704.5}
\]

then the negative logarithmic mass of the zero-free box scalar is subpower. The one-sided Mellin--Landau argument of `L-99270` then excludes every off-line zero.

Equation (L-99704.4) is the exact hostile-review interface. A claimed electrical proof must bound these live min-cuts; positivity of local Schur matrices, divisor-owner quadratic variation, or an unconstrained common contraction does not do so.