# Integration handoff — prime-only continuation of Issue #215

## Add

```text
T-21502  prime-only Hardy-energy exponent
L-21504  off-diagonal prime Gram as balanced squarefree-semiprime forcing
O-21502  prime-square layer cancellation and prime-only reconnaissance
X-21503  deterministic layer/event sweep
```

## Canonical global criterion

The cleanest current full-problem statement is

\[
 \mathrm{RH}
 \iff
 \int^X\left|
  \sum_p{\log p\over\sqrt p}
  H(x-\log p)
 \right|^2dx
 =\exp(o(X)),
\]

where

\[
 H(u)=G(u)-G(u-1)
\]

and `G` is the explicit triangular pole-safe window of `L-21501`.

The criterion uses ordinary primes only. Möbius inversion proves that the extra
difference cancels the sole boundary pole introduced by deleting prime squares
and higher powers, without canceling a shifted off-critical zero.

## Final arithmetic interface

The positive exponential exponent is carried by

\[
 \mathcal O_H^{\mathbb P}(X)
 =\sum_{n=pq,\,p<q}
  {\Lambda_2(n)\over\sqrt n}
  K_X^H(\log p,\log q).
\]

The support forces `p/q` into one fixed compact range. Integration should treat
this as a balanced Type-II semiprime form, not as an arbitrary prime-pair
matrix.

## Merge/integration guidance

- Keep `T-21501` as the all-prime-power global theorem.
- Promote `T-21502` as the sharper canonical arithmetic interface after review.
- Keep `O-21501/O-21502` strictly empirical.
- Do not infer a global bound from the finite `10^7` block table.
- Cross-route identities to PRs #202/#208 remain conditional on independent
  review of those transfer theorems.

## SERIOUS RESOLUTION PATH

```text
prime-only safe signal
-> exact Hardy exponent
-> balanced squarefree-semiprime forcing
-> signed Type-II subexponential estimate
-> RH
```

Exact missing theorem:

\[
 [\mathcal O_H^{\mathbb P}(X)]_+=\exp(o(X)).
\]

No full proof is claimed.
