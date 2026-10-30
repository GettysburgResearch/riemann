# Direct n-free density from a fourth detector witness

**Status: source-qualified analytic result.** [De Faveri’s Theorem 1.1](https://arxiv.org/abs/2610.04045v1) directly bounds n-th-power-free rows and n-th-power-free columns. The [uniform detector and fourth-moment proof](UNIFORM-DETECTOR-PROOF.md) derives the remaining long-cutoff interface from the classical fixed-field Hecke analytic theory and the stated FHL conductor and mask identities. Those source inputs and the printed sieve are not independently proved here. The result concerns polynomial-height density, not a new individual zero-free boundary. The named-source comparison is not an exhaustive priority claim. [A companion note](../2026-10-29-fixed-unitary-twists/README.md) transports the same exponents to any fixed unitary Hecke twist, including fixed angular and norm components, with separate treatment of possible pole rows.

Fix n≥4, a fixed number field K containing μ_n, and fixed FHL family data and bad set S. Use the source family’s primitive-conductor bound and exact zero masks and the classical fixed-field Hecke input stated in the detector proof. For fixed `1/2+1/n<σ<1−1/(2n)`, put `δ=2σ−1` and

    R_n(σ) = 2/n + 3(n−3)(1−1/n−δ)/[n(3−δ)−7].                  (1)

Then for each ε>0 there is τ>0, depending on the fixed field, order, σ, source data and ε, such that

    Σ_{u good, n-free; Nu≤X} N(σ,X^τ;χ_u)
       ≪_{K,S,n,σ,ε} X^(R_n(σ)+ε).                           (2)

Zeros of the primitive inducing functions are counted with multiplicity; fixed principal cases are included using individual zero counting. Good squarefree labels already give ≫X distinct primitive characters, since their good conductor supports are their labels. This is a label-ordered statement; it is not by itself a bound for every Hecke character ordered by conductor.

## Source estimate and detector

De Faveri's definition (1.2) explicitly uses the n-free summation symbol **on both rows and columns**. Its Theorem 1.1 states

    Θ_n(Y,D) ≪ (YD)^ε [Y+D+Y^(1−1/n)D^(2/n)
                                   +Y^(2/n)D^(1−1/n)].       (3)

Keep all four terms in (3); the pointwise absorption in (4) of [the earlier calculation](../2026-10-29-cubefree-core-density/README.md) is convenient but loses useful information. If the detector's buffered maximum selects the conjugate presentation, partition the two orientations and apply (3) to the conjugate family by conjugating the entire common coefficient vector; do not relabel the indices, which can change Nu. The inverse Möbius block has squarefree, hence n-free, columns. The ordinary second block has unrestricted columns: decompose each `a=a₁v²` with a₁ squarefree. At fixed v, `χ_u(v²)` is a row contraction, with its original zeros, so Minkowski and a divisor-bound loss give (3). For the ordinary fourth moment first convolve the two ordinary blocks and then perform the same decomposition. The coefficient ℓ² masses, fixed-v factors and common-profile derivatives cost only a fixed small power, using the fixed-v decomposition and the [common-profile Sobolev argument](../2026-10-29-detector-profile-sobolev/README.md). No squarefree-row restriction, moving twist or short-cutoff detector is used.

For D=X^x, division by a squared witness threshold X^(δx) gives the four faces

    f₀(x)=1−δx,            f_D(x)=(1−δ)x,
    f₂(x)=1−1/n+(2/n−δ)x, f₃(x)=2/n+(1−1/n−δ)x.                (4)

The conductor-uniform detector, for a fixed cutoff t>1 and small prescribed loss, produces simultaneous inverse and ordinary witnesses with `0≤r≤t`, `0≤m≤1/2`, and `r+m≥t` up to that loss. A suitable common-height/Sobolev step turns the inverse second moment into exponent `max_i f_i(r)` and the ordinary fourth moment into `max_i f_i(2m)`. The required long-cutoff detector and its common-profile step are derived for this fixed general FHL family in [the uniform detector proof](UNIFORM-DETECTOR-PROOF.md), using the stated standard Hecke and FHL inputs. In particular, the simultaneous lower bounds come from saturation against opposite pointwise upper bounds, not from the product inequality alone. Choose all fixed losses and profile orders before the small global height exponent τ.

Set

    t=3(n−3)/[n(3−δ)−7],        L=2t/3.                       (5)

The hypothesis `2/n<δ<1−1/n` gives `1<t<3/2` and `1/2<L<1`. On `[L,t]`, f₂ decreases and f₃ increases. For x≤1, `f₂(x)−f₃(x)=(1−3/n)(1−x)≥0`; for x≥1 the sign reverses. Also `f₂(x)−f₀(x)=(2x−1)/n≥0`, and `f₃(x)−f_D(x)=(2−x)/n>0`. Thus the maximum of all four faces on `[L,t]` is attained by f₂ at L or f₃ at t. Direct algebra gives `f₂(L)=f₃(t)=R_n(σ)`. If r≥L, use the inverse witness. If r<L, the actual witness constraints yield `2m≥2(t−r)>L` and `2m≤1≤t`; use the ordinary fourth moment. The finite margin and arbitrary ε absorb dyadic and fixed-profile losses. This proves (2) from the stated classical Hecke, FHL and printed large-sieve inputs.

## Comparison throughout the full interval

For every fixed n≥4 and every `2/n<δ<1−1/n`, the applicable middle branch of de Faveri Corollary 1.5 has exponent

    D_n(σ)=1−δ[δn²−(1+3δ)n+3]
                    /[n²δ(2−δ)−2n(1+δ)+2].                 (6)

Exact algebra gives the complete continuum comparison

    D_n(σ)−R_n(σ)
      = (nδ−2)[n(1−δ)−1][n(n−4)δ−n+5]
         /{n[n(3−δ)−7][n²δ(2−δ)−2n(1+δ)+2]} > 0.           (7)

The first two numerator factors are positive by the interval. The third equals 1 for n=4, and exceeds n−3 for n≥5 because δ>2/n. The last denominator factor is concave in δ and takes the positive values `2(n−3)` and `(n−3)(n−1)` at the interval endpoints; the other denominator factors are positive as well. Thus the source-qualified full n-free density theorem (2) improves this named fixed-height source for **every** σ in the indicated interval, not just the two numerical examples below. For each fixed (n,σ), the strictly positive gap persists for sufficiently small polynomial heights after incorporating both statements' height losses. The constant and height power are not uniform in n or as σ approaches the endpoints.

For comparison with the broader [conductor-family estimate of Khale–O’Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3), restrict to its fixed Galois-field finite-order setting and use its fixed-height exponent

    K(δ)=6(1−δ)/(3−δ)  if δ≤3/5,
         4(1−δ)/(1+δ)  if δ≥3/5.

Throughout the same interval, `K(δ)>R_n(σ)`. For δ≤3/5, K≥1>R: indeed `1−R` has positive numerator `δn(2n−7)−n+5>3(n−3)` over `n[n(3−δ)−7]`. For δ≥3/5,

    K−R = P_n(δ)/[n(1+δ)(n(3−δ)−7)],
    P_n=7n(n−1)δ²−(16n²−27n−5)δ+9n²−22n+5.

P′ is increasing but its value at δ=1−1/n is `−2n²−n+19<0`; hence P decreases across the relevant interval, and its endpoint value is `4(n−3)/n>0`. Good local-character injectivity and `Ncond≪Nu` place the source family inside that conductor family. This is a named-bound comparison rather than a proof of priority over every subsequent result; choose a sufficiently small height power after both sources’ T losses. The comparison requires the named Galois-field and finite-order hypotheses and is not asserted for general K outside that source's scope.

For n=6 and Liu's restricted field scope F⊃μ₁₂, [Liu's claimed inverse and ordinary moments](../2026-10-29-liu-source-minimax-barrier.md), if matched to the same rows and profiles, give the stronger exponent `(15−16δ)/(15−6δ)` throughout the present interval. Thus the strict comparison above to de Faveri does not constitute an improvement over Liu in that overlapping sextic setting. The recent Liu source and its exact generator-to-FHL bridge remain unverified here.

## Above the middle branch: an eighth ordinary moment

For every fixed n≥3, the same source-qualified detector proof also gives a separate bound for `1−1/n<δ<1`. Put `h=1−δ`, so `0<h<1/n`, and choose

    t=10/(4+nh),    L=4t/5,    R_high=10h/(4+nh).             (8)

Here `2<t<5/2` and `3/2<L<2<t`. The Γ-convolution and common-profile proof in [UNIFORM-DETECTOR-PROOF.md](UNIFORM-DETECTOR-PROOF.md) extends to this fixed bounded cutoff range by increasing its fixed tail order B before choosing τ; Families and High_match independently checked this replay. On `[L,t]`, the Θₙ count face is the decreasing f₃ up to 2 and the increasing f_D thereafter, and `f₃(L)=f_D(t)=R_high`. If r≥L, use the inverse second moment. If r<L, the actual detector constraints imply `4m≥4(t−r)>4(t−L)=L` and `4m≤2`; use the ordinary **eighth** moment, obtained by expanding S⁴ and applying Θₙ after the same squarefree-column extraction, original row masks and fixed-power divisor losses. Thus the whole actual m interval is covered; no equality m=t−r is assumed. The fixed-power Sobolev and height orders are selected before τ.

The inverse-only cutoff `t=(5−nh)/2` gives the weaker rate `h(5−nh)/2`; the difference between it and (8) is the strictly positive `nh²(1−nh)/[2(4+nh)]`. The new rate is valid but is not claimed to be optimal over all moments or cutoffs.

The relevant upper branch of de Faveri's Corollary 1.5 has `D_high=h[3−(n+2)h]/(1−nh²)`. The exact difference is

    D_high−R_high = h(1−nh)[2+(n−8)h]/[(4+nh)(1−nh²)] > 0.  (9)

For 3≤n<8 the bracket decreases to `3−8/n>0` at h=1/n; for n≥8 it is plainly positive. The rate agrees with de Faveri at h=1/n and is strictly smaller inside the high-δ range. Fixed polynomial-height losses are handled as above.

For the Khale et al. fixed Galois-field finite-order comparator `K=4h/(2−h)`, the sign is

    K−R_high = 2h[(2n+5)h−2]/[(2−h)(4+nh)].                 (10)

Thus (8) beats that named bound for `h>2/(2n+5)`, ties there, and is weaker for smaller h. No exhaustive priority claim is made. For n≥4 this entire open high-δ interval has σ>7/8. For n=3 it starts at σ>5/6. Liu’s claimed finite-order individual boundary `0.874886647…` and Hu’s claimed unitary boundary 7/8, if validated with the applicable scope, would supersede the density estimate strictly above their respective boundaries. Neither recent claim has been independently verified here.

At n=3 and the tracker boundary θ, (8) gives

    t=25000000/11891959,
    R₃(θ)=6306530/11891959≈0.53031885.

The same natural-label de Faveri upper-branch exponent is `2741281467955/5056830380773≈0.54209480`, a strict gap of about .01177595. This general fixed-K comparison is not the strongest known claim for every specific field: [rStation paper 52 v5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5), claims a stronger cube-free Q(ω) exponent `1891959/4564490≈0.41449516` at θ, with fixed finite S-supported twists and small polynomial height. That recent source has not been independently verified here and does not automatically cover general K.

For K=Q(ω), although the preceding bound is weaker than that claimed paper 52 density rate, the same argument illustrates the source-qualified field consequence. The nonunit cube-free FHL labels give cyclic cubic extensions L_u/K. The two nontrivial relative factors are conjugates; apply the same source estimate to both orientations without changing the label norm. Assuming the candidate's conventional interpretation, `ζ_K=ζ L(s,χ_{−3})` has no zeros in `Re(s)>θ`, and hence all but `O(X^(R₃(θ)+ε))` labels `Nu≤X` have `ζ_{L_u}` zero-free in `Re(s)>θ, |Im(s)|≤X^τ`. Squarefree labels provide ≫X distinct fields up to the two generators per field. The conductor–discriminant formula gives `|D_{L_u}|≪X²`; choosing `X≈c Y^(1/2)` with fixed c small yields a specified family of ≫Y^(1/2) fields of discriminant ≤Y, with at most `O(Y^(3153265/11891959+ε))` exceptions at a suitably scaled polynomial height. This is a source-qualified family result conditional on the candidate interpretation, not an all-height result or a count of all cubic extensions by discriminant.

## Exact retuned boundary and source comparison

At the separately kernel-replayed tracker value `θ=4369347/5000000`, δ=`1869347/2500000`. For every fixed n≥4, θ satisfies the hypotheses above, and (1) becomes

    R_n(θ)=(1891959 n²−1914571 n−12500000)
                    /[7n(804379 n−2500000)].                   (6)

At θ the applicable middle branch of de Faveri Corollary 1.5 gives a natural-label fixed-height exponent D_n. Exact simplification yields

    D_n−R_n = (630653n−2500000)(1869347n−5000000)Q(n)
      /[7n(804379n−2500000)(5852276793591n²
                                      −21846735000000n+12500000000000)],
    Q(n)=1869347n²−9977388n+12500000.

[check_theta_comparison.py](check_theta_comparison.py) verifies these exact identities. All denominator and linear numerator factors are positive for n≥4. With n=z+4, the quadratic Q becomes `1869347z²+4977388z+2500000`, so the difference is strictly positive for every fixed n≥4. For each fixed n, a sufficiently small positive height power preserves the comparison. The exact limits are `R_n→1891959/5630653≈0.336011` and `D_n→1261306/3130653≈0.40289`. For example R₄=`842755/1674204≈0.503377`, R₅=`5045224/10653265≈0.473585`, and R₁₁=`195366758/488809013≈0.399679`.

## Exact density at σ=4/5

At σ=4/5 the condition `2/n<δ<1−1/n` holds for every n≥4. The cutoff and exponent are

    t=15(n−3)/(12n−35),
    R_n(4/5)=(6n²−9n−25)/[n(12n−35)].                         (7)

In particular n=4 gives 35/52; n=5 gives 16/25; and n=6 gives 137/222. The named de Faveri natural-label exponent there is `D_n=(12n²−38n+5)/(21n²−80n+50)`, and exact factorization gives

    D_n−R_n = (2n−5)(3n−10)(3n²−17n+25)
                /[n(12n−35)(21n²−80n+50)] > 0               (8)

for every fixed n≥4. All factors are positive: the quadratic is positive at n=4 and increasing thereafter. This strictly improves the earlier source-qualified [n-free rate](../2026-10-29-full-order-natural-fourth/README.md), whose exponent minus (7) equals `(3n−10)²/[2n(3n−5)(12n−35)]`. Both comparisons concern fixed height or a sufficiently small polynomial height, with the stated detector and sieve inputs. At σ=4/5 the tracker θ-bound does not control the cyclotomic base ζ_K, so the argument supplies only relative-quotient density without a separate base nonvanishing input.

## Cyclic fields, conditional on the tracker base

For each fixed odd prime p≥5, take K=Q(ζ_p), and assume the compatible changed-root-embedding FHL families for all fixed nonzero powers j mod p. Applying (2) separately to each powered family on the **same** original labels and taking the finite union gives all but `O(X^(R_p(θ)+ε))` nonunit p-free labels Nu≤X with every nontrivial relative factor L(s,χ_u^j) zero-free in `Re(s)≥θ, |Im(s)|≤X^τ`. The field L_u/K is cyclic of degree p. The comparisons above are strict for every p≥5. Squarefree labels give ≫X distinct fields, up to at most p−1 generators per field.

The base factor is `ζ_K=ζ∏_{χ nonprincipal mod p}L(s,χ)`, with primitive factors. If the independently kernel-replayed [Dirichlet candidate](../2026-10-29-return-retune-8738694/README.md) is admitted with its conventional analytic meaning, it makes this base nonzero on `Re(s)>θ`; its pole at 1 is not a zero. Hence ζ_{L_u} is zero-free in the **open** rectangle `Re(s)>θ, |Im(s)|≤X^τ` for the stated density-one family. This is source-qualified by the detector proof and printed sieve, conditional on the candidate interpretation, and limited to polynomial height.

For any fixed `σ` with `θ≤σ<1−1/(2p)`, the same powered-family argument and continuum bound give a density-one full-field rectangle `Re(s)>σ` at small polynomial height, with exponent R_p(σ). The exact θ endpoint is included as above. Recent preprints claim stronger individual regions: Liu claims `Re(s)>0.874886647` for finite-order Hecke characters, and Hu claims `Re(s)>7/8` for unitary Weil L-functions. If validated with the relevant scope, either would supersede the corresponding exceptional-count conclusions above its boundary. We have not independently verified those claims; neither boundary covers θ or 4/5.

For p=5 the θ exception exponent is `5045224/10653265≈0.473585`, and for p=11 it is `195366758/488809013≈0.399679`. In the discriminant-truncated form below, these become `1261306/10653265≈0.118396` and `97683379/2444045065≈0.039968`, respectively, with an arbitrary additional ε in the exponent.

The conductor-discriminant formula gives `|D_{L_u}|≪_{p,S}X^(p−1)`. A sufficiently small fixed multiple of `X=Y^(1/(p−1))` therefore gives a specified family of ≫`Y^(1/(p−1))` fields with discriminant ≤Y, and at most `O(Y^(R_p(θ)/(p−1)+ε))` exceptions at a suitably scaled polynomial height. This does not purport to count every cyclic p-extension of K with discriminant ≤Y. All constants and height exponents may depend on the fixed p.

**Independent review.** [Families’ source and scalar review](INDEPENDENT-REVIEW.md) checks the printed n-free row and column conventions, column factorization and fixed-v masks, and the earlier three-face detector calculation; Families also [independently checked the sharper four-face argument](FOUR-FACE-INDEPENDENT-REVIEW.md), the exact θ factorization and the σ=4/5 identities. [High_match independently checked the detector saturation and Sobolev interface](DETECTOR-INDEPENDENT-REVIEW.md). The printed FHL/sieve and the candidate interpretation remain explicit inputs, and the recent source proofs have not been externally verified here.

## A limitation of generic mixed moments

Within this detector relaxation and arbitrary-coefficient Θ_n moments, taking any fixed finite collection of mixed monomials `M_r^a S_m^b`, with nonnegative integer a,b and a+b>0, cannot lower (1) for `1≤t≤3/2`. Put `t_*` and `L_*=2t_*/3` as in (5), and `R=R_n(σ)`. Expanding a fixed mixed monomial and applying Θ_n after extracting square factors gives the scalar face maximum f(ar+bm). The product coefficients are divisor-bounded and have X^ε ℓ² mass after normalization; fixed-v row contractions preserve all original zero masks. The parameters of the common profiles and their derivatives are handled as in the detector proof.

If `1≤t≤t_*`, the relaxed witness

    r=L_*,  m=L_*/2,  r+m=t_*≥t

is admissible because `L_*<1≤t` and `m<1/2`. For (a,b)=(0,1), `f₂(m)≥f₂(L_*)=R` since f₂ decreases. For (1,0) or (0,2), `ar+bm=L_*` and f₂(L_*)=R. Every other nonzero pair satisfies `ar+bm≥3L_*/2=t_*`, and `f₃(ar+bm)≥f₃(t_*)=R` since f₃ increases. Thus no finite selection of such moments gives an exponent below R at this witness.

If `t_*≤t≤3/2`, the admissible witness `(r,m)=(t,0)` has every a=0 monomial exponent at least f₀(0)=1, and each a≥1 monomial exponent at least `f₃(at)≥f₃(t_*)=R`. Here R<1 by the positive numerator for 1−R given in the comparison above. At t=t_* both witnesses apply. These two cases establish an exact scalar obstruction for all fixed mixed monomial moments estimated by the displayed generic Θ_n bound. They are **not** a lower bound for actual selected rows or zeros, and do not rule out mixed estimates exploiting arithmetic coefficient cancellation, a stronger detector, or a different cutoff range. Families independently checked the full mixed-monomial argument, the coefficient and mask reduction, and the Khale comparison; the obstruction remains confined to the stated generic estimate.

[A separate local reduction](../2026-10-29-critical-mixed-moment/README.md) identifies a concrete stronger input: a fixed power saving for the actual mixed Möbius–ordinary moment only near `(r,m)=(L_*,L_*/2)` would yield a strictly smaller density exponent. That mixed estimate is not proved; the accompanying coefficient lower bound shows that a saving cannot come from a power-small ℓ² norm alone.

## The lower-δ limit of generic long-cutoff moments

For fixed n≥3 and `0<δ≤2/n`, de Faveri's lower branch is `D=1−δ/(4−nδ)`. For every hypothetical detector cutoff t≥1, the relaxed witness `(r,m)=(t,0)` is admissible. On x≥1, the generic Θₙ face f₃ is increasing, and every fixed mixed monomial with a≥1 inverse factors has exponent at least `f₃(at)≥f₃(1)=1+1/n−δ`. Ordinary-only monomials and the trivial family count have exponent at least 1. Therefore this generic long-cutoff relaxation has lower bound

    min(1,1+1/n−δ).                                           (11)

For δ≤1/n this equals 1>D. For `1/n<δ≤2/n`, its difference from D is exactly `(nδ−2)²/[n(4−nδ)]≥0`. Thus this particular generic mechanism cannot improve the named source below the middle interval, even with finitely many higher mixed powers and arbitrarily long fixed t. It does not exclude short cutoffs, arithmetic coefficient savings, stronger source moments, or a better bound on actual rows.

High_match independently checked the high-δ endpoint comparison and the fixed-cutoff extension in [LONG-CUTOFF-REVIEW.md](LONG-CUTOFF-REVIEW.md).

## High-δ generic mixed-moment limitation

The high-δ rate (8) is also the exact worst-case limit of this detector relaxation with **any fixed finite collection of generic mixed monomial moments**, for every t≥1 in the abstract relaxation, whether or not a detector at that cutoff has been proved. This is a statement about the available scalar upper bounds, not about actual zeros. Put

    v=2/(4+nh),   L=4v,   t*=5v,   R=5hv.                    (12)

Then 2/5<v<1/2, `2v<1`, `4v<2<5v`, and `f(4v)=f(5v)=R`. For each fixed nonzero pair of nonnegative integers (a,b), the generic moment of M^aS^b has count exponent `f(ar+bm)` after expanding the product, extracting squarefree columns, retaining original zero masks and applying fixed-order divisor bounds. It is enough to exhibit one admissible relaxed witness for each t at which every such exponent is at least R:

* If `1≤t≤3v`, choose `(r,m)=(2v,v)`. Then r≤1≤t and r+m=3v≥t. Each length is `(2a+b)v`. For k=1, `f₀(v)−R=[2+(n−8)h]/(4+nh)>0`; for k=2, `f₂(2v)−R=[4+n(n−7)h]/[n(4+nh)]>0`. The second numerator is positive on the open h interval: for n<7 its endpoint at h=1/n is n−3≥0, and for n≥7 it is plainly positive. At k=3, `f₃(3v)≥f₃(4v)=R`; at k=4 equality holds; and for k≥5, `f_D(kv)≥f_D(5v)=R`.
* If `3v≤t≤4v`, choose `(r,m)=(t,0)`. For a=1, f₃(t)≥f₃(4v)=R; for a≥2, `at≥6v>5v`, so f_D(at)>R. Ordinary-only monomials have f(0)=1>R.
* If `4v≤t≤5v`, choose `(r,m)=(4v,v)`. Then r≤t, r+m=5v≥t, and all lengths are `(4a+b)v`; the preceding integer cases apply.
* If `t≥5v`, choose `(r,m)=(t,0)`. Every a≥1 monomial has `f_D(at)≥f_D(t)≥R`; ordinary-only monomials again have f(0)=1>R.

These witnesses also cover the endpoints. Thus no number of fixed higher ordinary or inverse moments, nor their generic mixed products, can improve (8) within this scalar detector/Θₙ mechanism. More explicitly, at any of the four witnesses one may take about X^R abstract selected rows with `|M|²=X^(δr)` and `|S|²=X^(δm)` and zero elsewhere; every displayed generic mixed-moment inequality and the pointwise saturation bounds hold up to small powers. Hölder combinations of those positive inequalities therefore do not eliminate this abstract model. It is not asserted to come from actual Hecke characters or zeros. The obstruction does not rule out arithmetic cancellation, non-generic source moments, detector restrictions or improvements for actual selected families.

Families independently checked all four high-δ mixed-monomial witness cases, the integer-length inequalities for n≥3, endpoints and the fixed-power coefficient/mask reductions. The conclusion remains a limitation of the generic Θₙ scalar mechanism.
