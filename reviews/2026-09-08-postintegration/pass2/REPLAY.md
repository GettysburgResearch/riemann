# Executed review evidence and reproduction

The publication contains reviewer-written code and result receipts, not copies of the authors' numerical libraries. `EXECUTION.json` pins the local code and outputs. The original paper and executable bytes are independently identified by commit/path/blob in FILES.tsv. Full repository checkout, original package-wide test suites, Lean, Windows and remote CI are not claimed.

## Independent finite reconstruction

```sh
python -I -S -B independent_checks.py > independent.normal.json
python -I -S -B -O independent_checks.py > independent.optimized.json
diff -u independent.normal.json independent.optimized.json
```

Both modes pass 3,024 exact bounded assertions with identical output. This code imports no research module and uses integers and `Fraction`, not numerical spectra. The N=32 calculation reconstructs all 65 prime-power edges and eleven prime bases, proves three exact 31-pivot factorizations, and uses directed logarithm endpoints plus inverse order. Its tighter enclosure is **reviewer-produced finite evidence** corroborating the source's advertised bracket, not an automatically accepted stronger canonical statement.

The other groups reconstruct CRT/period means, rational tail consistency and centering controls, the full divisor form and tree, one-prime spectra, two physical-norm representations, exact multiplier piece integrals and fixed feedback atom. Finite substitutions do not machine-prove their infinite or all-parameter paper theorems. In particular the finite tail-overlap group is a consistency control, not an independent proof of the complete analytic tail inequality.

## Two pinned certificate calculations

Retrieve the exact source subsets into separate directories, using an LF-preserving checkout or `git show`:

- **WP:** from `31a35a90b0b924dc98a2c89c463fb59577f45a4e`, root `standalone/2026-09-06-logarithmic-core/window-one-positivity/`, take `intervals.py`, `verify.py`, `certificate.json`.
- **IE:** from `c4fb013692c51d6b26b8a3c33200615af764da82`, root `standalone/2026-09-08-astra-intrinsic-entropy/`, take `interval_core.py`, `certificate.py`.

`replay_certificates.py` requires all five exact blobs, rejects symlinked input components, compiles authenticated bytes, and rechecks them after execution. It uses no network and has no fixture-only fallback. Its input roots may be outside a Git checkout. That is intentionally a **source-subset** replay, not a complete package/checkout validator. All output names below must initially be absent.

```sh
python -I -S -B replay_certificates.py --wp-root /path/to/wp --ie-root /path/to/ie --case wp --output wp.normal.json
python -I -S -B -O replay_certificates.py --wp-root /path/to/wp --ie-root /path/to/ie --case wp --output wp.optimized.json
python -I -S -B replay_certificates.py --wp-root /path/to/wp --ie-root /path/to/ie --case ie --output ie.normal.json
python -I -S -B -O replay_certificates.py --wp-root /path/to/wp --ie-root /path/to/ie --case ie --output ie.optimized.json
python -I -S -B replay_certificates.py --wp-root /path/to/wp --ie-root /path/to/ie --case contracts --output contracts.normal.json
python -I -S -B -O replay_certificates.py --wp-root /path/to/wp --ie-root /path/to/ie --case contracts --output contracts.optimized.json
diff -u wp.normal.json wp.optimized.json
diff -u ie.normal.json ie.optimized.json
diff -u contracts.normal.json contracts.optimized.json
```

The WP result must also equal published Git blob `a94e20c9cbdb16e29fc95d5a95d6be9e660de2e5`. IE reproduces the whole fixed trial calculation and the tail, not its author package's source-lock/CLI rejection campaign. Both arithmetic cores are reused implementations, not independent replacements. The 213 additional contracts test rational primitive containment, zero division/type refusals, the actual WP certificate parser, strict output-type comparison and source mutation detection. Source-mutation hash detection is not described as a resealed semantic proof check.

The WP primitive audit used the classical formulas and analytic remainder bounds in the pinned paper/code, including [NIST DLMF 5.11](https://dlmf.nist.gov/5.11) for digamma asymptotics and error bounds. The zeta Euler–Maclaurin background is [DLMF 25.2](https://dlmf.nist.gov/25.2). These references are external analytic inputs, not machine proofs produced by the replay. No original PDF, zero census or external high-ordinate numerical oracle was used.

## Receipt interpretation

Each retained JSON is one representative of byte-identical normal and optimized runs; EXECUTION.json records both source output names and their hashes. Duplicate executions of the same calculation are not counted as independent certificates. Early direct subset executions and final wrapper executions agreed. The unsuccessful attempt to request a streaming container session was an orchestration limitation, not a completed test; no result is attributed to it.

No error bound, iteration speed or finite test count proves an RH-strength upper estimate. Author identity/referee independence is separate from code independence. The integration decision remains for a later pass and must retain these boundaries.
