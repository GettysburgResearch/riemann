# X-106710 — Carrier-adapted antiphase source softening

Run:

```bash
python experiments/X-106710-carrier-adapted-antiphase/verify.py
```

The replay checks the fixed-scale decomposition, the nonnegative odd-order
coefficient proof through order fifteen, the exact fifth-order positive gap,
and the conditional fifth-order ratio algebra.

Expected marker:

```text
PASS_T106710_CARRIER_ADAPTED_ANTIPHASE_SOURCE_SOFTENING
```

The replay does not prove the physical scale bridge, the full source-Pick
free-energy estimate, ninety percent, density one, or RH.
