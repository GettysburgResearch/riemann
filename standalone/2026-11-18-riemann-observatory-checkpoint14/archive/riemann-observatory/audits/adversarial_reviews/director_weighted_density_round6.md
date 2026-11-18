# A precise weighted replacement for the BGSTB density premise

The director independently reconstructed the proposed refinement from the already checked retained-horizontal-denominator repair, read the proposal and independent ratio62 review, and checked endpoint atoms, the moving-profile countermodels and height exponents. This is a conditional refinement, not a new unconditional density estimate or a claim about the inaccessible journal version. Source is BGSTB arXiv2306.04799v1 §§2,4–7; its later horizontal grouping method is in2501.14545v3 §§1–2,6. Full source scopes remain in their paper records.

Let L=logT,a=1/2,B=L/2. Count zeros with multiplicity and 0<γ≤T. Define μ_T on[a,B] by right-side displacement y=L(β−1/2); D_T(y)=μ_T([y,B]) is inclusive. Put G(y)=e^(2y)/(1+y²), r_T(y)=e^(2y)D_T(y)/T. Then the following condition suffices for the source far-pair sum S(T)=o(TL):

    r_T(a)+∫_a^B r_T(y)/(1+y²)dy →0.                 (A)

It is necessary and sufficient for *this nonnegative horizontal majorant* to be o(T). No necessity assertion for the signed S(T) is made.

For a far pair assign a copy of maximal m=L|β−1/2|≥1/2 as outer zero. Write d=L|β−β′|≥1 and v=L(γ−γ′); then d≤2m. Source kernel bounds give Ce^d/(d²+v²). Set q=2m−d≥0; since m/d≤(1+q)/2, multiplying the ratio(1+m²+v²)/(d²+v²) by e^(−q) is bounded. Thus a pair is bounded by Ce^(2m)/(1+m²+v²). Unit-window O(L) counts, with multiplicities, give the sum over partners O(L/(1+m²))+O(1/L)=O(L/(1+m²)); the last absorption uses m≤L/2. Reflection preserves height, displacement and multiplicity, so

    |S(T)|≤CL M_T,  M_T=∫_[a,B]G(y)μ_T(dy).

Summing the identity G(x)=G(a)+∫_a^BG′(y)1_{y≤x}dy over the atoms gives the exact formula, including an atom at a,

    M_T/T=(4/5)r_T(a)+∫_a^B
       [2−2y/(1+y²)] r_T(y)/(1+y²)dy.

The bracket is in[1,2] for y≥a. This proves(A) with explicit two-sided comparison constants and no microscopic occupancy assumption. D_T(a)=o(T) forces r_T→0 uniformly on each fixed compact interval; weighted tail tightness is exactly the remaining premise. Uniform bounds by C(1+y)^p with p<1 and scaled pointwise decay are one sufficient dominated-convergence condition.

## Negative implication controls

An atom of mass⌊T⌋ at a gives a nonzero boundary contribution and zero Lebesgue integral, so the endpoint term cannot be dropped. Put Y=(logT)^(1/4). An atom of multiplicity⌊T e^(−2Y)(1+Y²)⌋ at Y has local-uniform scaled decay and vanishing full-interval unweighted mean, but M_T/T→1. Replacing its count by⌊T e^(−2Y)⌋ gives M_T/T→0 while r_T(Y)→1. Thus(A) is weaker than uniform scaled little-o among abstract counting profiles, and local convergence alone does not imply it.

These profiles fit the two quoted Guth–Maynard power envelopes: throughout their occupied σ-range, σ=1/2+o(1), those exponents exceed1 by a fixed amount, while the example has o(T) displaced mass. Above that range the profile is empty. This disproves an implication from these power inequalities alone. It does not construct an actual zero distribution, a jointly consistent all-height model, or a counterexample to a zeta density conjecture.

## Height localization with a closed endpoint

Assume separately the source's uniform bound N(σ,X)≪X^(2(1−σ)) for σ*≤σ≤1, with fixed1/2<σ*<1 and the stated fixed-margin conventions. This is a declared input, not independently re-proved here. For 0<θ≤2(1−σ*) let X=T^θ. On β≤σ*, the low-height count is O(X logX) and G(L(β−1/2))≤C T^(2σ*−1)/L² at the upper endpoint (monotonicity handles all smaller displacements). Its total is O(T^(θ+2σ*−1)/L)=o(T), including equality inθ. Aboveσ*, the layer integrand is bounded by

    C T L^(-2) exp[−2(1−θ)(B−y)],

whose integral and lower boundary term are O(T/L²). Thus the low-height moment is o(T), and(A) may be imposed only on T^θ<γ≤T. For sourceσ*=25/32+η,θ=3/8 includes η=1/32, provided the uniform fixed-margin input is available there. This endpoint saving comes from retaining G's denominator, rather than bounding it by e^(2y).

## Consequences and their exact counting meanings

Using the source kernel positivity and Lemma7, M_T=o(T) gives the same bound limsup Σ_{distinctρ}mρ²/N(T)≤C_K. The diagonal inequality1_{m=1}≥2m−m² gives simple-zero proportion≥2−C_K, wherever those simple zeros lie.

To obtain an intersection statement, use the separately inspected horizontal-grouping method. Condition(A) gives D_T(a)=o(T). The good strip |β−1/2|<1/(2L) therefore contains N_good=N(T)−o(T) copies. At each ordinate g, let H_good(g) count those copies. Any two are a near pair. The source integral representation with nonnegative j(α)sechα implies K(iu)≥K(0), hence Σ_gH_good(g)²≤(C_K+o(1))N(T). A group of size1 must lie on the line and be simple by reflection. Its count is at least2N_good−ΣH_good². Thus the same2−C_K is a lower bound for simple *and* critical-line zeros under these additional steps.

A good copy outside the union(simple OR critical line) is an off-line multiple copy; its reflected multiple point forces H_good≥4. Consequently the number of omitted good copies is≤(ΣH_good²−N_good)/3, giving union proportion≥(4−C_K)/3. For the inspected Montgomery–Taylor test these are about0.61748 and0.87249. They are conditional consequences of this premise and test, not current-best bounds; later separately verified finite-window constants are stronger.

Evidence: proposals/independent_campaigns/threshold62_weighteddensity_bgstb.md; audits/adversarial_reviews/ratio62_weighteddensity_bgstb.md; retained-denominator and follow-up source reviews. Next precise step is a theorem controlling the weighted scaled-displacement tail, possibly with the proposal's dyadic partner-occupancy refinement. Existing broad power density estimates alone do not provide it.
