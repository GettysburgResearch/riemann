# Run the direct xi-modulus scan

This marker launches `.github/workflows/arb-xi-modulus.yml` from a base branch
that already contains the workflow definition.

The production backend now uses FLINT's rigorous Riemann--Siegel zeta routine and
the direct completed-xi product, not generic high-height zeta evaluation. It
evaluates nine exact dyadic horizontal points at the common exact ordinate

```text
20225875608343121406355 / 2^32
```

at 192 and 256 bits. It checks all 22 declared monotonicity,
divided-difference, and integer-power shape rows and requires coordinatewise
precision nesting.

No counterexample is asserted by this marker. A strict negative directed row
would be a rigorous nomination pending independent special-function
reproduction and analytic review of L-7501.
