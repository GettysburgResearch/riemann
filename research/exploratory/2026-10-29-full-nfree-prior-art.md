# Targeted prior comparison for full n-free natural-label density

This note compares stated source bounds with the proposed full n-free natural-label zero-density estimate at σ=4/5. The proposal depends on a detector uniform for the **growing** multiplier arising from the squarefree/square decomposition, common profiles and small-power heights, and the appropriate higher-order sieve. Those analytic transfers are not independently established here. This is a comparison with named results, not an exhaustive priority finding or an individual zero-free theorem.

For fixed 4≤n≤10 and a fixed field K containing μ_n, let χ_u be the chosen good FHL family with `u` n-free, ordered by `Nu≤X`. The proposed X-exponent is

    R_n=(3n²−10)/[n(6n−10)].

[De Faveri v1, Corollary 1.5](https://arxiv.org/html/2610.04045v1#S1.Thmtheorem5) applies to the **same entire n-free natural-label family**, not merely squarefree labels. At σ=4/5, its exponent and height factor are

    D_n=(12n²−38n+5)/(21n²−80n+50),
    X^(D_n+ε) T^[1+[K:Q]/7+ε].

At fixed or polylogarithmic height its exact comparison is

| n | Proposed R_n | De Faveri D_n | D_n−R_n |
|---|---:|---:|---:|
| 4 | 19/28 | 15/22 | 1/308 |
| 5 | 13/20 | 23/35 | 1/140 |
| 6 | 49/78 | 209/326 | 82/6357 |
| 7 | 137/224 | 109/173 | 715/38752 |
| 8 | 91/152 | 469/754 | 1337/57304 |
| 9 | 233/396 | 635/1031 | 11237/408276 |
| 10 | 29/50 | 11/18 | 7/225 |

Equivalently,

    D_n−R_n=(3n−10)(3n³−26n²+70n−50)
                  /[2n(3n−5)(21n²−80n+50)] > 0.

For n≥4 the cubic numerator is positive and increasing, and every denominator factor is positive. To compare at `T=X^τ`, choose fixed ε and τ sufficiently small relative to the relevant positive gap and the source's T exponent; the proposal's own allowed positive height exponent must also be respected. The n=4 gap 1/308 is particularly small. The source is a 2026 preprint and its proof is not independently verified in this comparison.

The later [all-order rational cover](2026-10-29-full-order-natural-fourth/README.md) extends the same source-qualified proposal to every fixed n≥11 with `R=29/50` for `11≤n≤20` and `R=14/25` for `n≥21`. The same D_n decreases for n≥4. Thus the first block has gap at least `D_20−29/50=36/3425`, and the second has gap at least its limiting value `4/7−14/25=2/175`. Its exact finite cover, ordinary second-moment mode and t=1/2 perturbation are reviewed [here](2026-10-29-full-order-natural-fourth/ALL-N-COVER-REVIEW.md). The added orders retain the same analytic assumptions and fixed-n quantifiers.

The source states that its Corollary 1.5 improves the earlier [Blomer–Goldmakher–Louvel](https://arxiv.org/abs/1112.1650) density estimate, while also covering the larger n-free family. [Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677v3) gives fixed-height conductor exponent 1 at σ=4/5 for the broad primitive finite-order family in its fixed Galois-field setting. Good n-free labels are distinguished by their nonzero local exponents, and their conductor is at most a fixed multiple of the natural label norm; subject to those source hypotheses this comparator is weaker than each R_n. Its explicit height factor must be included for positive-power heights. It does not automatically establish a comparison for arbitrary fixed infinite-type twists or arbitrary nongalois K.

[rStation paper 52 v5](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5) gives a stronger natural-index result for its **cubic** Eisenstein family, not a stated full order-n result for 4≤n≤10. In the sextic case the cubic powers are separate L-functions; a bound for them does not bound the original sextic character. Similarly, [Corrigan–Zhao](https://doi.org/10.1017/S0004972722001617) treat selected Dirichlet families, which are not automatically the full higher-order Hecke family over K.

[Hu's preprint](https://hexagonmath.org/2610.00216v1) claims all-height nonvanishing for unitary Weil L-functions in the strict half-plane `Re s>7/8`, with stated pole exceptions. If correct, it supersedes positive density counts for σ>7/8, but it does not imply nonvanishing at σ=4/5. This is an unverified source claim in the present work. A targeted search did not locate another stronger directly applicable full n-free Hecke-family theorem at σ=4/5; no conclusion about all prior literature follows.

## The four-face continuum

For the newer [direct full-family calculation](2026-10-29-direct-nfree-density/README.md), fix n≥4 and `2/n<δ=2σ−1<1−1/n`. Its proposed exponent is

    R=2/n+3(n−3)(1−1/n−δ)/[n(3−δ)−7].

The middle branch of De Faveri Corollary 1.5 is indeed the applicable source formula throughout this open interval. Direct subtraction gives

    D_n−R = (nδ−2)[n(1−δ)−1][n(n−4)δ−n+5]
            /{n[n(3−δ)−7][n²δ(2−δ)−2n(1+δ)+2]} > 0.

The first two numerator factors are positive; the third is 1 for n=4 and exceeds n−3 for n≥5. The last denominator factor is concave and positive at both endpoints, with values `2(n−3)` and `(n−3)(n−1)`. The other factors are positive. Thus the direct proposal beats that named natural-index exponent at every fixed point of the interval, subject to its stated detector and source inputs.

In the fixed Galois-field, finite-order setting of Khale et al., its broader conductor-ordered exponent H also exceeds R throughout this same interval. For δ≤3/5, `H=6(1−δ)/(3−δ)≥1`, while

    1−R=[δn(2n−7)−n+5]/[n(n(3−δ)−7)]>0.

For δ≥3/5,

    H−R = P_n(δ)/[n(1+δ)(n(3−δ)−7)],
    P_n=7n(n−1)δ²−(16n²−27n−5)δ+9n²−22n+5.

The derivative of P_n is increasing and at `δ=1−1/n` equals `−2n²−n+19<0`; hence P_n decreases throughout the relevant range and is bounded below by `P_n(1−1/n)=4(n−3)/n>0`. Thus there is no fixed-height crossover in this interval. For the source's conductor ordering, the good local exponents distinguish the n-free labels and `N conductor≪Nu`; apply its T factor and choose the polynomial-height exponent small enough relative to the fixed strict gap. Do not extend this comparator to nongalois fields or arbitrary infinite-type twists without another source.

[Liu's preprint](https://arxiv.org/abs/2610.26835v1) claims every finite-order Hecke L-function over every number field is zero-free for `Re s>B_flat≈0.874886647039964`, with the usual principal-pole qualification. If validated, this is a stronger individual statement than positive exceptional bounds for every fixed σ strictly above B_flat, including some points below Hu's claimed 7/8 boundary. It is an unverified source claim here and does not cover σ=4/5 or θ=0.8738694. The search did not locate a different directly applicable stronger full-family density theorem below those thresholds; that is not an exhaustive prior-art claim.
