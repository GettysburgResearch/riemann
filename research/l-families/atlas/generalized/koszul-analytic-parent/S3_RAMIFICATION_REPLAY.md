# S3 ramification and finite-grade global family replay

The [proof](S3_RAMIFICATION_AND_GRADED_FAMILY.md) places the canonical
(2,3) Segre/Koszul construction on the actual cubic S3 covering already
frozen in the adjacent geometric source packet. The input is the
augmentation representation and the permutation representation, with
their matrices constructed from all six permutations before evaluating
symmetric powers.

This replay checks all three source character series through grade 24,
the three actual low Lie grades, and the full representation-ring
Koszul inverse. It detects both false ramification shortcuts: taking
input invariants before forming the source, and keeping only invariant
Lie grades in its superdeterminant. The correct full invariant tensor
complex retains the missing sectors and has zero positive-degree Euler
characteristic.

For every replayed grade it checks irreducible multiplicities, all
inertia dimensions, the conductor/cohomology ledger, and the exponents
in the finite-sheaf identity

    L(j_*R_n,T)=Z(P^1,T)^a_n P_D(T)^b_n P_E(T)^c_n.

The local Euler factors are checked against traces of Frobenius powers,
including both infinity cosets over fields of sizes 5,7,25,49,125.
These field-size controls specify residual action; they are not point
counts. The distinct arithmetic Frobenius sign for Q=2 mod3 is retained.
Only bounded integer and rational arithmetic is used, with no state
expansion and no infinite product over arithmetic places.

From this directory:

```text
python -B s3_ramification_replay.py --write
python -B s3_ramification_replay.py --check
python -B -O s3_ramification_replay.py --check
python -B -m unittest discover -s tests -p test_s3_ramification.py
python -B -O -m unittest discover -s tests -p test_s3_ramification.py
```

The analytic runtime is authenticated before import. Both the analytic
and geometric proof freezes are resolved to their exact Git blobs and
LF-normalized hashes; changed working copies are rejected. The generated
fixture binds the four new source files and requires full recomputation.
The serialized run passed focused Ruff checks, producer write and both
check modes, and all 24 tests in normal and optimized Python. The
exact-SHA independent review follows the source freeze.

The all-grade sheaf theorem, canonical complex exactness, trace formula,
and Weil weights are mathematical inputs or proved consequences in the
note, not claims of the finite replay.
