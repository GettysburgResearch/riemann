# M-9503 — All-moments program for the critical totient energy

Claim ID: `M-9503`  
Title: Replace the uniform RH estimate by a hierarchy of positive multilinear moment bounds  
Status: `PROPOSED RESEARCH PROGRAM`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9512`, `T-9504`, `T-9505`, `R-9503`  
Scope: full-problem attack  
Related counterexample candidates: none

## Exact target

For every fixed integer `k>=1`, prove

\[
\boxed{
\int_X^{2X}|E^{\rm AN}(t)|^{2k}dt
\ll_{k,\varepsilon}X^{k+1+\varepsilon}.}
\tag{M-9503.1}
\]

An unbounded sequence of passing `k` proves RH by `T-9505`. At finite `k`, the
same theorem gives the explicit pointwise exponent

\[
\frac12+\frac1{4k+2}.
\tag{M-9503.2}
\]

Thus every completed rung is a genuine zero-free-half-plane improvement, not
merely numerical evidence.

## Fractional-part form

Use

\[
E^{\rm AN}(x)
=\frac12\left(1+\sum_{d>=1}\mu(d)\{x/d\}^2\right)
\tag{M-9503.3}
\]

or the equivalent finite-plus-tail form from `L-9512`. Dyadically partition the
denominator variable and retain the tail exactly before applying any norm.

On each block, expand the periodic Bernoulli components into rational
frequencies

\[
e(hx/d),
\qquad h\ne0.
\tag{M-9503.4}
\]

The `2k`-th moment becomes a finite multilinear Farey-frequency sum. Its phase
is

\[
\sum_{j=1}^{2k}\varepsilon_j{h_j\over d_j},
\qquad\varepsilon_j\in\{+1,-1\}.
\tag{M-9503.5}
\]

The proof must separate:

1. exact resonances, where the rational frequency in (M-9503.5) is zero;
2. near resonances at spacing `O(1/X)`;
3. genuinely separated tuples, controlled by integration by parts or a Farey
   large sieve.

## Load-bearing arithmetic cancellation

A phase-blind large sieve at denominator scale `X` costs `X^2` and is one full
power too large. The required gain must come from the Möbius coefficients and
the exact endpoint coupling among the two Bernoulli channels and two Mertens
tails.

The proof-facing objects are therefore:

\[
\sum_{d_1,...,d_{2k}}
\mu(d_1)\cdots\mu(d_{2k})
\,\mathcal K_{k,X}(d_1,...,d_{2k}),
\tag{M-9503.6}
\]

where `mathcal K` is the positive integrated rational-frequency kernel obtained
before taking absolute values.

Priority subtargets:

1. derive an exact gcd/lcm expression for the resonant part;
2. prove a Möbius-weighted large-sieve inequality for the near-resonant part;
3. retain the tail `d>X` as one analytic block rather than truncating it
   coefficientwise;
4. identify a Selberg-square or Ramanujan-sum factorization of the complete
   kernel;
5. export each fixed-`k` contraction to exact rational arithmetic whenever the
   frequency partition is finite.

## Connection to local Möbius moments

A July 2026 preprint of Alberto Verjovsky proves that RH is equivalent to
subpolynomial growth of arbitrarily high local moments of normalized Möbius
Fourier polynomials on arcs of radius `c/N`.

Its moment-to-point-value loss is

\[
\frac1{2(q+1)}.
\]

Taking `q=2k` gives exactly

\[
\frac1{4k+2},
\]

the loss in (M-9503.2). The two programs are therefore quantitatively aligned:

- Verjovsky localizes the Möbius Fourier polynomial near its distinguished
  value `M(N)`;
- `T-9505` localizes the analytic totient error in the physical scale variable;
- both require unbounded moment order to reach the critical line.

The preprint explicitly presents its result as an equivalent reformulation,
not a proof of RH. The present program seeks a transfer or multilinear estimate
special to the extra Green smoothing in `E^AN`.

Primary source: A. Verjovsky, *Local Moments of Möbius Fourier Polynomials and
the Riemann Hypothesis*, arXiv:2607.25002.

## Fail-closed milestones

For each fixed `k`, a proof packet must state:

1. the exact finite/tail decomposition of `E^AN`;
2. all rational-frequency cells and coverage semantics;
3. the resonant and nonresonant partitions;
4. the directed multilinear estimate;
5. the final exponent in (M-9503.1);
6. the resulting zero-free half-plane through `T-9505`.

A finite numerical moment table, random-sign heuristic, or coefficientwise
absolute bound is not a theorem milestone.

## Exact blocker

The smallest unresolved statement is the critical multilinear estimate
(M-9503.1) for an unbounded sequence of `k`. Equivalently, one must prove
subpolynomial local moments for a complete Möbius/Farey rational-frequency
packet after the two-Green smoothing.

This is genuinely RH-bearing. `T-9504` proves that any off-line zero forces the
positive energy exponent to be nonzero, while `T-9505` proves that the complete
moment ladder would force it to vanish.
