# Exact ramified continuation and a shifted zero detector

**Status: PROPOSED component mathematics; NOT PUSHED.** Complete arguments
are supplied, but no independent mathematical referee or Lean build has
checked them. No new global zero-free fraction or RH proof is announced.
This add-only continuation is prepared against #966 at
`8d94494698ee447711a53dec922986586418e398`.

## Results

**1. An actual correction-domain enlargement.** `RAMIFIED_FACTORS.md` sums
all five ramified valuation classes of CT's original Poisson correction.
Their exact rational factors remove the auxiliary requirements
`3 Re xi>2` and `3 Re xi+Re w>5/2`. The remaining Euler-convergence domain
is stated explicitly. On its closed compacts with `Re xi>=1/2`, the
correction is `O_epsilon(q_u^epsilon)` uniformly in height. For each fixed
frequency it also continues to the larger open domain left of 1/2, with
an explicit valuation weight. The complete correction second moment is
`O(U^(1+epsilon))` for `Re xi>1/3`, subject to the other domain conditions.
A prime-square-frequency example proves that an arbitrary-epsilon uniform
supremum really can fail below 1/2. These are statements about the original
correction, NOT about an inverse L-function or zeta zero-free region.

**2. An improved exceptional-character count.** `SHIFTED_DETECTOR.md` moves
the auxiliary zero detector from real part 1/2 to 6/11, changing both its
Mellin factor and its mollifier weights. It proves the off-central numerator
fourth moment with exponent `max(1,13/6-2lambda)` and retains the actual
inducing conductor in the dual AFE. At threshold 3/4 the resulting count is

    R(U) << U^(395/552+epsilon)

on a sufficiently short fixed polynomial-height rectangle. This improves
#966's exponent 43/60 by exactly **1/920**. It is an exceptional-index
count, not a new optimized total-zero-count theorem. The new component
uses DF's stated sieve, Hecke AFE/continuation and classical zero detection;
it does not assume CT's proposed global conclusion or an unknown native
moment. Neither component depends on the other.

## What did not close

The signed fixed-principal-twist estimate remains open. The principal
specialization of CT's old correction still has its stated 2/3 convergence
threshold; moving a nonprincipal correction is not a free replacement for
that scalar numerator. No new all-field boundary is promoted by combining
the two components without a complete new contour calculation.

`ATTACK.md` records the unsuccessful direct mixed-moment attempt and the
remaining jobs. Classical methods and overlapping predecessor results are
credited in `SOURCES.md`; no global literature-priority claim is made.

## Reproduce

    python verify_manifest.py
    python verify.py > /tmp/checks.json
    cmp CHECKS.json /tmp/checks.json
    python -O verify.py > /tmp/checks-opt.json
    cmp CHECKS.json /tmp/checks-opt.json
    python run_mutations.py > /tmp/mutations.json
    cmp MUTATIONS.json /tmp/mutations.json

The 1,507 predicates include finite algebra and repeated parameter guards,
not 1,507 independent analytic cases. Direct complete residue-ring checks
include norms 13, 37 and the unramified norm-25 local ring; see VALIDATION.md
for the precise coverage. The infinite assertions rest on the written
arguments and imported sources, not the number of tests.

No inherited source is changed. `PUBLICATION.md` gives the exact base and
safe patch/branch instructions; there is no remote head SHA for this packet.
