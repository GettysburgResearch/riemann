# T-4601 — Proposed finite Robin region through `10^100`

Claim ID: T-4601  
Title: A mixed powered canonical certificate excludes Robin counterexamples through `10^100`  
Status: PROPOSED  
Authoring agent: `gpt56-03-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-2001; T-2002; L-3502; L-4601; X-4601  
Scope: every integer `n` with `5041<=n<=10^100`  
Related counterexample candidates: none

## Statement

Let

\[
 B=10^{100}.
\]

Assume the proposed structural dependencies T-2001 and T-2002 in their stated
normalizations, and assume the exact shared-budget envelope L-3502 and replay
lemma L-4601.

The X-4601 production terminal stream has been generated and replayed with exact
integers, exact rational abundancy and powered-envelope comparisons, and
outward fixed-denominator dyadic enclosures. It covers all consecutive-prime,
nonincreasing positive exponent vectors under `B` and has the following replayed
counts:

```text
canonical support maximum       53
internal nodes              236209
separate-cap prunes          180109
powered shared-budget prunes    444
satisfied leaves                326
below-domain leaves              43
unresolved leaves                 0
violation leaves                  0
```

The powered-prune dual usage is

```text
(a,d)=(1,128): 437
(a,d)=(1, 96):   5
(a,d)=(1, 64):   2
```

The controlling strict terminal is support `43` with prefix

```text
[8, 8, 5, 4, 3]
```

and the outward global normalized-quotient upper bound is

```text
0.999999970290790912669514849764
```

Consequently, subject to the named proposed dependencies, every integer

\[
 5041\le n\le10^{100}
\]

satisfies Robin's strict inequality

\[
 \sigma(n)<e^\gamma n\log\log n.
\]

In particular, no Robin finite witness against RH occurs in this exact finite
region.

## Definitions

A **canonical image** of an integer is the consecutive-prime,
nonincreasing-exponent integer supplied by T-2002. It is no larger than the
original integer and has abundancy at least as large.

The **normalized Robin quotient** is

\[
 \mathcal R(n)=
 \frac{\sigma(n)}{e^\gamma n\log\log n}.
\]

The displayed bound is an outward rational/dyadic upper endpoint, not a rounded
midpoint.

## Motivation

PR #34 produced a proof-carrying canonical certificate through `10^54`. PR #40
proved an exact shared-budget tail envelope but did not integrate it into the
complete production traversal. X-4601 composes those pieces and extends the
finite all-integer checkpoint by forty-six decimal orders of magnitude.

This remains a finite negative-search result. Its purpose is to remove a very
large exact region from the Robin route while improving the reusable
proof-producing search architecture.

## Proof

We divide the integer range into three cases.

### Case 1: `5041<=n<=5582`

T-2001's independently reproduced finite barrier gives

\[
 \frac{\sigma(n)}n\le\frac{224}{65}
 <e^\gamma\log\log 5041
 \le e^\gamma\log\log n.
\]

Thus Robin's inequality holds throughout the initial finite window.

### Case 2: `5583<=n<=B` and the canonical image is at most `5040`

Let `h` be the canonical image supplied by T-2002. Then

\[
 h\le n,
 \qquad
 \frac{\sigma(n)}n\le\frac{\sigma(h)}h.
\]

If `h<=5040`, T-2001 gives

\[
 \frac{\sigma(h)}h\le\frac{403}{105}
 <e^\gamma\log\log 5583
 \le e^\gamma\log\log n.
\]

Therefore Robin's inequality again holds.

### Case 3: `5583<=n<=B` and the canonical image exceeds `5040`

Now `5041<=h<=n<=B`. By L-4601 and the exactly replayed X-4601 terminal stream,
every canonical integer in this region is covered by a strict separate prune, a
strict powered prune, or a strict leaf. Hence

\[
 \frac{\sigma(h)}h<e^\gamma\log\log h.
\]

More quantitatively, X-4601 gives

\[
 \frac{\sigma(h)}{e^\gamma h\log\log h}
 \le C,
 \qquad
 C<1,
\]

where the outward endpoint `C` is the number displayed in the statement.
Using the canonical dominance and `h<=n`,

\[
 \frac{\sigma(n)}n
 \le\frac{\sigma(h)}h
 < e^\gamma\log\log h
 \le e^\gamma\log\log n.
\]

The three cases cover every integer from `5041` through `B`, proving the
statement. ∎

## Analytic domain audit

Only the real natural logarithm occurs, at integers greater than one. The
transcendental comparisons are outward dyadic enclosures built from proved real
series and remainders. No complex branch, contour, zeta evaluation, or zero sum
is used in the finite arithmetic computation.

## Dependency audit

- T-2001 supplies the exact two finite barriers at `5041` and `5583`.
- T-2002 supplies canonical dominance for arbitrary integers.
- L-3502 supplies the exact powered shared-budget ceiling.
- L-4601 turns the mixed terminal stream into complete finite canonical
  coverage.
- X-4601 supplies the exact terminal stream and replayed arithmetic.
- Robin's published equivalence theorem is required only to interpret a future
  violation as an RH counterexample; it is not needed to prove the finite
  inequality asserted here.

## Gap audit

- Every named dependency remains at its repository status; this theorem is not
  promoted merely because the finite computation replays.
- Search and replay were authored by the same agent and share `certmath.py`.
  They give independent traversal implementations, not independent numerical
  backends.
- The compressed certificate and manifest must match the source hashes and
  exact parameters recorded by X-4601.
- No inference is made for `n>10^100`.
- A finite negative search is not evidence for RH as a universal statement.

## Adversarial tests

1. Independently reconstruct the three-case all-integer transfer.
2. Recompute the exact support maximum and every child boundary.
3. Replay the mixed stream with a separately written implementation.
4. Recompute every powered recurrence with exact rational arithmetic.
5. Replace the dyadic backend by Arb or MPFI and require containment of the
   production signs.
6. Mutate the controlling terminal, dual pair, or global bound and require
   rejection.

## Remaining uncertainty

The exact Python search and replay agree and the production arithmetic is
outward rounded, but independent mathematical and implementation review is
still pending. The imported Robin criterion itself has not been reconstructed
in this branch.

## Suggested next attack

Reproduce X-4601 with a second backend and language. In parallel, use the same
mixed-terminal architecture to test a larger endpoint only after establishing
a compact sharding and independent-verifier policy for multi-megabyte
certificates.
