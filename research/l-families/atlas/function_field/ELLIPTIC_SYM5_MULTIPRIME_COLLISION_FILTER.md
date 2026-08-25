# A bounded multi-prime filter for the elliptic Sym5 collision

## Status and scope

This packet is an exact finite compatibility firewall.  It starts from the
source-locked local collision at q=31,

\[
 P_5(-7,31)=P_5(3,31)=5544,
\]

where P5 is the scalar trace of the fifth symmetric power.  It realizes both
trace classes by every good short Weierstrass coefficient model

\[
 y^2=x^3+Ax+B,\qquad -4\le A,B\le4,
\]

and asks whether the scalar collision persists at the declared auxiliary
primes 5, 7, 11, and 17.

This is not an isomorphism-class or bounded-height catalogue.  It does not
classify global spectral twins, motives, isogenies, correspondences, Euler
products, or zeros.  RH and GRH remain open.

## Exact bounded result

The coefficient box contains exactly three good q=31 models with trace -7:

\[
 (-4,4),\quad(-3,-3),\quad(3,1),
\]

and exactly four with trace 3:

\[
 (-1,-1),\quad(2,-4),\quad(3,-2),\quad(4,-2).
\]

Thus there are twelve cross-realizations of the locked scalar collision.
Every one splits at a prime of simultaneous good reduction in the auxiliary
panel.  Ordered by the first separating prime, the exact counts are

| first separator | cross-pairs |
|---:|---:|
| 5 | 4 |
| 7 | 6 |
| 11 | 1 |
| 17 | 1 |

No cross-pair survives the full panel.

This does not say that multiple primes make local equality impossible.
Occasionally two models have the same ordinary trace at an auxiliary prime,
so their Sym5 scalar traces agree there automatically.  The theorem is only
that each of these twelve q=31 collision realizations is separated somewhere
in the declared panel.

## Why this is useful

The q=31 equality is a genuine representation-theoretic scalar alias, but the
locked local factors already differ in their second coefficient.  The new
experiment adds a different firewall: even after choosing integral global
models realizing the two trace classes, the scalar equality does not persist
across a tiny held-out prime panel.

The correct automated-motive workflow is therefore:

1. enforce good reduction and weight/determinant at every prime;
2. demand a multi-prime fingerprint rather than one local scalar;
3. compare complete local factors, not only one symmetric-power trace; and
4. quotient models by a justified global equivalence before counting twins.

The next serious experiment should replace the coefficient box by a small
isomorphism-invariant bounded-height catalogue, reserve held-out primes, and
require complete-factor equality.  The present packet is the regression
control that such a search must pass.

## Provenance and resources

The primitive source is
elliptic_sym5_collision_diophantine_pilot.json at LF-normalized SHA-256
66635391ee4d69382eaf6d11fd78a77c90cffc8919ccbede9d0f568915cdf167.
Both that external file digest and its internal canonical payload hash are
checked before the experiment runs.

The exact replay counts model candidates and individual finite-field point
evaluations.  It refuses before 4,096 source atoms, uses no random sampling,
and performs no zero or broad prime scan.

Replay with:

    python research/l-families/atlas/function_field/elliptic_sym5_multiprime_collision_filter.py --check
    python -O research/l-families/atlas/function_field/elliptic_sym5_multiprime_collision_filter.py --check
    python -m unittest tests.test_elliptic_sym5_multiprime_collision_filter -v
    python -O -m unittest tests.test_elliptic_sym5_multiprime_collision_filter -v
