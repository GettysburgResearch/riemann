# Resume this review without losing the version boundary

This is a continuation guide, not a new workflow or acceptance schema. Keep main's cumulative scientific organization. Do not restore an old main tree from this review branch when eventually preparing integration.

## Immutable anchors

Pass one is the complete directory `reviews/2026-09-08-postintegration/pass1/` at `29d2337255cb467c8d83d070ebe71917d6221c7c`. Its initial census contains 39 packets; its closing late-delta note adds RC and the two divisor packets, for 42. Pass two has [17 watched source records](SOURCE_HEADS.json), [25 file reading records](FILES.tsv), and [12 main-proof coverage rows](COVERAGE.tsv). These are different denominators.

The exact commit and blob on a file record are the reviewed version. An unchanged branch head with unread siblings is **not** complete review. Conversely, when the head advances but a reviewed file's blob is unchanged, preserve that file-level work while checking whether a changed dependency alters its applicability. Do not inherit a verdict through a short claim number alone.

## Next-pass delta procedure

1. Read the current main and the review PR. Record both exact heads. Leave the existing pass-one and pass-two evidence unchanged; append a later pass.
2. Resolve every branch in SOURCE_HEADS.json, repeat dated-ref and updated-PR/issue discovery, and inspect successor/correction comments. Record disappeared branches and new PRs explicitly. Discovery here is not exhaustive over arbitrary unpublished or deleted refs.
3. Fetch the newly observed head to a **separate local ref** and compare against the full reviewed SHA, not the current name of the branch. For example, for #803:

```sh
git fetch origin refs/heads/research/astra/20260906-logarithmic-core-certification
after=$(git rev-parse FETCH_HEAD)
before=31a35a90b0b924dc98a2c89c463fb59577f45a4e
git merge-base --is-ancestor "$before" "$after"
git diff --name-status "$before" "$after"
git diff "$before" "$after" -- standalone/2026-09-08-rational-residual-capture
```

Record the ancestry command's exit status. If it is not an ancestor, do not describe the change as an append-only continuation: compare both full trees, inspect replacements/deletions and shared dependencies, and retain both snapshots. A GitHub three-dot comparison alone can hide changes relative to the exact reviewed tree in a diverged history.

4. Compare each FILES.tsv blob to `git rev-parse "$after:path"`. Preserve unchanged file review with its original dependency conditions. Review changed statements, imported locks, checkers, and result files together; a changed `README` is not evidence that the mathematical source changed, nor the reverse.
5. Mark each new or changed packet as unread, paper-read, code-audited, replayed, repaired, or held. Record consumed bytes before execution and use normal and optimized modes where relevant. Never borrow a run receipt from a neighboring target, norm, cutoff or branch.
6. Use pass-one's queued files even when the current diff is empty. Then issue an integration recommendation only at claim/source scope. An eventual integration branch must start from **then-current main**, not this review branch's old main ancestry.

## Highest-priority queue

**New arrival: #828**, observed at `528b33ac8d57b5a046260ee45d585cd3fe720f4c`, root `standalone/2026-09-08-astra-grounding-capacity/`, stacked on #825. Only its description and announcements were read. Independently check the centered versus anchored constants, fixed-prime tensor assumptions, all-exponent domain, complete subset formula, growing-prime asymptotic, secular equation, and actual logarithmic finite certificates. Its advertised cross-branch synthesis is research, not a reviewer acceptance. No statement from #828 was used as a premise of this pass.

**Unreplayed numerical evidence on paper-reviewed packets:** FR's fixed-horizon ideal/ordinary-compact trial in #812; CD's predecessor finite campaign in #804; RC's three balance-only finite minima in #803; SSQ's actual finite prime-energy prefixes in #818. Keep the stronger or different source/jet requirements apart. WP and IE have now been replayed only at the consumed subsets specified in REPLAY.md; their original whole-package rejection suites remain unrun here.

**The 21 original packets still at triage depth:**

| Source | Packet IDs and exact roots relative to `standalone/` |
|---|---|
| #803, `31a35a90b0b924dc98a2c89c463fb59577f45a4e` | HT `2026-09-06-logarithmic-core/height-transfer-and-prime-squares`; AN `.../annular-scalar-route`; ES `.../euler-tail-stability`; FM `.../fixed-moment-counting-attempt`; PC `.../prime-curvature-and-failure-count`; SS `.../sparse-sign-bootstrap`; MC `.../balanced-mobius-contour`; CR `.../completion-rigidity-review`; PR `.../positive-residual-review`; RN `2026-09-08-residual-normalization-and-minima`. The ellipses in this table refer only to the same `2026-09-06-logarithmic-core` prefix; full paths are preserved in pass1/CENSUS.tsv. |
| #804, `0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad` | DC `2026-09-06-astra-domain-cutoff`; MW `2026-09-06-astra-mobius-work-resonance`. |
| #805, `602d7ddf9dbd2ba79bd6cada149772111ca72150` | DO `2026-09-06-astra-dilation-observability`; BG `2026-09-06-astra-block-gain`; GT `2026-09-06-astra-growth-transfer`; BL `2026-09-06-astra-balanced-lift`; GE `2026-09-06-astra-green-energy`; TE `2026-09-06-astra-terminal-endpoint`; BH `2026-09-07-astra-balanced-hyperbola`; CL `2026-09-07-astra-critical-line-attempt`. |
| #811, `946dedfa3f6ec2d74f3f0f00f9ca511abf9652d7` | EF `2026-09-07-astra-entropy-feedback`. OEC's auxiliary Abel note and EPD/PDS attempt notes also still need full reading, despite their main proofs being covered. |

**Inherited source obligations:** complete the specific LC/CSM/HC source adapters and any all-scale exponent assumptions left in pass one. Preserve classical RH-conditional Cramer input versus unconditional Brun–Titchmarsh. Complete the branch-only spectral packet's publication/source attribution and global compatibility boundaries without rerunning its affine census unnecessarily.

**Older held dependency #790:** this pass's DC10 read and HH5 sections 1–3 do not clear every earlier theta/heat/capture/renormalization layer. The exact DC10 head predates integration and appears in the old census. Reconcile its old review/independence holds, then audit only the remaining necessary adapters or genuinely new deltas. Do not count the same old packet as newly created research merely because a September-8 comment links it.

## Integration interpretation to preserve

WP could replace the statement that an actual length-one sign remains uncertified, but not the all-window target. IE supplies a modest fixed bound for a classical defect, not defect zero. RC controls full finite-support approximation before minimization, not the growing-prefix minimum. ADG and DPG give real graph coercivity and decoding, not the missing coherent-source sign. FC obstructs repeated use of one fixed controller; it does not undo a fixed-horizon improvement. EPD and PDS share one complete physical norm. A future metric/source comparison between that norm, the floor residual and the divisor graph is a **new theorem requiring review**, not editorial integration.
