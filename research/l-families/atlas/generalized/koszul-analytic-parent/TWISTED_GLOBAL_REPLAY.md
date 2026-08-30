# Actual ramified twisted completion replay

The [proof](RAMIFIED_TWISTED_GLOBAL_COMPLETION.md) constructs R_n tensor
chi_u after forming the source. Its genus-two sign-twist curve and
rank-four Prym source give an entire global cohomological determinant.
The actual genus-nine regular-source double cover supplies signed
point-count differences. Their integrality, invertible Frobenius
recurrence and weight bound prove a grading natural boundary for every
fixed real 0<T<1/Q, even when all odd differences vanish.

The replay uses complete fields of sizes 5,25,125,7,49,343 only.
Two extension counts and proved reciprocal duality reconstruct the
rank-four polynomials; degree three is held out. It tests all finite
stalk sectors, ramification, a grade-two chi-versus-chi-squared
falsifier, and two independently bounded determinant constructions.
No sampled sign pattern substitutes for the infinite boundary proof.

From this directory:

```text
python -B twisted_global_replay.py --write
python -B twisted_global_replay.py --check
python -B -O twisted_global_replay.py --check
python -B -m unittest discover -s tests -p test_twisted_global.py
python -B -O -m unittest discover -s tests -p test_twisted_global.py
```

The executable dependency is authenticated before import. The fixture
binds all four new files and requires complete recomputation. The
serialized producer, ordinary and optimized fixture checks, focused
Ruff checks and all 24 tests in each Python mode passed. The independent
exact-SHA review is pending.
