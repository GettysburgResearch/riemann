# A continuous squarefree-family improvement from the long detector

**Status:** Source-qualified family density consequence, conditional on the fixed-order conjugate-pair sieve replay and long buffered detector/profile/height transfer in the [unbalanced-box note](../2026-10-29-unbalanced-cubic-density/README.md). The imported preprint and these replays are not independently established here. This is not an individual zero-free region and no exhaustive priority claim is made.

For fixed n≥7, K containing μ_n, its fixed good set S and its FHL order-n family, put

    Δ_n = sqrt(1−8(n−1)/n²),
    σ_−=(3−Δ_n)/4,   σ_+=(3+Δ_n)/4.                            (1)

For every fixed `σ_−<σ<σ_+`, set δ=2σ−1 and

    R_n(σ)=1/n+(1−δ)(1−3/n+δ/2)/(1−2/n).                      (2)

For each ε>0, the cited inputs give τ>0 such that

    Σ_(B good squarefree, NB≤X) N(σ,X^τ;χ_B)
       ≪_(K,S,n,σ,ε) X^(R_n(σ)+ε).                            (3)

Zeros are primitive Hecke zeros, counted with multiplicity. This is the A=(1) case of the conjugate-exponent box estimate: `χ_(B^(n−1))` and `barχ_B` agree on all good ideals including their zero masks, and their primitive L-functions have identical counts in a symmetric height window. For a global cutoff, sum dyadic boxes under a common detector base X and common height; the cited detector replay gives uniform polynomial height for all boxes, and O(log X) scales cost X^ε. A split into small labels is not silently discarded.

The good primes B alone give ≫X/log X distinct exact-order-n primitive characters of conductor O(X); their conductor at each good prime is that prime, with bounded fixed bad part. A fixed rescaling therefore gives the same lower bound for conductor ≤X. Since (4) below shows R_n is strictly smaller than the already subunit source exponent D_n(σ), (3) gives density-one zero-free rectangles for this squarefree family at some small power height. This does not yield a uniform rectangle for any individual L-function.

## Exact comparison with the stated natural-index theorem

Throughout interval (1), `δ∈(2/n,1−1/n)`, so de Faveri [Corollary 1.5](https://arxiv.org/abs/2610.04045v1) has its middle-branch natural-index exponent D_n(σ). It gives `X^(D_n+ε) T^[1+[K:Q](1−σ)/(3−2σ)+ε]` for all n-free labels, hence also this squarefree subfamily. Straight algebra gives

    D_n(σ)−R_n(σ)
      = (δn−2)² [δ(1−δ)n²−2n+2] /
        {2n(n−2)[(2δ−δ²)n²−2δn−2n+2]}.                     (4)

The denominator is positive throughout `2/n≤δ≤1−1/n`: the negated bracket is a convex quadratic whose values at the endpoints are `6−2n` and `−n²+4n−3`, both negative for n≥7. The remaining numerator is positive exactly when

    δ(1−δ)>2(n−1)/n²,

which is exactly (1). At either endpoint the two displayed exponents coincide; we do not claim improvement outside this interval. Choose τ and ε sufficiently small compared to the fixed positive difference to retain a strict comparison at height X^τ.

The optimized detector uses

    t=(1−3/n+δ/2)/(1−2/n).

The second long-cutoff constraint strictly dominates the first for δ>2/n, with their difference `(δn−2)/(n(n−2))`. Both `δ>2/n` and `1<t<3/2` hold in (1), so this is the A=(1) specialization of the cited long-detector minimax. The ordinary and inverse moment estimates, rowwise profile reduction, zero-count multiplicity and fixed-height scaling are inherited conditions, not new proofs in this note.

For example, n=7 gives `σ∈(5/7,11/14)`; at σ=3/4 the proposed exponent is `201/280`, while the stated natural-index exponent is `51/71`, a gap `9/19880`. At n=11 and σ=4/5 the proposed exponent is `1468/2475`; its explicit natural-index comparison is in the [optimized-box note](../2026-10-29-optimized-monomial-box/README.md). The n=7 gap is small, so all profile and height losses must be chosen smaller. The comparison only concerns this named source; other results may be stronger.

For a larger fixed-order example, n=31 and σ=4/5 give `R=12288/22475≈0.54674`, compared with `D=3453/5917≈0.58357`. The corresponding induced family has degree 30. Constants and the admissible height power are allowed to depend on the fixed order 31.

A targeted literature check also found the earlier Blomer–Goldmakher–Louvel squarefree order-n exponent `8(1−σ)/(7−6σ)`, which is 4/5 at σ=3/4, and the generic finite-order Hecke bound of Khale and coauthors weaker at this point. De Faveri explicitly compares his natural-index result with the former. No stronger directly applicable squarefree order-n theorem was found in that targeted check; it is not an exhaustive novelty review.

## Induced representations

For an odd prime n=p≥7 choose K=Q(ζ_p), and restrict B to prime ideals above completely split rational primes. There are ≫X/log X such labels. Their exact-order-p characters have full Gal(K/Q) orbit because only one prime in each full split orbit ramifies. Class field theory and cyclic automorphic induction give irreducible `(p−1)`-dimensional monomial Artin representations and cuspidal GL_(p−1) inductions, with standard L-function `L_K(s,χ_B)` and conductor `|D_K| N f(χ_B)`. Isomorphism fibers have size at most p−1 by restriction to W_K, so the family still has ≫X/log X distinct classes of conductor ≤X after a fixed rescaling. Applying (3) gives at most X^(R_p(σ)+ε) exceptional classes in a sufficiently short polynomial-height rectangle. This remains conditional on the same analytic inputs and is a selected automorphic family, not a bound for all GL_(p−1).

The comparison factorization, quadratic endpoint signs and n=7 example are reproduced by [check_scalars.py](check_scalars.py). Two independent reviews checked these calculations, common-X handling of small labels and heights, character masks and the induction, conditional on the cited analytical assumptions. This does not prove the analytic inputs.
