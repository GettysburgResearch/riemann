# T-97101 — Parity-contractive annular Mellin–Landau RH candidate

**Status:** candidate complete unconditional RH proof proposal; independent reconstruction required.  
**Depends on:** `T-97100` and the fixed-row Mellin transform of PR #547.  
**RH is not treated as established by publication.**

The Mellin transform of the nonnegative scalar kernel is

\[
\int_1^\infty\mathcal A_X X^{-s-1}\,dX
=(1-4^{-s})\left[
\frac6{s^2}-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}
\right],
\qquad z=s+\frac12.
\]

The factor `1-4^{-s}` has no zero in `Re s>0`. The finite numerator vanishes only when `2^{-z}=1` or `2^{-z}=2`, which force `Re z=0` or `Re z=-1`; neither can cancel a nontrivial zero in `0<Re z<1`.

Landau's real-abscissa theorem applied to the nonnegative kernel therefore gives the proposed conclusion `RH`.

Immediate review order:

1. reconstruct the complete `P_61` bias certificate in `L-97100`;
2. check the signed/unsigned source covariance and current formulas;
3. audit one-use first ownership and terminal low-child recombination;
4. verify the fixed-row Mellin transform and Landau hypotheses.
