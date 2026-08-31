# Six-hour S/G integration: independent provenance audit

Status: PASS for the two fixed combined heads below, with the historical
fixed-lambda audit-helper caveat retained. Workflow/provenance only:
this adds no mathematics, does not enlarge any accepted scientific scope,
and is not a substitute for the release owner's full test/proof review.

## Frozen targets and inventory

| Group | Combined head | Public baseline | Review heads | Added paths | PR-delta test modules |
|---|---|---|---:|---:|---:|
| S | 245943ccd1b381e2ca80625546a6851e85978057 | 1904d20cdb76ecd26e0e63472625da930075303e | 11 | 81 | 32 |
| G | 3f5441b26d7f2e64247a4e4d52eb82eb7e27dbb1 | 7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e | 9 | 59 | 35 |

Every listed review head is an ancestor of its combined head. Each combined
public-baseline delta is exactly the union of its review-head additions:
no missing files, unexpected files, modifications to baseline files, or
unreviewed final blob versions. The JSON records every path, combined Git
blob, and supplying review-head versions. The only differing scientific
versions among those reviewed heads are the intentional four-file FC and
three-file HC metadata successors. Ordinary merge ancestry preserves the
original scientific identities and preregistrations.

The 32/35 module counts use the original PR bases
b870366141fe8d5f43d5b81f6e50a67d2a888070 and
10446e8ea9c55162c317810f63c1f7a379466459, respectively. They are distinct
paths, not sums that double-count inherited tests. SC/QT and any later
release changes are outside these fixed targets.

## Reproducible manifest traversal

| Group | Root manifests | Manifest versions | Binding edges | Source versions | Source commits |
|---|---:|---:|---:|---:|---:|
| S | 32 | 37 | 258 | 113 | 41 |
| G | 35 | 49 | 266 | 102 | 34 |

A root is each .sources.json path changed from the original PR base.
A manifest version is the ordered pair (commit, path), even when
different pairs happen to contain identical bytes. Within each visited
manifest, every JSON dictionary occurrence with string commit and path
fields contributes one edge. Repeated references are counted repeatedly.
Referenced .sources.json files are traversed recursively, once per
version. Other source files are authenticated but not parsed as manifests.

This is an explicitly delimited manifest-binding closure: prose citations,
arbitrary executable imports, remote paper bytes, and references lacking
that field shape are not silently added to its edge count. Every referenced
source object exists locally; every supplied Git-blob and LF-SHA256 seal
matches. Source versions are also distinct (commit, path) pairs.
Deterministically sorted edge and source catalogs are committed through
their SHA256 hashes; each visited manifest has its exact Git/LF identity
and outgoing-edge count/hash in the report.

The script reads fixed Git trees/source bytes through no-replace-objects
Git commands, including git show at exact commits, not mutable S/G
worktree files. It checks fresh source-derived results against the complete
report, in addition to checking the report's own payload hash. Editing and
resealing derived JSON does not bypass primitive reconstruction.
The script/report/note are frozen by the enclosing audit commit, not by a
circular self-commit identifier.

## Executable metadata compatibility and the one caveat

The initial read-only audit actually ran merged-tree source authentication
for S HA/FC and G FI/CF/SD/MP. It also independently invoked
CF.source_payload(Budget()) and SD.native_source(Budget()); both validated
historical source reconstructions with newer local HC metadata present.
These are recorded prior execution observations, not operations secretly
rerun by this dependency-free inventory script. The release owner
separately owns all-module scientific test replays.

- HA reads historical FC data from frozen Git; its executable local-byte
  locks apply to unchanged BC/OA, not the newer FC metadata.
- FI reads the original HC fixture through frozen Git; CF compiles the
  frozen FI producer; SD compiles the frozen original HC producer.
- The original HC independent audit helper likewise reads frozen Git.
- The original xi_fixed_lambda_joint_independent_review.py deliberately
  requires the original FC fixture in the current local tree. At line 85
  of the fixed combined version, its required LF digest is
  504071292138882ad5192fc62f765edc5615c3140542c7f597651679ba682cdb.
  The reviewed metadata successor has a different fixture digest. The
  helper therefore raises "ValueError: current source fixture" in the
  combined tree. This expected failure was actually reproduced.

Replay that historical helper at review head
26201b3a7de6293ea47621f06b45dd9837521a20, original science
0e3fc9b482f0f115a49a6209ccbfeffae640014a, not as a combined-release
science producer. Preserve it unchanged. The inventory script
independently verifies its literal local-byte comparison and the two
different frozen fixture digests without importing FLINT.

## Interpreter split

Use the pinned native-Xi FLINT runtime for these five science modules and
their tests: off-axis certificates, box-count compression, fixed-lambda
joint compression, fixed-lambda heldout alignment, and Laplace low-pass.
Their names are recorded exactly in JSON. That runtime contains FLINT and
mpmath, but was independently observed to lack SymPy and NumPy.

Use system Python 3.12 for the remaining modules, including the global
odd-order saddle's SymPy dependency. G's higher-power chamber producer,
FI tests, and several independent review helpers also need SymPy. The
two S scouts add only mpmath. No other external package was found by the
fixed-tree import scan. This static scan is not a package-installation
certificate and does not resolve arbitrary dynamic imports. Do not alter
the pinned FLINT environment to force all modules through one interpreter.

## Historical remote reachability

Two source pins had no covering local branch/tracking-ref alias and are
not ancestors of fixed combined S. Read-only ls-remote on 2026-08-31
nevertheless confirmed:

- refs/heads/research/gpt56-pro/107100-xi-reverse-rolle-execution advertised
  cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57 itself.
- refs/heads/research/gpt56-pro/102700-half-divisor-defect-factorization
  advertised 59654c02d13545d6c8c0972315db2628e9efa1f6, which locally
  contains ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc in its ancestry.

Thus absence of local tracking aliases was not evidence of an unpublished
source. Offline replay authenticates those exact ancestry relations, not
future persistence of remote refs. Optional --verify-remote repeats the
exact advertisement check and fails if the observed values changed;
it never fetches. Both fixed combined heads and their historical source
objects must be available in the local Git object database for replay.

## Replay and boundaries

From this audit worktree, using standard-library Python and Git:

    python -B research/exploratory/sixhour_integration_provenance_audit.py --self-test
    python -B research/exploratory/sixhour_integration_provenance_audit.py --check
    python -B -O research/exploratory/sixhour_integration_provenance_audit.py --check
    python -B research/exploratory/sixhour_integration_provenance_audit.py --emit

The emitter writes canonical LF JSON to stdout only. The checker freshly
reconstructs both fixed targets before comparing the complete report.
Embedded hostile controls test duplicate/noninteger JSON rejection, depth
limits, payload tampering, fully resealed tampering, bool/integer
distinction, and binding-occurrence multiplicity. All decisive checks use
explicit exceptions, not Python assertions, and remain active under -O.

The normal and optimized self-tests and full fresh report checks passed.
The normal check also repeated both remote advertisements successfully.
Ruff lint/format checks passed. A separate read of the complete inventory
confirmed that all seven overlapping paths select the reviewed metadata
successor, rather than an older reviewed version.

No release tree, frozen science, PR, main branch, or remote ref was changed
by this audit. The separate audit branch adds only this note, the standalone
script, and its exact JSON report. A clean integration inventory does not
prove RH, any new analytic result, source alignment, full source closure
beyond the defined traversal, or passage of suites not actually run here.
