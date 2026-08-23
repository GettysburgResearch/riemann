# Bootstrap validation record

## Completed before publication

The bootstrap was checked against the exact repository tree from the 2026-08-22 scientific integration.

```text
FORMALIZATION_MAP generation:       PASS, 139 canonical rows
formalization registry validation:  PASS
source-lock validation:             PASS
blueprint semantic-ID validation:   PASS
trusted-source sorry/admit scan:    PASS
trusted-source custom-axiom scan:   PASS
Python syntax compilation:          PASS
shell syntax validation:            PASS
remote PR tree materialization:      PASS
```

The generated `formal/registry/FORMALIZATION_MAP.tsv` is intentionally not committed; it is reproduced from the canonical scientific registry and sparse reviewer deltas in CI and local builds.

## Lean build boundary

This environment did not contain a Lean toolchain and cannot access external package hosts directly. Therefore this record does **not** claim that `lake build` or `#print axioms` was executed locally.

The path-filtered workflow performs, on a networked GitHub runner:

```text
lake update
lake exe cache get
lake build
lake build Challenge.RH Solution.RH
no-sorry/custom-axiom audit
#print axioms audit
```

Because this workflow is introduced by the bootstrap itself, the first authoritative workflow result should be inspected immediately when the branch is merged into `main`. Any Lean build failure is an infrastructure defect to repair before the A/B/C heavy formalization passes are treated as based on a stable bootstrap.

## Scientific boundary

```text
Riemann Hypothesis: UNPROVED
formal proof of RH: NONE
```
