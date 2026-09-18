# v0.1 architecture and extension contracts

## Deliberate simplification from the programme

The programme suggested React/TypeScript as a long-term workbench option. v0.1 uses native browser ES modules plus Python. This is a deliberate delivery tradeoff: there is no npm install/build/CDN path to get a first useful instrument. There is still a real separation between numerical providers, transport, rendering, and experiment state. A later UI framework must preserve those contracts and produce a user-visible improvement, not become a prerequisite for research.

```
Spec (validated request)
  -> registry in engine.PROVIDERS
  -> pure computation in its own spawned process
  -> typed-by-schema JSON artifact + engine source hash + result hash
  -> app.js experiment state
  -> charts.js numerical display + separate event/inspector views
  -> save/export/replay and window.observatory.scene()
```

`run.py` provides loopback startup and an offline numerical CLI. `server.py` serves static assets and API endpoints from one origin. It starts at most two numerical processes, tracks deadlines independently of the polling browser, terminates cancelled/over-budget work, and keeps at most eight terminal jobs for at most 15 minutes. These are ephemeral transport records, not a persistent experiment store. Active jobs are cancelled when the server shuts down.

FastAPI endpoints that access Jobs run on the same event loop; they must not be casually changed to threaded sync endpoints without adding a synchronization design. Numerical work stays outside that loop. Completed artifacts are read over multiprocessing pipes. The bounds on individual requests constrain output size; this is a small local worker system, not a distributed queue.

## Core contracts

### Request

`Spec` rejects unknown fields, nonfinite numeric inputs and out-of-capability bounds. Its module selects one provider. It is currently a single flat model to keep initial extension simple; discriminated per-provider schemas are a v0.2 cleanup. The UI never sends expressions for evaluation.

### Result

Every result carries `schema_version`, `engine_version`, `engine_source_sha256`, full normalized `request`, `provider`, `precision`, `evidence`, definitions/warnings, data, and a `result_id` SHA256 over canonical JSON excluding the result_id itself. A result is a numerical artifact, not an accepted mathematical claim. Actual dependencies must remain reflected in the version/provenance if extended.

`series`: retained display vertices plus per-bucket sample counts, extrema, positions and sums. Null samples remain breaks. `grid`: either sampled complex values (including phase and magnitude) or a finite signed interaction matrix. `events`: a separately stored list with kind/status. `metrics`: exact strings/integers where appropriate, otherwise explicitly approximate values. `sources`: source-pinned imported material when used.

### Browser state and replay

Draft controls and computed requests are separate. An outstanding job uses a captured request. Generation IDs prevent cancelled or superseded responses from relabeling the scene. Plot viewports and selection belong to that displayed result; scene(), PNG stamps and DOM identity refer to its hash.

A portable export includes the numerical artifact, request, notes, supported viewports and selection. Import does not trust the numerical artifact: it revalidates/recomputes the request, checks the resulting identity, and restores supported view state from bounded values. It is not offline artifact-only rendering. Local notebook storage keeps request-level records only (12 most recent). Pinned baseline comparison is transient in v0.1.

### Display preservation

The reducer scans all finite input samples. Each bucket retains first, last, minimum and maximum vertices, their coordinates, count, signed sum and absolute sum. Buckets stop at missing-data boundaries. None of that establishes a continuous extremum, a zero census, or a bound on unsampled values. Separate approximate event producers declare their limitations.

A million-point reducer test demonstrates spike retention and finite aggregation only. It is not a multilevel tile store, a proof of asymptotic scalability, or a browser performance result. Adaptive complex tiles and certified contour rules are intentionally not simulated here.

## Adding a provider with Codex

For an additive real-curve provider:

1. Extend the module Literal and add only bounded, named parameters to Spec. Register a pure `provider(q, ctx)` function in PROVIDERS.
2. Return series/grid/events under the existing representation, plus a formula, warnings, metrics, and source details. Do not call a remote service without an explicit adapter/caching/provenance design.
3. Use exact integer/decimal representations when required. Use finite() to mask unsupported floating display values. Do not turn a ball midpoint into a certified scalar.
4. Add a module preset and declared controls in app.js. Reuse Curve or Field. Add cross-panel linking only for an explicitly identified common coordinate.
5. Add known-value tests and at least one refusal/adversarial case. Add a replay example. Update README capabilities and limits.

For a different kind of observable, design its schema first; do not wedge an eigenvector, zero census, or imported certificate into an unrelated float curve.

## Boundaries / remaining engineering

No directed rounding, arbitrary user plugins, durable artifact store, distributed compute, adaptive tile cache, authentication, shared accounts, concurrent-user fairness, accessible table equivalent of every plotted vertex, or production deployment is claimed. The charts offer keyboard interactions and textual inspectors but have not undergone a full accessibility audit. Native-origin browser, clean package installation, Windows/macOS, and remote CI validation remain explicit acceptance tasks.
