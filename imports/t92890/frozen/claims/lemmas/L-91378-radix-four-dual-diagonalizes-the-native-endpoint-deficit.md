# L-91378 — The radix-four dual diagonalizes the native endpoint deficit

Claim ID: `L-91378`  
Status: **PROVED EXACT POSITIVE-DUAL THEOREM**  
Created: 2026-08-14  
Depends on: the exact average-binomial carry identity  
RH status: **unproved**

## 1. Positive dual weight

For every integer `q>=1`, define

\[
\boxed{
 Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k).
}
\tag{L-91378.1}
\]

Every term is nonnegative. The finite recurrence is

\[
\boxed{
 Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q).
}
\tag{L-91378.2}
\]

Indeed, all terms except the `k=0` term cancel after shifting the second sum.

## 2. Radix-four summation by parts

For any finitely supported ordinary-column vector `C(q)`, put

\[
 (\mathcal D_4C)(q)=C(q)-2C(4q).
\]

Using (L-91378.2) and changing variables in the second term,

\[
\boxed{
 \sum_q\Lambda(q)C(q)
 =\sum_qY_4(q)(\mathcal D_4C)(q).
}
\tag{L-91378.3}
\]

No convergence issue occurs for a finite endpoint packet.

## 3. Row score and native benchmark

For a finite nonnegative row `d`, the exact carry identity gives

\[
 \mathcal H(d)=\sum_q\Lambda(q)C_d(q).
\]

Therefore

\[
\boxed{
 \mathcal H(d)=\sum_qY_4(q)\Xi_d(q),
}
\tag{L-91378.4}
\]

where `Xi_d=D_4 C_d`.

Applying (L-91378.3) to the native capacity `w_X` gives

\[
\boxed{
 J_\Lambda(X)=\sum_qY_4(q)\Omega_X(q).
}
\tag{L-91378.5}
\]

Consequently every detail-feasible row satisfies the exact deficit identity

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)]\ge0.
}
\tag{L-91378.6}
\]

## 4. Consequences

The endpoint objective has no independent hidden score term. It is exactly the
positive `Y_4`-weighted unused detail capacity.

Thus an explicit producer proves the needed one-sided endpoint bound as soon as
it proves

\[
\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)]=o(\log^2X),
\]

or any stronger uniform bound.

The theorem also gives a strict audit rule: ordinary feasibility alone is
insufficient; the proof object must expose the signed radix-four slack on every
physical column.

```text
Y_4 recurrence                         EXACT / POSITIVE
row score = Y_4-weighted detail use    EXACT
J_Lambda = Y_4-weighted native target  EXACT
endpoint deficit = weighted slack      EXACT
small weighted native slack producer   OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```
