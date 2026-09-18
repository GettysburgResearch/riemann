# v0.1 validation record

Status: software research preview. No mathematical theorem, analytic certification, primitive SARG26 replay, or RH acceptance is claimed.

## Baseline / source boundary

Additive directory against `main@f99d9e3908dde4865377c75d9ca051c1f545bf4f` (root tree `8bddd12122e8a772683c9ed0b37dbcb945036893`). The programme issue, root AGENTS and README, repository metadata/root inventory, and #891 source/status were inspected. This was not a census or numerical audit of the other research branches. A direct Git clone failed because GitHub DNS/network access was unavailable in the execution container; the connected GitHub API is used for publication.

The implementation is developed/tested as an isolated additive directory. No full repository validator, Lean build, other research producer, remote CI, clean package-index installation, or actual public deployment is represented as run.

## Executed environment

Linux container; Python 3.13.5; mpmath 1.3.0; FastAPI 0.128.2; uvicorn 0.48.0; pydantic 2.13.4; httpx 0.28.1; Node 22.16.0 for JS syntax checks. Numerical/API tests use real spawned worker processes. Package versions were already installed in this environment; attempting package-registry access failed DNS, so a clean dependency installation remains a platform-acceptance task.

## Numerical and API tests: 51 passed

`python -m pytest observatory/tests -q`

The suite covers bounded capability rejection, invalid/nonfinite input and unknown fields, exact huge-height decimal addition, Möbius divisor identities, sieve counts, zeta/eta/xi and two Dirichlet-L known values, xi removable values, Li/R comparison against mpmath calls at seven scales, spike/alternation/missing-region reduction, reduction-independent event lists, complete finite cross-term accounting, finite Euler products/omission, underflow/nonfinite masks, initial approximate zero values/gaps, deterministic canonical result hashing for all six providers, and imported pending-state retention.

HTTP tests cover static assets/schema/security headers, Host/origin/client-header checks, 16 KiB request limit, validation refusals, a real process job, concurrency refusal, actual cancellation/termination, deadline termination, unknown jobs, and exact coordinate API output. These tests do not authenticate arbitrary mpmath computations or substitute for independent mathematical review.

Both browser ES modules were syntax checked using `node --check`.

## Browser exercise: six workspaces, with a declared harness substitution

A native Chromium navigation to localhost was blocked by the container's managed browser policy (`ERR_BLOCKED_BY_ADMINISTRATOR`). The browser policy was not changed. The successful run used the explicit `--bridge` mode in `scripts/browser_smoke.py`:

- Actual HTML/CSS and application JavaScript executed in headless Chromium with real canvas/DOM interactions.
- A Python HTTP bridge sent the browser's API operations to the actual live loopback FastAPI server and real spawned numerical workers.
- Source ES modules were combined in memory by removing their import/export wrappers for this restricted harness.
- Browser localStorage was replaced with an in-memory Map because the harness used an about:blank document.

The run exercised all six workspaces, clicked a sampled field and a curve, zoomed, saved a request/notebook record, exported an in-memory experiment packet, replayed it, and verified equal result hash, restored selection and viewport. It tested a changed-sigma pinned baseline, draft-control separation, actual cancellation, a later successful computation, structured scene/DOM result-ID agreement, exact-height endpoint text, desktop screenshots and a 390-pixel mobile layout with no horizontal overflow. No JavaScript page errors were reported.

**Not covered by that pass:** native-origin ES-module loading and browser fetch/CSP behavior, actual browser localStorage durability, OS download dialogs/PNG and JSON file downloads, Windows/macOS/Safari, mobile touch behavior, full accessibility, or remote CI. The normal smoke mode is supplied for Codex to close that acceptance gap on an unrestricted local browser. Static/HTTP behavior was separately exercised through the API tests.

## Reducer stress test

`python observatory/scripts/benchmark.py`

One observed run reduced 1,000,000 alternating samples with one exceptional spike to 3,000 display vertices and 1,000 summaries. The spike, counts, and signed sum were retained. Observed runtime was approximately 8.31 seconds with tracemalloc enabled; additional traced allocations were about 0.93 MB. Source arrays were allocated before tracing. These are measurements of that Python summary workload on this container, not end-to-end UI performance, total-memory usage, a disk-tile benchmark, or a scalability guarantee.

## Known fixes caught during this pass

The tests exposed mpmath 1.3's cloned-context zetazero requirement for its fast context; the worker now supplies it. Job table access stays on the event loop, avoiding a sync-endpoint/thread race. A post-await generation check prevents stale job responses from replacing a cancelled scene. Replays restore both the active inspection and previously selected field cells/plot ranges. Native float underflow is masked instead of silently turning a tiny nonzero value into a plotted zero.

Read the final PR receipt for the published commit and source verification. External review, clean installation, and native-origin browser acceptance remain separate from these author-run tests.
