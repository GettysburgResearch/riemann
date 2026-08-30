# Finite-group and S4 source boundary replay

The [proof](FINITE_GROUP_SOURCE_BOUNDARY.md) derives the global grading
boundary directly from complete inertia coset averages. Nonidentity
elements that act as scalars on both inputs contribute additional
positive resonances; an actual ramified C2 cover detects their omission.
The actual S4 standard/permutation source has only one full-order
class, producing the coefficient 5/12 times its genus-nineteen closure
point-count series. Its native finite duality exponents grow as
N^6/96 and N^7/112.

The new replay reconstructs symmetric powers from permutation cycle
lengths, checks every finite ramification sector and graded cohomology
dimension, and tests finite-source functional equations. It authenticates
the earlier S4 polynomial reconstruction and recounts only degrees one
and two here, with maximum field size 49. The frozen higher-extension
data are reused transparently, not described as newly recounted.
Exact radial and limiting constants have separate proved tails.

From this directory:

```text
python -B finite_group_boundary_replay.py --write
python -B finite_group_boundary_replay.py --check
python -B -O finite_group_boundary_replay.py --check
python -B -m unittest discover -s tests -p test_finite_group_boundary.py
python -B -O -m unittest discover -s tests -p test_finite_group_boundary.py
```

Dependencies are authenticated before imports. The fixture binds all
four new files and requires complete recomputation. The serialized
producer, ordinary and optimized checks, focused Ruff checks and all
24 tests in each Python mode passed. The independent exact-SHA review
is pending. The general theorem
and root-density argument are proved, not inferred from finite probes.
