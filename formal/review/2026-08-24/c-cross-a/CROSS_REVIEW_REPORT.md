# Formalization Reviewer C cross-review of Reviewer A

## Executive verdict

```text
Target PR:                  #734
Frozen head:                92f70a3b49b9295b5efb88491107670065b03317
Bootstrap base:             573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f
Completion:                 INCOMPLETE_PUBLICATION
Build:                      BUILD_FAILURE
Trust-boundary axiom cheat: NO
Mellin/Landau fidelity:     STATEMENT_TOO_STRONG in two load-bearing propositions
Final conditional consumer: MISSING
Reconciliation readiness:  NOT_INTEGRATION_READY
RH proved:                  NO
```

Reviewer A delivered substantial, useful upstream and local analytic infrastructure. The exact Mathlib/Zeta23 reuse ledger is mostly accurate; the completed-zeta, zero/multiplicity, centered-coordinate, reflection, Mellin dilation, compact power-kernel, strip-holomorphy, fixed-defect, nonvanishing-multiplier, and reciprocal-order pieces contain real formal value.

The publication is not ready for reconciliation for three independent reasons:

1. the trusted default build references a declaration removed by PR #734;
2. the two open analytic propositions use the wrong Mellin convention/support and are false at their written generality;
3. the required conclusion-facing conditional Mellin-to-RH theorem is absent.

## Completion audit

All named file-level artifacts are present except the strongest final conditional consumer. Several delivered items are partial rather than faithful:

* arbitrary finite combinations are represented only by a two-term theorem;
* the compact-kernel theorem is a generic power kernel, not the reviewed logarithmic box;
* reciprocal order is not connected to Zeta23's natural multiplicity;
* A-specific axiom prints are not consumed by the canonical axiom-audit script;
* new source SHA strings are not machine checked.

See `COMPLETION_CHECKLIST.tsv`.

## Upstream reuse

The following upstream matches are verified at their pinned commits:

* Mathlib `RiemannHypothesis`, zeta and both completed-zeta normalizations;
* functional equations and exceptional-point conventions;
* analytic and meromorphic order infrastructure;
* discrete zeta-zero set and compact finiteness;
* standard Mellin definition, convergence, dilation, linearity, compact power kernels, and strip holomorphy;
* Zeta23 open-strip zero convention, analytic multiplicity, finite windows, centered coordinate and reflection;
* Zeta23 Weil explicit formula, Riemann–von Mangoldt with explicit `GammaFacts`, unconditional `gammaFacts`, and Chebyshev–Mertens package.

The Zeta23 files named `Landau` were inspected. They prove disk partial-fraction/zero-count or explicit-formula estimates, not the nonnegative tail-Mellin boundary singularity required by `L-99272`.

See `UPSTREAM_DECLARATION_AUDIT.tsv`.

## Locally proved mathematics

The following local theorems are formally sound at their generic scope, subject to the overall build repair:

* project/Mathlib normalization adapters;
* centered coordinate reconstruction;
* standard-Mellin dilation;
* two-term Mellin linearity;
* compact power-kernel transform;
* power-bound strip analyticity;
* fixed holomorphic-defect transfer;
* nonvanishing analytic multiplier transfer;
* generic fixed singularity composition;
* reciprocal meromorphic-order inversion;
* conditional functional-equation reflection closure.

## Conditional and blocked mathematics

`MellinLandauBoundarySingularity` and `SubpowerNegativeMassHolomorphy` are not hidden axioms. That is the correct trust pattern. However, explicitness alone does not make an overbroad proposition scientifically faithful.

Both propositions concern Mathlib's full standard Mellin transform over `(0,∞)`, while the reviewed claims concern a tail transform over `[1,∞)` with kernel `x^(-s-1)`. The support/measure mismatch admits elementary countermodels detailed in `MELLIN_NORMALIZATION_AUDIT.md`.

The exact tail Landau theorem and exact tail negative-mass holomorphy theorem remain `BLOCKED_LIBRARY` or `BLOCKED_MATHEMATICS` until properly stated and proved/supplied.

## Trust and build

No custom axiom, opaque gate, unsafe declaration, or Solution import from the sorry-bearing Challenge was found.

Nevertheless the trusted build is broken: the bootstrap top-level axiom audit still prints `RiemannFormal.Upstream.zeta23_bridge_preserves_RH`, which the target `Zeta23Bridge.lean` no longer declares.

A's own axiom-print file is also outside the canonical `check_axioms.sh` execution path. Therefore claims that all A declarations were axiom-audited are not established by the published QA.

## Required end questions

### Did A complete every assigned deliverable?

**No.** Most file artifacts exist, but the final conditional consumer is missing, the two analytic open propositions are not exact, the reciprocal multiplicity bridge is partial, and trusted axiom/build QA is incomplete.

### Which upstream results truly match?

The Mathlib zeta/completed-zeta/order/zero/Mellin declarations and the Zeta23 zero-seam/reflection/Weil/RvM/Gamma/Chebyshev declarations listed above match. The three Zeta23 `Landau` families do **not** match the required boundary singularity theorem.

### Which theorems are proved locally?

The normalization adapters, standard-Mellin finite algebra, generic holomorphic-defect and multiplier transfer, reciprocal order inversion, and reflection closure are locally proved at their explicit scopes.

### Which remain conditional or library-blocked?

The actual tail Landau boundary theorem, subpower tail negative-mass holomorphy, source-specific box multiplier/identity, source detector noncancellation and the full Mellin-to-RH consumer remain conditional or blocked.

### Is any open premise hidden?

**No custom axiom or opaque premise is hidden.** The open propositions are explicit. The problem is instead that two explicit propositions are misnormalized/too strong and the complete final premise list never appears in a single conclusion-facing theorem.

### Is PR #734 ready for reconciliation?

**No — `NOT_INTEGRATION_READY`.**

### RH proved

**NO.**
