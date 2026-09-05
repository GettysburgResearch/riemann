# Reviewer C — second-pass blockers and closed coverage items

Baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Review PR #798 remains at `7466ad8081101508be7c7acf0065cb2e0944a639`; this second-pass update is prepared, not pushed. See `pass2/PUBLICATION.json`.

**Public-release readiness is not cleared.** The following are scoped C findings and omissions. Outstanding A/B scientific dispositions remain **pending integrator reconciliation**.

## Confirmed findings requiring action

| ID | Boundary | Finding | Required closure |
|---|---|---|---|
| C2-F01 | P0 formal nonvacuity | `ActualXiOrderThreeInputs` is empty: the raw Xi definition makes `actualXiNodeP(1/2)=0`, contradicting the stored strict diagonal positivity. Five actual-Xi canonical entries depend on this type. | Repair entire-Xi normalization and shared ChallengeDeps contract; trace every dependent declaration; regenerate locks and comparator statements; compile the regression and repaired statements; conduct fresh semantic review. Do not confuse an implication from empty inputs with kernel inconsistency or mathematical RH progress. |
| C2-F02 | P0 intended source-domain coverage | Injective `ℕ → ReflectedOffLineOrbit` excludes empty and finite off-line spectra. | Countable actual index/finite exhaustions or optional padding, complete representative coverage, and explicit empty/finite cases. Fixing C2-F01 alone is insufficient. |
| C2-F03 | P1 statement-strength accuracy | `NonremovableAt` means not analytic for the assigned value, not punctured analytic nonextendability. | Rename or strengthen with a proved bridge. Preserve the valid weaker transfer lemmas and separate the stronger negative-order pole hypothesis. |
| C2-V01 | P1 preflight policy | Baseline tactic-query PCRE misses ten ordinary query fixtures; the trailing word-boundary is misplaced after `?`. | Repair with a language-aware or correctly scoped check, test comments/strings/Unicode as well, and rerun at the repaired source. A lexical preflight defect is not a Lean kernel defect. |
| C2-V02 | P0 when used as an acceptance gate | Corrupted #568/#599 scripts reject normally and emit PASS under `-O`; source flags and self-hashes do not certify omitted arithmetic inputs. | Explicit fail-closed producer/checker checks, authenticated primitive inputs and independent recomputation; do not promote toy/float fixtures into source or asymptotic proofs. |
| C2-S01 | P0 source-qualified extraction | #599's final factor-67 packet is not identified by its historical census pin. The old pin is an intentional PR590 scientific input, not the new packet head. | Reconcile exact final source `8daa0a5d94de56c68a1ce710824b26cacc1a9bbc`, reidentified claims, earlier reviews and analytic dependencies. Do not relabel the pre-release commit as post-release mutation. |
| C2-W01 | P1 workflow extraction | #599 includes a write-enabled, branch-specific PDF publisher with persistent credentials and git push. | Exclude from blind mathematical extraction; owner reviews any deliberate workflow reuse. A pinned PDF hash does not make a publisher a passive checker. |

The ordinary algebraic proof, affected canonical IDs and repair target for C2-F01/F02 are in `pass2/FORMAL_NONVACUITY.md`. Its Lean regression is **NOT COMPILED**, a separate status from the completed source-level proof.

## Closed or narrowed items

**C-01 historical head acquisition is closed at its declared denominator:** 340/340 real PR sources compared across two passes, including 312 new observations; 338 match and two differ. The absent #417 is excluded. This closes the 312-head omission, not complete claim/attachment/branch-only coverage.

**#568 replay delta is resolved at finite source/replay scope:** two changed paths, identical old/new generated outputs and formatting-only retained JSON difference. No claim files changed; imported primitive interval endpoints were not recalculated.

**Formal catalog entry inspection is complete for the listed entries:** 31 canonical plus six API rows; all 34 declaration-bearing mappings and 33 distinct declarations read in 15 defining modules. This replaces metadata-only coverage for those entries, not full import closure or compilation. The count reconciliation was sound; five actual-Xi entries nonetheless have the new nonvacuity defect.

## First-pass blockers retained

The original report is preserved byte-for-byte as `pass2/evidence/PASS1_RELEASE_BLOCKERS.md`. Its consumer `assert`/duplicate/source-binding defects, #771/#774 and #731 claim-ID collisions, #752 unretained scout and correction-propagation debts, external-source promotion boundaries, and artifact permanence concerns remain unresolved unless a specific new result above narrows them.

Complete post-cut claim splits, all-ref/transitive source coverage, fresh Lean/kernel/Comparator runs and exact compilation-to-statement coverage are still not completed by C. The new vacuity finding makes statement/instance fidelity an explicit acceptance gate; a build receipt alone cannot clear it.

Public-launch rights, project licensing, all-import NOTICE/paper permissions, all-history secret/PII scanning, technical main-branch protections and owner access/ruleset checks remain separate owner-authorized tasks. No secret, compromise or specific rights violation is asserted merely because a complete audit is missing. No access, setting or repository visibility was changed.

## Integrator questions

Reconcile whether A/B reviewed the exact shared Xi blob or a different repaired source; whether empty/finite off-line cases have separately reviewed adapters; which canonical consumers need withdrawal or amended scope; and whether another exact review covers #599's final packet. Preserve differing verdicts and source versions. C's independent failure finding is not a declaration that A or B failed a review, and their pending dispositions are not permissions to accept a claim.
