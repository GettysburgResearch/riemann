# Heat and First-Hermite

> **Current interpretation:** the remaining First-Hermite problem covers the **whole complement** of the proved positivity regions, including bounded centers with arbitrarily large heat parameters. The historical constant-four shorthand below is not a reduction to a single transition curve. Read the [current heat account](../CURRENT_RESULTS.md#operators) and the [full-domain correction, R10](../../../reviews/D/REPAIRS.md) before using these rows. Earlier positivity results keep their own stated ranges.

The following manifest and status cells are retained historical source records, not a replacement for the current interpretation.

## Integrated scope

**Strongest reviewed result:** Uniform-center no-go and unconditional First-Hermite regions.

**First open arrow:** Fixed-center signed heat / constant-four cancellation.

**Relationship to RH:** open nodes: OPEN.HEAT.FIXED_CENTER_PHASE, OPEN.HEAT.HERMITE_CONSTANT_FOUR

**Family state:** `live`

This packet contains 6 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `REFUTATION.HEAT.UNIFORM_CENTER` | `REFUTED_MECHANISM` | Uniform-center fractional heat cannot obtain a tunable exponent: Weyl displacement changes parity and conjugates the heat generator. | uniform center over vertical translates | None | PR #708 `eb1987502ef9` `review/2026-08-21/operator/CLAIMS.tsv` |
| `OPEN.HEAT.FIXED_CENTER_PHASE` | `OPEN_SUFFICIENT_FOR_RH` | A fixed-center phase-sensitive fractional heat estimate controls the pole-bearing signed source. | fixed center and source-faithful phase | None | PR #708 `eb1987502ef9` `review/2026-08-21/operator/CLAIMS.tsv` |
| `HEAT.HERMITE.COUNTABLE_CRITERION` | `VERIFIED_WITH_FIXES` | First-Hermite nonnegativity on a countable declared test family is an exact RH criterion. | declared countable family and complete explicit formula | State normal convergence, terminal-pair completeness, and explicit-formula hypotheses; do not inherit upstream Lean status. | PR #379 `589f1c05ccaf` `research/external/anthropic-zeta23/proofs/CONFLUENT_ZERO_HEAT_MONOTONICITY.md` |
| `HEAT.HERMITE.UNCONDITIONAL_REGIONS` | `VERIFIED_WITH_FIXES` | Broad-kernel, fixed-resolution exterior, and q<=(4-epsilon)loglog(2+\|x\|) First-Hermite positivity regions hold. | each epsilon>0; sufficiently large height, with fixed-resolution/broad-kernel companion results from PR #384 | State epsilon dependence, effective-threshold scope, and normalization. | PR #385 `ea2d7c26c1fd` `research/external/anthropic-zeta23/proofs/GROWING_RESOLUTION_FIRST_HERMITE_WEDGE.md` |
| `OPEN.HEAT.HERMITE_CONSTANT_FOUR` | `OPEN_RH_EQUIVALENT` | Signed prime-power cancellation holds at the First-Hermite constant-four boundary near n~(log\|x\|)^4. | global first-Hermite criterion | None | PR #379 `589f1c05ccaf` `research/external/anthropic-zeta23/proofs/CONFLUENT_ZERO_HEAT_MONOTONICITY.md` |
| `Q4.HEAT.PHASE_LOCKED_SUBLINEAR` | `CONDITIONAL_EXACT` | Fixed and sublinear-order phase-locked Q4-Hermite positivity survives with a repaired tail envelope. | fixed/sublinear order | Retain the repaired tail envelope and keep fixed/sublinear order distinct from uniform-center or all-order positivity. | PR #520 `41db5f783c75` `claims/lemmas/L-94050-q4-critical-adjoint-first-hermite-filter.md\|claims/theorems/T-94051-all-sublinear-first-hermite-frontier.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
