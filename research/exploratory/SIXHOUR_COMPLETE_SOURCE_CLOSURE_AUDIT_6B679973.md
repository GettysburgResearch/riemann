# Independent audit: complete local manifest source closure

Verdict: **PASS for corrected workflow source
6b679973888841e56703ccf40ffe88e0574c1f01**, with the repair history below retained.
This is local provenance evidence, not mathematical acceptance or an acquisition
certificate. Review date: 2026-08-31.

Audited file: research/exploratory/sixhour_complete_source_closure.py.
Original reviewed source: 0c7c1192aa683daf6cc473fd168a7cf6cc7e3bb7.
The successor has that exact parent. The entire original script and successor
diff were read. No audited script or release tree was edited by this reviewer.

The resident review adds a separate Git-batch/BFS reference helper and 35
bounded tests. All reference identities below are full frozen commit hashes,
not local branch tips.

## 1. Found issue and independently checked repair

The original source() accepted a 40-hex Git tree object where it called the
identity a source commit. Concrete reproduction:

    source("31de5d7fa55e78462a95d22aec0cb6503b22d823", "README.md")

Here 31de5d7f is the tree of 0c7c1192, not a commit. The original returned the
same README bytes/blob as source(0c7c1192, "README.md"). The original also
accepted ./README.md as a second literal path for the same object.
This was reported before any author repair. None of the three supplied
regression panels used these malformed identities.

The separately frozen successor adds actual Git commit-type validation,
cached only after successful validation, at source() and both build() heads.
It also validates canonical relative POSIX source paths and the S/G programme
identity. It rejects empty paths, empty/dot/dot-dot components, slash-absolute
paths, backslashes, colons, ASCII control bytes and DEL.

The test suite retains the original tree-object acceptance witness and checks
that the successor rejects it as a source, head and base. Blob objects,
nonexact commit strings and strict type violations are also rejected.
The source change is limited to these guards; report schema, binding
precedence, source hashing and traversal are unchanged.

No assertion-based guard is relied upon. The corrected script uses
--no-replace-objects, preventing Git replacement refs from changing the
meaning of a frozen source identity.

## 2. Binding and traversal review

The supported binding semantics are explicit and tested:

- A dictionary with path plus commit is explicit; its commit wins over any
  document-level default, including when it declares no additional seal.
- A path with git_blob, sha256_lf or file_sha256_lf_normalized, but no commit,
  inherits only in riemann.atlas.generalized.* or
  graded-parent-global-boundary-sources-v1.
- Document-level precedence is imported_parent_state_commit, then
  source_commit, then base_commit. All seven nonempty combinations were
  tested. Nested defaults are not silently introduced.
- The archimedean-ladder-source-lock-v1 special record binds
  frozen_programme_path with its source_commit, frozen_programme_blob and
  frozen_programme_sha256_lf. An unknown special schema or incomplete
  special record aborts.
- Unknown sealed implicit rows abort; plain unsealed paths are outside the
  declared binding grammar and are not claimed as source dependencies.
- JSON pointers preserve list indices and escape tilde and slash. Every
  occurrence is an edge; repeated targets are deduplicated only in the
  source catalog. Identical bytes at two commits remain two source versions.

Roots are the .sources.json paths changed between the specified base and head,
not every manifest ever present in the repository. Recursion follows source
bindings whose target path ends in .sources.json. Seen commit:path manifest
versions stop cycles. Source-commit counts count commits in the referenced
source catalog, not automatically every root head.

The graph test includes a real cycle, a repeated edge and identical target
bytes at different commits. Exact expected counts are checked. Manifest and
edge caps are exercised at 1001 and 10001 respectively. Source byte cap,
read-size equality, independently computed Git blob identity and LF SHA
normalization are separately tested.

Both declared LF hash aliases must match if both are present. Bad declared
Git/LF hashes, including wrong JSON types, are rejected. Source caching is
appropriate because exact Git object identities are immutable; successful
cache reuse does not replace any mutable branch lookup.

## 3. Independent complete regressions

The reference helper does not call the audited source() or bindings() to
construct its expected graph. It uses git cat-file --batch, checks actual
commit and blob types, recomputes blob headers and LF SHA-256, and uses an
iterative FIFO breadth-first traversal. Its default-selection loop runs in
reverse priority, independent of the audited first-match implementation.

For each panel it independently compares all root paths, manifest catalog
entries and their seals/outgoing counts, referenced commit lists, complete
implicit-resolution lists, and both full edge/source-catalog digest values.
This is stronger than checking six aggregate counts.

| panel | roots | manifest versions | edges | source versions | source commits | implicit edges |
|---|---:|---:|---:|---:|---:|---:|
| old G | 27 | 43 | 246 | 104 | 27 | 75 |
| combined S | 32 | 37 | 259 | 113 | 41 | 1 |
| combined G | 35 | 55 | 341 | 147 | 43 | 75 |

Exact panels:

- old G head 7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e,
  base 10446e8ea9c55162c317810f63c1f7a379466459;
- combined S head 245943ccd1b381e2ca80625546a6851e85978057,
  base b870366141fe8d5f43d5b81f6e50a67d2a888070;
- combined G head 3f5441b26d7f2e64247a4e4d52eb82eb7e27dbb1,
  base 10446e8ea9c55162c317810f63c1f7a379466459.

Frozen report payload SHA-256 values:

    old G:      50598a03ca26b8739b13967c0349b34d1907277d7552873d7168557cc2eeff3d
    combined S: 1b76ecb50e7575be3d30456a8c5c1543addc88289a3c9b18be670def70bcdb54
    combined G: ab5990b10416dbfc50e6ba12959dfeec1345ea0a24a9d8f5a2bf144f8c60d6db

The original 0c7 script also reproduced all three expected count sets.
The corrected version preserves them. The expanded coverage does not rewrite
or falsify the earlier explicitly narrower provenance audit: its unsupported
inherited/special conventions are now included.

## 4. Replay and adversarial controls

The 35 new tests passed:

- normal Python: 3.020 seconds;
- optimized Python: 2.831 seconds.

The full independent three-panel reference comparison passed normal and -O.
Ruff lint/format and parent-to-successor/review whitespace checks passed.
The review uses the standard library and Git only; no FLINT, SymPy, external
papers or network acquisition is needed.

Controls cover duplicate keys at both JSON levels, floats/exponent notation
and nonfinite numbers, malformed UTF-8/JSON, nonobject manifests, commit/blob/
tree types, canonical path failures, missing objects, all declared hash fields,
source/manifest/edge caps, pointer escaping, precedence and special schemas.

Three freshly resealed report mutations also exercise the CLI's type-exact
canonical comparison, including integer/boolean collisions. That unit test
stubs the fresh build result to isolate the comparison; the separate full
reference regressions validate actual unmocked builds and source reads.
The note does not mislabel this comparison unit test as an independent
reconstruction of forged primitive objects.

Reproduce:

    python -B -m unittest discover -s tests -p test_sixhour_complete_source_closure_independent_audit.py
    python -B -O -m unittest discover -s tests -p test_sixhour_complete_source_closure_independent_audit.py
    python -B research/exploratory/sixhour_complete_source_closure_independent_audit.py
    python -B -O research/exploratory/sixhour_complete_source_closure_independent_audit.py

The helper first checks the local audited script against the frozen successor.
It prints each panel's counts and full graph digests, then a final PASS only
after all independent comparisons and payload seals succeed.

## 5. Scope that remains outside this report

"Complete" means the documented local manifest-binding grammar and its recursive
closure from these roots. It does not mean arbitrary prose citations,
executable import dependencies, all repository conventions, remote reachability
or reproducible acquisition, external-paper authentication, or scientific
validity of the source documents.

Explicit rows without declared seals are still resolved to exact local Git
bytes and catalogued; no missing independently declared seal is invented.
Missing/malformed objects and declarations abort rather than yielding a
successful partial report. Some malformed structures raise a Python/Git
exception rather than a custom ValueError; this remains fail-closed.

No source-fetch, publication, PR mutation, release-tree merge or mathematical
claim was made by this audit. Source interfaces, native capture, and RH remain
at their independently stated scientific boundaries.

