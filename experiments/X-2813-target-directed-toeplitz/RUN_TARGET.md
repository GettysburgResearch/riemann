# Full target run trigger

This child commit launches the two-job directed calculation defined in
`.github/workflows/target-directed-toeplitz-paired.yml`.

Each hosted job evaluates four disjoint MPFR subranges internally. Together they
cover all 200 half-open integer segments for the target.

Target:

```text
c = 10^11
T = 4709203636353.65
K = 1024
8 directed super-shards
200 complete integer segments
```

No mathematical claim is made by this marker. The uploaded final rational
interval is the only sign decision.
