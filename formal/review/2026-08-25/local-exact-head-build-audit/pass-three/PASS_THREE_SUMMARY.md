# Pass-three exact-head and combined-rehearsal addendum

This directory appends to pass one and pass two. It does not rewrite, squash,
or remove either earlier audit record.

## Result

| Scope | Frozen source | Trusted build | Comparator | No-sorry | Axiom output |
|---|---|---|---|---|---|
| Reviewer A | `ae0887b8125601c98dc809cffe01c7f1c78bb998` | PASS | PASS | PASS | PASS, 24/24 retained declarations |
| Reviewer B | `6d42bbc31c81e7d6a03909e205b56f30f6f7b49a` | PASS | PASS | PASS | PASS, 34/34 retained declarations |
| Reviewer C | `381a5a98ade7c6bad7122e5182c2fc07332dc747` | PASS | PASS | PASS | PASS, 40/40 expected declarations |
| Combined rehearsal | local `ae50ef2786b904a9aecdcfb1112d7b323f36ea41`, tree `bd621c02db310fc318ee287eefeb6e2c76c8b48a` | PASS, 8,806 jobs | PASS | PASS | PASS, exact 89/89 declarations |

Reviewer C contains the two owner-approved proposition-shape corrections:

- `actualXiInputs_have_concrete_dependencies` certifies
  `Nonempty (ActualXiReserveAllocation inputs.grouped)`;
- `buildLockedActualXiReserveAllocation` certifies
  `Nonempty (ActualXiReserveAllocation grouped)`.

They express existence of allocation data already carried or constructed by the
API. They add no hypothesis and do not change the actual-Xi order-three
comparator conclusion. No other mathematical theorem type was changed in the C
repair.

## Combined rehearsal

The rehearsal mechanically combined A, B, and C, in that order, from bootstrap
`573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`. It did not merge the review-only
PRs. The final runner recorded 58/58 exit-zero commands over 31m33s.

Verified gates include:

- full trusted `lake build`, 8,806 jobs;
- baseline A comparator smoke, aggregate comparator, and 21 explicit
  ChallengeDeps/Challenge/Solution targets;
- 139 unique canonical registry claims and 31 branch delta rows;
- source locks and three blueprint fragments;
- exact seven-topic Challenge boundary, with seven expected Challenge
  placeholders and none in trusted, ChallengeDeps, or Solution sources;
- nine committed axiom-print modules and 33 generated registry headlines,
  yielding the exact expected 89/89 outputs;
- only `propext`, `Classical.choice`, and `Quot.sound` in retained axiom output;
- A's retained validation replay, B's trusted arithmetic modules, and C's
  declaration/source/static/external-input/comparator-fidelity checks.
- an independent all-topic comparator probe: seven of seven Challenge/Solution
  theorem types match, with Challenge and Solution loaded in isolated Lean
  processes.

The normal registry generator initially exposed a duplicate blank reservation
for `API.MELLIN.SUBPOWER_NEGATIVE_MASS`. The rehearsal retained A's unchanged
nonempty `PROVED_CONDITIONAL` owner row and removed only B's blank/deferred
duplicate. No proved status was invented.

## Verdict

`READY_FOR_FORMAL_V0_1_RECONCILIATION_WITH_MECHANICAL_PATCHES`

This authorizes a scientific reconciliation from the frozen heads; it is not a
merge authorization. The combined patch is advisory, and the finished release
package must receive a fresh exact-tree audit before integration.

RH remains unproved.
