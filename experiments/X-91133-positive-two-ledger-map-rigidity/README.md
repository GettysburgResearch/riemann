# X-91133 — Positive two-ledger map rigidity

Companion replay for `L-91356`.

```bash
python3 experiments/X-91133-positive-two-ledger-map-rigidity/verify.py
```

Expected verdict:

```text
PASS_POSITIVE_TWO_LEDGER_MAP_RIGIDITY
```

The checker uses exact `Fraction` arithmetic to exercise the classified family

```text
M=[[1,b],[0,1-b/2]], 0<=b<=2,
```

and verifies that exact score conservation forces `b=0`, hence `M=I`. The universal classification is symbolic. The replay does not prove packet typing or RH.
