# X-91687 — Exact `P_61` causal target/score Hall replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The verifier uses integer/Fraction-style fixed-denominator outward square-root intervals. It checks both sides of every child and parent activation cell, all finite rough primes below the threshold-dependent tail boundary, the real tail boundary, and the child margins needed for monotonic extension to all larger primes.

It proves target and score Hall feasibility on the same displacement-eight graph. It does not prove that one common flow has favorable target, score, and all component-row gains.
