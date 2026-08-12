# X-91125 — P79 one-prime inherited-row splice

Companion directed replay for `L-91346`.

```bash
python3 experiments/X-91125-p79-one-prime-row-splice/verify.py
```

Expected verdict:

```text
PASS_P79_ONE_PRIME_ROW_SPLICE
```

The checker certifies:

- all `2^22` finite `P_79` prefix states, including
  `beta_79 < 1/700`, `|M_79| < 36/25`, and the centered spline bound
  `|E_79| < 269/200`;
- the finite boundary-functional geometry for every inherited row
  `2 <= j <= 82`;
- the compact `p=83` spline, logarithmic-Lipschitz, and Green-bulk gates;
- the `p=89` Green-bulk gate used for every `p >= 89` by monotonicity;
- the exact rational margins in the two analytic comparison regimes.

All square roots use exact integer enclosures. Logarithms use the standard
library's correctly rounded `Decimal.ln` with thirty guard digits and a further
two-unit outward enlargement at the retained denominator. The global scan and
all comparisons are directed.

The replay proves the inherited-row inequality in `L-91346`. It does not prove
the remaining bounded low-prefix target-transport theorem or RH.
