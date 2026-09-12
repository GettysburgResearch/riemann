# Execution, source, and scope record

The new infinite statements are paper proofs in PROOF.md and
BOUNDARY_CHANNELS.md. Their finite tests
do not authenticate an unbounded degree estimate or the value of Theta.

## Source reading

SOURCES.json pins the exact full DG26 and latest XCC26 proof bytes, including
SHA-256 and length. Both proofs were read in full. Main's AGENTS.md and its
current source/status guide were read. No earlier checker or numerical
campaign was rerun. The new Chebyshev/Fourier approximation is derived here
without importing a Jackson-theorem interface.

The independent root task also read the first complete proof and checked its
Fourier parity/degree, smooth cutoff powers, approximation-order threshold,
Theta=1 case, and finite odd/all-integer adapter. It reported no defect in
those arguments. This is same-team component scrutiny, not external referee
acceptance or an integrated repository status.

## Exact commands completed

In this directory on Windows, Python 3.12:

```text
python -S -B check.py --write results.json
python -S -B check.py --check results.json
python -S -O -B check.py --check results.json
python -S -B test_rejections.py
```

Normal and optimized reconstructions produced the same semantic SHA-256:

```text
2b706728d7d3ab92d6813eb98c98be6a18891756ae8e2acab6d6ec7e90824600
```

The program accepts only by reconstructing the entire expected payload, then
comparing canonical JSON bytes. Duplicate keys are rejected during parsing;
Boolean/numeric aliases do not compare equal in the canonical encoding. It
does not use assert for acceptance. The checker uses only the standard library.

The reproducible driver test_rejections.py passes four mutated reports
through the actual checker CLI in EACH mode,
after the pristine report succeeded: wrong first trace endpoint, Boolean
coverage alias, missing limitations field, and duplicate top-level key.
All eight subprocesses rejected. Temporary test reports were removed by
Python's TemporaryDirectory. These are report-corruption tests, not source
mutation or supply-chain assurance.

## Arithmetic and full coverage

Primitive enclosures use integer outward intervals with denominator 2^384.
Two distinct pi identities are evaluated with complete alternating remainders:
Machin's 16 atan(1/5)-4 atan(1/239), and 4[atan(1/2)+atan(1/3)]. Each is fed
independently into exact Bernoulli/even-zeta formulas and the complete output
column integrations. Their final trace intervals overlap. This is two
primitive routes with the SAME author and shared subsequent interval code,
not two independent numerical libraries or mathematical referees.

All eight column energies through N=8 include every monomial cross term and
the exact integral on the ENTIRE interval (1,3). The computation reconstructs
the scalar trace, not an eight-by-eight output Gram or its eigenvalues.
The 64 input Legendre orthogonality entries are exact Fraction identities.

Ordinary Mobius values through 177 are obtained both by a sieve and by trial
factorization. All 177 endpoint source identities F_Y=E_Y+(Y+1)u_Y^2 and all
177 odd/all-integer conversions are checked exactly. Eleven actual crossing
cuts below 32 have their complete pair-kernel energy compared with the
reciprocal-coordinate formula, and their balance and Liouville signs checked.
No covariance sign at a new large crossing is claimed.

The four displayed finite adapters use N=1,2,4,8 and the entire native
coverage indicated in results.json. They check normalization and concrete
inequalities with conservative constants. They do not numerically validate
the infinite exponent proof or suggest any fitted growth law.

The retained-boundary-channel check uses N=4, M=32, all four error column
norms, and all 64 cells partitioning the ENTIRE interval (1,3). Its squared
Hilbert--Schmidt error is enclosed in
[0.000000002183835895, 0.000000002183835896], below the proved bound
99648703/1073741824. The instance consumes odd Mobius coefficients through
96. Two primitive pi routes reconstruct the same displayed enclosure. The
128 exact activation checks cover moments q=2,4,6,8 at each odd integer
boundary in this interval. Even boundaries are unchanged identically.
The surrogate itself uses only q=2; higher even-zeta constants serve to
verify its complete error against the true operator. No fitted error law,
omitted tail, output Gram eigenvalue, or covariance sign is used.

## Limitations and edits during execution

No actual zeta zero, complex cutoff at a zero, asymptotic constant, large matrix,
or unbounded covariance bound was computed. No proof assistant, full-repository
validator, external CI, or independent author implementation was run.

The first result receipt called the eight complete column norms a full Gram
order. This coverage label was corrected before the final receipt and both
final replays. No output Gram computation is claimed. An initial text patch
for the effective-rank corollary failed to match and changed no file; the
subsequent patch applied successfully. These editorial events are not counted
as mathematical test outcomes.
