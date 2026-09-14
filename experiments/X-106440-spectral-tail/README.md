# X-106440 — Spectral asymmetry and in-band hole replay

Run:

```bash
python3 experiments/X-106440-spectral-tail/verify.py \
  --output experiments/X-106440-spectral-tail/results/verification.json
```

Expected classification:

```text
PASS_T106440_SPECTRAL_ASYMMETRY_HOLE_SPLIT
```

The replay checks exact finite Fourier/Hankel algebra:

- the hard-band coarea formula;
- the orthogonal outer-tail / in-band-hole split;
- the favorable sign for an inner monomial;
- the quadratic distinction between a safe vertical shift and a derivative companion;
- the rational `90%` budget ledger.

It does **not** evaluate Xi, authenticate the analytic input imported from PR
#729, prove `OUTASYM106440`, prove `INHOLE106440`, prove `SAFEHOM106441`, or
establish `90%`, density one, or RH.
