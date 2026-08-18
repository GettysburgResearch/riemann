# ZMCSCBI interface correction and exact surviving producer

## Verdict

The unconstrained feature/contraction schema in `T-98600` is circular: it is
finite-dimensionally equivalent to the desired statewise signs. It must not be
used as an RH producer.

## Exact advances

- `R-98610` proves the equivalence with the target signs.
- `L-98610` derives the exact prime update for the Tao completion and proves its
  reserve is parity-neutral.
- `L-98611` eliminates parity into the exact two-prime resolvent.
- `R-98611` proves local two-level current positivity is false even when the
  completed deficit is positive.

## Remaining source-faithful theorem

Construct an explicit nonnegative barrier

\[
B\le g^+ +R^2B
\]

from the finite source/quotient data, without using the unknown completed
solution. Equivalently, prove a root-owned signed Stieltjes or Type-II
factorization. This is still open and RH-bearing.

```text
RH established: false
```
