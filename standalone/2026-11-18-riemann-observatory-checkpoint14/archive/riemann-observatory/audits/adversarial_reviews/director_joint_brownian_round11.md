# Joint and functional prime-phase limits: director adjudication

18 November 2026. The director read both proposed proofs and the independent reconstruction, and independently checked the Fourier majorants, the exact reciprocal clock and the all-time interpolation argument. The results below follow under RH from the adjudicated effective restricted HLZ prefix estimate. They are conditional deductions from existing inputs; publication novelty is not established. Numerical onset constants have not been allocated.

## Fixed-dimensional arrays

Draw a signed ordinate with |gamma|>Y with probability proportional to |zeta'(1/2+i gamma)|^2/(1/4+gamma^2). Set U_p=exp(-i gamma log p). Fix d,D and deterministic real columns a_p,b_p in R^d supported on p<=(log Y)^D. Let

```text
X_Y = sum_p [ a_p(Re U_p−p^(-1/2)) + b_p Im U_p ],
Sigma_Y = sum_p ((1−1/p)/2) (a_p a_p^T+b_p b_p^T).
```

Assume Sigma_Y tends to a finite matrix Sigma. Then X_Y tends to N_d(0,Sigma) if and only if max_p(||a_p||+||b_p||) tends to zero. The necessity uses the unrestricted qualitative character theorem and the bounded-covariance array class. The sufficient direction is effective in bounded-Lipschitz distance when the fixed parameters, a covariance bound and convergence moduli are computable. Orthant convergence is effective if every limiting marginal variance is positive; no orthant continuity is asserted at a zero marginal atom.

For a bounded projection u, the absolute Laurent coefficients are majorized by positive cosine coefficients with weights d_p=sqrt((u^T a_p)^2+(u^T b_p)^2). The covariance bound gives sum d_p^2=O(1). The model-weighted coefficient mass is O_k((1+sqrt(H_P))^k), where H_P=sum1/p; the unrestricted mass is O_k(P^(k/2)). These pair with the relative and absolute character errors separately. A fixed moment degree fits a fixed larger logarithmic character range. Signed sine observables require the symmetric two-sign law; the imaginary one-sided character is not assumed controlled. Delete a possible exceptional prime, bound retained even moments, restore the full statistic at each prefix, and only then integrate to the strict tail.

The comparison model has independent bounded coordinates, exact covariance Sigma_Y, and higher cumulant sums tending to zero under the maximum-column hypothesis. Conversely, a nonvanishing column pair has a subsequential bounded nondegenerate summand. The remaining sum is tight by its bounded variance, and independence survives a subsequence. Cramér's Gaussian decomposition theorem excludes a Gaussian limit. This is a necessity theorem for this specified array class, not a universal criterion for arbitrary test functions.

For fixed 0<a<b, the unnormalized centered band sum on (log Y)^a<p<=(log Y)^b tends to a Gaussian of variance (1/2)log(b/a). Disjoint such bands give independent limits. Its variance does not diverge: smallness comes from all the contributing primes tending to infinity. By contrast separately standardized cumulative cutoffs (log Y)^D_i have limiting correlation one. Distinct cutoffs alone do not produce Brownian covariance.

## A functional Brownian limit

Put L=log Y, b=log L and H=log b. For fixed 0<=u0<1 define the right-continuous process on [u0,1]

```text
P_Y(u)=exp(b^u),
X_Y(u)=sqrt(2/H) sum_(p<=P_Y(u)) [cos(gamma log p)/sqrt p−1/p].
```

Then X_Y converges to standard Brownian motion restricted to [u0,1], in the Skorokhod J1 topology. In particular its limiting value at u0 has variance u0. There is an effective conditional bounded-Lipschitz onset for fixed computable u0 and tolerance, with no numerical threshold supplied.

The essential new check beyond finite-dimensional convergence is a bound for EVERY subset I of the primes p<=log Y, however small: E_Y |sum_I(cos(gamma log p)/sqrt p−1/p)|^4 <= C (sum_I 1/p)^2, uniformly at sufficiently large Y. In the model, Hoeffding's variance-under-tilting argument gives centered moments C_j h^(j/2) for h=sum_I1/p, including h<1. The raw positive Fourier expansion and binomial centering bound the relative error by O((log L/log T)(h^2+h^4)). The unrestricted Fourier mass is at most16 L^2 h^2, absorbed by any fixed log saving of degree B>2. There is no interval-independent error. Restoring a deleted prime costs at most a constant times h^2 in fourth power, even for a singleton subset. Positivity permits the negative strict-tail boundary to be discarded in this upper bound, after restoring the full fixed subset.

Interpolate in the exact deterministic clock v_j=H^(-1)sum_(i<=j)1/p_i. Grid increments have fourth moment C(v_j-v_i)^2. A fractional cell scales by the fourth power of its fraction; an arbitrary increment decomposes into at most three pieces. Minkowski gives the same bound for all real interpolation times. A dyadic union bound and chaining provide an effective modulus. The effective elementary Mertens estimate yields sum_(p<=exp(b^u))1/p divided by H = u+O(1/H), uniformly even at u=0. Thus the original step process is uniformly close in probability to the continuous interpolation evaluated at ordinary time. Its largest jump is deterministically O(H^(-1/2)). Joint comparison identifies covariance min(u,v). This proves tightness and the process law, rather than inferring it from finite-dimensional limits.

For effectivity, choose a finite mesh from the modulus bound before choosing the moment order needed for its finite-dimensional comparison. Polygonal interpolation is Lipschitz from the mesh sup norm to the uniform path norm; J1 distance is bounded by uniform distance. Brownian fourth moments give the matching modulus bound. This also works with the degenerate initial component at zero.

## Primary antecedents and limits

The source comparison identifies Vassaux arXiv:2505.07352v2, Theorem1.1 and sections2.2–3, as a genuine functional Brownian antecedent with a related fourth-moment strategy. Its observable is an analytic horizontal log zeta, sampled at continuous uniform height, and its theorem does not assume RH. Fazzari's continuous |zeta|^2 prime moments already have the exact1/p centering. The derivative-squared continuous results, Bui–Gonek–Milinovich's exact discrete prefix twist, ordinary-counted zero results and mesoscopic linear statistics have different measures or ranges. The proof methods are standard once the uniform arithmetic and local-mass bounds are established. A bounded search finding no identical statement does not establish novelty.

These results supply no unweighted zero law, spacing statistic, total-variation convergence or numerical onset. Larger prime cutoffs are under a separate campaign. The two-sign sampling is essential for the stated general sine array; the cosine process itself is unchanged by restricting to positive ordinates.

[Joint proof](uniform65_joint_exceptional_prime_clt.md) · [Process proof](uniform67_brownian_prime_phase_process.md) · [Independent reconstruction](analytic67_joint_process_skeptic.md) · [Primary priority comparison](uniform68_priority_prime_phase_process.md)
