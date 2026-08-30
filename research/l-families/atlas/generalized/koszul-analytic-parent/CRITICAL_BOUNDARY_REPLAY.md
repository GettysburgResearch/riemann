# Critical-boundary replay contract

[The proof](CRITICAL_GRADE_BOUNDARY.md) gives all-rank critical singular
value asymptotics, the exact block oscillation, and identity/scalar-phase
ordered boundary recovery. This finite replay does not infer any of those
infinite statements from sampled values.

All singular multiplicities remain compressed. The `(2,5)` grade-24
example has over ten billion singular values, but the replay stores only
24 multiplicities and exact partial sums. There is no large state-space
allocation. The Lorentz endpoint constants and log-log partial sums are
enclosed using rational arithmetic.

Logarithms use a range-reduced atanh series with an explicit geometric
tail and outward rounding to a rational grid. No ordinary floating-point
logarithm is labeled certified. The negative-boundary controls compare
`log D_N(-rho)+H_N` with the native derivative `log(rho F'(-rho))` using
the proved infinite error bound. The complex boundary controls compare
actual finite Gaussian-rational products with the exact scalar value and
the Dirichlet-plus-exponential-tail enclosure. The exceptional zero is
rejected by the arc checker and handled by its separate rate theorem.

From this directory:

```text
python -B critical_boundary_replay.py --write
python -B critical_boundary_replay.py --check
python -B -O critical_boundary_replay.py --check
python -B -m unittest discover -s tests -p test_critical_boundary.py
python -B -O -m unittest discover -s tests -p test_critical_boundary.py
```

The second companion's producer and theorem are authenticated against
compiled frozen Git blobs before import. Its predecessor chain authenticates
the first source packet and the original all-rank interlacing theorem.
This fixture also binds all four new proof/explanation/producer/test files.
Acceptance requires full recomputation, not internal JSON consistency.
Root's serialized run passed Ruff, producer write/check, optimized check,
and all 16 critical-boundary tests in both normal and optimized Python.
The independent reviewer read the proof, bounds, producer, and tests with
no blocker. The exact-SHA report follows the final freeze.
