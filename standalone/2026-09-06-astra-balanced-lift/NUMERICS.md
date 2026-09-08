# Numerical contract: rational source, full infinite Gram, bounded indices

This file defines the scope of the checker. No unbounded source-norm estimate,
Mertens saving, all-scale block gain, or RH statement is tested by finite runs.

## Primitive source

The input is the exact dictionary `h_k(n)=(n mod k)/k` with weights
`1/[n(n+1)]`, not stored Gram entries, target zeros, or fitted coefficients.
Mobius values are produced by trial division and checked by the divisor identity.
Euler phi is independently counted by gcd, and Jordan J2 is reconstructed from
Mobius inversion and checked by its divisor sum. The balanced coefficients are
rational expressions in these primitives, independently checked by solving the
full constrained rational linear system. Both affine constraints are exact.

For every algebraic fixture the step source is independently computed in two
ways: its fractional-part coefficients and its cumulative odd-divisor formula.
Every cell through 128 is checked, including the n=0 and n=1 endpoints. The exact
ordinary Mobius comparison is a finite divisor identity, not a sampled PNT.

The algebra-M list is `[3,4,5,8,9,16,24,32]`. The coherent counterexamples use
K in `[2,4,8,16]`; their source support is at most 64. The arithmetic API has a
hard cap 128. Counts are executed controls, not a claim of distinct theorems or
statistically independent samples. Some finite identities are rechecked for
several M values.

## Full norm and infinite summation tails

For a finite coefficient vector c, the full norm is `sum c_j c_k G_jk`, where

```
G_jk = sum_(n>=1) ((n mod j)/j)((n mod k)/k)/[n(n+1)].
```

Let q=lcm(j,k). Absolute convergence and periodicity yield exactly

```
G_jk = (1/q) sum_(r=1..q-1) ((r mod j)/j)((r mod k)/k)
                     [psi((r+1)/q)-psi(r/q)].
```

The unchanged parent numerical proof derives this identity for arbitrary
positive j,k and the digamma remainder for every x>0. The parent replay's cap
of 16 is NOT silently changed. The new packet implements the same general
formula in its own `gram` function, with strict cap 32; at M=16 the actual
source consumes indices through 30 (odd k through 15 and their doubles).
All 120 original Gram entries through 16 are cross-checked against the unchanged
parent implementation. This overlap check tests consistency, not independence
of the shared remainder proof.

Two parent modules are authenticated by literal SHA-256 before their source
bytes are compiled directly. Bytecode caches are not loaded for either one.
The positive-real digamma function is shifted by 128 and evaluated by
Euler--Maclaurin through Bernoulli degree 32. Its rational remainder bound is

```
|R_16(y)| <= A_32/(32 y^32),
A_32 = sum_(j=0..32) binom(32,j)|B_j|,  y=x+128.
```

The exact recurrence subtracts `sum_(j=0..127)1/(x+j)`. Logarithms use a
90-term atanh series after dyadic range reduction, with the complete geometric
remainder. Pi uses the parent's alternating rational arctangent enclosure.
Every operation rounds outward on the dyadic grid of denominator 2^224. These
are the unchanged algorithms in the authenticated parent `intervals.py`;
its full analytic justification is the separately pinned parent NUMERICS.md.
The residue count increases in this pass, but x remains positive and the same
remainder bound applies; no unexplained large-index asymptotic is introduced.

For each M=4,8,16:

- `E_M` is evaluated from ALL pairs of finite source coefficients using the
  infinite Gram; no cross terms are omitted.
- The target pairing is evaluated both from `sum c_k log(k)/k` and the
  independent removable Mellin value `-sum lambda_k log(k)/(2k)`.
- The full squared error is `1-2<chi,F_M>+E_M`.
- The detail error is `pi^2 D/(16K)-1/2`.
- A rational 512-cell source sum and the elementary tail
  `(sum |lambda_k|)^2/[4(513)]` independently bracket the full norm coarsely.
  This coarse check is NOT responsible for the tight reported intervals.

The explicit narrow energy and target intervals must strictly contain the
entire computed dyadic enclosures. The stored decimal bounds are display-only
rational renderings; comparisons use exact integer endpoints. The result
retains those endpoints and their denominator bits.

## Acceptance and corruption tests

The normal CLI authenticates five parent files, validates a fixed source-lock
schema, checks a nonempty exact nine-file SHA inventory, reconstructs all data,
and requires exact canonical-JSON equality with the retained result. Duplicate
JSON keys, floating JSON numbers, NaN/Infinity, malformed or empty inventories,
unknown payload files, and symbolic input paths are refused. The new inventory
uses POSIX paths, including on Windows in principle; no Windows run is claimed.

All resource-input functions reject bool/float aliases and out-of-range indices.
Their memoization is explicitly type-sensitive so a previously cached integer
cannot bypass the strict input check through a numerically equal float/bool.
Scientific acceptance uses explicit exceptions, never removable `assert`.

`--write` is an explicit producer mode: it authenticates its primitive dependencies
and rebuilds output, but intentionally does not require a preexisting result
manifest. Only `--check` is the packaged acceptance command. A self-consistent
forged source and completely changed checker is not independently authenticated
by a local hash file; the frozen Git/source review remains part of the trust
boundary. The code and analytic remainders still require independent review.
