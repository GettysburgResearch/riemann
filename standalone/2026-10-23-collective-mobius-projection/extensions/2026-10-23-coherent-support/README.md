# Coherent continuation and physical-support extension

Status: proposed, source-dependent mathematics; internal review only.
This additive packet preserves the earlier PR1019 files byte for byte.
Its inherited conventions, analytic sources, source-pin errata, and imported
PR1013/1015 proofs are in the parent packet two directories above.
Every norm power below suppresses the explicitly stated epsilon losses.

The strongest currently reviewed actual-projection statement is
`COHERENT_PRIMITIVE_REMAINDER_VECTOR.md`, CP8:

    ||P_K A_U bar(b)||^2
       << KU + D^(11/12) K^(1/12) + D^(5/6) K^(7/6)
          + U^(1/3) D^(2/3),
    K <= D^(1/7), K <= U^(1/2-delta), U >= 1.

For U=D^(6/7), K=D^(1/12), the result is D^(20/21+epsilon),
against the inherited D^(41/42) inverse resource. Thus the same 1/42
saving now covers labels through D^(1/12), instead of the earlier
unconditional example D^(1/32). The label set is sixth-power-free.
This is an estimate for the actual arithmetic coefficient and its full
specified projection, including its pole and continuous contribution.
It does not estimate the orthogonal complement.

The physical local modulus constraint supplies a separate stronger full-series
finite-vector factor `min(K,1+K/sqrt(X))`. Its proof is
`LOCAL_SUPPORT_VECTOR_REFINEMENT.md`; the deduction in
`LOCAL_SUPPORT_RESIDUE_RANGE_EXTENSION.md` gives residue energy D^(2/3)
through K<=D^(1/6) and, at every physical scale U>0,

    sum_R |R_R^full(U)|^2 << D^(11/12)K^(1/12)+D^(5/6)K,
    K <= D^(1/6).

At U=D^(7/8), K=D^(1/8), the latter is D^(23/24), a 1/48 saving
against D^(47/48). This full-series improvement is not silently substituted
into the primitive theorem: its local inversion and partial poles are separate.

## Proof and review map

1. `COHERENT_FULL_REMAINDER_VECTOR.md` and `COHERENT_FULL_ALL_SCALES.md`
   retain every reciprocal-completion term and the exact subunit pole.
   Their older plateau remains a valid input to the primitive proof.
2. `LABEL_EULER_DENOMINATOR_CLOSURE.md` supplies uniform restoration of
   label-supported Euler factors.
3. `COHERENT_PRIMITIVE_REMAINDER_VECTOR.md` retains the common inverse row,
   restricted-row aggregation, and the exceptional fifth-power inclusion-exclusion.
   Its exact final hash is bound in `REVIEW_COHERENT_PRIMITIVE_VECTOR.md`.
   That reviewer co-derived several local ingredients; the receipt explicitly
   distinguishes this authorship from checking the final assembly.
4. The physical-support and residue-range notes have separate internal reviews.
   Root authored the former and reviewed the latter; the global agent reviewed
   the former and authored the latter.

The analytic functional equation, sieve, inverse-row estimate, density identities,
and Gram theorem are imports from the named source versions and predecessor
commits. This packet does not independently reprove all imported theorems.
The finite checkers authenticate local rational inequalities and exponent
bookkeeping. They do not certify the imported analysis or prove RH.
`FINITE_REPLAY.json` records normal and optimized isolated Python runs,
166 exact predicates in total. `COMPONENT_MANIFEST.json` binds 22 source files.

## Other explored routes

`RAW_FUNCTIONAL_EQUATION_ZERO_RESIDUES.md` records why a tempting gamma
cancellation does not remove the zeta-zero residues from a raw contour shift.
It is a diagnostic, not a stronger remainder theorem.

The Artin-rescaling and normal-family notes identify obstructions to promoting
a common zero-free half-plane to RH. The quantitative note gives a lower bound
on the non-normality of the constructed quadratic family.
`FINITE_ORDER_HEAT_TRACE_POSITIVITY.md` derives finitely many derivative-sign
inequalities from an imported verified zero height; its example covers
12.5 billion derivative orders. This is not complete monotonicity of every
order, a higher verified zero height, a new zero-free region, or RH.

No smaller fixed B_flat is proved. The complementary inverse space and the
primitive partial-pole/volume losses remain the central route-specific gaps.
These results are submitted as draft research, without a priority claim.
