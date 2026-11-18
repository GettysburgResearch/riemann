# Growing logarithmic Riesz order: a conditional approximate-identity proof

Date:2026-11-17. Contributor:equivalences. **Proposed complete argument, independent adversarial review pending.** No novelty or RH proof is claimed. The proposition below assumes RH. It aims to close the explicitly missing weighted estimate in the preceding fixed-order campaign, using already declared classical RH inputs rather than a new zero-spacing or derivative-moment hypothesis.

## Proposed statement and parameter scope

Assume RH. There is a sufficiently large fixed constant c>0 such that, for

L=logN, epsilon_N=c/loglogN, alpha_N=epsilon_N L,

V_N(s)=sum_(n<=N)mu(n)(1-logn/L)^(alpha_N)n^(-s),

one has, for every fixed integer q>=1,

d_q(V_N)^2=(2pi)^(-1)integral_R |1-zeta(1/2+it)V_N(1/2+it)|^2/|1/2+it|^(2q)dt ->0.

Only sufficiently large integers N are involved; then epsilon_N<=1/8 and alpha_N>=4. Endpoint n=N has weight0. Constants can depend on fixedq and the classical RH bounds. No usable numerical c or N_0 is estimated. This is a prescribed array, not an optimized coefficient choice. The proof does not use the fixed-order multiplicity obstruction with a moving alpha.

The stronger target from the preceding campaign follows by the triangle inequality if the separately audited horizontal ratio limit zeta(s)/zeta(s+epsilon_N)->1 in weighted L² is invoked. The argument here proves convergence directly, without relying on that limit.

## Declared RH inputs and inspected source

1. The finite-height inverse bound LemmaF in `audits/baez_uniform_dependency_round2.md`, derived there from PAPER-M001 pp354–355,Eqs14.14.2–5, gives fixed constants A,b>0 such that, uniformly in realu and sufficiently largeN,

   |1/zeta(1/2+epsilon_N+iu)| <= exp(A L/loglogN+b ell(u)),

   ell(u)=log(|u|+3)/loglog(|u|+3),

   provided c>=1. Indeed use V=|u|+N^4+3 in LemmaF and its explicit splitting bound; the earlier proof takes A=8K,b=2K. The same bound holds throughout epsilon_N<=Rew<=1/2+1/L for reciprocal zeta(1/2+it+w), after replacingu by the relevant imaginary part. This is a global-in-height bound, with its N-dependent loss retained explicitly.

2. RH implies |zeta(1/2+it)|<=C_delta(|t|+3)^delta for every fixed delta>0. This is the already declared classical critical-line subpower bound, not a newly audited historical proof.

3. There is an absolute D such that, under RH,

   |zeta'/zeta(1/2+epsilon+iu)| <= D log(|u|+3)/epsilon,

   for0<epsilon<=1/8 and all realu. Actual PAPER-M001 Theorem9.6(A), Eq9.6.1, printedp217 (PDF113), was visually inspected and its displayed proof read: uniformly for−1<=sigma<=2 at large positive height, zeta'/zeta(s)=sum_(|t-gamma|<=1)1/(s-rho)+O(logt). Riemann–von Mangoldt gives O(logt) local zeros counted with multiplicity; RH gives distance>=epsilon. Negative heights follow by conjugation; bounded heights follow from the meromorphic partial fractions on a fixed compact set. The pole at1 is excluded because sigma<=5/8. No bound across that pole is asserted.

4. The completed xi-function is horizontally monotone in modulus under RH: |xi(1/2+it)|<=|xi(1/2+epsilon+it)|. A direct proof is included below, so a new monotonicity theorem is not invoked without justification.

Full ancestry of the classical RH subpower estimates is not re-audited. The assertion remains conditional on these explicitly sourced standard consequences of RH.

## 1. Exact shifted contour and its complex kernel

For alpha>0 the classical first-kind Perron formula (PAPER-M002,Theorem39/Lemma10 p50 and Eq2p51) on an absolutely convergent initial line is

V_N(s)=Gamma(alpha+1)/(2pi i L^alpha) integral_(Rew=1/2+1/L) e^(Lw)/[w^(alpha+1)zeta(s+w)]dw,

when Re(s)=1/2. The principal Logw is holomorphic throughout Rew>0. Under RH shift this line to Rew=epsilon>0. There are no poles of1/zeta inside the strip; its zero at the zeta pole is harmless. For fixedN the uniform inverse bound above is subpower in the imaginary height, whereas the kernel is O(|Imw|^(-alpha-1)). Horizontal integrals tend to0 along rectangles because alpha>0; bounded strip width and the fixedN exponential prefactor cause no difficulty. The new vertical integral is absolutely convergent. No contour crosses Rew=0 or a branch cut.

Set alpha=epsilon L and

K_(alpha,epsilon)(v)=Gamma(alpha+1)e^(alpha+iLv)/[2pi L^alpha(epsilon+iv)^(alpha+1)].

Then exactly

V_N(s)=integral_R K_(alpha,epsilon)(v)/zeta(s+epsilon+iv)dv.       (G1)

The scalar inverse-Laplace formula gives integral_R K(v)dv=1. Writing y=v/epsilon,

|K(v)|dv = B_alpha(1+y²)^(-(alpha+1)/2)dy,

B_alpha=Gamma(alpha+1)e^alpha/(2pi alpha^alpha).

Stirling's upper bound gives B_alpha<=e^(1/24)sqrt(alpha/(2pi)) for alpha>=2. On |y|<=1 use log(1+y²)>=y²/2; on |y|>=1 use (1+y²)^(-(alpha+1)/2)<=|y|^(-alpha-1). These estimates show

integral_R |K(v)|dv<=3, alpha>=2.                             (G2)

For every fixed0<eta<=1 and0<delta<=1/8, the same density gives

integral_(|v|>eta epsilon)|K(v)|(3+|v|)^delta dv
 <=C_delta sqrt(alpha) exp(−kappa_eta alpha),

kappa_eta=log(1+eta²)/4, alpha>=4, epsilon<=1.                 (G3)

Indeed (3+epsilon|y|)^delta<=3^delta 2^(delta/2)(1+y²)^(delta/2). Reserve alpha/4 of the exponent to obtain(1+eta²)^(-alpha/4); the remaining exponent(alpha+2−2delta)/4 is at least1, and its integral is at mostpi. This estimate controls the entire noncompact vertical tail, not only a local Gaussian approximation.

## 2. Horizontal ratio and central height domination

Put w=s−1/2. Under RH the even canonical product is

xi(1/2+w)=xi(1/2) product_(gamma>0)(1+w²/gamma²),

with multiplicities. Its normal convergence follows from sum gamma^(-2)<infinity, itself a consequence of Riemann–von Mangoldt. Evenness and order1 remove any nonconstant exponential factor in this paired product. At w=it and w=epsilon+it each factor satisfies

|gamma²−t²|² <= |gamma²+(epsilon+it)²|²,

because the difference is2epsilon²(gamma²+t²)+epsilon^4. Product comparison yields the claimed xi ratio inequality, including numerator zeros by continuity. The critical value xi(1/2) is nonzero; for example zeta(1/2)<0 follows from the alternating eta-series.

Dividing the completion factors, uniform gamma-ratio Stirling and a compact-height bound give

|zeta(1/2+it)/zeta(1/2+epsilon+it)| <= C(|t|+3)^(epsilon/2),

uniformly for0<epsilon<=1/8. The polynomial s(s−1) completion factors have a bounded ratio on these lines; no pole or gamma pole occurs.

For |v|<=eta epsilon integrate the log-derivative along the vertical segment in Re(s)=1/2+epsilon. The declared bound, with a harmless enlargement D_1 of D to compare nearby heights, gives

|zeta(s)/zeta(s+epsilon+iv)|
 <=C(|t|+3)^(epsilon/2+D_1 eta).                              (G4)

Choose once and for all eta<=min(1,1/(16D_1)). For sufficiently largeN, epsilon<=1/8; hence the exponent in(G4) is at most1/8. This domination is independent ofN. No division by zeta(s) at a critical zero is needed; the displayed ratio is0 there since the shifted denominator is nonzero under RH.

Let

C_N(t)=integral_(|v|<=eta epsilon) K(v) zeta(s)/zeta(s+epsilon+iv)dv.

Equation(G2) and(G4) imply |C_N(t)|<=C(|t|+3)^(1/8). For every t that is not a zero ordinate, zeta(s+epsilon+iv)->zeta(s) uniformly in |v|<=eta epsilon as epsilon->0. Also the central kernel mass tends to1 by(G3) and integralK=1. Therefore C_N(t)->1 for almost everyt. For fixed integerq>=1,

|C_N(t)−1|²/|1/2+it|^(2q)
 <=C[1+(|t|+3)^(1/4)]/|1/2+it|^(2q),

which is integrable. Dominated convergence proves C_N->1 in the required weightedL² norm. This is where the central proof uses almost-everywhere convergence rather than asserting convergence at zero ordinates.

## 3. Full-height tail: paying the moving inverse-zeta loss

Set delta=1/16. The first two declared inputs imply

||zeta(s)/zeta(s+epsilon+iv)||_(L²(dt/(2pi|s|^(2q))))
 <=C_q exp(A L/loglogN)(3+|v|)^delta.                         (G5)

To check the full height integral, absorb exp(b ell(t+v)) into C_delta(|t+v|+3)^delta and use |zeta(s)|<=C_delta(|t|+3)^delta. Since |t+v|+3<=(|t|+3)(|v|+3), the squared integrand is bounded by a constant times(|t|+3)^(4delta)/|s|^(2q), integrable forq>=1. All C_delta are fixed; only exp(A L/loglogN) depends onN.

Minkowski's integral inequality and(G3),(G5) show that the weighted norm of the tail in zeta(s)V_N(s) is at most

C_q sqrt(alpha) exp[(A/c−kappa_eta)alpha].                    (G6)

Choose fixedc>=max(1,2A/kappa_eta). Then this tends to0. This explicit inequality is the parameter condition that a purely local saddle heuristic misses. The Bochner integral is justified by these absolute norm estimates; no conditionally convergent double integral is interchanged.

Combining the central weighted convergence with(G6) proves the proposed RH-conditional d_q(V_N)->0. The same sufficiently largec works for every fixedq>=1; the height integrability is hardest atq1. No uniform estimate asq grows withN is claimed.

## Review targets and limitations

The main points requiring an independent check are: normal paired xi product and uniform completion ratio; the low-height patch for zeta'/zeta; extension of LemmaF to the whole contour strip; exact alpha=epsilon L normalization and kernel mass; preservation of the N-dependent loss through Minkowski; and the strict largec inequality in(G6). No numerical experiment is needed to establish these analytic assertions.

This is a conditional constructive approximation proposition, not a solution of RH. The converse for arbitrary finite arrays comes from the separately established Hardy-space evaluation obstruction; it should be cited separately if the proposition is presented as an equivalent criterion. No historical priority search has established whether this particular moving logarithmic-order array is already in the Riesz summability literature. The earlier campaign's missing-estimate status must remain pending until independent adjudication, even though a complete proof attempt is now recorded here.

## 4. Proposed strengthening: every fixed c>0

Root identified a free auxiliary scale in the tail proof, independently checked by equivalences before this addendum was written. **Independent skeptical review is still pending.** The preceding proof fixed the auxiliary scale at N^4 because it imported that convenient scale from the earlier truncated-Perron estimate. The present contour is infinite and imposes no such truncation, so the auxiliary exponent can instead be any sufficiently small fixed positive number.

For every fixed a>0, the same finite-height argument gives a version of LemmaF:

sup_(|u|<=V,1/2+a/loglogV<=sigma<=2)|1/zeta(sigma+iu)|
 <=exp(K_a logV/loglogV), V>=V_a.                            (G7)

Here K_a,V_a can depend on fixeda. In the high-height split U=exp(sqrt(logV)), a/loglogV>=a/(2loglog|u|); use the actual Titchmarsh source bridge with fixed parametera/2. In the low-height Borel–Carathéodory patch the loss is O((loglogV/a)sqrt(logV))=o(phi(V)); fixeda changes only constants and the starting threshold. The pole-removed logarithm and right-strip bridge are the same as in the audited LemmaF.

Now fix **any** c>0, set a=c/2, and choose a fixed r>0 later. Put V=|t+v|+N^r+3. For sufficiently largeN depending onc,r,

epsilon_N=c/loglogN >= a/loglogV,

because loglogV>=loglog(N^r)=loglogN+logr, whose ratio tologlogN tends to1. More explicitly, for r<1 it suffices that loglogN>=−2logr; for r>=1 the inequality is immediate for largeN.

The same elementary splitting bound gives

phi(V)<=4r logN/loglogN+2ell(t+v),                           (G8)

once loglogN is large compared with|logr|. Thus(G5) is replaced by

||zeta(s)/zeta(s+epsilon_N+iv)||_weighted
 <=C_(q,c,r) exp[(4K_a r/c)alpha_N](3+|v|)^(1/16).

Choose, for example, any fixed0<r<kappa_eta c/(8K_a). The tail bound becomes

C_(q,c,r)sqrt(alpha_N) exp[−(kappa_eta/2)alpha_N] ->0.

All central estimates are unchanged. The contour shift remains inside the fixed strip Rew>=epsilon_N; its horizontal limits need only the subpower-in-height bound for each fixedN, so introducing N^r does not restrict the contour truncation height. This proves the **proposed strengthened statement**: under RH, for each fixedc>0 the prescribed array above converges in every fixed weighted norm d_q,q>=1. Constants and N_0 may deteriorate arbitrarily withc; no conclusion uniform asc↓0 or for c=c_N→0 is asserted.

The corresponding structured THM-E-W312 retains pending-review status. The earlier largec condition is a sufficient condition in the first proof, not a claimed necessary threshold. A review must check(G7),(G8), the free-r quantifiers and the absence of any remaining N^4 truncation dependency before accepting this strengthening.
