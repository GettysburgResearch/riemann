# M-15105 — Directed quartic target-preservation ladder

Methodology ID: `M-15105`  
Status: **PROOF-PRODUCING PROTOCOL; TARGET INTERVAL PRODUCED, OPERATOR ROWS PENDING**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15138`--`L-15140`, `T-15117`, `X-15119`

## 1. One row per coupled level

For each window `M`, compute `N=N(M)` from `T-15117`.  A row must contain
independent directed intervals for

\[
 a_{4,M}^{\rm lin},
 \qquad
 \operatorname{Tr}(A_{M,N}^{4}),
 \qquad
 \operatorname{Tr}(K_{M,N}^{4}),
\]

and for the body/tail diagnostics

\[
 \|c_{4,M}\|,
 \quad
 \|C_M-C_{M,N}\|_4,
 \quad
 \|A_M-A_{M,N}\|_2.
\]

Every row is bound to the exact window, cutoff, Gram, finite-jet, seam,
readout, and normalization fingerprints.

## 2. Independent target

`X-15119` produces a directed interval for

\[
 \tau_4=-\frac16\left[
 \frac{\xi^{(4)}(1/2)}{\xi(1/2)}
 -3\left(\frac{\xi''(1/2)}{\xi(1/2)}\right)^2
 \right]
\]

from the classical theta kernel, independently of all Shimizu comparison maps.

## 3. Verdicts

Use only:

```text
QUARTIC_TARGET_ONLY
QUARTIC_ROW_OVERLAPS_TARGET
QUARTIC_TARGET_CHANGE_CERTIFIED
JET_BODY_PERSISTENCE_CERTIFIED
READOUT_TAIL_CERTIFIED
UNRESOLVED_INTERVAL
```

A sequence of ordinary midpoints is never a convergence proof.

## 4. Generalization after quartic success

If the quartic rows pass, retain the same schedule and evaluate orders
`6,8,...,2L`.  With uniform `S_2` radius `C`, the geometric majorant bounds the
uncomputed coefficient tail on `|w|<=r<1/C`.  Increase `L=L(M)` so

\[
 \frac{C^{2L+2}r^{2L+1}}{1-C^2r^2}
\]

is below the row's directed error budget.  The finite-window body errors and
readout tails must remain separate fields at every order.

## 5. Current state

The independent directed interval for `tau_4` has been produced.  No actual
matrix representation of `A_(M,N)` or `K_(M,N)` is committed by the source
manuscript, so the first operator row remains `MISSING_OPERATOR_PRODUCER` rather
than being synthesized from a surrogate matrix.
