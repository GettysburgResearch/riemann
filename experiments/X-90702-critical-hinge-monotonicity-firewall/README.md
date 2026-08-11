# X-90702 — critical-hinge monotonicity firewall

This standard-library checker verifies the exact top-inverse cone and the
directed \(T=894\) counterexample to indefinite recursive residual monotonicity.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90702_CRITICAL_HINGE_MONOTONICITY_FIREWALL
```

The radical certificate uses exact rational pullback through the triangular
elimination maps and integer-square-root enclosures with denominator \(10^{60}\).
It does not prove or refute Critical Hinge Saturation or RH.
