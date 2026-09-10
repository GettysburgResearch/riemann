# Full-norm transfer, not a uniform-gain proof

**Status:** proposed complete component proofs; independent review required.
**RH, the original uniform block gain, and the new subpower target are unproved.**
Author continuation of PR #805, frozen parent
`0f8724bbd86c1de8f40eacbf30129321e0ebc8aa`.

The previous parity relaxation has an exact positive Mobius-square solution,
but its direct coarse lift fails to improve the true optimum at 8 -> 16.
This pass retains that coarse component and proves a bounded, invertible
operator-valued Dirichlet convolution between the explicit full lift and
classical raw Mobius fractional-part sums.

Start with **PROOF.md sections 1--4**, then the fully stated analytic imports
and growth theorem in sections 5--6. Section 7 rules out full-norm convergence of the explicit lift; section 8 distinguishes approximation
of one target from ambient density and from exact finite optimality.
Section 9 proves a classical-scale full-norm bound; section 10 records the attempted completion and its stopping point.

## Component conclusions

* The forward and inverse operator coefficient norms sum to less than 3
  and 8, respectively; all cutoff identities are finite and source-exact.
* The formerly unresolved signed scalar normalization satisfies |A_M| <= 2
  for every M, using only elementary Mobius identities and an absolutely
  convergent positive scalar convolution. The total optimizer coefficient
  sum is exactly (8/pi^2) times the odd Mertens sum.
* Prefix full norms obey H(X) <= 4 + 12 R(X) and
  R(X) <= 20(H(X) + 4). These are not comparisons with the detail norm.
* If Theta is the supremal real part of nontrivial zeta zeros, the explicit
  full lift has exact limsup growth exponent Theta - 1/2. The proof retains
  the zero-free hypothesis in the imported Balazard--Saias estimate.
* Importing the classical quantitative Mertens estimate gives a full-norm
  bound C sqrt(M) exp(-c sqrt(log M)); this is not a power saving and does
  not prove subpower growth.
* The prescribed full lifts do not converge in norm, even if RH is true.
  A direct initial-horizon/critical-zero argument handles the raw source,
  and the bounded inverse transfers the obstruction.
* A fixed subdictionary approximates chi if and only if RH holds and it
  contains every squarefree index >= 2. Nonsquarefree indices can improve
  the finite optimum without being necessary for this target asymptotically.
  The squarefree span is not asserted dense in the full step space.

Thus a different route asks for **subpower full-norm growth** of explicit
unoptimized lifts. It does not ask for norm convergence or a prescribed
per-block rate. That growth bound is equivalent to RH and is not proved.
No novel zero-free region, zero proportion, or full-gain estimate is claimed.
Classical ingredients and the intended limited contribution are credited
in SOURCES.md. The infinite analytic arguments are not machine-verified.

## Bounded replay

From this directory, with the two sibling parent proof files present:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/replay.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/test_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -O scripts/test_replay.py
```

The replay uses the standard library only. It rebuilds Mobius values by
factorization and independently by divisor recursion, exact rational
operator polynomials (including inverse prime powers), cutoff identities,
and finite-support duals. It does not read or execute predecessor Python.
Two parent proofs are authenticated as sources. All new paths use POSIX
manifest separators; no Windows execution is claimed. The predecessor's
reported Windows manifest issue is preserved, not silently repaired.
