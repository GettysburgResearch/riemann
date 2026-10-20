# Independent review of the opposite-cubic joint mean

20 October 2026. Reviewed `mixed/OPPOSITE_CUBIC_JOINT_MEAN.md` at SHA256
`c97a23c55c79a95b6a61080805617a87396285cbd6738b822cd80728efec92aa`.
This reviewer did not derive that theorem. The inherited finite-profile,
angular-uniformity and large-sieve inputs remain explicit dependencies;
this is not an independent certification of every upstream theorem.

No new-interface defect was found.

1. De Faveri2610.04045v1, Proposition 8.1, has exactly the kernel
   `chi_c(S r^2)` with arbitrary squarefree column coefficients. Its
   parameters are `min(R,H)` and `max(R,H)` in the order used in OC3.
   The unrestricted positive row sets can be restricted to the actual
   squarefree coprime rows. Cubic reciprocity and the finite bad-place
   sectors preserve column independence. The downloaded primary HTML
   has SHA256 `7639be04b4023701377a4a339f2392994afdada8624b8f39e863fab7cbae91d4`.
2. The positive cubic character is a reflection fixed point:
   `bar(chi_S chi_S)=chi_S`. Its two primitive Gauss factors are
   conjugate characters and have product of modulus `NS`. At the
   negative cubic conductor the existing complete Ramanujan/divisor
   identity still applies. The full cube factor is untwisted, including
   its deleted Euler factors, since the new cubic character has cube
   one. Its local ramified ratio and the three-cusp extraction remain
   in the same finite family.
3. The original-side squarefree coefficient norm and all three cube
   exponents are correct. The piecewise powers in the cubic row bound
   are all greater than `2 delta` precisely in the claimed sufficient
   range `delta<2/9`. Continuity at `R=H` makes the split partial
   summation legitimate. Reflection preserves the quadratic-free
   conductor `S` and lowers only `r`, so finite conductor cutoffs close.
4. The inherited scalar cusp extraction has no geometric denominator
   on the preliminary left line. Reflection expands the cusps only on
   the absolute right line. The uniform gamma bound and Gaussian
   interpolation therefore give a finite height-normalized supremum
   before absorption. The cutoff `R^(1/2) H L^2` cancels the reflected
   conductor and height factor. Its largest original height exponent
   is the stated `2-4 delta`.
5. The free-column consumer retains all natural zeros and exact Gauss
   multiplicativity. Dividing by the cube factor on the right line
   uses only absolute Euler convergence. Its balanced optimization at
   `delta=1/6` gives `N^(8/3)`, equivalently `X^(8/9)`, and requires a
   free inner variable. The separate-sieve comparison is now correctly
   restricted to `0<delta<1/6`.
6. The specific rStation5 comparison uses the sextic row `z=S^2`,
   powerful-part norm `H^2`, and restores its `1/R` label normalization.
   It gives `RH+R^2 H^3/D`, whose combination with the original joint
   bound does not recover OC5. This checks that supplied route only;
   it is not a literature-priority conclusion.

The theorem is an auxiliary mean for opposite cubic orientations. It
cannot be substituted into the quadratic/sextic terminal, nor into a
prime-restricted inner series. The stated absence of a new numerical
boundary or RH conclusion is appropriate.
