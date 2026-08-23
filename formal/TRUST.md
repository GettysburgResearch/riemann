# Trust model

## Trusted targets

The default `RiemannFormal` library, `Solution` comparator library, and release modules must contain:

- no `sorry`;
- no `admit`;
- no custom mathematical axioms;
- no import of Formal Conjectures as proof evidence;
- no hidden assertion that an RH-bearing open cut holds.

The only permitted foundational axioms in headline `#print axioms` output are Lean's standard:

```text
propext
Classical.choice
Quot.sound
```

A theorem with an explicit unproved mathematical hypothesis is conditional and must be recorded as `PROVED_CONDITIONAL`.

## Trusted statements versus solutions

Files under `comparator/Challenge/` are trusted statement specifications. They may contain deliberate `sorry` placeholders and import only Mathlib through their complete statement dependency layer.

Files under `comparator/Solution/` are untrusted implementations checked against those statements and must be sorry-free.

## External libraries

- Mathlib supplies the canonical Riemann zeta function and `RiemannHypothesis`.
- Zeta23 is a pinned Apache-2.0 dependency and supplies reusable analytic infrastructure.
- Formal Conjectures is a statement-comparison reference only.

Exact pins and the upstream comparison decision are in `registry/SOURCE_LOCKS.json` and `UpstreamAudit.md`.
