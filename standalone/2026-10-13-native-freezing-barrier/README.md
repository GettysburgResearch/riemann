# Native obstruction to uniform prime-freezing continuation

**Status: proposed component mathematics, not independently reviewed.**
The generalized native moment and RH remain unproved. This pass establishes
an obstruction and a sharp operator cost; it establishes no improved full
moment or zero-free exponent.

## The result that changes the continuation strategy

The preceding #936 packet controlled a mask-preserving partially randomized
moment when native prime phases were retained through log-square. Its
sharpness example allowed arbitrary phases or an uncontrolled-height CRT
row. The new argument needs neither: it uses the true Mobius coefficients,
one fixed nonnegative compact smooth test, and actual sixth-power rows
inside H=D^h.

For the partial moment Q_(k,y), a uniform diagonal bound throughout
2<=y<=(log D)^A is impossible whenever

    A > 12k/(6k-5h),       0<h<6k/5.

For k=2 and h=21/20, a concrete consequence is

    Q_(2,y)(D,D^(21/20)) >= c H D^(2+1/16)/log D

along unbounded pairs with y<=(log D)^4. This lower bound is for the
partially randomized model, NOT the original unrandomized moment.
For cofinal orders with h_k=o(k) and defect e_k=o(k), every fixed A>2 fails.
Thus #936's logarithmic-power-two boundary is sharp for this uniform-cutoff
hierarchy even with native coefficients.

## Mechanism and complete proofs

1. [SMOOTH_MOBIUS_RESONANCE.md](SMOOTH_MOBIUS_RESONANCE.md): the finite
   smooth-Mobius product has logarithmic magnitude asymptotic to
   y^(1-sigma)/((1-sigma)log y) at t=pi/log y. An exact Mellin identity with
   the original compact test forces a large smooth-Mobius sum at a physical
   scale D>=exp(y^(1/A)). The maximal exponent for y<=(log D)^A is exactly
   1-1/A. The proof localizes the witness window and gives sharp forward and
   inverse small-prime dilation norms.
2. [NATIVE_PARTIAL_MOMENT_BARRIER.md](NATIVE_PARTIAL_MOMENT_BARRIER.md): on
   sixth-power rows coprime to the frozen primes, the conditional mean is
   the actual smooth-Mobius sum. Jensen and genuine replicas in the row box
   give the displayed lower moment bounds. The fixed-order and cofinal
   quantifiers, and the required cancellation in any successful recoupling,
   are explicit.
3. [SOURCES.md](SOURCES.md) and [VALIDATION.md](VALIDATION.md) record classical
   credit, inspected sibling work, exact finite tests, and review limits.

The witness chooses y within a permitted range. No lower theorem on the
single prescribed curve y=(log D)^A, no failure at every D, and no sharp
fixed-order converse threshold are asserted. The window refinement yields
nearby power-law witness sequences, not that exact-curve statement.

## What failed and what remains

Extending the proven partially independent model to ever more native primes
while requiring every intermediate model to remain small cannot supply the
cofinal hierarchy in this uniform form. If the desired full native moment
is small at the exhibited scales, nearly the whole oversized reference
must be cancelled by negative rough-block interference. The next target
must keep that signed compensation; a generic positive comparison is not
an adequate substitute.

The safe-cutoff one-sided remainder from #936 is still open. The new
lower bound is not evidence against its possible validity or against RH.

## Reproduce the finite diagnostics

    python checks/check_native_barrier.py > /tmp/native-barrier.json
    python -O checks/check_native_barrier.py > /tmp/native-barrier-opt.json
    cmp /tmp/native-barrier.json results/exact.json
    cmp /tmp/native-barrier-opt.json results/exact.json
    python checks/verify_manifest.py

All arithmetic diagnostics are exact integers, cyclotomic pairs, or
fractions. They test finite Euler and projection identities, true sextic
nonunit masks, norm multiplicities, and exponent algebra. They do not
certify prime asymptotics, Mellin estimates, or any infinite moment claim.
The copied Eisenstein arithmetic helper is bound to its #936 source bytes.
