# Formalization status

Current release: **formal-v0.1**

```text
Riemann Hypothesis: UNPROVED
reviewed unconditional Lean path to RH: NONE
conditional Lean path to RH: PRESENT WITH EXPLICIT PREMISES
trusted sorry/admit/custom axioms: NONE
Challenge-only placeholders: 7
canonical scientific claims represented in registry: 139
post-PR-707 research included: NO
heavy computation run by this release: NO
```

## Audited release census

- 139 unique canonical registry rows;
- 31 A/B/C canonical delta rows;
- 2 `STATED` rows;
- 10 `PROVED` rows;
- 8 `PROVED_CONDITIONAL` rows;
- seven exact comparator topics;
- nine committed axiom-print modules;
- 89 expected axiom outputs in the combined rehearsal;
- only `propext`, `Classical.choice`, and `Quot.sound` permitted.

The authoritative detailed front door is [`FORMAL_V0_1.md`](FORMAL_V0_1.md).
The complete claim-by-claim status is generated at
`registry/FORMALIZATION_MAP.tsv` from the August 22 canonical registry and the
sparse reviewer deltas.

A `PROVED_CONDITIONAL` theorem is a genuine Lean implication whose unproved
mathematical inputs appear as explicit parameters. It is not evidence that
those inputs hold. In particular, the fixed-detector negative-mass theorem and
the actual-Xi order-three theorem do not prove RH or unconditional Xi
positivity.
