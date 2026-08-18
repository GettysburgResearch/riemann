# M-97810 — Hostile review protocol

Review in this order.

1. Freeze PR #590 at `223f11259b3e7134f78d6492795e6e94caca8be3`.
2. Verify that `b(Y)` has the two-sided square-root bounds used in R-97810.
3. Check the product-safe cutoff `Y=X^(1/(2(L-1)))` and that every selected
   last-layer child has endpoint at least `sqrt(X)`.
4. Reconstruct the repeated-coordinate bound in (R-97810.7).
5. Check that `L log(2L)=o(Lambda_X)` implies both limits in (R-97810.5).
6. Do not infer positivity at larger depths; the theorem is a no-go only in the
   stated subcritical regime.
7. Reconstruct PR #590's exact largest-prime identity before using L-97810.
8. Check that the Lorenz atom scalar coordinates are nonnegative before setting
   `(r_i-0*t_i)_+=r_i`.
9. Keep root-only `RBLPTE67`, state-wise `BLPTE67`, and all-hinge `CPSL67`
   distinct.
10. Treat `RBLPTE67` and RH as open.
