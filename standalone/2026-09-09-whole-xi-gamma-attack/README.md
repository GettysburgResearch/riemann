# Whole-function xi attack: gamma convolution, reflection, and remote zeros

**Outcome: the proposed full RH proof fails at its finite zero-location step.**
The supplied mathematical result is an explicit approximation of the whole
xi function, together with a proof that these finite approximants have
spurious off-line zeros in the actual critical strip. This is not an RH
counterexample. Independent mathematical review is required.

## What was attempted

Instead of refining the residual solver again, this pass tested a global
route inspired by the classical Biane--Pitman--Yor representation:

1. Sum independent Gamma(2) variables with the exact weights 1/n^2.
2. Take finite complex moments and impose s versus 1-s reflection.
3. Remove all finite Mellin poles using a precisely stated gamma factor.
4. Prove the resulting entire functions have only critical-line zeros in
   the critical strip; local uniform convergence would then prove RH.

Steps 1--3 are supplied, with exact values 1/2 at s=0,1 and compact error
O(1/N). Step 4 is false for this construction. The manuscript proves:

- An exact rational-sign certificate at N=256 forces infinitely many zeros
  of that approximant in 2/3<Re s<1, at unbounded heights.
- More generally, for each beta in (1/2,1), EVERY sufficiently large cutoff
  has arbitrarily high zeros with real parts arbitrarily close to beta.

The second result uses ordinary unconditional PNT. The first does not.
Finite prime phases are transferred to zeros of the actual approximants
using recurrence and Rouche, not treated as a random model for zeta.
The entire completion is nonzero on the critical strip, so the displayed
zeros are not artifacts introduced by its removable-pole normalization.

Read **PROOF.md** and **REVIEW.md**. The new family is not the finite Euler
product, native Mobius polynomial or positive graph used in other packets.
Its exact limiting source is xi; no equality of its finite zero divisor with
xi is asserted. Positive Mellin measure is retained before regularization;
a positive-probability interpretation after gamma regularization is NOT claimed.

## Relation to the project

The selected current reading is recorded in SOURCES.json. Main's cumulative
route map and xi hypothesis-strength note were used to reassess the attack.
The recent divisor, source-domain and residual work controls important
components but does not supply the global sign. This note does not accept
any earlier author work or amend the pending integration.

The direct claim above is materially different from proving another
truncation rule or an RH-equivalent residual estimate. It tests an entire
proof architecture and gives a definite negative answer to its proposed
all-height lemma. That does not establish another route to RH. No improved
native residual bound, sparse-failure count or unbounded Weil sign is proved.

## Executable scope

```
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
```

Standard-library integers and Fractions only. See VALIDATION.md for the
executed boundary and the separate exploratory calculations. The code does
not evaluate gamma, zeta, xi, a complex zero or a phase-return height.

This is a proposed research packet, not a canonical accepted theorem and
not a complete RH proof awaiting only a referee's signature.
