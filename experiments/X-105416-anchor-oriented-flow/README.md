# X-105416 — Anchor-renormalized oriented-flow replay

Run:

```bash
python -B experiments/X-105416-anchor-oriented-flow/verify.py \
  --output experiments/X-105416-anchor-oriented-flow/results/verification.json
```

Expected verdict:

```text
PASS_X_105416_ANCHOR_ORIENTED_FLOW
```

The checker uses exact `Fraction` arithmetic. It verifies on one odd and one
even rational polynomial fixture:

- the inverse-power polynomial-square primitive;
- source-anchor quadratic forms;
- noncentral shifted-critical zero velocities;
- exact `source + oriented zero flow = boundary reserve`;
- the moving-central-branch correction for even parity; and
- the affine polynomial outer-window remainder.

Retained count:

```text
44 odd checks
47 even/regularized checks
91 exact checks total
```

The replay does not evaluate Xi, prove the cofinal outer-phase gate, authenticate
the moving complex saddle, perform low-order reverse-Rolle descent, or prove
RH.
