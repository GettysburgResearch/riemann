# O-91311 — Corrected direct-row factor-54 proof DAG and frozen review frontier

Claim ID: `O-91311`  
Status: **CURRENT FULL-PROPOSAL HANDOFF — NO ACCEPTED RH CLAIM**  
Created: 2026-08-13  
Depends on: `T-91304` and its exact dependencies  
RH status: **proposed pending independent review**

## 1. Corrected proof DAG

```text
finite factor-54 endpoint producer
  -> exact least-prime source partition
  -> P79 terminal child projection
  -> direct Euler row identity
       parent = p^(-1/2) terminal child + arithmetic residual
  -> inherited arithmetic residual row positive (L-91346)
  -> residual target positive (L-91345/L-91350)
  -> residual score > residual target (L-91351/X-91128)
  -> one-use sum-before-quantize physical assembly
  -> substochastic score recurrence with bounded debt
  -> O(log X) endpoint-score loss
  -> endpoint-score RH consumer
  -> RH, conditionally on review
```

## 2. Mandatory firewalls

The DAG does not use:

```text
L-91112 finite seed = continuum Volterra seed;
independent scalar rough-port tensorization;
completed two-state SHARP tensorization;
full-parent source duplication across prime branches;
raw-l1 contraction of the four-state lift;
Hall target residual as automatic arithmetic-row typing;
integer-column estimates at fractional child columns.
```

The corresponding refutations and corrections remain mandatory dependencies.

## 3. Exact replay packet

```text
X-91122  terminal P79 target/score/row projection;
X-91125  inherited P79-plus-p row positivity;
X-91127  corrected finite low-prefix Hall theorem;
X-91128  P79 child first-moment upper bound;
X-91129  direct Euler composition and homogeneous debt algebra.
```

## 4. Independent-review obligations

A reviewer should freeze the live head and reconstruct:

1. every analytic inequality used by `L-91346` before consulting its checker;
2. the activation-cell partition and derivative signs in `X-91127`;
3. the exact first-moment prefix bounds;
4. the typing of inherited versus current-generation frontier rows;
5. source-disjoint least-prime substochasticity;
6. ordinary and radix-four one-use physical assembly;
7. the endpoint-score loss orientation and the final RH implication.

Any failure retains all earlier verified finite theorems but blocks `T-91304`.

## 5. Status

```text
full proof proposal assembled       YES
independent adversarial verification NO
accepted proof of RH                NO
```
