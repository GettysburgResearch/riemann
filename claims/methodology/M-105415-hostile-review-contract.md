# M-105415 — Hostile review contract for the fixed-width moving-saddle endpoint

Claim ID: `M-105415`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-24  
RH status: **unproved**

Review in this order:

1. Re-derive the first-orbit ratio and all derivative bounds in the strip `|Im u|<=2 delta_0`.
2. Check `(log phi_1)''=-2x-12x/(x-3)^2`, `x=2pi e^(2u)`.
3. Verify `Re S_m''(t+delta)<0` on the complete large shifted ray, including the sign of `Re(1/(t+delta)^2)`.
4. Verify the exact translated ray is `delta+[0,infinity)` and the saddle is at parameter `t=w_m`.
5. Check the compact initial segment and both connectors relative to the moving saddle.
6. Reconstruct the complex Gaussian branch and standardized remainder uniformly for every `m>=M`.
7. Use local `z` disks of radius `asymp 1/w_m`, not a curvature-sized disk, for derivative transfer.
8. Check the phase-cell complement as well as the individual Rouché cells.
9. Retain the `O(T)` correction in the linear phase count; only the exact phase count has `O(1)` endpoint error.

No finite replay authenticates these contour estimates. Until independent review is complete, `L-105413--L-105415` remain proposed complete proofs.

```text
fixed-width high derivative endpoint  PROPOSED COMPLETE / REVIEW REQUIRED
low-order descent                      OPEN
RH                                     UNPROVEN
```
