# Sixth/third Hölder in the theta cube tail

**Status.** Source-qualified partial control of restricted sextic dual frequencies, not a full inverse-moment estimate or an individual zero-free result. It uses the same GL, Θ₆, completed-theta, physical Poisson, phase/mask and common-profile inputs as [the fourth-tail note](../2026-10-29-fourth-moment-theta-tail/README.md); the recent source proofs and their physical calibration are not independently established here. No Hu zero-free hypothesis is used. An internal independent review is recorded below.

For the source cube tail, let `A_b(x)` be the Möbius/angular/quadratic prefix and `T_{bk}(Z;f)` the completed theta sum, with B actual sixth-free b rows, fixed k of norm ≈K, squarefree label f of norm F and column scale D. The GL sixth moment and theta second/fourth moments give

    Σ_b |A_b(x)|⁶ ≪ (BKFx)^ε [B x³ + B^(1/2)x⁶],                (1)
    Σ_b |T_{bk}(Z;f)|² ≪ (BKFZ)^ε [BK+B²K²F/Z],                (2)
    Σ_b |T_{bk}(Z;f)|⁴ ≪ (BKFZ)^ε
                 [B+Z²+B^(5/6)Z^(2/3)+B^(1/3)Z^(5/3)].          (3)

For (1), cube the common-coefficient prefix, split its column into a squarefree part times a square, split b similarly, and apply GL with fixed-square-part zero masks and divisor-bounded coefficients. For (2), enlarge bk only in the completed-theta `prop:R` row ball. For (3), fix each source theta cube index, remove its bounded b-row character contraction, square the remaining squarefree n-polynomial and apply Θ₆ to its sixth-free b rows; then use ℓ⁴ Minkowski over the cube index. All common k,f multipliers, row-dependent zero masks and differentiated profiles are as in the linked fourth-tail proof.

Hölder gives

    ||A_b(x)T_{bk}(Z;f)||₂
       ≤ [ (Σ|A_b(x)|⁶)(Σ|T_{bk}(Z;f)|²)
                                  (Σ|T_{bk}(Z;f)|⁴) ]^(1/6).   (4)

The same holds with the theta derivative in place of T. Insert `Z=D/x³` into the source cube inversion and use Stieltjes partial summation. There are 16 product monomials from the two, two and four source faces. If the x exponent after taking sixth roots is <1, integrate from cutoff C to `D^(1/3)` and balance the resulting squared tail against `W C³`, `W=B²K²F/D`. At exponent 1 use a logarithm; above 1 use the upper endpoint. Every balance scale is at most D^(1/3). Up to small powers, the resulting 16 B,K,F,D exponent tuples are exactly those printed by [check.py](check.py). Its last column verifies that after taking a square root and multiplying the source mask-divisor factor `(Ne)^(−1/2)`, every moving e exponent is nonpositive.

## Guard and core consequence

In the physical source take `f=gke`, `D′=P/(D₀G Ne)`, where `e|rad(a d′)`, and use the original masks and sector/diagonal order of the linked proof. The balance corresponding to A6's first face, prop:R's nontrivial face and Θ₆'s Z² face is at least one whenever

    D′^(4/3) ≥ B K^(4/3) (Nf)^(2/3).                         (5)

For every mask divisor e, its logarithmic margin is at least

    [17−10b−40d−30g−5κ]/15
       ≥ [17−10b−40C₀]/15,                                    (6)

using `Ne≤Na Nd′`, the nonempty dual/root cutoff and `d+g+6κ/5≤C₀`. It is strictly positive for `C₀≤7/50` and the b ranges below. Thus the largest balance cutoff is ≥1 for every e; no unsupported small-cutoff fallback or e-uniform scale guard is used. All are ≤D′^(1/3).

After taking the square root, summing over e by Minkowski and multiplying the original divisor factor, the 16 e exponents are negative. The common physical prefactor and H cutoff are the same as in the fourth-tail note. Exact linear optimization of the 16 upper-bound faces on `0≤κ≤d`, `d+g+6κ/5≤C₀` is recorded by [check.py](check.py). Each face is maximized at a vertex; the worst b threshold is

    b≤1208/1325≈0.91169811                  for C₀=7/50, E=21/20,
    b<96729607/103515625≈0.93444451         for C₀=1925877/15625000,
                                               E=19949123/18750000.  (7)

The θ inequality is strict to reserve a fixed margin. The limiting face in each case is the product of A6's first face, prop:R's nontrivial face and Θ₆'s `B^(1/3)Z^(5/3)` face. The BK base face and the artificially subtracted diagonal are bounded separately and are below the targets; no local g-dyad diagonal cancellation is assumed. The source dual-core restriction and the fixed original column sector are retained. The complement of (7), all imported physical identities, and the full zero-free objective remain open.

**Independent internal reviews.** High_match and Other_families checked the source/mask decomposition, Hölder interpolation, 16 monomials and upper integration endpoints, each moving-e loss and cutoff guard, and both exact core thresholds. The source Poisson and profile calibrations remain imported.
