# Validation — v0.4 research preview

**Scope:** isolated software extension of v0.1 `f7e8518275203bfb796b82f91d1d652b5c9257a8`, confined to `observatory/`. No mathematical-canon change, independent proof review, remote CI success, public deployment, full-repository validator or Lean build is claimed.

## Executed checks

| Check | Actual result |
|---|---|
| Original extracted v0.1 subtree | Matched published Git subtree `4e3345da0d8518eb39e0b100fca19b065d18695b` before changes |
| Baseline tests before implementation | Original 51 tests passed |
| Final numerical/API/storage suite | **108 passed, 1 skipped**; observed final run 13.81 s |
| Optional FLINT | Not installed; native point-enclosure test explicitly skipped. No enclosure execution is claimed |
| JavaScript syntax | All four modules passed `node --check` |
| CLI | Linked-cancellation and Gaussian-explicit examples computed; exact-coordinate sample imported through `--import-series` |
| Actual service restart | A saved two-result investigation was fetched, the server terminated/restarted against the same data directory, and the fetched bundle remained equal |
| Chromium UI | All 12 numerical desks plus stored-data desk exercised in **bridge mode**, with no page errors |
| Capture/replay | Both result identities, full artifacts, selection and supported viewports preserved in tested cancellation export/inspect/reopen/recompute workflow; scene-plus-canvas image capture exercised |
| Refinement | Complex-grid sample refinement left the parent result intact and attached a separate higher-precision artifact |
| Stored data | Browser demo ingestion, indexed zoom and exact-coordinate/event inspection; independent 100,000-sample store benchmark below |
| Mobile layout | 390×844 Chromium viewport, no document horizontal overflow in the tested cancellation view; not a full mobile/accessibility audit |

The baseline hash tests were updated for the explicitly versioned schema-2 identity, and a separate test verifies that legacy schema-1 hashes are **not** silently repaired. Browser-number normalization is tested through an actual Node JSON parse/stringify round-trip. Tests use the real spawned numerical workers for each new module, not only mocked API responses.

The suite covers complete block/cross identities, source controls, split invariance of full energy, term-by-term differences, eigensystem reconstruction, frozen training selection independent of holdout location, independent Fourier/digamma integration checks, deliberate explicit-formula undertruncation, literal zero bands, character multiplicativity/induction, sequence membership, exact point input, request bounds, artifact corruption, duplicate JSON, restart-safe storage, gaps/events/extrema, indexed boundary queries and Host/origin/job guards.

## Browser limitation: bridge is not native acceptance

A real Chromium attempt to navigate `http://127.0.0.1:8765` failed with **`net::ERR_BLOCKED_BY_ADMINISTRATOR`**. Browser policy was not changed or bypassed. The explicit test bridge loads the application modules in isolated IIFE scopes, directs fetches through Python HTTP to the actual running server, and substitutes Map-backed localStorage. It exercises real DOM/canvas events and actual numerical/storage endpoints, but not native origin/module resolution, CSP enforcement, download durability or browser storage persistence.

The supplied smoke script supports both modes. Only native mode runs its actual download/storage acceptance section. Successful bridge canvas-to-PNG generation is not represented as a successful operating-system file download. Native-origin startup, clean installation, Windows/macOS/Safari/Firefox and comprehensive accessibility remain open.

```sh
python -m pytest observatory/tests -q
node --check observatory/web/app.js
node --check observatory/web/charts.js
node --check observatory/web/labs.js
node --check observatory/web/datasets.js
python observatory/scripts/browser_smoke.py --browser /usr/bin/chromium --bridge
```

Run without `--bridge` on an unrestricted local browser. Dependencies were available in the implementation environment; no clean package-index install is claimed. Optional FLINT must be tested in an environment where it is actually installed.

## Stored-data benchmark

Command: `python observatory/scripts/benchmark_store.py --samples 100000`.

Environment: Python 3.13.5, Linux 6.18.44 x86_64/glibc 2.41. One deterministic alternating synthetic source with one injected spike, a three-sample missing run and a separately indexed event. Observed:

- Import/index construction: **1.682 s**; SQLite file **10,371,072 bytes**.
- Full-range stored query: **0.0134 s**, **1,176 display vertices**, **0 original boundary rows** read.
- 801-sample local viewport: **0.00157 s**, **33 boundary rows** read.
- Spike, gap, event and finite/missing counts retained.

These are one-machine stored-query measurements, **not** browser frame rates, certified floating-sum bounds, a streaming workload or a billion-point claim. Imports remain capped at 250,000 samples. Many missing runs/events can require more vertices than the nominal target. The source and benchmark assertions are included; timing will vary.

## Numerical and trust boundaries

The Gaussian formula is a finite numerical implementation of a specified classical identity. Its tails/rounding/quadrature bounds are unknown, even where finite sides agree closely. Cancellation energies are full finite binary64 values for literal or explicitly synthetic coefficients. The generic Gaussian PSD kernel is not a repository-specific RH witness. Initial zeros, central values, sign candidates and selected eigenmodes are not independently certified censuses/ranks/witnesses.

Storage verifies content consistency and the tested accessed-record checksums; it does not authenticate an imported author's claims or prove an untrusted database has no missing rows. Exact anchors remain decimal strings. New provider source/dependency identities travel with results. The remotely published subtree is to be compared with the locally tested Git subtree before publication is reported; the PR records the actual commit/tree receipt.

The original v0.1 validation record is preserved at [docs/VALIDATION_V01.md](docs/VALIDATION_V01.md). It is historical, not the current feature or test inventory.
