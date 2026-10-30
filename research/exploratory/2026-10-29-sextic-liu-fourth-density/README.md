# Sextic density from the Liu ordinary fourth moment

**Status and scope.** The deduction below uses [Liu, Theorem 12.14 and Remark 12.16](https://arxiv.org/abs/2610.26835v1), de Faveri's printed sextic large sieve, the fixed-field buffered detector, and the stated finite-sector match between their sextic presentations. These are recent source inputs; their complete proofs have not been independently verified here. It is a polynomial-height density estimate, not an individual zero-free strip or an exhaustive novelty claim.

**Stronger source consequence under audit.** Liu's own Lemma 10.6 supplies a substantially stronger inverse second moment for sixth-free rows. Combining it with the same Liu ordinary fourth moment gives the exponent `(15−16δ)/(15−6δ)` for `δ=2σ−1∈(0,5/6)`, namely `9/19` at σ=4/5 and approximately `0.288787` at the separately assumed tracker boundary θ. The dyadic-to-global height transfer, source matching and possible overlap with Liu's own Proposition 2.7 are being audited. Thus the `181/298` calculation below is an improvement over the named de Faveri bound, not a claim of a new best rate or of independence from Liu.

Let `K=Q(ζ₁₂)`, let S be a fixed admissible bad set large enough for both source constructions and let χ_u be the good sextic FHL family, with u sixth-power-free and `Nu≤X`. Subject to the source match in the last section, for every ε>0 there is τ>0 such that

    Σ_{u good, sixth-free; Nu≤X} N(4/5,X^τ;χ_u)
       ≪_{S,ε} X^(181/298+ε).                                  (1)

Zeros of the primitive inducing function are counted with multiplicity. The finitely many principal inducing presentations are handled separately by individual zero counting. Good squarefree labels already give ≫X distinct primitive characters. This is a natural-label bound on the full sixth-free family.

## Proof from the two source moments

Write `δ=2(4/5)−1=3/5`. At cutoff `t=175/149`, the simultaneous saturated detector gives `0≤r≤t`, `0≤m≤1/2`, `r+m≥t`, up to fixed arbitrarily small losses. The inverse second moment from de Faveri's Θ₆ gives, on `t−1/2≤r≤t`,

    f(r)={ 5/6−(4/15)r       if r≤1,
           1/3+(7/30)r       if r≥1. }                         (2)

These are the exact dominant source faces in the indicated range. Liu's z=0 ordinary fourth-moment specialization gives `Σ_u |S_m(u)|⁴≪X^(1+ε)` uniformly for every `m≤1/2`, hence the ordinary witness count exponent

    g(m)=1−(6/5)m.                                               (3)

The standard bin and Sobolev step is applied to both bounds with common profiles and finite derivatives, before choosing a small height power. Each detected row is bounded by the smaller of (2) and (3). If r≤1, the worst case is `m=t−r`, and f decreases while g increases in r. Their intersection is

    r=505/596,  m=195/596,  f(r)=g(m)=181/298.                  (4)

If r≥1, both f and g(t−r) increase with r; their minimum is therefore at most its value at r=t, which is `f(t)=181/298`. Fixed detector and bin losses are absorbed in ε. This proves (1), conditional on the displayed inputs.

The scalar exponent `181/298` is also the exact minimax of these two moment bounds for cutoffs `1≤t≤3/2`. If `t≤175/149`, the pair (4) remains admissible since r≤1≤t and r+m=175/149. If `t≥175/149`, the admissible pair `(r,m)=(t,0)` has ordinary exponent 1 and inverse exponent at least 181/298. These relaxed witness pairs need not be realized by any actual characters or zeros.

At 4/5, the direct four-face Θ₆-only calculation gives `137/222`, and de Faveri Corollary 1.5 gives `209/326`; both are strictly larger than `181/298`. The comparison is for the same natural sixth-free labels and fixed height, or sufficiently small fixed height powers after allowing source height losses. Liu also claims a separate individual nonvanishing region to the right of approximately 0.874886647; that claimed region is to the right of 4/5 and does not itself yield (1). No comparison with every source is asserted.

## Source family and common profiles

Liu Remark 12.16 specializes Theorem 12.14 with no prime marks, `q=0`, basic presentations `ψ_k(n)=ν(n)χ_n(k)`, fixed finite ν and fixed S, and excludes principal inducing characters. It explicitly gives the ordinary fourth bound `X^(1+ε)(1+H)^A` for normalized plain lengths up to `X^(1/2+small loss)`, with fixed profile seminorms and polynomial height H. The z=0 clause is separate from the extra zero-free condition attached to κ<1 with prime marks.

To apply this to the FHL family, one needs the fixed-field source normalization: Liu's exterior-ideal sextic symbol and FHL's χ_u agree on coprime good ideals after partitioning u into finitely many fixed ray/Kummer classes and multiplying by a fixed finite-order good-prime character for each class; both sides have the same noncoprime zero masks. One representative per good ideal is included in Liu's row sum, and restricting rows is harmless. This is the source comparison described in [the general-field collapsed sieve](../2026-10-29-general-field-collapsed-sieve/README.md), with the root-of-unity and S-unit choices fixed before the moment. The exact finite-character and presentation conventions are a source-matching input and must not be replaced by a conductor-only identification. Theorem 12.14 is stated over cyclotomic fields containing μ₁₂; an Eisenstein-field version would need a separate check of Liu's Proposition 2.6 and its cited sources.

Liu's bound is for fixed profiles and a common height. The detector gives varying β and h; apply fixed-order Sobolev on β and h before selecting the family moment, as in [the reviewed uniform-detector proof](../2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md). Differentiating adds bounded log powers on annuli. Choose τ small enough that the common-height cover, the source polynomial `(1+H)^A`, and the individual zero-count cost fit within the requested X^ε. Restriction to the detector's bin and fixed presentation classes preserves positivity.

A Cauchy estimate combining Liu's ordinary fourth moment with the generic inverse fourth does improve the former Θ₆-only balanced witness by `1/222`, but it does not improve (1) at the new optimum: at (4) its exponent is `2389/3576`, larger than `181/298` by `217/3576`. At the second witness `(t,0)` it is also no better than the inverse second-moment face. This observation concerns that Cauchy estimate, not all possible arithmetic mixed moments.

## Stronger rate from Liu's inverse moment: source audit pending

Liu's Lemma 10.6, equation (10.15), states the sixth-free inverse estimate on each norm shell `U≤Nu≤2U`, for a fixed finite family of twists supported in S and either orientation,

    Σ_u |M_r(u)|² ≪ U^[max{1,(1+5r)/6}+ε] (1+H)^A.          (5)

Assuming its stated source family agrees with the ordinary-fourth family and with the FHL presentations through the finite-sector match above, it can replace (2) throughout the detector proof. For fixed `0<δ=2σ−1<5/6`, put

    t=5/(5−2δ),       L=2t/3,       R=(15−16δ)/(15−6δ).         (6)

Then `1<t<3/2` and `2/3<L<1`. The inverse count exponent is `1−δr` for r≤1 and `1/6+(5/6−δ)r` for r≥1. The Liu ordinary fourth exponent is `1−2δm`. If r≥L, the inverse exponent is at most R on `[L,t]`: its two endpoint values equal R and its left face decreases while its right face increases. If r<L, then the simultaneous detector gives `m≥t−r>t/3`, so the ordinary exponent is at most `1−2δt/3=R`. The usual fixed losses are absorbed in ε. Thus, under these two printed Liu inputs and their source match, the corresponding sixth-free family has zero count `O(X^(R+ε))` in a sufficiently small power-height window. This is a direct source consequence, not a claimed new result independent of Liu.

The inverse source is printed dyadically. To recover the global height `X^τ`, fix a small η>0: handle `Nu≤X^η` by a trivial row count and individual zero-count bound, and for each larger dyad U choose τ below η times its admissible U-height exponent. Sum the logarithmically many dyads. The small-label and height costs are absorbed by taking η and then τ sufficiently small relative to R and ε. At σ=4/5 this gives `t=25/19`, `R=9/19`; at the tracker boundary θ it gives `R=3795224/13141959≈0.28878678`.

The exponent agrees with the x=0 scalar specialization of Liu's Proposition 2.7, but the exact scope of that proposition's detected class and its relationship to the global family count require separate checking; the proof above instead makes the two required moment inputs and the row/height transfer explicit. Neither source preprint's analytic proof nor the sixth-power-lift/FHL source identification has been independently established here.
