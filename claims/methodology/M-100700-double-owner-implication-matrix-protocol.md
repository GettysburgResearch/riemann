# M-100700 — Hostile protocol for the double-owner dual terminal matrix

The packet has one producer and two disjoint terminal estimates. Review them in
this order.

## 1. Producer and weights

1. Reconstruct the native Euler coefficient identity of PR #691.
2. Re-run `L-100700` from the one-prime convex inequality.
3. Check that
   
   \[
   w_empty+sum_i w_(i,i)+sum_(i<j)w_(i,j)=1.
   \]
4. Do not confuse the coefficient identity with the Hilbert inequality.

## 2. Route A

1. Keep the endpoint owners outside every completion.
2. Apply `(I+rU)` only to interior primes and before physical collapse.
3. Expand the completion into explicit divisor restrictions.
4. Apply positive divisor renewal only after the divisor sign is exposed.
5. Reject any use of a positive scalar inverse.
6. The theorem to prove is the one-sided logarithmic bound `LRNM100704`.

## 3. Route B

1. Use the ordinary-Mobius minimal wavelet, not an auxiliary normalization.
2. Verify `K_0(1)=0` and the continuous definition of `J_0`.
3. Remove the `k=0` root before estimating the moment tower.
4. Apply `L-100700` to the complete direct-sum observation.
5. Keep all within-block distinct-core cross terms.
6. The theorem to prove is `SCME100704`; a diagonal-only replay is not enough.

## 4. Composition

The exact scalar split is

```text
G_mu = G_short + G_long.
```

The only admissible gluing is

```text
(G_mu)_- <= |G_short| + (G_long)_-.
```

No positive source, score, capacity, or root term may be spent in both routes.

## 5. Immediate falsifiers

Reject a proposed completion if it:

- estimates the root-containing Hardy square rather than the centered tower;
- uses `p^(-3/2)` after the physical conjugation where the activity is
  critical;
- desquares after scalar collapse;
- counts one endpoint-collar term in both regions;
- replaces the long-block divisor sign by unsigned mass;
- claims pairwise positivity implies all-prime positivity;
- claims that RH-equivalence makes a target unusable rather than checking its
  independent incoming arrows.
