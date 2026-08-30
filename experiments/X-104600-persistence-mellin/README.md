# X-104600 — Persistence–Mellin exact algebra replay

This standard-library replay verifies the finite algebra used by T104600.

It checks:

1. the exact threshold identity `G_y-W_y=N_y/2` at four rational levels of a
   six-critical-point fixture;
2. the power-moment/coarea identity for `p=1,2,3,4`;
3. one nonnegative Hankel/log-convexity determinant for the normalized Mellin
   hierarchy;
4. the exact excursion-complexity transfer constant `eta=1/3` on the fixture.

Run:

```bash
python3 experiments/X-104600-persistence-mellin/verify.py \
  experiments/X-104600-persistence-mellin/results/verification.json
```

The replay does not prove `EXCUR104600`, `PVAR104600`, a numerical
`alpha_2` descent, or RH.
