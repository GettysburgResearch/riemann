# Native Newton compression after NRC32

Status: **proposed unconditional component theorem, awaiting independent
mathematical review. RH and the native coarse-energy recurrence remain
open.**

For each fixed logarithmic mesh enlargement, this packet compresses the
complete reciprocal-Mobius energy on the strict square step
`Y < k < (Y+1)^2` to `O(Y/log^r Y)` exact old-prefix quadratic coordinates.
The complete omitted variance is `O_B(log^-B Y)` for every fixed `B>0`.

The proof combines NRC32's exact coefficient reconstruction and orthogonal
variance identity with a precise maximal Mobius short-interval estimate
from Matomaki--Radziwill--Shao--Tao--Teravainen, arXiv:2411.05770v2,
Theorem 3.1(i). It sums over every interior starting point to retain the
whole exceptional-set contribution. No deterministic-endpoint inference
from an almost-all theorem is made.

## Files

- `PROOF.md`: full statement, complete proof, exact imported input, signed
  quadratic coordinates, and two controls delimiting the conclusion.
- `check_newton.py`: exact finite coefficient/endpoint/energy replay from
  a primitive Mobius prefix, with a separate full-length Mobius sieve.
- `audit.json`: output of the stated finite replay. Decimal energy displays
  are diagnostics; acceptance uses exact integer and rational arithmetic.
- `SOURCES.md`: pinned repository and primary-literature dependencies.

## Reproduce the finite replay

```bash
python3 check_newton.py --output audit.json
```

The replay covers the declared complete finite cases, not an asymptotic
tail. It does not reprove or independently reproduce the imported analytic
theorem. Both producer and checker implementations were authored in this
packet; no independent review is claimed.

The next required statement is an upper bound on the retained coarse
quadratic forms in terms of the previous native energy, with sufficient
saving from the quadratic exponent. The new dimension bound does not
provide such an amplitude bound.
