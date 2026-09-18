# Codex handoff: run, play, then extend

Copyable first-session task:

> Work on the Observatory branch, inside observatory/. Read README.md, AGENTS.md, VALIDATION.md and ROADMAP.md. Set up a Python virtual environment, install requirements-dev.txt, run the numerical/API tests, and start run.py on loopback. Exercise all six workspaces in a real browser, including exports, local save/replay, a pinned baseline, and cancellation. Do not remove security/numerical guards to make a test pass. Report exact environment and any untested platform/browser boundaries. Then implement the v0.2 native-origin/platform acceptance slice before broadening capability, or take a separately bounded 0.2-A/B/C workstream with its stated acceptance tests. Preserve result/source identities and keep ordinary numerical precision distinct from certification. Do not modify main or the scientific canon.

## Expected project layout

- `engine.py`: Spec, numerical registry, definitions, exact coordinates, reducer, result hash.
- `server.py`: local boundary, request checks, API and spawned numerical workers.
- `run.py`: one-command startup and JSON numerical CLI.
- `web/app.js`: experiment state, presets/controls, inspectors, replay and agent API.
- `web/charts.js`: numerical rendering, viewport/cursor interactions and PNG stamp.
- `web/style.css`: responsive visual workbench; no external assets.
- `tests/`: executable mathematical, reducer, payload, job and boundary checks.
- `scripts/browser_smoke.py`: normal-origin browser test plus explicitly labeled restricted bridge mode.
- `scripts/benchmark.py`: million-sample reducer stress test, not a UI throughput claim.
- `examples/`: portable request examples.

## Initial acceptance commands

From repository root:

```sh
python -m pip install -r observatory/requirements-dev.txt
python -m pytest observatory/tests -q
python observatory/run.py --compute observatory/examples/first-zero.json > first-zero-result.json
python observatory/run.py
```

In another terminal, after installing a Playwright browser:

```sh
python observatory/scripts/browser_smoke.py
```

Then test Windows/macOS startup, native JSON/PNG downloads and actual localStorage manually or in additional automated cases. These are not covered merely by the restricted bridge pass.

## Practical exploration recipes

- Change complex object between zeta, eta and completed xi around the first zero. Compare the phase picture with sampled values, and raise the grid/working precision independently.
- Inspect Euler cutoff dependence on either side of sigma=1 and with prime 2 omitted. The target remains the original zeta value, as labeled.
- Raise the Mertens curve to 200,000 while leaving the matrix prefix at 48. Confirm the interface cannot confuse those scopes. Then vary matrix size/width and inspect Q_A, Q_B and the signed cross term.
- Export a zoomed, selected experiment; change workspaces; import/replay it; check source/result IDs, selected sample and viewport.
- Inspect both enormous anchors as strings, and exercise /api/coordinates with nearby exact offsets. Do not wire the native zeta evaluator to huge heights.

## Known first-pass limits

Local single-user only; no validated ball provider, full explicit-formula implementation, coarse #891 import, complete zero certificate, persistent server artifact store, adaptive tiles, distributed jobs, arbitrary function uploads, or deployment. No React/TypeScript build is required by v0.1. Introduce one only with a concrete maintainability/interaction migration and functioning acceptance tests.
