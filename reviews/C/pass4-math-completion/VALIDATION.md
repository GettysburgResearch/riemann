# C4 validation and exact execution boundary

## Mathematical controls

From this packet directory, with Python and SymPy installed:

```sh
python -B checks/math_checks.py --check checks/result.json
python -B -O checks/math_checks.py --check checks/result.json
python -B checks/validate_packet.py
python -B -O checks/validate_packet.py
python -B checks/test_rejections.py
```

The mathematical checker independently reconstructs 1,092 bounded controls:
17 symbolic identities; 18 rational constant certificates; 270 orbit-parameter
fixtures; 390 prefix/Pick packets; 11 spectrum-contract fixtures; 237 Mellin
domination fixtures; 128 Schur/energy fixtures; and 21 normalization fixtures.
The same finite data are checked in both modes. Repeated runs do not double the
mathematical coverage. Complete stdout/stderr hashes are in `evidence/`.

All calculations used for accepting these finite controls are rational or
symbolic. No actual zero census, upstream numerical producer, broad prime sum,
non-directed zeta evaluation or sampled actual operator sign is used. SymPy and
Python arithmetic are trusted by this checker; it is not a Lean or independent
kernel verification. The infinite arguments live in the proof notes, not in a
finite list of successful examples.

## Delivery validator

`checks/validate_packet.py` has an independent fixed inventory of files,
source pins, claim IDs, edge IDs, hypothesis nodes, exact declared scope and the
mathematical result hash. The manifest covers every file except itself. The
validator rejects missing/extra files, wrong hashes, duplicate rows, malformed
scope, source/claim binding mismatches, unknown premises, altered open-node
status and any route in the small recorded hypergraph that bypasses all open
premises to RH. It verifies references and explicit proof anchors.

This is a structural/integrity contract, **not a theorem prover or exhaustive
transitive source-closure scanner**. Pinning a source string to a literal does
not authenticate its external origin. GitHub exact-ref reading supplies the
source observation; the optional checkout checker below supplies a reproducible
object comparison when the full required Git objects are available.

The rejection driver runs 11 packet corruptions and nine mathematical-result
corruptions in each mode (40 separate expected-refusal CLI executions). It
includes re-sealed empty scope, omitted claims, duplicate claims, changed source
pin, promotion of an open node, unknown premise, missing/extra proof files,
changed proof bytes, empty manifest, Boolean/float count aliases, altered
constants, altered counts and duplicate JSON keys. Each refusal requires the
expected exit code and an explicit rejection prefix. This is not the original
C3 scanner, consumer or axiom parser suite.

An initial combined refusal-test orchestration hit its execution limit and is not
counted as a completed run. The final refusal tests were partitioned by suite
and Python mode. A placeholder execution-receipt file was present while they ran;
only receipts and their manifest rows were updated afterward. The final clean
package was revalidated in both modes. No scientific source, proof, checker or
scope flag was changed between those tests and final sealing. File authenticity
and mathematical correctness remain separate questions.

## Optional source-object check (not executed against a full checkout here)

```sh
python -B checks/verify_source_checkout.py /path/to/riemann \
  --mathlib-checkout /path/to/pinned/mathlib
```

This read-only command requires every listed historical commit to be present.
It resolves each exact commit:path, verifies the expected blob and recomputes
its Git object ID. It never fetches, executes upstream code or modifies a ref.
A missing source object is an error, not accepted absence. It does not expand
this pass's declared reading ranges.

## Explicitly not run

Lean, Lake, Comparator, Nanoda, all-history security/rights scans, original
paper PDF audits, repository-wide CI, earlier C suites, the prior A independent
seven-point certificate, #792 author checkers, actual continuum quadrature and
all-length arithmetic sign tests were not run. The Lean candidate is marked
NOT_COMPILED and kept outside trusted imports. The active environment has no
Lean/Lake executable, and direct GitHub DNS access failed; connector text reads
succeeded. No tool limitation is treated as a mathematical refutation.
