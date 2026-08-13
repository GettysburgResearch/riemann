# R-91309 — A target-exact Hall residual does not automatically reproduce the arithmetic component row

Claim ID: `R-91309`  
Status: **EXACT SCOPE CORRECTION — DIRECT ROW SPLICE `L-91351` IS THE REPAIR**  
Created: 2026-08-13  
Depends on: proposed `L-91348/T-91303`; exact row splice `L-91346/L-91351`  
RH status: **unproved**

## 1. Target Hall residual

Let `T_d>0` be one-prime target atoms and let a target-mass Hall flow satisfy

\[
 \sum_e t_{o,e}=T_o,
 \qquad
 \sum_o t_{o,e}\le T_e.
\]

The residual coefficients

\[
 \nu_e=1-\frac1{T_e}\sum_ot_{o,e}
\]

are positive and reproduce the signed target exactly.

## 2. The missing row identity

Let `R_d(j)` denote the corresponding one-prime component-row atom and put

\[
 \rho_j(d)=\frac{R_d(j)}{T_d}.
\]

The signed arithmetic row is

\[
 A_j=\sum_eR_e(j)-\sum_oR_o(j),
\]

while the row of the target residual source is

\[
 P_j=\sum_e\nu_eR_e(j).
\]

Their difference is exactly

\[
 \boxed{
 A_j-P_j
 =\sum_{o,e}t_{o,e}
   [\rho_j(e)-\rho_j(o)].
 }
\tag{R-91309.1
}

For no-upward edges, normalized-row monotonicity can make every summand
nonnegative.  The finite `P_79` Hall theorem requires bounded upward edges
`o<e<=o+8`; target feasibility alone gives no sign for those row differences.

Thus

```text
positive Hall residual coefficients
+ exact target ledger
```

does not imply that the same residual source equals, or is dominated by, the
signed arithmetic row.

## 3. Consequence

The provisional composition in `T-91303` overstates what the Hall residual alone
supplies.  Its target and bounded-score conclusions remain useful, but its row
interface requires an additional correction theorem.

The live repair avoids this interface entirely.  The exact Euler identity

\[
 D_P(py)=p^{-1/2}D_P(y)+D_{Pp}(py)
\]

uses the actual arithmetic residual row, and `L-91346` proves that residual row
is nonnegative on the inherited block.  `L-91351` combines this with the exact
target and score identities.

```text
Hall residual target exactness                EXACT
Hall residual score bound                     EXACT AT SCALAR SCOPE
Hall residual arithmetic-row typing           NOT AUTOMATIC
provisional T-91303 row interface              GAP
exact Euler residual row                       POSITIVE / REPAIR
Riemann Hypothesis                             UNPROVED
```
