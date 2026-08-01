# X-20705 — Log-squared source-canonical Schur reconnaissance

This experiment nominates the explicit unbounded schedule

```text
c_j = ceil(exp(j))
N_j = j^2
```

for a future directed prime-side LDL producer. It imports the complete D-0001
assembly from `X-20704`, including the full polar and cutoff-free archimedean
blocks and every prime power `q<=c`.

Run from this directory with

```bash
python recon.py \
  --digits 180 \
  --j-min 2 \
  --j-max 6 \
  --x20704 ../X-20704-growing-prime-side-recon/recon.py \
  --output results/recon.json
```

## Classification

The arithmetic is ordinary `mpmath`, not interval arithmetic. The retained table
is reconnaissance only. In particular, the extremely small complement
eigenvalues are not directed lower bounds.

The cancellation control at `(c,N)=(500,7)` contracts all three channels on the
same source-constrained harmonic minimizer. The individual terms are of order
`1e30`, while the joint quotient is about `3.1e-2`; separate channel bounds are
therefore unusable for the final sign.
