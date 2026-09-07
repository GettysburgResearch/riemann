# Independent review handoff

Please review this as a component-theorem packet and a failed closing
attempt, NOT as an RH proof. The open premise in PROOF.md 7.3 is not a task
for the referee to fill in or silently accept.

## Claims to examine

QP26.1: Every finite Gram of the ACTUAL factorial-source all-pass orbit has
the explicit quasipolynomial floor in PROOF.md 3.1--3.2. Quantifiers include
all ranks, both signs of frequency, all multiplicities, and possible off-line
zeros. The source normalization at the removed pole is essential.

QP26.1a: Section 4's source-cutoff time O(log^2 n) preserves the Gram floor
with complete filter tails. It is not an arithmetic complexity theorem.

QP26.2: The inverse-input lower bound in Section 5 is general, sharp in its
exponent, and applies to the actual source without assuming zero simplicity.
It prohibits a bounded-input exact inverse, not approximation in the closure.

Open: No quantitative capture of the horizon-dependent target is proved.
Neither small-time certificates nor Gram conditioning close this assertion.

## Load-bearing proof checks

1. Reconstruct (1.2) from the Euler--Maclaurin convention, including the
   coefficient of B5 and the cancellation of the zeta pole.
2. Check the radius-4 bound, the nonzero normalization on Re s=2, the two
   Jensen counts (radius 3 and radius 7/2), and the finite Blaschke/Harnack
   estimate. No point inside a removed zero disk may be used for the lower bound.
3. Check the Cayley measure, tail arc and polynomial L-infinity estimate.
   The global zero union deliberately overcounts; verify that it contains
   every local zero required at every retained t. No actual zero list is used.
4. Check every power of 2 in (3.5)--(3.6), especially the final square and
   retained polynomial mass. The resulting constants are conservative.
5. Check that all source truncations retain future filter tails; verify
   (4.3) prices perturbation relative to the finite floor before inversion.
6. Check the choice r=8epsilon^2/h0^2 in Section 5, the small-error condition,
   and the distinction between exact range and its closure. The rational model
   verifies sharpness but is not a substitute for the zeta source.

## Limitations

No external novelty claim; the tools are classical. No new zero-free region,
zero count, RH proof, all-horizon gain, parent-code replay, Lean build, or
remote CI result is asserted. Large displayed ranks are parameter arithmetic
only, not Gram computations. The analytic theorem is not machine-proved by
JSON consistency or by the bounded checks.

## Publication request

Add this directory on the existing PR #812 research branch or a new stacked
research branch. Preserve its parent packet byte-for-byte. Do not modify main,
review verdicts, canonical registries, formal sources, workflows or settings.
The publication receipt must name the actual new commit once uploaded; no
local tree/patch identifier should be represented as a remote commit.
