# Shared comparator-isolation pass-two report

Verdict: `PASS`. The shared Lake/comparator infrastructure repair is independently green at the exact detached commit below. It is advisory infrastructure evidence and does not merge or alter any mathematical branch.

## Frozen source

- base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- repaired commit: `db95fa09d9e956807099eb9d140de374f3ceca67`
- tree: `1ed15fd373f5f07d58907fc3fea0ff30f07ac7e6`
- parent: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- status: clean detached worktree at `C:\riemann-pass2\shared`
- committed toolchain SHA-256: `0d3c76ccd8772d8bcbe207241421a760312b71a6aa82f84194391fdf5cb026d6`
- committed manifest SHA-256: `6be307e0de2294f99ce68e80903cd4cc88e77b6797c853c67be5cd9f6a1db453`

The repair is a single commit directly on the requested bootstrap base. The committed toolchain and dependency-manifest blobs are unchanged, and no dependency update is included.

## Why target-only renaming was insufficient

The root formal project and pinned Zeta23 dependency both exposed the module roots `ChallengeDeps`, `Challenge`, and `Solution`. Giving only the local Lake libraries distinct target names did not disambiguate those module identities. With elan restored to Bash `PATH`, Lake still resolved `ChallengeDeps.RH`, `Challenge.RH`, and `Solution.RH` into Zeta23 and attempted to compile nonexistent files under:

```text
.lake/packages/Zeta23/comparator/ChallengeDeps/RH.lean
.lake/packages/Zeta23/comparator/Challenge/RH.lean
.lake/packages/Zeta23/comparator/Solution/RH.lean
```

The successful repair makes both layers unique:

- Lake targets: `RiemannComparatorChallengeDeps`, `RiemannComparatorChallenge`, and `RiemannComparatorSolution`;
- Lean file/module prefixes: `RiemannComparatorChallengeDeps.*`, `RiemannComparatorChallenge.*`, and `RiemannComparatorSolution.*`.

The files remain in the same trust directories—`comparator/ChallengeDeps`, `comparator/Challenge`, and `comparator/Solution`—and the declarations retain their original namespaces and names, including `ChallengeDeps.ProjectRH` and `rh_statement_exact`. Thus the repair changes package/module routing, not the trusted proposition or solution theorem.

## Retry sequence

1. The first Bash invocation failed before Lake ran because elan's directory was absent from Bash `PATH` (`lake: command not found`, exit `127`).
2. Retrying with elan on `PATH` exposed the substantive target-only failure above (exit `1`).
3. After relocating the files and imports to unique Lean module prefixes, all three baseline comparator libraries built successfully. The Challenge-side RH statement retains its one intentional `sorry`; that placeholder remains outside Solution and the trusted formal library.

The first four registry-script attempts separately hit the Windows Store `python3` application alias (exit `9009`). Re-execution with the bundled Python interpreter succeeded; these are recorded as environment retries, not formalization failures.

## Authoritative results

| Command or check | Exit | Classification | Result |
|---|---:|---|---|
| initial `bash scripts/build_local_comparators.sh` | 127 | `TOOLCHAIN_FAILURE` | Bash could not find `lake`; no comparator ran. |
| PATH-corrected target-only comparator build | 1 | `COMPARATOR_FAILURE` | Lake selected the identical Zeta23 module roots and requested nonexistent dependency files. |
| unique-target and unique-module comparator build | 0 | `PASS` | Baseline RH ChallengeDeps, Solution, and Challenge modules compiled (`3146` jobs). |
| `lake build` | 0 | `PASS` | Trusted root library compiled (`3185` jobs). |
| bundled-Python registry generation | 0 | `PASS` | `139` claims, `0` reviewer delta rows at bootstrap. |
| bundled-Python registry validation | 0 | `PASS` | `139` claims; `1` stated, `0` proved, `0` conditional. |
| bundled-Python source-lock validation | 0 | `PASS` | `139` claims; exact Mathlib and Zeta23 pins accepted. |
| bundled-Python blueprint validation | 0 | `PASS` | `3` fragments. |
| `bash scripts/check_no_sorry.sh` | 0 | `PASS` | Trusted sources and Solution contain no sorry/admit or custom axiom/opaque declaration. |
| `bash scripts/check_axioms.sh` | 0 | `PASS` | `6/6` declarations from exactly `2/2` fail-closed manifest modules. |

The six retained axiom results use only `propext`, `Classical.choice`, and `Quot.sound`, or no axioms for the two release metadata equalities. The axiom runner's manifest must exactly match the discovered root audit module and RH comparator print module.

## Additional infrastructure retained

- The workflow no longer performs an unreviewed `lake update`; it consumes the committed manifest and calls the unique comparator build script.
- The comparator configuration names the unique RH Challenge and Solution modules.
- The LF checkout rule for C's locked external-statement text is included.
- The advisory patch contains ordinary textual Git diff output only; `git diff --numstat` reports no binary entries.

RH remains unproved. No source branch was edited, committed, pushed, or merged while preparing this evidence.

Run `sha256sum -c concise-staging/shared/SHA256SUMS` from `audit-local-20260826-pass2/` to verify the retained shared raw logs.
