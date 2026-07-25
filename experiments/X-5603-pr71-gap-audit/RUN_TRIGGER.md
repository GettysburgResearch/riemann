# Trusted-base execution trigger

This file exists only to trigger `.github/workflows/pr71-rigorous-gap.yml` from a
base branch that already contains the workflow definition.

The workflow uses FLINT's directed Platt/Turing routines at the exact PR #71
dyadic ordinate. It attempts two finite decisions:

1. isolate consecutive total-zeta-zero balls around the target;
2. construct an exact critical-line-empty slab and compute
   `N(b)-N(a)` with multiplicity.

A positive discrepancy is the `L-5605` RH-disproof predicate pending independent
backend reproduction. A zero discrepancy certifies only that exact interior slab
is empty. No sign is claimed by this trigger file.
