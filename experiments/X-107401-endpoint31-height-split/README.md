# X-107401 — Endpoint-31 height split replay

Run:

```bash
python3 verify.py
```

The replay checks the exact defect-to-height factor \(1/4\), the deep-charge
formula, the \(37/500\) shallow allowance, and the additional
\(897/15500\) source-transfer room.

It does not prove either shallow transfer gate, more than \(90\%\), or RH.
