# Director reconstruction of the adaptive Nyman–Beurling main theorem

Source: bramble_trace, *Adaptive zero clusters and optimal Nyman–Beurling approximation rates*, rStation paper48, v2, posted2026-10-24 15:17:54UTC. V1 was posted11:26:11UTC the same day. Primary v2 Markdown SHA256: `57a65d19bc9914db42dfc2869850cc02e959b87699099abeb40525085600681b`. [Exact source](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2). The director read §§1–10 and references and independently reconstructed the main RH-conditional theorem through equation78. The prefix lower-bound theorem and finite-off-line-zero extension have separate unverified dependencies and are outside this adjudication. Platform Accept is not journal refereeing.

## Disposition and exact scope

The main theorem's upper construction is supported by a complete scoped reconstruction, with a fixed-Laurent-term qualification filling the compressed localization step in §7.2. The lower bound is the published Burnol theorem in exactly the required norm and cutoff. The conclusion is conditional on RH and classical RH consequences stated below. It neither proves RH nor supplies a rate for a prescribed coefficient array. This is the source author's theorem; the Observatory contributes independent reconstruction, the explicit local qualification and reusable interfaces. Publication novelty and independent external expert validation remain open.

Write s=1/2+it, L=log N and

    ||f||_*² = (2π)^(-1) ∫_R |f(1/2+it)|²/(1/4+t²) dt.
    Δ_N² = inf_{A(s)=Σ_{n≤N}a_n n^(-s)} ||1−ζA||_*².

Allow arbitrary complex coefficients and multiplicities mρ. Assuming RH,

    lim_N (log N)Δ_N² = lim_N (log N)d_N²
      = Σ_{distinct nontrivial ρ} mρ²/|ρ|²,

where d_N restricts the polynomial multiplying ζ to value0 at s=1, equivalently the source's floor-difference space. Both ordinate signs are included. The constant converges since Σ_{j<|γ|≤j+1}mγ²=O(log²(2+j)). If all zeros are simple it equals 2+γ_E−log(4π).

## 1. Classical inputs and good contours

RH supplies ζ(σ+it)≪ε (2+|t|)^(max(1/2−σ,0)+ε) on fixed bounded strips away from the low pole; for fixed η>0, 1/ζ(σ+it)≪η,ε (2+|t|)^ε on σ≥1/2+η. The latter follows from an analytic logζ, Borel–Carathéodory anchored to the right and the former subpower bound. The functional equation controls the corresponding fixed line on the left. RH also supplies S(T)=O(log T/loglog T), hence for every fixed h>0,

    N(t+h)−N(t−h) ≤ (h/π)log t + O_h(log t/loglog t).

The inspected source for this exact fixed-h use is Balazard–de Roton Proposition8. No h=h(T) assertion is used.

For a fixed interval J of length ℓ, average Kη(t)=Σγ log(1+η²/(t−γ)²). Its nonnegative kernel has integral2πη. Unit-window counting gives average O((η/ℓ+η²)log T). Choose fixed η sufficiently small *after* fixing ℓ and the requested exponent ε. At some t_J the kernel is sufficiently small. Integrating the real Hadamard logarithmic derivative horizontally gives source(12); its gamma contribution has the favorable negative sign for log|1/ζ| as one approaches the line. This bounds the reciprocal uniformly over a fixed horizontal strip at t_J. Functional equation and absolute convergence finish the horizontal bound. Constants may be very large but are independent of the growing cluster cardinality.

Choose D=e=10^(-4), δ=10^(-6), where e is an exponent. Good heights in [jD+D/3,jD+2D/3] have consecutive spacings in [2D/3,4D/3]. Rectangles have vertical sides1/2±δ. Their representatives τ_C have fixed separation; root counts satisfy k_C≤D log T_C eventually, T_C=2+|τ_C|. Finite exceptions enter one fixed prefactor. The contour perimeter is<4D, every contour-to-root distance is<2D and sup_Γ|1/ζ|≤C_F T_C^e. Retain empty cells: they are needed for high-strip cancellation.

## 2. Collision bounds without inverse derivatives

For the principal part R_C of F=1/ζ, finite backward Newton expansion gives

    R_C(s)=Σ_{j=0}^{k−1} d_j / Π_{i=j+1}^k(s−ρ_i),
    d_j=(2πi)^(-1)∮_Γ F(z)Π_{i=j+2}^k(z−ρ_i) dz.

The final interpolation remainder integrates to zero because F(z)Π_i(z−ρ_i) is holomorphic inside the contour. Repeated nodes cause no change. If m=k−j, |d_j|≤C T_C^e(2D)^m. In particular the contour prefactor C_F is not raised to k.

On |t−τ_C|≤5D, ζ(s)/Π_i(s−ρ_i) is the k-th divided difference of ζ at the repeated zero nodes and s. Cauchy's estimate on radius-D disks gives k!D^(-k) times the strip supremum; the Hermite–Genocchi simplex has mass1/k!, canceling the factorial. Therefore the quotient is ≤C D^(-k)T_C^(D+e). Removing k−m factors costs≤(6D)^(k−m). Combining with d_j leaves≤C6^k T_C^(D+2e), rather than a power of a reciprocal derivative or minimum gap.

For source taper w_k (equations22–23), k≥2, use beta-polynomial coefficients to get exponential bounds in k. It agrees with1−u for u≤1/4, is C^(k−1) and vanishes to order k at1. For P(z)=Π_{i=1}^m(z−iθ_i), m≤k, the causal inverse transform h is the convolution of the exponential kernels. Applying P(D_x) to w_k(x/L)h(x) gives one δ0 and subset terms

    L^(-1) B_j(x/L) E exp(ixΘ_j),
    B_j(u)=u^(j−1)w_k^(j)(u)/(j−1)!.

There are no other deltas: matching jets at the interior knot and the zero of order k at1 suffice. Exponential coefficient and variation bounds give

    ||1−P(it)T_{L,w_k}(1/P)(it)||²_{L²(dt/2π)} ≤ k²200^(2k)/L,
    |1/P(it)−T_{L,w_k}(1/P)(it)| ≤ 4k²200^k/[L d^(m+1)]

when d is distance to the ordinate hull and d>0. The far estimate is integration by parts for each bounded-variation B_j after averaging its simplex frequency; no derivative of the root locations is taken.

## 3. The summable corrected tail

The near-cluster squared weighted contribution is bounded by

    (C/L) T_C^(-2+2D+5e+2D log1200).

The exponent correction is<0.002119. Near windows have bounded overlap because representatives, rather than individual zeros, are separated. Outside them d>13D/3, so summing (2D/d)^m is geometric. The far term is bounded pointwise by

    C_D |ζ(1/2+it)| T_C^β / [L(1+|t−τ_C|)²],
    β=2e+D log200<0.000730.

Cauchy–Schwarz with this separated lattice kernel and

    ∫(1+|t|)^(-p)(1+|t−τ|)^(-2)dt ≪_p(1+|τ|)^(-p), 1<p<2,

give a far squared bound C L^(-2)Σ T_C^(-2+2β+2e). The convolution inequality follows by splitting near0, nearτ and the remainder. Thus for every finite subset B, and then by norm convergence,

    ||Σ_{C∈B} ζ(R_C−T_{L,w_k}R_C)||_*²
      ≤ (C/L)Σ_{C∈B}T_C^(-2+1/100).                 [source41]

The tail is O(Y^(-99/100)/L). This supplies uniform Hilbert-space tails over arbitrary subsets. It does not assert summability of individual norms. No growing inverse Gram matrix enters.

## 4. Base identity and the entire remainder control

For remote clusters, R_C′(s)=−(2πi)^(-1)∮F(z)/(s−z)² dz=O_K(D T_C^(-2+e)). The twice-subtracted Cauchy kernel at0 and−1 is O_K(T_C^(-3)). Send good horizontal heights to infinity at fixed vertical edges, then the right edge to infinity and the negative odd left edge to minus infinity. The latter is justified by the functional equation and integer gamma product, giving source(19), with factorial decay in the edge location. This proves the regularized expansion17 including the trivial poles and interpolant10s−2. It is important not to infer the expansion merely from the poles: an entire term would otherwise be possible.

The differences R_C(0)−R_C(−1) are absolutely summable by integrating the remote derivative bound on[-1,0]. After differentiating, any remaining constant is zero by F′(x)→0 and Σ|R_C′(x)|≪x^(-1+e) as real x→∞. Trivial derivatives also tend to zero. Hence source(21) follows with no entire derivative remainder.

Perron's formula at fixed N shifted across complete contours gives LV=LF+F′+Σ B_C+Σ B_n^tr for V=Σ_{n≤N}μ(n)n^(-s)(1−log n/L). The endpoint weight is zero. The elementary rational identity T_{w1}R=R+(R′+B)/L then gives source(45). The complete contour expression for each first-order error is

    1_{s insideΓ} − ζ(s)/(2πiL) ∮_Γ F(z)[exp(L(z−s))−1]/(z−s)² dz.

The indicator and integral move together. Empty cells have zero combined expression. Their insertion allows exact cancellation of shared edges *before* estimation. Alternatively the retained-left-edge identity94–97 with W=1 gives the same main theorem and an O(1/L) remainder without a far-left expansion; this is a useful independent sign and remainder check.

## 5. Uncorrected high strip

At a shared cutoff h=H+O(D), telescope the exterior rectangles. At fixed N the outer boundary tends to infinity. Squared norms of the omitted outer vertical and horizontal terms are O(N^(2δ)L^(-2)H′^(-1+4e)) and O(N^(2δ)H′^(-2+4e)); the omitted indicator is O(1/H′). Thus the passage to the infinite strip is in the full weighted norm, not just pointwise.

The remaining vertical sides use kδ(v)=(δ²+v²)^(-1). Cauchy–Schwarz against kδ and Tonelli reduce their squared norm to C N^(2δ)L^(-2)∫_{|y|>h}(2+|y|)^(-2+4e)dy. On the cutoff horizontal sides retain exp(Lw)−1=w∫_0^Lexp(uw)du. The resulting real integral is Aδ(v)=2asinh(δ/|v|), whose square has only an integrable logarithmic singularity and a v^(-2) tail. The same convolution split applies. Therefore

    ||high first-order tail||_*²
      ≪ H^(-1)+N^(2δ)L^(-2)H^(-1+4e)+N^(2δ)H^(-2+4e).

Trivial-pole errors have norm O(1/L) from the factorial decay of 1/ζ′(−2n). All bounds preserve the actual indicator and both horizontal connectors.

## 6. Actual integer coefficients and finite fixed repairs

Set b=1/4,H=N^(1/20),K=N^(3/20). For low clusters write h_C(x)=(2πi)^(-1)∮F(z)e^(zx)dz and ψ_C=w_k−(1−u). Its support starts at b and it vanishes at1. The correction is the actual polynomial

    D_N(s)=Σ_{n≤N}n^(-s−1)Σ_{|τ_C|≤H}h_C(log n)ψ_C(log n/L).

Its continuous integral replaces exactly the low first-order errors by delayed-profile errors. The contour majorant gives collective sums |h_C|≪H^(1+e)y^(1/2+δ), |h_C′|≪H^(2+e)y^(1/2+δ). Profile differentiation costs less than the latter power. The resulting quadrature integrand has derivative ≤C H^(2+e)(1+|t|)y^(-2+δ), and is continuous by zero extension at both endpoints. Integrating its derivative gives sum-minus-integral ≤C H^(2+e)(1+|t|)N^(-b(1−δ)), including noninteger N^b. Low/high t estimates give squared exponents

    (4+2e)/20−2b(1−δ)+(3/20)(1+2e) = −0.1499595,
    (2+2e)/20+2δ+(3/20)(−1+2e) = −0.049958.

The slowest high-strip exponent is−0.049978. The growing anchor exponent is(1+e)/20−b(1/2−δ)=−0.07499475. Thus all these errors are negligible at norm scale L^(-1/2). The correction never uses n>N.

For a fixed finite zero set the separate fixed-profile quadrature lemma uses a continuous piecewise polynomial q with q(0)=q(1)=0. On its first piece the power coefficients of x^(m−1)q(x/L)/(m−1)! cost O(1/L). On later pieces the regular-zeta terms cancel between cutoffs. The exact noninteger Euler identity is

    Σ_{n≤X}n^(-1−z)−∫_1^Xy^(-1−z)dy
      = [ζ(1+z)−1/z]−{X}X^(-1−z)+(1+z)∫_X^∞{y}y^(-2−z)dy.

Differentiated remainder integrals converge on Re z=0. Taking X comparable to |z| also proves the needed O(log^(h+1)(2+|z|)) bound on derivatives of the regular term. The first positive fixed knot gives a negative power of N in the remainder; splitting at T=N^(α1/2) controls the whole boundary norm. This proves an O_F(1/L) norm and anchor cost, not a uniform bound for growing F.

## 7. Explicit local qualification and the optimal constant

In §7.2 the sentence applying(26) outside fixed zero neighborhoods is incomplete if read for the full cluster hull: a gap between zeros is still inside that hull. Repair it for the fixed finite collection only. Expand R_C into its individual Laurent terms a_{ρ,j}/(s−ρ)^j. Linearity of T_{L,w} and the repeated-singleton version of(26) give

    |ζ(s)[a_{ρ,j}/(s−ρ)^j−T_{L,w}(a_{ρ,j}/(s−ρ)^j)]|
      ≤ C_F |ζ(s)|/[L |t−γ|^(j+1)]

on |t−γ|≥r for any fixed r>0. This includes gaps inside the original hull. Its square times the Cauchy weight is integrable, uniformly in L after multiplying by L²: at infinity it is O((1+|t|)^(2e−2j−4)). Constants may depend on the fixed zero set. The optimal replacement taper(1−u)^m has the same bounded-variation product-rule estimate. This repairs the localization without adding a growing separation hypothesis.

On a small neighborhood of a fixed zero of order m the top Laurent term becomes (Gρ(s)/Gρ(ρ))e_{m,w}(L(t−γ)), ζ(s)=(s−ρ)^mGρ(s). Plancherel identifies its local leading constant with

    c_m(w)=∫_0^1 |(d/du)^m[u^(m−1)w(u)/(m−1)!]|² du.

Lower Laurent orders have an extra positive power of s−ρ, giving O(L^(-2)) squared local errors. The singleton far bound gives O_F(L^(-1)) norm elsewhere. Thus cross terms from distinct fixed neighborhoods vanish after scaling squared norms by L. For the first m shifted Legendre polynomials, integrating by parts m times gives inner products(−1)^(j+1). Their squared projection norm is Σ_{j<m}(2j+1)=m². The taper(1−u)^m attains it because its derivative above has degree m−1. All terms in the local constant have the exact Cauchy weight1/|ρ|².

## 8. Limit order, anchoring and published lower bound

Fix F comprising finitely many complete clusters; use the fixed-profile corrections to replace their top Laurent tapers by(1−u)^m. For any fixed Y beyond F, retain clusters up to Y, take N→∞, and then Y→∞. Source(41) bounds the omitted scaled norm by C Y^(-99/200) uniformly in N. The high-strip and quadrature errors vanish. This proves equation75 with F held fixed. Its excess constants are summable by(41) and the finite local limits. Since each fixed F gives actual admissible polynomials for all sufficiently large N, taking limsup first and then exhausting F proves the optimized upper bound. No F(N), growing fixed-profile constant or uniform inverse Gram estimate is assumed.

RH and Abel summation give V_{N,1}(1)=1/L+Oε(N^(-1/2+ε)); it uses F(1)=0,F′(1)=1. Together with the growing and fixed anchor bounds, A(1)=O_F(1/L). Subtracting this constant changes the residual norm by at most |A(1)| ||ζ||_*=O_F(1/L), since convexity gives ||ζ||_*<∞. Anchoring is therefore negligible at the established leading scale.

I checked the original Burnol math/0103058v2 definition and Theorem1.3 on printed pp3–4. B_λ is the unrestricted complex span of fractional parts {θ/u}, λ≤θ≤1, in L²(0,∞). Mellin–Plancherel sends the residual χ(u)+Σ_{n≤N}a_n{1/(nu)} to(1−ζA)/s, with precisely dt/(2π). The sign is absorbed in the unrestricted complex span of scalesθ=1/n. Therefore D(1/N)≤Δ_N≤d_N. Squaring Burnol's nonnegative lower bound gives the exact liminf constantΣmρ²/|ρ|². The inverse Hilbert block's(0,0) entry is m² by the same shifted-Legendre evaluation kernel. No unverified rStation projection theorem enters this main lower bound.

## Independent challenges and remaining work

Advocate: rstation48_adaptive_upper_rt62_rstation48.md and rstation48_quadrature_norm_rt62_rstation48.md. Skeptic: threshold62_rstation48_main_theorem_skeptic.md and threshold62_rstation48_lower_and_tail_supplement.md. Further independent reconstruction: latest62_rst048_independent.md. Provenance/version audit: ratio62_rstation48_provenance.md. These are separate reconstructions with explicit evidence, not votes. The director independently checked the Newton expansion, cancellation of the factorial, subset product rule, convolution exponents, noninteger Euler sign, local repair, integer support and ordered limits.

Next precise tasks: obtain effective constants and certified finite-Y errors under explicit reciprocal bounds; audit the separate prefix arithmetic lower bound from its actual compact-jet source; audit the discrete synthesis used by the finite-off-line extension; test the transfer to explicitly specified other L-functions with their pole, gamma and coefficient structures retained. A bounded provenance search found no independent journal/arXiv manifestation of this source claim; source credit and review scope must remain visible.
