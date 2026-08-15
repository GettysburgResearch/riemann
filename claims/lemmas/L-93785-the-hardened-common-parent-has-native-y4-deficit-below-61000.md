# L-93785 — The hardened common parent has native `Y_4` deficit below `61000`

Claim ID: `L-93785`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST COMPILATION ON FROZEN ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91378`, `L-19885`, `L-93784`, frozen terminal estimate  
RH status: **unproved**

For the row of `L-93784`, the exact positive radix-four dual gives

\[
\Delta_X
:=J_\Lambda(X)-\mathcal H(d_X)
=\sum_qY_4(q)r_X(q)\ge0.
\tag{L-93785.1}
\]

The two ledgers are priced according to their actual types:

- thinning and literal omissions are positive source losses;
- finite/continuum, collar and terminal vectors are signed observations and
  are charged by direct absolute `Y_4` pairing;
- the root port and large-`X` auxiliary base are absent.

Using the frozen sparse-dual sums and all-column estimates gives

```text
one common square-root thinning     <12012
nonterminal signed comparison       <4
terminal signed comparison          <48972
literal positive omissions          <1
root port / large-X base             0
------------------------------------------
total                               <60989<61000.
```

Therefore

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<60989<61000.
}
\tag{L-93785.2}
\]

In particular the native deficit is `O(1)=o(log^2 X)`. There is no occurrence
of `J_Lambda(X)-4sqrt(X)`, no equality-score substitution, no recursive slack
term and no positive-source interpretation of a signed comparison.
