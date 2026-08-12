# X-91118 — Canonical rough-child source partition

Companion exact replay for `L-91330/L-91331`.

```bash
python3 experiments/X-91118-canonical-rough-child-source/verify.py
```

Expected verdict:

```text
PASS_CANONICAL_ROUGH_CHILD_SOURCE_PARTITION
```

The checker uses exact arithmetic in `Q[r]/(r^2-1/p)` and verifies the
canonical-child identity, the factor-54 contraction for representative rough
primes, and the inherited `3/5` SHARP-source Hall margin. It does not certify
the parallel least-prime source partition or RH.
