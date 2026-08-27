# Trust model

formal-v0.1 separates statement identity, proof implementation, scientific
status and external evidence.

## Trusted source closure

The trusted Lean library consists of:

```text
formal/RiemannFormal/**
formal/comparator/ChallengeDeps/**
formal/comparator/Solution/**
```

It must contain no `sorry`, `admit`, project `axiom`, `opaque`, `unsafe`, or
unresolved tactic-suggestion declaration. The standalone
`RiemannFormal.Analysis.ComparatorSmoke` file imports a Solution module only to
exercise the comparator build and is deliberately not imported by the trusted
`RiemannFormal.Analysis` aggregate.

The permitted foundational axioms are exactly:

```text
propext
Classical.choice
Quot.sound
```

The fail-closed audit rejects missing output, unexpected output, duplicate
output, `sorryAx`, malformed multiline output and every other axiom.

## Challenge/Solution separation

The seven Challenge files are Mathlib-only statement surfaces. Each contains
exactly one deliberate placeholder. The matching ChallengeDeps and Solution
files are placeholder-free.

Exact statement fidelity is checked in isolated Lean processes. The verifier
removes only the exact queried declaration-name prefix and whitespace before
comparison. Explicit binders and every mathematical symbol remain
load-bearing.

Challenge placeholders do not enter the trusted aggregate or Solution proof
closure.

## Open mathematics

An open theorem is represented as a proposition or an explicit theorem
parameter. It is never installed as an axiom asserting that it holds.

For example, the tail-Mellin Landau and negative-mass holomorphy results are
exact propositions consumed explicitly by a conditional theorem. Compiling
that implication establishes the implication only; it does not prove either
premise or RH.

Likewise, the actual-Xi order-three wrapper keeps the external verified-height,
grouped convergence, multiplicity, tail and reserve inputs explicit.

## Source and release locks

The release manifest pins:

- the August 22 scientific integration and PR #707 research cutoff;
- the formal bootstrap;
- exact A/B/C source heads;
- the independent exact-head build audit;
- Lean, Mathlib and Zeta23 revisions;
- expected registry, comparator and axiom counts.

The final reconciliation commit and tree are recorded in the integration PR,
because a commit cannot contain its own hash.

## Computation boundary

This formal release runs ordinary Lean compilation and small exact validation
scripts. It does not rerun historical zeta-zero scans, interval campaigns,
finite-field censuses, trace-cube searches or other heavy computations.
External artifacts remain external unless a kernel-checked certificate and
verified checker are supplied.

Machine verification checks the declaration actually presented to Lean. Human
and comparator review remains necessary to ensure that declaration is the
intended scientific statement and uses the correct source, normalization,
quantifiers and conclusion scope.
