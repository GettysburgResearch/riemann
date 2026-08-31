# Six-hour pass 3: final publication acquisition and replay

The scientific release and the fresh-network checks are separate evidence.
This report binds the exact fetched publication checkpoints below, not a
later documentation-only tip containing this report.

| Programme | Fetched publication checkpoint | Computational panel's scientific head |
|---|---|---|
| Riemann Structures | `408a9bd84a44d4878b957175516caddb81540f33` | `6bc9f5fc499fbdc4b9807b49975988f4fba67740` |
| Generalized L-objects | `64885db5848252b8f013a24333fa3c2462101dee` | `dde680d50358fb6d269485b1b8f61f23ba6b221e` |

## Acquisition and exact source checks

A new repository was initialized empty on2026-08-31 at16:48+03; an independent
reviewer personally verified its empty state at16:52. One literal HTTPS fetch
then acquired the two published programme heads and all40 exact archive refs.
The expected mappings were retained before that fetch.

The new store is independent of the author's original shared object store:
no alternates, grafts, replacements, shallow/promisor/partial-clone state or
object-directory overrides. Its pack and index are native files with
hardlink count1. The separate Structures checkout shares only this newly
network-acquired store. Strict full Git fsck passes.

All42 ref identities, all63 full result-map commit identities and the four
analytic proof/review seals pass. The first native-restriction corollary
remains identified by its reviewed content hash, not a fabricated original
science commit. The independent reviewer reran both declared manifest closures:

| Programme | Roots | Manifest versions | Edges | Source versions | Source commits | Inherited legacy edges |
|---|---:|---:|---:|---:|---:|---:|
| S |38|47|389|142|54|1|
| G |37|59|368|160|48|75|

See the [complete acquisition evidence](sixhour_pass3_network_acquisition.json)
and [independent acquisition review](SIXHOUR_PASS3_NETWORK_REVIEW.md).
The [initial timed snapshot](sixhour_pass3_network_acquisition_initial.json)
is deliberately immutable; its then-running replay status is historical,
not the final outcome below.

## Scientific replay, with scopes kept separate

| Location and scope | Normal | Optimized Python |
|---|---|---|
| Original isolated S release: full declared38-module suite |1056 tests +38 producer checks PASS|1056 tests +38 producer checks PASS|
| Original isolated G release: full declared37-module suite |962 tests +37 producer checks PASS|962 tests +37 producer checks PASS|
| Fresh HTTPS-acquired G checkout: full37-module suite |962 tests +37 producer checks PASS|962 tests +37 producer checks PASS|
| Fresh HTTPS-acquired S checkout: producer-only verification |38 producer checks PASS; no unit rerun|38 producer checks PASS; no unit rerun|
| Fresh closure-workflow regression suite, separate from science |35 tests PASS|35 tests PASS|

The fresh S check is expressly NOT a second execution of all1056 unit tests.
It reruns each of the38 producers' --check paths and authenticates all declared
test/producer files against the same panel. The fresh G run executes both
the962 unit tests and37 producer checks. Each run has a fixed observed HEAD;
the panel scientific head is separately verified as an ancestor.

Fresh reports:

- G [normal](sixhour_pass3_network_g_normal.json) and
  [optimized](sixhour_pass3_network_g_optimized.json).
- S producer-only [normal](sixhour_pass3_network_s_producers_normal.json) and
  [optimized](sixhour_pass3_network_s_producers_optimized.json).

The four analytic notes retain separate non-author proof reviews; none is
machine-proved by these replay counts. All declared input hashes remain unchanged. Reports retain commands,
interpreter selection, exit codes and output hashes. The complete producer-only
driver and acquisition verifier are retained as text in the evidence bundle.
All38 S producer output hashes also match the original run in each mode.
Ten G producers print absolute artifact paths: a separate20-case comparison
(normal and optimized) verifies that those stdout differences are solely the
checkout prefix, with unchanged stderr. No scientific fixture changed.
Runtime packages are pre-existing local dependencies; a network source fetch
is not a clean-room installation of Python, FLINT, SymPy or their libraries.

## Publication boundary

The original reviewed scientific commits remain in branch ancestry.
Later publication commits containing this report, replay outputs and handoff
clarifications add only documentation/evidence; they do not change the
scientific notes, fixtures, producers, tests or replay panels.

The PRs remain open drafts and were not merged. No archive ref was moved,
force-pushed or deleted. Acquisition is not a mathematical proof, an external
novelty claim, an audit of every arbitrary dynamic/prose dependency, or an
assertion that external primary papers were acquired by Git.

