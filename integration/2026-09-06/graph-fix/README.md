# Conditional-API graph interpretation repair

Baseline: `main@c7069c1b49c1f46be42175271667917bedf17dfc`.
Status: tested proposed software repair; no new mathematical acceptance.
Authoring boundary: exact source files and the actual failing chain were
retrieved through the GitHub connector. A complete Riemann checkout and GitHub
write actions were unavailable in the authoring session. This receipt is not
a full-checkout PASS or evidence that the patch has been merged.

## Failure and correction

The old resolver filters on review verdict alone. It therefore treats
`EDGE.CONJ.SPARSITY_ENERGY`, whose type is `CONDITIONAL_API`, as an application:

```text
API.CONJUNCTIVE.SPARSITY_ENERGY
  -> OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS
  -> RH  [with API.MELLIN.SUBPOWER_NEGATIVE_MASS]
```

The first arrow is not justified. The row describes an available inequality;
its `first_missing_premise` is the unproved target itself. After D-F07's
endpoint repair the inequality bounds negative mass by an interior derivative
energy term plus both boundary contributions. The needed arithmetic bounds
are not proved merely because this deterministic inequality is available.
See the preserved [D repair](../../../reviews/D/REPAIRS.md), R7.

The resolver now interprets both the historical and current views using the
same rules. Only explicit application types can propagate a conclusion.
`CONDITIONAL_API` and `STRUCTURAL_USE` remain nonapplication records. Every
pipe-separated `first_missing_premise` ID is a required conjunct. Self-dependent
application records cannot bootstrap their own target. Unknown types and
unresolved prerequisite IDs fail closed.

Exported `premise_ids` contain all effective prerequisites;
`historical_premise_ids` preserves the original declaration. The output also
records `current_missing_prerequisite_ids`, `current_block_reasons`, and
`current_traversable`. Consumers must honor the latter. No historical TSV,
review packet, mathematical decision, or Lean source is edited.

This is not an unconditional ban on deriving OPEN-labelled nodes. The tests
include a genuine implication that derives such a node once its premises
hold. The RH-reachability assertion also remains active: deleting both the
edge-type and missing-premise safeguards from the failing chain must still
make the resolver abort. No hard-coded exception for this edge ID appears in
the production resolver.

The hardening wrapper's resolver hash is deliberately updated to the repaired
source identity. Its seven review-tree pins, six historical integration pins,
and eight other payload pins are unchanged. The original resolver and wrapper
remain in Git history at the baseline. The hardening checksum manifest changes
only its `verify.py` entry; historical execution reports are not relabeled.

The independent Windows-path correction uses `PurePosixPath` and
`posixpath.normpath` for Markdown/Git path keys, rather than host-dependent
normalization that emits backslashes. This was tested by simulating Windows
normalization, not by claiming a native Windows execution.

## Regression and evidence

`actual_chain.json` is an exact projection of the resolver-relevant fields in
four claim rows and two edge rows. It records the complete original table
blob IDs. In default mode the regression authenticates those complete tables,
checks the projection against them, reproduces the original false closure,
and runs the repaired resolver on all 139 claims, 36 edges and 43 decisions.
It does not fall back to fixtures when actual tables are missing.

```sh
python3 -I -S -B integration/2026-09-06/graph-fix/test_graph_dependencies.py
python3 -I -S -B -O integration/2026-09-06/graph-fix/test_graph_dependencies.py
```

The authoring environment executed the explicitly narrower `--fixture-only`
mode: 24 graph/path tests pass in each Python mode. The unchanged 29 hardening
contract tests also pass in both modes. Ordinary/optimized JSON outputs agree.
`EXECUTION.json` records these boundaries, tested source hashes, and the exact
abort reproduced using the original hash-authenticated resolver source.
Neither a full-registry run nor full-checkout validation was executed here.

## Full-checkout acceptance

First run the default real-table regression above and the existing
`hardening/test_verify.py` in both modes. Commit the patch on its own branch
before running the authenticated wrapper: it intentionally rejects working
bytes that differ from HEAD. Use an LF-preserving checkout so Git newline
conversion is not mistaken for the committed source bytes.

From the clean committed repository root, with new output directories outside it:

```sh
python3 -I -S -B integration/2026-09-06/hardening/verify.py --output ../riemann-graph-check-normal
python3 -I -S -B -O integration/2026-09-06/hardening/verify.py --output ../riemann-graph-check-optimized
git diff --no-index ../riemann-graph-check-normal ../riemann-graph-check-optimized
```

Acceptance requires `PASS_AUTHENTICATED_SCOPED_RELEASE` from both runs and
identical outputs. Until those commands actually complete on the real checkout,
the full-checkout release check remains outstanding. Do not substitute the
fixture marker `PASS_ACTUAL_CHAIN_FIXTURE_SCOPE` for it.

No license, distribution/privacy decision, visibility/access setting, branch
protection, or Actions setting is changed by this repair. No RH or formal-proof
completion is claimed.
