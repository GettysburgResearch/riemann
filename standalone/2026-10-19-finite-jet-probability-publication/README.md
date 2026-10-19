# Publication recovery: finite jets and positive probability countermodels

Date: 19 October 2026.

**Status:** Publication of the complete previously delivered research packet, not a new zero-free theorem or mathematical acceptance. The accompanying draft PR adds nine unchanged original files and this separate publication record. No inherited research, main, or integrated scientific-status file is modified.

The archived README, VALIDATION.md, MANIFEST.json, and checker's hardcoded `github_written: false` retain their historical publication/access labels. This notice supersedes those labels only. Writable connected GitHub actions were available for this recovery. Scientific hypotheses, limitations, and original receipts remain unchanged.

## Read the research

Start with the [original assessment](../2026-10-19-finite-jet-and-probability-models/README.md), then [finite-jet zero insertion](../2026-10-19-finite-jet-and-probability-models/FINITE_JET_ZERO_INSERTION.md) and [positive probability model ambiguity](../2026-10-19-finite-jet-and-probability-models/PROBABILITY_MODEL_AMBIGUITY.md).

The first proposed theorem inserts four prescribed nonreal zeros into a nonsingular fixed-order canonical model, preserving its exact finite jet and the same whole-plane Gaussian envelope. Its exact additional quadratic-node mass is `16 T^2 B^2 / [v^2 (T^2+B^2)^4]`. Its theta application consumes the frozen order-26 source in #1003; the complete source and Gaussian-reserve guard were not independently replayed.

The second proposed theorem builds positive probability laws with exact finite moment repair, all-zero strip confinement, a variance-controlled envelope, calibrated leading xi growth and zero-count terms, and a logarithmic theta-tail rate. Its theta application consumes the order-20 finite Ising realization in #994, not the order-26 polynomial construction. The zero-count error is only `O(sqrt(T))`. The huge model is not numerically instantiated. In Section 4, the phrase "positive random variables" means variables with nonnegative probability laws, not variables taking only nonnegative values: the summands are symmetric signed observables.

Both are auxiliary-model constructions requiring independent mathematical review. They do not exhibit off-critical zeros of zeta, prove RH, refute the cofinal weighted-canonical criterion, or produce a new zeta zero-free boundary. The original notes explicitly acknowledge overlap with #1005's kernel-instability theorem.

The retained research recommendation is to target an estimate using the actual signed Mobius inversion source, a new direct numerator estimate changing the binding comparison, or a source-specific positive construction at unbounded orders. Neither another finite theta match nor removal of auxiliary family variance supplies the missing statement. These are research priorities, not proved critical estimates.

## Exact preservation and fresh execution

The original delivered ZIP has SHA-256 `5aceb990e56378912a93507b3d621db17ddcd3c6bde597ebbb85bad5c32cdc2a`.

All nine original files, totaling 50,545 bytes, are preserved byte-for-byte as ordinary browsable text files. All eight original manifest entries pass. The separately delivered README equals the archive README. The locally reconstructed and remotely created original packet trees both equal `4b28ff479cb91f98bc0e02b1f568ca7307e95bcf`.

Fresh ordinary and optimized isolated Python runs each pass all 25 component predicates, including 15 exact pair geometries and 4,950 integer zero-count comparisons. Both runs have empty stderr. The two new reports are byte-identical to each other and JSON-value-identical to the archived report. They are NOT byte-identical to the archive: only ordering of entries in `file_sha256` differs because the unchanged checker iterates directory entries without sorting. No original report or code was rewritten to conceal that distinction.

Fresh report SHA-256: `6d0de1eb9a151c4f6a168885cfc55ffdb762bc52bef46a1c6be73831141c8e1b`.

All three optimized mutation controls were rerun in separate copies: duplicate active node, negative active node, and oversized reported beta. Each rejected at its designated mathematical predicate. The complete original source, upstream analytic inputs, all-order theorem, independent referee review, proof assistant, whole-repository CI, and remote CI were not run or established by these checks. See [RECOVERY.json](RECOVERY.json) for exact file identities and replay scope.

To run without overwriting the historical report, give an output path outside the original packet, with basename `results.json`:

```sh
mkdir -p /tmp/finite-jet-ordinary /tmp/finite-jet-optimized
python -I -S -B standalone/2026-10-19-finite-jet-and-probability-models/check.py --output /tmp/finite-jet-ordinary/results.json
python -I -S -O -B standalone/2026-10-19-finite-jet-and-probability-models/check.py --output /tmp/finite-jet-optimized/results.json
```

## Repository placement

The new branch is `research/finite-jet-probability-recovery-20261019`, stacked on #1005 at frozen parent `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1`. Its base branch is `research/amplified-boundary-global-attacks-20261018`. This keeps the finite theta dependencies resident and makes the intended diff additive only.

The publication pass observed newer PR metadata through #1007; it does not extend the archived assessment's mathematical review beyond #1005 or import other contributors' later work. No merge or change to main is part of this recovery. The PR and immutable commit are the authoritative remote publication identity.
