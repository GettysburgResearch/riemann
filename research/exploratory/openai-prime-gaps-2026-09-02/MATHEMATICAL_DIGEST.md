# Mathematical digest

```text
Status: SOURCE-PINNED ANALYSIS / REVIEW_PENDING
Scope: conditional bounded gaps; unconditional long gaps; common sieve infrastructure
RH status: unproved
```

## 1. Executive comparison

The imports attack opposite tails of the consecutive-prime gap distribution.

| Package | Endpoint | Main mechanism | Nonstandard theorem assumptions |
|---|---|---|---|
| `PrimeGaps186` | `liminf (p_(n+1)-p_n) <= 186` | multidimensional sieve, trace-function cancellation, certified trial weights, compact admissible tuple | two Kloosterman estimates and one 152-clause physical-integral package |
| `LongGapsBetweenPrimes` | `G(X) >= c log X (log_2 X)^2 log_4 X/(log_3 X)^2` eventually | Erdos-Rankin residue covering plus a random-sieve short-translates theorem | none beyond the ordinary Lean/mathlib trust boundary reported upstream |

Here `log_j` denotes the `j`-fold iterated logarithm, and `G(X)` denotes the largest relevant consecutive-prime gap below `X` in the upstream formulation.

The packages share a subject but not a decisive analytic input. The bounded-gap proof forces two primes into one short translate of an admissible tuple. The long-gap proof forces every integer in one long interval to have a small or medium prime divisor. One is a concentration theorem for primes; the other is a covering theorem for composites.

## 2. `PrimeGaps186`

### 2.1 Exact exported endpoint

The principal declaration is

```lean
PrimeGap186.primeGapLiminf_le_186
```

with mathematical content

\[
\liminf_{n\to\infty}(p_{n+1}-p_n)\le 186.
\]

In the completed module this conclusion is conditional on exactly three project-level assumptions. The ordinary logical axioms reported by Lean are separate and should not be conflated with those mathematical inputs.

### 2.2 Proof architecture

The proof decomposes cleanly as

```text
K3: normalized rank-3 Kloosterman bound
K2C: rank-2 Kloosterman correlation bound
PHY: exact physical-integral inequalities for a fixed trial function
                         |
                         v
                weighted sieve positivity
                         |
                         v
                     DHL[40,2]
                         |
                         v
 explicit admissible 40-tuple H, max(H)-min(H)=186
                         |
                         v
 infinitely many n for which at least two n+h, h in H, are prime
                         |
                         v
 infinitely many consecutive-prime gaps <=186
                         |
                         v
                  primeGapLiminf <=186.
```

The intermediate declarations advertised upstream are:

```lean
PrimeGap186.dhl_40_2
PrimeGap186.infinite_two_prime_translates_admissibleTuple
PrimeGap186.primeGapLiminf_le_186
```

The finite tuple begins

```text
0, 2, 6, 12, 20, 26, 30, 32, 36, 42, 48, 50, ...
```

and has forty shifts spanning 186. The important reusable theorem is not the hard-coded tuple but the abstract implication

\[
\mathrm{DHL}[k,2]+\text{an admissible }k\text{-tuple of diameter }D
\Longrightarrow \liminf (p_{n+1}-p_n)\le D.
\]

That implication should be extracted as a stable API before further numerical optimization.

### 2.3 The three unresolved theorem inputs

#### K3: `PrimeGap186.kloosterman3_bound`

The source defines a rank-three hyper-Kloosterman-type sum over `ZMod p`, normalized by `1/p`, and assumes norm at most `3` for nonzero parameter. This is a Weil/Deligne-type finite-field estimate. The exact normalization, the treatment of `p=2`, and the translation from any classical source theorem to this `ZMod` definition require line-by-line review.

#### K2C: `PrimeGap186.kloosterman2_correlation_bound`

The source assumes a two-trace correlation estimate of size

\[
8p\sqrt p
\]

for a sum over `t`, with the singular values `t=0,-1` removed and with nonzero parameters `A,B`. This is structurally deeper than a pointwise Weil bound: a proof must identify the underlying sheaves or an equivalent finite-field cohomological statement, classify exceptional/degenerate parameter configurations, and recover the exact constant and normalization.

#### PHY: `PrimeGap186.physical_integral_bounds`

This is a conjunction of 104 outer bounds, 45 inner bounds, and 3 scalar caps: 152 concrete inequalities tied to a fixed trial function, mesh, exact integer tables, and rounding conventions. The upstream Python/FLINT program recomputes these inequalities, but no generated proof object is consumed by Lean. Thus `PHY` is mathematically much more accessible than K3 or K2C, yet still theorem-bearing in the current formal boundary.

### 2.4 Where the number 186 comes from

There are two logically distinct optimization layers:

1. **analytic/sieve layer:** prove `DHL[k,2]` for some `k`;
2. **combinatorial geometry layer:** find an admissible `k`-tuple with the smallest possible diameter.

For the imported endpoint, `k=40` and the chosen diameter is 186. A smaller final constant can arise by either route:

- retain `DHL[40,2]` and find a diameter `<186` admissible 40-tuple;
- prove `DHL[k,2]` for a smaller `k`, then use a tighter admissible tuple;
- improve the trial-function optimization enough to cross the threshold for a better `(k,D)` pair;
- strengthen the distribution/correlation input and rebuild the sieve threshold.

These routes should not be mixed in one generated file. The tuple search, the analytic theorem, and the numerical certificate should have independent interfaces and review records.

### 2.5 What is genuinely reusable

The reusable mathematical components are:

- abstract admissible-tuple and diameter lemmas;
- the bridge from two-prime translates to consecutive gaps and an `EReal` liminf;
- finite-field additive-character and Kloosterman definitions;
- a parameterized multidimensional sieve theorem whose numerical input is a record rather than a global axiom;
- exact interval-certificate schemas for high-dimensional trial functions.

The 10 MB generated Lean file is evidence that the theorem has been instantiated, but it is not the right long-term library boundary.

## 3. `LongGapsBetweenPrimes`

### 3.1 Exact exported endpoint

The principal completed declaration is

```lean
LongGapsBetweenPrimes.long_gap_theorem
```

which packages the existence of a constant `c>0` such that, for all sufficiently large `X`, there are consecutive primes `p<q<=X` with

\[
q-p\ge c\,\log X\,
\frac{(\log\log X)^2\log\log\log\log X}
     {(\log\log\log X)^2}.
\]

The package defines an eventual predicate `LongGapTheorem`, an iterated-log scale `gapScale`, and a concrete preceding statement `long_prime_gaps` before deriving the final asymptotic form.

### 3.2 Proof architecture

The completed source implements the following Erdos-Rankin strategy.

```text
choose a large sieve parameter x
        |
        v
small primes <=z choose residue classes and cover most of [1,y]
        |
        v
uncovered sparse set S
        |
        v
short-translates/random-sieve theorem chooses additional residue data
        |
        v
medium/large primes cover every remaining element of [1,y]
        |
        v
one full congruence cover modulo a primorial
        |
        v
Chinese-remainder translation produces y consecutive composite integers
        |
        v
neighboring primes p<q are consecutive and q-p>=y
        |
        v
parameter conversion x=(log X)/8 gives the stated gap scale.
```

The important named interfaces include:

```lean
ShortTranslates
short_translates_with_sieveDelta
short_translates
small_primes_residue_choice
prime_gap_from_full_cover
long_prime_gaps
long_gap_theorem
```

The source proves concentration and tail estimates for an abstract random sieve, obtains a positive-probability translate, and then instantiates the deterministic covering argument.

### 3.3 Constant flow

The proof exposes several losses that are invisible in `\gg` notation:

- the parameter conversion uses an upper location of the form `exp(8*x)`;
- the full-cover statement yields a gap with a factor resembling `coverEta/16`;
- the final `X`-scale theorem uses a constant resembling `coverEta/128`.

These constants should be represented as named fields in a parameter record. That would permit optimization without replaying the entire asymptotic proof and would make it clear which losses are structural and which are bookkeeping.

### 3.4 What is genuinely reusable

The strongest reusable components are:

- a generic short-translates theorem for sparse sets;
- a random-sieve moment and concentration library;
- a small-prime residue-selection theorem;
- a full-cover-to-consecutive-prime-gap theorem;
- iterated-log asymptotic comparison lemmas;
- residue and primorial APIs robust enough to prevent off-by-one and zero-residue mistakes.

This source is compact enough to refactor into theorem-oriented modules without preserving its current single-file layout.

## 4. Common formal library suggested by both imports

The shared layer should be deliberately elementary:

```text
PrimeGaps/Definitions.lean
  ConsecutivePrimes, gap sequence, liminf gap, maximal gap below X

PrimeGaps/Admissible.lean
  admissible tuples, diameter, translate counting, compact tuple certificates

PrimeGaps/Covers.lean
  residue covers, primorial moduli, CRT translations, composite intervals

PrimeGaps/Asymptotics.lean
  iterated logarithms, eventual positivity, scale comparison

PrimeGaps/Certificates.lean
  exact finite tuples, residue assignments, interval enclosures
```

The bounded-gap analytic sieve and the long-gap random cover should sit above this layer in separate namespaces.

## 5. Mathematical significance and boundary

These are substantial formal analytic-number-theory artifacts:

- the long-gap package appears to carry a complete, axiom-light implementation of a sophisticated asymptotic covering proof;
- the bounded-gap package exposes a sharp conditional theorem in enough detail that its numerical and deep finite-field inputs can be attacked separately.

But their conjunction says only that the prime gap sequence has infinitely many small values and, at a different scale and along different subsequences, very large values. That is compatible with many possible zero distributions for zeta. RH governs a global signed error term or an equivalent positivity/completeness statement; extremal support geometry alone does not supply that sign information.

The honest use of these imports in the Riemann project is therefore:

1. as formal endpoint tests for any future prime-distribution theorem;
2. as reusable sieve and arithmetic infrastructure;
3. as a source of exact finite-field cancellation problems;
4. as a firewall against claiming that impressive gap phenomena have already crossed the RH gate.
