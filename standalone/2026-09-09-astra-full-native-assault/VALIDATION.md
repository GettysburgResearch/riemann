# Executed validation and limits

Date: 2026-09-09. No RH completion is claimed.

## Executed

`python -I -S -B check.py --emit result.json` reconstructed the finite algebra.
The following acceptance commands both completed with byte-identical stdout:

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
```

Their canonical reconstructed-result SHA256 is
`7ada0d5d70f947052d3739db6aa5a0d3aaec0bb718776b8aff86ea037ce5b276`.

The exact scope is eighteen candidate cutoffs Y=2,...,19, 189 prefix
coefficients, 189 initial integer cells, and independent sieve/trial
classification on integers 2,...,256. Every squarefree Euler divisor and every
combined late-correction coefficient in those eighteen panels is retained.
Balance and centering are checked separately in the constant and formal c_Y
coordinates. Derivative identities are checked as exact rational coefficients
of logarithms of primes; substituting the specified c_Y then yields p'(1)=1.
These overlapping checks are not counts of distinct analytic theorems.

Four actual malformed-result CLI tests were executed in EACH Python mode:
a false RH flag, Boolean/integer alias, changed coefficient fingerprint, and
duplicate JSON key. All eight were rejected with nonzero exit status. Canonical
serialization distinguishes false from 0; noninteger JSON numbers are forbidden.
The checker does not use assert for mathematical acceptance.

Only Python standard-library integer/Fraction arithmetic is used. No actual
zeta value, numerical prime asymptotic, critical-frequency integral, residual
minimum, or full-energy value is computed by the checker.

## What these checks do not establish

The proof of the asymptotic uses ordinary PNT, the uniform phase argument,
Fourier Plancherel, and analytic properties of zeta. These are paper proofs and
classical inputs, NOT machine consequences of the finite checks. The eta-series
argument proves the required nonzero value at 1/2 analytically; no zero table
or numerical zeta oracle is used.

The support of the candidate is much larger than the native fixed-ratio classes
in #803. No inference about those optimized minima is made. Prior research
programs and numerical campaigns were not rerun. The source readings and their
limits are recorded in SOURCE_LOCK.json. No full repository build, Lean check,
remote CI run, or independent referee acceptance is claimed.

## Artifact verification

SHA256SUMS authenticates the other seven regular files in this packet. The
archive, add-only patch roundtrip, and remote publication, when completed, have
separate receipts outside this directory so no circular checksum is needed.
Integrity checks establish byte identity, not the validity of the analytic proof.
