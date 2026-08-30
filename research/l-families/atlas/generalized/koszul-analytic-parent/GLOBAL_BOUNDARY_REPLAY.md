# Global duality and grading-boundary replay

The [proof](GLOBAL_DUALITY_AND_GRADING_BOUNDARY.md) preserves the actual
finite-cutoff functional equation and its two divergent source exponents.
It also gives a precise Hilbert-scale duality, while explaining why an
infinite-dimensional compact operator cannot retain a bounded perfect
pure-weight pairing on the same space.

Its strongest analytic conclusion is a meromorphic natural boundary
|z|=1 for each fixed real 0<T<1/Q. The leading radial constant at a root
of unity comes from the actual genus-three S3 Galois-closure counts.
The two infinity points over a quadratic extension supply strict
positivity for every root order, without assuming every small count is
positive. The theorem concerns the grading variable and the stated real
T region only.

The replay checks the exact finite functional equations and both
source exponent formulas. It reconstructs higher closure traces from
the authenticated cohomological source, checking degrees one and two
against complete primitive counts; it does not claim new independent
point counts in every higher degree. Positive boundary constants are
enclosed with a proved tail. Radial probes at roots of orders 1,2,3 use
exact Q(omega) arithmetic and a separate proved complex tail bound.
Only after exact evaluation are coordinate intervals rounded outward
for compact output; no approximate roots or logarithms are used.

From this directory:

```text
python -B global_boundary_replay.py --write
python -B global_boundary_replay.py --check
python -B -O global_boundary_replay.py --check
python -B -m unittest discover -s tests -p test_global_boundary.py
python -B -O -m unittest discover -s tests -p test_global_boundary.py
```

The executable dependency is authenticated before import. The fixture
binds all four new source files and requires full recomputation.
The serialized replay, ordinary and optimized fixture checks, and all
20 tests in each Python mode passed; focused Ruff checks also passed.
The independent exact-SHA review is pending. The finite
root list does not purport to prove density, compactness, or the
all-root meromorphic natural-boundary theorem.
