# Reviewer D — executed validation and trust boundary

## Executed bounded reconstruction

Environment: Python 3.13.5, GCC 14.2.0 build; SymPy 1.14.0.
No network, repository checkout, upstream producer or source fixture is imported
by `checks.py`. The script implements its own finite constructions from the
source formulas. Its exact GitHub source inspection is documented separately
in `SOURCES.tsv`; running the checker does not itself retrieve or authenticate
those original remote blobs.

At the final checker bytes:

```
PASS_REVIEWER_D_BOUNDED_RECONSTRUCTIONS
named_checks=45 fixtures=9380
RH_UNPROVED; NO_UPSTREAM_OR_LEAN_REPLAY
```

The script completed `--write` in normal and optimized Python, with byte-identical
outputs. Its final `--check` also completed against each retained output in the
corresponding mode. Each valid check reconstructs all 45 groups before accepting.
The 9,380 count is a declared fixture count, not a theorem count or a count of
independent mathematical propositions.

Checker SHA-256:

```
26694e95cd50afa7b9b9934b545acee8b58acf2266ec53bd33b8fd92d27a4bb2
```

Common result SHA-256:

```
d5314a9747f94997522412dd1b715b8c2524417384217d49565a4351309f9d24
```

### What the checks cover

The machine-readable output names every group and records its count. Major
scopes include:

- all sigma(n) through 5582, independently by divisor accumulation and prime
  factorization; directed gamma/loglog barrier and exact powered-tail fixture;
- all 66 compact SHARP prefix extrema, RN ratios, removal mass and row identities;
- variable-order filter counterexample, spectral-threshold approximation,
  principal-minor controls, actual finite wavelet endpoint mismatch and the
  lost one-node annihilator hypothesis;
- full symbolic three-node Xi determinant, orbit curvature and reserve algebra,
  local half-divisor convolution, finite Haar overlap and rational cyclic Green norm;
- safe-line beta/Bernstein algebra, Hermite inertia, finite terminal-pair and
  Gaussian exponent controls, signed Perron/matched-transfer/root-excess algebra;
- the initial-excursion counterexample and nonuniform growing-region construction.

The Robin interval backend uses exact rational arithmetic, 100-bit dyadic
outward rounding, integer-square-root bounds, an 80-term atanh logarithm series
with its analytic tail, and a 64-term positive exponential series with its tail.
No stored digits of gamma and no floating-point sign decisions enter those
finite certificates. SymPy is used for exact algebra and symbolic identities,
not claimed as a separately verified proof kernel.

## Corruption refusals

`rejection_checks.py` successfully executed six deliberate corruptions in each
of normal and optimized Python, 12 refusals total, retaining exit code 2:
changed named-count, floating-point fixture-count alias, integer/Boolean flag
alias, a false RH flag, duplicate JSON key, and changed checker bytes.
`rejections.json` binds the checker and driver hashes and stores all outcomes.

Metadata errors are rejected at preflight; a valid payload must still undergo
the full reconstruction. This is not acceptance based on self-consistent counts.

Four additional package-validator refusals are recorded in
`package_rejections.json`: altered report bytes and an unlisted file, each in
normal and optimized Python. The unaltered packet passes in both modes.
`SHA256SUMS` covers every other file exactly once, and `validate.py` checks
coverage, hashes, ledger IDs, cross-references, the 139-row denominator and
result/source bindings. The manifest is anchored by the published Git commit;
it is not a substitute for proof review.

## Authoring failures retained

An early checker run used structural rather than simplified equality for one
SymPy polynomial comparison; the independent algebraic residual was simplified
and the check then passed. This was a checker-authoring defect, not a new
source-theorem counterexample.

Two combined corruption-run attempts reached orchestration timeouts without a
final refusal report. The checker then acquired an early metadata/hash preflight
so malformed files need not repeat all symbolic mathematics. A subsequent
combined write/refusal orchestration also timed out after both successful write
markers. The separately executed final refusal run completed, and both final
valid reconstruction checks completed afterward. Interrupted attempts are not
counted as successful runs or mathematical failures. No other agent's process
was modified.

## Reproduction

From this directory, with the stated Python/SymPy versions available:

```sh
python checks.py --check checks.normal.json
python -O checks.py --check checks.optimized.json
python rejection_checks.py --write /tmp/reviewerD-refusals.json
python validate.py
python -O validate.py
sha256sum -c SHA256SUMS
```

The existing rejection report is not overwritten by this example command.
The four package corruptions can be reproduced by copying the directory to a
temporary location, appending a byte to REPORT.md or adding an unlisted file,
and invoking `validate.py --root` on that copy, once in each Python mode.

## Explicit non-executions

No upstream full producer suite, full source-tree closure, large prime/zero
scan, historical Robin traversal beyond 5582, 665135-cell screw certificate,
original infinite Gram computation, Brownian campaign, Lean build, Comparator,
Nanoda, GitHub Actions dispatch or external numerical verification was run.

The P15 general reciprocal-zeta/Hardy theorem, P61 uniform profile inputs,
full balanced two-field identity, Julia channel mass bounds and original
safe-line arithmetic construction retain their explicit unread/imported boundary.
Finite replay does not prove Landau, a Hadamard product, infinite Gaussian or
Mellin interchange, all-order positivity, the new analytic suffix criterion,
or RH. Those arguments are prose mathematics subject to further review.
