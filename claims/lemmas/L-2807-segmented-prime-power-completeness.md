# L-2807 — Completeness of the directed producer's finite prime-power stream

Claim ID: L-2807  
Title: The segmented sieve plus one higher-power stream enumerates every `p^m<=c` exactly once  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: the fundamental theorem of arithmetic  
Scope: X-2805 finite source enumeration for integer cutoff `c`  
Related counterexample candidates: any complete D-0801 prime certificate

## Statement

Let `c>=2` be an integer. Partition the half-open integer range

\[
 [2,c+1)
\]

into consecutive half-open segments. In every segment `[A,B)`, X-2805:

1. prepares all base primes `p<=floor(sqrt(B-1))`;
2. marks every integer multiple of such a prime beginning at
   \[
   \max\{p^2,\lceil A/p\rceil p\};
   \]
3. emits every unmarked integer in `[A,B)`.

Separately, in exactly one declared shard, for every prime `p<=sqrt(c)` it emits

\[
 p^2,p^3,\ldots,p^m\le c
\]

by repeated exact integer multiplication.

If the segment ranges form a contiguous nonoverlapping partition of `[2,c+1)`,
then:

- the ordinary stream emits every prime `p<=c` exactly once;
- the separate stream emits every prime power `p^m<=c`, `m>=2`, exactly once;
- the two streams are disjoint;
- together they emit every prime power appearing in the finite von Mangoldt sum
  exactly once.

## Proof

### Base-prime list

The initial Eratosthenes sieve starts with every integer `2<=n<=R` unmarked and,
for every unmarked `p<=sqrt(R)`, marks all multiples beginning at `p^2`. A prime
has no smaller prime divisor and is never marked. A composite `n<=R` has a prime
divisor `p<=sqrt(n)<=sqrt(R)` and is marked when that `p` is processed. Hence
the resulting base list is exactly the primes through `R`.

### One segment

Let `n in [A,B)`.

If `n` is prime, no base prime divides it except `n` itself. When `n<=sqrt(B-1)`,
the marking for `p=n` starts at `n^2>B-1`, so `n` is not marked. Thus every
prime in the segment is emitted.

If `n` is composite, the fundamental theorem of arithmetic supplies a prime
divisor

\[
 p\le\sqrt n\le\sqrt{B-1}.
\]

That prime belongs to the base list. Since `n` is a multiple of `p` and
`n>=p^2`, it lies at or after the declared first marked multiple in the segment.
Therefore it is marked and not emitted. The segment output is exactly the primes
in `[A,B)`.

### Global ordinary stream

A contiguous half-open partition contains every integer in `[2,c+1)` in exactly
one segment. The segment result therefore emits every prime through `c` exactly
once and no composite.

### Higher powers

A prime power with exponent at least two has base prime

\[
 p\le\sqrt{p^m}\le\sqrt c,
\]

so its base occurs in the finite base-prime list. Starting from `p^2` and
repeatedly multiplying by `p` emits every exponent `m>=2` until the next product
would exceed `c`.

For a fixed base `p`, exponents strictly increase, so no value repeats. If
`p^a=q^b` for primes `p,q` and positive exponents, unique factorization implies
`p=q` and `a=b`; different base-prime loops cannot collide. The higher-power
stream is therefore duplicate-free and complete.

Finally, the ordinary stream uses exponent one and the separate stream uses
exponents at least two, so the two streams are disjoint. This proves the claim.

## Overflow audit

The implementation performs repeated multiplication only after checking

```text
current_power <= cutoff / p
```

so the next multiplication cannot overflow an unsigned integer before exceeding
the declared cutoff. The present target `c=10^11` is far below `2^64`.

The first marked multiple and segment endpoint calculations are likewise below
`c+segment_size`, which is explicitly checked against the unsigned range by the
run-plan validator.

## Relationship to the exact checker

L-2807 proves correctness of the enumeration algorithm. L-2804 separately
checks that the declared segment ledger has no gap or overlap and that exactly
one shard contains the higher-power stream. Neither layer alone is enough:
algorithmic correctness plus a complete ledger gives the closed finite source.

For the optimized target, the retained expected totals are

```text
ordinary primes          4,118,054,813
higher prime powers             28,156
total prime-power terms  4,118,082,969
```

A mismatch causes the assembler to fail.

## Gap audit

1. This is a proof of the specified algorithm, not proof that an arbitrary
   compiled binary matches its source.
2. Hardware faults, compiler defects, and memory corruption remain trusted-base
   risks; independent reproduction is required for a counterexample.
3. A correct enumeration does not certify the logarithm, phase, amplitude, or
   accumulated interval; L-2806 handles those operations.
4. The same prime power may contribute zero at the support endpoint; it remains
   part of the complete enumeration ledger.

## Adversarial tests

X-2805 compares the segmented stream with direct small prime lists, checks
partition invariance, rejects gaps and overlaps, requires exactly one
higher-power stream, and verifies the target count identity.

## Remaining uncertainty

No mathematical gap is known in the enumeration proof. Independent source and
compiler review remain necessary before candidate promotion.

## Suggested next attack

After the target run, independently reproduce the global counts with a second
segmented sieve or a trusted prime-counting implementation, then compare random
segment digests and all higher powers exactly.
