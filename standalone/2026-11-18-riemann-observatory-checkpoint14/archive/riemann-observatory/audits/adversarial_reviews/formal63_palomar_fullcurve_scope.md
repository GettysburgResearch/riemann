# Cached Lean query of Palomar's exact density curve

17 November 2026. The existing `Solution.olean` was loaded using Lean 4.35.0-rc2 at commit `11acb17ec6b07a8f9e9173e6845197929540936b`, Palomar project pin `ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0` and Mathlib pin `065356127b1dc0016f66b7283ce0ce2c4055aa55`. The one-thread query exited 0 in 26.66 seconds with empty stderr. The module hash matched the previous cached run before and after this query. Both declarations printed exactly `propext`, `Classical.choice` and `Quot.sound` as axiom dependencies. This run queried the already compiled module. The earlier compilation and external kernel replay have separate provenance. [Query source](../../experiments/code/Palomar39FullCurve63Query.lean) · [Raw result and hashes](../../experiments/results/formal63_palomar_fullcurve_query.json) · [Earlier build](../../experiments/results/formal62_palomar39_build.json)

## Statement and boundary scope

`GuthMaynardStatement.full_curve` has \(1/2\le\sigma\le1\) and \(\varepsilon>0\) as inputs before the existential \(C>0\). This gives a constant \(C_{\sigma,\varepsilon}\) for all real heights \(T\ge2\) at that fixed \(\sigma\).

`GuthMaynardStatement.uniform_away_boundary` fixes \(\delta,\varepsilon>0\) before its existential \(C>0\), then quantifies over both \(\sigma\) and \(T\). Thus one \(C_{\delta,\varepsilon}\) works on \([1/2,3/4]\cup[3/4+\delta,1]\) and all real \(T\ge2\). Both bounds use the same exponent \(E(\sigma)+\varepsilon\), where \(E(\sigma)=\texttt{densityCoefficient}(\sigma)(1-\sigma)\). Neither query gives a uniform constant across thresholds that approach the join from its right with a vanishing \(\delta\), or a statement at \(\varepsilon=0\).

The printed coefficient has the closed branch \(9/4\) at \(\sigma=3/4\), so \(E(3/4)=9/16\). The right branch is strictly above \(3/4\) and has \(E(\sigma)=3(1-\sigma)/(2\sigma)\) with right limit \(1/2\) at the join. For \(3/4<\sigma<1\), the gap to the density-hypothesis exponent is

\[
2(1-\sigma)-E(\sigma)=\frac{(1-\sigma)(4\sigma-3)}{2\sigma}>0.
\]

This is the input to the fixed compact slab argument. The branch gain does not apply at the join itself. [Density frontier](density63_combined_frontier.md)

The printed `actualZeroBound` quantifies a finite set of the actual Mathlib zeta zeros with \(0<\Re\rho<1\), \(\Re\rho\ge\sigma\), and \(|\Im\rho|\le T\), and sums their natural analytic orders. Both height signs and equality at the two counting cutoffs are included. Restricting to positive ordinates preserves the upper bound. This query resolves the exact piecewise-curve declarations separately from the earlier query of `global_uniform` with coefficient \(39/17\). [Exact source wrapper](../../sources/palomar_formal62/zeta-density-39-over-17-lean/lean/Solution.lean)
