# A weighted density condition for the BGSTB far-pair sum

2026-11-17. Scoped mathematical reconstruction from arXiv:2306.04799v1. This is a conditional replacement premise for the §6 far-pair estimate. Priority unassessed.

## Source scope and notation

I inspected the actual arXiv:2306.04799v1 PDF passages in §2, Lemmas 6–7, §6 on pp. 9–10, and the first application in §7. The two inputs to the estimate are Tsang's Lemma 6(b) bound on the complex kernel and the unit-window count (2.5). Both are used below. The kernel positivity in Lemma 6(c), Lemma 7's main term, and the diagonal comparison in §7 are separate source inputs to the multiplicity consequence. Theorem 2's box assumes the strict real-part bounds for T^(3/8)<γ≤T. Theorem 3 uses the strong density premise (6.2), up to σ*=25/32+η. The continuation above σ* uses the Bourgain bound cited as (6.5). These are source-specific thresholds and windows. [BGSTB primary PDF](../../sources/analytic/2306.04799.pdf) [Retained kernel review](../../audits/adversarial_reviews/witness62_bgstb_section6.md)

Write L=log T, a=1/2, b=L/2. Count nontrivial zeros with multiplicity. Define μ_T as the counting measure on [a,b] that puts one unit at y=L(β−1/2) for each zero ρ=β+iγ with 0<γ≤T and β≥1/2+a/L. Then D_T(y)=μ_T([y,b])=N(1/2+y/L,T) on this interval, with endpoints inclusive. Put G(y)=exp(2y)/(1+y²).

## Reduction to a horizontal moment

For a far pair, choose a member whose m=L|β−1/2| is maximal. Then d=L|β−β′|≥1, d≤2m≤L, and v=L(γ−γ′). The source kernel bound and boundedness of w give the positive majorant C exp(d)/(d²+v²). Indeed w(z)=4/(4−z²), and for |Re z|≤1 the denominator has real part at least 3+(Im z)². To estimate the kernel let q=2m−d≥0. The quotient (1+m²+v²)/(d²+v²) is bounded by 1+(1+m²)/d²≪(1+q)². After multiplication by exp(−q) it is bounded uniformly. Therefore the pair contributes at most C exp(2m)/(1+m²+v²). Charging each ordered pair once and extending to all partners costs at most an absolute factor of two. Reflection ρ↦1−conj(ρ) preserves positive height, the value of m, and multiplicity, so the outer sum reduces to zeros on the right of the line.

For a fixed outer zero the partners with |γ−γ′|<1 contribute O(L/(1+m²)); use (2.5) on a bounded number of unit intervals. Each two-sided shell j≤|γ−γ′|<j+1, j≥1, contains O(L) ordinates counted with multiplicity and contributes O(L/(jL)²). Their total O(1/L) is O(L/(1+m²)) because m≤L/2. Thus the full far-pair sum in (5.2) satisfies
    |S(T)| ≪ L ∫_[a,b] G(y) μ_T(dy).
The unit-window bound gives O(L) possible partners in the first shell. It provides no microscopic O(1) occupancy assumption.

## Exact Stieltjes identity and weakest input for this majorant

For each atom x∈[a,b], use G(x)=G(a)+∫_a^x G′(y)dy. Summing gives the exact inclusive formula
    ∫_[a,b] G dμ_T = G(a)D_T(a)+∫_a^b G′(y)D_T(y)dy.
The atom at a is counted by the first term, and the upper endpoint needs no additional term. In Stieltjes notation, d(−D_T) here means the positive measure defined by the atoms, with the lower endpoint included. This convention avoids assigning a jump at an endpoint by the wrong one-sided tail value.

Explicitly,
    G′(y)e^(−2y) = (2−2y/(1+y²))/(1+y²).
For y≥a the numerator lies in [1,2], since 0≤2y/(1+y²)≤1. In particular G is increasing. If r_T(y)=e^(2y)D_T(y)/T, the following are equivalent with absolute comparison constants:
    ∫_[a,b] G dμ_T = o(T)
    and
    r_T(a)+∫_a^b r_T(y)/(1+y²)dy → 0.
Either implies S(T)=o(TL). This is the exact density requirement for the displayed horizontal majorant to be o(TL). The signed far-pair sum can be smaller by cancellation, and sharper vertical information can also improve the majorant.

If one uses an explicit envelope D_T(y)≤T e^(−2y) R_T(y), it suffices that R_T(a)→0 and the weighted integral of R_T tend to zero. Equivalently for the actual normalized counts, impose D_T(a)=o(T) and weighted tail tightness
    lim_{R→∞} limsup_{T→∞} ∫_R^b r_T(y)/(1+y²)dy = 0.
The boundary count forces r_T→0 uniformly on each fixed [a,R] by D_T(y)≤D_T(a), and the weighted integral condition then reduces to the tail estimate. For example, pointwise convergence with a uniform envelope C(1+y)^p for p<1 suffices by dominated convergence. The source's upper-range O(T e^(−2y)) for y≥(σ*−1/2)L makes that piece of the weighted integral O(1/L); it does not handle the intermediate moving y-range.

## Logical tests of the quantifiers and known estimates

The following are abstract integer-valued tails on one scale T. They test implications between density bounds and do not specify zeta-zero locations or a jointly consistent zeta-like distribution across T.

* The separate boundary term is needed. Put floor(T) atoms at a. The integral of r_T over [a,b] is zero, but the Stieltjes moment is comparable to T.
* Pointwise or locally uniform decay is insufficient, even if supplemented by vanishing unweighted means over the full interval. Choose Y=L^(1/4), and place floor(T e^(−2Y)(1+Y²)) atoms at Y. Then D_T(y) equals that number up to and including Y, and zero above. For every fixed R its r_T tends to zero uniformly on [a,R]. Also L^(−1)∫_a^b r_T(y)dy≪(1+Y²)/L→0. Nevertheless T^(−1)∫G dμ_T→1. The normalization is sharp here, because T e^(−2Y)(1+Y²)→∞ and rounding is negligible.
* A weighted condition can hold while the uniform little-o of (6.2) fails. Replace the preceding atom count by floor(T e^(−2Y)). Its normalized horizontal moment tends to zero, while r_T(Y)→1 and Y belongs to the interval in (6.2) for all sufficiently large T. Thus this is a genuine weakening at the level of allowable density profiles.

Guth–Maynard's primary Theorem 1.2 uses the inclusive convention Re ρ≥σ, |Im ρ|≤T. It bounds the count by T^[15(1−σ)/(3+5σ)+o(1)], and their equation (1.4) gives T^[30(1−σ)/13+o(1)]. Under conjugation symmetry these also bound the positive-height count, with irrelevant fixed factors. At σ=3/4 the first exponent is 5/9, whereas r_T's comparison exponent is 2(1−σ)=1/2. The difference is 1/18. The second bound has the same mismatch with a gap of 1/13 there. More directly, for our moving atom above, throughout the occupied interval σ≤1/2+Y/L=1/2+o(1) both published power exponents exceed 1 by a fixed amount for large T; the atom count is o(T) and vanishes above that interval. Hence even the pure power forms of both upper bounds and the order of the total zero count do not imply the weighted condition. This demonstrates the failure of that inference without alleging anything about the actual normalized zeta-zero tail. [Guth–Maynard primary PDF, Theorem 1.2 and (1.4)](../../sources/analytic/2405.20552.pdf)

## A high-height window version

Fix σ*=25/32+η<1 and 0<θ<2(1−σ*). Let X=T^θ, and retain the source's uniform consequence N(σ,X)≪X^(2(1−σ)) on σ*≤σ≤1. Then the contribution to ∫G dμ_T from 0<γ≤X is o(T), with y still scaled by log T.

For the low-height atoms with β≤σ*, the total count is O(X log X), while G(L(β−1/2))≤T^(2σ*−1). Their contribution is O(T^(θ+2σ*−1)L)=o(T). For β≥σ*, write y*=(σ*−1/2)L. Use the layer identity starting at y*, including its boundary count. On this part G(y)≪e^(2y)/L² and G′(y)≪e^(2y)/L². Multiplying by the low-height count gives at most
    C T L^(−2) exp(−2(1−θ)(b−y))
for the boundary term at y* and the integrand. Its integral in y and its value at y* are O(T/L²), because θ<1. This calculation uses no zero-free cutoff near β=1.

Consequently the weighted condition need only be imposed on the count of T^θ<γ≤T, with the same horizontal scale L and the same inclusivity at a. At θ=3/8 this applies with 0<η<1/32. The source's strict box in this window makes the high-height count zero, but a weighted upper bound permits zeros outside the box. If the Bourgain input for the low-height upper range is omitted, this localization step requires independent control of that low-height contribution.

## Optional replacement using local partner counts

To retain vertical information, for each right outer zero let Z_T(γ,r) count all partners with 0<γ′≤T and |γ′−γ|≤r, with multiplicity. Put u_m=√(1+m²)/L. Summing on the ball of radius u_m and the dyadic annuli 2^(j−1)u_m<|γ′−γ|≤2^j u_m gives
    ∑_{γ′} 1/(1+m²+L²(γ−γ′)²)
    ≪ (1+m²)^(−1) ∑_{j≥0} 2^(−2j) Z_T(γ,2^j u_m).
Indeed each term in annulus j≥1 is at most 4·2^(−2j)/(1+m²). This yields the sufficient localized premise
    ∑_{right outer ρ} G(m) ∑_{j≥0} 2^(−2j) Z_T(γ,2^j u_m) = o(TL).
Reflection preserves γ and m as required. The inner occupancy quantity is O(L) by the source unit counts, since Z_T(γ,r)≪L(1+r), u_m≪1, and both geometric sums converge. This premise permits using any stronger local information available for the charged pairs. No stronger vertical bound is inferred here from (2.5).

## Finite-moment consequence

For the fixed Tsang kernel in Lemma 7, the weighted premise yields S(T)=o(TL). Lemma 7 and the strict positivity in the near-pair region permit the same diagonal moment bound as §7, since a distinct zero of multiplicity m_ρ contributes m_ρ² ordered coincident pairs. Thus the limsup of ∑_distinct m_ρ²/N(T) is at most C_K=[K̂(0)+2∫_0^1 αK̂(α/(2π))dα]/[2πK(0)]. The distinct simple-zero count is at least 2N(T)−∑_distinct m_ρ², by applying 1_{m=1}≥2m−m² to each distinct zero. The resulting liminf is at least 2−C_K, with the source numerical value about 0.617483786 for the Montgomery–Taylor kernel (§7, p. 12). The conclusion uses the stated fixed tests and positive-ordinate count. It supplies no unconditional new zero-density bound.
