# STC26 validation and scope

## Executed mathematics versus imported mathematics

PROOF.md supplies proposed analytic proofs for the matched transport sector,
its exact negative empty-bank formula, the all-scale multiplicative-sign
obstruction, and the conditional consumer. LFAMILY.md supplies proposed
causal norm/Parseval proofs and the central-stripping calculation. They use
classical ingredients. Numerical execution is not independent proof review.

PET26's finite d_b,h_b theorem and its asymptotic are inherited and were read;
we do not re-run its entire old checker or promote its status. RCB26's parity
idea is adapted in a different physical kernel with a new direct proof.
No equality to its individual harmonic covariance blocks is asserted.

The Sylvester global rank theorem and ordinary fixed-progression PNT are
external mathematical inputs only to their declared uses. No CM integral,
height, global L-value, full elliptic coefficient list, zero location or
analytic rank was computationally certified here.

## Actual programs and complete coverage

transport.py uses a smallest-prime-factor sieve and explicit parity lookup.
For every prime p and squarefree cofactor n, it enumerates EVERY compatible
target m in a matched sector. All weights use the exact max(b,m,p*n)
kernel, not sampled observation points. Positive and negative pairs are
reported separately. The full P_b, physical energy, both signed means, and
completed A are evaluated on every integer cell through N.

verify.py imports neither transport.py nor repository code. It uses trial
factorization, the three-case arithmetic classification in PROOF.md, and
reverse integration for the full P_b. It shares exact.py, copied unchanged
from PET26, for directed scalar arithmetic. It checks every reported
scientific interval, all counts, and the multiplicative-sign control.
Its interval comparison checks a tight enclosure, not byte identity; replay
also checks byte-canonical semantic hashes of complete reconstruction.

Seven cutoffs Y=3,7,15,31,63,127,255 cover 87,369 coefficient indices counting
overlap. Three banks per stage cover 1,588,798 matched triples, again counting
overlap across banks/stages. Largest output index: 65,535. There is no
unbounded extrapolation of observed remainder signs.

family.py uses exact integer point counts and exact fractions. The model is
a FINITE good-prime Euler product based on E_17, NOT the whole elliptic curve
L-function. It includes split primes 7,13,19 and eight active odd good inert
primes below 64. All 256 inert-square signatures through 4095 are reconstructed
by two distinct coefficient assemblies, for 1,048,320 comparisons. Exact
rational energies satisfy Parseval, restoration and individualization bounds.
Rational endpoints X/d^2 and the mixed-square index 3025 are retained.
The family code has two coefficient routes but NOT a separately authored
independent verifier; the separate verifier concerns the transport report.

The new physical report was compared with the published PET26 result at
all seven stages: 42 intervals overlap (P, E, I, two means, completed state).
This is a compatibility replay, not a new improvement to those old values.

## Commands actually run

All of the following passed in ordinary Python and with `-O` inserted after
`-S`. The accepting calculations use no floating-point tests, third-party
packages, external services, or network requests.

```sh
python -S -B replay.py
python -S -B transport.py --check reports/transport.json
python -S -B verify.py reports/transport.json
python -S -B family.py --check reports/family.json
python -S -B test_packet.py
```

The twelve unittest methods include twelve corrupted-report variants,
boolean/float numeric aliases, duplicate keys, the exact finite character
average and its required chi(p) factor, parity versus radical, the native
negative sector, the nonnative mu^2 control, normalization, causal inverse,
and a rational observation endpoint. Tests do not rely on Python assert,
so optimization does not disable their acceptance conditions.

Full reports are reproducibly regenerated under ignored reports/. Their
canonical semantic SHA-256 values are committed in EXPECTED.json. The
published archive also includes those complete reports. Edited bulk matrices
are not manually transmitted into GitHub. SHA256SUMS authenticates source
bytes, not mathematical truth.

## Corrections caught before publication

The first independent three-case implementation looked up mu(a) for a bank
divisor a larger than the finite endpoint. Such divisors produce no admissible
triples; they are now excluded before lookup. The initial tiny character
average test also omitted the last legal cofactor when p did not divide the
observation endpoint. Its reference loop was corrected to n<=(X-1)//p.
Both failures were in auxiliary enumeration code, not repairs of a theorem.
The final full producer, verifier, receipt replay and both test modes were
run after these corrections. A small primality helper was also changed from
a floating square-root bound to integer isqrt before final validation.

## Publication boundaries

All changes are additions in this new standalone directory. Earlier BCP26,
SBC26, RCB26, PET26, canonical statuses, main and workflows remain unchanged.
No full Riemann checkout validator, remote CI, Lean/Metamath build or
independent mathematical acceptance is claimed. All code and proof text in
this pass have one author. No full native unmatched bound or RH/GRH solution
is asserted. The external publication receipt records the actual remote
commit, branch read-back and add-only comparison after they occur.
