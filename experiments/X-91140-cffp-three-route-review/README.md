# X-91140 — CFFP three-route review regressions

Companion exact replay for:

```text
L-91370  first activation-strip domination;
T-91311  subcritical packet-envelope factor;
L-91372  butterfly dual / convex-potential identity.
```

Run:

```bash
python3 experiments/X-91140-cffp-three-route-review/verify.py
```

Expected:

```text
PASS_CFFP_THREE_ROUTE_REVIEW
```

The checker uses only the Python standard library and exact `Fraction` arithmetic. It does not certify the global canonical-row theorem, the literal entropy theorem on PR #437, CFFP, or RH.

`X-91140` supersedes the malformed retained JSON under provisional `X-91139`.
