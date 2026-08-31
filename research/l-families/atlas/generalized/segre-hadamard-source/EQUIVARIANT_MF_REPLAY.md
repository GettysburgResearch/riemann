# Equivariant matrix-factorization trace replay

The [proof](EQUIVARIANT_MATRIX_FACTORIZATION_TRACE.md) derives the character
twist from the actual D columns. Its producer uses Gaussian integer pairs
only, with no numerical eigenvalue or executable predecessor import.
The original Chow proof/artifact at `a895f47628b0bc7c7ee5e0392df2f79c24166f92`
are authenticated before rebuilding the source monomials.

The checks compare four-variable even/odd invariant monomials with the
rational character, the complete three-factor Chow source with its module
decomposition, and the visible Euler rows of the minimal resolution.
They retain source weights on every matrix column, the relation character,
and the two-step twist. Five small diagonal panels include two distinct
finite-order trace collapses, a second-power recovery, and two generic
noncollapse controls. Degrees stop at twelve; no homological conclusion
is extrapolated from this finite cutoff.

The ordinary determinant 1-u^2 on the two-dimensional degree-one module
and its second-power trace2 distinguish this example from a vanishing
source. The residual operator is a declared finite linear representation,
not an arithmetic Frobenius identified with an earlier global cover.

Execution is queued for root's serialized runtime. The proof, replay note,
producer, and substantive tests are bound by the fixture.

```text
python -B research/l-families/atlas/generalized/segre-hadamard-source/equivariant_mf_replay.py --write
python -B research/l-families/atlas/generalized/segre-hadamard-source/equivariant_mf_replay.py --check
python -B -O research/l-families/atlas/generalized/segre-hadamard-source/equivariant_mf_replay.py --check
python -B -m unittest discover -s tests -p test_segre_hadamard_equivariant_mf.py
python -B -O -m unittest discover -s tests -p test_segre_hadamard_equivariant_mf.py
```
