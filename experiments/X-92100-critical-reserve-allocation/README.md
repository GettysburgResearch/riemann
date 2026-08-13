# X-92100 — Verified critical-line curvature check

This replay checks the exact rational identities in `L-92101` and the coarse
global estimate in `L-92102`.

## Run

```bash
python3 verify.py --json /tmp/verification.json
cat /tmp/verification.json
```

Expected verdict:

```text
PASS_CRITICAL_RESERVE_ALLOCATION
```

The checker verifies the orbit formula, the cross-term factorization, the
nonnegative combined curvature, the `9m/b^2` estimate, and the coarse global
bound at the declared verified height.

It does not replay the external zero verification, prove the grouped Hadamard
limit, or prove RH.
