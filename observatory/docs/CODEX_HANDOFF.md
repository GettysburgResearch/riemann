# Codex handoff — linked Observatory research preview

## Start here

Branch: `feat/observatory-linked-labs-v0.4`. Base: v0.1 `f7e8518275203bfb796b82f91d1d652b5c9257a8` / PR #898. Work is isolated under `observatory/`; do not change main or scientific status files. The full roadmap is not complete just because the preview is named v0.4.

Read README, AGENTS, VALIDATION, ROADMAP, then docs/EXPLICIT_FORMULA.md, ARCHITECTURE.md and STORAGE.md. Start the app and use it before refactoring.

```sh
python -m venv observatory/.venv
# Activate it, or call its Python executable directly on Windows.
python -m pip install -r observatory/requirements-dev.txt
python -m pytest observatory/tests -q
python observatory/run.py
```

Open `http://127.0.0.1:8765`. Run the browser smoke script in a native browser. Its `--bridge` option documents a restricted test harness, not native-origin acceptance. Original implementation environment: Chromium blocked localhost navigation; 108 numerical/API/storage tests passed and one optional FLINT test skipped. Do not recycle those counts after changing code: rerun.

## A useful first session with Gideon

1. In Linked cancellation, compare μ with |μ|, then with hash signs/permutation. Change split and width; verify both block/cross identities and unchanged full energy when only the split changes. Click a difference cell, inspect its actual factors, select an eigenmode and its kernel section.
2. Pin a baseline and change a parameter. Save/export both artifacts. Reopen without computation and then recompute both requests. Compare identities and restore selection/view state. No silent interpolation in generic differences.
3. Run a bounded sweep, inspect a nonwinning trial and the frozen winner's holdout separately. Changing the holdout window must not change the training trials or frozen detector.
4. In the Gaussian formula desk, select a log-center and inspect prime powers, zero pairs, the band contribution, pole/logπ/gamma terms and all five unknown budgets. Deliberately use a small prime cutoff to expose the resulting discrepancy.
5. Refine a complex grid sample; confirm the parent result/selection survive and the higher-precision artifact is attached. Point precision is not a grid-cell certificate.
6. Import the stored-data demo; zoom and inspect the exact coordinate of a spike. Confirm gaps/events survive reduction. Then import a real bounded user dataset with accurate provenance and coverage.

## Best next assignable work

**Acceptance track:** native-origin browser, clean install, Windows/macOS startup, real downloads, accessibility, sustained race tests and local-disk recovery. Tests are already supplied but native environment acceptance is not closed.

**Mathematical track:** independent review of EXPLICIT_FORMULA and providers/explicit.py. Add actual rigorous tail/rounding bounds or the authenticated primitive zero adapter as separate reviewed changes, never by turning null into zero.

**Optional numerical track:** install and test FLINT point enclosures, then refine error contracts. Requested FLINT must fail visibly when absent; it must not silently fall back to mpmath.

**Instrument track:** user-selectable comparison observables and linked viewports, a source-pinned native repo operator/witness adapter, or one well-specified new family. Avoid rewriting the whole application solely to switch frameworks.

**Scale track:** start from benchmark_store.py, measured real datasets and import bounds. Add exact-height navigation or binary/streamed adapters with independent gap/event semantics. Current sample-index navigation is deliberate and must not silently become rounded huge-coordinate navigation.

## Review gates

Keep new providers bounded, source-hashed and separately testable. Preserve literal signed terms and finite scope. Retain both sides of a comparison, frozen detectors and negative trials. Do not confuse stored integrity with trusted authorship or a mathematical certificate. Keep deployment loopback-only and paid infrastructure out of scope. Publish a scoped PR with the actual commands, source SHA, observations and remaining failures.
