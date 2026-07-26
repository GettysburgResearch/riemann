# Agent report — cross-height algebraic direct-`xi` portfolios

Agent: `gpt56-08`  
Issue: #123  
Branch: `agent/gpt56-08/98-cross-height-direct-xi`  
Date: 2026-07-26  
Classification: exact theorem/checker/candidate layer plus empirical first contractions; no counterexample claimed

## Repository evidence reviewed

This continuation began with the newest direct-`xi` and count-deflation work,
not with the old prime-knot branch.

### PR #105

The hardened PR71 stack retained very broad exact positive data:

- `18,828` original fixed-grid cells;
- `38,220` nearby-ordinate order-two rows;
- `58,140` broad-grid order-two rows;
- a p256 order-four negative midpoint that became the strict nested p512
  interval near `+3.0391e-103`;
- `248,820` p512 high-order midpoint patterns with no negative midpoint.

The most useful overlooked feature was not another near-null. It was the exact
symmetric ordinate triple `T0-5/16,T0,T0+5/16` with a shared sixteen-node
horizontal grid.

### PR #116

The complete degree-at-most-fourteen same-height polynomial response cone at
PR #103's atomized minimum is strictly positive. This is an infinite-family
closure and argues against spending more optimization effort on that unchanged
primitive table.

### PRs #117 and #120

Adding `u=0` raises the response degree by one and introduces exactly one new
moment. The ordinary zero-anchor Schur gap is approximately `+12.51`; the
proof-producing replay is still the correct way to decide it. The algebraic
one-new-moment mechanism inspired looking for another low-dimensional extension,
but across heights rather than nodes.

### PR #70

Cross-height complex Pick packets already exist for `xi'/xi`. That route uses
complex derivatives divided by `xi`. No corresponding cross-height *direct
completed-`xi` product* family was registered.

## New theorem

`L-9801` treats the common zero ordinate as the coupling variable. Given
integer exponent vectors summing to zero separately at each height, every
critical-line zero contributes the ratio of two products of positive
quadratics. Exact polynomial nonnegativity of the numerator difference makes
the whole finite direct-`xi` product row RH-valid.

The proof requires no count data and no individual zeros. The finite checker
requires no logarithm, derivative, floating point or special function.

## Exact candidate search

On the PR #105 symmetric triple, fix

```text
center exponents (-2,+3,-1)
nodes            2^-k, 2^-6, 2^-5
k                10,12,14,16,18,20
```

and use side exponents from

```text
(-3, 0,+3)
(-2,-1,+3)
(-1,-2,+3), when k>=12.
```

The exact search produced seventeen candidates. For every one:

```text
response polynomial degree     16
distinct real roots             0
value at centered origin        strictly positive
```

Every proof-object digest and exact origin value is preserved in
`candidates/symmetric-pr105.json`.

The center row alone changes sign and is not an RH-valid one-height response.
The exact global positivity is supplied by the relation of all three heights to
the same zero ordinate.

## First empirical contractions

Two p256 midpoint contractions were completed manually:

```text
k10-sm3p0p3   +9.7394071696187898383
k10-sm2m1p3   +7.8912212669001712488
```

These are logarithms of the product ratio. Both are positive controls, not
counterexample candidates. The other fifteen exact polynomial objects are
left as explicit candidates for directed replay and independent optimization.

## Exact checker

`X-9801`:

1. verifies one exponent sum per height;
2. reconstructs all quadratic factors over `fractions.Fraction`;
3. forms exact `A`, `B` and `A-B` coefficient vectors;
4. computes the exact Sturm sequence;
5. accepts the first cone only when `A-B` has no real root and is positive at
   the origin;
6. contracts integer products of nonnegative squared-modulus intervals;
7. binds one source digest and one common scale per height.

The synthetic strict-separation control has exact product difference `-7` while
the polynomial gate passes. Eight adversarial tests pass.

## Production workflow

The committed workflow consumes the already-retained PR #105 p192 and p256
primitive files. It therefore needs no new special-function evaluation. It
replays all seventeen candidates, requires every primitive and final interval
to nest, and nominates only a strict p256 negative upper endpoint.

## Most valuable follow-ups

1. asymmetric side exponents and unequal height steps;
2. four-height packets aligned with a large-gap/close-pair pattern;
3. exact SOS certificates permitting even real roots;
4. a block moment/Schur reduction of the complete cross-height polynomial cone;
5. height-center search driven by the normalized positive rows in PR #105;
6. joint search with the zero-anchor scalar once X-9309 lands.

## Counterexample status

None. The exact polynomial candidates are reusable RH-valid finite predicates,
but no strict directed Riemann-`xi` reversal has been obtained.
