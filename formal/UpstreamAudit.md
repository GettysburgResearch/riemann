# Upstream dependency audit

## Zeta23

The Riemann project previously audited:

```text
anthropics/zeta-23-lean@3635e74826a4c1fcece7d1cd2b6fa75e43a00510
```

Current upstream at bootstrap is:

```text
anthropics/zeta-23-lean@cec57f919ccf34e5fa5372b4ba332f7c848bbb6e
```

GitHub comparison reports the current head is nine commits ahead and changes only:

- `AUDIT.md` and `README.md`;
- comparator trusted/solution/config files;
- `formalization.yaml`.

No file under `Zeta23/` changed in that interval. The bootstrap therefore pins current `cec57f9...` while recording both commits. This decision does not transfer formal status to any local Riemann theorem.

## Mathlib

The project pins the exact Mathlib revision used by Zeta23:

```text
51e6992efd06126df61a496bebf8f49482a4e129
```

Mathlib's global `RiemannHypothesis` proposition is the sole RH conclusion used here.

## Formal Conjectures

`google-deepmind/formal-conjectures@488aade228ec37880b8fec178c173c07d279bb53` is used only to compare the intended RH statement. Its open theorem contains `sorry` by design and is not a proof dependency.
