# Selected sextic source norm: recent methods and remaining mismatch

This is a targeted literature check, not a new zero-free region. The target is the selected-row Gram bound in [the fourth-cycle note](2026-10-29-complete-source-four-cycle/README.md), for complete or smoothly majorized source norm L≥Y and the actual fixed smooth prime-slot selector. At the difficult parameter the selected row count is conditionally M≪Y^{0.60938}; a bound Tr(E⁴)≪L^{4+ε}+L^{2+ε}M³ would suffice for the desired L^{1+ε} operator bound, but it is not currently proved.

## Fixed-form metaplectic large sieve

Dunn, [*Metaplectic cusp forms and the large sieve*](https://arxiv.org/abs/2403.13151), published in *Algebra & Number Theory* 19 (2025), Theorem 1.5, proves a Type-II bound for the kernel ρ_f(ab), where f is one fixed cubic metaplectic **cusp form** on the Eisenstein field. With squarefree a in a norm dyad A, b in a dyad B, AB≈X, a fixed ray congruence ab≡u mod v, and the source's smooth profile W_K, it is

    B_f(α,β) ≪_{ε,f} (XK Nv)^ε K^8 (Nv)^4
                  · ((AB)^{1/2}+A^{3/2}B^{1/4}) ||μ²α||_∞ ||β||₂.

Theorem 1.2 uses this and a separate Type-I estimate for a fixed form to bound a prime sum by X^{1−1/34+ε}, with explicit polynomial smoothness and ray-modulus factors. The proof uses a number-field circle method and two Voronoi transforms, then averages the resulting homogeneous correlations. This is a plausible *methodological* template for retaining cancellation in a signed row cycle, but it is not the desired estimate: the selected kernel is a sextic residue-character matrix with variable pair conductor, not the coefficient sequence of one fixed cusp form; the relevant metaplectic contribution may include residual theta spectrum; and the factor (Nv)^4 cannot be ignored when a putative v grows as a positive power of Y. No matching transform, growing-conductor uniformity, or treatment of the prime selector is supplied by the theorem.

## Explicit obstructions from metaplectic theta spectrum

De Faveri, Dunn and Hoffstein, [*Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*](https://arxiv.org/abs/2607.07911), Theorem 1.1, prove unconditionally, with both arguments primary squarefree and A,B≥1,

    Ξ₃(A,B) ≫_ε (AB)^(−ε) [A+B+(AB)^(2/3)].

Thus an unrestricted cubic perfectly orthogonal bound fails even at squarefree indices. Their proof uses mean-square control of Kubota Dirichlet series and metaplectic theta coefficients; Theorem 1.2 gives a separate quartic lower bound. This supports investigating the structured theta/residual spectrum and subtracting or isolating it, but gives no bound on the number or size of residual modes for the selected sextic operator. In particular it does not prove the L⁴ term in the desired fourth-cycle bound. The sextic unrestricted obstruction is established directly in [Xu–Sang](https://arxiv.org/abs/2610.17675), and does not automatically persist under the physical prime-response selection.

## Non-abelian amplification and its boundary

Pascadi, [*Non-abelian amplification and bilinear forms with Kloosterman sums*](https://doi.org/10.1007/s00039-026-00746-0), Theorem 1.2, treats a **single rational modulus** c=dd′e with d′|d and (d,e)=1. For intervals of lengths at most c^{1/2+o(1)}, arbitrary coefficient sequences, and f the largest integer with f²|cd, it bounds the bilinear form with kernel S(am,n;c) by

    ||α||₂ ||β||₂ c^{1+o(1)} ( f/min(c,d²) )^{1/6}.

For a balanced product of two primes the factor is c^(−1/12). The underlying SL₂ non-abelian amplification is a genuine 2026 advance. But the present matrix consists of rank-one sextic Kummer characters on varying ideals, not S(am,n;c) at a common rational modulus. Before this estimate could enter a proof one would have to produce exactly such a Kloosterman bilinear form after reciprocity/Poisson, keep the varying moduli and fixed ray/zero masks, and establish the required interval geometry. No such reduction follows from the theorem. Directly applying its square-root-modulus saving to the Gram entries would be invalid.

## Prime Gauss-sum cancellation

The September 2026 preprint [*An unconditional first moment for cubic Gauss sums*](https://wcook04.github.io/plectis-atlas/papers/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026.html), Theorem 1.1, claims the primary-prime first moment has an explicit nonzero X^{5/6}/log X main term; its Appendix A treats each fixed angular mode. The source uses bilinear dispersion and a metaplectic mean square. This is a claimed preprint result whose dependencies and proof have not been independently checked here. It concerns one cubic Gauss-sum phase and is not uniform in a conductor-varying sextic twist or a row-dependent selector. An untwisted prime first moment therefore does not bound the selected four-row correlation; in particular the nonzero main term warns against discarding theta terms as generic cancellation.

## A concrete next analytic question

Expand a fixed prime-slot selector with a *fixed* integer k:

    1_{|Q(u)|² ≥ P^σ} ≤ P^{−kσ}|Q(u)|^{2k}.

After opening the prime products, a viable route would prove a **signed**, theta-corrected correlation estimate for the resulting finitely many complete-source kernels, uniformly in their changing ideal conductors, the source's ray phases, prime masks and all fixed profile derivatives. The key is an operator or fourth-cycle estimate after combining the prime factors; applying ordinary large sieves separately loses the selector and returns to the unrestricted obstruction. The above papers provide candidate tools for parts of this calculation but do not supply this uniform estimate. The exact required range, dependence on P=Y^w, and the admissible k must be checked against the original detector before such an estimate can imply a fixed-strip improvement.

There is an additional obstacle to the displayed pointwise majorization: if used on the *whole* positive Gram matrix, its diagonal is weighted by P^(−kσ)|Q(u)|^{2k}, which can be as large as P^{k(1−σ)+o(1)}. Thus the desired O(L) diagonal is not preserved. One can instead keep the selected diagonal separately and sandwich the off-diagonal matrix: on selected rows write D_u=P^{kσ/2}|Q(u)|^{−k}≤1, so E_F is a compression of D(P^{−kσ/2}diag(|Q|^k) E diag(|Q|^k)P^{−kσ/2})D. But that replaces the problem by a strong signed weighted off-diagonal estimate, not an automatic consequence of the moment expansion. A clipped bounded weight may be another route, but its approximation and spectral error would also need proof.
