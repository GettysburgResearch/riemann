# Shared-prime resolution for the joint sixth-power dilation

Status: PROPOSED component proofs; NOT PUSHED. No independent review.
Scope: the precise pre-Poisson Gauss/theta row operation, finite ideal
algebra, raywise operator energies, and an explicit remaining signed target.
No full native moment, improved zero-free exponent, or RH proof.

Intended base: PR #950, `5a6418b021a35c95bbc2c80775353ee33506faee`.
The current #951 head `aba76e1df38dc438b9f5c5f20b698fb26fb1716e` was checked
at metadata and ATTACK_STATUS scope. Its direct Gaussian transfer is not
repeated here. Nothing in this packet changes an inherited file.

## What was actually advanced

The preceding pass retained common-prime terms in a joint dilation but
had not evaluated their physical-row effect. The new proof gives the
literal divided-row kernel, then splits its dilation ideal into a part
coprime to the Gauss denominator and a part supported on it.

At a denominator prime with exponent NOT divisible by six, the Gauss row
is supported on exactly one valuation shell. Different shared-prime
sixth-power dilations therefore have DISJOINT row supports. This proves
an exact Lp energy identity, not merely a triangle-inequality estimate.
At exponent divisible by six, the zero-extended principal character gives
a Ramanujan sum with overlapping shells; that part is retained and bounded
separately.

For the explicitly defined critical JOINT-RAY row energy, the complete
shared-prime operator has scale- and denominator-independent bounds at
orders two and four. A coarse fourth-energy constant is exp(32 [F:Q]).
At all finite orders the active-prime energy budget is uniformly bounded;
the full fixed-order budget is at worst (Ns)^epsilon. The weaker,
unnormalized L2 version has its own divisor-sized budget.

**These are operator bounds on an UNKNOWN input.** At p<6, a constant
for the full dilation also follows by plain Minkowski in this ray norm;
we do not advertise the constant itself as a new arithmetic power saving.
The exact support split is the additional information. The ray norm is
not the same-height native moment envelope used earlier.

The active bound is sharp for the specified class of arbitrary row
families and a hard-ball test. A concrete compatible artificial source
prevents a universal power saving from this operator alone. It is not
an actual-theta or RH counterexample.

## Reading order

Read RAMIFIED_DILATION.md for all definitions, hypotheses and proofs.
ATTACK_STATUS.md identifies the exact surviving signed sum and the failed
closure attempt. SOURCES.md states what was actually inspected.
VALIDATION.md and results.json describe finite coverage and its limits.

The written S-arithmetic adapter assumes the original primitive-character,
PID/principalization, unit-invariance and Haar data. It uses a sixth-unit
row quotient, so positive unit rank does not create an infinite norm ball.
This is not a fresh formal build of the upstream ActualRecipe.

## Reproduce

From this directory:

```sh
python check_manifest.py
python verify.py > replay.json
cmp replay.json results.json
python -O verify.py > replay-optimized.json
cmp replay-optimized.json results.json
```

Both modes were run and agree: **3,679 explicit finite predicates**,
including setup/repeated checks and nine negative controls. Residue tests
include complete small split/inert residue rings and six declared norm-7
exponent-six samples. The physical tests are finite sparse Eisenstein
fixtures with named prime semigroups, NOT a complete native ideal/row census.
No infinite Gaussian/Schwartz/theta sum is numerically evaluated.

## Publication

This session could read GitHub but exposed no create/update/commit/PR
write action. Plugin discovery returned the installed hybrid connector;
the runtime has no gh executable, and direct network access failed DNS.
No new remote branch, commit, PR, or comment was created. The supplied
add-only patch and application instructions are the publication handoff.

Proposed branch name: `research/ramified-dilation-20261016`.
Main, #950, and #951 are unchanged by this pass.
