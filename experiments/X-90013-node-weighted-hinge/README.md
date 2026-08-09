# X-90013 — Node-weighted SHARP hinge mutation

Directed finite certificate for `R-90005`.

Run:

```bash
python experiments/X-90013-node-weighted-hinge/verify.py
```

Expected line:

```text
PASS_NODE_WEIGHTED_SHARP_AVERAGE_ROW_REFUTATION
```

The script constructs the multiples-Möbius state and the exact average-row
adjoint for

```text
g_T(q)=2sqrt(q)-2q/sqrt(T).
```

Using `mpmath.iv` at 70 decimal digits it certifies

```text
a_18(3) in (-0.016357533249176,-0.016357533249175),
a_24(4) in (-0.385666938614629,-0.385666938614628).
```

It also scans `3<=T<=18` and records that `T=18,j=3` is the first finite
mutation.  Only the two displayed negative intervals are load-bearing.
