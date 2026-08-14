# X-91671 — final single-SHARP dependency and lock validator

This validator is fail-closed for the repository state of `T-91656`.

It checks:

```text
all local dependency paths exist;
all local Git blob hashes match the final manifest;
all identifiers and paths are unique;
no placeholder blob is present;
R-91659/L-91670/L-91671/T-91656 are load bearing;
L-91668/L-91669/T-91655 are forbidden as live proof inputs;
R-91658 is retained as a scope firewall;
the X-91670 result has the required classification and proof object;
external source commits and blobs have valid immutable forms;
the manifest names the single-SHARP normalization and equality-deficit ledger.
```

Run from the repository root:

```bash
python3 experiments/X-91671-final-single-sharp-lock/verify.py \
  --manifest integration/2026-08-14/t91656-dependency-manifest.json \
  --json experiments/X-91671-final-single-sharp-lock/results/verification.json
```

A PASS result certifies the declared repository freeze only. It does not prove
the mathematics or RH.
