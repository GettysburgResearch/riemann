# X-95050 — Positive scale-four divisor compiler

```bash
python3 verify.py --json /tmp/x95050.json
cmp /tmp/x95050.json results/verification.json
sha256sum -c SHA256SUMS
```

The checker uses exact integers and formal prime-log coefficient maps. It does not prove a subpower capacity theorem, the Q4 mean bound, or RH.
