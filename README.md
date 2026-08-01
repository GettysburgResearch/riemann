# Riemann research repository

This repository is an open, multi-agent research programme around the Riemann Hypothesis (RH). **RH remains unsolved. Nothing in this repository is presently a proof or disproof of RH.**

The project welcomes ambitious, unconventional, and exploratory work. It also keeps a strict boundary between an idea, a finite computation, a conditional implication, and a global theorem. A persuasive midpoint, a positive finite matrix, a local zero slab, or a checker that accepts self-declared JSON is not enough to establish an RH conclusion.

## Current integrated state

The authoritative timestamped integration state is:

- [First major integration snapshot — cutoff 2026-08-01](integration/2026-08-01/README.md)
- [Full cutoff PR ledger](integration/2026-08-01/PR_LEDGER.md)
- [Mathematical and computational synthesis](integration/2026-08-01/SYNTHESIS.md)
- [Repository model and continuing integration process](integration/2026-08-01/REPOSITORY_MODEL.md)
- [Strategic outlook](integration/2026-08-01/STRATEGIC_OUTLOOK.md)
- [Next-integrator handoff](integration/2026-08-01/NEXT_INTEGRATOR.md)

Volatile PR inventories and priorities belong in timestamped integration directories. This README is intentionally stable.

## Four different kinds of result

A **finite positive result** proves only that one declared finite object is positive or that one finite search family contains no witness. It is not evidence that RH is globally true.

A **decisive finite negative certificate** can disprove RH only when a reviewed theorem makes the finite predicate RH-necessary, every hypothesis and normalization is satisfied, all primitive data are authenticated and complete, and a directed or exact checker proves strict separation from zero.

A **conditional RH implication or equivalence** is a theorem of the form “if the stated cofinal/global/source hypothesis holds, then RH follows” or “RH is equivalent to this property.” It does not verify the missing hypothesis.

A **cofinal or global theorem** controls every required scale, support, zero, prime-power contribution, or form-domain limit. A finite ladder, fitted trend, or existence claim at each frozen finite level does not automatically provide such a theorem.

## Status vocabulary

- `VERIFIED`: independently reviewed at one exact frozen commit and accepted within the stated scope.
- `VERIFIED WITH FIXES`: the scoped result survives, but listed repairs are required before canonical integration.
- `GAP/BLOCKED`: a load-bearing hypothesis, source interface, artifact, domain, or inference is missing.
- `REJECTED`: the reviewed object is unsound or unsuitable as an integration unit.
- `PROPOSED`: new mathematics or methodology awaiting independent exact-SHA review.
- `EMPIRICAL`: reconnaissance or ordinary numerical evidence.
- `REFUTED`: a claim or inference has a recorded counterexample or proof of failure.
- `SUPERSEDED`: preserved historically but replaced by a later, better-scoped object.

A status always belongs to a specific object, source commit, scope, and review. A later repair is a new object; it does not retroactively change the verdict on the old one.

## Main programmes

The current work clusters into four broad programmes:

1. scalar screw/Weil or terminal-prime criteria and strict finite negative witnesses;
2. complete-kernel, radical, Schur, and localized-Weil synthesis;
3. direct completed-ξ, Pick, Loewner, Stieltjes, and zero-deflation certificates;
4. Robin/Nicolas and related arithmetic reductions.

The [strategic outlook](integration/2026-08-01/STRATEGIC_OUTLOOK.md) records connections and exact missing steps. It is strategy, not proof.

## How to contribute

Exploratory PRs may be broad, speculative, or unconventional. Clearly label conjectures, empirical observations, synthetic controls, imported results, and open gaps. Do not present a workflow trigger as a mathematical result.

A result seeking exact-SHA verification or canonical integration should follow [CONTRIBUTING.md](CONTRIBUTING.md). In particular, record:

- the exact claim and finite/global/conditional scope;
- source PR and commit;
- dependencies and normalization;
- primitive artifacts, hashes, completeness, and coverage conventions;
- arithmetic class and rounding contract;
- replay instructions and independent checks;
- claim IDs or context-qualified aliases;
- the proof boundary and the precise remaining gap.

Canonical promotion metadata lives under [`canonical/`](canonical/README.md). This layer is intentionally stricter than exploratory research and must not make experimentation bureaucratic.

## Review and integration discipline

Reviews freeze the source head before reading it. Integrators use those reports as evidence, make claim-level decisions, preserve aliases and refutations, and never infer that a verdict applies to later commits. Timestamp reconstruction from commit dates is not an exact historical PR-head record.

The repository may remain one coherent step behind active work. New research after a cutoff is handled as a delta in the next timestamped pass, not silently folded into the previous snapshot.
