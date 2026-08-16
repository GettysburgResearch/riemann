# Standalone review front door: phase-locked safe-line and two-row Landau

This directory is the compact review front door for the 93280 successor.

Review order:

```text
R-93280
L-93280
L-93281
L-93282
L-93283
L-93284
T-93280
T-93281
M-93280
X-93280
```

Replay:

```bash
cd experiments/X-93280-phase-locked-two-row
python3 verify.py --json /tmp/x93280.json
cmp /tmp/x93280.json results/verification.json
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c integration/gpt56-pro-93280-content-sha256.txt
```

Expected verdict:

```text
PASS_X_93280_PHASE_LOCKED_TWO_ROW_CONSUMER
```

The replay authenticates finite algebra and targeted diagnostics only. It does
not prove `SCID_PL`, `LPTRP_23`, the analytic boundary-value theorem, Landau's
theorem, or RH.
