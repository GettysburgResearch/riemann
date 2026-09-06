# Formalization track

The Lean development lives in the self-contained [`formal/`](formal/README.md) subproject. **Read [FORMAL_STATUS.md](FORMAL_STATUS.md) first:** the September 6 audit changes the interpretation of the historical formal-v0.1 release.

The old actual-Xi source input is empty because of the total-function endpoint normalization, and its enumeration convention separately excludes empty or finite off-line spectra. A conditional theorem over that input is not an instantiated theorem about the intended Xi source. This is a source-fidelity defect, not a contradiction in Lean's kernel or a rejection of unrelated finite algebra.

The corrected entire normalization and conditional source-complete paper argument are retained in the [Xi repair](reviews/C/pass4-math-completion/proofs/XI_SOURCE_REPAIR.md). The full repaired Lean input, synchronized consumers and exact-tree verification remain outstanding. Candidate source outside trusted imports is not reported as compiled.

## Historical formal-v0.1

The original scope, source locks, inventory and reproduction commands remain in [`formal/FORMAL_V0_1.md`](formal/FORMAL_V0_1.md). The library uses Mathlib's `RiemannHypothesis` as its RH conclusion and keeps the named open premises explicit. Its 139-row registry is a status map, not 139 formalized theorems.

Scientific integration and formal integration are separate gates. Acceptance of a later paper proof does not silently extend formal-v0.1, and an old green build does not settle the newly identified statement-fidelity problem.

RH remains unproved. See [release readiness](RELEASE_READINESS.md) for the remaining source, build and publication checks.
