# X-15103 — Exact Finsler target-completion certificates

Experiment ID: `X-15103`  
Agent: `gpt56-04-f`  
Issue: #151, parallel positive-path continuation  
Status: exact finite linear algebra; no RH claim  
Date: 2026-07-31

## Objective

Replace the sufficient graph-weight screen in `T-15103` by the complete finite
decision for the target-pinned one-scalar matrix pencil

\[
 T_p(c)=A_p+cB_p.
\]

A passing finite object must prove

\[
 T_p(c)\succeq0,\qquad \ker T_p(c)=\mathbb Rp
\]

with exact arithmetic. A failing object may instead carry a rational Finsler
obstruction.

## Checker

`verify.py` supports three schemas under

```text
riemann.target-pinned-finsler-completion.v1
```

### `feasible`

The checker:

1. verifies exact symmetry and `eta^T p=1`;
2. constructs the forced matrices `A_p,B_p`;
3. proves `A_p p=B_p p=0`;
4. builds a rational basis of `p^perp`;
5. performs exact no-pivot LDL on `U^T(A_p+cB_p)U`;
6. reports the graph interval separately.

A pass proves strict positivity on the complement. It does not import an
eigensolver.

### `null-obstruction`

A rational nonzero `x` proves

```text
x perp p
x^T B_p x = 0
x^T A_p x <= 0
```

and therefore rules out every strict scalar completion.

### `pair-obstruction`

A `B_p`-positive and a `B_p`-negative rational direction produce incompatible
strict lower and upper bounds on `c`.

## Retained exact controls

### Positive completion with an empty graph interval

`certificates/feasible-graph-empty.json` uses

```text
p = (1,1,-1/2,-1/2)
c = 0
```

and the Gram matrix

```text
[[ 50, 39, 15,163],
 [ 39, 54, 45,141],
 [ 15, 45, 54, 66],
 [163,141, 66,542]].
```

The exact complement LDL pivots are

```text
26
6075/104
48
```

so the completion is strict.

The graph separator is nevertheless empty:

```text
same-sign lower bound     66
opposite-sign upper bound 15
```

This is the regression for `R-15101`.

### Null-cone obstruction

With `Q=0`, the rational direction

```text
x=(-3,2,-1,-1)
```

is nonzero, lies in `p^perp`, and has both `A` and `B` values zero. Hence no
strict completion exists.

### Conflicting-threshold obstruction

Again with `Q=0`,

```text
x_plus  =(-3,3,-2,2),   x_plus^T B x_plus  = 2
x_minus =(-3,0,-3,-3),  x_minus^T B x_minus=-108
```

force respectively `c>0` and `c<0`.

## Reproduction

```bash
python verify.py certificates/feasible-graph-empty.json
python verify.py certificates/infeasible-null.json
python verify.py certificates/infeasible-pair.json

PYTHONPATH=. python -m unittest discover -s tests -v
```

Ten tests pass. They cover all three proof modes, the graph-incomplete example,
bad scalar rejection, normalization drift, Boolean rational rejection,
non-isotropic false obstructions, wrong threshold signs, asymmetry, and exact
slope inertia.

## Files

```text
verify.py
certificates/
  feasible-graph-empty.json
  infeasible-null.json
  infeasible-pair.json
results/
  feasible-graph-empty-verification.json
  infeasible-null-verification.json
  infeasible-pair-verification.json
  tests.txt
tests/test_verify.py
```

## Proof boundary

The checker certifies only finite rational linear algebra. A finite target
becomes a real-zero object only after review of:

1. the CCM/CvS special-matrix and parity dictionary;
2. the target/basis normalization;
3. the exact target transform;
4. the one-dimensional-kernel requirement.

RH additionally requires a cofinal sequence and locally-uniform convergence to
`Xi`, as stated in `T-15104`.

## Production handoff

For a real Hermite target level:

1. export `Q,p` as exact dyadics or directed intervals;
2. use an ordinary generalized eigensolve to nominate a scalar `c`;
3. rationalize `c`;
4. replay the complement matrix with exact/directed LDL;
5. if no scalar is found, search for a rational null or threshold obstruction;
6. independently certify the target interpolation polynomial by Sturm;
7. retain target-convergence error in a strip norm.

The graph interval may nominate a cheap pass, but an empty graph interval is no
longer a valid reason to discard the level.
