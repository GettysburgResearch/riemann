# Validation, sources and review boundary

Status: proposed reviewable component mathematics, not independently reviewed.
The author of the proofs also wrote the checker. There are no agent-review
receipts because no independent agent or human reviewed this pass.

## Reproduced locally

From this directory:

    python checks/check_singletons.py > /tmp/singletons.json
    python -O checks/check_singletons.py > /tmp/singletons-o.json
    cmp /tmp/singletons.json results/checks.json
    cmp /tmp/singletons-o.json results/checks_optimized.json

Both runs passed 23,604 predicates and their outputs were byte-identical.
The checker uses integer pairs in Z[omega] and fractions.Fraction, not floating
point evidence or interval certification. Explicit failure predicates remain
active under -O.

It verifies 48 symbolic largest-singleton decompositions; 2,052 physical row
identities and moment expansions; exact local combinatorics through k=40;
local symbol multiplicativity; masks; selected absolute majorants; and the
strict enlargement of the selected tuple domain. Predicate totals include
setup checks and are not a count of independent analytic cases.

The character data are the two primes over 7, the two primes over 13, and the
inert prime over 5 of norm 25. ALL squarefree products of these FIVE ideals under
the cap are used, not all Eisenstein columns under the cap. The X=25 panels use
all 54 nonzero element rows of norm at most 13; X=91 panels use a declared subset
of nine rows. Windows are finite sharp-cap models, not the universal analytic
test. The mathematical identities do not require a smooth window for their
finite versions.

Four deliberately false substitutions are rejected: the wrong Mobius root sign,
dropping the new prime exclusion, identifying conjugate split primes, and deleting
a principal nonunit mask because its charge is zero. During development, omega
was initially chosen as the split-prime distinction witness; its two symbols
coincide. The witness was corrected to the rational element 2. This was a test
fixture error, not a theorem repair. No failing test is concealed as a pass.

At X=91,k=2,y=7 with the selected nine rows, the diagnostic gives native moment
1580, selected signed sector 1132, and rooted remainder 448. The two previous
projection sums are 1194 and 1146. This illustrates exact accounting only; it
is not an asymptotic comparison, dominance claim for signed values, or empirical
support for the open remainder estimate.

## Recovered packet replay

The eleven files in ../2026-10-13-replica-physical-model were extracted from the
user-visible riemann-replica-continuation.zip and matched against its original
manifest. Its existing verifier passed the complete ten-payload inventory.
Its checker was run in ordinary and optimized Python; each reproduced the
archived exact_checks.json byte for byte. The archived mutation report is
preserved, but its mutation-generation procedure was not newly replayed.
The old local-publication labels in that packet are preserved historical bytes.

## Analytic review performed here

Same-author reconstruction checked: the positive local polynomial and its
quadratic bound; every growing-k constant in Theorem 5.1; both Rankin weights
in the singleton-norm bound; the total prime ordering including equal norms;
the minus sign and factor 2k; the unchanged physical row measure; the D/Np
window; and the failure to infer an open signed bound from any of these identities.
This reconstruction is not independent peer review.

The only quantitative external input to the NEW upper bounds is classical
elementary Chebyshev counting, with its proof outline and ideal adapter included.
The new proof does not assume native second moments, the imported quasi-RH
framework, GRH, a large sieve, or unproved prime randomness. The existing
moment-to-zero extraction is mentioned only as a conditional payoff.

## Publication procedure

Work is additive on a newly created branch based at PR #932 commit
c63b5aaa5d53dd183abb20299cea4628f0ab57b7. No inherited proof, main, integrated
status, workflow or CI configuration is altered. Local shell network access
failed, so writes use the connected GitHub Git-object and pull-request actions.
Remote object IDs and the final PR head are checked separately after creation.
The manifest authenticates payload bytes only, not mathematical truth.

Preferred independent review: Sections 2, 5, 6 and 7 of MATHEMATICS.md, followed
by fresh finite-check replay. The smallest missing mathematical claim is the
one-sided physical prime/cofactor bound (OPEN-k), particularly (OPEN-2).
