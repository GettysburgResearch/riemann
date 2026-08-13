# X-91651 — corrected provenance-envelope algebra replay

This is a small exact-rational regression for `T-91652`.  It checks:

- the nonduplicating reset coefficients;
- cancellation of each contracted child inside its causal difference;
- total recursive coefficient mass below `1/8`;
- the geometric packet-envelope bound;
- the root mass-54 composition arithmetic;
- the one-sided endpoint threshold logic;
- a finite structural replay of the least-prime rough-reservoir partition;
- shape and uniqueness of selected frozen blob identifiers.

It does **not** replay the expensive finite Hall, B-spline collar, mismatch,
terminal omission, or endpoint-port certificates.  Those are the explicit
independent-review boundary in `L-91659` and the full-ledger lock.

Run:

```bash
python3 verify.py --json results/verification.json
```

Expected verdict:

```text
PASS_CORRECTED_PROVENANCE_ENVELOPE_ALGEBRA
```
