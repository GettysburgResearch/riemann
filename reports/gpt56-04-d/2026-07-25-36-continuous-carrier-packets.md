# Agent report — continuous off-lattice and confluent carrier packets

Agent: `gpt56-04-d`  
Issue: #36  
Branch: `agent/gpt56-04-d/36-continuous-carrier-packet`  
Date: 2026-07-25

## Starting problem

The existing carrier-Weil program had two complementary but incomplete finite
families:

1. integer-lattice sinc packets, whose exact D-0001 matrix formulas are stable
   but whose geometry is rigid;
2. arbitrary continuous sinc carriers, whose prime kernel was known but whose
   exact pole/archimedean blocks and generalized Gram treatment were missing.

A naive continuation of integer-index formulas to real carrier indices had
already produced a false negative by dropping endpoint phases. Directly
optimizing many close continuous carriers is also numerically dangerous because
the sinc Gram matrix becomes nearly singular.

## Main mathematical results

### L-3601 — exact off-lattice block

For arbitrary real carriers, L-3601 derives from the compact box transform:

- the exact sinc Gram matrix;
- the complete finite prime block with all endpoint phases retained;
- the exact pole block;
- a compact `[0,2L]` archimedean block;
- the scalar Fejer limit;
- the exact integer-lattice sign congruence;
- an explicit fractional-index adversary showing why naive interpolation fails.

### L-3602 — orthogonal confluent hierarchy

L-3602 introduces normalized Legendre envelopes on the compact Fourier interval.
Their transforms are spherical-Bessel carrier functions

```text
Phi_n,T(z) = sqrt((2n+1)*Delta) j_n(pi*Delta*(z-T)).
```

The coefficient Gram matrix is exactly the identity. The hierarchy is the
confluent closure of clustered sinc translates, so it preserves the continuous
packet witness class while analytically removing the close-carrier Gram
singularity.

The shifted-Legendre overlap admits an exact `O(N^2)` recurrence. This makes a
complete prime matrix practical at low degree. The finite spaces are nested and
their Ritz minima converge to the continuum compact-envelope bottom.

### L-3603 — carrier gauge theorem

For the full compact-envelope space, carrier translation is unitary modulation
of the Fourier envelope. Thus the carrier does not enlarge the continuum test
class: it is a coordinate gauge or preconditioner controlling finite-basis
compression.

An arbitrary complex envelope decomposes into two Hermitian-symmetric envelopes,
and the corresponding nonnegative test decomposes additively. Therefore a
negative complex-envelope witness implies a negative real-on-the-line packet;
restricting to the real Legendre--Bessel hierarchy loses no negative witness.

### M-3601 — block-confluent search

A stable continuous search should use a few separated carrier centers, each with
a small identity-Gram Legendre block. Cross-center Gram and source blocks are
evaluated by the exact L-3601 formulas. This combines stable local jets with
arbitrary global carrier geometry.

## Computational work

A complete prime-power discovery producer was written for L-3602. It uses exact
integer enumeration, binary128 logarithm/product/remainder, long-double
trigonometry and overlap recurrence, compensated accumulation, and an ordinary
symmetric eigensolve.

At

```text
T = 4709203636353.65
```

the retained ladders were:

| cutoff | dimension | complete prime powers | leading value |
|---:|---:|---:|---:|
| `10^7` | 5 | 665,134 | `+0.03762842178460375` |
| `10^7` | 9 | 665,134 | `+0.03078117008809567` |
| `10^7` | 13 | 665,134 | `+0.02894569108367382` |
| `10^7` | 17 | 665,134 | `+0.02861094133528108` |
| `10^7` | 21 | 665,134 | `+0.02843496091166272` |
| `10^8` | 5 | 5,762,859 | `+0.01055049694092198` |
| `10^8` | 9 | 5,762,859 | `+0.00734955574210520` |
| `10^8` | 13 | 5,762,859 | `+0.00700360683739740` |
| `10^8` | 17 | 5,762,859 | `+0.00695074871143398` |

All values remained positive.

PR #44 reports approximately `+0.006643091775833554` for the 1,024-cell
piecewise family at the same cutoff and carrier. The 17-dimensional smooth
hierarchy is only about `3.07657e-4` above it, a roughly `4.63%` margin
difference with about sixty times fewer coordinates and no Gram conditioning
problem.

## Verification performed

The retained nine-test suite checks:

1. shifted-overlap endpoint identities;
2. transpose parity;
3. the recurrence against independent quadrature;
4. real symmetry of the carrier kernel;
5. scalar Fejer recovery;
6. reality and support orthogonality of the Legendre--Bessel basis;
7. the off-lattice frequency formula against direct support integration;
8. integer-lattice sign congruence;
9. strict rejection of the fractional-index interpolation ghost.

The test transcript records all nine tests passing.

## Candidate counterexamples

None. No directed negative interval was found and no `Z-####` identifier was
allocated.

## Classification

- L-3601, L-3602, L-3603, M-3601: `PROPOSED` pending independent review.
- O-3601: `EMPIRICAL`.
- X-3601 formulas and tests: high-precision noninterval controls.
- Prime enumeration: exact finite integer work.
- Matrix entries and signs: ordinary numerical discovery.
- Counterexample status: none.

## Important strategic conclusions

1. Continuous carrier location is a finite-coordinate gauge, not a distinct
   continuum witness class.
2. Close-carrier optimization should be done in the orthogonal confluent basis,
   never with a nearly singular raw sinc Gram matrix.
3. The optimized 1,024-cell basin is highly compressible: its smooth local
   content is captured by approximately 17 modes.
4. One local confluent center did not reproduce the broad old X-0602 packet at
   height `3e12`; the next geometry should use two or more separated confluent
   centers.
5. A small block-confluent finalist is far cheaper to evaluate with balls than
   either a 1,024-cell matrix or a dense 128-carrier raw packet.

## Remaining uncertainty

- The exact block formulas require independent analytic review.
- The overlap recurrence needs a directed implementation for certification.
- The empirical matrix replaces exact archimedean and pole blocks by the leading
  scalar.
- Huge phases and accumulation are not enclosed.
- The RH implication remains tied to the T-2801 normalization review.

## Recommended next actions

1. Implement a two-center block-confluent search with degrees approximately
   `8--16` at each center.
2. Optimize center separation against the exact sinc Gram matrix.
3. Recompute every retained finite prime entry directly, not through a wide FFT.
4. Add Arb enclosures for the compact archimedean and pole blocks.
5. Freeze a finalist to exact dyadics and pass its fixed-vector form to the
   existing exact witness checker.
6. Compare its envelope with the cloud-directed piecewise result once PR #64
   completes.

## Process improvement

Continuous carrier searches should publish both the physical test-function norm
and the coefficient Gram spectrum. A raw Euclidean negative in an off-lattice
basis is not even a valid nomination unless the generalized Gram problem has
been handled and the physical vector is nonzero.
