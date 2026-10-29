# A low-dual portion of the 61/72 correlation

**Status.** This is a source-qualified partial bound, subject to the cited source Poisson identity and the imported analytic theorem in [rStation paper 5 v3, Theorem 5](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3). It concerns only the original common-gcd d=1 and fixed divisor k=1 sector of the [physical signed dual correlation](2026-10-29-61-72-dual-correlation/README.md), with a smooth dyadic cutoff Nv≈H≤P. It does not bound the other gcd/divisor sectors or the remaining dual frequencies, and proves no zero-free region. Independent audit requested.

Set P=Y^(6/5), and preserve all good-prime, fixed ray and original zero-mask conventions of the cited correlation. Work in one fixed column class C. For an annular dyadic dual cutoff Nv≈H≤P, the desired bound for the indicated block is O_ε(Y^(1+ε)). The relevant arithmetic identification is this **calibration**: de Faveri's split one-column root phase β(r), combined with the dual quotient orientation, must give, after conjugating the entire product if necessary,

    μ(r) overline(β(r)) χ_r(v)
       = ν(r) C_{−1}(r) χ_r(v),                        (1)

with ν a fixed finite-ray function (separable after finitely many sector expansions), C_{−1}=α^(−1)γ₂ in the paper 5 conventions, and the same sextic character and zero extensions. The [OpenAI quasi-RH source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) (9.4) directly states Γ^(1)_{b,c}=η_{t(b),1}γ₁(b)γ_{−1}(c) for coprime squarefree b,c in one ray class. Its (4.7) gives μγ₁=G·overline(C_{−1}) and μγ_{−1}=χ(−1)G^(−1)·C_{−1}; G and χ(−1) are fixed-ray phases. Its dual quotient supplies conjugate χ_b(v) on the b side and χ_c(v) on the c side, giving precisely the conjugate theta pair in (2). This source identity establishes the orientation in its conventions. Use its direct fixed-sector Poisson identity (9.6), including its self-dual radial transform and normalization, for this calculation; this avoids importing an uncalibrated de Faveri epsilon convention. It is the unrestricted term in the original finite-S mask expansion, hence k=1.

After (1), the physical block, up to fixed finite ray factors, is a finite linear combination of expressions

    (Y/P) Σ_{v≠0, Nv≈H} Σ_{r₁,r₂ sf, (r₁,r₂)=1}
       C(r₁) overline(C(r₂)) ν₁(r₁) overline(ν₂(r₂))
       χ_{r₁}(v) overline(χ_{r₂}(v))
       W(Nr₁/P) overline(W(Nr₂/P))
       Ṽ(Nv Y/(Nr₁ Nr₂)) / sqrt(Nr₁ Nr₂).             (2)

The transform Ṽ is exactly the self-dual radial transform in quasi-RH (9.5)–(9.6). The dual v sum in (9.6) runs over all nonzero integral ideals, including the S-supported parts, and Theorem 5 permits the full natural element-row family. In the Eisenstein PID, passing between the two costs a bounded unit multiplicity and a finite ray-sector expansion. More general primitive Hecke or fractional-lattice presentations require their fixed S-local matching.

For r_i in the fixed annulus and Nv≈H≤P, the parameter HY/P²≤Y/P<1. A smooth partition and Fourier inversion in log(Nr₁/P), log(Nr₂/P), and log(Nv/H) express the kernel in (2) as an integral of products of two one-column profiles and one bounded row phase, with rapidly decaying frequency density and uniform profile seminorms. Thus it suffices, by Cauchy–Schwarz in v, g and the fixed finite sectors, to handle a pair of squares with arbitrary common smooth column profile; their norm-twist heights have the polynomial costs stated in Theorem 5, absorbed by the Fourier density. This step does not replace the physical kernel by a factorized one without integration.

Use the exact projector 1_((r₁,r₂)=1)=Σ_{g|r₁,r₂} μ(g) and write r_i=g n_i. Squarefreeness enforces (g,n_i)=1. For good coprime squarefree ideals, paper 5 (4.8) gives

    C_{−1}(gn)=C_{−1}(g) C_{−1}(n) χ_n(g)^4.           (3)

The factor χ_n(g)^4 has its original zeros, so (3) extends by zero to every squarefree n and automatically enforces (n,g)=1. Also χ_{gn}(v)=χ_g(v)χ_n(v), with original zeros, and |χ_g(v)|²=1_((g,v)=1). The common C(g), finite ray factors and μ(g) have modulus at most 1. For each fixed g the mask 1_((g,v)=1) is nonnegative and may be discarded only after forming the square, or after the two-profile Cauchy inequality. The residual class of n is fixed once the finite ray class of g is fixed; its indicator expands in finitely many fixed ray characters. Thus the column is exactly a paper 5 C_{−1} polynomial with fourth-power label f=g, and no growing column puncture Q is needed: the χ_n(g)^4 zeros already supply it.

In the dyad Ng≈G, the residual column length is D≈P/G. With paper 5's 1/sqrt(Nn) convention, the exterior weight is exactly (Y/P)/G. Theorem 5 (9.3), with nonnegative label weight at most 1, F≈G and Q=1, bounds the unnormalized g and row mean by

    Σ_{g≈G} Σ_{Nv≤2H} |S_{v,g}(D;1)|²
       ≪ (HPG)^ε G · min{H+DG, H+HG}.                 (4)

Dyadic smooth radial profiles and finite class restrictions are allowed as in the theorem; weights, sectors and profiles are independent of v and n. Therefore the g dyad in (2) contributes

    ≪ (Y/P) min{H+P, H+HG} (YPGH)^ε
     ≪ Y^(1+ε) (1+H/P).                               (5)

There are only O(log P) g dyads. The original restriction r₁≠r₂ is redundant here for large P: under (r₁,r₂)=1, equality forces r₁=r₂=1, outside the annular column support. If P is bounded this exceptional finite case is trivial. This argument includes all g in the auxiliary projector, even though the original gcd d is fixed to 1; the two gcds must not be confused.

For H≤P, (5) gives the stated O(Y^(1+ε)) bound for the low-frequency, d=k=1 block, conditional on the quoted source Poisson identity and Theorem 5. The physical dual norm extends to P²/Y=Y^(7/5)>P. Applying (5) without the H≤P restriction gives only YH/P, namely Y^(6/5) at that full scale; hence this calculation by itself does not close the 61/72 target. The theorem itself imports the rStation paper's quasi-RH inverse-moment and theta-reflection inputs; this note does not independently verify them.

**Independent review:** High_match checked the γ₁/γ₋₁ phase against quasi-RH (9.4) and (4.7), the fourth-power label and zero masks, and the label/column normalization. Families independently confirmed the direct Poisson orientation and fourth-power label; uniform-kernel matching remains under review.

## Extension to original gcd d and k=1

The same mechanism controls the **entire natural dual range** for every original gcd dyad `Nd≈D₀≥Y^(1/5)`, still with the single divisor term k=1. For fixed squarefree good d the residual r_i have length `P/Nd`, are coprime to d and belong to the common fixed ray class `C[d]^(−1)`. In the auxiliary gcd expansion write r_i=g n_i. The condition `(d,g)=1` restricts the positive label weights, and `(d,n_i)=1` is imposed by the fixed column puncture `Q=d` in paper 5 Theorem 5. The original source normalization in the physical correlation remains Y/P: `μ(dr_i)=μ(d)μ(r_i)` and the two μ(d) factors cancel. The character associated with the original common d has already been expanded by its divisor mask, and k=1 is the unrestricted term of that expansion; no further `(v,d)=1` is inserted into this term.

In an auxiliary dyad `Ng≈G`, the remaining column scale is `D≈P/(D₀G)` and the g average has F≈G. For each **fixed** d, use the first alternative in (9.3), where the puncture enters only through `(NQ)^ε`:

    Σ_{g≈G} Σ_{Nv≤2H}|S_{v,g}(D;d)|²
       ≪ (YPGD₀H)^ε G(H+DG)
       ≪ (YPGD₀H)^ε G(H+P/D₀).                         (6)

The outer factor is `(Y/P)/G`. There are `≪D₀^(1+ε)` fixed d in the dyad, and only logarithmically many G dyads. Applying the common-profile argument separately for each d is legitimate: within this dyad, `Nd/D₀` ranges over a compact interval, so the profiles and their derivatives are uniform. After r_i=g n_i, logarithmic Fourier separation also splits each `Ng·Nn_i` scale, leaving common n-profiles and label-only norm phases. Those phases are outside the squares and are handled by Cauchy in g; no label-dependent column profile is silently inserted into (9.3). It follows that the whole original gcd dyad is bounded by

    ≪ Y^ε [Y + Y D₀H/P].                                  (7)

The source Poisson decay confines nonnegligible dual dyads to `H≲Y^ε P²/(YD₀²)`. Substitution in (7) gives `Y^ε[Y+P/D₀]`, which is `≪Y^(1+ε)` for `D₀≥P/Y=Y^(1/5)`. A negligible tail is handled by the source's rapid transform decay, with the tail order chosen after all profile and height orders. When `D₀≈P`, restoration of the excluded principal pair `r₁=r₂=1` must be treated separately: its nonzero-dual transform is evaluated at `Nv·Y` and is rapidly negligible after summing d. Its zero-frequency principal term never belongs to the off-diagonal expression. In the nonnegligible dual range one has `D₀≲P/√Y` up to small losses, so the annular residual columns have length ≫√Y and the principal pair is absent. Thus the quantitative full-dual k=1 bound is `Y^ε(Y+P/D₀)`. Writing D₀=Y^d, it has exponent `6/5−d` for `0≤d≤1/5`, compared with the generic sieve exponent `41/30−d` in the linked note. Compared with the separate source Möbius inverse benchmark `Y^(7/6+ε)`, it is smaller when `d>1/30`, while at d=0 the new Y^(6/5) bound is weaker. The Y-threshold improves the generic sieve's k=1 threshold `D₀≥Y^(7/10)`. It covers only k=1; all `k|cd` with k≠1, and the original gcd range below Y^(1/5), remain to be controlled before any full inverse moment or zero-free conclusion.

For a growing divisor k|d, the k-dependent character cannot simply be dropped. In the conjugated column orientation it satisfies

    χ_n(v) overline(χ_n(k)) = χ_n(vk) χ_n(k)^4,

including zeros. Since `(g,k)=1`, the fourth-power label becomes the squarefree product `f=gk`, while the row becomes `h=vk`. Paper 5 controls the complete f-average at length `GK`, not the sparse subfamily of multiples of k at its actual cardinality G. Using that bound and `Nh≲HK` loses a factor K: after the original d-sum it yields at best `Y^ε[YK+Y D₀HK/P]` for `Nk≈K`. The physical dual cutoff is now `H≲Y^ε P²K/(YD₀²)`, making the latter term `P K²/D₀`. This does not give a Y-bound uniformly for growing k. For each fixed bounded k these losses are harmless, provided its fixed S/finite-ray factors are matched; the uncontrolled issue is the collection of growing divisors and their signed sum.

**Extension review:** Families and High_match independently checked the fixed d puncture, auxiliary labels, d and g aggregation, normalization, and the principal-pair qualification. Source analytic assertions and fixed-sector matching remain imported.

**Independent review of the original-gcd extension.** Amplified_opt checked the application of (9.3)'s first alternative with column puncture `Q=d`, fourth-power label `f=g`, label scale `F=G`, and residual column scale `D=P/(D₀G)`. The factor `1/G` outside the label average and `O(D₀)` possible original gcds give (7). The principal pair `r₁=r₂=1`, if restored during factorization, can occur only when `Nd≈P`; its artificial nonzero-frequency contribution is bounded by `(Y/P)·O(P)·Σ_(v≠0)|Ṽ(NvY)|≪_A Y^(1−A)`, using rapid decay and ideal counting. Thus it may be removed at negligible cost. This review assumes the cited source's Poisson phase, transform and theorem and does not bound the growing-divisor terms.

## A proposed growing-k aggregation (under independent review)

The preceding loss is avoided if the original divisor d is opened at the same time as the auxiliary label. The following is a source-conditional deduction; High_match has independently reviewed the coupled row/label masks as stated below. Localize `Nd≈D₀`, `Nk≈K`, `Ng≈G`, with `D₀≤Y^(7/10)` up to small losses; write `d=k d′`, and fix d′ as well as the finitely many ray classes of k and g. In this range the annular residual columns have length ≫Y^(1/2), so `r₁=r₂=1` cannot be restored by the auxiliary gcd expansion. Original squarefreeness gives `(k,d′)=1`, and `(g,d)=1` gives `(g,kd′)=1`. Put

    f=gk,    h=vk,    Q=d′,    D≈P/(D₀G),    F≈GK.      (8)

The f-label is squarefree; χ_n(f)^4 enforces `(n,k)=1`, while Q=d′ supplies the other original `(n,d)=1` condition. Exact multiplicativity and the zero masks give

    χ_n(g)^4 χ_n(v) overline(χ_n(k))
       = χ_n(f)^4 χ_n(h).                               (9)

The common g-factor supplies the positive mask `1_((g,h)=1)`. After the common-profile separation and Cauchy, each fixed (d′,g,k) contributes a nonnegative squared polynomial. Dropping that mask and the condition `k|h` is then legitimate. The factorization f=gk has at most τ_K(f) choices; after taking absolute values, this becomes a nonnegative divisor-bounded label weight independent of h and n, of the precise kind admitted by (9.3). Fixing the ray class of k also fixes the residual n-sector, so finitely many ray-character expansions give common column coefficients. Logarithmic Fourier separation first splits all products of column, label, and row norms; any label-only phases are removed by Cauchy. These points are essential: one cannot simply change f or h inside a signed bilinear sum and then assert that its row-dependent weights are common.

The positive sum over admissible (g,k,h), for one d′, is at most the complete paper 5 average with row norm `≲HK`, label annulus `F≈GK`, puncture Q=d′, and first alternative:

    Σ_{f≈GK} w(f) Σ_{Nh≲HK}|S_{h,f}(D;d′)|²
       ≪ Y^ε GK [HK + D GK]
       ≪ Y^ε GK [HK + P K/D₀].                         (10)

The original coefficient is `(Y/P)/(GK)` up to dyadic constants. There are `≪(D₀/K)^(1+ε)` possible fixed d′, so the resulting dyad is bounded by

    Y^ε [Y + Y D₀H/P].                                  (11)

The true Poisson cutoff is `H≲Y^ε P²K/(Y D₀²)`, and (11) would therefore imply

    block(d≈D₀,k≈K) ≪ Y^ε [Y + P K/D₀].               (12)

In logarithmic scales, (12) is `≪Y^(1+ε)` whenever `d≥1/5+κ`, within the indicated d range. Do not extend the principal-pair argument from k=1 to `d≈P`: for growing k its transform is Ṽ(Nv·Y/Nk), which need not be small. The generic source bound already handles d≥7/10 for every k, so this restriction does not lose the intended union. As before, all source profile and finite-sector identifications are imported, tails need separate rapid-decay handling, and the argument does not control its complement. In particular this is a proposed partial bound, not a new zero-free theorem. The looser `h=vk⁵, f=g` alternative gives `Y+P K⁵/D₀` and avoids this divisor-label aggregation, but controls a smaller set.

**Growing-k review:** High_match independently checked (9), puncture Q=d′, zero masks, label multiplicity, normalization, and source-dependent Cauchy/separation. Combining `d≥1/5+κ` with the generic source criterion controls every admissible k once `d≥12/35`: the two boundaries meet at `(d,κ)=(12/35,1/7)`, and the generic source already controls all k at `d≥7/10`. Families independently checked the coupled masks, divisor-bounded label weights, Q=d′ and scaling; Amplified_opt independently checked the exact profile factorization and label multiplicity below. Fixed bad divisors of c are treated in finitely many separate sectors. This remains conditional on the cited analytic source and does not control smaller original gcds.

**Independent review of the growing-k aggregation.** Amplified_opt checked the common-profile issue directly: with `d=kd′`, `r_i=gn_i`, `f=gk`, and `h=vk`, the two physical column windows are `W(Nd′ Nf Nn_i/P)`, while the dual kernel argument is exactly `Nh·Y/(Nf² Nn₁ Nn₂)`. Thus both are independent of the particular decomposition `k|gcd(f,h)`, before logarithmic Fourier separation. The χ_n(f)^4 zero supplies the missing k part of the original d-puncture; `Q=d′` supplies the rest. After Cauchy the remaining common-g zero mask is bounded by one, and the number of admissible decompositions is at most `τ_K(f)`, an allowed label weight independent of h. With fixed d′ and finite reciprocity sectors, (9.3) then gives (10); the factors and ideal count give (11)–(12). This is a review conditional on the cited source identity and analytic theorem.

In particular, this source-qualified bound combines with the generic controlled polytope in the [dual-correlation note](2026-10-29-61-72-dual-correlation/README.md) to control **every divisor scale** for `d≥12/35` in logarithmic exponents, up to the customary ε losses: the aggregation covers `κ≤d−1/5`, while the generic branch covers `κ≥7/25−2d/5` for `12/35≤d≤7/10`, and the generic bound covers all κ for `d≥7/10`. The two thresholds meet at `d=12/35, κ=1/7`. The range `d<12/35` is not thereby controlled; this is still only a partial estimate for the desired inverse moment.

For `0≤d≤12/35`, the combined source-conditional bound, uniformly over all admissible k dyads and up to ε-losses, has exponent

    max{1, min{6/5, 47/35−d}}.                            (13)

Indeed the new bound has exponent `6/5+κ−d` and the generic source bound has five exponents listed in (7) of the linked correlation note. At κ=1/7 the latter are all at most `47/35−d` on the stated d interval. If d≤1/7, the new bound alone is at most 6/5 for all κ≤d. If 1/7≤d≤12/35, use the new bound for κ≤1/7; for κ≥1/7 each generic exponent is nonincreasing in κ, so the κ=1/7 estimate suffices. This yields a power improvement over the separate source Möbius benchmark `Y^(7/6+ε)` as soon as `d>37/210`, and reaches Y at `d=12/35`. This upper bound does not assert that any exponent is attained, and does not resolve the small-gcd sector d≈0.
