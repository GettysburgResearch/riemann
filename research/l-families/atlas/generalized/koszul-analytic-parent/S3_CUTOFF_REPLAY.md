# Native S3 cutoff-anomaly replay

The [proof](S3_GRADE_CUTOFF_ANOMALY.md) uses the actual S3 action on the
previous canonical Lie parent. Its dimensions remain exponential and
its trace-class threshold remains 1/2. The enlarged disk belongs to
ordered whole-grade products and their trace cancellations.

The exact finite-band formula exposes an anomaly at tau^d=-1/2:
the product limit is d^(-1/d) times the rational source shadow. It also
proves a compact-complex 1/N transition profile and two explicit exterior
ray behaviors. These analytic results are not inferred from finite data.

The replay reconstructs the S3 characters by source Adams inversion,
checks the first three actual quotient Lie grades, and validates all
integer root-of-unity eigenspace multiplicities through grade 256.
No eigenspace is expanded. Exact source determinant blocks are evaluated
using t^d as a rational input, including the boundary and both exterior
ray types. Weighted rational atanh intervals apply the integer
multiplicity before outward rounding; a strict tail target and bounded
iteration cap make failure explicit. The proved Cauchy remainder bounds
compare the corrected whole-grade logarithm with the source shadow.

From this directory:

```text
python -B s3_cutoff_replay.py --write
python -B s3_cutoff_replay.py --check
python -B -O s3_cutoff_replay.py --check
python -B -m unittest discover -s tests -p test_s3_cutoff.py
python -B -O -m unittest discover -s tests -p test_s3_cutoff.py
```

The preceding S3 source runtime is authenticated before import. The
fixture binds all four new source files and requires full recomputation.
The serialized run passed focused Ruff checks, producer write and both
check modes, and all 20 tests in normal and optimized Python. The
independent exact-SHA review follows the source freeze. This packet does
not alter any preceding source freeze or construct an infinite arithmetic
Euler product.
