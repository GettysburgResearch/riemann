# Θ₆ and theta bounds for general small-gcd dual cores

**Status.** A source-qualified restricted-frequency estimate, not a bound for the complete signed inverse moment or an individual zero-free region. It assumes the physical Poisson/sector/Fourier calibrations, theta mean and original zero masks in [the sixth-power dual note](../2026-10-29-sixth-power-dual-core/README.md) and [the low-dual source analysis](../2026-10-29-low-dual-theta-bound.md), and de Faveri's printed Θ₆ sieve. The recent sources and physical-to-FHL identification are not independently established here. The complementary large sixth-free dual cores and other source guards remain open.

In the fixed original column sector put P=Y^(6/5), and localize the original common gcd `Nd≈D₀`, its divisor `Nk≈K`, the auxiliary gcd `Ng≈G`, the dual norm `Nv≈H`, and the sixth-free part of `v=b a⁶` to `Nb≈B`. Assume good squarefree k|d and write d=k d′, with the original masks and finite ray/unit classes retained. The nonnegligible Poisson range has

    H≲Y^ε P² K/(Y D₀²),   D≈P/(D₀G).                         (1)

The physical prefactor after summing `d′`, k and g is `(Y/P)(D₀/K)` up to X^ε factors, and a nonempty b-dyad has at most `(H/B)^(1/6+ε)` choices of a. Thus any valid nonnegative b-row mean bound T supplies

    block ≪ Y^ε (Y/P)(D₀/K)(H/B)^(1/6) T.                    (2)

The g-localized physical offdiagonal is bounded by the **full square plus its subtracted diagonal**. We do not invoke cancellation of an artificial diagonal inside an individual g-dyad. The diagonal is bounded by B times the normalized column coefficient mass, and the B face is included in every T below. The principal pair is absent in the small original-gcd range used here; its separate restoration is not silently dropped in other ranges.

## Two row bounds and masks

After Fourier separation and two-profile Cauchy, the common squarefree n-column carries `χ_n(g)^4 χ_n(k)^5` and the d′ and a masks. For fixed d′, k, g and a, these are common bounded column multipliers, independent of the sixth-free b-row. With the fixed finite reciprocity/ray sectors and original shared-prime zeros, Θ₆ gives

    T_Θ ≪ B+D+B^(5/6)D^(1/3)+B^(1/3)D^(5/6).               (3)

For the theta alternative, rewrite the character product with the exact zero extensions as `χ_n(bk)χ_n(gk)^4`. The source theta mean may then enlarge b k to all rows of norm ≲BK and its squarefree label gk to the corresponding label range. Expanding the combined mask `(n,a d′)=1` over `e|rad(a d′)` and writing n=e n′ retains every natural zero; the e-dependent row factor satisfies

    χ_e(b)χ_e(k)^5 = χ_e(bk)χ_e(k)^4.                         (4)

The first factor is a bounded row multiplier discarded only after positivity, and the second is fixed for e,k. The source f-label is `gke` on the nonzero terms, with its original coprimality enforced by the displayed zero factors. The same cube-inversion/theta argument as in the sixth-power dual note gives

    T_theta ≪ BK + B^(3/2)K² G^(1/2).                         (5)

The two separated column profiles are treated separately, followed by Cauchy. Both (3) and (5) are imported/source-qualified moment bounds; the fixed physical reciprocity sectors and smooth Fourier integrations must be matched exactly.

## Two auxiliary-gcd splits

Put `A=P/D₀`. Since B,K,G≥1, the second term in (5) dominates BK. For the smaller B range, balance the theta term against the elementary b-row bound `BD=BA/G` at

    G₁=(A/(B^(1/2)K²))^(2/3).

If G₁<1, use BD throughout; otherwise use theta for G≤G₁ and BD for G≥G₁. If the split lies beyond the allowed G range, the corresponding one-sided estimate is still smaller. With (1)–(2), this gives the uniform bound

    Y^(13/30+ε) D₀^(1/3)K^(1/2)B^(7/6).                      (6)

For the other range balance (5) with the `B^(1/3)D^(5/6)` face of (3):

    G₀=A^(5/8)K^(−3/2)B^(−7/8),
    T₀=A^(5/16)K^(5/4)B^(17/16).                             (7)

The exact sufficient guards are

    B³≥AK⁴,       B⁷K¹²≤A⁵,       1≤K≤D₀≤P.                 (8)

The first makes the D face of (3) ≤T₀ at G₀; the second makes G₀≥1. The B face is automatic, and the remaining `B^(5/6)D^(1/3)` guard `B≤A³K¹²` follows from the second inequality since A,K≥1. Also G₀≤A. Therefore use theta for G≤G₀ and Θ₆ for G≥G₀, sum gcd dyads, and obtain

    Y^(49/120+ε) D₀^(17/48)K^(5/12)B^(43/48).               (9)

Both bounds retain the dyadic root saving and cover the individual offdiagonal after the explicit diagonal majorant described above. The exact rational exponent and endpoint checks are in [check.py](check.py).

## Uniform small-core consequences

Write `D₀=Y^d`, `K=Y^k`, `B=Y^b`, with `0≤k≤d`. For the 125/144 target, the reviewed residual signed core has `d+g+6k/5<7/50`; hence `d+6k/5<7/50`. For the current θ threshold, replace 7/50 by `1925877/15625000`. The following are uniform in every such d,k and every auxiliary-gcd dyad, with the stated source and mask inputs:

* For the target exponent 21/20, all dyads with `b≤1421/2150≈.66093023` are bounded by `Y^(21/20+ε)`.
* For the θ moment threshold `19949123/18750000`, all dyads with fixed `b<458975011/671875000≈.68312560` have a strict power saving.

To check this, when `3b<6/5−d+4k`, (6) has exponent at most `9/10−d/18+37k/18≤9/10+10C/11`, where C denotes the relevant core constant; this is strictly below either target. Otherwise the first guard of (8) holds, and (9)'s exponent is

    49/120 + (17d+20k+43b)/48.                               (10)

Subject to `k≤d` and `d+6k/5≤C`, the maximum of `17d+20k` is 17C. The stated b cutoffs make (10) at most the corresponding target. The remaining guard `7b+5d+12k≤6` has strict positive margin throughout both domains; [check.py](check.py) verifies its maximum and both low-range margins with exact rational arithmetic. The condition `b≤7/5+k−2d` for nonempty roots is automatic in these numerical domains. Equality in the 125/144 target is allowed with the usual ε losses; the θ comparison needs a fixed strict b margin.

This controls only the restriction to small sixth-free **dual** core b. It neither proves cancellation in the complementary b-range nor removes the need to recombine the signed auxiliary projector and verify the original physical/source Poisson interfaces. No full inverse-moment improvement or zero-free boundary follows from this partial estimate.

## Sharper uniform cutoff using the actual core g-restriction

Inside the residual core itself one may use its additional upper bound on G, rather than the all-G balance above. The second term of (5) dominates BK, so (1)–(2) give, for each g-dyad,

    E(d,k,g,b) ≤ 1/30 + 2d/3 + 7k/6 + 4b/3 + g/2.          (11)

For a core constant C, the actual restriction is `g≤C−d−6k/5`, alongside `0≤k≤d`. Thus

    E ≤ 1/30+C/2+d/6+17k/30+4b/3
      ≤ 1/30+5C/6+4b/3,                                     (12)

because `d+6k/5≤C` and k≤d imply `d/6+17k/30≤C/3`; the maximum occurs at d=k=5C/11 and g=0. Hence, **within the specified signed residual core**, the theta input alone controls the entire dual-core subrange

    b≤27/40=.675                          at exponent 21/20,
    b<8699123/12500000=.69592984          at the θ threshold. (13)

The endpoint comparison, constrained maximum and strict θ margin are checked in [check.py](check.py). These improve the all-G cutoffs in the preceding section, but use the actual g-core restriction and should not be applied to arbitrary g-dyads. The two-source Θ₆ split can still improve individual regions; it does not enlarge this elementary uniform boundary at the above maximizing point. Each individual offdiagonal is controlled by full square plus diagonal as stated, so this subrange calculation does not assume artificial-diagonal cancellation before the auxiliary projector is recombined. The complement, phase/source calibration and full core remain open.

The uniform thresholds in (13) are locally sharp for the **present positive-bound scheme**. At `d=k=5C/11`, g=0 and b equal to its stated threshold, the Θ₆ `B^(1/3)D^(5/6)` face exceeds the theta face by `17/528` for C=7/50 and by `24207893/825000000` for the θ core. For any fixed larger b, taking d=k just inside the strict core boundary leaves both this increasing Θ face and the increasing theta face above the target. This is not a lower bound on the signed physical correlation; cancellation or different arithmetic estimates could improve it.

**Independent review.** Families checked the general phase/mask bookkeeping, both G splits, diagonal majorization, the uniform core guards and the sharpened g-restricted threshold, subject to the physical/reciprocity/Fourier and source assumptions stated above.
