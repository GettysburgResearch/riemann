# X-15603 — Exact dimension-only weighted-index refutation

This experiment is the finite regression for `R-15601`.

It verifies an exact two-dimensional model in which

```text
weighted threshold index = 1
source packet dimension  = 1
```

but the source packet is orthogonal to the weighted-deficit direction. The
uncaptured trace is therefore

```text
1 > kappa = 1/2.
```

Thus a dimension comparison alone cannot prove the leverage trace-tail or the
complement floor.

## Run

```bash
python verify.py certificates/synthetic.json \
  --output /tmp/verification.json
python -m unittest discover -s tests -v
```

## Exact result

```text
threshold index             1
source dimension            1
dimension comparison        true
captured trace              0
uncaptured trace            1
required threshold          1/2
verdict                     REFUTED_DIMENSION_ONLY_WEIGHTED_INDEX_COMPARISON
```

The proof-object SHA-256 is

```text
e9b4cf2fcf4be0d6c0a9d20108bf98a48a222108bece992747c97bf9f436321c
```

This is an exact synthetic counterexample to a proposed abstract implication,
not a Riemann-zeta counterexample.
