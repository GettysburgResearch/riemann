# Beurling 1955: full primary-source reconstruction

Date: 2026-11-17. Primary work: Arne Beurling, *A closure problem related to the Riemann zeta-function*, PNAS41(5) (15May1955),312–314, DOI [10.1073/pnas.41.5.312](https://doi.org/10.1073/pnas.41.5.312). Read in full from the official PMC facsimile images for pages312–314, available through https://pmc.ncbi.nlm.nih.gov/articles/PMC528084/ . The PDF endpoint returned an HTML challenge; the official page images were downloaded, read visually, hashed and OCRed. The first and last scan pages contain neighboring articles; only Beurling's article is counted as read.

The cited dependency was also read in full: Beurling, *A theorem on functions defined on a semi-group*, *Mathematica Scandinavica*1 (1953),127–130, DOI [10.7146/math.scand.a-10372](https://doi.org/10.7146/math.scand.a-10372), current publisher PDF https://journals.msp.org/mscand/article/download/2951/2950 . Its old mscand URLs failed; the migrated publisher PDF was obtained and all four scanned pages were read.

Overall source audit level:1 for each whole work, with detailed technical reconstruction of the explicit Mellin, support and duality steps. The canonical-factorization dependency of the 1953 proof is identified and checked for applicability but has not been independently reproved from the 1922 source. No Level3 adversarial reconstruction or exhaustive correction search is claimed.

## Exact theorem and spaces

Write ρ(u)={u}. Let C be the set of finite sums

f(x)=Σ_{ν=1}^n c_ν ρ(θ_ν/x),  0<θ_ν≤1,

subject to Σ_ν c_ν θ_ν=0. Original source: p.312, definition immediately before the theorem. The constraint implies f(x)=0 for x>1; each such function is bounded on(0,1).

For **each p with1<p<∞**, Beurling's theorem states

C is dense in L^p((0,1),dx) ⇔ ζ(s) has no zeros in Re(s)>1/p.

The half-plane inequality is strict. No assertion at p=1 or p=∞ is part of this theorem. In particular, p=2 gives RH after using the usual functional-equation symmetry and known absence of zeros outside the critical strip. The theorem is not restricted to p=2 and does not assume RH during its proof.

The original generators use continuously varying θ. The theorem does not restrict θ to reciprocal integers, does not choose Möbius coefficients, and makes no claim about convergence of a prescribed coefficient sequence.

## Dependency architecture

1. The constrained space C is invariant under compressed dilations T_a,0<a≤1.
2. Dilation invariance shows density is equivalent to approximating the constant1.
3. The exact fractional-part Mellin identity turns L^p approximation into zero exclusion by Hölder's inequality.
4. If density fails, L^p duality gives a nonzero annihilator g∈L^{p′}.
5. A dyadic test-function argument shows g cannot vanish on any interval adjacent to0.
6. Beurling's 1953 semigroup theorem produces a power character in the **weaker L^r closures**, r<p′, of the dilation orbit of g.
7. Since every test function in C is bounded, those weaker closures suffice to preserve annihilation.
8. The Mellin identity then forces a zero of ζ in Re(s)>1/p, contradicting zero-freeness.

This is the source's actual route. The 1955 note does not simply assume an outer-factor conclusion for every invariant subspace. Its external semigroup theorem and strict change of integrability exponent are essential.

## Independent check of the dilation reduction

For0<a≤1, define T_a f(x)=f(x/a) for0<x≤a and0 for a<x≤1. For f∈C,

T_a f(x)=Σ c_ν ρ(aθ_ν/x)

also for x>a, because then the right-hand side equals(a/x)Σc_νθ_ν=0. Thus T_a maps C into C and

||T_a f||_p=a^(1/p)||f||_p.

If1 lies in the closure of C, then so does1_(0,a)=T_a1 for everya; differences give interval indicators, whose finite spans are dense in L^p for finitep. The converse is immediate. This confirms the reduction on p.312 with the exact norm factor.

## Independent check of the Mellin identity and easy direction

For0<θ≤1 and Re(s)>0, with the removable singularity at s=1 understood,

∫_0^1 ρ(θ/x)x^(s−1)dx = θ/(s−1)−θ^s ζ(s)/s.       (B1)

One way to verify it is to start from ∫_0^∞ρ(θ/x)x^(s−1)dx=−θ^sζ(s)/s for0<Re(s)<1 and subtract the x>1 tail θ/(1−s). Both sides then continue analytically to Re(s)>0. For a constrained f, the θ/(s−1) terms cancel, giving Beurling's equation(2):

∫_0^1 f(x)x^(s−1)dx=−[ζ(s)/s]Σc_ν θ_ν^s.           (B2)

Let r=p/(p−1) be the dual exponent; the original 1955 source calls this exponentq. If ||1+f||_p<ε and σ=Re(s)>1/p, then

|1−ζ(s)Σc_νθ_ν^s|
≤ ε |s|/[r(σ−1/p)]^(1/r).                         (B3)

Indeed ∫_0^1|x^(s−1)|^r dx=1/[r(σ−1/p)]. For any fixed s in that half-plane the right side can be made less than1, excluding ζ(s)=0. The source further records the quantitative zero-free region σ>1/p+ε^r|s|^r/r. This check preserves the strict inequality and all integrability conditions; no Mellin evaluation on the boundary Re(s)=1/p is used.

## Independent check of the annihilator-support lemma

Suppose g∈L^r(0,1) annihilates C and vanishes almost everywhere on(0,a). Choose a<b<min(1,2a) and define

f_(a,b)(x)=bρ(a/x)−aρ(b/x).

The coefficient constraint is ba−ab=0. This f vanishes for x>b and equalsa on(a,b), because a/x<1 and1<b/x<2 there. Belowa it may be nonzero, but g is zero there. Hence

0=∫_0^1 f_(a,b)(x)g(x)dx=a∫_a^b g(x)dx.

As this holds for every suchb, g vanishes almost everywhere up to min(1,2a). Iterating finitely many times gives g=0 on(0,1), a contradiction. Thus any nonzero annihilator has ∫_0^x|g(t)|dt>0 for everyx>0. This is equation(8), p.314, and the hypothesis needed for the semigroup theorem on p.313.

## The semigroup-character step, with its exact topology

For g∈L^r, r=p/(p−1)>1, let E_g^u be the closure in L^u(0,1) of span{g(ax):0<a≤1}. The 1955 note invokes the following consequence of the 1953 theorem:

If g has no initial interval on which it vanishes, there is λ with Re(λ)>−1/r such that x^λ belongs to E_g^u for every1≤u<r. It need not belong to E_g^r.

From dilation invariance and annihilation,

0=∫_0^1g(x)T_a f(x)dx=a∫_0^1g(ax)f(x)dx.

Every f∈C is bounded, so the functional h↦∫hf is continuous even in L¹. Therefore the character x^λ also annihilates C despite being supplied only in weaker closures. Put s₀=1+λ. Then Re(s₀)>1−1/r=1/p.

For θ∈(0,1), use f_θ(x)=ρ(1/x)−θ^(−1)ρ(θ/x)∈C. Equation(B2) gives the source's equation(9):

0=∫_0^1 f_θ(x)x^(s₀−1)dx=[(θ^(s₀−1)−1)/s₀]ζ(s₀).

The exceptional point s₀=1 is excluded explicitly: the removable limiting value of the right side is logθ≠0. For s₀≠1, chooseθ with θ^(s₀−1)≠1; such a choice exists because the expression is not identically1 as a function ofθ. Therefore ζ(s₀)=0 in Re(s)>1/p. This completes the converse conditional on the cited semigroup theorem.

## Inspection of the 1953 dependency

TheoremI, p.128, is formulated for f∈L^P(0,1),1<P<∞, with no initial support gap. Let C_f^u be the L^u closure of its multiplicative dilation orbit. It defines

Γ_f^P = (intersection over1≤u<P of C_f^u) ∩ L^P.

Then Γ_f^P contains a character x^(−λ) with Re(λ)<1/P. The sign of λ differs from the normalized positive exponent in the 1955 argument; replacing λ by−λ reconciles them.

Its first page explicitly explains that corresponding character existence in the original L² closure is **false** in general. Thus replacing Γ_f^P by C_f^P would be an unjustified and potentially false strengthening.

The proof on pp.128–130 can be reconstructed as follows.

* For an annihilator k∈L^{u′},u<P, extend f,k by0 past1 and form g(ξ)=∫_0^∞k(x)f(ξx)dx. Annihilation gives g(ξ)=0 for0<ξ≤1. Hölder yields |g(ξ)|≤||k||_{u′}||f||_P ξ^(−1/u) for ξ>1.
* The Mellin transforms G(s)=∫_1^∞g(ξ)ξ^(s−1)dξ and K(s)=∫_0^1k(x)x^(−s)dx converge absolutely for Re(s)<1/u; F(s)=∫_0^1f(x)x^(s−1)dx converges for Re(s)>1/P.
* In the nonempty overlap1/P<Re(s)<1/u, absolute double-integral convergence permits Fubini and gives G=KF. If all such annihilators vanish, the required weaker closures are already the whole spaces. Otherwise F continues meromorphically through the left half-plane as G/K.
* The bound |F(σ+it)|≤const·(σ−1/P)^(−1+1/P) has exponent less than1. It excludes a meromorphic pole on Re(s)=1/P. Any pole λ to its left forces K(λ)=0 for **every** relevant annihilator, placing x^(−λ) in every weaker closure by duality.
* If F has no pole and is entire, the source applies the Nevanlinna canonical decomposition to bounded analytic G,K in a left half-plane. Their Mellin definitions make them regular at every finite boundary point of a selected line Re(s)=α between1/P and1/u. Zero inclusion follows from entire F=G/K. The only remaining singular term is the linear harmonic contribution at infinity, giving |F(s)|≤M exp(c(Re(s)−α)) on the left and a uniform bound on the right.
* If c≥0, Liouville and F(σ)→0 as σ→∞ force F=0. If c<0, set a=e^c and form F₁(s)=∫_0^1 f(ax)x^(s−1)dx=a^(−s)[F(s)−∫_a^1f(x)x^(s−1)dx]. It is entire and bounded in both half-planes, hence0; this forces f to vanish on(0,a), contradicting the support hypothesis.

The final canonical-decomposition step relies on the theorem of F. and R. Nevanlinna cited as the 1922 reference on p.130. Its role and applicability conditions are explicit here; this audit has not independently proved that entire canonical-factorization theorem. It is not an RH assumption. The Fubini, support, exponent and duality steps were independently checked in this reading.

## Relation to the later full-half-line and discrete variants

Beurling's C uses continuousθ and the exact constraint Σcθ=0 on L^p(0,1). Later formulations use unconstrained finite sums on the full half-line and a target interval indicator. At p=2 the constraint can be restored by a controlled anchoring operation, but the norm domain must be retained.

Indeed let g(x)=Σc_νρ(θ_ν/x), A=Σc_νθ_ν and χ=1_(0,1). On x>1, g(x)=A/x. Therefore ||g−χ||_L²(0,∞)≥|A|. The anchored function g−Aρ(1/x) has coefficient sum0 and

||g−(g−Aρ(1/x))||_L²(0,∞)=|A|·||ρ(1/x)||_L²(0,∞).

Thus full-half-line convergence forces A→0 and yields an anchored approximating sequence; constrained functions already vanish beyond1, so the converse is immediate. This is an elementary equivalence of formulations, not the deep discrete strengthening.

Báez-Duarte's later theorem restricts θ to1/n while preserving closure equivalence. That restriction is not present in Beurling1955 and cannot be inferred just from the dilation argument. No prescribed fixed coefficient array follows from either closure theorem.

## Findings, limitations and useful negative knowledge

Classification: **independently checked with no issue found in the inspected explicit proof architecture**, conditional on the clearly identified canonical-factorization dependency. Two whole primary works were read, not merely their abstracts.

The most reusable caution is topological: the 1953 character theorem deliberately weakens L^P closure to all L^u,u<P. General invariant spaces need not contain a character in their original norm topology. The 1955 RH criterion succeeds because its test functions are bounded, so weaker convergence still preserves annihilation. A proposed transplantation to an unbounded test class would require new uniform integrability or another continuity argument.

Next precise task: reconstruct the 1922 factorization step in modern half-plane bounded-type language, including the singular term at infinity, then formalize the support propagation and Hölder/Mellin portions separately. No result here advances RH itself or establishes a new convergence rate.
