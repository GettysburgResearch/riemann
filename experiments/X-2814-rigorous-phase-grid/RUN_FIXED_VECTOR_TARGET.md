# Run the complete fixed-vector target

This marker launches `.github/workflows/target-fixed-vector-single-host.yml` from
a base branch that already contains the workflow definition.

The job evaluates the preserved exact 96-bit vector

```text
vector SHA-256  3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
c                  10^11
T                  94184072727073 / 20
K                  1024
precision          192 bits
workers            4 internal processes
complete terms     4,118,082,969
```

It then assembles the exact alpha and prime intervals, applies the rational
nonprime correction, and emits one strict positive, negative, or unresolved
verdict.  No sign claim is made by this marker.
