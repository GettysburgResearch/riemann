# Retaining the row mask through a second Poisson step

**Status.** A source-qualified partial refinement of [the second-Poisson aggregate](2026-10-29-second-poisson-aggregate.md). The theorem below is a deduction conditional on the explicitly listed Poisson, phase, fibre, profile and inverse-mean inputs from the cited recent sources; those imported analytic inputs have not been independently established here. Three source-level reviews checked the replay, including its masks and principal restoration. It is not a proof of a new inverse moment or zero-free region.

## Source-qualified partial theorem

Fix the Eisenstein field and fixed good-prime, finite-ray and smooth-profile data of the linked physical correlation. Assume: (i) its fixed-sector Poisson identity and zero-mask conventions; (ii) paper 5 v3 (10.4)–(10.10), including its finite-ray phase, formal off-coprime extension, divisor-fibre and uniform Fourier-profile statements; and (iii) the all-natural-row inverse estimate (10.2), uniformly with a squarefree puncture at subpower cost. These are analytic source inputs, not consequences established in this note.

Put `P=Y^(6/5)`. Localize the original good squarefree common gcd and its good divisor to `Nd≈D₀≤Y^(7/10)`, `Nk≈K`, and use any smooth dyadic partition in the auxiliary squarefree gcd `Ng≈G`. Remove the artificial theta diagonal **only after summing the complete signed auxiliary-g partition and all its auxiliary ray classes**, as described below. Original column sectors may be fixed throughout; auxiliary g-ray classes are separated only after diagonal removal. Let `B_off(D₀,K,G)` denote the resulting nonprincipal part of one G block, summed over its original d and k and over all nonzero physical dual frequencies, with the original masks retained. Then, for every ε>0,

    |B_off(D₀,K,G)| ≪ Y^ε [Y/K + Y^(7/6)/(K D₀^(5/6)G^(5/6))].

The implied constant depends on ε, the fixed field, ray data and finitely many profile seminorms. Fixed bad-prime divisors are handled in finitely many sectors. In particular this part is `O(Y^(1+ε))` when `d+g+(6/5)κ≥1/5`, with `D₀=Y^d`, `K=Y^κ`, and `G=Y^g`. The theorem bounds the signed, diagonal-subtracted contribution described here; it does not assert that an individual positive theta square has this bound. Summing the finitely many logarithmic dyads preserves an arbitrarily small power loss.

Use that note's fixed sectors and dyads `Nd≈D₀`, `Nk≈K`, `Ng≈G`, and fix `d′=d/k`. Keep the physical common-g zero mask `(v,g)=1` when the auxiliary gcd projector is expanded. Do not replace it by one before separating the theta diagonal. Write `r_i=g n_i`; the theta diagonal `n₁=n₂` has `r₁=r₂=r`. For each fixed r, all v, k, d, profiles, physical phases, and original zero masks depend only on r, not its factorization. The signed auxiliary projector contributes

    Σ_(g|r) μ_K(g) = 0,     r≠1.                              (1)

Thus all of these artificial diagonals cancel **exactly across the complete auxiliary-g sum**. In the range `D₀≤Y^(7/10)`, the physical residual column annulus has norm `≈P/D₀≫1`, so r=1 is absent. Crucially, the cancellation is made before bounding separate g dyads or replacing the v mask by a positive majorant. It works for any common v cutoff and does not require a Poisson estimate for the diagonal.

For the offdiagonal, open the retained mask by `1_((v,g)=1)=Σ_(ℓ|g,ℓ|v) μ_K(ℓ)`. Write `g=ℓ a`, `v=ℓ w`, `Nℓ≈L`. Squarefreeness and `(g,k)=1` imply `(ℓ,a)=(ℓ,k)=1`. The exact zero-extended character identity is

    χ_n(v)χ_n(g)^4χ_n(k)^5
       = χ_n(w)χ_n(a)^4χ_n(kℓ)^5.                         (2)

The second-Poisson source row and label lengths are `H/L` and `G/L`. Its nonzero-frequency inverse-row scale is `R′₀=D²G²/(HL)`, and the moving factor `χ_n(kℓ)^5` combines into row t=kℓr. Thus `Nt≲K L R′₀=K D²G²/H`, which is Y up to small powers at the physical cutoff. For fixed t, both k and ℓ divide t, and the remaining frequency, label and divisor choices obey the source's divisor-bounded fibre count. After Cauchy, the outer masks may be discarded, while the inverse input's fixed puncture is `d′s` as before.

The proposed crucial replay is: apply paper 5 (10.4)–(10.10) to the **nonprincipal offdiagonal only**, for each separated Fourier mode, and restore its artificial inverse principal term as a separate harmless error. If all these operations retain the source's uniform seminorms and fibre accounting, then for each ℓ dyad the nonzero-frequency contribution has an `H/(L D)` prefactor and an all-row inverse sum at `T≲K D²G²/H`. Multiplication by the physical outer factor and summation over d′ then gives, at the natural cutoff and after summing logarithmically many ℓ dyads,

    ≪ Y^ε [Y/K + Y^(1/6)D^(5/6)/K]
     = Y^ε [Y/K + Y^(7/6)/(K D₀^(5/6)G^(5/6))].         (3)

This would improve the previous `P/D₀` diagonal loss and control each `(d,κ,g)` dyad whenever

    d+g+(6/5)κ ≥ 1/5,                                       (4)

using `D₀=Y^d`, `K=Y^κ`, `G=Y^g`. The complementary small-scale core is still unresolved: at `D₀=K=G=1`, (3) is `Y^(7/6)`, exactly the current source inverse benchmark. Hence even a verified (3) does not prove the `O(Y^(1+ε))` target or the `61/72` boundary.

The principal restoration in paper 5 costs `O((DF)^ε)` per fixed k,ℓ in the normalized F-average. Multiplying by `F=G/L`, counting `O(KL)` possible k,ℓ, and then applying the physical factor and `O(D₀/K)` possible d′ gives `O_ε(Y^ε YD₀/(P K))`, which is `O(Y^(1+ε))` because `D₀≤P` and `K≥1`. Families checked this count.

The main remaining proof obligations are the precise signed-kernel Fourier separation after (1), the ℓ/k/t frequency-fibre bound with all source masks and finite sectors, the artificial principal-restoration estimate after summing the dyads, and the rapid-tail bounds. One cannot use the positive theta row mean to discard the original row mask and then claim the diagonal cancellation.

**Independent reviews.** Families checked the exact diagonal cancellation, character identity, length scales and principal-restoration count. High_match checked the same algebra, divisor-fibre accounting and the exponent condition (4). Both reviews explicitly leave the line-by-line signed offdiagonal source replay, Fourier uniformity and the underlying imported theorems as open proof obligations.

## Source replay and principal-restoration ledger

The following records the proposed replay of paper 5 (10.4)–(10.10) in more detail. It is conditional on the source identities, same-sector character presentation and uniform common-profile Fourier calculus; it does not turn those imports into an independently verified theorem.

Fix d′, the outer norm dyads K,L,G,H and all finite ray classes before opening the second Poisson sum. Use a and w for the theta label and row after g=ℓa, v=ℓw. Their scales are F=G/L and K_row=H/L. The theta column is the C_{−1} coefficient with label a, fixed puncture d′ and the additional multiplicative factor χ_n(kℓ)^5. In the source's common-factor substitution n₁=u b,n₂=u c, this factor splits as `|χ_u(kℓ)|² χ_b(kℓ)^5 overline(χ_c(kℓ)^5)`. Its common factor is a bounded outer mask. After the source's second coprime projector b=sx, c=sy, the χ_s(kℓ) factor likewise cancels; the residual factors attach to x and y.

Source (10.4)–(10.5) converts the first residual factor to an inverse coefficient with row character `overline(χ_x(r))`, where

    r = h a² u²/e = h a² e (u/e)²,       e|u.                   (5)

All symbols here denote the source's second-Poisson frequency and internal gcd/divisor variables; this r is unrelated to the first-stage residual column. The extra factor gives exactly

    χ_x(kℓ)^5 overline(χ_x(r)) = overline(χ_x(t)),   t=kℓr,     (6)

including zeros. The only remaining inverse puncture is d′s, with the source's full zero extension. A residual x meeting kℓ already vanishes through t. Fixed-ray factors are expanded in a finite basis after fixing the indicated sectors; no moving kℓ-character remains in the column coefficient.

For fixed t, both k and ℓ divide t. Source (10.9) says a,u,e divide r and the original second frequency h is then determined; consequently k,ℓ,a,u,e all divide t, and the number of possible tuples is at most a fixed divisor power τ_K(t)^C. Coprimality and the original support only reduce it. The source's weighted Cauchy and finite projector in s may therefore enlarge the positive t sum and absorb this fibre weight into `(Nt)^ε`; the inverse input has the same fixed ν and puncture d′s. The bound remains valid if some labels have several representations, because those representations are counted in this same divisor fibre rather than replaced by one.

The physical column windows are smooth functions of the normalized norms of d′, k, ℓ, a and n; the dual kernel has the same property with row w. On each fixed dyad, logarithmic Fourier inversion separates these into a common pair of annular n profiles and bounded outer norm phases. The source's polynomial norm-height order is fixed before choosing the Fourier decay order, so integration costs only a fixed finite seminorm factor and subpowers. In particular no k-, ℓ- or row-dependent arithmetic multiplier is inserted into an inverse coefficient after (6).

For each ℓ dyad, source (10.10) consequently gives an unnormalized nonprincipal contribution bounded by

    (H/(L D)) (YD₀KLGH)^ε [T+T^(1/6)D^(5/6)],
    T ≪ K L R′₀ = K D²G²/H.                                    (7)

The original source's auxiliary principal restoration can be handled separately even without a fibre saving: source's bound after (10.5) is O((DF)^ε) for its label-average normalization, so it is O((G/L)Y^ε) before that normalization. There are O(KL Y^ε) pairs k,ℓ and O((D₀/K)Y^ε) choices of d′. Multiplying by the physical `Y/(P K G)` yields `≪Y^ε·Y D₀/(P K)≤Y^(1+ε)`, since D₀≤P and K≥1. The zero-frequency principal term is not introduced into the physical offdiagonal; the artificial nonzero-frequency restoration is the term just bounded. Fixed S divisors change only constants.

The omitted large-frequency tails are estimated as in source §10.3 after all coefficient and height orders are fixed, with arbitrary Schwartz decay. At the physical H₀ cutoff, the scalar in (7) is monotone in H and its inverse-row scale is T≈Y; the physical outer factor, d′ count and geometric summation of the 1/L dyads yield (3). This closes the algebraic and normalization ledger subject to the stated source replay. Amplified_opt independently checked the factorized kernel scales, uniform Fourier separation, masks, t-fibre and restoration ledger under the stated source inputs; a separate audit is still in progress. The imported inverse and reflection estimates have not been independently proved.

**Further independent ledger review.** Amplified_opt checked the transformed kernel `Ṽ(Nw·Y/[Nℓ·(Na)²·Nn₁Nn₂·Nk])`, whose normalized scalar is `HY/(KG²D²)` independently of L, and the physical windows `W(Nd′·Nk·Nℓ·Na·Nn/P)`. This supports the common-profile separation under the source's stated Fourier seminorm hypotheses. The common u,s masks, t=kℓr fibre and restoration count also match. The source identities and analytic inputs remain imported; the result has not been independently formalized.

## Detailed source-qualified replay of the nonprincipal term

The following spells out the deduction from paper 5, rather than asserting a
new instance of its theorem without checking the moving coefficients. It
retains as inputs the source's (10.4)–(10.10), its all-natural-row inverse
estimate (10.2), and the physical fixed-sector Poisson identity. In particular,
the replay is conditional on their analytic proofs and on the common-profile
uniformity stated there. The artificial principal restoration is treated
below; it is not included in the inverse estimate.

First fix `d′`, the norm dyads, the finitely many relevant fixed ray classes,
and one smooth nonzero-v norm dyad. In the **exact** signed expression, insert
a partition of unity in the auxiliary g norm and sum it back to one on the
theta diagonal. No dyadic constant may replace `Ng` in this step. For fixed
`r=gn`, the diagonal column coefficient, the physical kernel, the k factor and
the v zero mask depend on r alone, and the entire g dependence is `μ(g)`.
Because r is squarefree and coprime to d, every g|r occurs. Thus (1) removes
the diagonal before any triangle inequality. The r=1 pair is outside the
residual column annulus for `D₀≤Y^(7/10)`. The argument also permits two
different original profiles of `Nr`: on the diagonal their product depends on
`Nr`, not on its divisor g. This does **not** assert cancellation separately
for a Fourier mode introduced after g-localization, which can carry separate
`Ng` and `Nn` factors. After removing the diagonal and recombining the full
g-partition, dyadic partitions and triangle inequalities may be used on the
**remaining** signed terms.

For an `Nℓ≈L` block expand the row mask exactly, put `g=ℓ a`, `v=ℓ w`,
and use (2). Both a and ℓ are good and squarefree and `(a,ℓ)=1`;
`(k,ℓ)=1` follows from `(g,d)=1`. The source's original row, squarefree
label and column length are now respectively

    H′=H/L,        F′=G/L,        D≈P/(D₀G).                (5)

The label a remains squarefree. All restrictions involving a, ℓ, k or d′
are retained until the point at which the source opens the square and applies
Cauchy; the zero in `χ_n(kℓ)^5` enforces `(n,kℓ)=1`, and `(n,d′)=1` is
the column puncture. For each k,ℓ, the factor `μ(g)μ(ℓ)` and the remaining
factor depending only on g,k,v have modulus at most one and belong to the
outer weight. They are not inserted as arbitrary multipliers in the column.

To compare directly with the source, call its column gcd u, its divisor
`e|u`, its secondary Poisson frequency j, and its coprime-projector divisor
s. Source (10.4) gives a nonprincipal phase whose inverse character is
`overline(χ_x(r))`, with

    r=j a²u²/e = j a² e (u/e)².                              (6)

The present extra column factor changes this inverse character to
`overline(χ_x(rkℓ))`; this is an identity with the source zero conventions,
not a division by a residue symbol. On the source's first column-gcd split
it also contributes the outer mask `|χ_u(kℓ)|²`. When the source projector substitutes
`x=s x′`, the common factor from the moving twist is the outer mask
`|χ_s(kℓ)|²`; it can be dropped only after Cauchy. The remaining column
puncture is `Q=d′s`, and the residual inverse polynomial has the source
coefficient `I_0(x′)=μ(x′)ν(x′)` up to one of finitely many fixed ray
characters. Its row is

    t=kℓ r,   Nt≲ T := K D²G²/H,                              (7)

up to the conventional small-power tail enlargement. This follows from
source (10.8): `Nr≲D²(F′)²/H′=D²G²/(HL)`. The multiplicative kℓ mask
is already in `χ_(x′)(t)` and must not be imposed again as a moving
puncture. Source (10.6) is the full coprime projector, and its off-coprime
extension is the *formal separate-column expression* described immediately
before (10.6), not the primitive character Poisson formula applied to a
noncoprime pair.

For fixed t, the possible outer k and ℓ divide t. After choosing them, the
source fibre (10.9) bounds the remaining choices `(a,u,e,j)` by a fixed power
of `τ_K(r)`, hence the combined fibre is at most `τ_K(t)^{O(1)}`. The
additional coprimality and fixed-class restrictions only reduce it. Apply the
source's weighted Cauchy at each common Fourier mode, **then** enlarge the
positive inverse-row sum to all `Nt≲T`; the divisor weight costs `T^ε`.
For each fixed s, (10.2) applies with puncture `d′s`; the `Ns≈S` sum with
its `1/Ns` weight is `O(1)` up to subpowers, as in the source. This yields,
for this ℓ dyad and fixed d′, the nonzero-frequency bound

    (H/(L D)) (YD₀KGH)^ε [T+T^(1/6)D^(5/6)].                (8)

Here the source's normalized (10.10) has prefactor
`H′/(F′D)`; multiplying by the label normalization F′ gives `H′/D`.
No additional factor K or L is inserted: the combined fixed-t fibre has
already counted k and ℓ. Summing the O(log Y) ℓ dyads is harmless and
`L≥1`, so one may discard `L^(−1)` after (8).

The source's artificial restoration `a=b=1` in the nonzero-frequency
expression **before** inserting the s-projector is handled separately, using
the elementary bound immediately following its (10.5). Terms with
`x′=y′=1` after writing `a=sx′, b=sy′` are not separately discarded:
for `s≠1` they belong to the source's formal projector expansion and are
covered by its inverse norm. The pre-projector restoration's normalized total
is `O((DF′)^ε)` for each fixed
k,ℓ and ray sector, so the unnormalized cost is `O(F′(DF′)^ε)`.
There are `O(KL Y^ε)` such k,ℓ, yielding `O(KG Y^ε)` for one d′ and ℓ
dyad. Including the original outer factor `(Y/P)/(KG)` and the
`O((D₀/K)Y^ε)` choices of d′ costs at most

    Y^(1+ε) D₀/(P K) ≪ Y^(1+ε),                               (9)

since `D₀≲P` and `K≥1`. This bound does not use cancellation in the
restoration and does not confuse it with the physical theta diagonal already
removed. The zero frequency for every *nonprincipal* source character is
zero, as in the source; it is not restored.

For the Fourier step, smooth dyadic partitions are chosen first. The original
column and physical-kernel cutoffs have arguments in fixed compact ranges;
after restricting `H≤Y^ε P²K/(YD₀²)`, their normalized derivatives have
fixed-order bounds with at most `Y^ε` losses. Separate the logarithms of
`Nk/K`, `Nℓ/L`, `Na/F′`, the two column norms, and `Nt/T`; on their
compact supports the relation `Nr=Nt/(Nk Nℓ)` has uniform derivative bounds.
The Fourier coefficients have arbitrary fixed polynomial decay and the source
inverse estimates have fixed polynomial norm-twist costs, so choosing the
integration-by-parts order afterwards makes the mode integrals finite. The
resulting two column profiles may differ; retain them through the nonprincipal
Poisson step and apply Cauchy to the two inverse norms, as in source (10.6)–
(10.10). Taking positive squares before removing the exact physical diagonal
would lose the cancellation. The source's rapid transform estimate handles
secondary-frequency dyads `Nr≫D²(F′)²/H′`, while the original dual tail
`H≫P²K/(YD₀²)` is handled before this replay, with fixed tail orders chosen
after the profile orders. Fixed S-supported divisors are split into finitely
many sectors; an extension to a different Poisson normalization requires a
separate local-lattice check.

Finally multiply (8) by the outer factor `(Y/P)/(GK)` and by the number of
d′. With `H≤H₀=Y^ε P²K/(Y D₀²)`, the first part is independent of H and
the second grows as `H^(5/6)`, so the endpoint H₀ gives (3), together with
(9). This establishes the displayed reduction **conditional on the cited
source identities and uniform estimates**. It does not independently verify
paper 5, the physical Poisson normalization, or the global `Y^(1+ε)`
inverse moment.

**Detailed independent review.** High_match checked the moving-twist factor through both common-factor splits, exact t-fibre divisibility and τ(t) multiplicity, d′s puncture and masks, both shortened scales, Fourier-height ordering, principal-restoration count, and the final exponents. The audit uses the cited source's asserted Poisson and fixed-puncture inverse bounds; it does not independently establish those inputs or the global inverse target. Diagonal cancellation must occur with the complete g partition before any individual g-localized Fourier mode is bounded.
