# T-96011 — Exact status of the hardened four-adic annular chain

Claim ID: `T-96011`  
Status: **UNCONDITIONAL SUCCESSOR STATUS THEOREM**  
Created: 2026-08-16

The following statements are exact:

1. PR #541 invalidates the endpoint consumer used by PR #535.
2. The annular fixed-row transform `L-96010.6` is independent of that
   normalization.
3. The two rows \(2,3\) cannot share an open-strip cancellation.
4. Eventual nonnegativity of those two rows implies RH.
5. Their positivity is exactly the pair of finite Riesz-reserve inequalities
   in `L-96012.9` and can be checked at integer knots.

The following is not certified:

\[
a_X(2)\ge0,\qquad a_X(3)\ge0\qquad(X\text{ sufficiently large}).
\]

PR #535's numerical evidence survives, but its Peano display does not prove
this pair. Therefore this successor does not promote RH as established and
does not describe the old proof as complete.

The strongest live annular chain is now

```text
explicit two-row Riesz reserves         OPEN / RH-BEARING
 -> exact annular Mellin transform       PROVED
 -> exact two-row noncancellation        PROVED
 -> Mellin-Landau                        PROVED IMPLICATION
 -> RH
```
