# T-97400 integration handoff

Do not integrate PR #565's `1/40` certificate, swapped-current source claim, or
root marginal. Do not integrate PR #566's `L-96651(iv)` from the reserve
injection proof.

Retain:

```text
L-97400  repaired all-real P61 bias 1/42 <= F/M <= 1/8
L-97401  exact critical contraction arithmetic and one-prime scalar positivity
R-97400  x=184 counterexample to 1/40
R-97401  PR565 parent/source type mismatch
R-97402  PR566 reserve/current mismatch
```

The next theorem must be a literal source identity for the actual rough Möbius
root. Its current and children must be disjoint positive subobjects, and its
signed marginal must retain every `-p^{-1/2}` rough coefficient. Once such an
identity supplies child mass `<M/8`, `L-97401` closes positivity with the
repaired `1/42` constant.

RH remains unproved.
