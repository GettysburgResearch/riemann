# X-106150 — Corrected Wick equal-pair half-source square

Standard-library exact replay for:

- Boolean half-source square;
- canonical equal-pair Beta/Wick coefficient;
- owner-exclusion functoriality;
- ordinary versus Boolean/Wick source multiplication;
- exact overlap-contraction decomposition;
- common-mother differential Wick self-convolution;
- CV, XD, outer and derivative-outer multiplier images.

Run:

```bash
python3 verify.py
```

Expected:

```text
PASS_X_106150_WICK_EQUAL_PAIR_HALF_SOURCE_SQUARE
exact_checks=47263
proof_object_sha256=d0cec21f67433559415ee8a62af24db4829606b87b10ed5f5933a406d8004390
```

The replay does not prove `WKSFSC106150`, `SFSC106150`, `REFEV106150`,
`REFOD106150`, `CBKM106130`, `BCI102990`, or RH.
