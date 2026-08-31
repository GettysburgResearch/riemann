# Replay of the infinite extension-order comparison

This companion is separate from the first finite-generator packet. Its theorem
is `INFINITE_EXTENSION_ORDER.md`. The completion dependency is frozen at
`64075f1a3f81529f217dee1ae139656dfb9356f3`; the finite-extension dependency is
frozen at `0018b73f60e42bc793d172c381547de34322d8ca`. Both proofs and producers
are authenticated before dynamic imports. Missing pins fail closed.
No execution of this companion is claimed yet.

The declared source panels are the actual coherent S3 algebra over F7 with
parameters A=1,B=0, its constant-field extension to F49, every old/new/infinity
inertia type, and the first two even generators T2=Std and T4=sign+Std.
No new group or curve is selected after viewing output.

The independent controls are:

- Triangular PBW character extraction versus the frozen Mobius formula and
  odd-divisor anti-invariant projection, through grade48.
- Symmetric-generator products versus their Newton recurrence, and full
  Reynolds averages versus the reduced V/W/X/Y boundary ratios, through grade24.
- Literal eigenmonomial bases through grade8 using actual T2 and T4, including
  residual infinity Frobenius signs. The new T4 anti-invariant vectors add six
  old-C2 cokernel vectors in grade5. The degree4 trace/dimension discrepancy
  remains 1 versus13 at nonsplit infinity for the T2 source.
- The F7 discriminant factorization, its two rational branch signs and the
  irreducible degree-two branch norm. F49 uses constant extension and norm,
  without an F49 enumeration. Omitting the degree-two branch changes grade6.
- The exact degree4 failure of the proposed scalar norm identity, while
  explicitly retaining ordinary sheaf base change.
- Exact finite-generator critical products up to grade8 and rational
  enclosures for analytic-unit logarithms using24 generator pairs and the
  proved infinite remainder bounds. No divergent infinite product is evaluated
  at the boundary, and no radius is inferred from numerical fitting.

All coefficient, field and precision caps are explicit. Large multiplicities
are used as integers; no high-dimensional Lie space or matrix is expanded.
Only the small T2/T4 invariant bases are enumerated. Each logarithm is enclosed
by rational atanh remainders, weighted before outward dyadic rounding.

Parent-serialized commands from the worktree root are:

    python -B research/l-families/atlas/generalized/extension-order-defect/infinite_replay.py --write
    python -B research/l-families/atlas/generalized/extension-order-defect/infinite_replay.py --check
    python -B -O research/l-families/atlas/generalized/extension-order-defect/infinite_replay.py --check
    python -B -m unittest discover -s tests -p test_extension_order_infinite.py
    python -B -O -m unittest discover -s tests -p test_extension_order_infinite.py

Ruff is restricted to this producer and its test file. The root applies the
shared RAM gate before running these commands. Independent proof reading is
complete for the principal comparison; the new finite-generator critical
constants, code and final source freeze still require review.

The proof establishes the F7 before-source radius1/2 versus after-source
radius1/sqrt(2), and the changed F49 branch exponent. Those are not outcomes
of the finite test table. This packet does not assert an ordinary Fredholm
determinant at the critical point, a finite-rank infinite constructible sheaf,
failure of sheaf base change, or any number-field/RH consequence.
