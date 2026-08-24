# Build and axiom audit

## Frozen target

- Repository: `gfreund123/riemann`
- Bootstrap base: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- PR: `#733`
- Supplied observed head: `6e6fb8b120069eaed2cc7f7cf966bb082c54eb4d`
- Actual frozen head: `770c61e9d0ace520be2333f348d0bf239e0120ad`
- Target tree: `9d86d86981af2d16bd26c56dcb5b31f04182a505`
- Lean toolchain: `leanprover/lean4:v4.33.0-rc2`
- Mathlib: `51e6992efd06126df61a496bebf8f49482a4e129`
- Zeta23: `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e`

## Requested commands

| Command | Duration | Result |
|---|---:|---|
| `lake exe cache get` | not started | **BUILD_FAILURE**: no `lake` executable and no network checkout |
| `lake build` | not started | **BUILD_FAILURE** |
| `lake build Challenge.ArithmeticRows23` | not started | **BUILD_FAILURE** |
| `lake build Solution.ArithmeticRows23` | not started | **BUILD_FAILURE** |
| `lake build Challenge.FixedDetectorFiveThree` | not started | **BUILD_FAILURE** |
| `lake build Solution.FixedDetectorFiveThree` | not started | **BUILD_FAILURE** |
| registry generation/validation | not started | repository checkout unavailable |
| source-lock verification | not started | repository checkout unavailable |
| blueprint validation | not started | repository checkout unavailable |
| no-sorry script | not started | repository checkout unavailable |
| axiom script | not started | repository checkout unavailable |

The environment preflight was exact:

```text
command -v lean: exit 127, 0.00 s
command -v lake: exit 127, 0.00 s
git clone: exit 128, 0.01 s
fatal: Could not resolve host: github.com
```

## Exact-tree remote CI attempt

A separate temporary branch and PR were used so PR #733 remained untouched:

- temporary PR `#745`;
- parent/source tree exactly `770c61e9d0ace520be2333f348d0bf239e0120ad`;
- inert Markdown trigger commit `56244466351cffa5653780f9ad58070986e1910d`;
- `opened`, `ready_for_review`, `push`, and `synchronize`-eligible events were generated;
- elapsed open-to-close time: 163 seconds;
- workflow runs observed for the exact head, trigger head, and merge heads: **0**;
- combined statuses observed: **0**.

The probe PR was closed and its temporary branch reset to the bootstrap base. This leaves no modification on PR #733.

Therefore an independent Lean compilation was **not established**. This is an execution-infrastructure `BUILD_FAILURE`, not evidence that a particular theorem is false. It is nevertheless an integration blocker because the assignment expressly requires an exact-head build.

## Static trust audit

The complete 20-file PR diff was inspected.

- `sorry` occurs only in the two statement-only `Challenge` modules, matching bootstrap policy.
- No `sorry` or `admit` appears in the added `RiemannFormal`, `Solution`, or `ChallengeDeps` source.
- No custom `axiom`, `opaque`, or `unsafe` declaration appears in the added trusted source.
- `Solution` imports `ChallengeDeps` and the formal library, not the `Challenge` modules.
- `RiemannFormal.Arithmetic.ComparatorSmoke` imports `Solution`, not challenge-side sorry. There is no direct sorry leakage, although this reverses the intended one-way comparator layering and should be removed from the default formal library.
- No post-#707 scientific module is imported.

## Axiom-coverage defect

`RiemannFormal/Arithmetic/AxiomAudit.lean` and `comparator/PrintAxioms/ArithmeticFixedRows.lean` exist, but the authoritative bootstrap `scripts/check_axioms.sh` directly invokes only the global `RiemannFormal/AxiomAudit.lean` and `comparator/PrintAxioms/RH.lean`. Imported `#print axioms` command output is not a retained substitute for directly running the B-owned files. Several headline source-firewall declarations are also absent from B's print list.

Verdict: static source is trust-clean, but the required compiled axiom audit is incomplete.
