# Regularized Frobenius tower: exact replay

This implements the preregistered finite controls for
`REGULARIZED_FROBENIUS_TOWER.md`. The proof is root-authored; the replay
was independently implemented by the extension-order lane. Neither the
all-grade analytic radii nor the determinant-line construction is inferred
from the finite output.

The producer authenticates the actual F7 completion source, its proof, and
the frozen AFTER and BEFORE proofs before importing the one frozen source
module. It compares its PBW characters with the restricted odd-divisor
multiplicities through grade 64. Frobenius traces are reconstructed from
the recurrence of `1+7T^2` and separately checked on powers of the fixed
integer matrix `[[0,-7],[1,0]]`. That algebraic matrix basis is not called
the orthonormal eigenbasis used for the operator norm in the proof.

For extensions e=1 through 8 and regularization orders p=1 through 8,
the finite canonical product retains each proper Frobenius determinant
and multiplies it by the exact exponential counterterm. An independent
formal-log recurrence gives its coefficients through degree 64 with
generator cutoff 16. A formal logarithm here is normalized at zero;
the replay never declares it a zero-free logarithm on an entire analytic
disk containing finite-head zeros.

Cyclic norms of degrees 2, 3, and 4 are checked with a roots-of-unity
coefficient sieve applied to the **Frobenius power**, not the total grading
degree. The left side uses the actual powered matrix and the specified
grading substitution. The right regularization order changes to dp.
For e=1,p=2,d=2 the false unchanged-order formula already fails at degree
8: the correct side has coefficient zero and the false side has 28.
The p=1 example would conceal that error because its odd traces vanish.

Finite transition identities are checked by multiplication, without division
at zeros. The coefficient-limit control uses p=8 through degree 28, where
the regularized scalar is one. The proof, not that finite check, supplies
the all-p coefficientwise limit and the obstruction to preserving the
native source frame. Ordinary operator ideals, continued scalar functions,
and line-valued sections remain separate.

Validation status: proof audit and bounded implementation are complete;
root execution and an independent code/frozen-SHA review are pending.
No computation was run by the authoring subagent. Root-only commands:

```text
python -m ruff format research/l-families/atlas/generalized/graded-completion-lab/regularized_replay.py tests/test_graded_completion_regularized.py
python -m ruff check research/l-families/atlas/generalized/graded-completion-lab/regularized_replay.py tests/test_graded_completion_regularized.py
python research/l-families/atlas/generalized/graded-completion-lab/regularized_replay.py --write
python research/l-families/atlas/generalized/graded-completion-lab/regularized_replay.py --check
python -O research/l-families/atlas/generalized/graded-completion-lab/regularized_replay.py --check
python -m unittest discover -s tests -p test_graded_completion_regularized.py
python -O -m unittest discover -s tests -p test_graded_completion_regularized.py
```

The worker uses sparse-degree rational series, no eigenvalue-list expansion,
no field sweep, and no matrix larger than two by two. Owned files and all
frozen sources are bound into the artifact. Type-sensitive canonical JSON
rejects Boolean/integer/float aliases, nonfinite values, and container
substitutions.
