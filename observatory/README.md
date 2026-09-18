# Riemann Observatory · v0.1

A runnable, local visual research desk for programme [#897](https://github.com/GettysburgResearch/riemann/issues/897). Six workspaces, five analytic objects, cancellable numerical jobs, sample-preserving reduction, linked inspection, baseline overlays, and replayable experiments.

**Status:** implemented research preview; ordinary numerical exploration, not a certificate service or an RH claim. No public deployment has been made. See [VALIDATION](VALIDATION.md) for what was actually exercised, including the restricted-container browser-test boundary.

## Start here

Use Python **3.11 or newer**. No Node, npm, frontend build, database, API key, GPU, or paid service is required. The interface and API share one loopback server.

From the repository root on macOS/Linux:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r observatory/requirements.txt
python observatory/run.py
```

From the repository root in Windows PowerShell (activation is not required):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r observatory\requirements.txt
.\.venv\Scripts\python.exe observatory\run.py
```

Open **http://127.0.0.1:8765**. Stop with Ctrl+C. Use `--port 8766` when the default port is occupied. Installation commands need package-index access; after installation, all six workspaces run without external services or assets.

The application deliberately binds to loopback and rejects non-loopback Host names. It has **no accounts, authentication, or multi-user isolation**. Do not expose it publicly. For a remote workstation, use an SSH tunnel, for example `ssh -L 8765:127.0.0.1:8765 user@host`, and open the same loopback URL locally. Hosted Codex environments need a supported localhost browser/port-forward path; the local-only host check is intentional, not something to remove casually.

## First ten minutes

1. **Complex geometry:** the startup preset shows zeta near the first few zeros. Click a domain-color sample; inspect its actual sampled complex value and the matching height in the slice. Change the slice sigma, grid side, precision, or object. Five providers are available: zeta, eta, completed xi, Dirichlet beta, and the real character modulo 3. Hardy Z is always evaluated on the critical line, independently of the chosen zeta-slice sigma.
2. **Prime counting / Euler products:** compare pi, Li, R and their residuals; then watch a finite Euler product approach or fail to approach zeta as the prime cutoff grows. Try sigma=1.5 and sigma=0.5. Remove a local factor. The latter experiments are visibly marked as altered objects/outside absolute convergence, not as analytic continuation.
3. **Cancellation:** raise the Mertens prefix, inspect a signed Gaussian interaction matrix, change its width, and expand the energy metrics. The matrix uses its own explicitly labeled complete finite prefix, not the larger Mertens prefix. Inspect both block energies and the retained cross term.
4. **Zero spacing / exact-height desk:** inspect approximate indexed zeros and their gaps. Then view either imported fine bracket from #891; exact anchors remain decimal strings, and the display plots offsets only. There is no made-up Hardy-Z curve at enormous height.
5. **Preserve an observation:** zoom by dragging horizontally; use the buttons or arrow keys as alternatives. Click to pin a sample, name the experiment, add a question, and save locally or export JSON. Import re-evaluates the saved request, restores supported viewports/selections, and warns if the result hash differs.

Only related coordinates are linked. A prime cutoff, zero index, complex real part, and zero height are not silently treated as the same axis.

## What is implemented

| Workspace | Implemented views and data |
|---|---|
| Complex geometry | Sampled phase/magnitude field; Re, Im and modulus slice; critical-line Hardy Z; separately retained sampled sign-change candidates; pole/nonfinite masks |
| Prime counting | Exact integer sieve/pi; Li and R main terms; both counting residuals; normalized psi and theta residuals |
| Euler products | Re/Im/modulus by prime cutoff; distance to the original zeta target; full finite Argand trajectory; single-prime omission |
| Cancellation | Exact Mertens source and sums; harmonic signed/absolute sums; Gaussian signed interaction matrix; complete finite block/cross-term energy identity |
| Zero spacing | First 2–64 mpmath indexed zeros; full numerical decimals; raw and locally normalized consecutive gaps |
| Exact-height desk | Two source-pinned imported fine brackets; exact endpoint arithmetic; explicit primitive-replay-pending status |

Shared functionality: canvas plots with resize handling, zoom/reset and keyboard stepping; numerical inspectors; first-series baseline overlays; PNG exports with a scout/result-ID stamp; local request notebook; JSON result artifacts and replay; structured browser scene; numerical CLI; bounded API jobs with real process termination on cancel/deadline; schema/size/origin/Host checks.

**Baseline scope:** Pin overlays the first series of the current result when comparing within the same module. It is not a complete multi-experiment comparison manager. Browser notebook saves retain at most 12 request records. Portable exports include the result artifact. Replay intentionally recomputes rather than trusting arbitrary imported result JSON; it does not restore a pinned baseline or implement offline artifact-only playback.

## Numerical limits and honesty

- Analytic evaluations use mpmath 1.3.0 at 20–70 requested decimal working digits. They are **not directed-rounding enclosures**. Plotted numbers, grids, prime main terms and interaction kernels use binary64; changing dps does not upgrade those operations.
- Live analytic heights are restricted to `|t| <= 1000`, sigma to `[-4,4]`, domain grids to 80 by 80, and line samples to 2048. The native zeta provider does not evaluate at height 10^30.
- Prime/Mertens prefixes are capped at 200,000. Euler products are capped at prime cutoff 10,000. The interaction matrix is capped at 96 by 96. The job deadline is 60 seconds; narrow expensive requests when needed.
- Li and R use explicitly documented 80-term Ei/Gram series in the bounded arithmetic domain. Their implementation is compared with mpmath in tests, but no interval tail bound is supplied.
- Each plot reducer retains sampled first/min/max/last values and extrema locations; bucket metadata retains signed/absolute sums and counts. Missing samples remain breaks. This is **sampled-data preservation**, not a continuous-function bound or a zero-finding algorithm. Lines connect retained samples and are not fresh evaluations between them.
- Events are retained independently of line reduction. Sampled sign changes are not certified brackets and do not detect all possible zeros, including even-multiplicity events. A small zero table is not a certificate of all-zero completeness.
- Prefix counts are exact Python integers within these finite domains. Energy kernels and cross-term sums remain numerical, and no finite PSD conclusion is promoted to an infinite theorem.
- Exact-height endpoint addition uses decimal strings with enough working precision for the accepted bounded lengths. Its exact coordinate arithmetic does not certify the imported analytic claim.

The result identity hashes canonical result JSON, the request, provider/engine versions, and the engine-source SHA256. A matching hash authenticates bytes, **not mathematical correctness**. Different provider environments may yield a different replay hash.

## For Codex and other contributors

Start with [AGENTS.md](AGENTS.md), [docs/CODEX_HANDOFF.md](docs/CODEX_HANDOFF.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), and [ROADMAP.md](ROADMAP.md).

```sh
python -m pip install -r observatory/requirements-dev.txt
python -m pytest observatory/tests -q
python observatory/run.py --compute observatory/examples/first-zero.json > result.json
python observatory/scripts/benchmark.py
```

For a normal browser smoke test, leave the server running in a second terminal:

```sh
python -m playwright install chromium
python observatory/scripts/browser_smoke.py
```

A system Chromium can be selected with `--browser /path/to/chromium` or `CHROMIUM_PATH`. The explicit `--bridge` option is only for restricted test harnesses; its substitutions are described in VALIDATION, and it is not equivalent to native-origin browser coverage.

## Browser-agent API

In the browser console / a computer-use agent's JavaScript evaluation surface:

```js
await window.observatory.run({module: 'mobius', limit: 20000, kernel_n: 64, width: 0.8});
window.observatory.scene();             // displayed request, hash, viewports, selection, metrics
window.observatory.result();            // current computed artifact
const packet = window.observatory.exportExperiment();
await window.observatory.replay(packet);
await window.observatory.cancel();
```

The DOM root `#workspace[data-scene-id]` identifies the displayed artifact. Uncomputed control edits are separate from `displayed_request`. A screenshot's selection/viewport should be read together with `scene()`, not inferred from pixels alone. Every analytic result carries its scout status.

The HTTP schema is at `/api/openapi.json`, and executable request capabilities are at `/api/capabilities`. POST/DELETE requests require `X-Observatory-Client: v0.1`. This header is a local cross-origin guard, **not authentication**.

## Sources and licence

The code is covered by the repository's MIT licence. Mathematical function implementations are provided by mpmath; this suite does not claim their novelty. See the [mpmath zeta/L-function documentation](https://mpmath.org/doc/current/functions/zeta.html).

The exact-height panel transcribes only the two fine brackets from [news.txt at d5d55b7](https://github.com/GettysburgResearch/riemann/blob/d5d55b7950a4cc8a850e99c82b8f40e1699c7a3e/standalone/2026-09-15-s-argument-records/news.txt). The original announcement is credited in #891 to Avraham Eisenberg; that packet identifies its input as a user-supplied transcription. No source authentication, scalar checker, coarse-bracket census, or primitive Hardy-Z replay is newly performed by this adapter.
