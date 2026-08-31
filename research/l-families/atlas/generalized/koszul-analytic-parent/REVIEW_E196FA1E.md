# Independent exact-SHA review: effective resonant pole classification

Reviewed scientific freeze: `e196fa1e4265b482ad1fa495436ed0e4ff088419`.

Inspected the complete proof `FINITE_RESONANT_COHERENT_POLES.md`, the 374-line producer `finite_resonant_poles_replay.py`, all 22 test methods in `tests/test_finite_resonant_poles.py`, and the replay/verification scope. Confirmed the committed five-file packet and reread the frozen proof. Paths are under `research/l-families/atlas/generalized/koszul-analytic-parent/`.

## Independent mathematical findings

The equivariant Mobius inversion retains the necessary group powers. Its elementary dimension and nonidentity-character bounds give the stated sufficient inequality with margin 1228 at n=6. The decreasing normalized right side proves strict domination for every even n at least six; the bounded rows are not used as an extrapolation.

The exact grades two, four and eight cover both equal and opposite resonant elliptic signs. Together with the previously proved all-Q divisor rule, they establish exactly two double poles, at the two zeros of `P_E(z^2)`, and no other interior poles. The strict excess principal zeros on all larger even-grade circles give dense boundary accumulation and the claimed meromorphic natural boundary.

The complex principal-part subtraction and the integer polynomial multiplication are correctly distinguished. Subtraction leaves a holomorphic unit-disk function with coefficient root limsup one, without claiming algebraic residues. Multiplication by the actual `P_E(z^2)` gives the unique constant-one minimal polynomial clearing factor, degree four, and the stated integer coefficient recurrence. Neither operation improves the original Euler coefficients' quarter-power root growth. The fully resonant hypothesis is essential throughout this classification.

## Independent code and test reading

The producer authenticates the prior source before import, reconstructs bounded Adams characters and compares them with the frozen native source, and checks the inequality bounds against actual multiplicities. The low-grade controls separate the two elliptic sign patterns. The principal-part examples are plainly labelled algebraic calibration rather than computed arithmetic residues; the F7-to-F49 elliptic clearing factor is separately authenticated from the existing source and requires no F49 enumeration. Input and canonical-JSON controls are present. No implementation or coverage blocker was found in the complete producer/test read.

## Execution and scope

I did not run computation. The parent reports Ruff, all three producer modes, and 22 ordinary plus 22 optimized tests passing, with test times 0.430 and 0.435 seconds and final rebound producer checks passing. Those are parent-reported execution results, separate from this independent proof/code review.

This is an effective source-specific consequence of the classical character, cohomology and Euler machinery already named in the packet. It is not a new general pole theorem, an automatic ramified tensor-algebra realization, a larger Schatten domain for the original Lie operator, a number-field transfer, or an RH statement. The subsequent proposed constructible-algebra source is a separate packet and is not included in this freeze.

No remaining proof or code blocker found.
