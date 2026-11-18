# Independent challenge: existence of all expected sine-Gram moments

Reviewer: li_advocate. Date: 2026-11-17. The spanning-tree mechanism was proposed by li_skeptic. I reconstructed the proof below before reading their draft. No issue was found in this inspected mechanism. The parent subsequently independently checked and accepted the scoped expected-model conclusion; the strengthened campaign and theoremTHM-SG309 now reference this review.

## Statement and scope

For the unit-density sine process and sinc Gram matrices G_R defined in `proposals/independent_campaigns/sine_gram_all_moments_round3.md`, every expected per-length moment

    m_{j,R}=(1/R)ETrG_R^j

has a finite R→∞ limit, for every fixed integer j≥1. Combining this with the separately proved uniform bound m_{j,R}≤4^j j! gives a unique full weak limit of the expected spectral measures. No almost-sure law, rate, growing-j limit, arithmetic prime-side moment asymptotic, or RH statement is asserted.

The proof is a self-contained graph-integrability argument plus the actual DPP correlation convention from Soshnikov Eq1.5/1.20. It does not assume the moment limits it is meant to prove.

## 1. Trace partitions and the quotient graph

Expand TrG_R^j as a closed walk of length j through process points, and partition positions1,...,j according to which positions have the same process point. Order the v blocks of a partition by their first occurrence, giving a sum over ordered v-tuples of **distinct** process points. The factorial moment formula gives the contribution

    ∫_[0,R]^v product_{ell=1}^j k(x_{b(ell)}−x_{b(ell+1)})
                 ρ_v(x1,...,xv) dx1...dxv,

with b(j+1)=b(1). There is no factor1/v!: the tuple is ordered by the chosen block ordering. There are finitely many partitions for fixed j.

If v=1 the contribution is R, since k(0)=ρ1=1. Suppose v≥2. Discard loops from the quotient of the closed j-cycle: they contribute k(0)=1. Distinguish parallel edges. The resulting undirected multigraph Γ is connected, because it is a quotient of a connected closed walk. Each vertex has even degree: before loop deletion its degree is twice the number of positions in that block, and each deleted loop removes two incidences.

A connected graph with all degrees even has no bridge. Indeed the sum of the degrees on either side of a purported bridge cut is even, whereas a single crossing edge would make it odd. Thus Γ is a connected **bridgeless** multigraph.

## 2. Rooted graph integrability via spanning-tree Hölder

For every edge e let θ_e be the probability that e belongs to a uniformly chosen spanning tree of Γ. Every nonloop edge belongs to some spanning tree, so θ_e>0. Because e is not a bridge, Γ−e is connected and has a spanning tree, so θ_e<1. These facts hold for distinguished parallel edges as well.

Fix x1=0 and put a_e=|k(x_i−x_j)| for edge e=(i,j). If T ranges over spanning trees with probabilities p_T, define

    f_T(x2,...,xv)=product_{e∈T} a_e^{1/θ_e}.

The exact pointwise identity is

    product_e a_e =product_T f_T^{p_T},

since the exponent of each a_e on the right is sum_{T∋e}p_T/θ_e=1. Weighted Hölder therefore gives

    ∫_(R^{v−1}) product_e a_e
       ≤product_T (∫f_T)^{p_T}.

For a rooted tree, leaf elimination factors the integral:

    ∫f_T=product_{e∈T} ∫_R |k(t)|^{1/θ_e}dt.

The sinc function belongs to L^p(R) for every p>1, using |k(t)|≤min(1,1/(π|t|)). Because1/θ_e>1, each factor is finite. Consequently

    ∫_(R^{v−1}) product_e |k(x_i−x_j)|
       ≤product_e (∫_R |k(t)|^{1/θ_e}dt)^{θ_e}<∞.     (GI)

This proves exactly the absolute integrability needed below. It does not use an unjustified claim that sinc itself is in L¹, and it does not discard the decay supplied by a parallel edge. The bridgeless property is crucial: a bridge would have θ_e=1 and this argument would encounter the nonintegrable L¹ norm.

## 3. Translation and the thermodynamic limit

The sine correlation function is translation invariant and0≤ρ_v≤1. Set u1=0 and u_i=x_i−x1. After integrating the location x1 of the whole configuration in[0,R], the normalized partition contribution is

    ∫_(R^{v−1}) (1−span(0,u2,...,uv)/R)_+
        product_{ell=1}^j k(u_{b(ell)}−u_{b(ell+1)})
        ρ_v(0,u2,...,uv) du2...duv.

The overlap factor is the exact length divided by R of the allowed translation interval; it lies in[0,1] and tends to1 pointwise. The absolute value of the remaining integrand is bounded by the integrable function in(GI), because ρ_v≤1. Dominated convergence gives a finite limit for each partition. Summing the finite set of partitions proves the stated fixed-j moment limit.

There is no need to expand the determinant into signed permutation terms or to bound divergent pieces separately. The determinant is retained as a bounded factor. This avoids a possible source of unjustified cancellations.

## 4. Consequences and limits

The previously established moment bound4^j j! makes the limiting moment sequence Hamburger determinate. Tightness of the expected spectral measures follows from their first moment1; uniform higher moments make every fixed power uniformly integrable. Thus every weak subsequential limit has the just-proved common moment sequence. Determinacy identifies all such limits and yields full **expected** weak convergence.

The separate thinning/quantile argument shows this limiting law has no atom at0. Therefore the model law needed for the all-fixed-moments conditional certificate exists uniquely and has the necessary zero-atom and determinacy properties. These are properties of the random sine-Gram model; the required zeta prime-side moment matching remains an unproved arithmetic input.

As a normalization check, j=1 gives m1=1. For j=2, the two partitions give

    m2=1+∫k(t)²(1−k(t)²)dt=1+1−2/3=4/3,

using Fourier Parseval for the interval indicator and its triangular self-convolution. This matches the source's unit-density normalization. The subsequent exact24-permutation/15-partition calculation in `sine_gram_fourth_moment_advocate_archived_round3.md` independently derives the fourth moment13/4 and has a separate parent autocorrelation check.

## Classification

Independently checked with no issue found in the inspected graph/Hölder/limit argument. This strengthens the campaign's deliberately conditional moment-existence scope. The exact PW² interpolation input used for the no-zero-atom component remains documented in the separate source review. Publication novelty and prior-art completeness are unassessed; no new RH claim is made.
