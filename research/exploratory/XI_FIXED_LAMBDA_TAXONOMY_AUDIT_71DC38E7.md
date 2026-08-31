# Fixed-lambda Xi taxonomy successor: independent release review

Verdict: PASS, metadata-only successor. No scientific verdict is enlarged.

Original science: `0e3fc9b482f0f115a49a6209ccbfeffae640014a`.
Reviewed successor: `71dc38e7619409a27dd4d1973dec985b0e655a30`.
The full earlier mathematical/independent-numerical review remains
`26201b3a7de6293ea47621f06b45dd9837521a20`, resident note
`XI_FIXED_LAMBDA_JOINT_COMPRESSION_AUDIT_0E3FC9B4.md`.
This review concerns the exact successor delta and release assurance,
not another independent implementation of Xi special functions.

## Exact semantic comparison

Exactly four scientific files differ: proof, producer, fixture and source
manifest. Tests are byte-identical. The added contract keys are exactly
`arithmetic_class`, `arithmetic_components`, `rounding`, `source_quantifiers`.
Their values are identical in the producer, manifest and fixture.

The independent adjacent script removes only those four keys from the new
producer's literal CONTRACT and compares the complete AST with the original.
It is identical. Removing the single new metadata paragraph restores the
entire original proof text byte-for-byte after LF normalization. Removing
the four new keys restores the original manifest exactly. In the fixture,
only those keys and the independently checked artifact/payload seals differ;
all other fields, including the complete old contract, compare exactly.

In particular there is no change to lambda, its enclosure, the three boxes,
boundary arcs, root rectangles, source jets, any matrix entry, all five
compressions, the orthogonal-input increments, Gaussian-integer witnesses,
thresholds, caps, precision, source formulas or runtime. The original
preregistration and all six direct frozen source bindings are unchanged.
No rounding through JavaScript/binary64 was used in these comparisons.

The canonical scientific payload excluding contract/artifacts/payload seal
has the advertised identical SHA256

    18b2bd7d928ae50fd6ebaf9dc751424b71cd756931ae04dd17f717d83150e7df.

The stronger comparison above also preserves every pre-existing contract
field, rather than accepting arbitrary changes to the whole contract.
The new fixture LF-SHA256 is

    2059059f8510b50d0e1baec364b86377371d84bf9141ea05c7d2b2355c813cfb.

All five old/new scientific file hashes are retained in the review fixture.
Both payload seals and all four bound artifacts in each identity were
independently authenticated. The unchanged test LF-SHA256 is
`deb2696c5c160e0da970c31f35e5ed472baabc4fb1d3db831b4e48371935ae80`.

## Arithmetic and scope declarations

The top-level class MIXED is an accepted resident provenance-schema enum.
Its declared components distinguish outward directed-ball enclosures,
exact rational decisions, and certified finite integer coverage. The
wording does not recast scouts or approximate eigenvectors as certificates.
Finite evaluations retain their pinned-runtime trust, and the Hardy
interpretation still requires component innerness. No band, native outer
metric, cofinal or RH conclusion has been added.

The unchanged implementation still reconstructs from authenticated primitive
sources. Four additional fully resealed metadata mutations are rejected by
the exact checker comparison; these target each newly added key separately.
They use the already verified expected report to isolate metadata acceptance,
not four independent special-function replays. The complete unchanged44-test
suite and both producer modes below perform fresh source reconstruction.

## Replays

All checks used the existing source-pinned runtime at
`isolated/native-xi-pass3-runtime/Scripts/python.exe`: CPython3.12.10,
python-flint0.9.0, FLINT3.6.0, with44 native files and aggregate SHA256
`36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc`.
The first attempted default-Python invocation lacked FLINT and failed to
import; it was not counted as a replay. No runtime was installed or modified.

- Successor44 tests: PASS normally in76.782s and under -O in75.344s.
- Both successor producer checks and all four LF-exact fixture/manifest
  emit comparisons: PASS.
- Independent semantic/AST/source/hash review and four resealed metadata
  controls: PASS normally and under -O.
- Ruff lint/format and the full original-to-successor whitespace check:
  PASS. Scientific files were not edited in this review worktree.

The independent script authenticates all six direct Git blobs/LF hashes,
calls the unchanged transitive source/native-runtime authenticator, and
checks that every current science file equals the exact reviewed successor.
Its comparison arithmetic is exact, with no rounding; it does not compute
new Xi values or enlarge the finite regions.

Replay the metadata audit with the same pinned runtime:

    python -B research/exploratory/xi_fixed_lambda_taxonomy_audit_71dc38e7.py --check
    python -B -O research/exploratory/xi_fixed_lambda_taxonomy_audit_71dc38e7.py --check

The original root review's finite/conditional scientific boundaries remain
binding. This release cleanup fixes explicit arithmetic classification;
it neither repairs a mathematical theorem nor pays an onward analytic gap.
