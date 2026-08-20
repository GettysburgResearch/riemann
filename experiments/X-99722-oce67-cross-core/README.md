# X-99722 — OCE67 scope, diagonal closure, and prime-interval firewall

Run:

```bash
python3 experiments/X-99722-oce67-cross-core/verify.py \
  --output /tmp/x99722.json
```

Expected verdict:

```text
PASS_T99722_OCE67_SCOPE_DIAGONAL_AND_PRIME_INTERVAL_FIREWALL
```

The replay checks:

- 500 exact complex-valued convex first-owner inequalities;
- the exact 21-prime interval fixture at `X=200`;
- the rational compact-diagonal constant `<60`;
- fail-closed status for source-orbit OCE67 and RH.

It does not prove the cross-core Gram estimate, SOCE67, or RH.
