# ACC29 / SFC30 — anchored composite covariance

**Research draft. Component proofs proposed; independent mathematical review required. The full native high-composite bound and RH are not proved.**

This is an additive packet on draft PR #905, stacked on #904 at frozen parent `879497b4f11be2618c448efc1fa93f69b4022e4c`. It preserves the previous in-chat pass and then develops a separately recorded continuation. No canonical status or predecessor file was changed.

## Read in this order

- [PROOF.md](PROOF.md): ACC29, the preceding chat in full mathematical context. Exact zero anchoring; entire prime-power and powerful-denominator bounds; growing singleton-prime bank; signed prime towers; completion and tail-transform compatibility. First published packet head: `e4498096eb9eeea7147e7128d89ef56fdd34fa0b`.
- [CONTINUATION.md](CONTINUATION.md): SFC30, the subsequent research. Squarefree-supported native completion with cap 16, support <=2Y, and completion-tail energy <=32F_Y. Complete conditional-square and coprime-pair expansion. Full square-amplitude energy <=648 K^4 H_L^6; sparse partner-graph mixed energy <=209952 Delta^2 K^4 H_L^8. NCG28 compatibility is rederived with source constant 192, not silently assumed for the new completion. Continuation proof and replay receipt were present at `4d134953b14d9858051d1be94cbb1b89f82a803a`.

The new square-amplitude sector is not an outer covariance diagonal. It contains a specified contribution at every surviving denominator; the remainder consists of real mixed products. The partner-graph theorem bounds those products whenever the chosen primitive-cofactor graph has bounded degree, including all cofactor gaps <=G. Entire selected functions are squared, with all internal covariance and the whole physical tail retained.

## Replay

Python standard library only. From this directory:

```sh
python verify.py
python -O verify.py
python verify_continuation.py
python -O verify_continuation.py
python verify_continuation.py --mutate
```

The first four commands must succeed; the last command is a deliberate negative control and MUST fail with nonzero exit status. Do not treat its expected failure as a passing research test or disable it.

- [results.json](results.json): 96,190 exact comparisons for ACC29. Both ordinary and optimized runs passed.
- [continuation_results.json](continuation_results.json): 179,941 exact comparisons for SFC30, 82 balanced squarefree sources, finite completion base Y=2,...,255, and native Newton reconstruction through 65,535. Both ordinary and optimized runs passed. Gap-graph extraction is checked against a separate direct coefficient selection; the dilation polynomial is evaluated independently. The final sign mutation is rejected.

Historical rounded chat diagnostics are preserved separately in PROOF.md and are NOT claimed as freshly reproduced or interval-certified. A weak early mutation fixture and its correction are disclosed in CONTINUATION.md. All asymptotic estimates are manuscript proofs, not conclusions from the finite checks.

## What remains open

After the square-amplitude and selected partner-graph components, the remaining coefficient tensor is still a subsum of NCG28's positive threshold majorant. Its low/moving denominator window can retain the prior 4/3 source exponent, with changed constants and all activation corrections. The restricted transformed HIGH remainder is unbounded by this packet. Its dense partner graph cannot be paid by pretending that many individually controlled matchings cost the same as one matching.

No full-checkout validator, remote CI, Lean build, external mathematical review, full predecessor replay, or external novelty certification is claimed. Direct Git failed DNS resolution; publication used authenticated GitHub connector writes, on a separate branch. Main, #904's branch, #848's branch, existing trusted formal files and canonical statuses were not edited.
