# X-20705 — Square-support D-0001 embedding reconnaissance

This ordinary-high-precision experiment evaluates the explicit schedule

```text
(N,c)=(M,M^2),  M=2,...,13.
```

At every level it constructs the complete cutoff-free D-0001 even matrix,
including:

- every prime power `q<=M^2`;
- the full polar block;
- the cutoff-free digamma/trigamma archimedean block;
- the rational-Leja first frame;
- the product-form rank-one kernel;
- the complete positive-sector Schur pivot.

It independently evaluates the square-screw scalar of `L-20704` and records

```text
square_screw-log(M)*A00.
```

The largest observed absolute mismatch is below `1.2e-69` at 70 decimal digits.
This is a numerical regression for the exact analytic identity, not its proof.

All twelve complete matrices and all twelve structured Schur pivots are positive
in the retained table. The smallest final pivot is approximately

```text
5.61140043407625e-48
```

at `(M,N,c)=(13,13,169)`.

The unnormalized graph-kernel metric grows to approximately `5.77e42`, while the
rational-Leja pivots remain around `1e-3` or larger. This again separates
algebraic frame conditioning from the physical near-null scale.

## Reproduction

```bash
python recon.py --digits 70 --max-M 13 --zero-count 180 \
  --output results/recon.json
```

## Classification

`NON_DIRECTED_HIGH_PRECISION_RECONNAISSANCE`.

`mpmath` values and zeta-zero ordinates are not directed intervals. The table
nominates square-support packets and checks formulas; it does not certify any
matrix sign or contribute an unbounded lower-bound proof.
