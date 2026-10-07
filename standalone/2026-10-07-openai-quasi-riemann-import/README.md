# OpenAI's quasi-Riemann result: complete source import and research bridge

Status: **IMPORTED EXTERNAL RESULT; SELECTIVE SOURCE AUDIT; CONDITIONAL SYNTHESIS.**
Scope: OpenAI math family 003, its three manuscripts, and the complete internal Lean implementation dependency closure.
Upstream: **openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a**, released 6 October 2026 at 21:58:50 UTC.
Repository base: **f99d9e3908dde4865377c75d9ca051c1f545bf4f**.
Review date: 7 October 2026.
Smallest remaining verification step: independently build the pinned formal implementation and run the four supplied Comparator challenges.
Smallest remaining mathematical bridge to our RH programme: control the literal native coarse covariance, with a genuine contraction and the full complement paid.

## What has been imported

The external claim is a fixed zero-free half-plane **$\Re s>7/8$ for every Dirichlet $L$-function, including zeta, and every finite-order Hecke $L$-function over $\mathbb Q(\sqrt{-3})$**, with principal poles retained. A separate, more readable manuscript proves the weaker **$\Re s>11/12$** claim by a different argument. A third manuscript proves uniform exclusion of Landau–Siegel zeros using interpolation determinants.

The first claim, if verified, is a major all-height analytic result. It does not prove RH or GRH, does not address the boundary line $\Re s=7/8$, and does not say that $7/8$ of the zeros lie on the critical line.

This packet preserves **3,286 upstream files, 40,874,019 bytes**, without modifying their contents:

- All three original PDFs, full LaTeX sources, and manuscript citation READMEs.
- All **3,232 internal Lean implementation modules** reached from the zeta/Dirichlet, Hecke, and Siegel-zero solution roots.
- The four Comparator challenge specifications and configurations, scope documentation, pinned Lean toolchain and package manifest, original Lake configuration, and every compatibility patch that configuration requires.
- Original Apache-2.0 licenses, repository README, manuscript catalogue, and overview.

The release's external Lean packages are pinned in its original manifest; their source trees and compiled caches are not duplicated here. This is a complete family-003 internal-source subset, not a copy of the entire 722-manuscript collection. The upstream library's default aggregate target spans unrelated families, so use the targeted verification commands in the formal audit.

## Read the findings

| Question | File |
| --- | --- |
| What exactly is claimed, and how does the proof work? | [Result and proof walkthrough](RESULT_AND_PROOF.md) |
| Which analytic steps were actually checked? | [Mathematical audit](MATHEMATICAL_AUDIT.md) |
| Is the Lean result conditional, and what was independently verified? | [Formalization audit](FORMALIZATION_AUDIT.md) |
| How does this connect to our current branches? | [Repository comparison](REPO_COMPARISON.md) |
| What concrete new deductions can we make conditionally? | [Conditional bridges](CONDITIONAL_BRIDGES.md) |
| Which next theorem would constitute a real advance? | [Research plan](RESEARCH_PLAN.md) |
| What was executed, and how can it be repeated? | [Validation record](VALIDATION.md) |
| Where did every byte come from? | [Source manifest](UPSTREAM_FILES.json), [provenance](PROVENANCE.json), [notices](THIRD_PARTY_NOTICES.md) |

## The strongest connection to our work

The most useful imported mechanism is the October 5 proof's signed allocation in its second Poisson transfer. Complete arithmetic preimages share one kernel. Summing them before taking absolute values forces a divisibility constraint, and that constraint makes the child family smaller. This is a concrete model for the cancellation our composite covariance programme is missing.

There is also a precise quantitative comparison. Via the classical reciprocal-zeta/Möbius-summation interface, the claimed $7/8$ theorem would give our native energies the envelope $F_X,E_X\ll_\epsilon X^{3/4+\epsilon}$. The completely assembled existing MHB32 estimate maps that exponent to $505/546>3/4$, so substituting this new input into that estimate does not improve it. A new mixed-covariance or native family-transfer theorem is still necessary.

One smaller conditional gain does follow from combining the new envelope with CAP36: its actual reciprocal-completion width improves to $J\ll Y^{7/8+\epsilon}$, and its bounded anchored-phase transport error becomes $O_{\epsilon,H}(\tau^2Y^{5/4+\epsilon})$. That is a bound on a difference of observables, not a bound on the unresolved observable itself. The full derivation and the incompatibility with the current long dephasing window are recorded.

## Verification boundary

The upstream release supplies an implementation whose exported theorems are unconditional and refer to the standard Mathlib zeta and Dirichlet functions. Our internal import-graph and lexical scan found no unresolved internal imports or the scanned proof-hole/escape tokens in that implementation. The intentional challenge stubs are separate.

A fresh Lean kernel build and Comparator execution were **not run** in this environment; the required tools are absent. The mathematical audit checks selected critical arguments and exact algebra, not every analytic line of the long manuscripts. The inherited research branches retain their earlier proposed status. This import does not promote the external theorem or any combination to the repository's accepted integrated results.

## Reproduce the local checks

From this packet directory:

~~~sh
python checks/verify_import.py --source /path/to/pinned/openai-math
python checks/verify_upstream_checkpoints.py
python checks/audit_lean_sources.py
python checks/hybrid_exponent_budget.py
~~~

The source checkout is optional for the first command; supplying it compares the copied blobs to an independently fetched frozen Git tree, in addition to the stored SHA-256 manifest. None of these Python checks is a replacement for the four formal Comparator runs.

Original upstream materials retain their original license. The new explanatory notes and checks are project contributions under the repository's MIT license.
