# Validation and review record

Status: **SOURCE INTEGRITY VERIFIED; SELECTED EXACT ALGEBRA VERIFIED; FORMAL BUILD NOT RUN.**
Date: 7 October 2026.
Upstream commit: **adc7f1241b42e322a6451854ab7e4b4c146bf78a**.
Repository base: **f99d9e3908dde4865377c75d9ca051c1f545bf4f**.

## What was executed

| Verification | Result | Exact scope |
| --- | --- | --- |
| Mirrored files versus the complete selected frozen Git tree | PASS: 3,286 files, 40,874,019 bytes | Every selected path, Git blob, SHA-256, byte count and executable mode; complete selection checked for omissions and extras |
| Importer/verifier adversarial fixtures | PASS: 15 temporary cases | Detects omitted files/manifest rows, duplicates, wrong mapping/pin/repository/count, symlinks and mode changes; confirms preflight rejection and importer round trip |
| Internal Lean dependency walk and lexical scan | PASS: 3,232 modules, 556,376 lines, 28,073,418 bytes | Three actual implementation roots; no missing internal imports or scanned tokens after comments/strings are masked |
| Upstream finite algebra checkpoints | PASS: 27 selected checks | Exact rational and polynomial identities, including 14 finite split-prime Gauss-conversion cases |
| Hybrid exponent budget | PASS | Exact conditional energy, MHB32 and CAP36 exponents; hypothetical recurrences remain assumptions |
| Manuscript and comparison reviews | No substantive error found in reviewed portions | Two separate mathematical readers checked the new exposition and conditional deductions against the pinned source; formal reviewer checked signatures and assembly |
| Original manuscript/PDF/source preservation | PASS | Original files copied byte for byte with their licenses and notices |
| New Markdown navigation | Checked | Project-created relative links resolve within the packet; original upstream catalog links retain their original full-repository meaning |

The source manifest's SHA-256 is **a0a35f01a37a6f4b4d65a76a00fd551832232e7be290e710ea4caeb011879a97**. It records each copied file's original path and Git blob as well as its SHA-256. A manifest alone is not authenticated provenance; the executed source-aware check also compared its entire selected set with the frozen upstream Git tree.

Machine-readable results:

- [Import integrity](checks/artifacts/import-integrity.json).
- [Importer/verifier fixture checks](checks/artifacts/source-integrity-fixture-results.json).
- [Internal formal-source audit](checks/artifacts/formal-dependency-audit.json).
- [Selected upstream algebra](checks/artifacts/checkpoint-results.json).
- [Conditional exponent bookkeeping](checks/artifacts/hybrid-exponent-budget.json).

## Reproduction commands

From this packet's directory:

~~~sh
python checks/verify_import.py --source /path/to/openai-math
python checks/verify_upstream_checkpoints.py
python checks/audit_lean_sources.py --output checks/artifacts/formal-dependency-audit.json
python checks/hybrid_exponent_budget.py
~~~

The optional source checkout must contain the pinned commit. To reconstruct the original mirror from a checkout at that commit:

~~~sh
python checks/import_upstream.py /path/to/openai-math
~~~

The importer performs a full preflight and verifies the selected source blobs before writing. It does not fetch or execute upstream code. Its selection contains the entire three manuscript directories, both complete implementation directories, and the complete compatibility-patch directory, plus the listed source and build metadata.

Use ordinary Python execution for the exact algebra scripts. Their results are finite checks and exponent arithmetic; no script claims a universal analytic theorem from finitely many examples.

## What was not executed or independently established

- A fresh Lean kernel build, Comparator run, kernel axiom report or independent external kernel check.
- A recursive audit of the external Lean dependency source trees.
- A complete independent analytic verification of every line of the $7/8$ manuscript or the full $11/12$ proof.
- A rebuild of the original manuscript PDFs.
- A rerun of the inherited numerical campaigns or all repository-wide validation.
- A proof of the new native signed-allocation adapter, full coarse-covariance contraction, or any improved zero-free boundary.

The runtime has no installed Lean, Lake, Elan or Comparator executable. The supplied formal source is substantial and its exported statements are unconditional; absence of a local build must not be described as an analytic hypothesis in those exported statements. Conversely, source inspection and configured allowed axioms do not amount to a completed kernel run.

The lexical scan is a heuristic source audit. It looks for specified proof-hole and execution-escape tokens, checks internal imports, and retains the standard-function binding visible in the exported declarations. It does not elaborate Lean syntax, establish theorem equivalence, inspect all definitions semantically, or certify external dependencies.

## Next formal verification

Use a fresh working copy of the imported Lean source, its original Lake files, and all patches. This keeps the source mirror suitable for the strict integrity check. The upstream toolchain is Lean **v4.34.1**; the exact package revisions are in the original manifest.

Install the verifier tools named in the [upstream Comparator instructions](upstream/lean/ComparatorChallenges/README.md), then run the four targeted configurations:

~~~sh
lake update
lake exe cache get
lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json
lake env comparator ComparatorChallenges/DirichletSevenEighths.json
lake env comparator ComparatorChallenges/HeckeSevenEighths.json
lake env comparator ComparatorChallenges/SiegelZeros.json
~~~

Preserve logs, dependency-lock changes, theorem-equivalence results and actual axiom reports. The original Lake configuration resolves additional packages used by the wider collection; all of its required compatibility patches are retained. The copied implementation subset is for these targeted builds, not the entire collection's aggregate library target.

## Mathematical review scope

The external-source reviewer inspected the theorem chain, the ordinary Mellin contradiction, family-wide supremum continuation, the constant-mode normalization, the two-Poisson support cancellation, the marked/plain moment interfaces and the final endpoint certificate. The shorter Siegel-zero argument was read through. No specific defect was identified in those portions. The audit explicitly lists the longer analytic obligations still requiring full verification.

The repository-comparison reviewer read the current remote mathematical files behind PRs #901, #903, #904, #905 and #907. It verified their current heads and draft/unmerged status, reconstructed the exact native coarse target, checked the conditional CAP36 deduction and identified the failure of the existing MHB32 exponent map to improve the imported seed.

Both mathematical readers then checked RESULT_AND_PROOF.md and the conditional research explanation. They found no substantive error; wording was tightened to specify the actual individual bound from a family mean square, exclude poles in the zero supremum, and treat the CAP36 observation condition as sufficient rather than necessary.

These reviews support the new explanation and the recorded conditional deductions at their stated scopes. They are not external peer review or promotion of the imported mathematical claims to the project's accepted integrated corpus.
