# X-90208 — Critical boundary, positive-defect, and minimax-filter replay

This package supports the exact algebra in:

- `L-90215` — repaired all-scale positive renewal;
- `L-90220` — positive Pascal rewards have positive square-root defect;
- `L-90221` — critical-neutral minimax debt and exact reciprocal-square tail sweep.

It is a mutation/replay package, not the proof of the analytic inequalities and
not a certificate for RH.

## Run

```bash
python3 verify.py
```

The script uses only the Python standard library. A successful replay prints:

```text
PASS_X_90208_CRITICAL_BOUNDARY_ATTACK
```

## Checked layers

1. Direct renewal versus the complete piecewise forcing for the canonical
   `15:4` scalar and for the critical-neutral `Q_star` scalar.
2. Positivity reconnaissance for the elementary fixed-hit critical defects
   through boundary state 10,000, including the repaired integral lower bound.
3. One hundred exact `Q(sqrt(2))` critical-neutral filter identities using
   rational-pair arithmetic in `Q(sqrt(2))`.
4. Exact minimax-debt mutation checks.
5. Exact uniform-Pascal reward rows for `Q_star` through state 256.
6. Thirty exact random-source checks of the reciprocal-square tail sweep.

The analytic proofs and scope boundaries remain in the claim files.
