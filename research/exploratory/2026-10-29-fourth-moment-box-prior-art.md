# Prior-art comparison for the variable-strip fourth-moment boxes

This is a targeted comparison, not an exhaustive literature search or a proof of the candidate. The candidate assumes the general-order rectangular-sieve replay and the detector, profile and height transfers in [the fourth-moment box note](2026-10-29-fourth-moment-cyclic-box/README.md). Fix n≥7 and δ=2σ−1 in (4/n,1); the candidate uses squarefree coprime ideal labels `g=A B^(n−1)`, `NA≈X^a`, `NB≈X^(1−a)`, with

    a=[n(1+δ)−4]/[(n−2)(n(3−δ)+4)],
    R=1−2δn/[n(3−δ)+4].

Its asserted exceptional-label exponent is R+ε at some sufficiently small positive X-power height. The boxes themselves depend on δ. All comparisons below are at fixed σ and fixed n; compare small power heights only after absorbing each source's T factor into a strict exponent gap.

## De Faveri: natural label, not conductor

[De Faveri v1, Corollary 1.5](https://arxiv.org/html/2610.04045v1#S1.Thmtheorem5), counts zeros over **all n-free natural labels** with norm at most N, over a field containing μ_n. It is not a conductor cutoff. In the symmetric height window, complex conjugation replaces `A B^(n−1)` by `A^(n−1) B` with the same nonunit zero masks. This gives a same-box natural cutoff `N≈X^[1+(n−2)a]`; apply the corollary to those conjugate labels. At σ=4/5, its exponent is

    D_n=(12n²−38n+5)/(21n²−80n+50),
    C_n=[1+(n−2)a] D_n,

and its explicit height factor is `T^[1+[K:Q]/7+ε]`. For n=7, `a=9/130`, so `C_7=3815/4498≈0.84815`, versus candidate `31/52≈0.59615`. For n=11, `a=17/342`, so `C_11=57145/65018≈0.87891`, versus candidate `43/76≈0.56579`. Directly comparing with D_7=109/173 or D_11=1039/1711 is invalid for this mixed-exponent box: those exponents apply without reordering to a squarefree-index subfamily, not to `A B^(n−1)` ordered by conductor. A fixed extra twist needs the corresponding source-uniformity bridge. This calculation invokes the stated preprint and does not independently establish it.

The same source says its Corollary 1.5 improves upon the earlier [Blomer–Goldmakher–Louvel](https://arxiv.org/abs/1112.1650) comparison for this natural-index zero-density problem. A better squarefree-index statement cannot simply be applied to the mixed box by fixing A: χ_A then has growing conductor and any fixed-twist constants require a separate uniform estimate.

## Other sources and the upper-strip crossover

[Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3) treats a broad conductor-ordered family of primitive finite-order Hecke characters in its fixed Galois-field setting. At fixed or polylogarithmic height its conductor exponent is

    H(σ)=2 min{3/(2−σ),2/σ}(1−σ).

At σ=4/5 this is 1, weaker than the two examples above. For the variable interval the comparison is **not** uniform up to σ=1. The candidate R is strictly below H for `4/n<δ<δ_c(n)` and H is strictly below R for `δ_c(n)<δ<1`, where

    δ_c(n)=[8n+10−sqrt(n²+76n+100)]/(7n).

For n=7 and 11 the crossover is approximately 0.8143678 and 0.8504995, respectively. For positive power heights, account for the source's T factor and choose τ sufficiently small for a strict fixed-height gap. Its finite-order and Galois hypotheses, source counting convention, and applicability to an additional background twist must be retained; it does not automatically cover every arbitrary fixed infinite-type twist.

## Stronger a=0 candidate and the direct squarefree comparator

An alternative source-conditional calculation uses A=1 and squarefree B when `δ≥3/5+4/(5n)`, with

    R₀=1/n + 3(n−2)(1−δ)/[n(3−δ)−4].

Here `χ_(B^(n−1))=barχ_B`, including the original zero masks. De Faveri's Corollary 1.5 **directly applies** to the same squarefree-index family in a symmetric height window, without any conductor-reordering loss. In its middle branch `2/n≤δ≤1−1/n`, comparison of the explicit functions gives the crossover values

    n=7:  δ=(29+sqrt(481))/70 ≈0.72759589;
    n=11: δ=(89+sqrt(5401))/198 ≈0.82066412.

The candidate beats the cited source between its own threshold and the listed crossover; De Faveri is stronger between that crossover and the end of its middle branch. In particular, for n=7 and σ=9/10 (δ=4/5), the candidate exponent is `54/133≈0.40602`, while Corollary 1.5 gives `57/149≈0.38255` with factor `T^[1+[K:Q]/6+ε]`. For n=11 at the same σ the candidate is `398/1111≈0.35824`, versus `179/491≈0.36456` from the cited source. Unlike the mixed-box calculation above, no fixed growing twist is introduced. If the background twist is nontrivial, its source uniformity requires an additional check.

The cited source's **upper branch** also beats R₀ for every n≥7 and `1−1/n≤δ<1`. To see this, put `z=n(1−δ)∈(0,1]` and let D_high be the source's upper-branch exponent. Algebra gives

    R₀−D_high = −N/[n(n−z²)(2n+z−4)],
    N=n²(−2z²+3z−2)+n(2z³+5z²−7z+4)−7z³+4z².

The denominator is positive, while on [0,1] the three parenthesized summands are bounded above respectively by `−7/8`, `4`, and `256/1323`; hence `N≤−7n²/8+4n+256/1323<0` for n≥7. The same small-height qualification applies to this strict fixed-height comparison.

[rStation paper 52 v5](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5), including its small-height Theorem 5.7, concerns the cubic Eisenstein family; it gives no stated n≥7 theorem. Its cubic natural-index method is relevant precedent but does not by itself yield the fixed-order n≥7 box estimate. Classical and contemporary induced-field results considered in [the cyclic prior-art note](2026-10-29-optimized-cyclic-prior-art/README.md) generally concern different base fields, conductor families or near-1 rectangles, and do not directly settle this mixed box at σ=4/5. No completeness or priority claim follows from this search.

Boyang Hu's [preprint on unitary Weil L-functions](https://hexagonmath.org/2610.00216v1) claims nonvanishing in the strict half-plane `Re s>7/8`, with its stated pole exceptions, for unitary Weil representations over number fields. If that claim holds and its character identifications apply, it gives **zero** exceptional characters at every height for each fixed `σ>7/8`, stronger there than a positive-power density bound. This is a source claim, not an independently verified result here. The strict inequality matters: it does not give nonvanishing on the line `σ=7/8`, and it does not cover the principal examples `σ=4/5` above.

A further check of induced Artin families gives a quantitative broader comparison. [Chen An, Theorem 1.1](https://arxiv.org/html/2004.14410v2#S1.Thmtheorem1), treats cuspidal representations over any fixed base field, assuming Ramanujan and bounded archimedean parameters. For a family of at most `X^(1+η)` characters over K, conductor `O(X)` and degree one, taking the source's cardinality parameter `d=1+η` and conductor parameter `A=1` gives

    X^[(15/2+2η+ε)(1−σ)] T^[([K:Q]/2+3+ε)(1−σ)].

At σ=4/5 this is X^(3/2+O(η)) before the height factor. Alternatively, for the subfamily whose induction from K=Q(ζ_p) to Q is cuspidal, use degree `p−1`, A=1 and d=1+η. The same theorem then yields X^(11/2+O(η)) T^(6/5+ε) for p=7 and X^(87/10+O(η)) T^(8/5+ε) for p=11 at σ=4/5. These upper bounds are weaker than even trivial box counting and do not improve the candidate. The induction comparison is conditional on the stated cuspidality, finite ramification and family-count hypotheses, and concerns its Artin L-functions rather than all induced objects. The separate cyclic-field applications of that paper deal with near-1 rectangles; their printed field-count asymptotic has the distinct issue documented in [the cyclic count audit](2026-10-29-cyclic-field-count-source-audit/README.md), which does not itself disprove Theorem 1.1.
