# R-96100 — Native-gap and imported-producer firewall for the annular lineage

Claim ID: `R-96100`  
Status: **PROVED EXACT CORRECTION / FAIL-CLOSED IMPORT AUDIT**  
Created: 2026-08-16  
Frozen annular parent: PR #535 at `988e9bfa55e7ed13c0ddbcab2f6138a83fd4f743`  
Compared resets: PR #541 and PR #542  
RH status: **unproved**

## 1. The radix-four native target prices the prime-power ramp

For a finitely supported ordinary response `C`, define

\[
 (\mathcal D_4C)(q)=C(q)-2C(4q)
\]

and

\[
 Y_4(q)=\sum_{4^r\mid q}2^r\Lambda(q/4^r).
\]

The exact adjoint identity is

\[
 \langle Y_4,\mathcal D_4C\rangle
 =\sum_q\Lambda(q)C(q).
\tag{R-96100.1}
\]

For

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
 \qquad \Omega_X=\mathcal D_4w_X,
\]

this gives

\[
 \boxed{\langle Y_4,\Omega_X\rangle=P_\Lambda(X),}
\tag{R-96100.2}
\]

not `J_Lambda(X)`. Therefore every physical row `d` satisfies

\[
 \boxed{
 J_\Lambda(X)-\mathcal H(d)
 =F_\Lambda(X)+
   \langle Y_4,\Omega_X-\Xi_d\rangle,
 }
\tag{R-96100.3}
\]

where `F_Lambda=J_Lambda-P_Lambda`.

Consequently, even exact native saturation gives

\[
 \mathcal H(c_X)=P_\Lambda(X)
\]

and leaves the complete arithmetic gap `F_Lambda` untouched. The endpoint consumer in `T-94201` on PR #535 is therefore not valid. This correction is independent of whether the annular row is positive.

## 2. The direct consumer on PR #542 is the correct downstream architecture

PR #542 avoids (R-96100.3) by taking a Mellin transform of a fixed component row. That architecture is retained and strengthened in `L-96101--L-96102`. No `J/P/F` benchmark identification enters the new implication.

## 3. The PR #537 `FRONTIER-CHAIN` producer is not imported

The displayed expansion in PR #537 groups terms by the fixed product `n=d m`:

\[
 \mathfrak S_{r,j}(e^x)
 =\sum_n\omega_{r,j}(n)\mathcal K_x(\log n).
\]

It then says that a residual path never combines different products `n`, while also claiming that positive atoms adjacent to one negative shoulder bracket it at distinct logarithmic positions. Within one fixed product every vertex is attached to the same point `log n`; there are no three distinct positions on which the stated convex packet can act. The ownership assertion and the bracketing assertion therefore do not compose as written.

This is a proof gap, not a numerical counterexample to the finite-sieve positivity statement. The statement may still be true, but it is not imported into this successor.

## 4. The PR #535 Peano display is not treated as a proof

The proposed formula `L-94201.5--.7` does not derive the set `J_(X,n,h)` or the two cut-block coefficients from the original Möbius sum, and its displayed right side contains no auditable occurrence of the divisor switch that is asserted to remove every Möbius sign. The regression checks the triangular inverse but not that symbolic identity.

Accordingly:

```text
annular numerical positivity                  retained as evidence
PR #535 four-block identity                   unverified / not imported
PR #535 endpoint consumer                     refuted by exact normalization
PR #537 FRONTIER-CHAIN proof                   ownership gap / not imported
PR #542 fixed-row Mellin architecture          retained and strengthened
Riemann Hypothesis                             unproved
```
