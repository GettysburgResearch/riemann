# Global cohomological completion replay

The [proof](GLOBAL_COHOMOLOGICAL_COMPLETION.md) constructs a new global
Hilbert operator from the actual finite-grade S3 sheaf cohomologies.
Its R_n multiplicity spaces have polynomial growth; it is explicitly
different from the preceding exponential homotopy-Lie parent. Complex
realization and finite norm choices are stated rather than suppressed.

The determinant has a genuine initial arithmetic Euler product, with
the compulsory closed-degree factor z^(n deg(v)), and a meromorphic
continuation in the whole T-plane for every |z|<1. It has stacked zero
circles and an explicit obstruction to a usual fixed-z functional
equation with a finite rational prefactor. No arithmetic RH claim or
interchange of sheaf cohomology with Hilbert completion is made.

The replay authenticates and reuses the frozen primitive geometric
source on fields of orders 5,25,7,49. It reconstructs P_E,P_D from
complete degree-one point counts and the proved determinant Q, then
checks extension degree two as a held-out prediction. Complete fibre
histograms and infinity sectors independently verify the all-grade
cohomological trace and catch the incorrect unpowered grading weight.

Two certified computations then enclose the same log determinant:
finite source grades, and finite cohomological Frobenius powers. Both
have explicit infinite-tail bounds. The test points include T=1/2,
z=1/10 over Q=5 and 7, beyond the initial arithmetic Euler disk.
The grade-zero zeta factor is recorded separately with its actual sign;
only the positive-grade factor is passed to a real logarithm.

From this directory:

```text
python -B global_cohomology_replay.py --write
python -B global_cohomology_replay.py --check
python -B -O global_cohomology_replay.py --check
python -B -m unittest discover -s tests -p test_global_cohomology.py
python -B -O -m unittest discover -s tests -p test_global_cohomology.py
```

The executable dependencies are authenticated before import. The fixture
binds all four new source files and requires complete recomputation.
The serialized run passed focused Ruff checks, producer write and both
check modes, and all 20 tests in normal and optimized Python. The
independent exact-SHA review follows the source freeze. The replay does
not perform a field sweep, expand an infinite state space, or claim that
finite divisor lists prove the analytic asymptotics.
