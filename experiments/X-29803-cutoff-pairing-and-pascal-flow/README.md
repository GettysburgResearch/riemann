# X-29803 — Cutoff pairing and nonnegative Pascal-flow regression

Run:

```bash
python experiments/X-29803-cutoff-pairing-and-pascal-flow/verify.py
```

Expected classification:

```text
EXACT_CUTOFF_PAIRING_AND_NONNEGATIVE_PASCAL_FLOW_VERIFIED
```

Exact finite counts:

```text
first-omitted index rows            16,511
single unmatched odd collar rows    10,712
paired pure-power jet rows          792,528
central/sibling carry rows           33,024
mutation tests                            1
```

Result digest:

```text
59fae15a93c4643c0a305dae8838f33ef27104cf303455e153180cfe04a2c3da
```

The checker proves only finite integer/rational source arithmetic. It does not certify the shifted Taylor superposition, all common destinations, the polylog collar capacity, DCD, the prime-ramp estimate, or RH.
