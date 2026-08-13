# X-91411 — Reciprocal-limit shifted-eight transport moment

Status: **EXACT FINITE CERTIFICATE; ANALYTIC TRANSFER SEPARATE**

The fully activated normalized causal score measures have source weights `1/d` on the `P_61` divisors.  Because every divisor divides `P_61`, all masses are exact integer units in the common denominator `P_61`.

The checker:

1. verifies every radius-eight prefix margin exactly;
2. constructs the exact left-greedy transport in integer units;
3. evaluates its square-root moment with outward rational intervals;
4. proves the prefix moat is above `1/100` and the moment is above `18`.

Run:

```bash
python3 verify.py
```

Retained verdict:

```text
PASS_P61_RECIPROCAL_LIMIT_HALL_MOMENT
```

The checker does not prove the separate finite-parameter perturbation estimate and does not prove RH.

SHA-256:

```text
verify.py                   b411ad53e4c29ad693e55f76f5bcac196f0b9201fb629b95d0c050207ce30775
results/verification.json   1df1e8ae42cb7cb31c53b7af51d4fa955cb556b62e4a0d99c76ed96e31832f3e
```
