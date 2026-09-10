# Validation contract and execution scope

This file records the intended bounded checks; the companion delivery receipt
records commands and actual exit statuses. No check below proves RH or machine-
verifies Jensen, Hardy theory, analytic continuation or an infinite quantifier.

## Arithmetic

Python standard-library integer and Fraction arithmetic only. No float, zeta,
gamma, zero table, numerical quadrature or RNG is used by acceptance.
The table of ranks includes K=2^64-1, but only scalar integer parameters are
computed there: NO large matrix, factorial source or prime campaign is run.

Reconstruction has 1,994 bounded controls in fifteen named groups. Of these,
1,792 are constant/formula checks through n=256. The remaining groups check
the Bernoulli polynomial, proof constants and induction base/steps, eleven
rank-parameter records, sixteen explicit synthetic tridiagonal Gram solves,
and nine rational boundary-zero inverse models. The rational models' complete
L2 norms are computed by exact exponential-polynomial integration, not a
truncated time grid. Their partial fractions are checked against the original
rational transform by independent polynomial reconstruction.

The conditional claims about the actual zeta source depend on paper proofs
and the explicitly cited existence theorem, not those synthetic models.
No new actual-source finite energy certificate was computed. The parent's
fixed-horizon improvement remains an inherited result at its exact freeze.

## Acceptance

The checker authenticates the exact nonempty nine-entry manifest and ten-file
packet inventory, then the parent's length, Git blob and SHA-256. It rebuilds
all bounded data and uses type-sensitive recursive comparison. Booleans are
not integers; duplicate keys, floating/nonfinite numbers, altered result
fields, source-lock drift, missing/extra files and symlinks reject. Acceptance
does not use Python assert. No parent code is loaded or executed.

The --reconstruct option bypasses package authentication only to produce
bounded development data and does not emit the acceptance marker. A newly
rewritten checker plus self-consistent hashes is not an externally trusted
replacement for this frozen checker. The delivery receipt supplies its hash.

## Commands

    python -I -B standalone/2026-09-07-astra-source-stability/check.py
    python -I -B -O standalone/2026-09-07-astra-source-stability/check.py
    python -I -B standalone/2026-09-07-astra-source-stability/test_check.py
    python -I -B -O standalone/2026-09-07-astra-source-stability/test_check.py

Five unittest methods include a pristine copied-packet CLI run and twelve
actual CLI rejection cases per mode: false RH flag, boolean/integer alias,
wrong floor exponent, wrong synthetic projection, wrong inverse cost,
narrowed scope, float, duplicate JSON, empty manifest, extra file, changed
parent proof and packet symlink. Semantic result mutations are rehashed so
that they test primitive reconstruction rather than only checksum mismatch.

## Unperformed checks

No actual large Gram matrix or source cutoff is evaluated. No existing
producer or test suite is replayed. No independent code implementation,
independent referee acceptance, Lean/Comparator/kernel build, Windows run,
remote CI success, complete repository checkout or unbounded gain test is
claimed. The constants are conservative and not numerically optimized.

## Publication boundary

GitHub PR #812 and its proof were read at the exact parent above. The current
connector exposes reads only, and git ls-remote failed DNS resolution for
github.com. The continuation is supplied as an add-only patch and ZIP. A
successful local application is not a GitHub push; the separate publication
receipt must say whether a remote head was actually changed.
