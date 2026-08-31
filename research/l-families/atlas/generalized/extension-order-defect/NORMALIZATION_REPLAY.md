# Normalization and exact invariant-base replay

The producer authenticates six Git blobs before importing the frozen C6
monomial helpers or reading the actual Lie source artifact. The older Lie
producer is authenticated as provenance but is not executed. Its sixteen
held source rows are reconstructed independently from the e/s/c Hilbert
series by the equivariant PBW recursion.

Literal controls retain the six Segre coordinates and three minors, the
scaled etale chart, and the full length-five nonflat fibre with its
multiplication and residual action. Separate synthetic polynomial sources
test the exact covariant quotient by invariant monomial divisors, including
same-charge squares, opposite-charge invariant products and trivial base
variables. The single standard-pair formula is checked against the actual
33-generator Segre module, not only against a displayed polynomial.

Actual even Lie cutoffs2,4,8,12 and held-out16 use compressed multiplicities
to produce the full minimal-generator polynomial, including all quadratic
covariants. The exact harmonic identity calibrates the proof's convolution;
it is not a numerical fit or an all-degree error estimate. Generic rank3,
the length-five chart fibre and the33-generator full vertex are different
objects. The infinite finiteness criterion and normalization uniqueness
are proof statements in the prescribed algebraic category, with no claim
that Euler data choose that category or an analytic frame.

Validation status: the root completed serialized Ruff, producer
write/check/optimized-check and28 ordinary plus28 optimized tests.
The proof and implementation also received independent full-read review.
This final note binding is replayed before freezing; an exact frozen-SHA
review is recorded separately. No scientific job was run by the author.

Commands from the GLO worktree (root executes under the RAM gate):

```text
python research/l-families/atlas/generalized/extension-order-defect/normalization_replay.py --write
python research/l-families/atlas/generalized/extension-order-defect/normalization_replay.py --check
python -O research/l-families/atlas/generalized/extension-order-defect/normalization_replay.py --check
python -m unittest discover -s tests -p test_extension_order_normalization.py
python -O -m unittest discover -s tests -p test_extension_order_normalization.py
```

All integer and rational source values are exact. New code limits source
degree16, output polynomial degree36, monomial length8, at most six
synthetic variables and square matrices of dimension at most16. It does
not enumerate large fields or expand Lie multiplicity spaces. Owned-file
hashes normalize LF consistently; canonical JSON comparison rejects
bool/int/float substitutions, duplicate keys and nonfinite numbers.
