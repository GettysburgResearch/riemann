# The unmarked sextic fourth moment and selected-prime amplitudes

**Status.** Source-qualified reductions and a scalar obstruction, not a new individual zero-free region. The cited Liu moment, de Faveri sieve, fixed-field detector and fixed-sector/FHL matching remain analytical inputs rather than independently proved results. The argument does not show that an actual zero has small prime amplitudes.

Liu [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835), Theorem 12.14 and Remark 12.16, claims for the allowed sextic family over a fixed cyclotomic F containing μ₁₂ the unmarked ordinary fourth moment `Σ|S_m|⁴≪U^(1+ε)(1+H)^A` for the relevant bounded lengths, excluding the principal inducing character. The z=0 clause does not use its positive-prime-slot zero-free premise. In the corresponding source inverse notation, `Σ|M_r|²≪U^(e(r)+ε)` with `e(r)=max{1,(1+5r)/6}`. One must separately match the chosen ideal-index FHL family to Liu's allowed generators, finite S-unit sectors, original zeros, common profiles and heights. Liu's field hypothesis does not literally include Q(ω), which does not contain μ₄.

For a zero detector bin with δ=2a−1∈(0,5/6), simultaneous witnesses give r≤t, m≤1/2 and r+m≥t. Using only the two unmarked moments, the count exponent is at most

    min{ max[1−δr, 1/6+(5/6−δ)r], 1−2δm }.

Choosing `t=5/(5−2δ)∈[1,3/2]`, the maximum over the true witness region is

    R₀(δ)=(15−16δ)/(15−6δ).                                (1)

Indeed r≥t−1/2≥1/2. For r≤1 the inverse exponent is 1−δr, and the worst intersection with `1−2δ(t−r)` occurs at r=2t/3. For r≥1 the inverse exponent increases, so its endpoint at r=t dominates that part; it equals the crossing exponent by the chosen t. At σ=4/5 this is 9/19. This row count is source-qualified and has no selected-prime lower bound.

It does not improve the already available Xu–Sang selected-bin count merely by taking a minimum. With α=5/6, c=4/9, x∈[0,1/2], write

    D=3−(1+2c)x,  P=(2−2cx)(1−x),
    R_sel=1−δ+(α−δ)δP/[2((α−δ)D+δP)].                       (2)

At x=0, `R_sel=R₀`; and `2D/3−P=4x(11−6x)/27≥0`. Since the correction in (2) increases with P/D, `R_sel≤R₀` throughout this rectangle. Thus adding (1) as a separate unmarked branch does not tighten the selected count. As one concrete first-stage test at θ=4369347/5000000, ℓ=4(11/12−θ), b=173/2000, δ=23/50 and x=1/2, the selected bound is 929/1550, whereas (1) is 191/306; the conditional moderate-contour exponent is positive `463835687/104625000000`. This is a blockage for that precise substitution and geometry, not a proof that other methods or source131 cannot improve.

## Why a prime spike is an additional statement

For a fixed n≥3, take all good n-free FHL row labels Nu≤U and a finite fixed collection of complete smooth prime-slot polynomials Q_i with lengths `P_i=U^(w_i)`, where each `0<w_i≤1/2`. The source Θ_n sieve gives, with arbitrarily small fixed ε,

    Σ_u |Q_i(u)|² ≪ U^(1+ε).                                (3)

The normalized prime coefficient vector has squared mass O(1); each of the source's offdiagonal terms is at most U when `P_i≤U^(1/2)`. Good squarefree labels alone give ≫U distinct rows. For any fixed α₀>0, Chebyshev and the finite union over slots give

    #{u : some |Q_i(u)|>P_i^α₀}
       ≪ Σ_i U^(1−2α₀w_i+ε)=o(U),                          (4)

provided ε is chosen below all finitely many positive margins. Thus a density-one set of rows has every slot amplitude below P_i^α₀. The assumptions allow arbitrary small *positive* bin amplitudes on those rows; they do not prove that any such row has a zero in the detector region. The exceptional zero-bearing rows could lie inside the sparse set omitted in (4).

There is also a direct logical countermodel to deriving a positive amplitude from the moment inequalities alone. Take one abstract row with simultaneous witness values `|M|²=U^(δr)`, `|S|²=U^(δm)`, `r=2t/3`, `m=t/3`, and every Q_i=0; take all other abstract witness values zero. For 1≤t≤3/2 and δ≤1, one has r≤1 and m≤1/2, so the unmarked inverse and fourth moments are ≤U, and every positive-slot marked moment vanishes. The scalar witness inequalities all hold on that one row, while its selected amplitude is zero. This is not an example of an actual Hecke zero; it demonstrates that the listed upper moments and witness inequalities do not logically imply a prime spike without an additional arithmetic relation.

An individual-bound improvement therefore needs a new estimate coupling zeros with the actual selected prime sums, or a different physical return argument. An explicit formula or Turán argument would have to produce a lower bound inside the particular short, disjoint source windows and retain all phases and masks; a large prime sum somewhere at an uncontrolled scale is insufficient. The separate all-row inverse target leading to 125/144 has its own [prime/composite cancellation obstruction](2026-10-29-prime-only-sixth-power-obstruction.md); the ordinary fourth moment by itself does not establish that inverse estimate.
