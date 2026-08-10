# X-90503 — Intrinsic Darboux pole-null replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay checks exact pole annihilation of the Darboux kernel, positivity of one finite evaluation Gram, the two pole moments, and inversion of `d^2/du^2-1/4` on a super-Gaussian pole-null test.

It does not prove the trace-class estimates, the global index theorem, or RH.
