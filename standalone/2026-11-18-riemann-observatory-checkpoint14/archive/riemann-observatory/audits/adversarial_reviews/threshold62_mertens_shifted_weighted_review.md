# Independent review of the shifted Möbius array rate

2026-11-17. Reviewer threshold_review_62. This checks the conditional transfer, the converse, and the separate ratio-slope corollary. No novelty or optimality judgment. [Candidate proof](../../proposals/independent_campaigns/mertens_shifted_weighted_latest62_round5.md) [Candidate records](../../theorems/mertens_shifted_weighted_latest62_round5.jsonl)

## Exact inputs

The actual Bui–Florea–Heycock arXiv:2610.27591v1 PDF, p. 4, Theorem 1.4, assumes RH and gives for each integer k≥1 an upper bound √x exp(C(k)(log x/log log x)^(k/(k+1))) for the absolute generalized Möbius sum. Their discussion on p. 3 defines μ_k(n) as the coefficients of ζ(s)^(−k), so k=1 is the ordinary Möbius function. This review treats the theorem as an external input and checks its application. [Bui–Florea–Heycock PDF](../../sources/recent_corpus_round5/2610.27591.pdf)

The actual arXiv:0812.1689v1 PDF gives the precise q=1 decomposition for this shifted coefficient family on p. 4, Proposition 1, and J_ε≪ε under RH on p. 5, Proposition 2. J_ε uses dt/(2π|s|²), with s=1/2+it. The candidate link to p. 4 locates the decomposition, and the ratio estimate appears on the following page. Classical convexity at σ=1/2 is Titchmarsh (1986), §5.1, equation (5.1.5). The RH implication of Lindelöf is recorded at the close of §14.2. [Balazard–de Roton PDF](../../sources/selberg_round2/balazard_roton.pdf) [Titchmarsh PDF](../../sources/equivalence_round2/titchmarsh1986.pdf)

## Abel endpoint and the full real-line bound

Suppose |M(x)|≤K√x exp(F(log x)) eventually, with F eventually C¹ and concave and F(u)=o(u). Use integer N large enough that all x≥N are in the bound and u≥L=log N in the concavity range. For z=s+ε, ε>0, partial summation on N<n≤Y gives the upper term M(Y)Y^(−z), the lower term −M(N)N^(−z), and +z∫_N^Y M(x)x^(−z−1)dx. The lower term uses M(N) and so excludes n=N from the remainder. The upper term tends to zero and the integral converges absolutely since F(u)−εu≤−εu/2 for all sufficiently large u. Away from Re z=1/2 this convergence is locally uniform by the same estimate with ε bounded below and |z| bounded. Agreement with the Euler-product reciprocal on Re z>1 identifies the holomorphic sum with 1/ζ(z) under RH on Re z>1/2, including its value zero at the removable reciprocal singularity z=1. Thus the sign and endpoint in (3) are correct.

Set E=εL−F(L), λ=ε−F′(L)>0. The global supporting line for concavity on u≥L gives F(u)−εu≤−E−λ(u−L). After x=e^u the tail identity has form
    reciprocal minus polynomial = −M(N)N^(−s−ε) + (s+ε) ĝ(t),
where g(u)=1_{u≥L} M(e^u)exp(−(1/2+ε)u). Its Fourier transform has kernel e^(−itu). Then ∥g∥_1≤Ke^(−E)/λ and ∥g∥_2≤Ke^(−E)/√(2λ). Both inequalities hold on the entire tail from L to infinity, independent of whether E is positive. The Fourier-Plancherel convention gives ∥ĝ∥_{L²(dt/(2π))}=∥g∥_2. Because g is also in L¹, the transform here agrees pointwise with the absolutely convergent integral.

The boundary norm of ζ(s)/s is finite. For large |t|, convexity gives the squared integrand O((1+|t|)^(−3/2+2η)) with any η in (0,1/4). Compact t causes no failure, since ζ is analytic on the critical line and |s|≥1/2. This handles the Abel endpoint term for q≥1 by |s|^(1−q)≤2^(q−1). For q≥2 the estimate |ĝ|≤∥g∥_1 works on the entire real axis, since |s+ε|≤(1+2ε)|s| and |s|^(2−q)≤2^(q−2). This argument works for every real q≥2 in particular.

For every fixed real q>1, choose 0<η<q−1. Under RH, Lindelöf gives |ζ(s)|≪_η(1+|t|)^η on the critical line. Thus ζ(s)(s+ε)/|s|^q is bounded uniformly in t and 0<ε≤1/4, since it is O((1+|t|)^(η+1−q)). This goes into the Plancherel estimate and yields the truncation error O_q(Ke^(−E)(1+λ^(−1/2))). This argument requires positive q−1 in its choice of η. The q=1 truncation estimate is outside this proof.

The quotient defect is bounded by 2^(q−1)√J_ε for q≥1, using the exact critical-line inequality above. Minkowski now gives O_q(√ε+Ke^(−E)(1+λ^(−1/2))) for real q>1. No truncation of the t-integral or constants tied to bounded t are needed.

## The specified shift

For φ(u)=√(u/log u), direct differentiation gives
    φ′(u)=(log u−1)/(2√u(log u)^(3/2)),
    φ″(u)=(3−(log u)²)/(4u^(3/2)(log u)^(5/2)).
In particular φ is concave for u>exp(√3), and φ(u)/u→0. With F=Cφ and ε=A/√(L log L), E=(A−C)φ(L) and
    λ=[A−(C/2)(1−1/log L)]/√(L log L).
It is positive for all sufficiently large N when A>C, and λ≍_{A,C}ε. Since φ(L)/log L→∞ and λ inverse grows at most polynomially in L, the truncation term is o(√ε) and indeed smaller than every fixed inverse power of L. The ratio defect is O(√ε), giving d_q(P_N)=O((log N log log N)^(−1/4)) over the full sequence. Its square is O((log N log log N)^(−1/2)). Constants depend on the fixed parameters and source bounds.

## Converse for real q≥1

For any finite Dirichlet polynomial D(s)=Σ a_n n^(−s), let A_D=D(1) and define h_D(x)=1+Σ a_n{1/(nx)} for 0<x≤1. This bounded function belongs to L²(0,1). Its Mellin transform H_D belongs to H²(Re s>1/2) with norm measured by boundary dt/(2π). The fractional-part Mellin identity on 0<Re s<1, after subtracting the elementary tail beyond x=1, gives H_D(s)=(1−ζ(s)D(s))/s+A_D/(s−1). This is an analytic identity with its removable singularity understood.

Use the principal branch of Log s on the right half-plane and define s^(−q)=exp(−q Log s). Since q is real, its modulus is |s|^(−q). Put b_1(s)=(s−1)/s. It is bounded by one in modulus on Re s>1/2 and has boundary modulus one. Thus
    b_1(s)(1−ζ(s)D(s))s^(−q) = b_1(s)H_D(s)s^(1−q)−A_D s^(−q)
belongs to H². The first term uses a bounded analytic multiplier and the second uses s^(−1)∈H² and the same multiplier. The representation proves Hardy membership and cancellation at s=1 directly. Its Hardy norm is d_q(D) exactly. At an interior zeta zero ρ=β+iγ, β>1/2, its value is (ρ−1)/ρ^(q+1). Mellin representation and Cauchy–Schwarz give the point evaluation norm 1/√(2β−1), so d_q(D)≥√(2β−1)|ρ−1|/|ρ|^(q+1)>0 for every D. Therefore subsequence convergence for the prescribed arrays and any fixed A>0 excludes all such zeros. Reflection excludes nontrivial zeros to the left, proving RH. The argument uses no assumptions about spacing or monotonicity of the subsequence. [Existing integer Hardy audit](../weighted_criterion_round2.md)

## Separate ratio-slope corollary

For fixed q≥1, let W(t)=|1/2+it|^(−2(q−1)). It is bounded, continuous, and positive. Multiply the measure dν=dt/(2π|s|²) of the independently adjudicated Poisson exhaustion by W. For each finite set of zeros use the bounded rescaling windows t=γ+εu with |u|≤R fixed. W(γ+εu)→W(γ) uniformly on every such window. The weighted limiting local masses on these windows are the original local squared-defect masses multiplied by W(γ). The large-|u| limit and the sum over zeros are justified by exhausting the unweighted positive real-defect mass first: on the omitted set contractivity bounds the weighted squared defect by 2∥W∥∞ times the original real defect. This shows that arbitrary large-height contributions are controlled as well. The whole-line O(ε) norm bound for the completion ratio passes to √W times the completion error with factor √∥W∥∞. The resulting change after squaring is O_q(ε^(3/2)), hence o(ε).

The completed-to-uncompleted argument thus gives weighted squared quotient defect asymptotic to ε S_q with the proposed coefficient. Its series converges absolutely by the unweighted exhaustion and W bounded. It is strictly positive by existence of nontrivial zeros and the positive contribution from each multiplicity. For the full array, fixed q>1, the previous truncation estimate gives a norm o(√ε_N). The reverse triangle inequality implies d_q(P_N)=√(S_q ε_N)+o(√ε_N) and the stated squared asymptotic. The transported ratio limit itself includes q=1. The full-array asymptotic uses the q>1 truncation bound. This is a statement about one coefficient array and one shift for each admissible A. [Ratio-slope adjudication](horizontal_ratio_slope_director_adjudication_round5.md)

I found no gap in the scoped transfer, real-q converse, or the optional corollary with the declared inputs.
