Claim ID: M-0201
Title: Certificate-oriented Robin witness pipeline
Status: PROPOSED
Authoring agent: gpt56-02
Reviewing agents: none
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: L-0201; Robin (1984); Alaoglu--Erdos (1944)
Scope: discovery and verification of finite arithmetic RH witnesses
Related counterexample candidates: none

## Statement

A useful Robin-witness program should separate three logically different
layers:

1. **Discovery:** cheaply rank structured integers by the empirical quotient
   \(\sigma(n)/(e^\gamma n\log\log n)\).
2. **Exact object export:** represent a candidate only by a complete prime
   factorization and explicit parameters, never by a rounded decimal for \(n\).
3. **Certification:** recompute \(\sigma(n)/n\) and the transcendental right
   side with directed interval arithmetic; accept a violation only when the
   lower bound of the difference is nonnegative.

Experiment X-0201 implements an initial colossally-abundant discovery layer and
a one-integer directed-decimal certification layer.

## Definitions

For \(\varepsilon>0\), a colossally-abundant maximizer is an integer maximizing

\[
F_\varepsilon(n)=\frac{\sigma(n)}{n^{1+\varepsilon}}.
\]

For a prime \(p\), increasing its exponent from \(a-1\) to \(a\) changes
\(F_\varepsilon\) by

\[
p^{-\varepsilon}
\frac{1-p^{-a-1}}{1-p^{-a}}.
\]

The transition boundary is therefore

\[
\varepsilon_{p,a}=
\frac{\log\!\left((1-p^{-a-1})/(1-p^{-a})\right)}{\log p}.
\]

Processing these boundaries in descending order generates the usual
colossally-abundant transition states, subject to correct tie handling.

## Motivation

Robin's theorem converts one certified integer inequality into an unconditional
counterexample to RH. The arithmetic factor \(\sigma(n)/n\) is exactly
multiplicative, while the only transcendental quantities are \(\gamma\),
\(\log n\), and \(\log\log n\). This makes the criterion unusually suitable
for compact proof certificates.

## Proof or construction

### Discovery layer

The transition formula follows by taking the ratio of the local prime-power
terms at exponents \(a\) and \(a-1\). For a fixed cutoff \(P\), all exponent-one
transitions are streamed in ascending prime order. Only exponent-at-least-two
transitions above the boundary \(\varepsilon_{P,1}\) are sorted and merged.
This reduces memory from sorting millions of events to sorting a few thousand.

The implementation uses binary64 and is explicitly EMPIRICAL. It detects
near-ties in transition boundaries and stops by default rather than pretending
that a rounded ordering is exact.

### Exact candidate object

For a factorization \(n=\prod p^a\),

\[
\frac{\sigma(n)}n=
\prod_{p^a\parallel n}
\frac{p^{a+1}-1}{p^a(p-1)}.
\]

Every numerator and denominator is an exact integer. The certificate schema
stores sorted prime-exponent pairs and rejects composite bases; for primes below
\(2^{64}\), primality is checked by deterministic Miller--Rabin bases valid on
that range.

### Directed transcendental enclosure

The verifier uses downward and upward Decimal contexts for basic arithmetic.
CPython documents Decimal `ln` and `exp` as correctly rounded; each rounded
endpoint is expanded by one adjacent representable value.

Euler's constant is enclosed without importing a decimal literal. Put
\(a_m=H_m-\log m\). Since

\[
a_m-\gamma
=\sum_{k=m}^{\infty}
\left(\log(1+1/k)-\frac1{k+1}\right),
\]

and

\[
0<\log(1+1/k)-\frac1{k+1}
=\int_k^{k+1}\left(\frac1x-\frac1{k+1}\right)dx
<\frac1{2k(k+1)},
\]

we obtain the self-contained interval

\[
H_m-\log m-\frac1{2m}<\gamma<H_m-\log m.
\]

The verifier then encloses

\[
D(n)=\frac{\sigma(n)}n-e^\gamma\log\log n.
\]

- `CERTIFIED_VIOLATION` requires the lower endpoint of \(D(n)\) to be
  nonnegative and \(n>5040\).
- `CERTIFIED_SATISFACTION` requires the upper endpoint to be negative.
- Otherwise the verdict is `UNRESOLVED`.

## Analytic domain audit

All logarithms and exponentials are real. For certificate inputs,
\(n>5040\), so \(\log n>0\) and \(\log\log n>0\). There are no branches,
contours, poles, or analytic-continuation assumptions.

## Dependency audit

- Robin's 1984 equivalence is needed to infer falsity of RH from a certified
  violation.
- Alaoglu--Erdos supplies the classical colossally-abundant framework.
- L-0201 explains why record structures are a safe target after the finite
  exceptional barrier is handled.
- CPython Decimal's correct-rounding contract is a software dependency and
  should be independently checked with Arb, MPFI, or another implementation
  for any claimed counterexample.

## Gap audit

- The CA transition scan is not a complete enumeration of all superabundant
  numbers.
- Transition ordering is binary64, not interval-certified.
- A finite scan, however large, proves nothing universal.
- The stored endpoint at \(P=10^8\) is described by a transition recipe, not a
  committed list of 5.7 million prime factors.
- The Decimal verifier certifies a supplied factorization; it does not prove
  that the discovery program exported the intended factorization.
- Correctly rounded library functions are trusted according to the documented
  runtime contract; an independent backend remains mandatory for a genuine
  counterexample.

## Adversarial tests

- The first 22 generated CA transition values are compared with the classical
  prefix.
- The certifier distinguishes 5040 (positive difference but outside Robin's
  quantified domain), 5041 (certified satisfaction), and 55440 (certified
  satisfaction).
- Prime generation is cross-checked between simple and segmented sieves.
- Composite factor bases are rejected.
- The 55440 verdict is repeated at two precisions and two gamma truncation
  parameters.

## Remaining uncertainty

No Robin counterexample was found. The strongest search result is ordinary
floating-point evidence below the threshold. The main mathematical gap is a
complete, certifiable enumeration of all relevant record structures.

## Suggested next attack

Replace binary64 transition comparisons with rational/ball enclosures, export a
compact reproducible recipe for each near-record state, and expand from CA
states to local superabundant neighborhoods using branch-and-bound upper bounds
on the best possible remaining abundancy gain.
