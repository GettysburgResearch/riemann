# External resource: Fermat's Last Theorem formalization

Status: IMPORTED_REFERENCE / OVERVIEW_ONLY / NOT_VERIFIED_HERE
Scope: contributor awareness and prospective reuse; no mathematical dependency added
Agent: astra-flt-awareness-20260905
Recorded: 2026-09-05
Exact source: anthropics/fermats-last-theorem at aa2d8b34692b16c70f699536de0d8e75b9a3e9ef
What was actually run: read the upstream overview; retrieved commit and README blob identifiers through GitHub; checked this documentation diff
Smallest remaining gap: before any mathematical reuse, inspect the exact theorem statements, dependencies, attribution, and toolchain compatibility

## Pinned source

- [Repository at the recorded revision](https://github.com/anthropics/fermats-last-theorem/tree/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef)
- [README](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/README.md), Git blob `f3cfcb92443c29a8ce87494f6c9a7b57e40129e9`
- [Proof-path map](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/PROOF-PATH.md)
- [Attribution](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/ATTRIBUTION.md)

The upstream README describes a complete Lean formalization following the Frey–Serre–Ribet–Wiles–Taylor–Wiles argument, with statement comparison, an independent-kernel check, and a browsable dependency site. These are upstream descriptions, not findings of a Riemann audit. It identifies Lean 4.33.1, Mathlib v4.33.0, Apache-2.0 licensing, and an unmaintained research-artifact status. It credits the Imperial College London FLT project, flt-regular, and Mathlib.

No Lean build, proof review, Comparator run, or independent-kernel replay was performed for this note. Only this reference note is imported; upstream source code and generated documentation are not vendored.

## Potential relevance to Riemann

The connections below are research suggestions, not established adapters.

| Existing program | Possible use |
|---|---|
| [#738: GL(2) twists and elliptic curves](https://github.com/gfreund123/riemann/issues/738) | Locate reusable elliptic-curve, Galois-representation, and modularity statements when formalizing the relationship between arithmetic objects and their L-functions. This supplies no zero-distribution estimate by itself. |
| [#763: Riemann Structures](https://github.com/gfreund123/riemann/issues/763) | Study modularity as an example of a precise bridge between arithmetic and another mathematical setting; distinguish actual bridge theorems from suggestive analogies. |
| [#764: Generalized L-Objects](https://github.com/gfreund123/riemann/issues/764) | Investigate whether specific deformation or representation-theoretic definitions help state rigidity and compatibility questions. Such reuse requires inspecting the definitions first. |
| Formalization and contributor onboarding | Consider proof-path maps, explicit theorem dependencies, statement-fidelity checks, and browsable documentation as presentation and verification patterns. |

## Suggested next use

When a contributor needs a particular result, identify its exact declaration and minimal dependencies at the pinned revision, check compatibility with Riemann's toolchain, and preserve upstream licensing and attribution. Propose any selective code import separately with an explicit review boundary.

This resource provides no immediate RH cancellation, positivity, or zero-exclusion theorem. It does not alter the canonical claim registry or the formal-v0.1 trusted release.
