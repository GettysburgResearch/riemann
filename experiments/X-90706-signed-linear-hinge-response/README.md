# X-90706 — signed linear-hinge and geometric response

This exact `Fraction` replay supports `L-90705`, `R-90704`, and `R-90705`.

It verifies:

- the linear-hinge extreme-ray decomposition of decreasing-convex targets;
- the complete `E=60` average-carry inverse row by row;
- the exact negative response `a_60(11)=-2/55`;
- positive neighbouring responses `53/45` and `131/33`;
- the complete truncated-geometric inverse at `E=126`, `x=99/100`;
- the exact negative geometric response `g(9)≈-0.00066584534761921811`.

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
