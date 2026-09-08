# Executed validation and limits

The retained code is Python standard library only (integers, Fraction, isqrt,
JSON). Exact execution details and hashes are recorded below after final replay.
No external executable or zeta, gamma, zero, or primality oracle is imported.

## Analytic contract of the certificate

The exact Mobius sieve supplies the finite coefficients. A 192-bit dyadic
interval type uses floor/ceiling integer division for every operation and
integer square roots for radical enclosures. Logarithms use 72 atanh terms
with the complete geometric remainder; pi uses Machin's identity with 72
alternating terms per arctangent and the next-term remainder. Log(2pi) is
evaluated monotonically on the resulting pi interval.

PROOF.md (17)-(21) prove the complete tail and the norm-cell antiderivative.
Every one of the 8 fixed candidates integrates all nonzero cells through
Y=32768; the earlier zero cells are eliminated by exact divisor identities.
The final analytic tail bracket covers infinity, not just another cutoff.

There are 261881 integrated cells and 255 exact zero cells, 262136 cells in
all across the eight candidates. These counts are coverage, not theorem counts.
The resulting rational interval endpoints are in certificate.json; decimal
renderings are never treated as directed endpoints.

## Commands

    python checks.py --output /tmp/checks.normal.json
    python -O checks.py --output /tmp/checks.optimized.json
    cmp /tmp/checks.normal.json /tmp/checks.optimized.json
    python certificate.py --output /tmp/cert.normal.json
    python -O certificate.py --output /tmp/cert.optimized.json
    cmp /tmp/cert.normal.json /tmp/cert.optimized.json
    python checks.py --compare checks.json
    python -O checks.py --compare checks.json
    python certificate.py --compare certificate.json
    python -O certificate.py --compare certificate.json
    # Execute separately for each mode in normal optimized, and each part below:
    python rejections.py --mode normal --part controls --output /tmp/refuse.normal.controls.json
    # Other parts: tail_removed, wrong_source_error, package.
    # Repeat all four parts with --mode optimized.
    python validate.py

Normal and optimized mathematical outputs are byte-identical. The published
single result per producer equals both outputs; there is no need for duplicate
published files. The exact checker has 14 named controls and 13366 bounded
fixtures per mode. Most fixtures are finite divisor/floor cancellation checks.
It rederives Mobius values by independent trial factorization, compact input
transforms by direct step integration, signed norm telescoping, Laguerre
orthogonality, finite jet expansion, and norm-antiderivative coefficients.

The rejection runner executes the actual CLIs on four altered exact-check
records and two altered complete-tail records, plus two package mutations,
in EACH interpreter mode. A return code of zero is rejected by the runner.
The final combined result is rejections.json. Package integrity validation
checks all declared bytes, the complete inventory and intended finite coverage;
it does not machine-prove the analytic theorem or establish primitive truth
merely because a JSON flag says so.

## Assurance boundary

No full-domain theorem, unbounded output estimate, new zero census, Lean build,
Comparator, remote CI, independent referee approval or external novelty claim.
Classical Hardy/Littlewood/Stirling inputs are explicitly imported. The source
proof's infinite arguments need mathematical review even after every script
passes. Predecessor bytes are pinned but predecessor mathematical suites were
not rerun in this pass.

Non-directed numpy/longdouble scouting selected a small candidate panel and
checked formulas during development; none of it is consumed by the retained
certificate. The final inequalities are recomputed solely by directed integer
arithmetic. The source-grid ceiling and all eight cutoffs are public constants.

Authoring changes before freeze: consolidated duplicate normal/optimized result
files into one authenticated copy; removed an unused alternative expression
in the bounded checker; corrected a percent-encoded bibliography URL. The
safe-range convergence corollary was added with its full proof. No frozen
predecessor was changed, and no incomplete run is recorded as a success.

## Final execution receipt

All eight partitioned rejection runs completed: four record controls, two
complete-certificate comparisons, and two package mutations in each mode,
16 actual subprocess refusals total. Earlier combined rejection runs exceeded
the outer execution limit and produced no accepted result; they are NOT counted.
The same tests were then split into bounded parts without weakening their
mathematical, coverage, or per-subprocess timeout contracts.

Python: 3.13.5 (main, Jul 15 2026, 20:25:40) [GCC 14.2.0]
Platform: Linux-6.18.35-x86_64-with-glibc2.41

certificate.py SHA-256: 25aebf55734b0ee9c75a8f494a5e0cbe998d0c92f8e73bc572ac775ac8e3d16b
certificate.json SHA-256: 2fb2b2961ad9d6ec1a24fe60a3e05c500ca3a4bd246ce2e1965f80ab046f3ecb
checks.py SHA-256: db2c0d3ef391089019adc38f6146d6bf30798c7c92efa4d7c12d2c9060c88f7e
checks.json SHA-256: a458e2b34333d8b0e43ddca0da5d123e989a85d0956265fa4d0a099d3c19146c
rejections.json SHA-256: 869eb13e0b1ac4f9a36808c58c6636a9ed79acacc61b622f4949a3d52f04220b

No source-code changes affecting mathematical results were made after their ordinary/optimized comparison. The partitioning change only affects the refusal runner.
