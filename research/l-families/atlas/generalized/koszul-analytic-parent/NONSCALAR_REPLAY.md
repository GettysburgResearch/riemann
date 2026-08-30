# Nonscalar source replay

[The proof](NONSCALAR_GRADE_RADIUS.md) treats all unitary first-zero
circles below the second-regularization boundary, then constructs an
explicit involution family. This replay uses native symmetric-power
coefficients for ranks `(2,3)`, `(2,4)`, and `(2,5)` through degree 64.

The equivariant PBW/Adams formula yields each involution character and
its actual plus/minus eigenspace multiplicities. Those multiplicities
must be nonnegative integers. Degrees 1--3 are checked independently
against the frozen quadratic-dual Lie quotient. The producer never
constructs an exponentially large eigenvalue list or raises a rational
number to an exponentially large source multiplicity.

At rank `(2,3)` and t=i/sqrt(3), paired odd grades make all block
determinants positive rational expressions using t^2=-1/3. Their logarithms
are enclosed by an exact rational log1p series, with rounding after
multiplicity weighting. The corrected finite sum uses H_floor(N/2),
which is essential to the factor two in the limit 27 exp(-gamma)/32.
The source regular part is 27/64. Proved Cauchy and block-tail estimates
bound the discrepancy; odd and even cutoffs are separately checked.

A real held-out point t=11/20 lies beyond trace class but before the
nonscalar grade radius. Its finite source log is compared with the exact
scalar value using the proved remainder estimate, not a fitted tolerance.

From this directory:

```text
python -B nonscalar_replay.py --write
python -B nonscalar_replay.py --check
python -B -O nonscalar_replay.py --check
python -B -m unittest discover -s tests -p test_nonscalar.py
python -B -O -m unittest discover -s tests -p test_nonscalar.py
```

The third companion's executable and proof are authenticated before
import, and its dependency chain binds earlier source freezes. This
fixture binds its own four proof/explanation/producer/test files and
requires complete recomputation. Root's serialized run passed Ruff,
producer write/check, optimized check, and all 16 tests in both normal
and optimized Python. Independent proof/code review found no blocker;
the exact-SHA report follows the freeze. The proof, not the finite fixture, establishes the limiting
constants, the all-k inequalities, and general-unitary boundary recovery.
