# Integrator patch: issue #3 literature atlas

Agent: `gpt56-03`  
Branch: `agent/gpt56-03/3-literature-claim-atlas`  
Date: 2026-07-22

This file avoids conflicting edits to root registries already bootstrapped on
agent #1's branch.  Apply or adapt these entries after that branch lands.

## `CLAIMS.md` rows

```markdown
| D-0301 | Definition | Standard zeta, xi, and zero conventions | PROPOSED | `gpt56-03` | `claims/definitions/D-0301-standard-xi-normalization.md` |
| L-0301 | Lemma | Xi-zero symmetry orbits | PROPOSED | `gpt56-03` | `claims/lemmas/L-0301-xi-zero-symmetry-orbits.md` |
| L-0302 | Lemma | Argument-principle zero count | PROPOSED | `gpt56-03` | `claims/lemmas/L-0302-argument-principle-zero-count.md` |
| L-0303 | Lemma | Rouché zero-count certificate | PROPOSED | `gpt56-03` | `claims/lemmas/L-0303-rouche-zero-count-certificate.md` |
| L-0304 | Lemma | Winding-number stability under uniform error | PROPOSED | `gpt56-03` | `claims/lemmas/L-0304-winding-number-stability.md` |
| L-0310 | Lemma | Compact support makes the prime-power sum finite | PROPOSED | `gpt56-03` | `claims/lemmas/L-0310-compact-support-finite-prime-sum.md` |
| L-0311 | Lemma | Finite Hermitian negativity has a rational witness | PROPOSED | `gpt56-03` | `claims/lemmas/L-0311-finite-hermitian-negativity-witness.md` |
| L-0320 | Lemma | Divisor and totient product formulae | PROPOSED | `gpt56-03` | `claims/lemmas/L-0320-divisor-totient-product-formulas.md` |
| L-0321 | Lemma | Robin exponent-swap dominance | PROPOSED | `gpt56-03` | `claims/lemmas/L-0321-robin-exponent-swap-dominance.md` |
| L-0322 | Lemma | Nicolas primorial recurrence | PROPOSED | `gpt56-03` | `claims/lemmas/L-0322-nicolas-primorial-recurrence.md` |
| L-0330 | Lemma | Speiser finite-certificate kernel | PROPOSED | `gpt56-03` | `claims/lemmas/L-0330-speiser-certificate-kernel.md` |
| L-0340 | Lemma | Li unit-circle geometry | PROPOSED | `gpt56-03` | `claims/lemmas/L-0340-li-unit-circle-geometry.md` |
| L-0360 | Lemma | Positive-time Newman witness | PROPOSED | `gpt56-03` | `claims/lemmas/L-0360-positive-time-newman-witness.md` |
| L-0370 | Lemma | Bounded-prime-sum dynamic program | PROPOSED | `gpt56-03` | `claims/lemmas/L-0370-bounded-prime-sum-dynamic-program.md` |
| T-0301 | Theorem import | Robin criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0301-robin-criterion.md` |
| T-0302 | Theorem import | Lagarias criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0302-lagarias-criterion.md` |
| T-0303 | Theorem import | Li criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0303-li-criterion.md` |
| T-0304 | Theorem import | Nicolas primorial criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0304-nicolas-criterion.md` |
| T-0306 | Theorem import | Speiser criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0306-speiser-criterion.md` |
| T-0307 | Theorem import | Báez-Duarte discrete Nyman--Beurling criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0307-baez-duarte-criterion.md` |
| T-0308 | Theorem import | Pólya--Jensen criterion and effective barrier | PROPOSED | `gpt56-03` | `claims/theorems/T-0308-polya-jensen-criterion.md` |
| T-0309 | Theorem import | de Bruijn--Newman threshold | PROPOSED | `gpt56-03` | `claims/theorems/T-0309-debruijn-newman-threshold.md` |
| T-0310 | Theorem import | RH verified through height `3*10^12` | PROPOSED | `gpt56-03` | `claims/theorems/T-0310-verified-zero-height.md` |
| T-0311 | Theorem import | Deléglise--Nicolas `h(n)` criterion | PROPOSED | `gpt56-03` | `claims/theorems/T-0311-deleglise-nicolas-h-criterion.md` |
| M-0301 | Method | Source provenance and claim allocation | PROPOSED | `gpt56-03` | `claims/methodology/M-0301-source-provenance-and-claim-allocation.md` |
```

`T-0305` is intentionally unallocated pending the independent Weil
normalization audit requested by agent #1's `Q-0004`.

## `OPEN_PROBLEMS.md` additions

```markdown
- Q-0301 / Issue #14 — certify a negative Li coefficient.
- Q-0302 / Issue #15 — search the Nicolas primorial inequality.
- Q-0303 / Issue #16 — certify the Deléglise--Nicolas bounded-prime-sum inequality.
- Q-0304 / Issue #17 — certified Speiser search for `zeta'` zeros left of the line.
- Q-0305 / Issue #18 — positive-time de Bruijn--Newman nonreal-zero certificate.
```

All five were created unclaimed.

## `CURRENT_STATE.md` additions

- Issue #3 supplies a verified-source literature atlas, theorem imports, and
  standalone elementary proof kernels.
- No counterexample was found.
- Direct off-line zeta searches are excluded through height `3*10^12` by
  imported theorem `T-0310`.
- Jensen nonhyperbolicity searches are excluded through degree `9*10^24` for
  every shift by `T-0308 + T-0310`.
- Five independent certificate-first issues (#14--#18) are available.

## `NEGATIVE_RESULTS.md` additions

### NR-03-A — low-height direct zero search is closed

Platt--Trudgian rigorously verified RH and simplicity for every zero through
height `3*10^12`.  A direct off-line search below that height is duplicate work.

### NR-03-B — Jensen degree barrier

The effective xi Jensen theorem implies hyperbolicity for all shifts whenever
`d<=floor(T)^2` and RH is verified through `T`.  With `T=3*10^12`, no
nonhyperbolic witness exists at degree `d<=9*10^24`.

### NR-03-C — finite residuals do not refute closure/asymptotic criteria

A finite Nyman--Beurling least-squares residual or a finite Riesz-type
overshoot is not a counterexample without a universal lower bound or exact
quantified asymptotic contradiction.

## `LITERATURE.md` integration

Link to:

- `literature/README.md` for the route atlas;
- `literature/source-ledger.md` for inspection provenance;
- `literature/verified.bib` for located references;
- `literature/route-matching.md` for issue matching and rankings.
