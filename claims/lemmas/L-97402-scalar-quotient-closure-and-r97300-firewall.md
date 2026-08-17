# L-97402 — The 5:3 quotient is closed only at scalar scope

Claim ID: `L-97402`  
Status: **PROVED EXACT TYPE THEOREM**  
Created: 2026-08-18  
Depends on: `L-97400`, `L-97401`, PR #575 `R-97300`

For every typed source atom define the scalar functional

`R_*=5R_2+3R_3`.

The following operations commute with this functional:

1. finite direct sums and positive scalar multiplication;
2. parity swap, with sign character `(-1)^|h|`;
3. finite-colour grouping diagonal in parity space;
4. first-owner restriction and exact source placement;
5. the completed-parity target-plus-scalar Lorenz LP;
6. finite summation over all owner classes.

Consequently a source-complete proof may legitimately descend to the scalar quotient if every operation is performed in this list and no rowwise or physical-capacity claim is subsequently inferred.

PR #575 proves the binding opposite statement. With

`rho(Y)=Q_Y(3)/Q_Y(2)`

nondecreasing, scalar exactness on one edge gives

`Delta_2=-3bQ_o(2)(rho_e-rho_o)/(5+3rho_e)<=0`,

`Delta_3= 5bQ_o(2)(rho_e-rho_o)/(5+3rho_e)>=0`.

Thus scalar exactness preserves `5Delta_2+3Delta_3=0` while generally losing row two. A scalar Hall certificate cannot be fed into a theorem requiring two nonnegative rows, common ordinary columns, or row-valued physical feasibility.

The present route avoids that invalid lift. Its downstream Mellin transform is the transform of the scalar itself. Therefore the exact remaining producer is scalar `CPSL67`, not two-row `GPHT23`.

```text
scalar source conservation             PROVED EXACT
scalar parity conservation             PROVED EXACT
scalar Lorenz optimization             PROVED EXACT
scalar -> two-row positivity           FALSE / R-97300
scalar -> scalar Mellin consumer        TYPE-CORRECT
```
