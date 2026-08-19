# T99230/T99231 — Distributional Volterra boundary modes and two-anchor calibration

This add-only audit is stacked on PR #620 at exact head

```text
493e12fcba3f9b98dda7c3595bff73b256e00ca4
```

It proves the exact distributional Green formula for the endpoint inverse used
there, identifies its two-dimensional homogeneous nullspace, records every
activation-knot atom, and reduces positive equality-frame reconstruction to one
finite two-anchor cone test.

The actual PR #620 knot ledger and anchor matrix are not supplied by this
packet. RH remains unproved.

Replay:

```bash
python3 experiments/X-99230-volterra-boundary/verify.py
sha256sum -c T99230_CONTENT_SHA256SUMS
```
