# M-26001 — Refutation verdict compatibility gate

Claim ID: `M-26001`  
Title: A counterexample refutes only the exact statement whose hypotheses it satisfies  
Status: **PROPOSED REVIEW METHODOLOGY; ELEMENTARY LOGICAL CORE EXACT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Scope: review verdicts, refutation records, integration ledgers, and cross-PR summaries

## 1. Purpose

The repository correctly freezes claims and reviews at exact commits, but one
additional distinction is needed. The words `REJECTED` and `REFUTED` are often
propagated from a failed construction to a stronger statement, an RH-bearing
hypothesis, or an entire route. That propagation is invalid unless the review
actually contradicts the exact statement.

Write a mathematical claim in the form

\[
S:\qquad \forall x\in D,\quad H(x)\Longrightarrow C(x).
\]

An exact refutation of `S` must provide an object `x_0` for which all three
checks are explicit:

\[
x_0\in D,\qquad H(x_0),\qquad \neg C(x_0).
\]

A failed proof, a counterexample outside `D`, or a counterexample to a stronger
surrogate does not refute `S`.

## 2. Required verdict classes

Every negative review should use one of the following classes.

### `CLAIM_REFUTED`

A counterexample satisfies every declared hypothesis of the frozen claim and
contradicts its conclusion.

### `DERIVATION_REJECTED__STATEMENT_OPEN`

A displayed identity, inference, estimate, or proof step is false or missing,
but no counterexample to the theorem statement is supplied.

### `SURROGATE_REFUTED__SPECIFIC_STATEMENT_OPEN`

The review disproves a stronger generic, unsigned, unweighted, monotone,
finite-block, sampled, or arbitrary-vector surrogate. The source-specific
signed or weighted statement remains open.

### `INSTANCE_REFUTED__ABSTRACT_CRITERION_SURVIVES`

An abstract implication or criterion is sound, but the proposed test function,
adjoint, packet, support, or finite construction does not satisfy its
hypotheses.

### `CONDITIONAL_THEOREM_SURVIVES__HYPOTHESIS_UNPROVED`

The implication `A => B` remains valid; the attempted construction or proof of
`A` failed.

### `LIFECYCLE_REJECTED__NO_MATHEMATICAL_VERDICT`

The object is a trigger-only branch, obsolete workflow, missing artifact,
provenance wrapper, duplicate, or superseded integration unit. This is a
repository-lifecycle disposition, not a refuted mathematical claim.

### `FROZEN_OBJECT_REJECTED__LATER_REPAIR_SEPARATE`

The exact frozen proof object is invalid. A later repair may be a new proposal,
but never retroactively changes the frozen verdict.

## 3. Composition rule

Suppose a proposed proof has the form

```text
A --construction P--> B --valid implication--> RH.
```

A counterexample to construction `P` proves only that the displayed route from
`A` to `B` fails. It does not refute `B`, and it does not refute the implication
`B => RH`, unless the counterexample also satisfies the hypotheses of one of
those statements and contradicts its conclusion.

Similarly, if a proof replaces a source-specific vector by an arbitrary vector,
a signed transport by a nonnegative cover, a weighted norm by an unweighted
norm, or a finite Gram matrix by a limiting Bohr variance, a counterexample to
the replacement refutes the replacement. It need not refute the original
source-specific statement.

## 4. Mandatory compatibility table

A refutation record should contain the following fields.

| Field | Required content |
|---|---|
| Frozen target | Claim ID, file, PR, and exact commit |
| Exact hypotheses tested | Every domain, sign, weight, normalization, quantifier, and boundary condition used by the target |
| Counterexample witness | Exact or directed object, with replay instructions when computational |
| Contradicted conclusion | The precise displayed conclusion that fails |
| Surviving scope | Every theorem, implication, source-specific estimate, or repaired object not contradicted by the witness |

If the fourth field cannot be filled, the result is not a claim refutation. If
the second field differs from the target, the result is a surrogate refutation
and must say so.

## 5. Aggregate-ledger rule

Mathematical verdicts and lifecycle dispositions must be stored in separate
columns. In particular, a count such as

```text
REJECTED = 3
```

must not combine false theorems with trigger-only branches or obsolete
provenance contracts. Recommended fields are

```text
mathematical_status
review_status
lifecycle_status
counterexample_hypothesis_match
surviving_scope
```

Historical ledgers should remain frozen. Corrections should be append-only
overlays, not silent rewrites.

## 6. Proof of the logical core

The negation of

\[
\forall x\in D,\ H(x)\Longrightarrow C(x)
\]

is

\[
\exists x\in D\quad H(x)\wedge\neg C(x).
\]

Therefore an object that fails a hypothesis, belongs to a different domain, or
contradicts only a stronger conclusion is not a witness to the negation of the
original statement. A derivation can be invalid while its conclusion remains
true or open. This is the complete logical content of the gate.

## 7. Status boundary

This methodology does not verify any RH-bearing statement and does not revive a
rejected proof. It prevents a valid narrow counterexample from being promoted
to an invalid broad refutation, while preserving every exact frozen verdict at
its proper scope.
