# X-105640 — Strong-log-concavity and depth-collar exact ledger

Run:

```bash
python experiments/X-105640-strong-logconcavity-depth-collar/verify.py
```

Expected output:

```text
PASS_X_105640_STRONG_LC_DEPTH_COLLAR
checks=4219
769c7f5f517949d0591e8cc33032a6f081abbf5ea43ad53556daeac2499b4a69
RH_UNPROVEN
```

The replay checks, using exact rational arithmetic:

- the final uniform-curvature constant ledger
  `20476/2345 = 8 + 1716/2345`;
- the first-theta-orbit mass ledger;
- the product-defect inequality used for finite Blaschke packets;
- the exact simple-factor charge `2y/(H+2y)` after cancelling the common
  Poisson-integral factor;
- finite layer-cake identities and soft-depth majorants.

It does **not** replay:

- the infinite theta-series proof of strong log-concavity;
- the Paley--Wiener/model-space functional-analysis argument;
- the Xi-prime zero-count passage to cofinal windows;
- the boundary-collar signed-index conversion;
- RH.

The retained result file is `results/verification.json`.