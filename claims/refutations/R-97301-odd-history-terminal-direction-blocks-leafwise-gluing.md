# R-97301 — Completed parity does not repair the odd-history terminal direction

Claim ID: `R-97301`  
Status: **PROVED FROM THE PR #561 DIRECTED CERTIFICATE**  
Created: 2026-08-17  
Frozen source: PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`  
RH status: **unproved**

Consider

\[
X=67\cdot71\cdot13=61841,
\qquad h=(67),
\qquad (p,y)=(71,13).
\]

PR #561's directed 192-bit target audit over all `239` active `P_61` divisors
certifies

\[
E_T(71,13)-O_T(71,13)>17.
\tag{R-97301.1}
\]

The incoming history has odd length.  By `L-97300`, the native terminal packet
is swapped, so a leafwise exact-target Hall map would require

\[
O_T(71,13)\ge E_T(71,13),
\]

contradicting (R-97301.1).

The ratio theorem `L-97301` concerns component rows only after a coefficient and
edge direction have been admitted.  It does not change the target coordinate
and cannot turn an infeasible reverse target edge into a feasible one.
Complete `P_61` grouping and `5:3` scalarization are diagonal in parity and also
cannot change (R-97301.1).

Therefore the order

```text
complete history -> assign parity -> terminalize each leaf
```

is still invalid when terminalization offers only the canonical orientation.
A valid successor must couple different histories globally or prove a second
positive realization for every reversed terminal datum.
