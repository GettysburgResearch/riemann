# Final acceptance addendum — Formalization Reviewer B

## Frozen objects

```text
repository:                   gfreund123/riemann
bootstrap base:               573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f
primary PR:                   #733
primary branch:               formal/020-arithmetic-mellin
originally reviewed head:     770c61e9d0ace520be2333f348d0bf239e0120ad
repaired primary head:        072b4dbd0e4e407728a59110eb4f7214e23f8f8d
repaired primary tree:        1c32466dd7928a24e0115268a6a330216f26ed3b
binding cross-review PR:      #750
cross-review branch:          formal/review/2026-08-24/a-cross-b
cross-review parent head:     81d201849514224d0a5899ac6b61dc66a71b8d1e
```

The repaired primary head is exactly two fast-forward commits beyond the head audited in the original cross-review. This addendum does not repeat the full review; it checks the repair against each binding P0/P1 finding and the original mismatch ledger. PR #733 was not modified.

**RH remains unproved.**

## Controlling result

The scientific and statement-fidelity repairs are substantial and mostly successful:

- 15 findings are `RESOLVED`;
- 9 are `RESOLVED_BY_HONEST_DOWNGRADE`;
- 4 are `PARTIALLY_RESOLVED_WITH_EXCLUSION`;
- 2 remain `UNRESOLVED_BLOCKER`.

The two unresolved blockers are mechanical trust gates rather than new mathematical gaps:

1. no exact-head Lean/Lake, comparator, registry, blueprint, no-sorry, or axiom suite was executed or retained;
2. the authoritative `formal/scripts/check_axioms.sh` still does not directly run
   `RiemannFormal/Arithmetic/AxiomAudit.lean` or
   `comparator/PrintAxioms/ArithmeticFixedRows.lean`.

Accordingly, the repaired source is suitable evidence for reconciliation planning, but it is not yet acceptable as compiled trusted formalization.

## Accepted repairs

### Exact strengthening

The formerly toy source firewalls were materially repaired:

- the exact SHARP target and `(Y,Z,t)=(16,4,4)` RN/raw-cutoff fixture are present;
- parent capacity `5`, child response `1`, RN density `1/5`, raw cutoff `1`, inequality, and transport are stated separately;
- response and capacity use distinct indexed source types at the exact cell;
- `r` versus `2r²` is quantified on `0<r<1/2`;
- `p^{-1}` versus `p^{-1/2}` is quantified for every real `p>1`;
- duplicate labels over prime `67` and an accumulated-parity fixture are present.

The exact rows-2/3 and fixed `5:3` finite numerator algebra remains statement-faithful on its literal domain `‖a‖<1`.

### Honest downgrades

The repair correctly chose exclusion rather than pretending to fill missing mathematics:

- the generic list recursion is no longer named as the canonical sequential first-owner theorem;
- role indices are documented as preventing implicit substitution only, while `rebuildAtRole` records the public-reconstruction limitation;
- fixed/moving detector data shape is separated from the explicit `QueryIndependent` proposition;
- generic wavelet, factor-67, Abel–Mertens, same-K1, and one-field helpers were renamed and their canonical claims remain blocked;
- the circular RH wrapper and its conclusion-bearing `consumes` premise were removed;
- Reviewer B now exports only non-circular finite arithmetic input packages and no theorem in its Mellin-Landau module concludes RH.

These downgrades are scientifically honest and remove the overstatement defects identified in the original review.

## Registry, blueprint, and provenance

`B.tsv` now gives `PROVED` only to the exact rows-2/3 and fixed `5:3` algebra and gives `REFUTED_FORMALIZED` to the exact alpha-child coefficient mismatch. The canonical first-owner, source-typing, wavelet, Abel–Mertens, same-K1, half-divisor packet, and Mellin consumer rows are conservatively blocked.

`content-B.tex` now:

- marks incomplete canonical nodes `\notready`;
- describes literal helper scope;
- states the source-provenance limitation;
- removes the false five-three-to-RH dependency edge;
- states that no Reviewer B theorem concludes RH.

`B_SOURCE_LOCKS.tsv` is a useful exact local ledger: it records source PR, SHA, path, claim ID, formal declaration, literal scope, status, and exclusion notes. It is accepted as review evidence, but not yet as machine-validated provenance because the bootstrap validator does not consume it and no validator execution was observed.

The versioned `Arithmetic/REPAIR_REPORT.md` is complete and consistent with the repaired source and PR description.

## Comparator and trust boundary

Both comparator topics remain textually faithful:

- `ArithmeticRows23` states exactly the finite unit-disc common-zero theorem;
- `FixedDetectorFiveThree` states exactly the finite unit-disc `5:3` noncancellation theorem;
- each solution imports `ChallengeDeps` and the trusted arithmetic theorem, not its `Challenge` module.

The exact repair diff adds no `sorry`, `admit`, custom `axiom`, `opaque`, or `unsafe` declaration. The only `sorry` occurrences remain in the two permitted statement-only challenge modules. `ComparatorSmoke` was removed from the trusted aggregate.

This is a static trust conclusion only. The relevant declarations have not received a compiled `#print axioms` acceptance in this pass.

## Required final gates

Before formal reconciliation may treat Reviewer B's accepted declarations as trusted compiled results:

1. wire the two B-owned axiom-print modules into the authoritative axiom runner, or execute and retain them through an equivalent authoritative mechanism;
2. run the complete exact-head suite at
   `072b4dbd0e4e407728a59110eb4f7214e23f8f8d`;
3. retain outputs establishing the library build, both comparator builds, registry generation and validation, source-lock validation, blueprint validation, no-sorry check, and axiom audit.

Build status for this addendum:

```text
BUILD_NOT_EXECUTED
workflow runs observed on repaired head: 0
combined statuses observed on repaired head: 0
```

## Integration boundary

Reconciliation may safely use the repaired branch as source-level evidence for:

- exact rows-2/3 and fixed `5:3` finite algebra;
- exact local RN, response/capacity, parity-label, `r`/`2r²`, and scalar normalization fixtures;
- exact half-divisor coefficient and arithmetic-function convolution algebra;
- explicitly generic wavelet, finite-sum, and one-field helpers;
- non-circular fixed arithmetic input packages;
- the repaired conservative registry, blueprint, and local source-lock ledger.

It must exclude:

- the full sequential first-owner theorem;
- provenance-safe source promotion;
- historical fixed-detector preselection as a consequence of a data constructor;
- the full normalized-box operator identity;
- the canonical minimal wavelet, factor-67, Abel–Mertens, same-K1, and ratio-four Hardy packets;
- any RH conclusion from Reviewer B's branch;
- compiled-trust status until the two gates above are closed.

NOT_READY_FOR_RECONCILIATION
