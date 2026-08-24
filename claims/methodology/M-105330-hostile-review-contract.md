# M-105330 — Hostile review contract

1. Recompute the sign in `partial_alpha(E_alpha'/E_alpha)`.
2. Verify the closed-contour integration by parts and the primitive convention
   `H_ij'=-W^2 phi_i phi_j`.
3. Check the implicit zero velocity `rho'(0)=F/F''`.
4. Reconstruct `E_alpha'/E_alpha=L+L'/(L-alpha)`.
5. Check that shifting alpha replaces the frozen coefficient parameter by
   `L-alpha`, not `L+alpha`.
6. Verify `partial_alpha C(N;L-alpha)|0=-partial_L C` and the sign in the
   T-105320 bridge.
7. Keep the `1/log N` primitive/Hardy division explicit.
8. Do not instantiate one shifted field as a reflection-invariant ZeroConfig;
   use the oriented `+alpha/-alpha` pair.
9. Require a complex-alpha disk and a Cauchy estimate before differentiating
   any error term.
10. Keep `SUEF105330`, the boundary/tail rows, the new proportion, and RH open.
