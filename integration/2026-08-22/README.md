# 2026-08-22 scientific integration

## Status

```text
RH:                              UNPROVED
REVIEWED-ONLY PATH TO RH:        NONE
FROZEN MAIN:                     677203992eb0168920365ee45ae9db76bfa97dcf
REVIEWER D:                      PR #721 @ 06c8ea18ffe20c7efa01b0fdacb8ebea0a2b5b22
RESEARCH CENSUS:                 PR #375 through #707
TARGETED REVIEW ROWS REMAINING:  0
UNRESOLVED ACTIVE CONFLICTS:     0
HEAVY CAMPAIGNS RERUN:           NONE
```

This release moves the scientific front door beyond the August 11 integration without bulk-merging the research branch jungle. It integrates reviewed mathematical objects, exact refutations, computation boundaries, and typed open interfaces.

## Contents

- `CLAIMS.tsv` - 139 reconciled semantic claims.
- `EDGES.tsv` - 36 typed implication and hyperedge records.
- `ALIASES.tsv` - 19 exact semantic relations.
- `FAMILIES.tsv` - 24 route families.
- `REFUTATIONS.tsv` - 19 canonical mechanism firewalls.
- `COMPUTATIONS.tsv` - 22 retained computation and formal-artifact records.
- `PR_DISPOSITIONS.tsv` - one lifecycle row for each PR #375-#707.
- `CONFLICTS.tsv` - every nontrivial review conflict and its resolution.
- `EXTRACTION_PLAN.tsv` - object-level canonicalization plan.
- `FIXES_REQUIRED.md` - mandatory local repairs for `VERIFIED_WITH_FIXES`.
- `REVIEWER_D_OPEN_CUTS.md` - final reconciliation cut map.
- `ISSUE_ARCHAEOLOGY.md` - bounded use of the 171-issue historical archaeology.
- `DIRECT_MAIN_SUMMARY.md` - complete classification of the 85 direct-main commits.
- `LATE_RESEARCH_QUEUE.md` - explicit post-freeze exclusion policy.
- `validate_integration.py` and `validation.json` - fail-closed release validation.

## Extraction policy

1. Exact proof bodies remain at their frozen source PR/head/path unless already resident on main.
2. Family packets under `research/integrated/` are reviewed residency manifests, not rewritten proofs.
3. `VERIFIED_WITH_FIXES` is canonical only with its named repair.
4. Open sufficient and RH-equivalent nodes stay explicit and cannot be traversed as verified premises.
5. Refuted and superseded proposals remain discoverable with their surviving subresults.
6. Finite and computational results retain their exact scopes.
7. Later research is excluded rather than silently merged.

## Human front door

- [`../../STATUS.md`](../../STATUS.md)
- [`../../RESULTS.md`](../../RESULTS.md)
- [`../../PROOF_GRAPH.md`](../../PROOF_GRAPH.md)
- [`../../OPEN_CUTS.md`](../../OPEN_CUTS.md)
- [`../../REFUTATIONS.md`](../../REFUTATIONS.md)
- [`../../COMPUTATIONS.md`](../../COMPUTATIONS.md)
- [`../../HISTORY.md`](../../HISTORY.md)

## Machine front door

The byte-identical release registry is mirrored under [`../../canonical/2026-08-22/`](../../canonical/2026-08-22/README.md). The Mellin-Landau consumer contract is separately exposed at [`../../canonical/consumers/mellin-landau/`](../../canonical/consumers/mellin-landau/README.md).
