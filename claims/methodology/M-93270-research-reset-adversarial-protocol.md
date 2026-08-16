# M-93270 - Research-reset adversarial protocol for the Peano/Hermite packet

Claim ID: `M-93270`
Status: **METHODOLOGY / REVIEW PROTOCOL**
Created: 2026-08-16

Review the packet in this order:

1. Recompute `D^2 Phi_P / x` and the rational Mellin transform.
2. Expand the factor-64 scale polynomial on each support cell and verify physical nonnegativity.
3. Verify the positive convolution factorization in logarithmic coordinates.
4. Recompute the centered-cubic positive Mellin smoothing identity.
5. Fix the Fourier convention and verify every reflection sign in `L-93272`.
6. Check real-axis nonvanishing of the cubic multiplier and the polynomial reciprocal bound.
7. Verify the exact positive-source curvature countermodel.
8. Verify the Gaussian saddle firewall before accepting any absolute-value heat argument.
9. Treat `SID_0` and `SID_H` as open RH-strength estimates. Reject any proof that imports either under a different name.
10. Re-run the lightweight exact checker and both SHA-256 ledgers.

Immediate rejection tests:

```text
Phi_64 is negative on any support cell;
the log-convolution constant is not 8192;
W_64 cancels an open-strip zero;
H is not Phi_P *_M g with g>=0;
k_C has a real Fourier zero;
A_q loses Schwartz decay;
positive transport is promoted to curvature positivity;
q/4 is claimed below y^2 for y<1/2;
SID_0 or SID_H is called proved without a signed arithmetic argument.
```

The checker authenticates finite algebra and deterministic identities only. It does not authenticate Mellin continuation, the Guinand-Weil formula, the terminal-pair theorem, either producer, or RH.
