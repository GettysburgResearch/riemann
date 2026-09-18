# Riemann Observatory — v0.4 research preview

A local, runnable visual laboratory for zeta, prime–zero relationships, arithmetic cancellation, L-function families and stored numerical data. **Twelve numerical desks plus an indexed-data desk.** This large pass implements useful slices across the v0.2–v0.4 roadmap; it does not claim every milestone is complete.

Start with **Linked cancellation**, the default desk. Change a block split, compare the literal Möbius source with a magnitude or synthetic control, select a discrepancy, and inspect every contributing term. Both complete experiments survive save, export, reopen and recomputation.

Programme: [#897](https://github.com/GettysburgResearch/riemann/issues/897). Earlier application: [#898](https://github.com/GettysburgResearch/riemann/pull/898). v0.2 follow-up: [#899](https://github.com/GettysburgResearch/riemann/issues/899). This preview builds on `f7e8518275203bfb796b82f91d1d652b5c9257a8` without changing the mathematical canon.

## Run locally

Use Python 3.11 or newer. From the repository root:

```sh
git fetch origin
git switch --track origin/feat/observatory-linked-labs-v0.4
python3 -m venv observatory/.venv
. observatory/.venv/bin/activate
python -m pip install -r observatory/requirements.txt
python observatory/run.py
```

If the local branch already exists, use `git switch feat/observatory-linked-labs-v0.4`. Do not discard uncommitted work to switch branches.

Open **http://127.0.0.1:8765**. There is no npm build, CDN, database service, API key, GPU requirement, or paid deployment. NumPy and SciPy are new dependencies in this preview; reinstall requirements after switching from v0.1.

Windows PowerShell, without needing to activate scripts:

```powershell
py -3 -m venv observatory\.venv
.\observatory\.venv\Scripts\python.exe -m pip install -r observatory\requirements.txt
.\observatory\.venv\Scripts\python.exe observatory\run.py
```

Select a different local port with `--port 8766`. The server binds loopback only and is unauthenticated. Do not expose it publicly or remove Host/origin guards. Windows/macOS native acceptance and clean installation remain unverified in the implementation environment; see [VALIDATION](VALIDATION.md).

## Five investigations to try

### 1. Where did the cancellation go?

Open **Linked cancellation**. Source A is literal μ; control B initially uses |μ|. Set the window, starting integer, block split, log-kernel width and weight exponent. Each side shows block A, block B, twice the cross term, diagonal/off-diagonal contributions and the full energy. A and B matrices share one color scale. The third matrix is their signed difference.

Click a matrix cell or a row in the discrepancy curve. The term table ranks **every contributor in that finite row**, retaining its integer indices, block membership, coefficients, two source terms and difference. Prefix energy includes every newly introduced cross term. Change the split: the ledger changes, but the full matrix/energy does not.

Controls include |μ|, deterministic hash-derived signs on squarefree support, a seeded permutation of the μ window, alternating signs on squarefree support, and literal Liouville values. Definitions distinguish changed signs, changed arithmetic locations, and changed support.

Select an eigenmode to inspect its coefficients, both source projections, modal energies and associated Gaussian kernel section. Near-floor or clustered eigenmodes are numerical, not certified witnesses. The Gaussian kernel is positive semidefinite by construction; its finite positivity is not a new arithmetic positivity theorem.

### 2. Compare, preserve, challenge

Pin a baseline, change width or the source control, and rerun. The comparison panel retains both full artifacts, exposes both requests, plots their first matching observable side by side, and subtracts only identical retained x coordinates. It does not interpolate mismatched data or infer a missing tail.

Add a name and observation. **Save investigation** writes to disk. **Export experiment** includes both results, notes, selection, supported viewports and attached refinements. Import offers two distinct actions: inspect saved data with integrity checks, or recompute the request(s). The original artifacts are not silently overwritten when numerical identities differ.

### 3. Search, freeze, hold out

**Disagreement search** scans a bounded width × split grid on one training window. Its score is the absolute cross-term difference divided by the two diagonal energies. It freezes the winning width and split before one evaluation on a disjoint holdout window. Every training trial is retained.

Click a trial to open its complete training comparison, or open the frozen holdout's term-level investigation. An alternative trial does not inherit the selected winner's holdout result. These are effect sizes, not p-values; repeated human retuning can consume a holdout.

### 4. One prime–zero formula, completely specified

**Prime–zero formula** uses `h(t)=exp(-a t²) cos(bt)` and one fixed angular-frequency Fourier convention. Move `b=log x`, change smoothing, prime-power/zero/quadrature cutoffs, or choose a zero band. Click a curve and select **Inspect selected b** to recalculate its term ledger.

The desk separately displays the pole terms, log-π contribution, gamma integral, prime-power sum, selected numerical zero sum, discrepancy and selected zero band. All finite prime-power and zero contributions are preserved. Trivial zeros are encoded by the gamma term in this convention, not counted a second time.

All five tail/error budgets remain explicitly **unknown**, not zero. A small finite discrepancy is not a certificate. See [the formula, derivation and truncation contract](docs/EXPLICIT_FORMULA.md).

### 5. Load data once; investigate different scales

Open **Stored data** and import its 4,096-point adversarial demo. Zoom into the spike or select an event. The data are stored in SQLite with persistent first/min/max/last summaries; viewports query these summaries rather than resending the whole array. Missing runs and registered events have independent indices. Per-sample inspection retains exact anchor, offset and exact decimal coordinate strings.

The x-axis is explicitly **original sample index**, not a rounded huge height. Imports are bounded to 250,000 samples / 24 MiB. Data provenance is required. This is not a billion-point tile service, arbitrary file loader, or live huge-height zeta evaluator. [Import format and limitations](docs/STORAGE.md).

## Other desks

**Quadratic L-families** constructs real quadratic characters for ten named fundamental discriminants, compares selected members, and exposes conductor, modulus, parity, exact tables, numerical central values and the local factors removed in induced members. Central values are not arithmetic ranks.

**Reciprocal families** constructs integers, primes, repeated prime-index selections, their counts and reciprocal sums, plus a separate fractional sequence `a_n=n^alpha`. Index cutoffs and value cutoffs are distinguished. These are not the Golomb–Erdős or residue-avoidance self-sieves.

**Point refinement** accepts decimal-string coordinates for zeta, eta, xi, beta and the mod-3 L-function. Complex-geometry samples can be refined and attached to their parent investigation. Ordinary precision comparisons are not rigorous error bounds. An optional FLINT zeta-point enclosure adapter is included, but its native package was unavailable here; its test is skipped, not represented as passed.

The original **complex geometry, prime counting, finite Euler products, Möbius prefix, initial zero gaps and exact-height desks** remain available. The enormous-height desk still imports only two fine brackets from source-pinned #891, with primitive Hardy-Z replay pending. No fabricated Z curve or new record verification is added.

## Save location, CLI and agents

Default persistent data: `~/.riemann-observatory/`. Override with `--data-dir PATH` or `OBSERVATORY_DATA_DIR`. Back up the entire directory: objects, index and series stores. It is not a shared multi-user service, and there is no disk quota/garbage collector yet.

```sh
python observatory/run.py --compute observatory/examples/linked-cancellation.json
python observatory/run.py --compute observatory/examples/gaussian-explicit.json
python observatory/run.py --import-series your-series.json --data-dir ./my-local-data
```

The numerical CLI accepts a request, result envelope or exported investigation. Replay can differ across library/producer versions; identities include numerical source hashes and dependency versions.

```javascript
await window.observatory.run({module:'cancellation', n:64, split:24,
  width:0.8, source_a:'mobius', source_b:'random_signs'});
const scene = window.observatory.scene();
const bundle = window.observatory.exportExperiment();
const receipt = await window.observatory.save();
await window.observatory.openInvestigation(receipt.investigation_id);
await window.observatory.replay(bundle);
const capture = window.observatory.capture(); // scene + canvas images, same synchronous capture
```

Stable controls, explicit requests, selections, numerical inspectors and scene descriptions support computer use. Capture is a bundle of chart canvases, not an operating-system screenshot. Scene/result identifiers are not mathematical certificates. Generic comparison currently uses the first matching observable; dockable arbitrary cross-workspace linkage remains future work.

## Validate and extend

```sh
python -m pip install -r observatory/requirements-dev.txt
python -m pytest observatory/tests -q
python observatory/scripts/browser_smoke.py --browser /path/to/chromium
python observatory/scripts/benchmark_store.py --samples 100000
```

Actual implementation validation: **108 tests passed, one optional FLINT test skipped**, all four JavaScript modules syntax-checked, all 12 numerical desks plus stored data exercised in Chromium through a documented bridge. Native localhost navigation is blocked by this environment's managed policy; native-origin acceptance remains open. [Full validation](VALIDATION.md).

Read [Codex handoff](docs/CODEX_HANDOFF.md), [architecture](docs/ARCHITECTURE.md), [roadmap / completed versus open gates](ROADMAP.md), and [AGENTS](AGENTS.md) before extending. Pure bounded numerical providers, reviewed formulas and useful investigations take priority over framework churn.
