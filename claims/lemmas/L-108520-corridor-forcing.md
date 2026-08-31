# L-108520 — Corridor forcing: an induced 2x15 ladder breaches both Ramanujan ends (window finiteness)

```text
Claim ID: L-108520
Status:   PROVED (complete elementary proof below: Dirichlet ladder
          modes + Courant-Fischer; the threshold constant is settled
          by the exact integer inequality 50 > 49). Machine layer:
          consistency spot-checks against the exact family data
          (phase_diagram.json, head_cap_atlas.json).
Created:  2026-08-31 (pass 3 continuation, Lane 3; converts the
          "every cap ends BOTH-END" pattern of the cap-window table
          into a theorem)
Programme: #763 (graph purity mechanisms)
Depends on: none (self-contained linear algebra)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement

Let `G` be any cubic graph containing an INDUCED `2 x k` ladder
(two rail paths `u_1..u_k`, `v_1..v_k` with rungs `u_j v_j`, no other
edges among these `2k` vertices). Then

```text
lambda_2(G)   >= 1 + 2 cos(2 pi/(k+1)),
lambda_min(G) <= -1 - 2 cos(pi/(k+1)).
```

In particular, for `k >= 15` both ends breach temperedness:
`lambda_2 > 2 sqrt 2` and `lambda_min < -2 sqrt 2` — the graph is
both-end non-Ramanujan. CONSEQUENCE (window finiteness): in every
capped-ladder family (arbitrary fixed caps joined by a growing rung
corridor) the Ramanujan and positive-only regimes are FINITE — every
family ends in the both-end phase, as the cap-window tables observed;
positive-only can only ever be a transitional window there, in exact
contrast to the lambda_min-bounded permanent regime of GP(n,2)
(T-108514).

## Proof

The standalone `2 x k` ladder is the Cartesian product `P_k x K_2`;
its adjacency eigenvectors are products of path and edge modes.
Explicitly, for `l = 1, .., k` let `phi^l_j = sin(pi l j/(k+1))` (the
exact eigenvectors of the path `P_k`, eigenvalue
`2 cos(pi l/(k+1))`), and define on the ladder

```text
x^{l,+}: u_j -> phi^l_j,  v_j -> phi^l_j      (symmetric),
x^{l,-}: u_j -> phi^l_j,  v_j -> -phi^l_j     (antisymmetric).
```

Then `A_ladder x^{l,+-} = (2 cos(pi l/(k+1)) +- 1) x^{l,+-}` (rail
edges give the path eigenvalue; the rung adds `+1` or `-1`).

Embed these in `G` by extending by zero. Because the ladder is
INDUCED, for any vector `x` supported on it,
`x^T A_G x = x^T A_ladder x` (edges leaving the support hit a zero
coordinate), and the Rayleigh quotients are unchanged.

1. (`lambda_2`) Take `V = span(x^{1,+}, x^{2,+})`. These are
   eigenvectors of the same symmetric operator `A_ladder` with
   distinct eigenvalues, so they are orthogonal AND A-orthogonal;
   hence for every nonzero `x in V` the quotient is a convex
   combination of the two eigenvalues, giving
   `min_{x in V} R(x) = 1 + 2 cos(2 pi/(k+1))`. By Courant-Fischer
   (`lambda_2 = max_{dim V = 2} min_{x in V} R(x)`),
   `lambda_2(G) >= 1 + 2 cos(2 pi/(k+1))`.
2. (`lambda_min`) Take the antisymmetric top path mode `l = k`
   (`phi^k_j = sin(pi k j/(k+1))`, path eigenvalue
   `2 cos(pi k/(k+1)) = -2 cos(pi/(k+1))`):
   `R(x^{k,-}) = -2 cos(pi/(k+1)) - 1`, so
   `lambda_min(G) <= -1 - 2 cos(pi/(k+1))`.

Threshold: at `k = 15`, `2 pi/(k+1) = pi/8` and
`1 + 2 cos(pi/8) = 1 + sqrt(2 + sqrt 2)`. Now

```text
1 + sqrt(2 + sqrt 2) > 2 sqrt 2
  <=> sqrt(2 + sqrt 2) > 2 sqrt 2 - 1
  <=> 2 + sqrt 2 > 9 - 4 sqrt 2
  <=> 5 sqrt 2 > 7   <=>   50 > 49 .
```

For the negative end, `cos(pi/16) > cos(pi/8)` gives
`1 + 2 cos(pi/16) > 1 + 2 cos(pi/8) > 2 sqrt 2` by the same integer
inequality. Monotonicity in `k` extends both to all `k >= 15`. ∎

## Remarks

- The constant 15 is not optimized: the exact family data
  (phase_diagram.json; head_cap_atlas.json) shows both-end entry at
  corridor lengths 5-6 already. The content is FINITENESS with an
  explicit, fully proved ceiling: no capped-ladder family can stay
  positive-only past corridor length 14.
- Contrapositive mechanism reading: an infinite family that stays
  positive-end-only forever (T-108514's GP(n,2)) can contain no
  arbitrarily long induced ladders — its lambda_min-boundedness and
  its ladder-freeness are the same geometry seen twice.
- The proof uses only that the corridor is PRESENT and induced;
  heads, caps, and the rest of the graph are arbitrary, so this
  applies verbatim to every family in the cap-window tables and to
  any future corridor construction.
```
