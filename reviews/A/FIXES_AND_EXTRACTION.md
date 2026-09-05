# Reviewer A — fixes, extraction, and independent handoff

**Preliminary and incomplete. No review PR was published or verified in this attempt.**

## 1. Blocking work before any integration acceptance

1. Retrieve and apply `docs/REVIEWING.md`; read the actual August 22 manifest rather than the README's description. Confirm the scientific boundary remains PR #707 even if main includes later formalization or housekeeping.
2. Freeze a current post-release source census with PR head, base, update time, exact inspected paths and blob hashes. Record stale body SHAs separately. Compare each frozen head with the head at publication; leave later commits unreviewed unless separately inspected.
3. Retrieve the issue specifications and complete relevant descendant lists for #743, #744 and #746. The present report does not complete that scope.
4. Replay only named certificates at their frozen sources, with analytic remainder and primitive-data assumptions explicit. Author-reported PASS totals are not this reviewer's evidence.
5. Finish the original mathematical-source review for #787--#789. Outstanding B/C scientific/formal/provenance questions are pending integrator reconciliation, not automatic acceptance or rejection.

## 2. Required statement repairs and scope constraints

| Item | Required action | Surviving material |
|---|---|---|
| #786/R-109203 | Do not extract a cofinal numerical refutation from phase sweep plus finite efficiency observations; obtain the missing asymptotic theorem or restrict the verdict | Finite counterchecks, exact mesh/winding identities if separately reconstructed |
| #786 fixed-detector LI branch | Keep LI, zero-safe multiplier and certified residue-sum hypotheses; non-directed numerical sums are not certified lower bounds | Exact Ingham consumer and conditional criterion |
| #786 PRIMLS / PRIMCAR | Inspect modulus/twist ranges and the Ng explicit-formula error before claiming equivalence or implication | Deterministic grouping and exact source normalization |
| Positive determinant compactness | Retain the exp(gamma*u) escape term until xi growth removes it | Existence theorem without compatible compressions |
| Finite quadrature | Call it a positive resolvent quadrature, not a low-rank ordinary determinant with integer multiplicities | Exact finite moment matching conditional on replayed signs |
| #785 spectral positivity | Do not infer Schur-coefficient signs; preserve the negative-minor counterexample | All-rank spectral Andreief identity and Casimir algebra |
| #790 heat regimes | Keep early-time uniform regime distinct from fixed t=m/u rays; retain complete prime-tail estimate | Uniform Fourier mixture, exact continuum subtraction, ray detection |
| Hardy/heat capture | Keep original metric, target-dependent gaps and all tails; do not transfer compact-band estimates without an adapter | Complete capture and prescribed finite source matrices |
| Arithmetic cutoffs | Distinguish raw prime truncation from exact finite-dimensional full-source compression | Raw-cutoff no-go plus balanced approximation error |
| Reciprocal versus logarithmic derivative | Do not assert RH implies polynomial reciprocal-energy growth without controlling multiplicities and conditioning | Subexponential reciprocal endpoint and the conditional multiplicity bound |
| Meromorphic radial/vertical norms | Require holomorphy or causality before identifying a norm with Taylor coefficients or the intended positive-time source | Exact anti-causal and interior-pole counterexamples; weighted-area criterion |
| F1 / principal restriction | No extraction from finite Hodge or nonprincipal purity to principal arithmetic without the exact source map | Finite geometry and source-blind non-implication in their actual scopes |

## 3. Proposed extraction organization

The destinations in `CLAIMS.tsv` are **proposals**, not files already accepted or created in the integrated tree. Use `research/integrated/<next-release>/` until the integrator chooses a release date. Keep separate packets for arithmetic consumers, theta spectral identities, heat detectors, Hardy capture, finite certified computations, and refutations. Preserve historical source paths and source commits in every extracted packet.

Canonical graph entries should distinguish:

- reconstructed unconditional component;
- exact implication with named open premise;
- conditional theorem importing a classical analytic input;
- finite numerical/interval certificate awaiting replay;
- refuted generic mechanism;
- unsupported extrapolation;
- unchecked scientific source.

Never place an edge whose premise is an open RH-strength bound into a reviewed-only proof path as though the premise were proved. Do not convert a generic altered-source counterexample into a refutation of the literal xi or Mobius statement.

## 4. Questions for reviewer B

- Does any finite Segre/Chow/Frobenius character construction actually realize the *literal* theta coefficients as positive traces, or only a virtual Euler characteristic? Identify exact functors and source maps.
- In the common-source and F1 programmes, which geometric quotient removes each carrier exactly once, and where is physical restriction proved with its original norm?
- For #778, are all purportedly preserved geometric/occupancy hypotheses invariant under the principal-mode counterexample? What extra source datum would prevent adding a constant mode?
- Independently check the Schur-polynomial/Vandermonde all-gap bounds, confluent metrics, and any finite Poincare-frame statements subsequently used in arithmetic claims.
- For reverse Rolle, check multiplicity-sensitive algebra and whether finite local countermodels satisfy the complete claimed admissible class; leave the global arithmetic phase estimate distinct.
- For #789, check the compulsory Pascal minor, clearing-factor accounting and minimum-versus-maximum quantifiers directly from the paper.

These are handoff questions, not prerequisites preventing A from finishing its own audit. They remain pending integrator reconciliation.

## 5. Questions for reviewer C

- Supply or reconcile exact current source heads and the August 22 manifest, without treating outstanding A/B scientific dispositions as failures or acceptances.
- For every interval certificate, distinguish raw primitive replay and explicit rounding/remainder bounds from a script accepting a stored result flag.
- For #787, identify the exact theorem assumptions, unconsumed physical-integral certificate and Kloosterman inputs; authenticate the long-gap proof and publication metadata pins separately.
- For #788, compare the finite theorem and zeta theorem types, especially `hRvM` and `hPC`, and distinguish analytic hypotheses from logical axioms.
- For #789, authenticate the exact v1 paper, revisions and any published cell certificates. A proof objection is version-specific.
- Flag source drift: the older PR bodies of #786/#777/#778 and later #790/#793 records contained SHAs different from their actual returned heads. The present ledger deliberately uses specific historical source pins rather than an assumed current head.

## 6. Publication status and next reviewer action

The four requested files are present in this local preliminary package. No own-branch commit, review PR number or remote head is asserted. Tool responses were not inspectable, so a publication receipt cannot be fabricated. The full assigned audit remains incomplete for the omissions in REPORT.md.

A subsequent session must authenticate these pins, complete the missing baseline/programme/import inspections, then publish on a separate `review/A/...` branch. It must not change main or any research branch. The final review PR should name the exact inspected-source census and exact review head, and the integrator should reconcile differences with B/C rather than infer agreement.
