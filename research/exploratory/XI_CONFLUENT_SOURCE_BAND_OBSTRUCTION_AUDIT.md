# Independent audit: Xi confluent source-band obstruction

Status: exact-source review passed; no mathematical or machine repair needed.
This is proposed, reviewed programme mathematics, not an integrated RH result.

Reviewed source: 8ef225b8753e2cd1f9c031fbb8038d1321c7f308.
Programme copy: 26420e1b4defbb43004ed91d97e08f92af7e44ee.
Review date: 2026-08-30.

The root read the complete proof, producer, tests and manifest; reconstructed
the analytic derivations; and replayed the source-authenticated fixture.
A separate exact-SHA reviewer independently checked the mathematics and code.

## Frozen identities

The [proof note](XI_CONFLUENT_SOURCE_BAND_OBSTRUCTION.md) has Git blob
76152f000c026c4a68ade2593b16ffbd7e0de528 at the reviewed SHA.
The producer, fixture and tests have blobs, respectively:

- 62c87dd4460670e9d2d0688ac60b4f8b529f87c5;
- d788b8d95ebfa47b3216eb3a94a7876d88b14f1e;
- 243e3615bb360a64009235a7c6a62b392967ee99.

All ten declared frozen source/review bindings authenticate, including
L-106671, L-106673, the actual-Xi concentration source and its independent
review. The current five-file packet is unchanged from the reviewed source.

## Proof review

The following load-bearing points passed independent reconstruction.

1. In the literal reduced endpoint N=OB_+, D=OB_-, the finite multiplication
   jets C=J_O and V=J_(B_+) commute with each other, not with the Hardy Gram
   or a band projection. Since J_R=VC and G_O=C^*GC, the determinant and
   source-band trace formulas are exact congruences. Dropping G_O is invalid.
2. For a single confluent cluster the Fourier space consists of polynomials
   of degree below q times exp(-(y+ia)xi). Rodrigues' formula, integration
   by parts, the three-term recurrence and the Laguerre ODE give the norm,
   first moment and derivative energy used in CB12.
3. The identity for x phi_j(x)^2 in CB13, followed by weighted
   Cauchy--Schwarz, has the correct sign and constant 2j+1. Summing proves
   xi K_q(xi,xi)<=q^2 uniformly in a,y and all positive integers q.
   The classical ODE and gauged form also agree with
   [DLMF 18.8, rows 8 and 10](https://dlmf.nist.gov/18.8).
4. Trace domination gives the claimed band Loewner bound in any derivative
   frame. Congruencing by actual J_R and contracting against G_O^(-1)
   preserves positivity without a condition-number loss or free-coefficient
   assumption.
5. For the actual-Xi accepted set, the fixed-K tail limits are uniform over
   xi>=X/2. The first localization estimate gives xi-X=o(1), after which
   substitution improves it to O(e^(-X)/X). Solving the exact rho identity
   gives the stated center and endpoint constants uniformly on the accepted
   set. Neither connectedness nor monotonicity in physical frequency is
   needed or asserted.
6. The error in the enclosing logarithmic width is independent of a,y,q.
   Therefore q=o(X exp(X/2)) suffices for the asserted vanishing band ratio.
   The zero-total-charge case is handled without division.

The dense-union countercontrol is valid: orthogonality to all polynomial
times exponential functions kills every derivative of a Laplace transform
at an interior point; analytic and Fourier uniqueness then give zero.
This does not claim actual Xi multiplicities are freely selectable.

The physical Blaschke convolution and its projection commutator were
independently recomputed. The tail is 2(B-A)exp(-s) for s>B, with squared
norm 2(B-A)^2 exp(-2B). Thus a nonzero inner factor cannot simply be commuted
through the frequency projection.

## Reproduction and controls

The root reran all 23 tests and the full producer in normal Python and
Python -O; all passed. Every declared source identity and artifact hash
matched. The second reviewer also replayed both modes, Ruff and whitespace
checks; the author separately reported a clean detached CRLF replay.

An additional independent root calculation used direct factorial integration
for Laguerre orders 0,...,16: 289 cross-orthogonality checks and 51 norm,
first-moment and derivative-energy checks passed. This extended census was
a memory-only review control, not a change to the bounded source fixture.

The second reviewer additionally reported an exact complex-Hermitian
congruence control beyond the real-rational producer. The root's own algebraic
proof check uses Hermitian adjoints throughout; no real-only argument is
silently used for the complex theorem.

The rational q=2 control retains total charge 82/81, while dropping the
outer metric gives 172/81. Its band traces are 2-6exp(-2) versus the incorrect
12-44exp(-2). These are synthetic native Hardy models, not sampled Xi jets.
The retained positive charge is compatible with, and does not eliminate,
the topological index.

## Decision and exact scope

Accept the packet as stated. It proves a coarse, all-multiplicity estimate
for one confluent source cluster and an actual-Xi accepted-frequency
envelope. A stronger bound discovered later should have its own identity,
not rewrite this reviewed proof.

At this source identity, arbitrary distinct-node clusters and the physical
inner-weighted band Gram in CB26 are not bounded by the packet. Nor does it
identify the scalar Xi residual energy with Pick free energy. Those are
explicit remaining questions, not conclusions supplied by finite tests.
Fixed K and M, the reduced endpoint normalization, exact outer retention
and the distinction between source jets and physical multiplication remain
mandatory. No critical-line proportion, density-one result, or RH conclusion
is inferred.
