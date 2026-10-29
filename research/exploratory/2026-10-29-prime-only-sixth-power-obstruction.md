# Prime-only Möbius columns saturate the sixth-power sector

**Status.** This is an unconditional elementary lower bound for a restricted coefficient vector. It is a counterexample to uniform bounds based only on the Möbius sign on individual columns, coprimality or auxiliary-gcd projector recombination. It is not a lower bound for the complete Möbius polynomial, a localization to the long-dual wedge, or a disproof of the proposed signed cancellation.

Work over E=Q(ω) with the fixed finite good set S. Let P=Y^(6/5), and choose a fixed nonnegative smooth compact-annular W that is positive on a nonempty interval. Restrict the original Möbius column to good prime ideals p in one fixed admissible finite ray sector, with W(Np/P)>0. Define

    M_u^prime = P^(−1/2) Σ_{p good prime} μ(p) χ_p(u) W(Np/P).

The original zero extensions are used. For all sufficiently large Y, every such p has Np>Y. Hence for each good ideal v with Nv≤Y^(1/6) and u=v⁶, χ_p(u)=χ_p(v)^6=1: the norm condition excludes p|v. The prime ideal theorem in a fixed ray sector gives

    |M_(v⁶)^prime| ≫ P^(1/2)/log P.                           (1)

Fixed-field ideal counting gives ≫Y^(1/6) distinct good ideals v in any fixed positive-width norm annulus at this scale. Thus even restricting the outer sum to sixth powers in a fixed row annulus gives

    Σ_{Nu≤Y} |M_u^prime|² ≫ Y^(1/6)P/(log P)²
                          = Y^(41/30)/(log Y)².               (2)

The same conclusion holds for an annular row weight bounded below on a positive interval: choose Nv in the corresponding sixth-root annulus. If the physical normalization uses primary generators, E is a PID and one fixes one generator per ideal; unit-sector restrictions cost only a fixed finite partition. No particular phase of a Gauss sum is involved.

The diagonal of the expanded square is at most

    Σ_{Nu≤Y} P^(−1) Σ_p |W(Np/P)|² ≪ Y/log P.                 (3)

The offdiagonal contribution is real by pairing (p,q) with (q,p), so (2)–(3) imply it is ≫Y^(41/30)/(log Y)². For each distinct prime pair p,q their common gcd is the unit ideal. Consequently, in any exact auxiliary expansion of the coprimality projector `Σ_{g|(p,q)} μ(g)`, the only term is g=(1); summing the complete signed projector does not itself save this prime-pair contribution. This yields a concrete obstruction to a power saving derived solely from the projector or from an estimate that is required to hold for every restricted subvector of the original Möbius coefficients.

The full Möbius polynomial contains composite columns, and its square has prime–composite and composite–composite cross terms. Those terms can cancel the prime–prime offdiagonal; the positive full energy does not dominate the energy of a partial column sum. Moreover (2) does not show that the large contribution lies in a specified dual-frequency band such as H>Y^(63/50). A successful 125/144 route may use those coupled cancellations or additional genuine arithmetic structure. Any such argument must preserve the complete coefficient vector until the cancellation is established.

The hypothetical full-vector target at E=21/20 even forces a concrete pointwise cancellation on sixth-power rows in its positive row shell. Let V≥0 be the target's fixed row profile, and fix a compact positive-width subannulus on which V≥c₀>0. Assume the weighted full-vector bound `Σ_u V(Nu/Y)|M_u|²≪_ε Y^(21/20+ε)`. For this calculation use all good columns, without the earlier prime-sector restriction, and put

    A(P)=Σ_{p good prime} W(Np/P),
    C_v(P)=Σ_{n good composite, (n,v)=1} μ(n) W(Nn/P).

For every v such that Nv⁶/Y lies in the selected subannulus, every prime p in W's support is coprime to v, and the full normalized inverse on u=v⁶ is exactly P^(−1/2)[C_v(P)−A(P)], with the same original masks. Since V≥c₀ there, a single squared row is bounded by c₀⁻¹ times the entire nonnegative moment, implying

    C_v(P)=A(P)+O_ε(P^(15/16+ε))                             (4)

uniformly for all such v. In deriving (4), use `P=Y^(6/5)` and absorb the conversion of ε. The prime ideal theorem gives A(P)≫P/log P, so (4) requires prime–composite cancellation with a relative power saving `O(P^(−1/16+ε) log P)`. This is a necessary consequence of the weighted target, not a proof of it; the statement concerns the unsplit physical inverse and cannot be transferred to an individual dual-frequency block without additional estimates.

There is an even sharper necessary *average* over sixth-power rows. Let 𝒱 range over the ≫Y^(1/6) good ideal roots with Nv⁶/Y in the selected positive subannulus. Summing only their nonnegative contributions to the putative full moment gives

    (1/#𝒱) Σ_{v∈𝒱} |C_v(P)−A(P)|²
       ≪_ε P Y^(21/20−1/6+ε) = P^(125/72+ε).               (5)

Thus its root-mean-square discrepancy is `≪P^(125/144+ε)`, and all but a vanishing proportion of these roots have discrepancy `≪P^(125/144+ε)` after allocating the loss. The exponent 125/144 arises directly from the normalization and the count of sixth-power rows; no zero-free theorem is assumed in this necessity calculation. As before, the moving coprimality mask `(n,v)=1` must be retained, and (5) does not localize to one dual band.

The weaker pointwise condition (4) would already follow from an accepted conventional E-zeta half-plane with boundary 0.8738702. For any fixed a>0.8738702, Mellin inversion on Re s=a bounds the masked sum by `≪P^a (Nv)^ε`: the variable Euler deletion contributes `∏_{p|v}(1−Np^(−a))^(−1)≪(Nv)^ε`, and the fixed-margin reciprocal-zeta bound and Ŵ decay handle the integral. Since Nv≤Y^(1/6), this is stronger than P^(15/16+ε). The RMS condition (5) is stronger: its boundary 125/144≈0.8680556 lies to the left of 0.8738702, so that candidate alone does not yield (5) by this uniform estimate. This distinction is consistent with the [exact sixth-power spectral-growth identity](2026-10-29-mobius-marked-boundary/README.md); it neither proves a failure of the target nor controls the coupled non-power rows.

**Independent review.** Families checked the good sixth-power row count in an annulus, the fixed-ray prime count and zero masks, the diagonal estimate, the unit-gcd conclusion, both cancellation exponents and the existing-candidate Mellin comparison. The review retains the positive-shell hypothesis and the limitations on full Möbius coefficients and individual dual-frequency bands.
