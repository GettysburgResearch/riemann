# Run the PR #71 zero-deflated direct-xi certificate

This child commit exists solely to launch
`.github/workflows/pr71-zero-deflated-modulus.yml` from a base branch that
already contains the proof-producing workflow.

The workflow binds two independent directed inputs at the exact ordinate

```text
20225875608341108140435 / 2^32
```

1. consecutive Hardy-Z zero balls and Turing total-zero counts from the exact
   X-5603 PR #71 gap producer;
2. direct completed-xi rectangles at nine exact dyadic horizontal offsets from
   the X-7501 Riemann-Siegel backend.

It evaluates both inputs at 192 and 256 bits, requires precision nesting, builds
two certified zero bins of multiplicity at least one, and checks twenty
zero-deflated monotonicity and logarithmic Loewner rows.

No sign is asserted by this marker. A strict negative row or a positive
line-empty-slab zero discrepancy is only a counterexample nomination pending
independent backend reproduction and analytic review.
