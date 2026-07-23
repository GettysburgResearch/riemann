# Full target run trigger

This child commit exists solely to launch the pull-request workflows whose base
already contains both directed target definitions:

- `.github/workflows/target-directed-toeplitz.yml`;
- `.github/workflows/target-directed-toeplitz-arm.yml`.

Target:

```text
c = 10^11
T = 4709203636353.65
K = 1024
50 complete directed coverage shards
```

The x86-64 and ARM64 jobs use the same MPFR inclusion contracts but independent
instruction sets and runner pools.  No mathematical claim is made by this
marker.  The uploaded final rational interval is the only sign decision.
