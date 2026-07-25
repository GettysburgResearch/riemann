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

at 192 and 256 bits. It checks 22 monotonicity, second-difference, and
three-point multiplicative shape rows, plus ten L-7503 odd-order logarithmic
localizers of orders three and five. The latter cancel polynomial background in
`log |xi|^2` through degrees two and four. Every 256-bit primitive coordinate
rectangle must be nested in its 192-bit predecessor.

The ordinary reconnaissance block was increasing and convex, so this run is a
proof-grade closure/regression pass rather than a midpoint counterexample
nomination. No counterexample is asserted by this marker. A strict negative
directed row would be a rigorous nomination pending independent special-function
reproduction and analytic review of L-7501--L-7503.
