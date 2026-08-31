# Independent replay of the arithmetic AFTER-radius dichotomy

This packet accompanies `ARITHMETIC_RADIUS_DICHOTOMY.md`. Its execution is
pending. The root owns the proof and discovery captures; the independent
producer/test implementation was written by `/root/generalized_l_review`.
No executable predecessor is imported. Five frozen source notes are checked
by Git blob identity and normalized byte hash before any discovery record
is accepted.

The declared finite parameter set is every admissible A!=0,B over
p=5,7,11,13,17,19,23,29,31, excluding singular cubics. These are3044 parameter
rows, not3044 curve isomorphism classes. Python reconstructs the elliptic
point counts by literal ordered quadratic solutions and the cubic fibres by
a complete polynomial preimage table. This is independent of the JavaScript
square-count lookup. It retains the sign-zero point, the two old branch signs,
the two nonzero completely split signs, and normalized infinity. Every raw
row, trace histogram, example and panel count must match the saved JS capture.

The new scalar classification uses exact fractions and the proved AFTER
criterion. It distinguishes the pure multiplier exponent from the actual
finite-source zero orders. The prior scout-derived class-count prediction is
1798 radius1/2 rows and1246 radius1/sqrt(2) rows; matching it is a finite
implementation check, not a proof of the all-field theorem.

Declared detailed panels are F5(1,0), F7(1,0), F11(1,3), F11(1,4),
F13(1,5), F13(4,1), and the separate heldout F31(1,2). They check literal
affine solutions on the actual genus-three Galois closure and its normalized
infinity, as well as the two elliptic factors. Exact finite polynomial
products through generator grade12 are compared with a Newton recurrence
formed from Frobenius powers, with coefficient cutoff24. No large field
extension is enumerated.

The source character controls cover every even grade2 through128. General
equivariant PBW extraction is compared with the restricted-divisor formulas;
the explicit dimension, transposition and cycle remainder bounds are checked
separately. Low-grade source irreducibles and the sharp grade-six errors are
retained. The all-grade estimates themselves are proved in the note.

All record comparisons use canonical serialized JSON with `allow_nan=False`.
Boolean/integer/float substitutions, nonfinite floats, source-field changes,
and artifact tampering have explicit tests. Cached primitive source values are
immutable tuples; public rows are fresh dictionaries. Input, coefficient,
field, byte and arithmetic caps are checked before computation.

Parent-serialized commands from the worktree root:

    python -B research/l-families/atlas/generalized/graded-completion-lab/arithmetic_radius_replay.py --write
    python -B research/l-families/atlas/generalized/graded-completion-lab/arithmetic_radius_replay.py --check
    python -B -O research/l-families/atlas/generalized/graded-completion-lab/arithmetic_radius_replay.py --check
    python -B -m unittest discover -s tests -p test_graded_completion_arithmetic_radius.py
    python -B -O -m unittest discover -s tests -p test_graded_completion_arithmetic_radius.py

Ruff is restricted to this producer and test file. Root applies the shared RAM
gate before any run; the worker target is below128MiB. No passing result or
measured memory usage is asserted until root records execution. The theorem
requires its separate proof audit and exact-freeze report.

This packet does not compute the BEFORE-extension criterion. That comparison
has its own source proof and replay. It also does not promote scalar analytic
continuation to a larger ordinary trace-class domain or claim a number-field,
archimedean or RH consequence.
