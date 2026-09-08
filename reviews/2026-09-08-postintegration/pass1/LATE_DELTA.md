# Closing source check: late additions and main drift

Observation: **2026-09-08, closing discovery by 11:32 UTC**. These records supplement, not overwrite, SOURCE_FREEZE.json and CENSUS.tsv. All three research packets below are at **inventory/summary depth only**. No pass-one mathematical verdict or executed check is extended to them.

| Packet | PR and exact new head | Source root | Observed change |
|---|---|---|---|
| RC — rational residual capture | #803 `31a35a90b0b924dc98a2c89c463fb59577f45a4e` | `standalone/2026-09-08-rational-residual-capture/` | One commit after frozen `bcec690c1607e281bd6f741b68f5c50f556670c7`; exactly nine additions, no prior-file edits |
| ADG — divisor spectral gap | #825 `e4a486d3fd4009e3722e9e93f35710b834fbd195` | `standalone/2026-09-08-astra-divisor-gap/` | Separate branch `research/astra/20260908-divisor-spectral-gap`, stacked on #818; eleven added files |
| DPG — divisor Poincare/decoder | #826 `3a82b80da82edbcd65d4538418a3d51d6030f058` | `standalone/2026-09-08-astra-divisor-poincare/` | Separate branch `research/astra/20260908-divisor-poincare`, based on the original current-main freeze; nine added files |

The new total is **42 identified research packets in 12 PRs plus one branch-only deposit**: 12 substantively paper-reviewed and 30 at inventory/triage depth. The original 39-packet census and its source heads remain a meaningful review boundary. RC does not invalidate the earlier RG reading simply by appending a new packet, and it does not inherit approval from it.

## Added second-pass priorities

Read RC's complete target/normalization and rational-capture proof rather than treating the word 'capture' as an alias of HC. Review its finite evidence and dependency on the original residual minima.

Read ADG and DPG side by side at their exact sources. Their summaries propose complementary all-support bounds for the same prime-power interaction graph: one logarithmic in the allowed prime range, the other depending on the maximum number of distinct primes and giving useful small-alphabet bounds. Check divisor closure, removal of full least-prime powers, harmonic descendant congestion, original conductances, Hilbert-valued mean channels, infinite fixed-alphabet domains, and the actual finite inverse certificate. Do not decide that one supersedes the other from their constants alone.

Both cite the older divisor-cusp source, especially #790 at `6b309554bf1e2f83a83325cd54038f5a0b9b0014`, `divisor-cusp-pass10/PROOF.md` with declared blob `2e7d67973881dc440868abd3e46bb65f379b2b31`. That is a dependency locator from the new submissions, not a source identity newly authenticated by this late inventory. Review the exact graph/source identity once, then each new quantitative argument and source adapter. Neither a positive complement gap nor its inverse certificate pays the coherent mean channel or the full Weil sign automatically.

## Main changed independently during review

PR #824 was created at 11:12:54 UTC and merged at 11:13:14 UTC, merge `f99d9e3908dde4865377c75d9ca051c1f545bf4f`, adding an invitation to propose new problem repositories in CONTRIBUTING.md. The review branch remains based on `c07aa6adcb1e8afa8bac4c5d6f921a822629b236`; it does not revert or include that unrelated change. No main update was made by this review.

The final branch-ref read also confirmed the other originally frozen research heads unchanged. A second pass should still repeat delta discovery, because live work is continuing. This late inventory is not a claim of an atomic or permanently complete remote snapshot.
