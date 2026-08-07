# M-24501 — Fail-closed review protocol for the carry-resolvent proposal

Claim ID: `M-24501`  
Title: A timid-reviewer protocol separating exact algebra, imported transfers, finite computation, and the sole cofinal theorem  
Status: **PROPOSED METHODOLOGY**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Scope: PR-level adversarial review; no mathematical promotion

## 1. Frozen dependency ledger

Review only the following frozen states unless a later delta is separately
requested:

```text
former proposal PR #226
  rejected head
  63a4d7c0f482a57893db420e64b22f6a605c72e6

adversarial repair PR #241
  3a227e7595e1fe9e38956048297aa97531c80e4e

fixed-ratio shell PR #234
  2d5043070e15fe6be94307381f4023eaa48c17a5

finite carry proposal PR #244
  a1582d6167cc777edf3e21292702beb268bec69b

square-screw transfer PR #202
  d8511ae3105c4b20524732455e4e55009091520c
```

A verdict on one SHA does not extend to a later mutable head.

## 2. Claim classes

Use four distinct classifications.

### A. Exact algebra

Claims whose proof is finite symbolic, rational, or absolutely convergent
calculus:

```text
L-9518 independent-frequency reflected identity;
L-24501 carry kernel transform and inverse formula;
L-24502 carry coefficient, comparison, and greedy feasibility.
```

Classify each as `VERIFIED`, `VERIFIED WITH FIXES`, `GAP/BLOCKED`, or
`REJECTED` independently.

### B. Imported global transfer

The square-screw/Landau implication is not re-proved by a finite carry checker.
Audit its exact normalization, one-sided direction, derivative interpolation,
and functional-equation conclusion at the frozen PR #202 head.

### C. Finite computation

`X-24501` verifies only declared finite algebra. It cannot promote DCRS, a
cofinal carry mass, or RH.

### D. Cofinal theorem

`L-24503` is the only new asymptotic hinge. It remains open until its continuum,
discretization, and blocker ledgers are all proved uniformly.

## 3. Minimal review order

A cautious reviewer may proceed as follows.

1. Verify `R-24501`; reject any reintroduction of the old shortcuts.
2. Verify the two-cell telescoping proof in `L-24501`.
3. Verify the finite carry comparison in `L-24502`.
4. Run `X-24501` and its mutations.
5. Check that `T-24501` invokes only `L-24503`, not a hidden packet theorem.
6. Audit the frozen square-screw transfer.
7. Attack `L-24503` in its three ledgers.
8. Run the fixed-ratio shell mutation.

No familiarity with the full historic packet repository is required before
Steps 1--5.

## 4. DCRS proof-object schema

A claimed proof of `L-24503` must produce, for a symbolic endpoint `X` or an
unbounded proof-producing family:

```text
A. continuum
  exact finite-horizon nonnegative profile;
  cell endpoints and coefficients;
  every convolution upper bound;
  critical mass lower bound;
  Abel boundary correction;

B. discretization
  exact n/q cells;
  beta/b error by q;
  quadrature direction;
  finite feasible vector;
  small-n and diagonal corrections;

C. greedy/blocker
  blocker and tie at each stage;
  residual vector after each elimination;
  mass comparison potential;
  entropy-debt potential;
  quotient/digit/reflected-square terms;
  lower-endpoint routes;
  final telescope;

D. arithmetic firewalls
  all prime-power rows;
  square-screw normalization;
  fixed-ratio 2/3 shell mutation;
  source and code hashes.
```

Missing data causes `GAP/BLOCKED`, not reviewer completion by inference.

## 5. Required mutations

The proof producer and consumer must reject at least:

1. wrong generalized-Lambda sign in `L-9518`;
2. single-frequency replacement of the physical block;
3. wrong carry remainder `r`;
4. reversal of `beta<=b`;
5. deletion of the diagonal blocker;
6. deletion of one prime-power carry row;
7. signed use of a continuum profile where nonnegativity is required;
8. replacement of Abel mass by ordinary convergence without proof;
9. an uncharged off-diagonal greedy blocker;
10. a lower-scale route with endpoint not strictly smaller;
11. deletion of the fixed-ratio shell;
12. a finite ladder promoted to a cofinal theorem.

## 6. Quantifier checklist

The final DCRS statement requires absolute `A,C` and **every** integer `X>=2`.
A proof for a sequence, almost all endpoints, density one, bounded `X`, or
endpoint-dependent exponents is insufficient unless a separate transfer theorem
is supplied.

The square-screw conclusion requires a polylogarithmic or subpower bound on the
complete negative part, not merely an average sign or a positive subsequence.

## 7. Status rules

- A repair cannot retroactively verify PR #226.
- `PROPOSED EXACT` means a proof has been written but has not passed independent
  review.
- `FULL PROPOSAL` means the implication graph is complete after the explicitly
  named hinge; it does not mean the hinge is proved.
- No result is labeled `PROVED` or `INDEPENDENTLY VERIFIED` by its authoring
  agent.
- No public README change or merge is part of this protocol.

## 8. Acceptance matrix

```text
all exact algebra passes, DCRS open
  -> serious proposal, RH unproved;

DCRS proof misses one ledger
  -> GAP/BLOCKED;

DCRS and square-screw transfer independently pass
  -> full proposed proof ready for external verification;

finite experiments only
  -> computational reconnaissance;

old terminal-face argument reappears
  -> REJECTED by PR #241.
```

## 9. Reviewer deliverable

The preferred review is a short table with:

```text
claim / frozen SHA / verdict / exact issue / required repair
```

followed by one paragraph titled `RH STATUS`. This keeps mathematical validity
separate from integration or publication status.
