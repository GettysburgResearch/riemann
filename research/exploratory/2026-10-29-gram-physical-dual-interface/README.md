# The Gauss frame inside the physical dual kernel

**Status.** The bounds below are deductions conditional on the fixed-sector physical Poisson identity, smooth profile separation and paper 5's theta mean, exactly as in the independently checked [low-dual note](../2026-10-29-low-dual-theta-bound.md). The source analytic inputs are not independently proved here. This is a partial signed-dual bound, not a whole inverse-moment estimate or a zero-free region.

Fix `P=Y^(6/5)`. Keep the original primary-good-ideal conventions, zero extensions, fixed finite ray character ν, and smooth annular column and row profiles of the low-dual note. Its original common-gcd and divisor are d=k=1; its separate auxiliary common divisor is g. Let H be a smooth nonzero-dual dyadic scale. After retaining the exact physical Poisson kernel, using its logarithmic Fourier separation, and summing the complete auxiliary g-projector with its signs as described in the linked note, the contribution of this H dyad has magnitude

    ≪_ε Y^ε (Y/P)(H+P).                                         (1)

In particular it is `O(Y^(21/20+ε))` whenever `H≤Y^(5/4)`; the natural non-negligible dual range is `H≲Y^ε P²/Y=Y^(7/5+ε)`. Summing logarithmically many such H dyads costs only `Y^ε`. Hence, for the proposed `Y^(21/20)` full inverse target, the remaining d=k=1 nonzero frequencies lie in

    Y^(5/4) < H ≲ Y^(7/5+ε).                                  (2)

The zero-frequency, diagonal, other original d/k terms and rapid tails are not included in (1), and their treatment must follow the physical identity separately.

## The exact source of (1)

At auxiliary scale `Ng≈G`, the factorization in the low-dual note has column scale `D≈P/G` and exterior factor `(Y/P)/G`. Paper 5 Theorem 5 (9.3), applied to a **common** separated column profile with fourth-power label f=g and the original zero masks, gives

    Σ_(g≈G) Σ_(Nv≤2H) |S_(v,g)(D;1)|²
        ≪ (YPGH)^ε G min{H+DG,H+HG}.                           (3)

Here the finite ray-class expansions are fixed in number; common Fourier/norm-height costs are polynomial, and the physical kernel is integrated rather than silently replaced by a product. The mask `(v,g)=1` is dropped only inside an already positive square, or after Cauchy for two separated profiles. The common Fourier tail and rapid dual tail orders are chosen after the source's fixed height order. The factor ν is a fixed ray character; its finite expansion is part of (3). Applying the first alternative of (3), the dyad contributes

    ≪ Y^ε (Y/P)(H+P).

There are O(log P) auxiliary-g dyads, and the principal pair accidentally restored during factorization is absent because the original columns are in a large P-annulus; the linked note discusses its separate negligible restoration in related d-ranges. This proves (1), conditional on all source matching and uniformity just listed. It is an absolute bound for the signed physical dyad after Cauchy and summing g; no separate cancellation in g is asserted.

For original gcd `Nd≈D₀`, still k=1, the same fixed-puncture source replay gives `≪Y^ε(Y+Y D₀H/P)`. It is therefore within `Y^(21/20+ε)` when `H≤Y^(5/4)/D₀`. Since the natural cutoff is `H≲Y^εY^(7/5)/D₀²`, this first-source argument controls every frequency for `D₀≥Y^(3/20)` up to small-power buffers. This does not replace the independently stated, stronger signed second-Poisson range `d+g≥7/50` in its own hypotheses, nor cover growing k.

## The arithmetic relation to the frame

The inverse-oriented frame vector in the [overlap note](../2026-10-29-cubic-theta-overlap-average/README.md) satisfies

    ⟨m_P,v⁻_(P,h)⟩
      = P^(−1/2) × [a fixed finite ray combination of S_h(P;1)],  (4)

where `S_h(P;1)` is the theta polynomial normalized by `1/√Nn`. The conjugation is essential: the frame contains `overline(χ_n(h))`, so its inner product contains `χ_n(h)` and the coefficient `μ(n)overline(γ₁(n))`, which is a fixed-ray multiple of `C₋₁(n)=α(n)⁻¹γ₂(n)`. The g=1 physical term therefore involves these actual frame overlaps for h=v, modulo the physical kernel separation. This is an arithmetic identity, not a claim that the vectors diagonalize the physical operator.

For general squarefree g, the exact source relation

    C₋₁(gn)=C₋₁(g) C₋₁(n) χ_n(g)^4

changes the moving label to `h=v g⁴`, retains the `(n,g)=1` and `(v,g)=1` zero masks, and dilates the column support to `Nn≈P/Ng`. Thus the P-scale frame `Nh≤P^(53/72−δ)` does not automatically control all these g-dependent theta squares: the coefficient vector, column scale and growing puncture are different. Reducing h modulo sixth powers can change the core label but cannot discard the accompanying masks. At g=1, its label cutoff is `Nv≤Y^(53/60−6δ/5)`, far below the residual high-dual band (2). The theta mean itself is more useful for the present low-frequency estimate than taking a projection through the frame.

## A concrete signed-cancellation target for the high band

The obstacle is already visible in a positive **factorized model**, with a fixed nonzero annular column profile U and fixed nonnegative annular row profile Φ. Define

    S_(v,g) = Σ_(n sf) C₋₁(n) ξ(n) χ_n(v)χ_n(g)^4
                            U(N(gn)/P)/sqrt(Nn),
    B(H) = Σ_g μ(g)/(Ng) Σ_v Φ(Nv/H) 1_((v,g)=1)|S_(v,g)|².  (5)

Use one fixed finite-ray expansion and all its original masks; (5) is schematic only in omitting the physical transform's coupled nonseparable profile and its fixed finite linear combination. A sufficiently uniform physical analogue of

    B(H) ≪ Y^ε P Y^(1/20),     Y^(5/4)≤H≤Y^(7/5),               (6)

would place this d=k=1 band within `Y^(21/20+ε)` after multiplying by Y/P. It must cover every Fourier mode of the actual coupled transform with one cumulative norm-height allowance; the fixed-profile model alone would not do so. At H=Y^(7/5), (6) asks for a saving `H/Y^(5/4)=Y^(3/20)` compared with the available `O(H+P)` theta mean.

The signed g-projector is essential. The source-conditional [long-dual diagonal calculation](../2026-10-29-sextic-dual-diagonal-obstruction.md) gives, for the g=1 square in (5),

    Σ_v Φ(Nv/H)|S_(v,1)|² ≍ H     when H=P^ρ, 1<ρ<2.         (7)

Consequently this individual positive model term is `≫Y^(6/5)` after the physical prefactor at H=Y^(7/5), too large for the `Y^(21/20)` target. It cannot be discarded or bounded by (6) in isolation. This is a source-qualified statement for the positive fixed-profile model; it is not a lower bound for the coupled physical transform or for the full signed sum. Cancellation across g, or a different signed treatment of the physical kernel, is required to exploit this model. In particular, absolute values before combining g cannot prove (6).

The radial physical transform has no available uniform power decay throughout (2): its argument is `HY/P²`, which ranges from `Y^(−3/20)` up to a fixed positive constant. Smoothness gives rapid decay only beyond the latter cutoff, not a power saving at the endpoint. Fixed-profile nonvanishing or cancellation at a particular transform value is not a substitute for the uniform coupled-kernel estimate.

## The long-dual positive model puts its mass outside the low frame

The relation above can be made quantitative. This statement uses the source-conditional positive diagonal asymptotic (7), the unrestricted-row sextic sieve, and the source theta-overlap mean. It is an assertion for the factorized model, not a lower bound for the actual signed physical correlation.

Let `A_H` be the matrix whose columns are the inverse-oriented vectors `v⁻_(P,v)` from the overlap note, with the full good natural v row family in a fixed annular range `Nv≈H` (no unproved restriction to an individual row ray sector), and include `Φ(Nv/H)^(1/2)` in each column. Fix the column and Möbius profiles so that their product is the nonzero U in (7); both are fixed smooth annular profiles, and all fixed ray sectors and masks in that source comparison are retained. Let m be the normalized Möbius vector, and let Π be the good spectral-frame projection of the [squarefree Gram note](../2026-10-29-squarefree-gram-moment/README.md), with cutoff `H₀=P^(53/72−δ)` and sufficiently small fixed δ>0. The low-frame result gives

    ||Πm||² ≪ P^(−19/72−δ+ε).                                (8)

Take `H=P^(7/6)`. By the exact `S_(v,1)=√P⟨m,v⁻_(P,v)⟩` normalization and the long-dual diagonal asymptotic,

    ||A_H* m||² ≍ H/P = P^(1/6).                              (9)

For arbitrary source coefficients, apply the unrestricted-row sextic sieve in v with squarefree n columns, including the common Gauss phase in the coefficients. Dividing its squared operator norm by P yields

    ||A_H||² ≪ P^(−1+ε)[H+H^(1/6)P+H^(5/6)P^(1/3)
                                +H^(1/3)P^(5/6)]
              ≪ P^(11/36+ε).                                  (10)

Thus

    ||A_H* Πm||² ≪ P^(1/24−δ+ε) = o(P^(1/6)),                (11)

and the reverse triangle inequality gives

    ||A_H*(1−Π)m||² ≥ (c+o(1)) P^(1/6)                         (12)

for some c>0 depending on the fixed profiles and sector. The assertion is uniform only in the source's fixed profile/ray data, with sufficiently small ε after δ is fixed. Here the high-row weights are nonnegative, so (9) is a positive mean; no eigenvector alignment assumption is used.

Multiplying (11)–(12) by the model's physical prefactor Y gives low-frame and complement energies respectively `≪Y^(21/20−6δ/5+ε)` and `≫Y^(6/5)`. Hence the long-dual g=1 positive model places essentially all its theta energy outside the low squarefree Gauss frame. This strengthens the abstract linear-algebra obstruction with an explicit source-qualified arithmetic example. It does **not** show that the full physical operator on `(1−Π)m` has this lower bound: the original kernel couples columns and the complete signed g-projector cancels its artificial diagonal before positive majorization. Any inference about the physical target must retain those cancellations.

The same argument is not confined to the target-adapted cutoff. For any fixed `0<a<31/36`, take the good spectral frame on squarefree labels up to `H₀=P^a`; the theta row mean gives `||Π_a m||²≪P^(a−1+ε)`. Then (10) bounds its high-dual contribution by `P^(a−25/36+ε)=o(P^(1/6))`. Thus the high-dual model's energy lies predominantly in the complement of **every** such low-label frame, despite the almost-full Gram conditioning available through `a<1`. This is still a fixed-profile positive-model statement, not a lower bound on the signed physical kernel.

**Independent review.** Families checked the four sieve exponents `1/6,7/36,11/36,2/9`, the low-frame overlap and reverse-triangle lower bound, and both physical-scale conversions, conditional on the cited theta diagonal asymptotic. The actual signed physical correlation remains outside this positive-model lower bound.

**Second independent review.** Literature checked the theta-mean prefactor and dual cutoffs, the growing `v g⁴` label and masks, the frame orientation and √P normalization, and the long-dual complement exponents. The fixed-profile positive model and the actual coupled signed kernel remain distinct, and all source identities are imported as stated.
