# O-91311 — Corrected direct-row factor-54 proof DAG and frozen review frontier

Claim ID: `O-91311`  
Status: **CURRENT CORRECTED FULL-PROPOSAL HANDOFF — NO ACCEPTED RH CLAIM**  
Created: 2026-08-13  
Corrected: 2026-08-13 after `R-91310/L-91352`  
Depends on: corrected `T-91304` and its exact dependencies  
RH status: **proposed pending independent review**

## 1. Corrected proof DAG

```text
finite factor-54 endpoint producer
  -> exact least-prime source partition
  -> P79 terminal child projection
  -> direct Euler row identity
       parent = p^(-1/2) terminal child + arithmetic residual
  -> inherited arithmetic residual row positive (L-91346)
  -> residual target and declared source score separately positive
  -> exact literal residual-row entropy formula
  -> positive von Mangoldt convolution and physical entropy moat (L-91352)
       literal row entropy > residual target by (4/15)sqrt(py)
  -> one-use exact frontier/collar/radix-four assembly
  -> substochastic score recurrence with bounded debt
  -> O(log X) endpoint-score loss
  -> endpoint-score RH consumer
  -> RH, conditionally on all review obligations
```

The former arrow

```text
residual declared score > residual target
```

is false and has been removed. `R-91310` gives the exact witness
`(p,y)=(83,1)`. The corrected composition uses the literal component-row entropy,
not the declared source-score label.

## 2. Mandatory firewalls

The DAG does not use:

```text
L-91112 finite seed = continuum Volterra seed;
independent scalar rough-port tensorization;
completed two-state SHARP tensorization;
full-parent source duplication across prime branches;
raw-l1 contraction of the four-state lift;
Hall target residual as automatic arithmetic-row typing;
integer-column estimates at fractional child columns;
active-threshold prefix bounds at arbitrary real endpoints;
declared source score as automatic physical row entropy.
```

The corresponding refutations and corrections remain mandatory dependencies.

## 3. Exact replay packet

```text
X-91122  terminal P79 target/score/row projection;
X-91125  inherited P79-plus-p row positivity;
X-91127  corrected finite low-prefix Hall theorem;
X-91129  direct Euler composition and homogeneous debt algebra;
X-91130  exact scalar counterexample and physical-entropy repair gates.
```

The `X-91125` source at frozen commit
`4b8b4306142e92d66bc27f7eda10f64a703ed3d8` has now been independently replayed.
It reproduced all `4,194,304` global states, the retained extrema, and the exact
margins

```text
38381/90000;
18779/1417500.
```

## 4. Independent-review obligations

A reviewer should freeze the live head and reconstruct:

1. every analytic inequality used by `L-91346` before consulting its checker;
2. the activation-cell partition and derivative signs in `X-91127`;
3. the exact entropy convolution and partial summation in `L-91352`;
4. the imported formal bound `psi(x)>=0.9x` for `x>=41`;
5. the typing of inherited versus current-generation frontier rows;
6. exact realization of all rows `j>y` in the entropy normalization used by
   `L-91352`;
7. source-disjoint least-prime substochasticity;
8. ordinary and radix-four one-use physical assembly;
9. the endpoint-score loss orientation and the final RH implication.

Any failure retains all earlier verified finite theorems but blocks `T-91304`.

## 5. Status

```text
false scalar surplus identified       YES
stronger physical repair proposed     YES
X-91125 independent replay             PASS
full corrected proof proposal assembled YES
complete independent verification      NO
accepted proof of RH                    NO
```
