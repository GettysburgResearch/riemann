# X-105640 — Strong-log-concavity and depth-collar exact ledger

Run:

```bash
python experiments/X-105640-strong-logconcavity-depth-collar/verify.py
```

Expected output:

```text
PASS_X_105640_STRONG_LC_DEPTH_COLLAR
checks=4223
b8d2c8770f38dbcace6a481f540d2fad1af8c01ad04fabde2ecc8167890adcf0
RH_UNPROVEN
```

The replay checks, using exact rational arithmetic:

- the final uniform-curvature constant ledger
  `20476/2345 = 8 + 1716/2345`;
- the first-theta-orbit mass ledger;
- the product-defect inequality used for finite Blaschke packets;
- the exact simple-factor charge `2y/(H+2y)` after cancelling the common
  Poisson-integral factor;
- finite layer-cake identities and soft-depth majorants;
- the critical-height Maxwell factor
  `79559/81904 > 97/100` and its exact rational margin.

It does **not** replay:

- the infinite theta-series proof of strong log-concavity;
- monotone-likelihood domination by the Maxwell law;
- the Paley--Wiener/model-space functional-analysis argument;
- the Xi-prime zero-count passage to cofinal windows;
- the height-owner or boundary-collar physical transfer;
- RH.

The retained result file is `results/verification.json`.