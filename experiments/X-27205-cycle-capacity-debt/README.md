# X-27205 — Cycle capacity-debt regression

This standard-library/Fraction checker verifies the finite algebra behind
`L-27205`:

- exact target divergence and carry reconstruction;
- invariance under balanced fundamental Pascal cycles;
- capacity baseline identity for arbitrary positive column weights;
- total variation equals baseline plus twice negative debt;
- weak duality for bounded-superadditive potentials;
- fail-closed cycle mutation.

The retained checker uses the rational surrogate column weight `y_q=1/q` so
all arithmetic is exact. The theorem permits arbitrary positive `y_q`; the RH
consumer uses `y_q=q^(-1/2)` together with the analytic comparison in
`L-27205`.

Run:

```bash
python verify.py
python -m unittest discover -s tests -v
```

Scope: finite linear algebra only. The checker does not prove the cofinal Cycle
Debt Theorem, MFT, or RH.
