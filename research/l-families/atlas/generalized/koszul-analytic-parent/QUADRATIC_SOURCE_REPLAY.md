# Quadratic signed-source and diagonal-infinity replay

The [proof](QUADRATIC_SIGNED_SOURCE_BOUNDARY.md) proves the signed
grading-boundary theorem for a geometrically disjoint quadratic cover,
with explicit faithful-input and positive anti-cohomology-rank
hypotheses. The actual S4 specialization has a genus-forty-nine joint
cover and rank-sixty anti-invariant source.

At infinity its twisted inertia is diagonal. The std and tw stalks
have dimension two even when their first trace is zero; the next
Frobenius power detects the missing factor 1-T^2. The fixed twist
has an entire completed determinant, distinct from the untwisted
principal-pole object.

The replay authenticates the separate geometric packet and recounts
only degrees one and two here, with maximum field size 49. Its p5
panel reuses the complete degree-ten reconstruction and held-out
sixth extension. The p7 panels retain only four independent tw traces;
they are explicitly rejected by full-determinant and higher-trace
operations. No unavailable polynomial is completed by guesswork.

From this directory:

```text
python -B quadratic_source_boundary_replay.py --write
python -B quadratic_source_boundary_replay.py --check
python -B -O quadratic_source_boundary_replay.py --check
python -B -m unittest discover -s tests -p test_quadratic_source_boundary.py
python -B -O -m unittest discover -s tests -p test_quadratic_source_boundary.py
```

Dependencies are authenticated before imports. The fixture binds all
four new files and requires complete recomputation. The serialized
producer, ordinary and optimized fixture checks, focused Ruff checks
and all 25 tests in each Python mode passed. The independent exact-SHA
review is pending. The infinite signed
nonzero-trace argument and primitive-root density are proved, not
inferred from the finite controls.
