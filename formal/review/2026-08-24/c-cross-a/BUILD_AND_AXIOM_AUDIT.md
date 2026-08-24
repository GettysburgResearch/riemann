# Build and axiom audit

## Frozen target

```text
PR #734
head 92f70a3b49b9295b5efb88491107670065b03317
bootstrap 573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f
```

## Requested command suite

```bash
cd formal
lake exe cache get
lake build
lake build Challenge.MellinAPI Solution.MellinAPI

python3 scripts/generate_registry.py
python3 scripts/validate_registry.py
python3 scripts/verify_source_locks.py
python3 scripts/validate_blueprint.py
bash scripts/check_no_sorry.sh
bash scripts/check_axioms.sh
```

## Execution status

A dedicated review workflow was deposited to check out the exact target SHA and run this suite. No observable GitHub Actions run or commit status was attached to the frozen target or review head during this pass. The local execution environment has neither a Lean toolchain nor network access to GitHub/package hosts, so it cannot independently fetch the pinned cache.

The review nevertheless finds a deterministic source-level `BUILD_FAILURE` before the command suite can complete:

```text
formal/RiemannFormal/AxiomAudit.lean
  #print axioms RiemannFormal.Upstream.zeta23_bridge_preserves_RH
```

PR #734 replaces `formal/RiemannFormal/Upstream/Zeta23Bridge.lean` and no longer declares `zeta23_bridge_preserves_RH`. The exact target therefore contains a trusted reference to a missing declaration.

Consequences:

| Command | Verdict |
|---|---|
| `lake exe cache get` | no observable exact-head result |
| `lake build` | `BUILD_FAILURE` by missing declaration |
| `lake build Challenge.MellinAPI Solution.MellinAPI` | source looks isolated/sorry-free, but not reached in authoritative suite |
| registry scripts | not independently executed on an exact checkout in this environment |
| `check_no_sorry.sh` | static diff shows no trusted sorry/custom axiom; authoritative run absent |
| `check_axioms.sh` | cannot complete while top-level audit fails; also omits A's audit modules from its input |

## Trust findings

* No custom `axiom`, `opaque`, or `unsafe` declaration appears in A's changed files.
* `MellinLandauBoundarySingularity` and `SubpowerNegativeMassHolomorphy` are ordinary propositions and are passed as explicit proof arguments.
* `Solution.MellinAPI` imports `ChallengeDeps.MellinAPI`, not the sorry-bearing Challenge module.
* The statement-only Challenge contains the permitted placeholder.
* No post-PR-#707 theorem is imported.
* Mathlib and Zeta23 pins match the bootstrap lock.

## Axiom-audit coverage defect

A adds `formal/RiemannFormal/Analysis/AxiomAudit.lean`, but the canonical script still runs only:

```text
RiemannFormal/AxiomAudit.lean
comparator/PrintAxioms/RH.lean
```

It does not execute or parse:

```text
RiemannFormal/Analysis/AxiomAudit.lean
comparator/PrintAxioms/MellinAPI.lean
```

Importing a module that previously emitted `#print axioms` does not make those outputs part of the later top-level audit. The A-specific declarations therefore lack authoritative parsed axiom coverage.

## Final build verdict

```text
BUILD_FAILURE
NOT_INTEGRATION_READY
```

This verdict does not assert that every A theorem fails to compile individually. It records that the required trusted default target and mandated command suite cannot succeed at the frozen head as published.
