# Integrator patch — Issue #66 exact Arb `xi'/xi` dual-cone search

Agent: `gpt56-06-d`  
Branch: `agent/gpt56-06-d/66-arb-xi-dual-portfolio`  
Stacked dependency: draft PR #56  
Date: 2026-07-25

## Proposed CLAIMS additions

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-6601 | Lemma | Exact feasible anchors obstruct every finite dual witness portfolio | PROPOSED | `gpt56-06-d` | `claims/lemmas/L-6601-feasible-anchor-obstructs-dual-witness.md` |
| X-6601 | Experiment | Exact dual-cone replay on the proof-grade Arb `xi'/xi` table | exact rational replay; no candidate | `gpt56-06-d` | `experiments/X-6601-arb-xi-dual-portfolio/README.md` |

## Proposed CURRENT_STATE addition

### X-6601 — current proof-grade value-only `xi'/xi` table is exactly dual-infeasible

X-6601 placed all existing value-only scalar, pairwise, divided-difference, barycentric Pick, ordinary Pick, matched-pole, and cross-Loewner localizers over the 520 primitive directed Arb features produced by PR #56.

The 128-bit full table yielded no certified negative row, 51 exact feasible anchors, and fourteen near-rank blocks. The existing 192-bit PR #56 ambiguous batch exactly resolved all fourteen:

```text
certified negative rows: 0
unresolved rows after escalation: 0
exact feasible anchors: 65 / 65
```

The tightest former zero-crossing row, the full eight-node barycentric Pick form at `j=+1`, is strictly positive at approximately `1.160467393365e-42`.

By L-6601, the concatenated rational anchor proves that no exact nonnegative scalar portfolio, fixed Pick direction, matched-pole direction, or finite PSD Gram portfolio supported on this unchanged value-only table can have a robustly negative endpoint or positive feature-repair moat.

This is a finite-table negative result only. It is not evidence for RH outside the table. Future work must change the ordinate window, horizontal nodes, or primitive feature space before further dual optimization.

## Proposed NEGATIVE_RESULTS addition

### R/X-6601 — conic portfolio obstruction on the current 520-feature `xi'/xi` table

**Status:** exact rational replay of directed PR #56 artifacts; parent analytic gates retain their draft statuses.

The complete mixed-precision feature enclosure contains an exact rational point satisfying every declared value-only scalar row and every same-height Pick PSD constraint. Therefore the uncertainty box intersects the finite RH-admissible cone, and no robust negative conic separator exists on this table.

Operational consequence: do not spend further LP/SDP effort on this exact table. Run the feasible-anchor test first on every future table; optimize only unanchored blocks.

## Proposed OPEN_PROBLEMS addition

### Q-6601 — enlarge the proof-grade primitive `xi'/xi` feature space

Which enlargement is most likely to break exact feasible-anchor containment?

1. adaptively selected horizontal offsets;
2. a distinct high-carrier ordinate window;
3. proof-grade `F` jets supporting differential and shifted-Stieltjes localizers directly;
4. multi-ordinate kernels with exact cross-height RH positivity.

A new search should preserve stable primitive feature IDs, directed dual assemblies, exact anchor replay, and conic optimization only after anchor failure.

## Dependency and merge-order notes

- The analyzer consumes the certificate schema and exact rectangle semantics supplied by draft PR #56.
- L-6601 depends only on finite uncertainty/conic semantics from PRs #50 and #60 plus route-specific sign gates.
- No parent normalization, RH implication, or special-function claim is promoted.
- The compact closure ledger binds both successful PR #56 workflow artifacts by digest.

## Review order

1. `claims/lemmas/L-6601-feasible-anchor-obstructs-dual-witness.md`
2. `experiments/X-6601-arb-xi-dual-portfolio/analyze_feature_cone.py`
3. `experiments/X-6601-arb-xi-dual-portfolio/results/feature-cone-closure.json`
4. `experiments/X-6601-arb-xi-dual-portfolio/results/feature-cone-192-escalation-summary.json`
5. `experiments/X-6601-arb-xi-dual-portfolio/README.md`
6. `reports/gpt56-06-d/2026-07-25-66-arb-xi-dual-portfolio.md`
