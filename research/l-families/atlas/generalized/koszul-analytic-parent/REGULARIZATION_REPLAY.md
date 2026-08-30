# Exact replay for the mixed-rank and regularization extension

This companion preserves the seven files frozen at
`4c04db224fedde5d589f05f7183e004a67441a9c`.
[The new proof](MIXED_RANKS_AND_REGULARIZATION.md) covers every finite
positive rank list; the replay covers the explicitly named small profiles.

Two independent exact constructions check each identity Hilbert numerator:
finite differences of the native symmetric-power dimensions and the
source differential recurrence. The first-coefficient witness distinguishes
the finite `(2,2)` exception from exponential parent growth. No finite
sample is used to prove the asymptotic or infinite classification.

For regularization orders 2, 3, 4, and 6, the equivariant logarithm is
computed both from the actual frozen quadratic-dual Lie modules through
grade three and from the Adams formula applied to native symmetric-power
characters. Coverage ends at degree `3p`, so no unconstructed higher Lie
grade is smuggled into these controls. Repeated inputs and a held-out
Gaussian unitary input are included.

The rational log enclosures at `t=3/5,p=2`, `t=-1/2,p=2`, and
`t=3/4,p=3` lie beyond the ordinary trace-class disk. They use proved
infinite tail bounds, not approximate transcendental functions. The
second point has scalar F=0 while the regularized determinant is nonzero
by the operator theorem. The intervals verify consistency of two exact
formulas; they are not an empirical proof of analytic continuation.

From this directory:

```text
python -B regularization_replay.py --write
python -B regularization_replay.py --check
python -B -O regularization_replay.py --check
python -B -m unittest discover -s tests -p test_regularization.py
python -B -O -m unittest discover -s tests -p test_regularization.py
```

The executable precursor is authenticated against its compiled Git blob
and content hash before import. The all-rank precursor proof is also
authenticated. The companion fixture binds its own proof, explanation,
producer, and tests and must equal a complete recomputation. All arithmetic
is integral, rational, or Gaussian rational; no builds or CAS are used.
Root's serialized cycle passed Ruff, producer write/check, optimized check,
and all 19 companion tests in both normal and optimized Python. Independent
proof/code review is in progress; its exact-SHA report follows the freeze.
