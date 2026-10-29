# Moving-twist pointwise bounds at the theta overlap bottleneck

**Status.** This is a source-range and exponent comparison, not a new theta estimate. The October 5 and September 25 manuscript inputs are not independently verified here. The notation T_h(X), P_h(P), H and P is that of the [averaged-overlap note](2026-10-29-cubic-theta-overlap-average/README.md); the twist h is allowed to move and all original zero masks and fixed sectors are retained.

The [October 5 completed-theta mean](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), Proposition `prop:R` at f=1, claims uniformly on fixed polynomial ranges that

    Σ_{0<Nh≪H} |T_h(X)|² ≪ (HX)^ε [H+H²/X].               (1)

The explicit theta coefficients and ideal counting also give uniformly |T_h(X)|≪X^(1/2+ε). Positivity in (1), with the row ball chosen to contain h, yields the pointwise consequence

    |T_h(X)| ≪ (HX)^ε min{X^(1/2), (H+H²/X)^(1/2)}.      (2)

The saved source powers and fixed profile seminorms are suppressed here; this is not an independently established bound. At X≈√H, the elementary alternative has size H^(1/4), while the pointwise consequence of (1) has size H^(3/4). The two alternatives meet instead at X≈H. Thus (2) gives no pointwise saving where the overlap proof's short-completion and cube-tail bounds balance.

In that proof, X=P/(Nd)³. Weighted Cauchy gives the short part H+H²C³/P and the elementary pointwise bound gives tail HP/C³. Equating the two nontrivial terms sets C³=P/√H and hence X≈√H; their value is H^(3/2). Applying (2) individually to the tail cannot improve this crossover: in the range X≤√H the elementary alternative √X is strictly stronger than the positive-mean pointwise alternative, while for X≫√H the optimized tail has not yet begun. A finer h-dyadic split does not itself change the largest dyad's exponent.

For a useful hypothetical uniform pointwise improvement, suppose at the relevant ranges one had

    |T_h(X)| ≪ (HX)^ε H^κ X^(1/2−η)                       (3)

with fixed η>0, κ≥0, including moving h, all sectors and masks, and the shortened scales in the cube inversion. At the balancing scale X≈√H, the ratio to the known √X bound is H^(κ−η/2). A fixed saving there requires κ<η/2. This is a **necessary comparison for this direct tail substitution**, not a claim that any source supplies (3) or that this condition is necessary for all possible averaging methods.

For context, the September 25 [cubic Gauss first-moment draft](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf), Theorem 2.4, quotes the unconditional Dunn–Radziwiłł level Voronoi formula for a **cube-completed pure cubic Gauss sum** with squarefree level r, giving a main term ≪X^(5/6)(Nr)^(−1/6) and remainder ≪(Nr)^(1/2) times small powers. If one formally normalizes that sum by X^(−1/2), its remainder is (Nr)^(1/2)X^(−1/2), which is X^(1/2) at Nr=X². Thus even that source's error does not provide a pointwise power saving at the relevant crossover.

More importantly, the θ polynomial in the overlap note carries the sextic character χ_n(h), not only a cubic character. Writing χ_n(h)=χ_n(h)^4χ_n(h)^3 leaves a moving quadratic twist in addition to the cubic factor handled by Gauss CRT; the angular factor, cube completion and zeros also require matching. The pure cubic level formula therefore cannot be substituted for T_h(X). The issue is worked out quantitatively in [the cubic–quadratic gap note](2026-10-29-mixed-cubic-quadratic-gap.md). A better pointwise input would need both a conductor exponent satisfying κ<η/2 at the transition and applicability to this coupled sextic presentation; no such theorem was found in this targeted search.
