# X-100103 — DCE/QPET hostile-disposition replay

This standard-library replay checks only the exact finite algebra and logical
interfaces used by `L/T/R-100103`:

```bash
python3 experiments/X-100103-dce-qpet-disposition/verify.py
```

Expected:

```text
PASS_T100103_DCE_QPET_HOSTILE_DISPOSITION
3c618fef8ef4f3012dfdb636be22dbe9c37736a0b5765e44b4f21a1a15070e86
```

It verifies:

- `DCE_(p,Y)` is exactly predecessor nonnegativity under the frozen recurrence;
- a corridor valid for every `A<A*` forces `liminf exponent >= A*`;
- the QPET strict reverse inequality is rejected;
- a superlarge selected residue in a bounded completed scalar forces a
  comparably large complementary term.

The replay does not prove DCE, RH, or any moving-cutoff explicit formula. Its
result object is fail-closed.
