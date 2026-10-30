# Repository overlap and proposed next tasks

Snapshot date: 30 October 2026. Base main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

The audit read the current entrypoint, scientific status, open cuts, relevant integrated result descriptions, the 40 most recent returned PR records, changed-file lists for eight selected October PRs, and representative source reports. This is targeted deduplication, not an exhaustive review of every branch or every proof.

## Exact current overlap

| Existing work | Source and observed scope | Consequence for this pass |
|---|---|---|
| Latest family-density and formal candidate work | [PR #1023](https://github.com/GettysburgResearch/riemann/pull/1023) at `a63f134369f4ccccb7d18fa2e6c5c9625db735ca`. Read `research/reports/direct-nfree-density.md`, the return-retune README, Arvi-return source history, the Hu numerator interface, and selected literature audits. | Preserve its source-qualified density results; the new tracker L01 takes priority over its `0.8738694` scalar candidate. Those are different result types. |
| Hardy–Littlewood–Chowla transfer | [PR #1022](https://github.com/GettysburgResearch/riemann/pull/1022) at `1bc2998f8cb72d3b3f2cc3f7974fbdc44f18cefc`. The source list already identifies Lü–Wang–Wu arXiv:2610.20242v1. Its thin-band large-value estimate remains open. | L19 is a known import, not a rediscovery; no growing-family power saving follows from a fixed-shift asymptotic alone. |
| Signed spectral selector and native moments | [PR #1021](https://github.com/GettysburgResearch/riemann/pull/1021) at `a9a19340d276ecf9a34c1f7aca0621c3524cfc0c`. Sources already include Connes–van Suijlekom 2511.23257v1, Connes–Consani–Moscovici 2511.22755v1, Suzuki 2606.09096v1, and Liu v1. | L02 is a revision refresh. L03 and L13 offer different positivity inputs, requiring an explicit source adapter. |
| Structured cubic/sextic moments | [PR #1020](https://github.com/GettysburgResearch/riemann/pull/1020) at `c690f96fe6876f945398b3e2779810c563a64743`. The proposed full inverse consumer and large-core complement are still open. | Compare L01's selected rows and its coefficient restrictions with the exact missing operator, rather than importing a numerical endpoint alone. |
| Actual Möbius projection | [PR #1019](https://github.com/GettysburgResearch/riemann/pull/1019) at `3bcc1daaeb51c71cb2785b9744cde0d641f68f4c`. The orthogonal complement remains unbounded at the desired strength. | An average, a projection estimate, or a new density theorem does not itself control that complement. |
| Weil-resolvent packet | [PR #1017](https://github.com/GettysburgResearch/riemann/pull/1017) at `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`. Spectral identification and cofinal convergence remain unresolved. | Finite-window L13 can be an audit/benchmark target; it does not supply all-window positivity. |
| Original all-field Liu import | [PR #1009](https://github.com/GettysburgResearch/riemann/pull/1009) at `d8e93ba4ab4dc593711c791ce3a002cb5d4796af`. Read `standalone/2026-10-20-liu-all-field-artin-and-barrier/liu_source_audit.md`, which explicitly pins v1. | Keep that historical audit intact. Add the v2 comparison separately and recheck theorem numbering before citing it. |
| Qualitative log-concavity obstruction | In PR #1023, `reports/2026-10-28-log-concave-countermodel.md` constructs a positive symmetric log-concave kernel with off-line transform zeros. | This does not refute Sra's source-specific reciprocal-density PF result. The objects and hypotheses differ. It does block an unjustified generic log-concavity-to-RH shortcut. |

The PRs above were open drafts when observed. Their own review and hypothesis qualifications remain in force. The snapshot does not adjudicate their proofs or integrate them.

## Priority 1: use the current external Dirichlet benchmark

**Task:** reproduce the upstream L01 canonical theorem at its pinned source, then write a mathematical map from its new selected-norm estimate to our inverse-moment notation.

Suggested bounded deliverable:

- Identify the selected row condition, the exact coefficient vector, and where the moment estimate is applied.
- Reconcile prime-slot masses, sixth-root classes, masks, conductor conventions, reflection, and endpoint strictness.
- Compare the selected norm with the missing full inverse operator in #1020 and the complementary projection in #1019.
- State explicitly what is available only for Dirichlet functions and what would be needed to transfer it to general finite-order Hecke families.
- Retain the existing #1023 proofs and certificates as historical work; avoid optimizing a superseded candidate.

**Acceptance condition:** an exact-source replay and a source-to-source lemma map, or the first explicit mismatch. Merely copying the endpoint or its standard-axiom list is not the adapter.

The scalar difference from our #1023 candidate is
$0.8738694-0.87341198=0.00045742$. This comparison is arithmetic, not a statement that the two proofs have identical analytic scope.

## Priority 2: audit the newly explicit moment uniformity

L02 directly intersects the inherited source contract. Compare v1 and v2 where the transformed norms, weighted integrations and finite-width induction are used. The relevant question is whether the exact row-dependent coefficients and parameter ranges needed here are within the printed source.

Build a short interface table with:

| Required datum | What the adapter must retain |
|---|---|
| Arithmetic family | Base field, fixed character, ramification, primitive/imprimitive convention |
| Coefficients | Original signed coefficients; independent versus coupled profiles |
| Norm scales | Actual transformed scales, bounded/subunit ranges, conductor deficits |
| Averaging | Physical measure, selected rows, extraction weights and multiplicity |
| Uniformity | Which constants depend on the field, character, order, height and profile derivatives |
| Closure | Induction direction and losses, with no use of the conclusion as an input |

**Acceptance condition:** one reviewed application of the revised source to a current packet, or a documented remaining gap. This is more useful than another free-parameter sweep inside an unchanged estimate system.

## Priority 3: make the positivity comparison source-faithful

L03 is particularly relevant to the project's higher-order xi tests, but a reciprocal-Laplace density is not automatically the theta kernel, a Pick matrix, or the legal resolvent in #1021.

**Task:** write the transform/normalization map, then identify exactly which finite minors or inequalities can be imported. Separate all real locations at bounded order, all orders on a bounded location set, and the all-order/all-location statement.

**Acceptance condition:** one actual source identity or inequality at a stated order and domain. A positive surrogate or a generic symmetric log-concave kernel is insufficient.

A useful compatibility check combines L03's low-height requirements with L14's finite formal theorem, if their zero conventions and normalizations can be matched. Restrict this proposed route to the reciprocal-law/PF2 conclusions and generalized Laguerre inequalities through $|x|\le99.5$ that can use height 100. It cannot discharge the height $3\cdot10^{12}$ input used for PF256. This is a proposed formalization route, not a completed composition.

## Priority 4: test a genuine new analytic input

The large-value/density and exponential-sum sources in L04–L07 are useful only after matching their variables to the target. A density bound with a positive power can still contain a single persistent exceptional member. A short-interval exponential sum with a scalar additive phase is not already a selected character-family estimate. A result assuming RH cannot be fed into an RH proof.

**Task:** choose one candidate source, state the required transfer lemma with all parameter inequalities, and test whether the original theorem's range intersects the unpaid range. Record a failed match as such.

**Acceptance condition:** an explicit nonempty legal parameter regime, or a sharp reason the source cannot help this target. Do not recast an average as individual nonvanishing.

## Priority 5: exploit the arithmetic consequences without overselling them

The exceptional-real-zero and effective class-number sources can strengthen applications of the programme. Their field, discriminant, real-axis and effectivity quantifiers should be compared directly with the Artin/descent notes already in #1009 and #1023.

**Task:** derive one precisely scoped application using the new source as an attributed dependency. Keep this separate from lowering the complex-zero boundary.

## Sources already known and sources not yet usable as theorem inputs

HLC, de Faveri's fixed-order large sieve, Hu's unitary-Weil preprint, and the older Connes/Suzuki papers are already present in the inspected branch sources. They belong in the baseline/overlap ledger.

The closed `0.8392` tracker submission and the autonomous-agent finite-window notes belong on an audit list. Closure of a PR is not a mathematical refutation, and an exact scalar certificate is not proof of its unverified analytic estimates.
