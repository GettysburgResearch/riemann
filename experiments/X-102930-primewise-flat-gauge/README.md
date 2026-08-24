# X-102930 — Primewise flat complementary gauge

Standard-library replay for `L-102901--L-102904` and `T-102930`.

It checks:

```text
local complementary-temperature products;
coordinate flatness identities;
primewise energy minimization;
endpoint native/squared placement;
endpoint-color Walsh decomposition;
absence of a linear term in the midpoint-transfer gauge.
```

It does not prove `PCOI102930`, `SGIC102890`, `CTZD102897`, or RH.

Run:

```bash
python3 verify.py --output results/verification.json
```
