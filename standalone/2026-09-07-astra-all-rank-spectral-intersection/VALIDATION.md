# TSR26 validation: a finite torsion proof, not rank extrapolation

Date: 2026-09-07. Environment: Python3.13.5, Linux x86_64. Only the standard
library is used. All arithmetic is integer or fractions.Fraction arithmetic.
No complex root is approximated. No finite field or elliptic curve is enumerated.

## Executed mathematical checks

    python -I -S verify.py --generate /tmp/tsr26-normal.json
    python -I -S -O verify.py --generate /tmp/tsr26-optimized.json
    cmp /tmp/tsr26-normal.json /tmp/tsr26-optimized.json
    python -I -S verify.py
    python -I -S -O verify.py

Both complete outputs are byte-identical. Generation refuses to overwrite its
output; result.json retains the normal-mode output.

The classification executes every one of the4320 affine rows:
180 trace triples (125+27+27+1 across the four square classes), times24 rank
residues. It solves F+kDelta=0 for ALL integers k>=0 by exact coordinate
consistency, sign and integrality, rather than scanning k up to a bound.
The paper proves the affine identity for all k independently. Results:

    admitted recurring rows: 560
    nonzero constant rows:   232
    inconsistent rows:        43
    negative-k rows:        3485
    nonrecurring solutions:    0
    nongraph exceptional rows:24

The24 exceptional rows are four sign triples at each of six residues in a
period24, exactly r==3(mod4). This is an exact finite classification after an
all-rank mathematical reduction. It is not empirical evidence for all ranks.

Additional regressions, separately counted:

- 152 signed integer graph-weight fixtures, at r=1,...,16,32,64,128;
- 304 full rational power-trace graph/square-class-two fixtures;
- a complete 3000-point trace-box comparison of the fast recognition predicate
  against ALL power traces needed for the full characteristic polynomial:
  q in {1,2,3,5,1/2,1/3}, r=1,...,4, A,B,C in {-2,-1,0,1,2};
- the actual primitive order-seven complex residual, which must not be erased
  by the generic argument;
- all nine coefficients of the q=2,r=3 exceptional factor, reconstructed by
  Newton identities and the required raw dilation;
- three refusals by the bounded recognition helper (rank0, rank129, negative q).

The fast recognition helper intentionally caps test rank at128 and input
numerator/denominator sizes at256 bits. The mathematical recognition recipe
is all-rank; its O(log r) count is a rational-operation count, not a bit-cost
bound. The helper's refusals occur before large exponentiation.

## Rejection and package checks

Eight checker-CLI mutations are run in each Python mode: a forged RH flag,
wrong affine-row count, deleted residue table, changed raw polynomial,
forged nonrecurring-solution count, resealed wrong source pin, empty manifest,
and an extra file. Each must return code2 and a REJECTED diagnostic; a pristine
copy must pass. The handoff includes the driver and exact execution receipt.

The SHA256 manifest covers every other file, exact inventory is enforced, and
all bounded mathematical data are regenerated. The checker enforces three
predecessor commit/path/blob records. It does not download or rehash those
unbundled parent payloads. Their pins were read through connected GitHub tools.
No upstream producer, field census or existing formal proof was rerun.

## Authoring correction, recorded rather than hidden

The first hand-written square-class-two table incorrectly used a period-four
sign for its even-rank x coordinate. The complete affine checker rejected it at
r=4, x=y=z=-sqrt2. The table was corrected to the period-eight signs +,-,-,+
for even residues0,2,4,6. The graph-plus-exception theorem was independently
formulated using exact Dickson polynomials and did not change. All final table
rows, graph comparisons and full raw regressions were rerun after the repair.

No floating-point discovery enters this proof. The initial scout used exact
integer residue multiplicities and exact quadratic-ring Dickson arithmetic.
The final checker independently compares the displayed canonical table, the
all-k affine solutions and the graph-plus-exception description.

## Limits of assurance

The eigenvalue-ratio lemma, rational descent, all-k affine reduction and
algebraic-group obstruction are paper arguments, not Lean proofs. The residue
table is exact Python-assisted finite proof data. External mathematical review
and novelty comparison remain pending. The finite result does not establish
elliptic realization, a global compatible system, automorphy, RH or GRH.
The SL2 obstruction requires its explicit reductivity/common-determinant/density
hypotheses and does not assert them for every proposed arithmetic family.

Publication is add-only on a new research branch from the frozen main baseline.
No historical proof, main file, existing research branch, reviewer record or
canonical status is modified. Remote identities are recorded in a separate
publication receipt after the write and read-back checks.
