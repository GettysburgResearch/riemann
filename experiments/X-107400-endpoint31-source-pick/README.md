# X-107400 — Endpoint-31 source-Pick reduction replay

Run:

```bash
python3 verify.py
```

The replay authenticates:

- the exact Conrey \(m=31\) certificate;
- the \(1/(2K)\) central source constant;
- the \(K=31\) \(90\%\) budget;
- finite-grid Hardy radial/input transference;
- the unit-index firewall.

It does not prove `XI31TRANSFER107400`, more than \(90\%\), density one, or RH.
