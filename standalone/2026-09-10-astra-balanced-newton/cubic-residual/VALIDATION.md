# CIR26 validation contract and execution boundary

## What the accepting calculation reconstructs

The two standard-library programs reconstruct the SAME source coefficients,
all coalesced quadratic/cubic product coefficients, all stated output indices,
and every time/product contribution in the declared covariance panels.
The native target is never replaced by random signs, a prime subset, an early
cutoff or a newly sampled endpoint law. All comparisons use exact integers,
rationals, or outward fixed-point intervals. No floating point, quadrature,
unknown zeta zero or special-function oracle enters acceptance.

Internal interval denominator: 2^128. Published interval denominator: 2^28.
Harmonic sums retain every endpoint. Logarithms use finite atanh series with
complete geometric remainders. Euler's constant is enclosed using the
positive-real digamma remainder in DLMF 5.11(ii), after ten Bernoulli terms;
producer N=256, consumer N=512. Gamma1 from the analytic hyperbola proof is
not evaluated by the software.

## Distinct reconstruction routes

The producer uses a Mobius sign sieve, sequential clipped completion, ordered
Dirichlet convolutions, direct cubic expansion, divisor-count harmonic sums,
and integer-cell physical energy.

The verifier uses smallest-prime factorization recurrence, cumulative capacity
for the tail, unordered factor pairs/triples with exact multiplicities,
c*(delta+e+e^2), and the exact harmonic hyperbola formula. Its source norm is
recomputed by the complete ordered max-kernel. Bernoulli numbers come from
t/(exp(t)-1), not the producer recurrence; logarithms are assembled from prime
factors. Neither imports the other or a repository module.

They have the SAME author. This is implementation independence, not a second
mathematical referee. A common conceptual error can survive both programs;
the analytic arguments require independent review.

## Frozen finite coverage

- Six complete cubic-generation stages: Y=1,3,7,15,31,63, with B=(Y+1)^3-1;
  largest output 262143. Every coefficient and the next excluded error are
  checked. Only 1->7 and 7->511 are consecutive cubic-ladder extensions.
- Fourteen native covariance panels: Y=1,...,12,15,19; largest annulus
  20<=k<=7999. All 417 combined products are retained at that last scale.
- Three non-native control panels: fake prefix (1,0,...,0), Y=4,8,12.
  Unlike native inputs, their residual does NOT vanish below Y+1.
- Total 5,433,258 combined product/time cells; 394 rational prime/prime-pair
  moment checks and 420 bounded packet-norm comparisons.
- 256 exact native divisor identities. Small panels also reconstruct the
  rational aggregate identity directly, without transcendental constants.
- Every clipped input's full physical norm, including its terminal tail,
  agrees with its reciprocal-coordinate energy. The completed-output whole
  norm is established by the proof, not an infinite raw-output replay.
- Twelve actual altered/resealed report objects are refused through the
  verifier's strict canonical typed acceptance. Mutations cover scope,
  removed panels, integer endpoints, same-product degrees, native/fake signs,
  primitive hashes/coverage and boolean/integer/integral-float distinctions.
  Duplicate JSON keys are refused separately. These tests run within the
  CLI self-test; they are not twelve complete subprocess reconstructions.

The finite native signs are all negative. They do NOT establish the proposed
all-scale sign, a bound between the sampled cutoffs, or the RH implication's
antecedent. The generic asymptotic control is proved in the manuscript; its
large first asymptotic threshold is not numerically evaluated.

## Failed intermediate attempts, retained honestly

An initial noncertifying floating scout for the fake input incorrectly used
the native/fake prefix partial sums as its later output. That scout's false
fake-case values are excluded from proof and from every final artifact.
The accepted fake panels instead compute the actual infinite arithmetic
formula coefficientwise through the stated finite cutoff.

The first independent verifier reconstruction failed to match the producer.
Diagnosis: its convolution loops assumed the native residual gap at Y+1 even
for the fake controls. The consumer now determines the first actual nonzero
residual before convolution. The native-gap theorem is never imposed on a
non-native input. The correction changed the verifier, not the canonical
producer result; final normal/optimized reconstructions agree.

## Executed runs and limitations

[validation.json](validation.json) records the final four commands, exit codes,
timings, stdout and exact software/result hashes. All include a comparison
against the immutable result.json; --output writes only separately named
files. Neither --check nor verifier acceptance overwrites the canonical data.

The semantic digest is
`1a3509a8baa22ba11d4b2161059845de43a494779f7bf3eb7f5131a1a79874cb`.

[MANIFEST.json](MANIFEST.json) identifies all eight other files by exact bytes
and hashes; it does not prove mathematics. An external bundle receipt records
any subsequent ZIP/patch fixture replay separately from the prepared commit.
No complete authenticated Riemann checkout was available: direct Git failed
DNS resolution. No full-repository validator, parent executable suite, remote
CI, external formalization, infinite cubic raw norm, zero census, or independent
mathematical acceptance is claimed. Connector tree readback is not a checkout.
