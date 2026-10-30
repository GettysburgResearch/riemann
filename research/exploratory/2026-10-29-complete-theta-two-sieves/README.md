# Complete cube-inversion mean from two theta estimates

**Status.** This is a newly derived, source-qualified restricted dual-slice estimate. It imports the October 5 source's cube inversion and completed-theta mean `prop:R`, de Faveri's Θ₆, and the finite-sector physical Poisson/reciprocity/profile calibration in [the general dual-core ledger](../2026-10-29-general-dual-core-sieve/README.md). These external inputs are not independently established here. The argument does not prove the full source moment or an individual zero-free region. Two independent internal audits are recorded below.

Use the notation of [the quadratic-prefix tail](../2026-10-29-quadratic-sieve-theta-tail/README.md): \(B\) bounds actual sixth-free row labels b, k and f are fixed, and D is the squarefree-theta column scale. The normalized source cube inversion is
\[
 P_b(D;f)=\sum_{Nh\ll D^{1/3}}\frac{a_h(b)}{Nh}\,T_{bk}\!\left(\frac D{(Nh)^3};f\right),\qquad |a_h(b)|\le1,\tag{1}
\]
where all angular phases and zero masks remain in \(a_h\). A finite number of common smooth profiles and finite ray sectors is understood; their norms and derivatives are uniformly bounded by the cited source inputs.

Two completed-theta means are available uniformly in \(X\ge1\):
\[
 \sum_{Nb\ll B}|T_{bk}(X;f)|^2
 \ll (BKFX)^\epsilon\min\left\{BK+\frac{B^2K^2F}{X},\;\Theta_6(B,X)\right\}.\tag{2}
\]
The first is prop:R after enlarging the injective row family \(bk\) to norm \(\ll BK\). For the second, fix the source theta cube index q. Its row factor \(\chi_q(bk)^3\) is a contraction, the squarefree n-polynomial has norm length \(\ll X/(Nq)^3\), and its normalized coefficient mass is \(\ll (Nq)^{-2}\) up to subpowers. Apply Θ₆ to the sixth-free b rows with fixed k,f source masks inside the common n-vector; sum q by row-space Minkowski and the harmonic ideal sum. The q-part, its original zeros, and all finite-sector phases are retained. The same profile uniformity applies to the polynomial needed in (1).

Weighted Cauchy in (1), followed by (2) on each dyadic h-scale, gives
\[
 \sum_b|P_b(D;f)|^2\ll (BDKF)^\epsilon
 \sup_{1\le X\ll D}\min\left\{BK+\frac{B^2K^2F}{X},\ \Theta_6(B,X)\right\}.\tag{3}
\]
Indeed \(\sum_{Nh\ll D^{1/3}}1/Nh\ll\log D\), and the weighted count on each h-dyad is \(O(1)\); the number of dyads is logarithmic. The source profile may vary with h only through its common norm scale, so (2) is applied after fixing h, with a uniform seminorm bound. There is no Möbius cancellation assumed in (3).

For the physical mask divisor e, put \(D_e=D/Ne\), \(F_e=FNe\), and take the exterior squared factor \((Ne)^{-1}\). At cube scale h set \(X=D_e/(Nh)^3=D/H_0^3\), where \(H_0=(Ne)^{1/3}Nh\). The first branch of (2), after exterior weight, is bounded by
\[
 BK+\frac{B^2K^2F}{D}H_0^3=BK+\frac{B^2K^2F}{X};
\]
its Θ₆ branch is also at most \(\Theta_6(B,X)\). The admissible X range is contained in \([1,O(D)]\), including all e, and the number of allowed e is a divisor-bound subpower. Thus the same (3) applies after the entire e-sum by Minkowski. Empty or bounded endpoint scales are absorbed in the fixed constants. The artificial diagonal in the physical g-localized expression is budgeted separately, as in the source ledger.

## Exact scalar consequence

For \(D=Y^\Delta\), \(\Delta=6/5-d-g\), \(B=Y^b\), \(K=Y^\kappa\), \(F=Y^{g+\kappa}\), the physical root-counting prefactor is \(Y^{p_0}\), where
\[
 p_0=\frac1{30}+\frac{2d}{3}-\frac{5\kappa}{6}-\frac b6.\tag{4}
\]
For \(x=\log_Y X\in[0,\Delta]\), the resulting exponent is
\[
 p_0+\min\!\left\{\max(b+\kappa,2b+3\kappa+g-x),\
 \max\left(b,x,\frac{5b}{6}+\frac x3,\frac b3+\frac{5x}{6}\right)\right\}.\tag{5}
\]
Maximize over \(d,g,\kappa\ge0\), \(\kappa\le d\), and \(d+g+6\kappa/5\le C_{\rm core}\). The [rational dual checker](check.py) proves these two uniform upper bounds, by checking exact nonnegative dual multipliers for all eight combinations of source and Θ₆ faces:

| \(C_{\rm core}\) | \(b_{\max}\) | exponent upper bound |
|---|---|---|
| \(7/50\) | \(554/575\) | \(21/20\) |
| \(1925877/15625000\) | \(88917107/89843750\) | \(19949123/18750000\) |

For the increment \(b\ge23/25\), every source face in (5) increases with b after adding \(p_0\). The Θ₆ x-face can be discarded since \(b\ge x/2\) throughout \(0\le x\le\Delta\le6/5\), so \(x\le b/3+5x/6\); the remaining Θ faces also increase with b. Therefore each endpoint check covers the entire lower increment. Previously reviewed bounds cover smaller b. The first row gives the target \(Y^{21/20+\epsilon}\). The second gives a strict saving below the current θ threshold for any fixed b strictly below its endpoint, with epsilon chosen after the margin.

The checker uses floating optimization only to propose multipliers; it verifies positivity and the full dual identities over the rationals. Its output is an exact upper certificate. No conclusion is asserted for the remaining high-dual complement.

**Independent review.** High_match and Other_families independently checked the fixed-q Θ₆ mean, scale-wise weighted Cauchy, arbitrary-e normalization, monotonicity and exact rational dual checker. The named external source and physical calibration inputs remain unverified by that internal review.
