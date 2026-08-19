# T-99700 — Canonical scalar/native-source spine

This packet reconciles the newest native-coefficient audits with the strongest
scalar Mellin consumer.

Its new exact ingredients are:

- a symmetric random-order Euler homotopy preserving every native coefficient;
- a positive inverse renewal at every half-order tilt;
- an exact positive prime-power owner evolution in the tilt parameter;
- a positive-work bound for the scalar negative part;
- an `O(log log X)` integrated critical tilt-energy budget;
- firewalls against degenerate Doob variance and pole-cancelling positive Euler
  smoothing.

The single open theorem is `TOCE67`, a source-root/boundary Carleson estimate.
It implies subpower logarithmic negative mass and therefore RH. `TOCE67` and RH
are not proved here.

Remote replay:

```bash
python3 experiments/X-99700-canonical-spine/verify.py \
  --output experiments/X-99700-canonical-spine/results/verification.json
python3 -m unittest discover \
  -s experiments/X-99700-canonical-spine/tests -v
```

The deterministic fallback archive carries its own complete SHA-256 ledger.
