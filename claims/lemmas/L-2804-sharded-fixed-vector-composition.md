# L-2804 — Sharded fixed-vector composition for piecewise carriers

Claim ID: L-2804  
Title: Exact composition of complete-prime shard intervals and the carrier correction moat  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; L-0901; L-2803  
Scope: fixed dyadic vectors and finite complete-prime certificates  
Related counterexample candidates: any future D-0801 fixed-vector witness

## Statement

Fix a decimal-power cutoff `c=10^n`, carrier `T>0`, and `K`-cell D-0801
family. Let

\[
 x=(x_0,\ldots,x_{K-1})\in(\mathbb Q(i))^K
\]

be a nonzero dyadic complex vector and put

\[
 N=x^*x>0.
\]

Let

\[
 \alpha(T)=\frac{\log(T/(2\pi))}{2\pi}
\]

and let the complete prime Toeplitz matrix be decomposed into a finite disjoint
sum

\[
 S_K(T,c)=\sum_{r=1}^m S_r.
\]

Assume exact rational intervals satisfy

\[
 \alpha(T)\in A=[a_-,a_+],
\]

and

\[
 x^*S_rx\in P_r=[p_{r,-},p_{r,+}]
 \qquad(1\le r\le m).
\]

Define the interval sums

\[
 P=\sum_{r=1}^mP_r
\]

and

\[
 Q_{\rm lead}=NA-P.
\]

Let `E` be any rigorous normalized operator correction radius satisfying

\[
 \|E_{\rm arch}+E_{\rm pole}\|_{\rm op}\le E.
\]

Then the exact full normalized fixed-vector value obeys

\[
 \boxed{
 x^*\widetilde Q_{\rm exact}x
 \in Q_{\rm lead}+[-EN,EN].}
\]

Consequently:

- if the upper endpoint is strictly negative, the supplied analytic intervals
  prove a negative exact D-0801 fixed-vector value;
- if the lower endpoint is strictly positive, they prove positivity for this
  fixed vector;
- if the interval meets zero, no sign is certified.

For the optimized PR #44 target, X-2801 recomputes `E` from L-2803 rather than
trusting a user-supplied smaller radius.

## Complete finite coverage contract

A composed certificate is **quantitatively closed** only when its shard metadata
also proves:

1. the declared half-open segment ranges form exactly one contiguous partition
   of `[0,M)` with no gap or overlap;
2. every shard has the same parameter fingerprint;
3. every shard has the same canonical dyadic-vector fingerprint;
4. exactly one shard declares the separate higher-prime-power stream;
5. every shard's declared total equals its prime count plus its higher-power
   count.

These checks prove consistency of the finite shard ledger. They do not by
themselves prove that a producer correctly enumerated every prime inside a
segment or that a reported analytic interval is valid. Those are separate
producer contracts.

## Proof

The complete prime matrix is a finite sum, so

\[
 x^*S_Kx=\sum_{r=1}^m x^*S_rx.
\]

Interval addition therefore gives

\[
 x^*S_Kx\in P.
\]

Because `N` is exact and positive,

\[
 \alpha(T)N\in NA.
\]

Interval subtraction yields

\[
 x^*\left(\alpha(T)I-S_K\right)x
 \in NA-P=Q_{\rm lead}.
\]

The operator-norm hypothesis gives

\[
 \left|x^*(E_{\rm arch}+E_{\rm pole})x\right|
 \le \|E_{\rm arch}+E_{\rm pole}\|_{\rm op}\,x^*x
 \le EN.
\]

Minkowski addition of the two real intervals proves the boxed enclosure. The
three sign conclusions are immediate.

The coverage assertions are finite exact checks on sorted integer endpoints,
boolean stream declarations, integer counts, and cryptographic fingerprints.
They prevent accidental composition of different vectors, parameters, or
incomplete declared segment ranges. They make no claim beyond those exact
ledger semantics.

## Certificate schema

X-2801 implements

```text
riemann.piecewise-carrier-fixed-vector.v1
```

with:

- exact rational `T` and `alpha_interval`;
- one dyadic complex vector;
- SHA-256 fingerprints of canonical vector and parameter JSON;
- one or more shard intervals for `x^*S_r x`;
- contiguous integer segment metadata;
- prime and higher-power counts;
- exact recomputation of the L-2803 correction radius;
- fail-closed positive, negative, or unresolved verdicts.

The checker evaluates no prime, logarithm, trigonometric function, eigenvalue,
or floating-point operation.

## Analytic domain audit

- `x` is a finite nonzero vector over dyadic complex numbers.
- All composed intervals are real rational intervals.
- The leading scalar and prime Rayleigh values require independent analytic
  producers; this lemma only composes their inclusions.
- The correction bound is normalized per unit Euclidean norm and is multiplied
  by the exact `N=x^*x`.

## Dependency audit

- L-0801 supplies the finite complete-prime Toeplitz decomposition.
- L-0901/L-2803 supply the target correction radius.
- D-0801 supplies the exact test family.
- The Guinand--Weil implication remains a separate logical gate.

## Gap audit

1. Contiguous integer segments do not prove correct primality enumeration within
   each segment.
2. SHA-256 equality is an integrity check, not a proof of analytic correctness.
3. The checker trusts the provenance of `alpha_interval` and each shard
   interval.
4. A negative checker verdict is not by itself an RH counterexample until the
   producer contracts, admissibility, normalization, and equivalence direction
   are independently established.
5. A positive fixed-vector verdict says nothing about other vectors or RH.

## Adversarial tests

The committed suite accepts strict synthetic positive and negative fixed-vector
certificates, rejects zero-touching, gaps, overlaps, duplicated or missing
higher-power streams, vector and parameter digest mismatches, term-count
mismatches, zero vectors, and boolean values passed as integer counts.

## Remaining uncertainty

No gap is known in the interval composition. The unresolved work is entirely in
analytic production and the logical gates listed above.

## Suggested next attack

Preserve the PR #44 target vector as dyadic data, then build an Arb producer that
emits one scalar `x^*S_r x` interval per coverage-checked prime segment. Avoid a
full interval eigensolver: discovery chooses the vector, while proof evaluates
that one frozen vector.
