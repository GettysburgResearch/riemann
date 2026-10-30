# A conditional angular-strip saving in the cube tail

This is an independent derivation of the same conditional calculation in the [canonical Hu-angular note](../2026-10-29-hu-angular-theta-tail/README.md). The two notes share the unverified source/strip inputs and make no stronger claim by duplication.

**Status: conditional partial estimate, not a zero-free theorem.** The input below is a uniform zero-free/reciprocal estimate for a family with a fixed **nontrivial angular infinity type**. The retuned θ candidate proves a finite-order Hecke statement and does not supply this input. Hu's recent preprint claims a unitary-Weil boundary 7/8 that could supply it if its scope and uniform reciprocal consequences are validated, but that claim has not been independently verified here. The source theta identities, physical Poisson/Fourier calibration and all masks in [the dual-core note](../2026-10-29-general-dual-core-sieve/README.md) are also imported; the large-core complement remains open.

Write E=Q(ω), let ξ be a fixed permitted finite ray character, and let α(h)=h/|h| for the source's fixed primary generator. After finite ray-sector separation, assume that for every fixed ε>0, for good b and squarefree good f in the source's polynomial ranges,

    A_{b,f}(X) := Σ_{Nh≤X} μ_E(h) ᾱ(h)^3 ξ(h)^3
                                  χ_h(b)^3 1_{(h,f)=1}
      ≪ (X Nb Nf)^ε X^(7/8).                                (1)

This is a sharp partial-sum assertion uniform in the moving b,f, in the finitely many relevant sectors and in the fixed profile height orders. The character in h has angular type ᾱ³, together with a quadratic Kummer twist depending on b; it is not a finite-order Hecke character. A sufficient route to (1) is a uniform all-height zero-free region to the right of 7/8 for these unitary Hecke characters, the standard conductor-uniform reciprocal bound at a fixed margin, and truncated Perron with divisor-bounded ideal coefficients. The primes dividing f and b retain their original zero masks; their deleted Euler factors and the fixed ray factors cost `(Nb Nf)^ε`. The source's quadratic reciprocity and primary-generator convention must identify the exact character on ideals. We assume (1) explicitly rather than claiming these ingredients have been proved.

For the source completed theta function T_b(X;f), also assume the elementary differentiated coefficient bound

    |T_b(X;f)| + |X ∂_X T_b(X;f)| ≪ X^(1/2+ε)               (2)

uniformly in these parameters and the fixed profile derivatives, with empty small scales handled by the source support. This follows from its completed coefficient formula and absolute ideal counting if that source formula and its derivative uniformity are granted.

## Cube inversion

The exact source inversion is

    P_b(T;f)=Σ_h μ(h) w_{b,f}(h)/(Nh) · T_b(T/(Nh)³;f),     (3)

where the weight w contains precisely the angular, quadratic and zero-mask factors in (1). For a split C≥1, summation by parts using (1)–(2) gives

    |Σ_{Nh>C} μ(h)w(h)/(Nh) T_b(T/(Nh)³;f)|
       ≪ (BTf)^ε T^(1/2) C^(−13/8).                         (4)

The boundary term has the same exponent. The earlier absolute-value tail was `T^(1/2)C^(−3/2)`; (4) saves C^(1/8). The source completed-theta mean and weighted Cauchy bound the short part, summed over `Nb≤B`, by `B+B² Nf C³/T` up to small powers. Balancing short and squared long tails at `C^(25/4)=T²/(B Nf)` yields

    Σ_{Nb≤B}|P_b(T;f)|²
       ≪ (BT Nf)^ε [B+B^(38/25)(Nf)^(13/25)T^(−1/25)].     (5)

When `B Nf>T²`, use the elementary bound `B T` instead; it is no larger than the second term in (5). A larger strict margin than 7/8 is absorbed by ε after all fixed losses are chosen. The finite ray/primary and profile-height qualifications in (1)–(2) remain essential.

## Restricted physical core

In [the general dual-core notation](../2026-10-29-general-dual-core-sieve/README.md), for `D=P/(D₀G)` and row/label replacements `b↦bk`, `f=gk`, expanding the combined a,d′ masks introduces `e|rad(a d′)`. On every nonzero term `(e,gk)=1`, the exact row factor is `χ_e(bk)χ_e(k)^4`; the first part is a bounded row multiplier after Cauchy and the second is fixed. Minkowski in the b-row norm costs only `(Na Nd′)^ε`: the new second term's square root contributes `(Ne)^(−11/50)` after the exterior `(Ne)^(−1/2)` and the `f↦fe`, `T↦T/Ne` changes.

Thus the theta alternative becomes

    T_theta ≪ BK + B^(38/25)K^(51/25)G^(14/25)(D₀/P)^(1/25). (6)

The root count, physical prefactor, explicit individual diagonal majorant and signed-core caveats are those of the general dual note. Write `D₀=Y^d`, `K=Y^k`, `B=Y^b`, `G=Y^g`, `P=Y^(6/5)`. The second term of (6) yields exponent

    −11/750 + 53d/75 + 181k/150 + 203b/150 + 14g/25.       (7)

Inside `d+g+6k/5≤C`, `0≤k≤d`, the maximum of its d,k,g part is attained at `d=k=5C/11`, `g=0`, giving

    E₂ ≤ −11/750 + 287C/330 + 203b/150.                    (8)

The BK face gives at most `1/30+2C/3+5b/6`, which is below the targets throughout the two numerical domains below. Therefore, conditional on (1)–(2) and the physical inputs, the restricted small sixth-free dual-core portion is controlled through

    b≤7779/11165≈0.69673086               for target 21/20,
    b<2504453563/3489062500≈0.71780129    for the θ threshold. (9)

The inequalities and endpoint maxima are checked exactly in [check.py](check.py). These cutoffs improve the unconditional-source theta-only values 27/40 and 8699123/12500000 under the additional unverified angular-strip input. They neither bound the complement nor imply a strict inverse-moment improvement.

**Independent review.** Families and High_match independently checked the angular weight, source theta derivative, partial summation and balancing algebra, conditional on the uniform Hecke/strip and source-normalization inputs. The canonical note contains the corresponding physical core calculation.
