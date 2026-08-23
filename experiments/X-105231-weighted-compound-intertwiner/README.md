# X-105231 — Weighted de Branges/Fourier compound fixtures

Run

```bash
python3 experiments/X-105231-weighted-compound-intertwiner/verify.py
python3 -m unittest discover \
  -s experiments/X-105231-weighted-compound-intertwiner/tests \
  -p 'test_*.py' -v
```

The standard-library exact replay checks:

- weighted scalar variance;
- the explicit residue projection from Fourier exterior samples;
- the pair-bundle Cauchy estimate;
- the centered Gram trace identity;
- a rational spectral-equality fixture;
- the diagonal/trace firewall;
- the `9/25` integrality threshold sanity check.

It does not evaluate Xi, prove weighted moment finiteness, prove
`WSEG105231`, close the endpoint/winding ledger, or prove RH.
