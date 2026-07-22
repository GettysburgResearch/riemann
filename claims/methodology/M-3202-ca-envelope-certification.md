# M-3202 — Exact transition-envelope certificates for the Robin route

Claim ID: M-3202  
Title: Turn a colossally-abundant transition ledger into whole-interval Robin coverage  
Status: PROPOSED  
Authoring agent: `gpt56-06`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-3201; L-3203; X-0201; Issue #25  
Scope: proof-producing finite negative regions for Robin's criterion  
Related counterexample candidates: none

## Objective

Implement the complete CA route recorded in T-3201 by upgrading the empirical
X-0201 transition stream so that every accepted
transition record certifies Robin's strict inequality for all integers between
two exact co-maximizing endpoints.

## Producer stages

### 1. Exact event generation

For each relevant prime power, construct a directed interval for

\[
\epsilon_{p,a}=
\frac{\log((1-p^{-a-1})/(1-p^{-a}))}{\log p}.
\]

Use exact primes and exponents. Increase precision until adjacent event
intervals are disjoint. If they remain unresolved, stop coverage at that
boundary; never choose an order from midpoints.

For a finite lower boundary `epsilon_min`, prove that no omitted prime or
higher exponent has transition value at least `epsilon_min`.

### 2. Exact contact states

Maintain the full prime-exponent factorization recipe before and after each
certified event. At the exact event value, independently verify that both
states have equal local objective and that every prime exponent is globally
optimal for the same `epsilon`.

A true equality cluster is processed as one contact: use the states before and
after all equal events. A merely unresolved cluster is not a contact
certificate.

### 3. Endpoint Robin enclosures

For each contact state, compute

\[
A(N)=\prod_{p^a\parallel N}\frac{p^{a+1}-1}{p^a(p-1)}
\]

as an exact rational. Enclose

\[
e^\gamma\log\log N
\]

with directed balls from the factorization's exact `log N`. Require a strict
endpoint margin.

### 4. Interval certificate

Each record contains:

- the exact event `(p,a)` and a disjoint interval for its boundary;
- endpoint factorization recipes or a hash-linked incremental recipe;
- exact rational endpoint abundancies;
- outward endpoint Robin intervals and strict signs;
- the supporting-line slope interval and equality checks;
- the covered closed integer interval `[N_0,N_1]`;
- a parent hash linking consecutive records.

### 5. Independent verification

The checker reconstructs prime validity, factorization updates, event order,
local exponent optimality, endpoint signs, and then applies L-3203. It does not
trust traversal order or producer state.

## Compaction

The endpoint integers can have tens of millions of digits. Certificates should
store factorizations and incremental event hashes rather than materialized
decimal integers. `log N` is reconstructed as a directed sum of `a log p`, and
integer ordering follows from the event sequence and multiplication by a
prime.

## Relationship to Issue #25

This method provides very broad interval certificates along the exposed
upper hull. Issue #25's canonical branch-and-bound remains valuable for:

- independent validation on small ranges;
- intervals blocked by unresolved event ordering;
- searches near a suspicious contact state;
- any proposed witness not represented by the exact contact ledger.

The two certificate formats should share exact factorization and Robin endpoint
records but retain independent traversal/checking code.

## Falsification audit

- A binary64 event order invalidates global contact claims.
- A state that is merely superabundant, rather than a global
  `A(n)n^{-epsilon}` maximizer at the same `epsilon`, is insufficient.
- Endpoint satisfaction alone does not cover an interval without the global
  support-line inequality.
- Concavity must be applied to
  `B(x)=gamma+log log x` with `x=log n`; using `gamma+log x` is the wrong
  barrier.
- A finite ledger certifies only the explicitly hash-linked range.

## First experiment

Rebuild the first 30 classical CA contacts with 256-bit balls. For every
contact interval above 5040, compare L-3203 coverage with brute-force exact
Robin checks. Then increase the prime cutoff while recording the first event
whose ordering or endpoint sign remains unresolved.
