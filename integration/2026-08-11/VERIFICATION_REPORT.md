# Pre-merge confirmation and verification report

**Validation cutoff:** `2026-08-11T09:05:27Z`  
**Repository:** `gfreund123/riemann`  
**Target PR:** `#374`  
**Frozen base:** `main@d6409319b4041cd09bee85f55a344631508f2501`  
**Validated integration head before this report:** `ec7109a3950b4cd471aeca05ad41f89be373e36b`  
**Scientific status:** **RH remains unproved and undisproved.**

This pass was performed after the initial synthesis and before changing `main`. It confirms repository state, exact review provenance, internal status consistency, front-door compatibility, refutation evidence, and post-review quarantine boundaries.

## 1. Live repository and merge-base confirmation

At validation cutoff:

```text
main                               d6409319b4041cd09bee85f55a344631508f2501
integration branch                 integration/20260811-major-review-synthesis
initial validated head             ec7109a3950b4cd471aeca05ad41f89be373e36b
relationship to main               ahead 11, behind 0
merge-base                         d6409319b4041cd09bee85f55a344631508f2501
PR mergeability                    mergeable
```

`main` had not moved since the original integration freeze. No rebase, conflict resolution, or source-branch import was required.

## 2. Changed-file boundary

The initial PR changed exactly eleven files:

```text
README.md
integration/2026-08-11/README.md
integration/2026-08-11/CUTOFF.yaml
integration/2026-08-11/REVIEW_SOURCES.tsv
integration/2026-08-11/CLAIM_LEDGER.tsv
integration/2026-08-11/ROUTE_DAGS.md
integration/2026-08-11/REFUTATIONS_AND_FIREWALLS.md
integration/2026-08-11/OPEN_HINGES.md
integration/2026-08-11/POST_REVIEW_DELTA.md
integration/2026-08-11/CANONICAL_EXTRACTION_PLAN.md
integration/2026-08-11/NEXT_INTEGRATOR.md
```

No theorem branch, experiment, canonical registry object, August 1 integration record, workflow, compatibility wrapper, or research packet was modified. This verification pass adds only this report and `REFUTATION_EVIDENCE.tsv`, then updates integration metadata to point to them.

## 3. Pull-request discussion and automation state

The PR had:

```text
review submissions             0
review comments                0
unresolved review threads      0
conversation comments          0 before the verification note
GitHub Actions workflow runs   0
combined status contexts       0
```

There was therefore no hidden review objection or failing status to resolve. The absence of CI is recorded rather than interpreted as a passing build.

A network clone was unavailable in the execution runtime, so verification used GitHub's exact commit, comparison, contents, PR, review-thread and status APIs. No heavy mathematical experiment was rerun.

## 4. Authoritative review packet resolution

Every authoritative artifact named by `REVIEW_SOURCES.tsv` was fetched successfully at its exact frozen review head.

| Review PR | Head | Artifacts resolved |
|---:|---|---:|
| #369 | `0f4cc8afd0dcfeabb3357225cbf6afd8f065a231` | 3/3 |
| #370 | `ad77d151ab2e753595a8b2b9d49ac0ba9e601634` | 5/5 |
| #371 | `fd9292cac2e12e825135b8949b3c3b778f4344d0` | 4/4 |
| #372 | `9b9c2536d89b65cb999ec08e20fce3386383803a` | 6/6 |

Total:

```text
18 authoritative artifacts resolved at exact SHAs
0 missing authoritative artifacts
```

This includes the Q4 exact-counterexample deposit and the independent-route final-drift addendum/TSV.

## 5. Refutation evidence audit

The canonical claim ledger correctly separates source proposal, mathematical status, review status, lifecycle and RH relationship. A second pass identified one provenance weakness: some `FALSE` rows named the original proposal SHA but did not independently expose the exact later refutation path.

`REFUTATION_EVIDENCE.tsv` now binds each load-bearing false/no-go/corrupted row to:

```text
exact evidence PR
exact evidence commit
exact evidence path
exact claim or review identifier
exact refuted scope
strongest surviving scope
```

The following source paths were independently resolved through GitHub during this pass:

- frozen GFEP/producer/BTF refutation;
- finite-stationary policy no-gap theorem;
- terminal-boundary atomic-norm refutation;
- source-mass/capacity refutation;
- Mersenne-collar refutation;
- Q4 source-order correction;
- Q4 inertia-to-current refutation;
- Q4 specialist exact counterexamples;
- Brownian reflected-tail and positive-mixture refutations;
- Schur-sign firewall;
- corrected hyperbolic pole-block refutation.

Two stale aliases in the elementary reviewer TSV were corrected at integration level:

| Reviewer-ledger alias | Actual resolvable source path |
|---|---|
| `claims/refutations/R-30402-complete-critical-boundary-has-linear-atomic-norm.md` | `claims/refutations/R-30501-terminal-commutator-atomic-norm-closure-is-false.md` at `18e25ec92583e9110a57cf037b691491c278fe39` |
| `claims/refutations/R-30801-eventual-mersenne-collar-saturation-fails.md` | `claims/refutations/R-28501-eventual-mersenne-collar-fragmentation-is-false.md` at `f07f44263c3ff4b219918b05cac61a75e18ff773` |

These are path/provenance corrections, not changes to the mathematical verdicts.

## 6. Front-door compatibility audit

The existing durable front-door validator was inspected. The PR preserves its stable machine contract:

- root README still contains the exact statement `RH remains unsolved`;
- the `Begin here` section still has exactly two numbered choices;
- required links to `research/RESULTS_INDEX.md`, `research/integrated/README.md` and `AGENTS.md` remain present;
- canonical registry, aliases and provenance schema are untouched;
- no forbidden legacy paths were introduced;
- integration wrappers and internal tools are untouched;
- no August 1 canonical blob or historical packet was rewritten.

The new integration documents are intentionally outside the validator's old curated list. Their internal links are local and their referenced review artifacts are source-pinned rather than assumed resident on `main`.

## 7. Claim-status consistency audit

The high-leverage ledger was reviewed row by row against the four specialist reports. The following conflict resolutions remain correct:

1. Frozen GFEP, frozen producer positivity and frozen BTF are `FALSE`, not `OPEN`.
2. Signed Cycle Debt, adaptive/nonstationary/continuum policies and uniform Pascal remain live outside that refutation.
3. PR #359 is a false full composition; its aggregate determinant/negative-inertia lemma is separately salvaged.
4. `RH ⇒ PIG` is reviewed; `PIG ⇒ RH` remains incomplete because the exact integrated recurrence and pole-energy adapter are absent.
5. The universal unpiecewise `tr(K_-)` formula is false, while neighboring inertia inequalities survive.
6. Corrected Brownian one-fiber theory survives; reflected-tail and positive-mixture closures do not.
7. The corrected-kernel floor and Fredholm/heat prime-side signs remain RH-bearing criteria, not independent solved estimates.
8. Upstream Anthropic/Lean status does not transfer to local extensions.

No row labels an RH-equivalent criterion as an accepted proof or as unconditional closure.

## 8. Post-review movement audit

The quarantined delta heads remained:

```text
#337  36b3bebea80e18f965f304638e2123c4d2363a09
#368  023434958a4c115c4d1f7d93ea310716f8bd81ae
#373  34fe2037ba33bc61fc1e6ce04c7e74ab7b13e794
```

No later PR appeared before validation cutoff. None of these descendants receives an inherited reviewed verdict.

## 9. Temporal normalization

Review #372's declared timestamp `2026-08-11T14:03:15Z` is chronologically impossible relative to the integration observation. The synthesis does not use that timestamp as a cutoff. It uses only the exact review head and exact source SHAs. This preserves mathematical provenance without inventing a corrected reviewer wall clock.

## 10. Computation boundary

This pass performed no:

- large exact recurrence replay;
- endpoint scan;
- interval/Rouché campaign;
- Lean build;
- Fredholm/Nyström sweep;
- large matrix or Gabor search.

The review wave had already inspected retained manifests, hashes, scripts and result objects. This pass verifies integration and provenance, not the underlying heavy computations anew.

## 11. Pre-merge disposition

After adding the explicit refutation map and this report, the integration is suitable for merge as a **scientific status/provenance front door**.

It is not suitable to describe as:

- a proof or disproof of RH;
- a wholesale merge of research branches;
- independent revalidation of every heavy computation;
- canonical theorem-packet extraction.

The next creation wave may rely on the route statuses, refutation scopes, exact review pins and post-review quarantine recorded here. Canonical theorem packets should still be extracted family by family under `CANONICAL_EXTRACTION_PLAN.md`.
