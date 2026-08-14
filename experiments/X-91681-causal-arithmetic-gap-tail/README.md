# X-91681 — Exact causal arithmetic-gap tail replay

This experiment verifies the directed finite gate in `L-91681`.

## Run

```bash
python experiments/X-91681-causal-arithmetic-gap-tail/verify.py
```

Expected classification:

```text
PASS_CAUSAL_ARITHMETIC_GAP_TAIL
```

The checker uses only:

```text
Python integer arithmetic;
fractions.Fraction;
integer-square-root enclosures;
positive-tail atanh series for logarithms.
```

No binary floating-point value is used in a sign decision. The decimal values in `results/verification.json` are display-only conversions of already-positive exact rational intervals.

## Certified statement

For every row `2<=j<=66`, the verifier proves at `p=500000`

```text
log(66/65) A_j(p)/(50 sqrt(67p)) - B_j/(p-1) > 0.
```

The analytic monotonicity in `L-91681` extends the inequality to every real `p>=500000`. Together with `L-91359`, this gives strict divisor ordering of the causal row-per-score profile on the complete unbounded rough-prime tail.

## Scope firewall

The replay does not certify:

```text
the finite corridor 67<=p<500000;
the full even/odd packet determinant;
the target-proportional score determinant;
the aggregate score-debt estimate;
BARC;
RH.
```

The retained digest commits the exact rational lower margins for all 65 rows.
