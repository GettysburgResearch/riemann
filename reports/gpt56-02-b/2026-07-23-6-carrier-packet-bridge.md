# Session report — carrier-packet bridge and wide high-carrier search

Agent: `gpt56-02-b`  
Issue: #6; cross-route handoff to #26  
Branch: `agent/gpt56-02-b/6-global-weil-search`  
Date: 2026-07-23

## Starting hypothesis

A scalar translated Fejer carrier may remain positive even when a coherent
finite packet of nearby translated sinc functions has a negative Weil
direction. The packet should retain compact Fourier support, real-axis
nonnegativity, and a finite prime-power contribution.

## Other work read for inspiration

- PR #23: exact prime-power derivative jumps, moment-neutral suppression, and
  Lerch resummation.
- Issue #26: direct translation of a triangular Fourier kernel to arbitrary
  carrier height.
- PR #24 / Issue #25: complete canonical Robin search and proof-producing
  pruning, retained as the strongest independent arithmetic continuation.
- PR #22: Li-coefficient search through 100,000 with no negative.

The Weil work was selected because the carrier translation directly reaches
the first unverified spectral range with a finite witness.

## New results

### Proved algebraically, submitted as PROPOSED

1. `L-0605`: exact compression of the finite prime matrix into `P_S` and `P_D`.
2. `L-0606`: an explicit nonnegative multi-carrier packet family with compact
   Fourier support and a closed finite prime matrix.
3. The Issue #26 scalar family is the one-carrier case.
4. At lattice carriers, the scalar functional is the D-0001 diagonal divided
   by `2*pi`; the full packet is a sign-congruent principal matrix.
5. `M-0602`: a moment-corrected nonuniform transform with uniform Taylor
   remainder `W exp(eta) eta^(R+1)/(R+1)!`.

### High-precision computational calibration

The scalar archimedean formula from Issue #26 and the independent D-0001
diagonal assembly agreed on ten `(c,n)` controls with maximum observed error
below `7e-53` at 70 decimal digits.

### Empirical search

At `c=10^8`, a wide offset scan around height `3e12` found:

```text
best scalar:        0.5504453445339111...
best 128-packet:    0.24237605690882058...
packet height:      2,999,999,997,911.094474...
```

The packet is substantially stronger but still positive. No `Z-####` object is
created.

## Candidate counterexamples

None.

## Certified computations

None. The Taylor gridding remainder is mathematically bounded, but the complete
matrix evaluation is not interval-certified.

## Failed or limited approaches

- Increasing a contiguous packet from 64 to 96 and then 128 coordinates lowered
  the value only gradually; a positive plateau near `0.242` emerged.
- Arithmetic-progression carriers at `c=10^7` did not improve the coherent
  packet beyond what was explained by sampling a lower scalar carrier.
- Earlier coarse FFT screens were sensitive at the scale of the reported
  margin. M-0602 removes most gridding bias but not floating FFT error.
- No interval/ball backend was available in the execution environment.

## Potential errors

- D-0001 source signs and the RH implication remain externally dependent.
- `__float128` phase reduction and long-double accumulation are not enclosures.
- FFT roundoff is not covered by the Taylor remainder.
- NumPy binary64 diagonalization can lose the sign of an ill-conditioned near-
  null direction.
- The lattice-congruence bridge needs independent block-by-block reconstruction.

## Files changed

- `claims/lemmas/L-0605-prime-source-compression.md`
- `claims/lemmas/L-0606-carrier-packet-bridge.md`
- `claims/methodology/M-0602-moment-corrected-carrier-transform.md`
- `claims/observations/O-0602-carrier-packet-basin.md`
- `experiments/X-0602-carrier-packet-search/`
- this report

The earlier colliding path `L-0601-prime-source-compression.md` is removed.

## Claims affected

- `L-0605` — PROPOSED
- `L-0606` — PROPOSED
- `M-0602` — PROPOSED
- `O-0602` — EMPIRICAL
- `X-0602` — EMPIRICAL

## Recommended next actions

1. Cross-review L-0606 with the Issue #26 author.
2. Implement continuous carrier offsets around the retained basin.
3. Replace the discovery source with complex balls and a certified final direct
   evaluator.
4. Search windowed/prolate and separated-cluster packets.
5. Preserve Issue #25 as the complete arithmetic backstop; its proof-producing
   canonical Robin traversal should proceed independently.

## Organizational improvement ideas

- Reserve claim IDs across stacked branches before authoring; L-0601 collided
  with PR #23 and was moved to L-0605.
- Treat scalar criteria as diagonal restrictions of their natural finite
  quadratic family whenever possible.
- Every fast transform should separate analytic approximation error from
  floating implementation error in machine-readable output.
