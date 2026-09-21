# Validation receipt and its limits

Authoring date: 19 September 2026. See `validation.json` for the exact
Python version, commands, captured output, elapsed times and exit codes.

## Executed

All four commands below passed in ordinary Python and again with `-O`:

```bash
python -S -B boundary.py --check result.json
python -S -B verify.py result.json
python -S -B lfamily.py --check lfamily_result.json
python -S -B -m unittest -v test_boundary
```

The producer reproduced the recorded JSON byte for byte. The separate
verifier does not import the producer or any repository module; it uses
trial factorization, direct Mertens/reciprocal sums, and a Stieltjes jump
identity at higher precision. The reported enclosures must contain the
independently computed enclosures, not simply intersect them.

Coverage: six complete stages, 70,986 coefficient checks with repeated
ranges counted, 1,964 upper-triangle Gram entries, every row mean, and
both full completed states. The largest stage covers every integer
through 65,535. The test suite has twelve methods, including twelve
corrupted report variants and duplicate-key controls, in each mode.

The separate L-family replay checks fourteen auxiliary-prime cases,
twelve divided projectors, two Fermat lifts and four three-point rank-
deflation matrices, all in exact rational arithmetic. It does not
certify elliptic L-values, CM integrals, heights or analytic ranks.

## Mathematical versus computational status

The component proofs in PROOF.md and LFAMILY.md are proposed for review.
Finite arithmetic cannot certify their universal quantifiers. The two
implementations have the same author and are not independent mathematical
acceptance. No novelty priority, full RH/GRH theorem, or all-scale native
upper bound is claimed.

The classical PNT is used only for the asymptotic corollary of an exact
prime-count lower bound. No numerical extrapolation or RH-strength prime
error term is used. The new prime-pivot decomposition is not represented
as PCR26's centered-harmonic covariance.

## Packaging

The delivered patch adds only this standalone directory. A fresh local
Git fixture, containing an unrelated sentinel, accepts the patch; its
file hashes and ordinary/optimized replays were checked. This is an
add-only packaging/replay check, not a checkout of the actual Riemann
repository and not its full validator. The sentinel was unchanged.

`SHA256SUMS` covers all packet files except itself. No original repository
files, canonical claim statuses, workflow settings, or historical review
records are changed by the patch.

## Publication

No remote write was performed. GitHub reads succeeded; the available
connector action catalog contained no writes. A direct Git clone failed
DNS resolution. The plugin-directory check reported GitHub already
installed, so this is not represented as a disconnected account.

The existing #903 head observed was
`67132424e3cbe35a94752581a5b5271ab8bfc56f`. That SHA does not contain this
new packet. `PUBLISH.md` supplies the intended safe continuation process;
a publisher should add a separate remote-SHA/readback receipt after a
successful push rather than rewriting this historical record.

No repository-wide validation, predecessor experiment replay, remote CI,
formal Lean build or independent referee review was performed.
