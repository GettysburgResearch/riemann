# Combined A+B+C rehearsal build report

## Frozen assembly

- Bootstrap: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- A: `ae0887b8125601c98dc809cffe01c7f1c78bb998`
- B: `6d42bbc31c81e7d6a03909e205b56f30f6f7b49a`
- C: `381a5a98ade7c6bad7122e5182c2fc07332dc747`
- Local rehearsal commit: `ae50ef2786b904a9aecdcfb1112d7b323f36ea41`
- Tree: `bd621c02db310fc318ee287eefeb6e2c76c8b48a`
- Advisory patch SHA-256:
  `99027ec29f916acf001eea9db1dcee5abf20dd014bd7781a51bc77459dc954a2`

All four frozen source commits are ancestors of the rehearsal. A, B, and C
were applied in the prescribed order. Review-only PR commits were not merged.

## Dynamic result

The final serialized runner executed 58 commands. All 58 exited 0 from
2026-08-27T00:47:05Z through 01:18:38Z (31m33s).

- Dependency sidecars matched the green C cache byte-for-byte.
- Four isolated pinned-Zeta23 recovery targets passed.
- Full trusted build: PASS, 8,806 jobs.
- Registry generation and validation: PASS, 139 unique claims.
- Source locks: PASS; Mathlib `51e6992e`, Zeta23 `cec57f91`.
- Blueprint: PASS, three fragments.
- Generalized no-sorry/custom-axiom boundary: PASS, seven topics.
- Complete fail-closed axiom audit: PASS, exact 89/89 outputs.
- Aggregate comparator and A's standalone bootstrap smoke: PASS.
- All 21 explicit comparator targets: PASS.
- Independent exact Challenge/Solution theorem-type comparison: PASS, 7/7,
  using isolated Challenge and Solution Lean processes.
- A retained validation: PASS in 547 seconds.
- B trusted arithmetic module group: PASS, 3,906 jobs.
- C declaration, statement-source, static, external-input, and comparator
  fidelity checks: PASS.
- All nine axiom-print modules also compiled independently.
- Closing registry, source-lock, and blueprint validations: PASS.

The runner ledger SHA-256 is
`188e07587a1b60d16bdf6fa31063c82c787de3134a4ab689ea5a546f7b127e97`.
The full local raw-log checksum file has SHA-256
`6b26b1831f9d185fd483560f8ee8ef60e60061f8bce1f5eb29b5f8a3b4b44bc2`;
every listed entry was reverified with `sha256sum -c`.

The first version of the separate exact-type audit parser rejected valid
explicit binders between a theorem name and its colon. That attempt is retained
as `COMPARATOR_AUDIT_TOOL_FAILURE`; it failed before comparing any theorem
types. The corrected parser removes only each exact declaration-name prefix and
Unicode whitespace, preserves all binders and mathematical symbols, passes an
explicit-binder regression fixture, and matched all seven topic types.

## Trust boundary

The trusted aggregate closure contains no Challenge or Solution import. The
standalone A comparator smoke module remains available for explicit validation
but is not imported by `RiemannFormal.Analysis`.

Exactly seven Challenge placeholders remain, one per topic. There is no
`sorry` or `admit` in trusted, ChallengeDeps, or Solution sources, and no
custom declaration-level `axiom`, `opaque`, or `unsafe` shortcut in those
trees.

The actual-Xi order-three comparator retains repeated-node branches and
concludes only the stated PSD result. RH remains conditional and unproved.

## Classification

`PASS`
