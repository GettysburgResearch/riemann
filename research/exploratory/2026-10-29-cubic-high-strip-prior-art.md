# Cubic natural-label density near 0.8738694: prior-art comparison

**Status.** These are comparisons of stated source exponents, not independent verification of the sources or a proof of an individual zero-free region. The proposed generic-sieve detector bound itself has its own source and detector-uniformity dependencies. The search is not exhaustive.

At σ = 4,369,347/5,000,000 = 0.8738694, set h=2(1−σ). The proposed cube-free natural-index exponent is

    R₃=h(5−3h)/2=6,689,992,880,773/12,500,000,000,000
       =0.53519943046184.

## A stronger specialized source claim

[rStation paper 52 v5, Theorem 1 and equations (1b)–(1d)](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5) claims the exponent

    E_new=1,891,959/4,564,490=0.4144951571807584

at this σ for the full family of good **cube-free** labels in a dyadic norm interval over E=Q(ω), with either cubic orientation and an arbitrary fixed finite-order Hecke twist ν of trivial infinity type whose conductor is supported on the fixed bad set S. The sum counts zeros with multiplicity of primitive inducing functions, and the source asserts a sufficiently small positive power height P^h, with h depending on the fixed data and loss. The optimizer in its (1b) is m=5, giving t=600000/456449. In (1c), the winning face is 5(1−σ)t/2; it is below both the intermediate E and H₅, so E_new=E₄ as displayed. This is a direct stronger natural-label comparison over this particular field and fixed-twist family. It does not establish that source's result over every number field containing μ₃, or for an arbitrary nontrivial fixed archimedean type. Source paper 52 and its analytic inputs have not been independently verified here.

To compare with a single global height X^τ for all labels Np≤X, split dyads at P=X^a for any 0<a<E_new. Standard ideal counting and the elementary individual zero bound control the smaller labels by X^{a+τ+ε}; pick τ>0 below both E_new−a and a times the source's fixed dyadic height exponent. Sum the larger dyads using the theorem. This yields the same exponent plus an arbitrarily small loss; the admissible τ depends on that loss. No uniformity in σ approaching 1 is asserted.

## Other directly quantified comparators

* [De Faveri, arXiv:2610.04045v1, Corollary 1.5](https://arxiv.org/html/2610.04045v1#S1.Thmtheorem5), gives the **full cube-free natural-index** family the high-strip fixed-height exponent

        2(10σ−7)(1−σ)/(24σ−12σ²−11)
        =2,741,281,467,955/5,056,830,380,773
        =0.5420948027795942,

  together with its explicit height factor T^{1+2(1−σ)/(3−2σ)+ε}. Hence the proposed rate is strictly better than this named comparator at sufficiently small positive-power height, subject to the source replay. This does not override paper 52's stronger E-specific assertion. It is the label norm, not the conductor, that is ordered.
* Paper 52 v5 Theorem 5.7 asserts the principal-twist **all natural labels**, including repeated inducing presentations and principal cubes, bound with exponent `(8−7σ)/(3(2−σ))=9,414,571/16,891,959≈0.5573403889981026` at small power height. This is weaker than R₃ at this σ but applies to a larger labelled collection than cube-free rows. Its theorem 1 is the relevant sharper direct cube-free comparison.
* [Khale–O’Kuhn–Panidapu–Sun–Zhang, arXiv:2008.09677v3, Lemma 3.3](https://arxiv.org/abs/2008.09677v3), gives exponent `4(1−σ)/σ=2,522,612/4,369,347≈0.5773430217375731` for the broad primitive finite-order conductor family over a fixed Galois base field, with a height factor. Natural index ≤X implies conductor ≪X in the fixed FHL presentation, and the bounded multiplicity of presentations must be checked when applying its primitive-character count. The fixed-field, finite-order and height hypotheses matter; the citation does not by itself address arbitrary fixed infinity-type twists or a general nongalois base.

The claimed individual bounds in Hu's and Liu's recent, unverified preprints start at 7/8 and approximately 0.874886647, respectively, so their stated strict half-planes do not cover σ=0.8738694. They would qualitatively supersede a density statement farther right. Neither source claim has been independently established here.
