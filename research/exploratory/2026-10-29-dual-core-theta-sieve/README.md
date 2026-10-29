# Combining theta and Θ₆ on small dual cores

**Status.** This is a source-qualified partial estimate for the `d=k=1` dual block, not a bound for the whole inverse moment or a new zero-free region. It uses the physical Poisson calibration, source reciprocity, original masks and theta/Fourier inputs stated in [the sixth-power-dual-core note](../2026-10-29-sixth-power-dual-core/README.md), plus de Faveri's printed n-free Θ₆ bound. The physical/source interface and this new combination have not been independently established here.

Let `E=Q(ω)`, `P=Y^(6/5)` and `H≲Y^εP²/Y`. In the fixed-column-ray `d=k=1` dual sum, restrict the dual frequency to `v=b a⁶`, with b sixth-free and `Nb≤B`; first split b into dyads `Nb≈B₀`, then sum the dyads. The original masks and full phases are retained. When

    P^(1/3) ≤ B ≤ P^(5/7),                                    (1)

the absolute contribution of this restricted subset is

    ≪ Y^ε (Y/P)(H/B)^(1/6) P^(5/16)B^(17/16)
     ≪ Y^(49/120+ε) B^(43/48).                               (2)

Consequently, the subset is `≪Y^(21/20+ε)` for `B≤Y^(154/215)` in this range; it is strictly below the staged θ moment threshold `19949123/18750000` for fixed `B≤Y^b`, `b<12292873/16796875≈.73185476`. This extends the earlier thresholds 37/80 and 11824123/25000000 for this same subset. Smaller B below P^(1/3) is already covered by the earlier bound. Large-core frequencies, the other original gcd/divisor blocks and every source-calibration issue remain open.

## The two row bounds

Fix an auxiliary gcd dyad `Ng≈G`, an allowed sixth-power root a and a logarithmically Fourier-separated column profile. Put `D=P/G`. The exact identity

    χ_n(b a⁶)=χ_n(b) 1_{(n,a)=1}                             (3)

holds including shared primes. The outer factor `|χ_g(b)|²1_{(g,a)=1}` is at most one and can be removed after the two original column profiles have been separated and Cauchy has produced a nonnegative b-row square. The earlier source-qualified theta argument gives

    Σ_{Nb≤B} |S_g(D;a,b)|²
       ≪ (P B Na)^ε [B+B^(3/2) G^(1/2)].                   (4)

Alternatively, for each fixed a,g the entire factor `χ_n(g)^4 1_{(n,a)=1}` is part of a common n-column vector; it does not depend on b. The normalized annular vector has squared ℓ² mass `≪P^ε`. Partition the finitely many reciprocity/unit/ray sectors needed to identify the physical row χ_n(b) with a fixed Θ₆ row χ_b(n), including any fixed column phase and the original zero at `(n,b)>1`. De Faveri's Θ₆ theorem, with b sixth-free and n squarefree, gives

    Σ_{Nb≤B} |S_g(D;a,b)|²
       ≪ (P B Na)^ε [B+D+B^(5/6)D^(1/3)
                                       +B^(1/3)D^(5/6)].     (5)

This use of Θ₆ requires the physical-to-FHL reciprocity and finite-sector identification just stated; neither a b-dependent column vector nor deletion of a shared-prime zero is permitted. The fixed a-mask is a column restriction, so no divisor expansion or loss in Na is necessary for (5). The two separated column profiles are handled separately and their mixed product by Cauchy.

## Balancing the auxiliary gcd

Put

    G₀=P^(5/8)B^(−7/8),      K=P^(5/16)B^(17/16).            (6)

Under (1), G₀≥1 and B≤K. For `G≤G₀`, the right side of (4) is `≪K`. For `G≥G₀`, D≤P/G₀ and each of the four terms in (5) is ≤K: the D term uses `B≥P^(1/3)`, while the other elementary endpoint inequalities use `B≤P^(5/7)` (in particular B≤P³ and B≤P⁵). These inequalities are recorded exactly in [check.py](check.py).

The physical coefficient for an Ng≈G dyad is `(Y/P)/G`; summing its O(G) ideals cancels this denominator, and for a dyad `Nb≈B` there are at most `O((H/B)^(1/6+ε))` possible sixth-power roots a, since `Nv≈H`. Enlarge the b-sum to `Nb≤2B` after using this root bound. Taking the better of (4) and (5) on each gcd dyad yields (2) for this b-dyad. Since the B exponent in (2) is positive, summing the b-dyads in the stated range costs only logarithms; the smaller b-dyads are handled by the earlier bound. This is a bound for the specified restriction after exact mask handling; it does not make any assertion about signs or cancellation in the complementary frequencies.

The numerical thresholds follow from solving `49/120+(43/48)b≤21/20` and `<19949123/18750000`; see [check.py](check.py). All exponent losses and Fourier-height costs are fixed before the common small power is selected.
