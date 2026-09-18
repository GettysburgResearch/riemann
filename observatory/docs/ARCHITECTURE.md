# Architecture and extension contracts — v0.4 preview

The browser remains native ES modules and Canvas; the server remains one loopback Python service. NumPy/SciPy, SQLite and modular providers add capability without an npm/build/service stack. This is still an experimental desktop-oriented instrument, not a hosted multi-user platform.

```
Provider-specific validated request
  -> spawned, bounded numerical worker
  -> complete finite result + source/dependency identities
  -> linked views / selection / comparison / point refinements
  -> immutable result objects + investigation manifest + SQLite index

Imported sampled series
  -> strict decimal coordinates + declared provenance/coverage
  -> SQLite samples + multilevel summaries + independent gaps/events
  -> viewport query -> bounded display + exact sample inspection
```

## Numerical providers

`engine.py` retains the original six providers and dispatches the new providers in `providers/`. New requests use a Pydantic discriminated union in `providers/contracts.py`. Each has separate bounds; unknown parameters are rejected. The old six retain the original flat `Spec` to preserve request compatibility. Migrating those remaining models is a future cleanup, not something this release claims to have completed.

`cancellation.py` owns the complete two-source finite matrices, decomposition, eigensystem and training-only sweep selection. `explicit.py` owns the one Gaussian formula; its mathematical definition is in EXPLICIT_FORMULA.md. `explorations.py` owns quadratic characters, named sequence constructions and bounded point refinement.

The provider is a pure computation of its validated request. Neither an uploaded artifact nor a browser expression can execute arbitrary Python. Provider extensions require trusted source changes, review and tests. Add source files under `providers/` so `source_identity()` includes them automatically. Engine, identity and numerical provider hashes plus dependency versions travel with every new result.

The output contract remains JSON with `series`, optional `grid`, independent `events`, definition, metrics, warnings and provider-specific structures. Renderer-facing imported shapes are bounded and checked, but not every output field has a generated Pydantic model. Full typed result contracts remain an integration task.

## Job transport and local boundary

`server.py` keeps two spawned numerical workers with 60-second deadlines, explicit cancellation and a small ephemeral terminal-job cache. Jobs are reaped even if the browser stops polling. They are not the durable artifact database. Active jobs stop on server shutdown; completed data become durable only when explicitly saved.

Numerical worker requests are limited to 16 KiB. Investigation JSON is limited to 16 MiB; sampled-series imports to 24 MiB and 250,000 samples. A write lock serializes storage operations; parsing/indexing/hash work runs off the async event loop. This does not implement CPU fairness, user accounts, disk quotas or distributed scheduling. Trusted local imports can consume disk; keep an explicit backup/retention policy.

The service binds `127.0.0.1`. Host and same-origin/custom-header checks remain. Scripts/assets use the same origin; no CDN or arbitrary script upload is introduced. Do not treat these guards as public-server authentication. No shared/paid deployment is part of this PR.

## Browser modules and linked investigations

`charts.js` supplies Curve/Field rendering, keyboard selection and viewport controls. `app.js` owns submitted requests, dirty controls, jobs, saved state, comparisons and refinements. `labs.js` supplies the new mathematical desks and named selection semantics. `datasets.js` owns stored-series queries and their exact-coordinate inspector.

A cancellation selection identifies an actual row/cell or eigenmode. Its term table uses original complete finite arrays, not display-decimated values. An explicit-formula selection proposes a log-center; recomputation at that center generates a new term ledger. Sweep drill-down creates a new cancellation request; it does not repurpose the frozen winner's holdout claim.

A pinned numerical artifact is retained alongside the current one. The generic comparison view matches the first common observable and only identical retained x coordinates. It does not invent interpolation, restore an unavailable continuum, or implement arbitrary cross-workspace linking. Source A and control B within the cancellation desk have complete matrices and share a fixed color scale.

Higher-precision point results are independent identified artifacts attached to a parent. Refinement preserves the parent view/selection. The default grid-to-point action refines the selected binary64 sample coordinate, represented as a decimal string; it cannot recover more precise coordinates than the original grid stored. The standalone point desk accepts the user's exact decimal strings directly.

Generation identifiers prevent cancelled or superseded jobs from replacing newer data. Portable bundles preserve the current result, optional baseline, up to 16 refinements, notes, supported viewports and selection. Import offers **inspect** (validate hashes, preserve stored values) and **recompute** (run requests, compare new identities). Changing a producer/library may change identities even when mathematical values agree.

`window.observatory.scene()` exposes the displayed request rather than edited controls. `capture()` synchronously redraws and packages the canvases with that scene; it is not a screenshot of surrounding browser chrome. There is no independent global scene-revision/MCP protocol yet. Images from the stored-data desk are interpreted through its dataset identity, not a zeta result identity.

## Extension recipe

1. Write the mathematical object, domains, measure/transform conventions and finite/unknown boundaries first.
2. Add one bounded model to `contracts.py` and a pure provider returning explicit data. Register in `engine.compute` and the model union. Do not weaken existing bounds.
3. Add a named preset/control declaration and view in `labs.js`, or a small separate view module. Reuse existing renderers where the coordinate relationship is valid.
4. Add known-value/independent checks, negative/adversarial cases, replay tests and an example JSON. Update imported-result shape checks if the view consumes new arrays.
5. Exercise the app in a native browser when available. A test bridge is useful but not equivalent to actual origin, CSP, downloads or browser storage acceptance.
6. Record source SHA, commands, exact tests and omissions. Review finite experiments as finite experiments; do not alter the repository's mathematical canon.

## Deliberate gaps

Native-platform and clean-install acceptance; independent review of the new mathematical implementation; FLINT package execution; rigorous tails/census/region refinement; full result schemas; arbitrary operator adapters; dockable multi-workspace views; comprehensive accessibility; sparse/streaming/billion-point stores; MCP; public hosting/authentication; disk quotas/migrations/garbage collection. See ROADMAP for a prioritized continuation.
