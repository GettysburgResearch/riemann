# A Hu-conditional angular tail bound for the sextic dual core

**Status.** This partial estimate is conditional on the claimed all-height unitary Weil-L zero-free region `Re s>7/8` in [Hu's preprint](https://hexagonmath.org/2610.00216v1), the standard uniform fixed-field Hecke/Perron consequences stated below, and the October 5 completed-theta mean and cube inversion plus the physical Poisson/Fourier source calibrations cited in [the dual-core note](../2026-10-29-sixth-power-dual-core/README.md). We have not verified Hu's claim or the imported analytic source proofs. The reduction controls only a restricted dual-frequency subrange, not the full inverse moment or an individual zero-free region.

The claimed Hu input is **not** the separately staged finite-order Hecke θ candidate. The cube-inversion multiplier contains the genuinely angular factor `overline(α(c))³`, where `α(c)=c/|c|`; after fixed primary/ray normalization its infinity type is −3. A finite-order-only Hecke zero-free statement does not control it.

## The source theta mean and a conditional prefix bound

Use the notation of [the dual-core note](../2026-10-29-sixth-power-dual-core/README.md). For a squarefree good label f, a row b and a fixed finite ray character ξ, the completed source has

    Ψ_b(n)=ξ(n)χ_n(b)χ_n(f)^4,
    Σ_(Nb≤B)|T_b(Z;f)|² ≪ (BZ Nf)^ε [B+B² Nf/Z].              (1)

The cube inversion is

    P_b(D;f)=Σ_c μ(c) overline(α(c))³ Ψ_b(c)³/Nc
                          · T_b(D/(Nc)³;f).                     (2)

All terms retain their zeros. Since `χ_c(f)^12=1_{(c,f)=1}`, the multiplier of μ(c) is a fixed-infinity-type unitary Hecke character after finite ray-sector reciprocity, times explicit deleted factors at primes dividing bf. Its infinity type is −3 and its primitive conductor has norm `≪_{K,S}Nrad(b)`; the fixed f mask is retained separately. In a fixed field the extra Euler factors have reciprocal size `≪(B Nf)^ε` on any fixed half-plane `Re s≥a>0`.

Assume Hu's claimed unitary zero-free half-plane. For every fixed η>0, standard Hecke functional equations, fixed-strip polynomial growth and the buffered Borel–Carathéodory/three-circles estimate give

    1/L(s,ψ_b) ≪_η [B(2+|Im s|)]^η    (Re s≥7/8+η),           (3)

uniformly for these conductor and fixed infinity-type characters. Here the nonzero angular type rules out a pure norm pole. A Perron contour with polynomial truncation, the ideal divisor bound for coefficients and the finite deletion factors then gives the sharp prefix estimate

    A_b(T):=Σ_(Nc≤T) μ(c) overline(α(c))³ Ψ_b(c)³
       ≪_η (B Nf T)^η T^(7/8+η).                              (4)

The implied constants are uniform in the source row and f within fixed polynomial ranges. The Perron height and the small loss are fixed before X grows; one may place the cutoff between consecutive integral ideal norms. This paragraph is a standard consequence **conditional on the asserted uniform unitary strip and the fixed-sector character identification**; it is not an independent proof of that strip.

The explicit theta coefficients and ideal counting also give uniformly

    |T_b(Z;f)| + |∂_(log Z) T_b(Z;f)| ≪ Z^(1/2+η)              (5)

for Z≥1, with both sides zero or O(1) on bounded/empty scales. Differentiation merely replaces W by a fixed smooth profile of the form `−W/2−xW′`; fixed norm-frequency modes have the usual polynomial seminorm costs. In (2), the index c changes only the scale `D/(Nc)³`: b,f and the common profile do not change with c.

## Partial summation and the averaged gain

Fix C≥1. Weighted Cauchy and (1) bound the short cube-index part in squared ℓ²(b) norm by

    (DBNf)^ε [B+B² Nf C³/D].                                  (6)

For the tail, apply ideal-norm partial summation to (2), with (4) and (5). The weight `(Nc)^(−1)T_b(D/(Nc)³;f)` and its logarithmic derivative are `≪D^(1/2+η)(Nc)^(−5/2+O(η))`. Hence the tail is bounded pointwise by

    ≪ (DBNf)^ε D^(1/2) C^(7/8−5/2),                           (7)

after shrinking preliminary η into ε. Squaring and summing B rows costs `B D C^(−13/4)`. If `B Nf≤D²`, take `C=(D²/(B Nf))^(4/25)`, which lies between 1 and `D^(1/3)`. Balancing (6) and (7) yields

    Σ_(Nb≤B)|P_b(D;f)|²
       ≪ (DBNf)^ε [B+B^(38/25)(Nf)^(13/25)D^(−1/25)].         (8)

When `B Nf>D²`, the direct pointwise trivial estimate gives `≪B D`, and this is at most the second term in (8) because their ratio is `(B Nf/D²)^(13/25)≥1`. Thus (8) is valid throughout the fixed polynomial ranges, without that guard. The use of a=7/8 in the exponents means the elementary fixed-margin argument is run at `a=7/8+η` and η is absorbed in the displayed ε.

## A conditional improvement inside the small-gcd core

In the exact restricted dual-frequency source of the [general d,k core](../2026-10-29-general-dual-core-sieve/README.md), write `D₀=Y^d`, `K=Y^κ`, auxiliary `G=Y^g`, sixth-free dual core `B=Y^b` and `P=Y^(6/5)`. The source label is `f=g k e` after the combined mask expansion, and the row is bk; hence the b-mean uses `B′≈BK`, `Nf≈GK` up to divisor weights, and `D≈P/(D₀G)`. Original zero masks, the χ_e(bk) row multiplier, g coprimalities and fixed sectors are retained exactly as in that note. The source prefactor after H cutoff is `Y^(1/30)D₀^(2/3)K^(−5/6)B^(−1/6)`.

For a divisor `e|rad(a d′)` introduced by the exact combined mask expansion, the actual source label and scale are `f=g k e` and `D′=D/Ne`. The guard `B′Nf≤(D′)²` need not hold uniformly in e, so use the **global** form of (8), including its trivial-bound continuation just proved. After taking the square root for Minkowski and multiplying by the exterior `(Ne)^(−1/2)`, the e-dependent exponent in the nontrivial term is

    −1/2 + 13/50 + 1/50 = −11/50.                              (8a)

Thus its sum over e is `≪(Na Nd′)^ε`; the B′ term gives the same conclusion with `(Ne)^(−1/2)`. No divisor is discarded or assumed to satisfy a scale guard. Once this divisor sum is absorbed, the nontrivial term in (8) gives the exponent

    E = −11/750 + (53/75)d + (181/150)κ
                    + (203/150)b + (14/25)g.                   (9)

The separate B′ term contributes an exponent at most

    1/30 + 2d/3 + κ/6 + 5b/6.                                 (10)

Keep (10) as an independent face; it is not always dominated by (9). In the residual core `d+g+6κ/5≤C`, `0≤κ≤d`, (9) is bounded by

    −11/750 + (287/330)C + (203/150)b,                         (11)

with the d,κ maximum at `d=κ=5C/11`, g=0. At the two thresholds below, the face (10) is strictly smaller than the intended target. Although the base-scale inequality `B′GK≤D²` holds here, it is not needed and does not by itself control `B′GK e≤(D/Ne)²` after the mask expansion.

Thus, conditional on all inputs above, every residual-core dyad with a sixth-free dual-core exponent b in the following ranges is controlled:

* At the `Y^(21/20+ε)` 125/144 target, `b≤7779/11165≈0.69673086`.
* To beat the staged θ threshold `E*=19949123/18750000`, any fixed `b<2504453563/3489062500≈0.71780129` gives a strict margin.

The source full square and its artificial subtracted diagonal are bounded separately as in the [general dual-core note](../2026-10-29-general-dual-core-sieve/README.md); no cancellation of that diagonal is asserted for an isolated g-dyad. There is a strict unhandled complement of these b ranges. Even if Hu's claimed 7/8 strip were assumed, this estimate does not prove the full inverse target or improve an individual ζ zero-free region.

**Independent review.** Amplified_opt checked the angular character and original masks, sharp-prefix/partial-summation conditional reduction, derivative and source-mean exponents, the global large-label continuation, divisor exponent and general-core arithmetic. Root and Families corrected an earlier erroneous attempt to apply the base-scale guard uniformly after the e-expansion. A parallel [independent derivation](../2026-10-29-angular-strip-cube-tail/README.md) records the same assumptions. Neither review verifies Hu’s claimed region or the imported source Poisson/Fourier calibration.

**Independent review.** Other_families checked the angular type and masks, partial-summation tail, balancing, the e-dependent Minkowski loss, the core exponents and both exact cutoffs. This review assumes Hu's claimed unitary strip and the cited source/profile identifications; it does not establish those external inputs.

At the uniform boundary points `d=κ=5C/11, g=0`, the competing Θ₆ `B^(1/3)D^(5/6)` face is above the Hu-conditional theta face by `4799/133980≈.035819` for the 21/20 cutoff and `1381172281/41868750000≈.032988` for the θ cutoff. Thus merely taking the better of these two current **positive** row bounds does not move the uniform b-threshold in a neighborhood of that extremum. This is a scalar method limitation, not a lower bound for the actual signed physical correlation.

Other_families independently checked the conditional angular −3/Perron setup, the differentiated tail, balanced mean, global large-label continuation, `e^(−11/50)` divisor loss and the two cutoffs. This is not a verification of Hu's claimed strip or the imported source theorems.

## General prefix exponent and the remaining large-core barrier

The same calculation works conditionally with any uniform sharp-prefix exponent `a∈[1/2,7/8]`, rather than only 7/8. Put

    α=3/(8−2a).

Partial summation gives tail `D^(1/2) C^(a−5/2)`; after balancing with the unchanged completed-theta short mean and treating the large-label regime trivially, the second mean-square face is

    B^(2−α) (Nf)^(1−α) D^(2α−1).                              (12)

Under the combined e-mask expansion its square root, together with the outer `Ne^(−1/2)`, has e-exponent `(1−3α)/2<0`, so the same divisor-loss argument applies. Inside `d+g+6k/5≤C`, `0≤k≤d`, the maximal exponent contributed by this face is

    1/30 + (6/5)(2α−1) + (115/66−20α/11)C
                                      + (11/6−α)b.            (13)

The g coefficient is `2−3α>0`; after using the core condition, the remaining d,k linear form is maximized at d=k=5C/11. This calculation uses the same fixed physical and source assumptions and treats the BK face separately.

As a hypothetical limiting comparison, even a fully uniform GRH-quality prefix bound `a=1/2+ε` gives only the cutoffs `b≤2433/3245≈.749769` at 21/20 and `b<782027209/1014062500≈.771182` at the θ threshold via this positive tail estimate. The BK face is below the targets there. Thus improving the uniform quadratic-angular strip all the way to 1/2 would still leave a large dual-core complement under this particular positive method; this is a limitation of the method, not an impossibility theorem for GRH or for signed arithmetic cancellation.
