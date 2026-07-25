# X-9302 — Total-count zero deflation for direct-xi modulus witnesses

This experiment implements L-9303. It replaces individually isolated
critical-line zeros by unconditional **total zeta-zero counts** in nested exact
windows about one ordinate.

Under the RH hypothesis, every zero counted by the Turing/argument-principle
primitive lies on the critical line. The nested total counts therefore become
the order-statistic bounds required by L-9302. A strict negative deflated row
contradicts RH, even though the count producer never assumes RH and never labels
an individual zero as a line zero.

## Why this changes the production problem

The parent PR #96 requests up to 128 individually isolated Hardy-`Z` zero balls.
X-9302 changes the proof interface: it needs two total-count evaluations per
radius and handles multiplicity without identifying individual roots:

```text
M(R) = N(T+R) - N(T-R).
```

The count includes multiplicity automatically. Nested counts are converted into
shell increments

```text
d_k = M(R_k) - M(R_{k-1})
```

and the checker subtracts

```text
sum_k d_k log(u + R_k^2)
```

from the direct completed-xi logarithmic modulus. No wall-clock speedup is
claimed before the FLINT implementations are benchmarked.

## Files

- `verify_total_count_deflation.py` — independent integer/Fraction checker;
- `build_pr71_total_count_certificate.py` — binds direct-xi rectangles and
  Turing count balls;
- `flint_pr71_nested_total_counts.c` — exact PR #71 total-count producer at
  radii `1/32,...,8`;
- `compare_total_count_precision.py` — count and ball nesting gate;
- `compare_total_deflation_precision.py` — primitive and final-row nesting gate;
- `certificates/synthetic-total-count-hidden-offline.json` — exact masked
  off-line synthetic control;
- `tests/` — mutation and end-to-end adapter tests.

## Exact synthetic control

For

```text
H(u) = (u-5)^2 (u+1)^20
```

an unconditional lower count of twenty zeros within radius one licenses removal
of the `(u+1)^20` background under the synthetic RH model. Both raw rows are
positive, while both deflated rows are strictly negative:

```text
raw monotonicity      CERTIFIED_NONNEGATIVE
deflated monotonicity CERTIFIED_NEGATIVE
raw Loewner           CERTIFIED_NONNEGATIVE
deflated Loewner      CERTIFIED_NEGATIVE
```

Thirteen exact tests pass. They reject decreasing counts, nonincreasing radii,
wrong semantic gates, Boolean counts, false point digests, ambiguous count
balls, endpoint drift, false count differences, and nonnested totals.

## PR #71 production

The workflow evaluates the exact ordinate

```text
20225875608341108140435 / 2^32
```

at 192 and 256 bits. It obtains unconditional total counts in nine nested
dyadic windows, reuses the inherited nine-point direct completed-xi primitive
table, checks the division-free two-point rows and cross-Loewner determinants
through order four, and requires precision nesting.

No production output is committed yet. A negative row is only a nomination
pending independent total-count and completed-xi reproduction plus review of
the analytic normalization. A wholly nonnegative run excludes only the declared
finite table.

## Local verification

```bash
python -m compileall -q .
python -m unittest discover -s tests -v
python verify_total_count_deflation.py \
  certificates/synthetic-total-count-hidden-offline.json \
  --output /tmp/synthetic-result.json
```

The last command intentionally returns status `1` because the synthetic
certificate contains strict negative rows.
