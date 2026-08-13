# X-92100 — Verified critical-line reserve allocation

This replay checks the exact rational algebra in `L-92101` and the coarse
global budget in `L-92102`.

## Run

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_CRITICAL_RESERVE_ALLOCATION
```

## Exact gates

The checker verifies:

1. the off-line curvature formula;
2. the exact cross-curvature factorization;
3. positivity after the declared reserve fraction;
4. the `9m/b^2` high-orbit bound on a rational control;
5. the exact coarse global budget
   
   ```text
   18(log H+1)/H < 18*31/H < 1
   ```
   
   for `H=3,000,175,332,800`, using `log H<30`.

The experiment does not replay the Platt–Trudgian zero verification, prove the
centered Hadamard grouping, or prove RH.
