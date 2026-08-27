# M-105410 — Hostile review contract for second-order tail scaling

Claim ID: `M-105410`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-24  
RH status: **unproved**

## Review order

1. Verify the parity-specific function law and the exact scale `E[V^2]=1`.
2. Verify the cancellation `E[V-1]=-(1/2)E[(V-1)^2]`.
3. Reconstruct the weighted second-order Taylor bound through two `y` derivatives, including the odd `1/V` factor and the off-saddle region.
4. Check the even two-power tilt identity `E_(r+2)[V^(2j)]=E_r[V^(2j+2)]`.
5. Verify the cellwise error `|W_r s_r^n-W s^n|=O(j^(-2n)/(r omega_r))`.
6. Verify the exact beta-tail scaling, Cauchy determinant and Schur constant.
7. Conjugate every source/prefix error by the natural tail diagonal; the worst exponent must be `4k-1`.
8. Keep the quantifier `fixed k` before `r->infinity`.
9. For `L-105412`, retain both open hypotheses: complete sharp residue sign and the scalar zeroth capacity pivot.

## Required firewalls

- The complete terminal matrices converge to zero; they are not claimed PSD at every finite derivative order.
- Fixed-order terminal control is not simultaneous all-order control.
- A high derivative endpoint does not perform the low-order reverse-Rolle descent.
- `ZCAP105412` is an open scalar boundary theorem, not a consequence of safe-axis positivity.
- The moving complex saddle is not used in `T-105410`.

## Replay boundary

The replay authenticates only exact finite Cauchy algebra, the graded congruence, and the abstract overstrong-rate separator. It does not replay the Xi real-saddle estimates, complete critical-tail sign, low-order descent, or RH.

```text
PASS_X_105410_SHARP_TAIL_SCALING
RH_UNPROVEN
```
