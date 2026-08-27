# formal-v0.1 — reviewed gold spine

This release consolidates the first reviewed Lean formalization wave for the
August 22, 2026 scientific integration. It is a kernel-checkable formal
substrate and dependency map, not a proof of the Riemann Hypothesis.

## Literal scientific and trust status

```text
Riemann Hypothesis: UNPROVED
Unconditional Lean theorem proving RH: NONE
Conditional Lean theorem concluding RH: PRESENT, with every open premise explicit
Trusted sorry/admit/custom axiom: NONE
Challenge-only statement placeholders: EXACTLY SEVEN
Post-PR-707 research: EXCLUDED
Heavy numerical campaigns: NOT RUN
```

## Frozen provenance

| Object | Exact lock |
|---|---|
| scientific release | `852d8aa05c701ea7818ce8a50543e68987fef5cc` |
| canonical scientific census | 139 claims through PR #707 |
| formal bootstrap | `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f` |
| Reviewer A | PR #734 at `ae0887b8125601c98dc809cffe01c7f1c78bb998` |
| Reviewer B | PR #733 at `6d42bbc31c81e7d6a03909e205b56f30f6f7b49a` |
| Reviewer C | PR #735 at `381a5a98ade7c6bad7122e5182c2fc07332dc747` |
| exact-head and combined audit | PR #755 at `8ef4b09093d8a1189c60287e70256aedda33b320` |
| Lean | `v4.33.0-rc2` |
| Mathlib | `51e6992efd06126df61a496bebf8f49482a4e129` |
| Zeta23 | `cec57f919ccf34e5fa5372b4ba332f7c848bbb6e` |

The independent rehearsal combined the three exact source heads from the
formal bootstrap and passed 58 of 58 serialized commands, an 8,806-job trusted
build, all 21 explicit comparator targets, all seven exact
Challenge/Solution theorem-type comparisons, the 139-row registry, and an
89-of-89 axiom audit. The retained axiom output contains only `propext`,
`Classical.choice`, and `Quot.sound`.

The finished reconciliation tree must receive one fresh exact-tree audit before
merge. The rehearsal result is evidence for the inputs and mechanical conflict
policy; it is not a substitute for auditing this release commit.

## What formal-v0.1 contains

### Analytic and Mellin lane

The release reuses Mathlib's `RiemannHypothesis` as the unique RH conclusion
and provides exact bridges to the pinned zeta infrastructure. It formalizes:

- Mellin dilation, fixed compact-kernel and two-term linear-combination APIs;
- fixed holomorphic-defect and nonvanishing-multiplier singularity transfer;
- the zero-safe logarithmic-box multiplier;
- reciprocal-zeta meromorphic-order and multiplicity interfaces;
- exact propositions for the missing tail-Mellin Landau theorem and
  subpower-negative-mass holomorphy theorem;
- an honest conditional theorem
  `RiemannFormal.Analysis.fixedDetector_negativeMass_implies_RH`.

The final theorem concludes Mathlib RH only after receiving every missing
analytic and arithmetic input explicitly. Neither exact Landau proposition is
installed as an axiom, and no fixed-detector negative-mass estimate is proved.

### Arithmetic and fixed-detector lane

The release formalizes at their reviewed scopes:

- the exact rows 2 and 3 common-zero exclusion;
- the fixed `5:3` numerator factorization and noncancellation;
- finite source-role, response/capacity, normalization, duplicate-label and
  parity firewalls;
- the exact `r` versus `2r²` native-promotion refutation;
- central-binomial half-divisor coefficients and the exact arithmetic-function
  convolution identity;
- generic finite first-owner, wavelet, shift and summation-by-parts helpers.

The complete labelled first-owner theorem, the native row producer, the fixed
`5:3` negative-mass estimate, the actual ratio-eight/factor-67 wavelet, the
full Abel–Mertens frame, and the quantitative half-divisor near-collision
packet remain blocked. The generic helpers are not advertised under those
stronger canonical theorem names.

### Xi, operator and refutation lane

The release formalizes:

- two- and three-point Pick algebra and the exact three-node determinant;
- finite reciprocal-concavity and divided-difference identities;
- repeated-node reduction to order-two positive semidefiniteness;
- exact reflected-orbit and finite reserve-allocation algebra;
- an actual-Xi order-three theorem with all external, convergence,
  multiplicity, tail and reserve inputs explicit;
- selected matrix, Schur, current, hyperbolic-block, square-root and polarized
  Gram firewalls.

The actual-Xi conclusion is positive semidefiniteness through order three only.
It does not assert positive definiteness, order four, or RH. The two
owner-approved `Nonempty (ActualXiReserveAllocation ...)` conclusions are
proposition-level existence wrappers for allocation data already carried or
constructed by the API; they add no hypothesis.

## Registry meaning

`formal/scripts/generate_registry.py` joins the canonical 139-claim scientific
registry with the sparse A/B/C formalization deltas. The generated map is the
authoritative claim-by-claim status surface.

The audited release expectations are:

```text
canonical claims:       139
canonical delta rows:    31
STATED:                   2
PROVED:                  10
PROVED_CONDITIONAL:       8
```

These counts do not say that the other 119 claims have been proved or even
fully stated in Lean. Most remain `UNSTATED`, `BLOCKED_LIBRARY`,
`BLOCKED_MATHEMATICS`, `REFUTED_FORMALIZED`, or otherwise conservatively
classified. Scientific review status and formal proof status remain separate.

`formal/registry/FORMAL_V0_1_THEOREMS.tsv` lists the release-facing
canonical and API declarations. `FORMAL_V0_1_EXCLUSIONS.tsv` records the most
important deliberate exclusions. The generated `FORMALIZATION_MAP.tsv`
remains the complete canonical source of truth.

## Comparator and trust boundary

There are seven Mathlib-only Challenge topics:

1. `RH`
2. `MellinAPI`
3. `ArithmeticRows23`
4. `FixedDetectorFiveThree`
5. `OperatorPositiveSchurRescue`
6. `XiPickThreeNode`
7. `XiPickOrderThreeConditional`

Every Challenge contains exactly one statement-only placeholder. The matching
ChallengeDeps and Solution sources are placeholder-free. The exact type audit
loads Challenge and Solution declarations in separate Lean processes and
normalizes only the exact declaration-name prefix and whitespace.

`Analysis.ComparatorSmoke` remains available for an explicit comparator build,
but is deliberately outside the trusted `RiemannFormal.Analysis` aggregate
import closure.

The fail-closed axiom audit discovers exactly nine committed print modules,
adds every nonempty A/B/C/C_API registry declaration, rejects missing or
unexpected output, and permits only the three standard Lean foundations named
above.

## Reproduction

From the repository root:

```bash
cd formal
lake exe cache get
cd ..
bash formal/scripts/run_formal_v0_1_release.sh
```

The release runner performs ordinary Lean compilation, statement comparison,
registry and source-lock validation, no-sorry checks and axiom inspection. It
does not run any historical zeta-zero scan, finite-field census, interval
campaign, or distributed mathematical computation.

## Merge and later work

Merge only the final reconciliation PR after a clean, byte-identical Codex
audit of its exact commit and tree. Do not merge PRs #733, #734, #735, #747,
#749, #750 or #755 as substitute source branches; they remain immutable
provenance and review records.

Wave two should begin from the merged and tagged formal-v0.1 release. Its first
objectives are exact statements for all 139 canonical claims, proof of the two
missing Mellin analytic propositions, the complete native arithmetic objects,
and a deeper actual-Xi/First-Hermite/Q4 formal library. Post-#707 research must
receive scientific review and integration before entering the canonical
trusted track.
