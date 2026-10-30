# Collapsed finite-order mixed moments from individual character sums

**Status.** This is an elementary fixed-field consequence of the stated FHL family properties and Wu's subconvex theorem, not a new zero-free region. Its generality is conditional on matching the family presentation, original zeros and finite reciprocity sectors as specified below. It does not improve the cited arbitrary-coefficient sieve in the diagonal range.

Fix n≥3, a number field K containing μ_n, a fixed finite S containing the primes above n and the auxiliary class-representative data, and the FHL/de Faveri characters χ_c on good integral ideals. Assume the precise source family has the standard local property: at every good p, the tame local character of χ_c has exponent v_p(c) modulo n; the good part of the conductor of χ_{c₁}overline(χ_{c₂}) is supported on rad(c₁c₂), with bounded fixed-S conductor. These are the usual properties used in [de Faveri §§2.3–2.5](https://arxiv.org/abs/2610.04045v1); check the actual representatives and masks for any different family. For a squarefree inverse index a and fixed number J of prime indices p_j, form c=a∏p_j. Keep only the source tuples for which c is n-th-power-free, including all collisions and signs that satisfy this condition. A sufficient condition is that no prime occurs among the p_j more than n−2 times. If the prime slots are pairwise disjoint, every such c is n-free for any fixed J.

Source label multiplicativity gives

    χ_a(u) ∏_j χ_{p_j}(u) = χ_c(u),                         (1)

with the original nonunit zeros. If the physical slot is χ_u(p_j) instead, reciprocity first separates finitely many fixed ray sectors; within each sector its phase is absorbed into the relevant prime coefficient. No arithmetic coefficient may depend on the varying row after this separation. For a common normalized inverse polynomial and normalized prime slots, collect all tuples with the same c to obtain a common coefficient b_c. Let L=D∏P_j denote the product of their fixed norm scales. Divisor bounds and a fixed number of slots give

    supp b ⊂ {c good n-free: Nc≪L},
    Σ_c |b_c|² ≪ L^ε,        Σ_c |b_c| ≪ L^(1/2+ε).       (2)

The original Möbius and prime weights are retained inside b_c; (2) does not require cancellation between tuples. More general coefficient sequences satisfying (2) are permitted.

For smooth nonnegative row weight V, or a row ball by dyadic majorants,

    Σ_{u good} V(Nu/Y)|Σ_c b_c χ_c(u)|²
      ≪_{K,S,n,ε} (YL)^ε [Y + Y^(1/2)L^(359/256)].          (3)

The exponent 359/256 uses Wu's Hecke-conductor exponent α=103/512. The result is uniform in a fixed finite number of sectors and fixed profiles. A fixed finite-order row twist common to every term contributes its modulus-squared coprimality mask after opening the square; its fixed conductor can be included in S. Nontrivial changing coefficients require their own uniformity.

**Proof.** If c₁≠c₂ are both n-free, a good prime has distinct exponents in {0,…,n−1}; the quotient character χ_{c₁}overline(χ_{c₂}) has a nontrivial local character there, hence its primitive inducing character is nonprincipal. Its conductor norm is ≪_S N rad(c₁c₂)≪L². The original extra zero masks cost at most (Nc₁c₂)^ε after primitivization. Wu's [Theorem 1.1](https://doi.org/10.1112/S0010437X19007309), followed by smooth Mellin inversion on Re s=1/2+ε, gives the off-diagonal row sum ≪(YL)^εY^(1/2)L^(2α). The diagonal row sum is ≪Y for each c. Opening the square and applying (2) gives (3), since 1+2α=359/256. A fixed ray restriction on u can be expanded into finitely many S-supported characters; it does not remove the nontrivial local component. Row unit sectors, if working with elements instead of ideal rows, must likewise be separated finitely before this argument.

Consequently the off-diagonal is O(Y^(1−κ)) when L≤Y^(128/359−δ), for any fixed δ>0 and sufficiently small losses.

## Comparison and collision limitation

The result does not supersede [de Faveri, Theorem 1.1](https://arxiv.org/abs/2610.04045v1). Its arbitrary-coefficient n-free sieve, combined with the decomposition u=w v^n where w is n-free, implies the all-row bound

    (YL)^ε [Y + L Y^(1/n) + Y^(1−1/n)L^(2/n)
                  + Y^(2/n)L^(1−1/n)].                       (4)

Indeed χ_c(wv^n)=χ_c(w)1_(c,v)=1; for each fixed v the mask restricts the same column vector, and summing the four source terms over Nv≪Y^(1/n) yields (4). For every n≥3, (4) is O(Y^(1+ε)) throughout the larger range L≤Y^(1/2), including the endpoint with small powers. Thus the direct individual-subconvex argument is a simple alternative with no separate inverse-moment hypothesis, but provides no extension of the collapsed diagonal region. For n=6, this is the same combined-length restriction used in the existing [collapsed sextic note](../2026-10-29-sextic-collapsed-moment/README.md).

The n-free hypothesis cannot be imposed after the fact on a product that includes tuples with a prime exponent ≥n: such a tuple is a distinct original contribution, and dropping it can change the squared norm. One must separately estimate all excluded collision strata, or ensure disjoint slots before forming the product. Also, distinct tuples may produce the same c and must be combined before the diagonal/off-diagonal split. Neither (3) nor (4) applies to coefficient vectors that vary arithmetically with the selected row, and neither controls the long source or selected-row range needed for a new fixed zero-free half-plane.

**Independent review:** High_match checked the FHL local nonprincipality and original masks, Wu's exponent, and the four-term all-row sieve comparison. The review is conditional on the stated source-family and finite-sector matching and does not establish a physical selected-row transfer.
