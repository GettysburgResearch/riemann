# Full target run trigger

This child commit exists solely to launch the directed target workflows whose
base already contains their definitions.  The quota-compatible production path
is:

- `.github/workflows/target-directed-toeplitz-paired.yml`.

It uses exactly two hosted jobs.  Each job runs four disjoint MPFR subshards
internally, so all 200 half-open coverage segments are evaluated without asking
GitHub to schedule more than two jobs at once.

Target:

```text
c = 10^11
T = 4709203636353.65
K = 1024
8 directed super-shards
200 complete integer segments
```

No mathematical claim is made by this marker.  The uploaded final rational
interval is the only sign decision.
