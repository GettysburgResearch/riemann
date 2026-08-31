# Full invariant-base replay

The separate [proof](INVARIANT_BASE_MATRIX_FACTORIZATION.md) gives the actual
binary cubic source, its full invariant base, and an explicit infinite minimal
resolution over the A1 hypersurface. This producer imports no predecessor
code. It authenticates the frozen Chow proof and artifact at
`a895f47628b0bc7c7ee5e0392df2f79c24166f92` before rebuilding its own primitives.

The new checks are literal W orbit-sum multiplication through degree three,
even-monomial normal forms through degree twelve, a polynomial matrix-square
identity before imposing its relation, and exact augmented resolution slices
through internal degree thirteen. The independent source parity count and
module Hilbert/Euler comparison run through degree sixteen. Sparse rational
elimination has at most 200 rows or columns; actual largest quotient matrices
are 64 by 108. No large field, prime search, numerical rank, or eigenvalue
fitting is used.

The false free-module replacement fails at degree four (67 versus 63).
The finite computations neither prove infinite exactness nor infer eventual
periodicity: those conclusions have the explicit all-degree source proof.
Minimality and maximal Cohen--Macaulay depth are likewise proof statements.

Execution is queued for root's serialized runtime. The test file and this
note are bound in the artifact; a later exact-SHA review distinguishes
independent reading from root-reported execution.

```text
python -B research/l-families/atlas/generalized/segre-hadamard-source/invariant_base_replay.py --write
python -B research/l-families/atlas/generalized/segre-hadamard-source/invariant_base_replay.py --check
python -B -O research/l-families/atlas/generalized/segre-hadamard-source/invariant_base_replay.py --check
python -B -m unittest discover -s tests -p test_segre_hadamard_invariant_base.py
python -B -O -m unittest discover -s tests -p test_segre_hadamard_invariant_base.py
```
