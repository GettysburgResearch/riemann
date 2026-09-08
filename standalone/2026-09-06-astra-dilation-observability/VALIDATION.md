# Executed validation — 6 September 2026

Environment: Linux; Python 3.13.5; Git available; no third-party Python
package is required by the packet. All commands below were executed locally.
No remote CI or formal proof build was executed.

## Scientific replay

Both

```text
python -I -S -B scripts/replay.py --check
python -O -I -S -B scripts/replay.py --check
```

returned

```text
PASS_DILATION_OBSERVABILITY_FINITE_REPLAY
controls=14073 max_N=16 RH_proved=false uniform_gain_proved=false
verification_sha256=07b8b88e0bdf66500cbf057303a3cb2dcd82580b4b825ee0f3fbcba4266945b9
```

The canonical reconstructed JSON bytes agree in normal and optimized modes.
One timed run took 4.31 seconds wall-clock in normal mode and 4.24 seconds in
optimized mode. These timings describe those runs, not a resource guarantee.

The 14,073 bounded controls consist of 9,090 exact dilation identities,
6 finite-vector norm identities, 529 dual biorthogonality identities,
23 target pairings, 24 independent Möbius cross-checks, 6 special-witness
checks, 4,275 interval/function consistency checks, and 120 full-Gram/coarse-
tail comparisons. Projection and Schur acceptance checks are additional
explicit conditions in the replay; they are not inflated into that count.

The numerical problem is fixed: 120 distinct symmetric Gram entries at
indices 2..16, five projections, and three full Schur doublings. Every entry
includes its infinite summation tail using the remainder proved in
NUMERICS.md. Distance, first-cell and full-gain interval widths are required
to be below 10^-25. The wider 12-decimal intervals shown in the README are
for readability only.

## Unit and rejection tests

`test_replay.py` passes **15 tests** in normal mode and **15 tests** under
`python -O`, including exact-type validation after cached calls, interval
arithmetic, pivot rejection, the prime-2 overlap exception, duplicate/float
JSON rejection, manifest coverage and changed-source refusal.

`test_cli_mutations.py` launches eight actual CLI checks in temporary copies.
All **8/8** corruptions were refused normally and **8/8** under optimized
Python for the intended reasons:

- altered RH or uniform-gain flags;
- Boolean substitution in the frozen integer configuration;
- a floating-point configuration alias;
- a duplicate JSON key;
- a changed exact interval endpoint;
- changed proof bytes without a matching source digest;
- a new path outside the checksum inventory.

The first six semantic/data mutations are rehashed before testing. Thus their
refusal is not merely a stale-checksum detection. The interval mutation is
rejected after rebuilding the actual numerical result. The source/coverage
mutations deliberately test their separate manifest gates. Temporary files
are removed and the delivered packet is never mutated by these tests.

The full commands, including those mutations, are repeatable from the source
scripts. `SHA256SUMS` binds every payload file except itself, and its exact
coverage is checked. This is source integrity, not independent proof review.

## Boundaries

No unbounded gain estimate, cofinal overshoot theorem, RH proof, strengthened
zero proportion, novel-priority finding, or independent referee acceptance
is reported. The analytic component proofs are prose proofs, not Lean or
kernel certificates. The interval algorithm is reviewable source with
explicit remainder proofs, not a formally verified arithmetic library.

GitHub reads succeeded at the frozen main commit in SOURCE_LOCK.json. The
available connector supplied no write action. The fallback noninteractive
Git probe failed with `Could not resolve host: github.com`. No GitHub push,
remote branch, PR, comment, workflow dispatch, or settings change occurred.
The separately supplied patch is a publication handoff, not a remote receipt.
