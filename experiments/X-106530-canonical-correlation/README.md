# X-106530 — Endpoint canonical-correlation replay

Run:

```bash
python -B experiments/X-106530-canonical-correlation/verify.py
```

Expected classification:

```text
PASS_T106530_CANONICAL_CORRELATION_DEFICIT
```

The replay checks with exact rational arithmetic:

- the one-factor identity
  `charge=((a-b)/(1-a*b))^2`;
- all Cauchy-Gram overlap identities for distinct real zero sets of sizes up
  to four on a seven-point grid;
- positivity, dimension-mismatch lower bounds and identical-space zero charge;
- pure favorable versus pure adverse inner orientation;
- the fifth-endpoint allowance `997/1000-9/10=97/1000`.

It does not compute Xi companion zeros, prove `CANONCORR106530`, establish
ninety percent, or prove RH.  The verifier writes its exact result and
proof-object digest to `results/verification.json`.
