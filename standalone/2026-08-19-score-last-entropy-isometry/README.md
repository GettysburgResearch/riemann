# T-99050 — Score-last entropy-isometric hardening

Frozen parent:

```text
PR #620
493e12fcba3f9b98dda7c3595bff73b256e00ca4
```

Main result:

```text
complete finite causal tree score loss   exactly zero
fixed top omission                       <60
one common thinning                      <792
complete root-owned score loss           <852
```

Replay:

```bash
python3 experiments/X-99050-score-last-tree/verify.py \
  --output experiments/X-99050-score-last-tree/results/verification.json
python3 -m unittest discover -s experiments/X-99050-score-last-tree/tests -v
sha256sum -c T99050_CONTENT_SHA256SUMS
```

Scientific status: proposed hardening; RH unproved pending independent review.
