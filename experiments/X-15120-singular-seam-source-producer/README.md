# X-15120 — Source-bound singular-seam quartic producer

This experiment assembles one finite singular-seam row from concrete source
matrices and fails closed when the public source package is incomplete.

## Files

```text
produce.py
certificates/
  shimizu-public-source-v8-v6-audit.json
  synthetic-complete-row.json
results/
  shimizu-public-source-v8-v6-audit.json
  synthetic-complete-row-verification.json
  tests.txt
tests/test_produce.py
```

## Run

```bash
python produce.py certificates/shimizu-public-source-v8-v6-audit.json
python produce.py certificates/synthetic-complete-row.json
python -m unittest discover -s tests -v
```

## Retained verdicts

The public-source manifest returns:

```text
SOURCE_SPECIFICATION_INCOMPLETE
missing_count = 17
```

The synthetic control returns a complete exact row and is visibly not Riemann
data.  It tests only the chain assembly, source-metric formulas, basis
invariance, target comparison, and validation rules.

The producer never fills missing maps from defaults and never treats a
synthetic or floating row as an actual source result.
