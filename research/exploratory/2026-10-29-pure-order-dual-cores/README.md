# Pure-order dual cores at high frequency

**Status.** This is a source-qualified estimate for sparse restrictions of the physical sextic dual sum, not the complete core or an individual zero-free result. It imports the fixed-sector Poisson/phase/Fourier ledger and masks in [the sixth-power dual note](../2026-10-29-sixth-power-dual-core/README.md), de Faveri's Θ₃ cubic sieve, and the Goldmakher–Louvel quadratic sieve. The recent source and physical-to-FHL matching are not independently established here.

Set E=Q(ω), `P=Y^(6/5)` and localize the original gcd and its divisor to `Nd≈D₀=Y^d`, `Nk≈K=Y^κ`, with `0≤κ≤d` and `d+6κ/5≤7/50`. For a nonempty dual dyad `Nv≈H`, the physical source gives `H≲Y^ε P²K/(YD₀²)`. Write uniquely `v=b a⁶` with sixth-free b and `Nb≈B=Y^b`; a and b may share primes.

The following **restricted-frequency** contributions are each `O(Y^(21/20+ε))`, uniformly over these gcd/divisor and auxiliary-gcd dyads:

* Every square dual core `b=ℓ²` with ℓ cube-free and `11/10≤b≤13/10`.
* Every fourth-power dual core `b=c⁴` with c squarefree and `b≥11/10` in the nonempty dual range.
* Every cube dual core `b=c³` with c squarefree and `b≥11/10` in the nonempty dual range.
* Every fifth-power dual core `b=c⁵` with c squarefree and `b≥11/10` in the nonempty dual range.

At the staged θ moment threshold `E*=19949123/18750000`, the same statements have strict savings for fixed b satisfying respectively

    3175877/3125000 < b < 4324123/3125000       (square core),
    b > 3175877/3125000                           (fourth, cube or fifth core),

with the strict margin absorbing fixed source losses. These are not estimates for arbitrary sixth-free b in the gaps.

## Source characters and common columns

At each fixed original d′, k, auxiliary g and root a, the physical row character is χ_n(b); all factors involving g,k and the a,d′ zero masks are common bounded n-column coefficients. In particular the identity

    χ_n(ℓ²)=χ_n(ℓ)²,   χ_n(c⁴)=χ_n(c)^4,   χ_n(c³)=χ_n(c)^3

holds with zeros even when the root meets a, k or g. Both powers 2 and 4 of the sextic symbol are cubic characters, while power 3 is quadratic. For the compatible primary/FHL presentations, fix the finite reciprocity, unit and ray sectors before the row sum. Then de Faveri's cubic Θ₃ applies to cube-free ℓ rows and squarefree n columns; its operator bound is

    C+D+(CD)^(2/3),                                            (1)

where `C≈B^(1/2)` for b=ℓ² and `C≈B^(1/4)` for b=c⁴, and `D≈P/(D₀G)` is the residual column scale. The special c⁴ core is a subset of square cores, but its smaller row parametrization improves the bound. For b=c³, c must be squarefree because b is sixth-free. Goldmakher–Louvel Corollary 1.2 gives the quadratic bound `C+D` for the squarefree c and n indices, now with `C≈B^(1/3)`; transpose its operator norm if needed. The fixed character power/embedding identification and all zero conventions are a source input, not an inference from conductors alone.

The artificial theta diagonal is not canceled separately inside an auxiliary-g dyad. Bound the full separated square and the diagonal subtracted from it independently; the latter costs the row-count face C times the normalized column ℓ² mass already in (1). Recombine the signed g-projector in the order required by the physical ledger. The same finite profile-seminorm, fixed-ray and source-height qualifications apply to both pieces.

## Norm exponents

The source physical factor after summing d′, k and g is `(Y/P)(D₀/K)`. A dyad `Nb≈B`, `Nv≈H` has `O((H/B)^(1/6+ε))` possible roots a. With the H cutoff, the common prefactor for any of the source row bounds is

    Y^(1/30+ε) D₀^(2/3) K^(−5/6) B^(−1/6).                 (2)

For square cores, (1) gives the three exponent faces

    1/30+2d/3−5κ/6+b/3,
    37/30−d/3−5κ/6−b/6,
    5/6−5κ/6+b/6.                                              (3)

For fourth-power cores, replace b/3 by b/12 in the first face and omit b/6 from the last. For cube cores, the quadratic sieve has only the first two faces, with b/6 in the first. These are upper bounds after dropping harmless negative auxiliary-g exponents; the actual support only shrinks the summed range.

The nonempty dual dyad condition gives `b≤7/5+κ−2d+O(ε)`. Under the small-gcd condition, it bounds the first face by 1/2 for square cores, by 11/50 for fourth cores and by less than 1/3 for cube cores. The second face is at most 21/20 when `b≥11/10`; the square-core third face is at most 21/20 when `b≤13/10`. The other last faces are already below the target.

For the fifth-power core, χ_n(c)^5 is the conjugate sextic source character, with its original zeros. Apply Θ₆ to squarefree c rows of size `C≈B^(1/5)` and squarefree n columns. Its four faces after (2), retaining the negative auxiliary exponent g, are

    1/30+2d/3−5κ/6+b/30,
    37/30−d/3−5κ/6−g−b/6,
    13/30+d/3−5κ/6−g/3,
    31/30−d/6−5κ/6−5g/6−b/10.                              (4)

On the stated domain and b≥11/10 the second is at most 21/20; the first is at most 41/250 by the nonempty-dual condition, and the remaining faces are smaller still. This proves the fourth assertion with the same source/sector qualifications.

Replacing 21/20 by E* and taking the worst case d=κ=0 gives the displayed θ inequalities. They are strict so that all source and height losses can be placed inside the margin. Finite dyadic and ray-sector sums cost only small powers. The bound does not infer cancellation across frequency subsets, omit the original masks or prove the full inverse moment.

**Independent arithmetic review.** Other_families checked the square and fourth cubic character exponents and source normalizations; Families and Other_families checked the fifth-power Θ₆ faces. The physical/analytic source inputs remain unverified externally.
