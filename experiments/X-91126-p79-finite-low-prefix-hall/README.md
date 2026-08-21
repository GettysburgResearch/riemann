# X-91126 — Exact finite `P_79` low-prefix Hall certificate

This standard-library checker proves the finite part of `L-91347`.

It enumerates every odd squarefree `P_79` threshold below `4096`, every child
activation cell on `1<=y<83`, the prime-switch curve `y=t/83`, and both source
channels:

```text
a=4  SHARP target;
a=5  endpoint score.
```

The support derivative in `sqrt(p)` is signed by the positive terminal child
Hall margin, reducing all real `p>=max(83,t/y)` to the smallest admissible
value.  The remaining `sqrt(y)` dependence is affine or quadratic and is checked
at exact endpoints and, when needed, its global convex critical point.

Replay:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_P79_FINITE_LOW_PREFIX_TARGET_AND_SCORE_HALL
```

Scope firewall: this certifies the two Hall problems separately.  It does not
identify one common two-ledger flow, certify the inherited row correction, or
prove RH.
