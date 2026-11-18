# Independent trace-buffer reconstruction

Reviewer: analytic_frontier; 17 November 2026. Scope: AF Proposition4.2 only. This is an independent hand reconstruction after reading the original passage and Arias de Reyna's alternative exposition. It does not audit the Hilbert–Schmidt asymptotic, headline density theorem, or all formal dependencies.

Sources: Alpöge–Furman, arXiv2608.13637v2, §§2.2–2.3, Lemma2.1 and Proposition4.2 pp4–6; Arias de Reyna, arXiv2610.24612v1, Proposition16 and footnote1 pp15–16, Proposition18 p17 and Proposition32 pp27–28. The latter's Proposition16 supplies the crude bound O(U sqrt(T) logT) and therefore chooses U=T^theta with 0<theta<1/2. Its footnote correctly says that this particular bound is insufficient when U=sqrt(T). That does not establish that a sharper estimate fails.

## Precise statement recovered

Let L=log(T/(2pi)), X=exp(L), h=2pi/L, d=floor(T/h), alpha_k=T+kh. Let phi be the real even compactly supported AF window, support[-L/2,L/2], a=||phi||_2^2/L bounded below by a positive constant. Assume the uniform decay estimate(2.8), and the standard multiplicity-counting bound O(logT) zeros per unit ordinate interval at heights in[T/2,3T]. Put I=[T,2T), I'=[T-U,2T+U), 0<=U<=T/2. For rho a nontrivial zero put z_rho=-i(rho-1/2), r=Re z_rho and y=Im z_rho; |y|<1/2. Define

G=(aL^2)^(-1) sum_{r in I'} m_rho v_rho v_rho^T,

v_rho=(hat(phi)(z_rho-alpha_k))_{0<=k<d}.

Then, uniformly in such U,

tr G = N(I) + O(sqrt(X)),

and consequently

tr G = N(I') + O(sqrt(X)+(U+1)L).

At U=sqrt(T), this gives O(sqrt(T)L), stronger than AF's stated O(sqrt(T)L^2). Constants depend on the fixed window/profile and the standard local zero-count bound. This is a repair of one estimate, not a new proportion theorem or a claimed literature novelty.

## Two identities and the near-boundary bound

Set F(z)=integral phi(u) exp(izu)du and A=aL^2. Fourier-series Parseval on[-L/2,L/2], applied to phi(u)exp(i(r-T)u-yu), gives

sum_{k in Z}|F(r+iy-alpha_k)|^2
 = L integral phi(u)^2 exp(-2yu)du <= A exp(L|y|) <= A sqrt(X).

The bilinear Fourier-series identity, using phi even, also gives sum_k F(z-alpha_k)^2=A. All sums converge absolutely by the preceding identity and Cauchy–Schwarz; no positivity of complex squares is assumed. This also independently justifies the complex specialization of AF Lemma2.1. Only real ordinates are formalized in the inspected Poisson.lean theorem types, so this hand argument must not be described as locally Lean verified.

A sharper bound uses the uniformly bounded window, |phi|<=C_phi. Since |y|<=1/2,

integral_{-L/2}^{L/2} exp(-2yu)du
 =2 integral_0^{L/2} cosh(2yu)du
 <=2 integral_0^{L/2} cosh(u)du
 =2sinh(L/2)<=sqrt(X).

Thus the normalized full absolute sum is at most C_phi^2 sqrt(X)/(aL). For any zero with distance from either endpoint T,2T less than1, its finite diagonal contribution has that bound; if it lies in I its deviation from1 is at most that bound plus1. There are O(L) such zeros counted with multiplicity. Their total cost is O(sqrt(X)+L)=O(sqrt(X)). The initial reconstruction used the looser mass bound sqrt(X) and obtained O(sqrt(X)L); the independent skeptic supplied this improvement, checked here by the displayed cosh argument.

## Interior zeros away from endpoints

For r in I and D=min(r-T,2T-r)>=1, subtract the missing infinite-grid tail from the bilinear identity. The floor in d matters: alpha_d is in(2T-h,2T], and can itself be inside I. Thus the right missing tail starts at distance at least D-h, rather than D. For h<=1/2, D-h>=D/2. The left missing tail starts at distance at least D+h. Integral comparison gives

sum_{k<0 or k>=d}|r-alpha_k|^(-4) <= C h^(-1)D^(-3).

Equation(2.8), |Im z|<1/2 and division by A give error at most C sqrt(X)/(L D^3) for this zero. Multiplicity-weighted summation over distance shells j<=D<j+1 gives sum D^(-3)=O(L), hence O(sqrt(X)) total.

## Exterior buffer zeros away from endpoints

For r in I' outside I and D=dist(r,I)>=1, estimate the FINITE inside grid directly. Since alpha_0,...,alpha_{d-1} are inside I,

sum_{0<=k<d}|r-alpha_k|^(-4) <= C h^(-1)D^(-3).

The same normalization and shell count give O(sqrt(X)) total, independently of the buffer width U. In this case there is no main term1 to assign to this zero. Replacing its finite diagonal sum by1 and attempting to estimate the missing outside grid would throw away the localization that is needed here.

Combining the near, interior and exterior cases proves the first estimate. The usual local zero count gives N(I')-N(I)=O((U+1)L), proving the second. Endpoint conventions only change O(L) zero multiplicity and are absorbed.

## What the printed argument does and does not justify

AF p6 claims for every k outside[0,d) that alpha_k is outside[T,2T) and |r-alpha_k|>=dist(r,{T,2T}). The former ignores alpha_d's floor discrepancy; the latter is not valid for r in the exterior buffer. A geometric witness is r=alpha_{-1}=T-h, which lies in I' if U>=h and gives zero distance to a missing grid point but distance h to the boundary. This witness is about the asserted geometric implication; it does not assert a zeta zero at that prescribed ordinate. More generally any actual exterior zero with D>=1 has a nearby exterior grid point at distance<=h/2<D, so the problematic step cannot hold uniformly there.

The estimate is nevertheless valid through the inside/outside split above. Arias's O(U sqrt(T)logT) comes from applying the full absolute-frame bound to every exterior buffer zero. Direct exterior-tail localization removes the factor U from the sqrt(T) contribution. Neither the prose defect nor that coarse alternative bound establishes failure of the AF main theorem.

## Separate formal route

At commit3635e74826a4c1fcece7d1cd2b6fa75e43a00510, Zeta23/PrimeSideA.lean:58–64 proves prop_trace_mu for the prime-side matrix, and :300–305 proves prop_trace:

|trGtA-a L N| <= C L sqrt(X),

under GammaFacts, ChebyshevMertens, fixed0<lambda<=1, taper LocalHyps, and the Riemann–von Mangoldt estimate on the abstract N. PrimeSideB/Traces.lean:145–156 instantiates N with the actual zero count. The proof uses the smooth density integral and prime-side estimates, rather than literally compiling the problematic zero-side Proposition4.2 paragraph. This is static source inspection; the full formal theorem cone has not been built locally in this checkpoint.

The independent search_skeptic was commissioned from the source without receiving this reconstruction or the director's derivation. It independently recovered the split and supplied the sharper near-boundary Parseval estimate. The director separately recovered the same repair. Compare the separate skeptic note before director adjudication. The stronger trG-N(I)=O(sqrt(X)) estimate is a scoped reconstructed bound; no literature novelty is asserted.
