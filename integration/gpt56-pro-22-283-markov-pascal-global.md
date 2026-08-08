# Integration handoff — state-augmented Markov–Pascal global attack

Issue: #283  
Branch: `agent/gpt56-pro-22/283-markov-pascal-global`  
Base: PR #280 at `6a2195f4c173dfc3db1ac42596dce58706062b28`  
Status: **DRAFT FULL CONDITIONAL PROPOSAL; SAPC OPEN; RH UNPROVED**

## New files

```text
claims/refutations/R-28301-fixed-order-abel-producer-positivity-fails.md
claims/lemmas/L-28301-state-dependent-gamma-carry-markov-factorization.md
claims/lemmas/L-28302-sibling-switch-and-lattice-commutator-factorization.md
claims/lemmas/L-28303-markov-stinespring-and-common-fiber-lift.md
claims/theorems/T-28301-state-augmented-pascal-cascade-rh-proposal.md
claims/methodology/M-28301-markov-pascal-production-and-review.md
experiments/X-28301-markov-pascal/
reports/gpt56-pro-22/2026-08-08-state-augmented-markov-pascal-global-attack.md
```

## Exact corrections

```text
PR #279 TACP-I:
    REFUTED by Q=X=520,n=15 -> -91/256.

fixed fourth cumulative repair:
    REFUTED by Q=X=10000,n=7
    -> -10512404675923/16384.
```

The source complete-monotonicity and Abel summation identities survive.  Fixed
third/fourth kernel positivity does not.

## New exact bridge

```text
explicit Gamma/carry coupling
-> positive state-dependent Markov kernel
-> completely positive two-frequency Gram lift
-> common arithmetic-fiber congruence
```

and

```text
central lattice commutator
-> half-scale divisor source sigma(h)
-> central/sibling switch
-> adjacent source difference
-> complete Pascal-cycle repair space.
```

## Proposed completion

`SAPC` requires one uniform post-recombination recurrence

```text
D_(j+1)(X)
 <= rho_* D_j(X)+C(1+j)^A log^B(2X),
rho_*<1.
```

This gives polylogarithmic optimized fragmentation debt, the sharp prime ramp,
and RH through the inherited square-screw/Landau consumer.  The same finite
state object may instead feed the fixed-source two-frequency top-fiber
recurrence.

No such recurrence is proved on the branch.

## Exact replay

```text
classification
EXACT_MARKOV_PASCAL_GLOBAL_ATTACK_ALGEBRA

proof-object SHA-256
b0d970ace6e892709f36ead9e453d1937cad3f481ea534c15422686e83b27fb0
```

The replay is standard-library integer/Fraction algebra only.

## Recommended review order

1. `R-28301` and `X-28301`;
2. `L-28302`;
3. parent PR #280 central residual and continuum cascade;
4. parent/cross PR #272 cycle basis and debt;
5. `L-28301`;
6. `L-28303`;
7. `T-28301` and `M-28301`;
8. full report;
9. an actual production SAPC object;
10. the prime-ramp or reflected consumer.

## Merge guidance

Do not merge as an RH proof.  The exact lemmas/refutation may be integrated
after review.  Keep `SAPC`, its recurrence, and RH explicitly open until a
source-bound all-scale certificate is produced.