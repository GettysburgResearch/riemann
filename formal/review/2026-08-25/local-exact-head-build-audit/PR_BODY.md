# Exact-head local Lean audit

This draft review PR publishes the independent local build evidence requested for the three repaired formalization heads. It contains no mathematical statement change, no source-branch merge, and no claim that RH is proved.

## Frozen heads

| Reviewer | Exact source head | Trusted build | Comparator | No-sorry | Axiom output |
|---|---|---|---|---|---|
| A | `9ed8988218fd9c3e1da33bde81361262fc0aa747` | FAIL | FAIL | PASS | FAIL / unavailable |
| B | `072b4dbd0e4e407728a59110eb4f7214e23f8f8d` | FAIL | FAIL | PASS | FAIL / unavailable |
| C | `b20ee9b3678e5d8fa32b04b156bc02cec782a97b` | FAIL | FAIL | PASS by exact-source scan; wrapper blocked by compilation | FAIL / unavailable |

All heads use `leanprover/lean4:v4.33.0-rc2` and committed manifest SHA-256 `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`. All ten package checkouts match the committed manifest. No `lake update` was run.

## Controlling result

`NOT_READY_FOR_FORMAL_V0_1_RECONCILIATION`

Each individual trusted library was required to build before a combined worktree could be created. That gate failed. Consequently the combined rehearsal is recorded as `NOT_RUN_GATE_FAILED`; no fourth worktree, merge, conflict resolution, combined registry, or combined patch was created.

The retained first causes include duplicate root/Zeta23 comparator-library resolution and independent local Lean errors at every repaired source head. Reviewer A also has a missing upstream declaration lock; Reviewer C has a cross-platform CRLF statement-lock defect. Reviewer B's authoritative axiom runner omits its two owned print modules.

## Evidence and patches

- `LOCAL_BUILD_MATRIX.tsv` and `outputs/*_COMMANDS.tsv` retain every command and exit code.
- `A_BUILD_REPORT.md`, `B_BUILD_REPORT.md`, and `C_BUILD_REPORT.md` identify first causal errors and trust-boundary results.
- `AXIOM_AUDIT.tsv` and `COMPARATOR_AUDIT.tsv` retain the explicit module/target verdicts.
- `RAW_LOG_INDEX.tsv` hashes every full local raw log; selected small logs are under `outputs/`.
- `SHA256SUMS` and `COMBINED_REHEARSAL_SHA256SUMS` bind the published evidence.
- `patches/` contains advisory, statement-preserving mechanical proposals only. None is applied to a repaired source branch.

PR #747 still has no final acceptance addendum. PRs #749 and #750 retain their original `NOT_READY_FOR_RECONCILIATION` build blockers. This audit does not alter any prior mathematical verdict.

RH remains unproved.
