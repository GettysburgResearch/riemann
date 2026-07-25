# Complete-stack trusted-base execution trigger

This child change triggers the current `pr71-rigorous-gap.yml` workflow after the
full producer–checker stack has landed on the base branch.

The run must execute:

- exact rational / IEEE-754 provenance tests;
- the separate standard-library line-gap certificate checker tests;
- 128- and 192-bit FLINT Platt Hardy-Z isolation;
- 128- and 192-bit FLINT Turing total-zero counts;
- exact replay of both discrepancy certificates;
- cross-precision index, count, classification, and zero-ball nesting checks.

A positive even discrepancy is the finite `L-5605` RH-disproof predicate pending
independent primitive reproduction. A zero discrepancy proves only the exact
interior slab is empty. This trigger asserts no result.
