# X-zeta23-terminal-resolvent

Finite regression for the terminal resolvent-derivative hierarchy.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected final line:

```text
PASS_TERMINAL_RESOLVENT_DERIVATIVE_HIERARCHY
```

The verifier checks rational-kernel algebra, Laplace moments, alpha
derivatives, the safe-Euler inverse-Gaussian identity, line/target signs,
normalization, the exact Abel/Euler gap, a synthetic terminal packet,
a line-only moment-Hankel Gram, terminal Hankel-diagonal failure, and far-zero
decay.

It does **not** prove the contour shift, terminal-pair theorem, complete zero-sum
limit, RH criterion, or the Riemann Hypothesis.  Those statements are in the
accompanying proof note and require independent review.
