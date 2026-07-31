# M-17801 — Schedule line notches by open-strip sensitivity, not zero-side annihilation alone

Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31

For each certified critical-line zero candidate, compare two proof-safe choices:

```text
box-square notch:
  stronger quadratic attenuation at the selected line zero,
  support cost 2r,
  open-strip loss proportional to |rz|^-2;

normalized first difference:
  linear attenuation at the selected line zero,
  support cost r,
  no high-frequency denominator,
  derivative-L1 and shell envelopes unchanged.
```

The scheduler should optimize the directed phase-band objective, not a midpoint
FFT RMS:

1. retain all already certified zero phases exactly;
2. compute the residual shell/high-zero moat for each hybrid filter;
3. compute a lower sensitivity envelope over the unexplored strip above the
   verified height;
4. rank by residual moat divided by the lower open-strip response;
5. run the exact triangular base first when it gives a competitive ratio;
6. preserve all failed, unresolved, or precision-sensitive cells.

A selected-zero phase that is already evaluated exactly need not be annihilated
to quadratic order. This is why normalized differences become useful only after
the phase-aware theorem of PR #181.
