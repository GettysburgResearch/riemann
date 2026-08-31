# Bounded completion replay

Run from the repository root, sequentially, under the research session's RAM gate:

```text
python research/l-families/atlas/generalized/graded-completion-lab/replay.py --write
python research/l-families/atlas/generalized/graded-completion-lab/replay.py --check
python -O research/l-families/atlas/generalized/graded-completion-lab/replay.py --check
python -m unittest discover -s tests -p test_graded_completion_ladder.py
python -O -m unittest discover -s tests -p test_graded_completion_ladder.py
```

Arithmetic is integer or exact rational. Rational logarithm bounds use the positive
atanh series and an explicit tail, rounded outward to dyadics. These are finite
intervals, not fitted asymptotic exponents. Source grades are capped at64 in the
artifact; the standalone odd-divisor helper permits128. Polynomial degree is64,
coefficient bit size4096, input JSON4MB. No field above F7 is enumerated.

The checker authenticates the exact frozen source commit/path/blob and compares
the working source bytes. It reconstructs source characters independently and
compares the prior authenticated character artifact. It also binds this packet's
proof, producer and tests. It does not rerun the entire predecessor validation
chain or prove the imported arithmetic geometry. New infinite analytic results
require proof review of MATHEMATICS.md; finite replay is not their proof.

The ordinary and optimized modes must both fail on malformed or altered data.
No validation is implemented only as a Python assert. Generation is not authority
to change a frozen dependency or to accept a mismatched artifact.
