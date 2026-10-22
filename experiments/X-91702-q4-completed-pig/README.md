# X-91702 — Exact complete-endpoint Q4 PIG replay

Arithmetic class: `EXACT_RATIONAL_WITH_FORMAL_LOG4`  
Claim exercised: `T-93010`

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The checker verifies the complete cell-field mean formula, the exact variance
identity that coerces the mean by the positive endpoint energy, the elementary
termwise Mellin kernel, and the finite scale-four source transform. It includes
reflection and scale-factor mutations.

It does **not** prove the von Koch estimate, analytic continuation, zero safety,
the endpoint PIG bound, or RH.
