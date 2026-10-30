# Chain131 v6 build: resource-guard stop

**Status.** The candidate at `43693463/50000000 = 0.87386926` did not complete its isolated dependency-closure build. It has not received a fresh kernel replay, an independent external kernel check, protected verifier or Comparator execution, or tracker admission. The following is evidence of a resource-guard stop, not evidence that Lean rejected the mathematical statement.

The preserved v6 manifest records 176 passed modules and one failed module in the affected closure. Its scope is an isolated changed-closure build with hash-verified reuse of previously passed v5 modules; this is not a fresh build of every imported dependency. After the resumed execution completed `Submissions.arvi_density.Return.Endpoint`, the builder started `Candidate.ChainExtension.Wiring`. It terminated the Lean process with exit status `-15` because its sampled resident memory reached `8456580 KiB`, exceeding the configured `8388608 KiB` sampled-RSS guard. The process was stopped after `20.309` seconds. The per-module Lean log is empty; no Lean diagnostic or proof rejection is recorded.

The evidence files below are copies of the source run records, not a new run:

| File | SHA-256 | Scope |
|---|---|---|
| [run-manifest-v6.json](run-manifest-v6.json) | `4f5fdcde11d433341d748e83e9b0132f42fe6fb50e553338916dd9a54aecdf3f` | Per-module records, source/object hashes, command and sampled resource failure. |
| [execution-v6-resume1.log](execution-v6-resume1.log) | `286650959b3c2657ad28122b530852421adfbe39c6436213df1016cdbc33f212` | Resumed execution log ending at the failed Wiring module. |
| [Candidate.ChainExtension.Wiring.log](Candidate.ChainExtension.Wiring.log) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Empty per-module Lean output. |

The manifest identifies its v6 plan as SHA-256 `cac55f696bbf9f594cd59296e409f41841c0b22e4c803501281a9a9a4e2b325b` and the reused v5 manifest as SHA-256 `5e6a0750cf1f8e415b1b2765a214355267cee935b99ad7d178da1984477e8b67`. These referenced source and object hashes are provenance claims in the original run record; this note does not authenticate the entire imported cache. The complete plan, compiled objects and compiler binaries remain outside this repository. The smaller `0.8738694` candidate and its separately recorded fresh and direct kernel checks have a different status; see [its packet](../../2026-10-29-return-retune-8738694/README.md).

The next step is to reproduce or resume the exact pinned source build under an appropriate resource budget with source, toolchain and cached dependency hashes checked. Only after a successful closure build can the prepared fresh-replay procedure be attempted; a successful replay would still be distinct from the protected challenge and tracker admission.
