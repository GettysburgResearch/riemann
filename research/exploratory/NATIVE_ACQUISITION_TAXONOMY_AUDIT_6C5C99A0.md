# Independent metadata-successor audit: native acquisition

Verdict: **PASS for the metadata-only release repair at
6c5c99a0d2f2d2ecca5087da0fd171998b444d2b.**
No scientific source or assertion changes. This closes the arithmetic-contract
cleanup requested by the original independent audit; it does not close the
native source reconstruction gap.

Review date: 2026-08-31. Exact parent:
a9e1587c90321e2f54e0a3c08a5ca74a15879f3b.
Original scientific identity:
ac7fa9af27c3fbcb3314f3ed58c8eed35b318052.

The review was performed in a separate worktree based on the successor.
No frozen scientific files, release trees or remote refs were changed.
The only review additions are this note and the adjacent replay helper.

## 1. Exact delta and semantic identity

The parent-to-successor delta has exactly four modified files:

- native_tuple_source_acquisition.py: three CONTRACT entries added;
- native_tuple_source_acquisition.sources.json: the same three entries;
- native_tuple_source_acquisition.json: those entries, three artifact digests,
  and its payload reseal;
- tests/test_native_tuple_source_acquisition.py: one twenty-line test added.

The proof NATIVE_TUPLE_SOURCE_ACQUISITION.md is byte-identical.
All five scientific files at the review parent are byte-identical to their
original ac7fa9 scientific versions.

The only new contract is:

    arithmetic_class = "MIXED"
    components = ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"]
    rounding = "none"

Independent whole-module AST comparison, omitting source locations, proves
that removing exactly these three literal CONTRACT keys makes the new producer
identical to the old producer. No calculation, bound, type guard, source loader,
fresh-reconstruction rule, or executable dependency changes.

Independent canonical JSON comparison proves that the entire scientific
fixture is type-exact identical after removing only the three added contract
keys and artifact/payload seals. The entire manifest is identical after removing
only the three added contract keys. This comparison includes every tuple,
physical support value, history, polynomial coefficient, character and scope
field; it does not select a handful of sample values.

The test AST is identical after removing exactly
test_release_arithmetic_taxonomy. That test checks the three metadata values
and rejects six freshly resealed deletion/replacement attacks. Test count
changes from 32 to 33; all earlier tests are unchanged.

## 2. Authentication and acceptance checks

The independent replay reads frozen commit:path bytes using Git, rather than
accepting current artifact metadata. It authenticated:

- all eleven unchanged source Git-blob identities and LF SHA-256 pins,
  independently of the producer's hashing functions;
- the exact four artifact hashes at both old and new snapshots;
- both payload seals;
- all five successor local files against their frozen LF-normalized bytes;
- absence of C0 controls other than tab/newline and of C1/DEL in those files.

Successor fixture LF SHA-256:

    b490a58b6277b944ca85d92431c5fe6620127048dd7878ef74efb4ec29c0f6b8

Successor payload SHA-256:

    3bda029b82f8276b164bc5c56bb5c04be83d6a20bffc0f2b181fa89900b5bab2

The fresh review replay passed:

- 33 tests, normal Python: 12.644 seconds;
- 33 tests, optimized Python: 11.070 seconds;
- both producer --check runs;
- both --emit and both --emit-sources outputs, exactly equal to the frozen
  fixture/manifest after CRLF-to-LF normalization: four emission comparisons;
- twelve independently resealed metadata attacks per mode, including the
  six advertised deletion/replacement cases and six additional null, case,
  order, duplicate-component, scalar-component and boolean-rounding cases;
- Ruff lint and format checks, and git diff --check both from the exact
  review parent and from original authoring base 1904d20c to the successor.

The additional attacks do not mock the expected report or source loader.
Each invalid payload is sealed independently, then rejected by actual fresh
reconstruction. The same checks work under -O without relying on assertions.

Reproduce from this review tree or any tree retaining the unchanged successor
scientific files and frozen Git objects:

    python -B research/exploratory/native_acquisition_taxonomy_independent_audit_6c5.py
    python -B -O research/exploratory/native_acquisition_taxonomy_independent_audit_6c5.py
    python -B -m unittest discover -s tests -p test_native_tuple_source_acquisition.py
    python -B -O -m unittest discover -s tests -p test_native_tuple_source_acquisition.py

The helper emits deterministic JSON only after its structural, source, seal,
mutation, producer and emission checks succeed. It uses only the Python standard
library and Git; no FLINT, SymPy, numerical precision or rounding is involved.

## 3. Scientific boundary

This is a narrow successor review, not a fresh re-proof of the eleven source
notes. Their bytes and pins are authenticated and unchanged. The full proof,
producer, manifest, test and original independent review were read; the complete
fixtures were compared programmatically.

The prior scientific acceptance in NATIVE_TUPLE_SOURCE_ACQUISITION_AUDIT_AC7FA9.md
transfers without altered hypotheses. The new metadata accurately describes
the existing integer enumeration and rational finite polynomial integration.
It does not certify the undeclared native coefficient density or the analytic
source integrals.

In particular native_reconstruction_complete remains false and
native_zero_or_nonzero remains undetermined. Canonical Boolean cancellation
is still not the complete retained-gamma reconstruction; the original measure,
literal diagonal and corrected full-core ranges remain unchanged. No principal
moment bound, native signed conductor cancellation, or RH conclusion is added.
