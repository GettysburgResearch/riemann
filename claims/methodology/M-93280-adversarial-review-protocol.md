# M-93280 - Adversarial review protocol for the phase-locked/two-row successor

Claim ID: `M-93280`  
Status: **METHODOLOGY / REVIEW PROTOCOL**  
Created: 2026-08-16

Review in this order:

1. Confirm that `L-93270.17` requires multiplication, not addition.
2. Reconstruct the continuous-prime asymptotic in `R-93280` and verify raw
   `SID_H` diverges at `t=1`.
3. Derive the centered measure `d nu_t` and the safe-line Fourier identity.
4. Check the subtraction `-1/(epsilon+i tau)` and the sign convention for
   `-zeta'/zeta`.
5. Verify `P(z)=4(1-4^(s-1))(1-4^(-s))` and every critical-lattice zero.
6. Verify the shift in `widehat B(xi)=widehat A(xi+i/2)` and cancellation orders.
7. Reconstruct the exact centered prime-field identity before applying Cauchy.
8. Treat the norm bound as an inverse theorem only; it does not prove the sign.
9. Recompute `P_2`, `P_3`, and the substitution giving
   `-3(x-1)(x-2)`.
10. Check that the finite Euler factors for primes two and three have no
    open-strip zero.
11. Verify the smooth-reservoir decompositions coefficient by coefficient.
12. Keep `SCID_PL` and `LPTRP_23` visibly open.

Immediate falsifiers:

```text
raw F_C belongs to unweighted L2 for every carrier;
P fails to cancel one critical-boundary zero;
B_(q,m) is not in L2 for m>=1;
P_2 and P_3 have a common open-strip zero;
the large-prime coefficient dictionary fails;
Landau is applied before positivity is proved;
SCID_PL or LPTRP_23 is silently assumed.
```
