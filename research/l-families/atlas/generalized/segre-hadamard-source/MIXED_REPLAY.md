# Grouped canonical-character replay

The independent producer uses the grouped source definition directly. It
forms complete-symmetric characters by multiplying geometric series, rather
than the first packet's composition-sum route. Its polynomial-base weights
are formed separately from symmetric tensors within each group. Exact
character coefficients are compared to the proved canonical-module top term.

Declared before execution:

- Generic `(d,m)=(2,2)+(3,1)`, followed by the multiplicity-reversed heldout
  `(2,1)+(3,2)`, with eigenvalues `(2,3)` and `(5,7,11)`.
- Six invertible diagonal deformations `(1,t)` at fixed declared integer
  values; the `t=-1` leading-character zero must not be labelled a Betti jump.
- The separate rational companion matrix `[[0,-1],[1,1]]` and four positive
  distinct eigenvalues `(5,7,11,13)`. The numerator degree drops although
  the denominator has eight distinct poles and no common factor. Polynomial
  gcd and squarefreeness are computed over the rationals; no approximate
  roots are used.

The producer is self-contained, imports no executable from a previous packet,
and authenticates the captured frozen T-108510 Git blob. It binds the complete
new proof, this contract, its own code and the dedicated tests. This is a
separate fixture; the first packet's frozen candidate files are not modified.

Parent-serialized commands:

    python research/l-families/atlas/generalized/segre-hadamard-source/mixed_replay.py --write
    python research/l-families/atlas/generalized/segre-hadamard-source/mixed_replay.py --check
    python -O research/l-families/atlas/generalized/segre-hadamard-source/mixed_replay.py --check
    python -m unittest discover -s tests -p test_segre_hadamard_mixed.py
    python -O -m unittest discover -s tests -p test_segre_hadamard_mixed.py

No successful execution is asserted yet. All arithmetic is exact and bounded
by at most 24 polynomial-base generators and cutoff 27. The all-grade module
theorem is proved separately; it is not inferred from the replay cutoff.
