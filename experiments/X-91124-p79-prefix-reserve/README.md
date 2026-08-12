# X-91124 — Exact `P_79` prefix reserve

This standard-library checker streams all `2^22` squarefree divisors of

```text
P_79 = product_(p<=79) p
```

without materializing the full divisor table. It certifies:

```text
raw reciprocal Hall prefix > 1/25 for every odd threshold t>=83;
8-shifted reciprocal prefix > 1/5000 for every odd threshold;
8-shifted inverse-square-root prefix < 3/2.
```

The reciprocal sums are exact integer comparisons over the common denominator
`P_79`. The square-root sum uses directed fixed-denominator intervals.

Run:

```bash
python3 verify.py
```

The checker does not prove the finite low-prefix upward-correction theorem or
RH.
