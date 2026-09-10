# Scope and validation receipt

## Mathematical status

Q-AC28 is NOT proved. The completed note gives exact inverse coordinates and
an all-N native-polynomial counterexample to a proposed **auxiliary** norm
comparison. It does not refute the compensated polynomial inequality, supply
its degree-uniform constant, or improve an RH-strength arithmetic estimate.
All new mathematical statements remain PROPOSED pending independent review.
No previous source or canonical status is amended.

## Exact source

- Repository: GettysburgResearch/riemann; PR #845.
- Frozen head: b9ccd03a681a73e91fb7bbfb7a3b97766fe8285e.
- Source: standalone/2026-09-10-astra-safe-source-kernel/PROOF.md, Section 7.
- Locally supplied source Git blob: `5d4c2738f30b40b9b18874607ad061b5b096d7f3`; matches the recorded frozen
  source identity in the conversation. Live PR metadata was reread in this pass.
- Interval-code pattern and Machin/Bernoulli primitives are adapted from the
  source packet's check.py. This is not a new independent implementation of
  that primitive layer. The exact polynomial and divisor reconstructions are
  separately written here.
- Primary literature comparison: Luis Baez-Duarte, *A sequential Riesz-like
  criterion for the Riemann hypothesis*, IJMMS (2005), 3527-3537,
  DOI 10.1155/IJMMS.2005.3527. Publisher abstract/metadata consulted:
  https://onlinelibrary.wiley.com/doi/abs/10.1155/IJMMS.2005.3527
  The related odd-integer formulas are derived in NOTE.md; the published
  all-integer criterion is not silently transferred. No external PDF or code
  is redistributed, and no priority claim is made.

## Commands actually run

```bash
P=standalone/2026-09-10-astra-polynomial-proof-attempt
python -B "$P/check.py" --write "$P/results.json" --self-test
python -O -B "$P/check.py" --check "$P/results.json" --self-test
```

Normal, optimized (-O), and fully optimized (-OO) executions completed with
the same mathematical payload and eight resealed
corruptions rejected per self-test. The self-tests invoke the real acceptance
function; they are not eight separately launched command-line processes.
Expected data are regenerated from the primitive definitions, not accepted
merely because their hash is consistent. Explicit exceptions remain active
under optimized Python; floats, nonfinite JSON and duplicate keys are rejected.

Semantic SHA-256: `938ab655ad56925f41f6cb1166138b107f97e3e6e1e8eda2c1af9ee61e7d5a37`.

A final normal-mode replay completed with the same payload. Fresh-directory
patch application and replay are recorded in the enclosing publication receipt.

## Coverage

- 65 exact beta-integral rows, N=0,...,64: coefficient multiplication and
  polynomial integration versus factorial/product formulas. All-N validity
  comes from the written proof, not these rows.
- 512 Mobius values: triangular divisor inversion versus trial factorization;
  both full and odd finite harmonic bounds checked.
- 33 native even-zeta moments, via directed 256-bit rational intervals using
  Machin pi, Bernoulli numbers, and the classical even-zeta formula.
- Seven actual polynomial families: N=0,1,2,4,8,16,32. Complete input/output
  polynomial-square integrals are enclosed, retaining every cross term.
- 49 point checks compare those polynomial formulas with literal truncated
  Mobius dilation sums; every omitted tail is bounded analytically by t/256.
  The intervals may be wider than the polynomial evaluation; an overlap is a
  bounded consistency check, not a new asymptotic estimate.
- Finite eta=1/100 ratios are recorded for these seven particular inputs only.
  They are NOT all-vector certificates or evidence of uniformity in degree.

Both construction paths have the same author. No independent referee review,
proof-assistant run, zeta-zero computation, or analytic theorem proved by the
checker is claimed.

## Development observations and limits

A first serialization attempt exceeded Python's integer-to-decimal digit
limit for exact partial-sum fractions. All mathematical comparisons had
completed, but that run is NOT counted as a successful serialized replay.
The final version compares the exact fractions first and records outward
256-bit enclosures, rather than relaxing the input parser's safeguards.

A separate non-certifying high-precision/NumPy exploration examined finite
Gram ratios at dimensions up to 96. Its floats are not certificate inputs or
premises in NOTE.md; no all-degree conclusion is drawn from them. An early
negative-index display error was discarded and corrected before subsequent
exploration. These numerical explorations do not prove the requested bound.

GitHub reads worked, but no write action was exposed by discovery. The installed
GitHub connection was found; no redundant installation was requested. Direct
`git ls-remote` failed with `Could not resolve host: github.com`. Consequently
this packet has not been pushed. No full authenticated checkout or
repository-wide validator execution is claimed. No remote source, report,
workflow, setting or branch has been modified by this pass.
