# Formalization track

The repository's Lean development lives in the self-contained `formal/`
subproject.

Current release: **formal-v0.1**, formalizing the reviewed August 22, 2026
scientific release through PR #707.

```text
Riemann Hypothesis: UNPROVED
unconditional Lean theorem proving RH: NONE
conditional RH implication with explicit premises: PRESENT
```

Read [`formal/FORMAL_V0_1.md`](formal/FORMAL_V0_1.md) for the exact source
locks, theorem inventory, exclusions, comparator surface, trust boundary and
reproduction command.

The formal release uses Mathlib's `RiemannHypothesis` as its unique RH
conclusion, pins Mathlib and the Anthropic Zeta23 dependency, and keeps every
unproved RH-bearing theorem as an explicit proposition or theorem parameter.
No open gate is installed as an axiom.

The generated `formal/registry/FORMALIZATION_MAP.tsv` maps all 139 canonical
scientific semantic IDs to their independent formal status. Most of the
canonical corpus remains unproved or not yet exactly stated in Lean; the first
release is a reviewed gold spine, not a full formalization of the repository.

Post-PR-707 research, including later beta and L-function-family work, is
excluded until it receives its own scientific review and integration.
