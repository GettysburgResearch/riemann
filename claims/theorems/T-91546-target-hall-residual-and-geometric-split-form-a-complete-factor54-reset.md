# T-91546 — Historical target-Hall composition; affine physical assembly withdrawn

> **SUPERSEDED / DO NOT USE AS A COMPLETE COMPOSITION.**  `R-91558` gives an
> exact canonical counterexample to the affine fixed-67 detail-capacity step in
> the original Sections 3--4.  The source-Hall and substochastic scalar
> statements survive.  The corrected physical route is
> `L-91556 -> L-91560 -> L-91545 -> L-91547 -> L-91559`.

Claim ID: `T-91546`  
Status: **HISTORICAL CANDIDATE — PHYSICAL CAPACITY STEP REFUTED / PARTIAL INPUTS RETAINED**  
Created: 2026-08-13  
Corrected: 2026-08-13  
Frozen parent: PR `#399` at `22d7f2f3f3668f664c09708838f6a738e4398eef`  
RH status: **unproved**

## 1. Retained exact inputs

The following parts of the historical composition remain valid on their stated
frozen inputs:

1. the binary target telescope
   \[
   T_s+T_h=T_{\rm parent};
   \]
2. the favorable full binary score telescope;
3. target-Hall residualization into positive source measures plus target-null
   positive row bonuses (`L-91545`);
4. the deterministic fixed-67 source split and child target
   subprobability (`L-91547`);
5. the abstract actual-packet branching consumer (`T-91541`);
6. one-use common-port accounting on the cited normalization (`L-91548`).

These are not themselves a physical detail-capacity lift.

## 2. Refuted step

The original theorem instructed the construction to:

```text
affine-lift a detail-feasible child by
n -> 67(n+1)-1;
regard positive unmatched-column carry as harmless;
sum the lifted finite children and appeal to L-91329.
```

`R-91558` disproves this.  The canonical child `Q_3` is detail feasible at
endpoint `3`, but its fixed-67 affine image at endpoint `201` overdraws the
unmatched physical detail column `200`:

\[
 \frac{597}{201\sqrt{134}}\log\frac32
 >
 \frac1{\sqrt{200}}\log\frac{201}{200}.
 \tag{T-91546.1}
\]

Therefore the former capacity-faithful assembly and the recurrence derived from
it do not follow.

## 3. Correct replacement

The fixed-67 child should not be dilated.  `L-91559` proves that the exact
component row has positive nested detail target

\[
 \Theta_Y(q)
 =q^{-1/2}[H(Y/q)-H(Y/(4q))]
 \tag{T-91546.2}
\]

and that direct identity embedding gives the exact replacement

\[
 d_X=a(Q_X-Q_{X/67})+d_{X/67}.
 \tag{T-91546.3}
\]

This is nonnegative and detail feasible at every physical integer column.

`L-91556` supplies the native row-budgeted binary coefficients, and `L-91560`
proves the exact residual-plus-child controlled cocycle in the literal row
space.  These results were not present in the historical theorem.

## 4. Current boundary

The old theorem is not the normative proof DAG.  A corrected composition must
still replay the finite least-prime source provenance and the live one-prime
Hall normalization before using the direct physical replacement.

```text
binary scalar target telescope                      RETAINED
Hall residual source and row bonus                   RETAINED
fixed-67 child target subprobability                 RETAINED
affine fixed-67 detail assembly                      FALSE / R-91558
identity fixed-67 detail assembly                    EXACT / L-91559
native row cocycle                                   EXACT / L-91560
historical complete composition                      WITHDRAWN
Riemann Hypothesis                                   UNPROVEN
```
