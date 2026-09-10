# Balanced hyperbola: the long scalar from a shorter, fully bound source

**RH and the full-source gain remain unproved.** These are proposed component
proofs and bounded checks, requiring independent mathematical and code review.

This continues PR #805 at `ea66cd5b152e7960ad51ea51b154734eebc9b96a` without
changing any predecessor. Start with [PROOF.md](PROOF.md), sections 1--4,
then the conditional implication and its exact stopping point in sections 5--7.
See [SOURCES.md](SOURCES.md) for the classical hyperbola literature and the
conditional analytic imports. No novelty or priority is asserted.

## What the attempt establishes

For the previous packet's exact terminal-balanced coefficients lambda_(k,Y),
define the rational kernel W(z)=sum_(odd r<=z)(z/r-1). The exact identity is

```
Q(Y^2) = 2 Q(Y) + B_Y,
B_Y = sum_(a,b<=Y odd) lambda_(a,Y)lambda_(b,Y) W(Y^2/(ab)).
```

Only Mobius values through Y are inputs to B_Y. This is a shortened primitive
input range, NOT a square-root analytic saving or an O(Y) algorithm.

The source balance annihilates the ENTIRE logarithmic main term. With
R(z)=W(z)-(z/2)(log z+gamma+log2-1), the same B_Y uses R in place of W,
and |R(z)|<3/(8z). The continuum kernel R(1/(uv)) has operator norm <=1/8.
The finite arithmetic matrix, however, has an O(Y), not O(1), norm bound.
We give explicit bounded balanced sources with quadratic-size forms of both
signs. Even adding first-cell normalization leaves these obstructions.

A source-complete all-order Dirichlet-Newton identity computes Q(Y^d) from
this same finite lambda and ordinary divisor-count kernels. The apparent
coefficient identity FAILS at n=Y^d, but its smoothed endpoint contribution
is exactly zero. Every s=1 pole main term is annihilated before estimates.
No convergence as d grows is asserted.

The remaining arithmetic bound is

```
|B_(2j^2+1)| = O_epsilon((2j^2+1)^(1+epsilon)) for every epsilon>0.
```

The proof supplies its complete implication to RH and, using the classical
RH-to-Mertens implication explicitly, the converse. This bound is NOT proved.
On all odd Y, critical-line zero existence already forces limsup growth
exponent at least 1 for |B_Y|. A bounded or sublinear all-Y target is therefore
false, even if RH holds. The near-linear target must not be replaced by what
a small finite numerical panel happens to suggest.

## Reproduce the bounded arithmetic

From this packet directory, with the unchanged sibling parent PROOF.md present:

```bash
python scripts/replay.py
python -O scripts/replay.py
python scripts/test_replay.py
python -O scripts/test_replay.py
```

The checker uses only Python integers and fractions. It reconstructs primitive
Mobius values, the rational kernels, both quadratic identities, the higher
hierarchy and its boundary error, and the sign obstructions. It does not
approximate zeta, gamma, eigenvalues or an infinite Gram tail. Its finite
checks do not prove an analytic bound at unbounded cutoffs.
