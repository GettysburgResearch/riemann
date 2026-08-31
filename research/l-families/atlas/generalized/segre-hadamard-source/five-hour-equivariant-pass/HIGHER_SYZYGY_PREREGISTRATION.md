# Complete Q-syzygy source before the actual d2

Status: preregistered before complete weight enumeration or rank acquisition.
Date: 2026-09-01. This is a separate packet after the accepted rank65 d2 calculation.

## Exact target

Using the canonical GL3 times S3 stable complement Q=(1-e_sym)R_1 and the source cycles/actions frozen in the first Q-action packet, compute the complete weight decomposition of

    delta: Lambda^2 Q tensor B_(1,2) -> Q tensor B_(1,3).

The source and target have total dimensions2720 and1105. Enumerate every weight of total degree12 that occurs in either side. For each complete block, retain its dimensions, exact rank, kernel dimension and rational matrix digest. No three-weight inference or target-character inference may replace this calculation.

The preregistered primary question is whether delta is surjective. A failure is a valid nonzero Q-Koszul H1 result and must be retained literally. If it is surjective, the E2 source of the already accepted higher differential has dimension1615.

## Representation and higher-differential consequence

Independently compute factor-S3 traces on the source and target from the frozen complete characters and exterior-square character identity. Verify them against direct action on the exact complete kernel; do not merely subtract dimensions. If delta is surjective, the kernel character must be (1615,-25,-35).

Import the separately frozen actual-d2 packet only after authentication. Its rank65 target character is (65,-25,35). If the complete source and actual d2 hypotheses both pass, prove that the surviving E3_(2,1),internal4 factor representation has character (1550,0,-70), hence

    235 trivial + 235 sign + 540 standard.

This forgets the GL3 grading only at the last displayed decomposition. The artifact retains all GL3 weights. No assertion about later higher differentials or the final ambient Tor group follows.

## Formality gate

State separately the standard filtered-complex implication: a filtered-compatible Sym(Q)-linear formality equivalence from the W-Koszul dg module to its homology module would force the associated change-of-rings spectral sequence to degenerate at E2. The already accepted nonzero d2 therefore obstructs such formality. This is not a claim that no unfiltered vector-space quasi-isomorphism exists, and no uniqueness of marked cycle representatives is inferred.

## Bounded replay

New producer `higher_syzygy.py`, artifact `higher_syzygy.verification.json`, replay note and `tests/test_equivariant_pass_higher_syzygy.py`. Bind the exact first Q-action freeze and the exact actual-d2 freeze once supplied. Authentication precedes compilation/parsing. Use exact rational arithmetic, complete weight blocks <=512, coefficient cap4096bits, artifact16MiB, working set1GiB and wall time240seconds. Shape mode precedes elimination and refuses if any declared cap fails. Negative controls change a complete weight, matrix column/sign, direct kernel action, source binding and numeric JSON type. Ordinary and optimized modes are required.

The computation is finite source algebra. It supplies neither a general (d,m) theorem, an arithmetic Frobenius sheaf, purity, nor any RH conclusion.
