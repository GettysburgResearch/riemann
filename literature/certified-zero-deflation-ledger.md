# Certified-zero-deflation transfer ledger

## Imported theorem shapes

1. **Lagarias positive-real criterion / zero resolvent.** Under RH, `xi'/xi` in
   the shifted right half-plane is a positive sum of critical-line Poisson
   kernels. This is the parent interface already recorded by D-3201/L-3201.
2. **Nevanlinna-Pick Gram kernel.** Under RH, finite Pick matrices are sums of
   rank-one zero resolvents, as recorded by L-3202.
3. **Hardy-Z sign changes.** A directed sign change on the critical line gives a
   finite lower zero count by continuity, without a completeness assertion.
4. **Deflation and model reduction.** Numerical linear algebra routinely removes
   known spectral components before resolving a residual. The repository
   transfer is proof-oriented: subtract only rigorous lower positive components,
   so no modeled or approximate zero enters the final sign.

## Repository novelty claim

No priority claim is made for zero-resolvent expansions or Hardy-Z methods. The
contribution is the finite RH-witness calculus that combines:

- independently certified lower critical-line zero counts;
- exact lower Poisson/Gram contribution bounds;
- direct outward `xi'/xi` primitives;
- strict residual sign certificates;
- uncertainty-closed and conic-portfolio replay.

## Source-audit blocker

Before any theorem status promotion, independently reconstruct the exact
D-3201/L-3201 product normalization and the Hardy-Z phase convention used by the
chosen producer. The elementary subtraction lemmas themselves are included in
full in L-8401–L-8404.
