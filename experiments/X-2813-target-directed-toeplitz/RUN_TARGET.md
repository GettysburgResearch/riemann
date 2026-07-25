# Full target run trigger

This child commit launches the quota-safe single-host calculation defined in
`.github/workflows/target-directed-toeplitz-single.yml`.

One hosted runner starts eight disjoint MPFR worker processes internally. Each
worker covers 50 of the 400 half-open integer segments, so the run evaluates the
entire cutoff without asking GitHub to schedule a large matrix of hosted jobs.

Target:

```text
c = 10^11
T = 4709203636353.65
K = 1024
8 directed super-shards
400 complete integer segments
96-bit frozen vector after post-selection
```

This marker was refreshed after the single-host workflow was installed on the
base branch. The job uploads partial shard and diagnostic files even if a worker
fails. No mathematical claim is made by this marker. The exact final rational
interval is the only sign decision.
