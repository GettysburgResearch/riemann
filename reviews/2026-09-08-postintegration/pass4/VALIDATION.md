# Executed numerical review and assurance boundaries

## 1. Consumed source, not a reconstructed filename

Five exact producer/core files are copied under `sources/`. Each copy was matched to the Git blob returned for the pinned source in FILES.tsv before execution. The FR core is the byte-identical reused 160-bit core identified by its current source lock; it is not claimed to be a new arithmetic implementation. No author module was fetched over a runtime import path or executed with repository credentials.

The accepting wrapper authenticates the entire five-file source inventory and each immutable Git blob, compiles the bytes actually consumed, and only then calls the fixed producer. It requires no external library. This is a numerical reconstruction, not a proof-kernel verification of the analytic manuscript.

| Selected replay | Executed function | Finite coverage | Complete future/remainder |
|---|---|---|---|
| FR | `full_certificate(core)` | 4094 half-cells, degree4, T=log2, x<=2048 | Smooth polynomial plus primitive Bernoulli tail; exact box/truncation output budget |
| CD | `run()` | Eight N values through128; 261881 integrated and255 exact zero cells, x<=32768 | Source Stirling/Bernoulli bound over the whole remaining half-line |
| MW | `compute()` | All65536 events; fifteen checkpoints | Exact stable four-state storage at each stopped input |
| SSQ | `run()` | Seven groups, all integers through16384,1900 primes; six M prefixes through128 | Complete Ei-difference primitive tail; no claim of an infinite coarse-energy tail |

FR's `actual_source` subsection agrees exactly with the current published `verification.json` (blob `bd1d5915847416c22a7daa49046d195441b2081d`). Its full metadata object was authenticated separately; the additional 231 controls were not executed. CD, MW and SSQ full output bytes have the same Git blobs as their current published result files. Only the FR numerical subsection is distributed here, rather than copying an entire unexecuted verification claim.

All four complete selected replays finished normally and under `-O`, with byte-identical mathematical results. EXECUTION.json records hashes and sizes. Their separate original whole-package parser/inventory/rejection suites were not run. The archive does not claim otherwise.

## 2. Mathematical primitive audit

FR retains the exact logarithmic-cell formula for the factorial source. Integrating its all-pass state chain gives polynomials on each half-cell, not sampled quadrature. The smooth infinite tail is integrated with the complete exponential moment recurrence; the periodic-Bernoulli primitive pays the remainder. The compactification bound uses an ordinary box approximate identity and a complete stable input-tail estimate. These are different from declaring a Dirac impulse to be L2 or dropping the source's future.

CD uses a 192-bit dyadic interval type with floor/ceiling operations, integer radicals, atanh logarithms and Machin pi. The finite output is affine on each integer source cell after its exact initial horizon. Its cell antiderivative and the complete tail formula were checked against the manuscript. The error is divided by the ramp target's squared norm2; no factor is borrowed from FR or IE.

MW uses the exact event multiplier `(n-1)/n`, a positive atanh remainder for each logarithmic gap, reciprocal square roots from integer square tests, and outward propagation of all four states. The signed work is evaluated with all cross terms. The future is a positive quadratic storage, not new arithmetic events beyond the cutoff.

SSQ uses the literal counting function including prime2 and Li with lower endpoint2. DLMF's positive Ei series is applied as a difference, so gamma cancels. The full difference tail is bounded by the larger positive tail at a fixed range bound. Squaring an interval crossing zero correctly has lower endpoint zero. The exact weighted sample sum is distinct from an orthogonal mean-square cell projection.

## 3. Different complete MW reconstruction

`independent_mw.py` imports no author code. Euler's linear sieve produces Mobius values through65536 and is checked against the full source's Mobius checksum. Its logarithms sum exact rational atanh terms and round once, retaining the entire positive remainder; the original producer instead rounds retained terms during its loop.

On an interevent gap `delta=log(n/(n-1))`, the actual filter output is `exp(-u)` times a cubic in u. Squaring gives degree6. With `r=(n-1)/n`, its moments are

```
I_0=(1-r*r)/2,
I_k=k I_(k-1)/2-r*r*delta^k/2.
```

All65535 gaps are integrated. The post-checkpoint future uses `integral_0^infinity exp(-2u)u^k du=k!/2^(k+1)`, not the supplied Q or signed-work sum. Known nonnegativity of each exact integral permits replacing a negative interval lower endpoint by zero; upper endpoints are never discarded. At each of fifteen checkpoints the new full/past/future intervals overlap the corresponding authenticated original intervals. The final coarse bounds hold independently. This is a compatibility check plus independent inequalities, not a claim that the tighter original endpoints have been independently tightened again.

Both full reconstruction modes finished with identical output. The number of integrated cells is coverage, not a theorem count, and it must not be added to the author's events as distinct arithmetic sources. Independence of implementation is not evidence of a distinct non-author human identity.

## 4. Actual-CLI controls

`test_mw_original_parser.py` reproduced the original comparison weakness in both modes: pristine input accepted; float/Boolean alias accepted; duplicate-key last-value input accepted; changed numerical endpoint rejected. The stored observations are in `evidence/mw-original-parser.json`. Running that optional diagnostic regenerates that file in place; it is not a mandatory accepting entrypoint and does not modify an author source.

`test_replay.py` invokes the new source-pinned wrapper through subprocesses. In each mode all four pristine paths reconstruct their entire selected mathematical result. Eighteen refusals cover aliases, duplicates, nonfinite/nonobject/truncated/oversized input, missing/changed numeric content, symlink receipts, and changed/missing/extra/symlink source inventories. The changed source is refused before its deliberately failing body can execute. No mutation is counted merely because a fixture was edited; its actual CLI exit is checked. There are no skips on this Linux run.

Pristine receipts always undergo fresh reconstruction. Malformed receipts may reject early on their type/content or source hash. This is explicitly not a claim that every malformed receipt reruns an expensive producer. Someone authorized to edit and reseal the checker can alter its contract; the published Git source identities, rather than an editable JSON flag, bind the selected program.

## 5. Reproduction and packet authentication

Use README.md's commands from this directory. Repeat them with `-O`. The scripts write temporary test fixtures outside the packet; `-B` prevents bytecode deposits. The distributed single mathematical result for each target equals both interpreter-mode outputs.

`verify_packet.py` checks a fixed nonempty file inventory, SHA256SUMS coverage, relative paths, regular-file status, source blobs and the selected evidence hashes. It also checks that the extraction table has45 unique packet rows and the decision table22 unique decisions. This is a byte/structure validator, **not a mathematical acceptance shortcut**. It does not execute the producers or prove an analytic infinite theorem.

A clean ZIP extraction and an add-only temporary-Git patch roundtrip are used for delivery checks; their exact executions and payload tree are recorded outside this self-contained packet in the delivery receipt. The temporary patch repositories include unrelated and earlier-review sentinel files; this is not a full Riemann checkout. No claim of remote publication is made by this file alone; the final PR comment and delivery receipt identify the actual remote commit after it is written and read back.

## 6. Explicit nonclaims

No fresh WP/IE, RN/RC, graph or 4320-row TSR campaign is counted here: their earlier scoped reviewer evidence is inherited. No whole author package is approved just because one selected producer reproduced. No global residual upper estimate, all-window positivity, source-domain completeness, zero census, external historical numerical computation, full repository validation, fresh Lean/comparator/axiom audit, native Windows execution, remote CI or settings change is claimed.

Initial HTTP acquisition failed DNS before receiving source bytes, so the connector-provided source text was copied and matched to exact Git blobs. A requested streaming container session was unsupported before code execution; all successful runs were ordinary completed synchronous commands. Discovery of nonexistent guessed `PROOF.md`/review-guide paths returned404 before the actual paths were located. None of those discovery failures is recorded as a successful numerical run.
