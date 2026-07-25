# Run the direct xi-modulus scan

This marker launches `.github/workflows/arb-xi-modulus.yml` from a base branch
that already contains the workflow definition.

The production backend uses FLINT's rigorous `acb_dirichlet_zeta_jet_rs`
routine and the direct completed-xi product, not generic high-height zeta
evaluation. It evaluates nine exact dyadic horizontal points at the common exact
ordinate

```text
20225875608343121406355 / 2^32
```

at 192 and 256 bits. It checks all 22 declared monotonicity,
divided-difference, and integer-power shape rows and requires coordinatewise
precision nesting.

The ordinary reconnaissance block was increasing and convex, so this run is a
proof-grade closure/regression pass rather than a midpoint counterexample
nomination. No counterexample is asserted by this marker. A strict negative
directed row would be a rigorous nomination pending independent special-function
reproduction and analytic review of L-7501.
