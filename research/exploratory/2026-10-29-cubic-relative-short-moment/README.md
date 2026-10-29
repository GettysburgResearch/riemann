# A short cubic relative-inverse and prime-mark moment

**Status.** A fixed-field estimate derived from squarefree row averaging, standard Hecke reciprocity and [Han Wu's GL(1) subconvexity theorem](https://arxiv.org/abs/1604.08551), combined with the [sextic prime-mark calculation](../2026-10-29-cubic-inverse-prime-mark/README.md). It does not give an individual zero-free region. Source normalization, ray masks and the quoted classical/Hecke inputs remain explicit; no exhaustive novelty claim is made. Independent review is requested.

Let K=Q(√−3), fix S containing primes over 6 and the reciprocity modulus, and let g run over good squarefree ideals in a fixed principal ray sector. Let χ_g be the corresponding cubic character with its original zero extension. Fix smooth compact-annular V≥0 and W. Put

    R_g(D)=D^(−1/2) ∑_{a,b good} μ(a)μ(b)χ_g(a)overlineχ_g(b) W(N(ab)/D).

This is the inverse block for the **relative** product `L_S(s,χ_g)L_S(s,barχ_g)`; it does not contain the common `1/ζ_{K,S}(s)` factor of the full extension inverse. For every ε>0,

    ∑_g V(Ng/Y)|R_g(D)|²
       ≪_ε (Y + Y^(1/2)D^(359/256))(YD)^ε.                  (1)

Using ordinary convexity instead of Wu gives the weaker exponent `3/2` in place of `359/256`. In particular, for `D=Y^r` and fixed `r<128/359`, the second moment is `≪Y^{1+ε}`. These are fixed-sector bounds; a finite union of sectors costs only a fixed factor.

## Proof

Write `a=h a₀`, `b=h b₀`, with h the gcd. Since μ(a)μ(b) vanishes otherwise, h,a₀,b₀ are squarefree and pairwise coprime. The h-character product is the exact mask `1_((g,h)=1)`, while the remaining cubic character is `χ_g(a₀)overlineχ_g(b₀)`. The pair `(a₀,b₀)` uniquely specifies its good-prime exponent vector modulo three. For a fixed pair, the absolute value of the h-sum is

    ≪ D^(−1/2) #{h : Nh ≪ [D/N(a₀b₀)]^(1/2)}
    ≪ [N(a₀b₀)]^(−1/2).                                     (2)

When the two exponent vectors in the opened square agree, simply bound the nonnegative row sum by O(Y), including both h masks. Summing (2) squared over the squarefree a₀,b₀ gives a diagonal contribution `≪Y(log(2D))^O(1)`.

If the two exponent vectors differ, a good prime has nonzero cubic exponent in their ratio. On each fixed reciprocity sector the row dependence is a nonprincipal finite-order Hecke character, whose conductor is at most a fixed S factor times `N rad(a₀b₀a₀'b₀')≤O(D²)`. Any cancellation at a shared prime leaves its original zero mask, and both h,h′ masks are retained as finite deleted Euler factors; their combined norm is `≪D^O(1)` and contributes `D^ε`. The sector indicator is a finite ray-character expansion and cannot cancel the nontrivial good-prime ramification.

For such a character of conductor Q, the squarefree-row Dirichlet series is `L(s,ξ)/L(2s,ξ²)` times the fixed and deleted Euler factors. Shift the Mellin transform of V to `Re s=1/2+η`. The denominator's reciprocal is absolutely convergent there, and Wu's bound plus fixed-field Phragmén–Lindelöf gives the uniform row correlation

    ≪_ε Y^(1/2+ε) Q^(103/512+ε) D^ε
    ≪_ε Y^(1/2+ε) D^(103/256+ε).                            (3)

The total ℓ¹ mass of the original a,b coefficients is `≪D^(1/2+ε)` by the ideal divisor bound. Multiplying its square by (3), and combining with the diagonal, proves (1). The profile and sector choices are fixed; the vertical growth factor in Wu's hybrid bound is absorbed by the rapid Mellin decay. □

For nonnegative nonzero W, the estimate is nonvacuous at these scales. In the family mean, the diagonal a=b=h contributes a positive constant after normalization: the squarefree h count weighted by `∏_{p|h}Np/(Np+1)` has Dirichlet series `ζ_{K,S}(s)G(s)` with G(1)>0. The other cubic exponent vectors have nonprincipal row averages and give a power-smaller contribution for fixed `r<128/359`. Thus the mean is ≫1 and the second moment is ≫Y, under the same standard input.

## Adding a prime mark

Let Q_P(g) be the compatible sextic prime slot of [the prime-mark note](../2026-10-29-cubic-inverse-prime-mark/README.md), with `Σ|λ_p|²≪1` and common row-independent coefficients. The same prime-square expansion applies to R_g. At distinct slot primes p,q the slot contributes odd sextic exponent at p, while every cubic inverse factor contributes an even exponent. Thus the row character is nonprincipal even if p or q meets an inverse index. Its conductor is `≪P²D²`, and the ℓ¹ masses give

    ∑_g V(Ng/Y)|R_g(D)Q_P(g)|²
       ≤ (∑_p|λ_p|²) ∑_g V(Ng/Y)|R_g(D)|²
          + O_ε(Y^(1/2+ε)(PD)^(359/256+ε)).                  (4)

For `D=Y^r`, `P=Y^z`, fixed `r,z>0` and `r+z<128/359`, equations (1) and (4) give the actual `≪Y^{1+ε}` marked bound. If the slot has a fixed nonzero smooth normalized prime profile, its diagonal mass is ≍1/log P; the mean lower bound and the power-smaller off-diagonal term show the marked moment is also `≫Y/log P` up to fixed constants and small losses. No order relation between r and z is required. This range is short and may be covered by other existing family-moment results; it does not reach the long-inverse detector target or imply a zero-free boundary for any individual L-function.

The printed OpenAI Lemma 17.1 has one `μ(n)ψ_g(n)` inverse with the same sextic orientation as its slots; it does not directly state this convolution of conjugate cubic inverses. This observation alone does not establish novelty over the broader literature.

**Independent reviews.** Other_families checked the h-mask diagonal, nonprincipal off-diagonal and Wu exponents. High_match independently checked those points, the positive mean (its nonprincipal error is `O(Y^{1/2+ε}D^{359/512+ε})`), the fixed-profile marked lower bound, and the limited comparison with Lemma 17.1.

**Independent review.** A second researcher checked the gcd grouping and masks, diagonal and Wu off-diagonal exponents, the positive family mean, the fixed-prime-profile lower bound, and the parity argument for marked off-diagonal characters. The source Lemma 17.1 treats a single sextic-character inverse with one common orientation; it does not directly furnish this convolution of the two conjugate cubic inverse factors. The review is conditional on the quoted Hecke and reciprocity inputs and does not establish novelty.
