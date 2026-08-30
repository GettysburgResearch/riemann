# Local natural-boundary replay

[The proof](LOCAL_NATURAL_BOUNDARY.md) concerns one local Segre source
with rational scalar F. It does not form a prime-indexed Euler product.
Prime indices in this replay are only exponents of the local variable.

The replay checks the exact rational residues of the continued primitive
and regularized logarithmic derivatives. It distinguishes vanished
coefficients from nonintegral branch exponents and includes the universal
first exponent 1/p. A finite index list does not prove that primes are
unbounded or that their lifted roots accumulate densely; the proof does.
Its mixed-rank extension excludes only finitely many prime grids through
an exact possible-collision argument. That analytic extension is not
claimed as a finite computational census.

Three independent critical-constant comparisons use source ranks `(2,5)`,
`(2,9)`, and `(2,5)` at regularization orders 2, 3, and 4. Their critical
points i/2, -1/2, and (1+i)/2 are exact Gaussian rationals. The primitive
caps explicitly permit q=8 and source rank nine. The same constants are
enclosed from source-grade logarithms and from the Adams formula, with
proved infinite error bounds. Both use exact rational/Gaussian arithmetic.

The harmonic correction is H_N/p, and the cutoff normalization is N^(1/p).
No extra p factor is hidden in the chosen local factor 1+qt^p. Finite
controls enclose log G_p(tau); the Euler-constant factor in the limit is
part of the proved theorem, not a floating-point fit.

From this directory:

```text
python -B local_boundary_replay.py --write
python -B local_boundary_replay.py --check
python -B -O local_boundary_replay.py --check
python -B -m unittest discover -s tests -p test_local_boundary.py
python -B -O -m unittest discover -s tests -p test_local_boundary.py
```

The prior executable and proof are authenticated before import, and the
dependency chain preserves earlier frozen sources. The fixture binds all
four new files and requires complete recomputation. The serialized run
passed focused Ruff checks, producer write and both check modes, and all
17 tests in both normal and optimized Python. The independent exact-SHA
review follows the source freeze. No state expansion or external CAS is
used.
