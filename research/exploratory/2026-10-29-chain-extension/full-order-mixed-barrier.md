# Mixed witnesses do not improve the full-order scalar bound

This is a conditional scalar limitation, not an arithmetic counterexample. Suppose for normalized squarefree-column polynomials the row second moment is `≪X^ε(X+X^c Q)` with fixed `1/2≤c<1`, and the same bound holds for ordinary blocks by the qv² decomposition. Multiplying an inverse and ordinary block and repeating that decomposition with divisor-bounded coefficients also gives

    Σ_g |M_r S_m|² ≪ X^ε [X+X^(c+r+m)].

The proof is identical to the [cubic mixed moment](../2026-10-29-mixed-detector-moment/README.md): the inner squarefree coefficient mass at fixed v is `≪X^ε/(Nv)²`, and the ideal sums `Σ1/Nv` and `Σ1/(Nv)²` cost respectively a logarithm and a constant. Source masks, common finite-ray classes and common-profile Sobolev assumptions must still be verified in each application.

Put `f(x)=max(1,c+x)−δx`. For detector parameters t>1/2, a saturated witness then has count exponent bounded by `min{f(r),f(m),f(r+m)}`. For the full-order family with c≥3/4 and δ>2c−1, the previous optimum `R=f(1/2)=c+1/2−δ/2` cannot improve: for 1/2<t≤1 take r=m=1/2, which is feasible and has f(1)>f(1/2)=R; for t≥1 take r=t,m=0, where `min{f(t),1}≥R`. This gives a lower bound on the **scalar relaxation**, while the two individual moments already attain R up to fixed losses. Thus the mixed convolution moment adds no improvement, even though it is a valid extra estimate.

For the quartic c=2/3 case and δ≤2/3 the same balanced witness gives the first-branch barrier. For δ≥2/3 put `t₀=2/[3(2−δ)]`, `R=1−δt₀/2=c+(1−δ)t₀`. When `t₀/2≤t≤t₀`, the feasible point `r=m=t₀/2` has all three exponents equal R. For `t<t₀/2`, use r=t,m=0 to obtain a value at least R; for t≥t₀ use the same point and the increasing upper face. Hence the mixed moment alone also leaves the quartic minimax unchanged. These are feasible scalar witnesses, not asserted actual rows or zeros.
