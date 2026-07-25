# Run the direct xi-modulus scan

This marker launches `.github/workflows/arb-xi-modulus.yml` from a base branch
that already contains the workflow definition.

The workflow evaluates nine exact dyadic horizontal points at the common exact
ordinate

```text
20225875608343121406355 / 2^32
```

using direct completed-xi Arb rectangles at 192 and 256 bits. It checks all 22
declared monotonicity, divided-difference, and integer-power shape rows and
requires coordinatewise precision nesting.

No counterexample is asserted by this marker. A strict negative directed row
would be a rigorous nomination pending independent special-function
reproduction and analytic review of L-7501.
