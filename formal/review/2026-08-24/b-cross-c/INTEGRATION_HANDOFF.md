# Integration handoff

## Frozen inputs

| Object | Exact identity |
|---|---|
| Bootstrap | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` |
| Reviewer C PR | `#735` |
| Reviewer C head | `4863c31dd497ffe69ea400fe29275decf4cb5d29` |
| Cross-review branch | `formal/review/2026-08-24/b-cross-c` |

## Reconciliation disposition

```text
Reviewer C finite algebra packet:        ACCEPT WITH LOCAL FIXES
Reviewer C firewall packet:              ACCEPT WITH SCOPE NOTES
Reviewer C actual-Xi order-three claim:  DO NOT INTEGRATE
Reviewer C reserve semantic rows:        DO NOT INTEGRATE AS PROVED
Reviewer C QA evidence:                  DO NOT TREAT AS FAIL-CLOSED
Overall:                                 NOT_INTEGRATION_READY
RH proved:                               NO
```

## Safe extraction candidates

1. `two_point_pick_identity`
2. `three_node_pick_determinant_identity`
3. reciprocal and companion factor identities
4. `ldl2_identity`, `ldl3_identity`
5. PSD/PD separation and duplicate-row finite identities
6. `Jet2.reciprocalConcavity_add`
7. `offLineOrbit_defect_formula`
8. `criticalOrbit_energy_zero`
9. finite Hermite/Q4 identities
10. the six exact matrix/operator firewalls

The generic absorption and finite allocation lemmas may be extracted under new
API semantic IDs, not under the stronger source theorem IDs.

## Exact reconciliation blockers

| Blocker | Required Reviewer D action |
|---|---|
| arbitrary external Prop labels | require concrete source-locked propositions |
| repeated-node PSD assumed | require a proof using node/value equality and duplicate-row lemmas |
| one-orbit semantic mismatch | split generic API from L-92101 source theorem |
| reserve shares not typed nonnegative | add nonnegative one-use allocation ledger |
| actual-Xi grouped bridge absent | keep actual reciprocal concavity and order-three headline blocked |
| comparator mismatch | require comparator for repaired full headline |
| QA booleans manually trusted | regenerate evidence fail-closed |
| no full build/axiom output | require successful exact-head workflow and logs |

## Registry deltas Reviewer D should apply

- retain `OPERATOR.XI.PICK_ORDER3.DETERMINANT` as `PROVED`;
- retain `OPERATOR.XI.RECIPROCAL_CONCAVITY.SUM` as `PROVED`;
- retain finite refutations at their exact scopes;
- downgrade/split `ONE_ORBIT`;
- downgrade `CRITICAL_RESERVE_BUDGET`;
- downgrade `RECIPROCAL_CONCAVITY.ACTUAL`;
- retain `PICK_ORDER3` as blocked/conditional only after its exact proposition is repaired;
- do not accept `comparator_checked=true` for the full order-three row.

## Next validation

After fixes, Reviewer D should require one commit-pinned workflow that runs all
requested commands and stores complete build, comparator, registry, source,
blueprint, declaration, and axiom logs.
