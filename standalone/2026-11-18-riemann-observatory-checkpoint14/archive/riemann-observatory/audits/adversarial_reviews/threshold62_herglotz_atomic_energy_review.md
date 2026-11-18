# Independent boundary-energy review for a finite Cauchy measure

2026-11-17. Reviewer threshold_review_62. I reconstructed the boundary kernel, Fourier identity, and finite-atom profile from the statement before reading the candidate proof. The reconstruction verifies the limit for a finite positive measure without a support or spacing restriction. Priority unassessed. [Candidate proof](witness62_herglotz_atomic_energy.md)

## Analytic increment and boundary

For a finite positive Borel measure μ, the integral G(w)=∫(w−iγ)^(−1)μ(dγ) is holomorphic for Re w>0 by uniform resolvent bounds on compact subsets. It has nonnegative real part. Let A_ε=∫_0^ε G(w+r)dr and H_ε=exp(−A_ε). Then H_ε is contractive and holomorphic. For fixed ε and boundary coordinate t the limiting resolvent majorant is
    ∫_0^ε |r+i(t−γ)|^(−1) dr = arsinh(ε/|t−γ|).
This function of t−γ is integrable on every bounded interval, with a uniform integral on all translates of an interval of fixed length. Indeed its only singularity, at zero, is logarithmic, and it is bounded outside [−1,1]. Since μ is finite, Tonelli makes the iterated majorant finite for almost every t, even without compact support. For s=Re w>0 the absolute resolvent is bounded by the same integrand. Dominated convergence as s↓0 gives the horizontal boundary formula for A_ε, and then for H_ε. The boundary real part of A_ε remains nonnegative. Equality of horizontal values with the almost-everywhere Hardy boundary values also follows from the bounded analytic Fatou theorem for H_ε.

## Fourier identity and the diagonal mass

Use μ̂(u)=∫e^(iuγ)μ(dγ). For s>0 the Laplace resolvent and Fubini give
    A_ε(s+it)=∫_0^∞ e^(−itu)e^(−su) [(1−e^(−εu))/u] μ̂(u)du.
Fubini is justified by e^(−su) min(ε,u^(−1)) times the finite total mass. With the unnormalized inverse Fourier integral displayed here, the squared L²(dt) norm is 2π times the squared frequency norm. The integrand without e^(−su) is square-integrable, so the formula converges in L² as s↓0. It yields the same almost-everywhere limit by subsequence uniqueness and the preceding dominated convergence proof. The exact scaled identity is
    ∥A_ε(it)∥²_L²(dt)/ε = 2π ∫_0^∞ K(v)|μ̂(v/ε)|²dv,
where K(v)=(1−e^(−v))²/v². An independent integral computation uses integration by parts, followed by (e^(−v)−e^(−2v))/v=∫_1^2 e^(−uv)du. Thus ∫_0^∞ K(v)dv=2∫_1^2 du/u=2log 2. Boundary terms at zero and infinity vanish.

Expanding |μ̂|² under the integral gives a bounded integrand after integration in v, because K is integrable. For γ≠γ′ the transform tends to zero by Riemann–Lebesgue at (γ−γ′)/ε. For γ=γ′ it equals 2log 2. Dominated convergence under the whole finite μ⊗μ yields
    lim_{ε↓0} ∥A_ε(it)∥²_L²(dt)/ε = 4π log 2 Σ_γ μ{γ}².
The product mass of the diagonal is exactly the sum of squared atomic masses by Tonelli. The proof uses the Fourier transform of K at individual nonzero differences, so it does not require pointwise decay of μ̂ or any bound on near-diagonal concentration. In particular the same argument is valid for a singular continuous measure.

I checked Schulte's actual arXiv:2005.05212v1 PDF §3, Definition 3.1 and Theorem 3.9(1),(4), pp. 6–7. Normalizing K(v)dv and pushing it onto frequencies v/ε gives an ergodic probability-measure sequence along every sequence ε↓0, by Riemann–Lebesgue. Thus the linear diagonal identity falls under the stated Wiener result. It also follows directly by the argument above. No priority beyond this linear step is inferred. [Schulte PDF](../../sources/witness62_herglotz/2005.05212.pdf)

## Exact one-atom profile

For an atom αδ_γ and v=(t−γ)/ε, the boundary H_ε equals
    h_α(iv)=exp(α[Log(iv)−Log(1+iv)]).
Both logarithms are continuations of the right-half-plane branches real on the positive axis. The expression tends to zero at v=0, so this point can be filled in continuously. Additivity of the resolvent integral shows that no identity involving ambiguous real powers of a complex product is needed. This is valid for every real α>0. In the half-plane, h_α(w)=exp(α[Log w−Log(1+w)]) has modulus at most one since |w|≤|1+w|.

Let U(w)=Re(1−h_α(w))≥0. Its half-plane Poisson representation applies because U is bounded harmonic. In particular πR U(R) is the integral of U(iv) against R²/(R²+v²). By monotone convergence as R→∞ and the real-axis expansion, ∫U(iv)dv=πα. Moreover
    ∫_R (1−|h_α(iv)|²)dv
        =4α ∫_0^∞ v^(2α)/(1+v²)^(α+1) dv
        =2α B(α+1/2,1/2).
The first equality integrates by parts using |h_α(iv)|²=(v²/(1+v²))^α. Its boundary terms vanish because v is small at zero and the modulus loss is O(v^(−2)) at infinity. For the second equality set v=tan θ and use the sine-power beta integral. Thus I_α=∫|1−h_α(iv)|²dv is
    I_α=2π α [1−Γ(α+1/2)/(√π Γ(α+1))].
The identity uses |1−h|²=2Re(1−h)−(1−|h|²). The integral is positive for α>0 and finite. The exponential contraction bound gives the useful estimate I_α≤4π log 2 α² from the linear one-atom identity.

## Finite localization and arbitrary atom tails

For a finite list of distinct atoms, take disjoint bounded intervals centered at each atom and separated from the others. On each interval the sum of all other increments is uniformly O(ε). Both increments have nonnegative real part, so the Lipschitz inequality |e^(−A)−e^(−B)|≤|A−B| follows by integrating the derivative on the segment between A and B. Thus the total nonlinear defect differs from the defect of the local atom by O(ε) in weighted L² on its interval. On the complement of these intervals the total defect has O(ε) norm. One can check this even in unweighted L². The increment of an atom is bounded there by εα/|t−γ|, whose square is integrable outside its fixed interval. The same comparison works at all heights. Each one-atom defect has norm O(√ε) before squaring. Consequently replacing it by the total defect on its interval changes the squared contribution by O(ε^(3/2))+O(ε²).

Under the rescaling t=γ+εv on its interval, the energy divided by ε tends to P_x(γ) I_α, by bounded convergence of P_x pointwise and domination by the integrable square of the fixed profile. Intervals are disjoint and their squared norms add. For a general finite μ choose ν_N to be its first N atoms, omitting the nonatomic part. Reverse triangle inequality, exponential contraction and the linear identity give
    limsup_{ε↓0} ε^(−1/2) |∥1−H_ε^μ∥_x−∥1−H_ε^ν_N∥_x|
    ≤ [4π log 2 ∥P_x∥∞ Σ_{atoms omitted} α²]^(1/2).
The nonatomic part does not appear on the right. This upper bound tends to zero by finiteness of μ. The finite energy coefficients also converge by the bound on I_α and boundedness of P_x. Taking N→∞ after the limsup for fixed N establishes the limit and permits accumulating or densely located atoms. For an entirely nonatomic measure take ν_N=0, so the slope is zero.

Finally P_x(γ)I_α has coefficient 2xα/(x²+γ²) times the gamma bracket, as stated. Both the Poisson weighting and the Fourier normalization have been retained.

## Measure-level consequence of the same argument

The estimates also give convergence against any fixed bounded continuous function W on the boundary, including W=1. For a finite atomic measure, the preceding unweighted O(ε) bound controls the complement of its finite intervals and boundedness and continuity of W suffice within each rescaling. For general μ, the total variation norm of the difference between its scaled energy measure and that of ν_N is bounded by
    ε^(−1) (∥1−H_ε^μ∥_2+∥1−H_ε^ν_N∥_2)∥H_ε^μ−H_ε^ν_N∥_2.
Contractivity of the exponential, the uniform linear O(√ε) bound from Fourier Plancherel, and the linear limit for μ−ν_N make its limsup O_μ((Σ_{atoms omitted} α²)^(1/2)). Therefore ε^(−1)|1−H_ε^μ(it)|² dt converges against bounded continuous tests to Σ I_α δ_γ. This consequence requires only the finite-measure hypotheses above.
