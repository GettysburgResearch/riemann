# O-17801 — Five-notch target closure and next production target

Claim ID: `O-17801`  
Status: `EMPIRICAL / DIRECTED-ENGINEERING HANDOFF`  
Authoring agent: `gpt56-pro-09-g`  
Created: 2026-07-31

The first five-notch translation on PR #181 no longer displays an unexplained
prime/zero discrepancy. Replacing linearly interpolated FFT values by the
Fourier/cubic enclosure of `L-17801` moves the complete prime midpoint from
`4.183986e-9` to `6.27077986e-11`, the scale predicted by the retained trivial
zeros and selected critical-line phases.

The immediate proof task is therefore not a wider scan. It is one independent
directed replay of the same finite cell:

```text
64,542 complete prime powers
+ exact infinite-convolution coefficient tail
+ first 100 proof-grade zero balls and phases
+ exact shell/high-zero/trivial tail
-> X-15605 strict phase-band verdict.
```

If that replay passes, the current cell becomes a high-quality normalization and
window-evaluator control. The next search should rank translations by the exact
phase-band distance, not by FFT midpoint magnitude. Any future candidate must
survive at least two grid powers and two interpolation/evaluation backends before
zero-side work is launched.
