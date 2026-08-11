# X-90706 — signed linear-hinge response

This exact `Fraction` replay supports `L-90705` and `R-90704`.

It verifies:

- the linear-hinge extreme-ray decomposition of decreasing-convex targets;
- the complete `E=60` average-carry inverse row by row;
- the exact negative response `a_60(11)=-2/55`;
- positive neighbouring responses `53/45` and `131/33`.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90706_SIGNED_LINEAR_HINGE_RESPONSE
```

The replay does not prove the square-root weighted cancellation, CHS, or RH.
