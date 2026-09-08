# Bounded validation and unperformed checks

Status: author execution record, not independent mathematical acceptance.
The decisive near-linear estimate and RH remain unproved.

## Scope and trust model

The producer uses ordinary Python integer and Fraction arithmetic only.
It builds mu by an integer sieve, compares it to trial factorization, and
checks odd divisor inversion. It reconstructs the terminal coefficient,
rational harmonic kernels, raw and balanced hyperbola expressions, the
higher-order convolution, its exact boundary defect, polynomial annihilation,
and explicit positive/negative balanced test sources. No floats, zeros,
special-function evaluator, external package or implicit Gram tail enters
acceptance.

The primitive Mobius scope is 1..1089 (independent trial factorization through
256). The actual quadratic panel has 14 specified odd cutoffs through 33.
The higher-order panel has nine (Y,d) pairs, with d<=5 and output cutoff<=625.
The coherent countermodels use six integer L values through 33, giving a
largest support cutoff 6601; their kernel arguments lie between 1 and 5, so
this does NOT run a Mobius census or large harmonic computation to 6601^2.
The main-term regression substitutes rational labels for logarithms in the
UNIVERSAL polynomial annihilation identity. It is not a numerical check of
transcendental values. The fixed continuum norm and asymptotic obstruction
remain paper proofs.

## Commands

From this packet directory, on the delivered final bytes:

```bash
python scripts/replay.py
python -O scripts/replay.py
python scripts/test_replay.py
python -O scripts/test_replay.py
```

The two reconstruction modes yield `PASS_BALANCED_HYPERBOLA 2702 EXACT_CHECKS;
RH_AND_GAIN_OPEN` and identical reconstructed verification JSON. Seven unit
methods pass per mode, including 15 distinct actual CLI corruption refusals
per mode. The corruption cases cover false theorem-status promotion, boolean
aliasing, narrowed source scope, wrong quadratic sign, lost terminal
correction, omitted source row, wrong higher-order boundary, wrong lobe sign,
floating-point JSON alias, source-lock drift, changed parent bytes, duplicate
JSON keys, empty manifest, an extra file, and a symlink. Semantic mutations
are resealed where appropriate to test reconstruction rather than only hashes.

One combined execution of the two replay modes and both unit suites exceeded
the execution-tool limit after the normal suite completed and during the
optimized suite. That partial optimized run is not counted as a suite PASS.
A subsequent standalone optimized invocation completed all seven methods and
all fifteen CLI refusals. Final-byte replays and suites were run separately.

The exact eight-path nonempty SHA-256 inventory uses POSIX-relative paths,
rejects missing/extra files and symlinks, and excludes only the checksum file
itself. The parent proof is authenticated by SHA-256, Git blob and byte count.
No parent code, bytecode cache or predecessor test suite is executed. The
trust root is the reviewed Git source plus the independently inspected
checker, not self-consistency of a rewritable JSON file.

The producer's `--write` mode regenerates an output for review; it is NOT
acceptance. Default mode checks the complete manifest, exact source lock,
strict JSON and theorem flags, and independently regenerates every result.
Tests use explicit exceptions and unittest, not removable acceptance asserts.

## Publication and limits

The intended publication is add-only under
`standalone/2026-09-07-astra-balanced-hyperbola/` on the existing PR branch.
No predecessor is repaired in place. The external publication receipt records
actual blob identities, branch movement, clean-extraction checks and any
application test after execution; this document does not predict CI or a
future owner action.

No broad campaign, Windows run, Lean/kernel build, fresh zero verification,
independent referee acceptance, remote CI success, uniform block-gain proof,
near-linear actual quadratic bound, or RH proof is claimed. Classical
analytic imports and their hypotheses are listed in SOURCES.md. Finite
arithmetic replay cannot prove the unbounded analytic implications.
