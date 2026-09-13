# PCR26 validation and evidence ceiling

The written component proofs are proposed. Computation does not establish the
all-scale native covariance inequality or RH. The exact executed commands and
stdout are recorded separately in validation.json.

## Primitive reconstruction

The producer uses a Mobius sieve, sequential clipped control, ordered convolution
of the actual c coefficients, and divisibility-multiple propagation for Newton
coefficients. The verifier imports neither the producer nor repository modules.
It uses trial factorization, divisor fibers, a closed threshold construction of
the clipped tail, and an ordered max-kernel norm for the complete input.

Newton output coefficients are compared with a separate primitive Mobius
construction BEFORE any numerical energy enclosure. Thus a consistent but
non-native output cannot pass merely by agreeing with its own derived energy.
All coalesced product coefficients are reconstructed and their hashes retained.
Every prime-log moment vanishes as an exact rational identity.

## Directed arithmetic

Acceptance uses only integers and fractions, not floating point, quadrature,
zero data, a probabilistic model or external packages. The producer uses 128-bit
outward fixed-point bounds and a 64-term atanh logarithm with complete remainder
and binary range reduction. The verifier uses 160 bits, exact rational harmonic
numbers, 192-term logarithms with base-four reduction, and the summed quadratic
polynomial in log d instead of the producer's cellwise squares. Prime logarithms
are combined by exact integer factorization.

The programs independently enclose the true values, then require both ends to
lie in ONE common cell of the 2^-40 output grid. A cell ambiguity raises an
exception rather than declaring a sign. This makes the canonical interval
endpoints identical despite different high-precision constructions. All signs
claimed in the finite corpus are strict at these directed endpoints.

The aggregate Q energy is reconstructed through rational coefficient sums;
logarithmic cancellation is not checked by testing a small floating residual.
The proof supplies the all-scale harmonic bounds and the complete omitted tails.
The twelve reported single-packet bounds are formula controls, not finite
numerical proofs of an infinite theorem.

## Complete declared corpus

- 28 complete native annuli: Y=1,...,24,31,32,47,63, with all k=Y+1,...,(Y+1)^2-1
  and every nonzero coalesced product d. Largest native annular cutoff:4095.
- Three complete non-native covariance annuli: Y=16,32,64, all with strictly
  positive cross covariance. These do not have the actual divisor inverse.
- 6,316,466 packet/cell contributions across those31 panels. This is arithmetic
  coverage, not a count of independent mathematical theorems.
- Six native prefix productions at Y=1,3,15,63,127,255, checking86,286 coefficients
  in total and every coefficient through65535 in the last production.
- 256 native divisor equations, complete physical input-norm identities for all
  panels, bounded-tail and reciprocal-moment guards, and exact prime-log moments.
- A positive individual covariance pair on the native Y=3 input, with margin>1/40.
- A separate large fake control at Y=127 validates the two-block gap and energy
  lower bound at the first permitted b=128. Its much larger full covariance grid
  is NOT claimed enumerated.

Twelve distinct report mutations are resealed and rejected by the real acceptance
function reading temporary files. They include boolean/integer and integer/float
aliases, changed arithmetic intervals, dropped coverage, a false all-scale scope,
the forbidden Newton boundary, and an erased tail. A duplicate-key JSON file is
also rejected. The expected body is reconstructed once per verifier run, not
trusted from the submitted checksum. These are acceptance-function tests, not
12 separate executions of the whole expensive protocol.

## Disclosed exploration and limits

Ordinary NumPy scouts helped select finite cases and inspected some gcd grouping.
They used non-directed floating point and are NOT proof evidence. The accepted
intervals were independently reconstructed in the two exact protocols. No
asymptotic trend or fitted gain is reported. A first exploratory attempt to run
NumPy with Python -S failed because site packages were unavailable; the final
acceptance programs use only the standard library and do run under -S.

All source coefficients in the native tests are exact. The non-native family
violates the divisor constraints at n=2; it is not evidence against the native
bound. The attempted per-pair sign argument is refuted by a genuine native
pair, while the total native sign remains unknown outside the fixed panels.

Both implementations and the proof have the same author. No independent proof
acceptance, complete repository checkout validation, remote CI success, parent
executable replay, external formalization, or full literature priority audit is
claimed. Direct Git access failed DNS resolution. Scoped local replays and the
GitHub publication/readback are distinct from a whole-repository validation.
