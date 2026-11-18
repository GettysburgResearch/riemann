# Fixed-size clusters through every collision stratum

Round2, equivalences agent,2026-11-17. Status: elementary approximation theorem with a self-contained quantitative argument; independent review requested. No historical novelty claim. No arithmetic infinite-zero transfer established. Earlier checkpoint/master reports are unchanged.

## Mathematical statement

Fix an integer m>=1 and C>=0. For every ordered real configuration c=(c_1,...,c_m) in[-C,C]^m (repetitions allowed), every N>=0 and L=N+m, put

Q_(L,c)(z)=product_(j=1)^m(1-exp(-ic_j/L)z),

E_(N,c)=inf_(deg A<=N)||1-Q_(L,c) A||²_(L²(S¹,dt/(2pi))).

The optimum is defined by this polynomial problem even when distinct real c_j map to the same circle point. Define normalized Hermite divided differences

h_j(x;c)=j! i^(-j)[c_1,...,c_(j+1)]_u exp(iux), 0<=j<m,

with repeated nodes interpreted by confluent derivatives, and G(c)_(jk)=integral_0^1 h_j(x;c) conjugate(h_k(x;c))dx. Let e_0=(1,0,...,0)^t and

kappa(c)=e_0* G(c)^(-1)e_0.

Then G(c) is positive definite, continuously in all configurations including every collision stratum. Kappa is continuous, real, positive, and invariant under permutation of the nodes. For fixed m,C,

sup_(c in[-C,C]^m)|L E_(N,c)-kappa(c)|=O_(m,C)(1/L).

Here is an explicit coarse constant. Let H_m=(1/(j+k+1))_(0<=j,k<m), T_m=trace(H_m^(-1)),

s=1/(1+2C sqrt(m T_m)), delta=s^(2m-1)/(4T_m), D=2m(C+m).

For every N>=0 and every configuration,

|L E_(N,c)-kappa(c)| <= (4D²+2D)/(delta² L).                 (A)

For L>=2D/delta the sharper bound

|L E_(N,c)-kappa(c)| <= (2D/delta²+2/delta)/L               (B)

holds. Constants are intentionally loose. In particular, no numerical usefulness is claimed when m is large.

If all c_j are equal, G is the Hilbert matrix H_m and kappa=m². Thus the limit includes the complete coalescence value and partial collisions without assuming a minimum separation.

## Prior work and exact provenance

Burnol math/0103058v2 §2, pp.5–6, obtains multiplicity-squared approximation constants from jet Gram matrices for fixed roots. BCF1211.5191v1 Theorem2,p.3, considers a particular explicit reciprocal-coefficient window for fixed simple roots. Neither is cited as establishing(A).

The relevant stable basis is established prior mathematics. Avdonin–Ivanov, **Exponential Riesz bases of subspaces and divided differences**, math/0103160v1, Definition1, Eq.(4), Theorem2 and its proof, treat exponential divided differences with repeated nodes. Their Lemma5,pp.14–15, proves uniform finite-cluster Gram and inverse bounds via compactness; its Hilbert space and frequency assumptions differ from the present finite-interval setting. We use the same established stabilization mechanism, with a direct quantitative finite-interval bound and finite-grid quadrature. Carl de Boor, **Divided Differences**, math/0502036v1, §9 Eq.(52),pp.63–64, states the Hermite–Genocchi integral representation. Only these specified portions of the two additional sources were read; neither whole-paper audit is claimed. These sources substantially weaken any claim that the basis or compactness argument is new. Historical priority for the exact quantitative specialization has not been searched exhaustively.

## Hermite–Genocchi representation and collision stability

The integral representation gives

h_j(x;c)=x^j E exp(ix U_j),

where U_j=sum_(r=1)^(j+1)t_r c_r and(t_r) is uniform on the j-simplex (the simplex has volume1/j!, which the normalization j! cancels). For j=0 this means U_0=c_1. Consequently, for0<=x<=1,

|h_j|<=x^j, |h_j-x^j|<=C x^(j+1),

|h_j'|<=j+C, |h_j''|<=(j+C)².

Terms with negative powers of x in differentiating x^j are absent when their integer coefficient is zero. The functions are jointly continuous in all nodes, including repetitions. Their Taylor expansions start with x^j. Thus the matrix of derivatives at0 is triangular with nonzero diagonal j!, proving linear independence for every configuration. Their continuous Gram matrix is therefore positive definite. This already proves uniform invertibility by compactness; the next argument supplies an explicit lower bound.

## Explicit lower Gram bound

For a coefficient vector a=(a_0,...,a_(m-1)), restrict integration to0<=x<=s and write x=st, b_j=a_j s^j. Then

sum a_j h_j(st)=sum b_j t^j + error(t),

with |error(t)|<=Cs sum|b_j| t^(j+1)<=Cs sqrt(m)||b||_2. The polynomial part has L²(0,1) norm at least ||b||_2/sqrt(T_m), because lambda_min(H_m)>=1/trace(H_m^(-1))=1/T_m. By the definition of s,

Cs sqrt(m)<=1/(2sqrt(T_m)).

The triangle inequality gives norm at least ||b||_2/(2sqrt(T_m)). Returning to x and using s<=1 yields

||sum a_j h_j||²_(L²(0,1)) >=s||b||²/(4T_m)
                              >=s^(2m-1)||a||²/(4T_m)=delta||a||².

This proves G(c)>=delta I uniformly. The constant does not depend on separation or the collision pattern.

For explicit evaluation one may use

T_m=sum_(j=0)^(m-1)(2j+1) binom(m+j,m-j-1)^2 binom(2j,j)^2,

the trace of the classical inverse Hilbert matrix. Alternatively, defining T_m as the trace of the inverse rational matrix avoids requiring this closed identity; it is a finite exact computable constant. The proof only uses its defining matrix property.

## Finite coefficient constraints and aliases

For a residual R(z)=sum_(k=0)^L r_k z^k, divisibility of1-R by Q is equivalent to value1 and zero higher jets at its circle roots. If L>C/pi, distinct real nodes in[-C,C] cannot differ by2pi L. In that range the circle map is injective on distinct nodes. Hermite interpolation in the frequency variable applied to R(exp(iu/L)) then makes these constraints equivalent to

sum_(k=0)^L r_k h_j(k/L;c)=delta_(j0), 0<=j<m.

The repeated-node assertion follows by the chain rule: u→exp(iu/L) has nonzero derivative, so its jet transformation is triangular and invertible. Newton/Hermite divided differences of the constant function1 are1 in order0 and0 in higher orders. The normalization j!i^(-j) preserves these right-hand sides.

Let d=L+1 and G_L=(1/d)sum_(k=0)^L h(k/L)h(k/L)*. The minimum-norm coefficient formula and Parseval give

E_(N,c)=(1/d)e_0* G_L^(-1)e_0,

when the constraints above apply. This is an exact formula, not an asymptotic. It also includes all actual coincidences c_j=c_k. A nonzero alias at small L is handled directly by the original polynomial definition; the frequency divided-difference formula is not asserted there.

The limiting kappa is independent of the node order: each ordered divided-difference system is an invertible transformation of the same evaluation/jet constraints with the same constant target. Alternatively, uniform convergence to the permutation-invariant actual optimum proves this directly.

## Uniform quadrature and proof of(A),(B)

The normalized endpoint sample mean of a K-Lipschitz function differs from its integral by at most K/(L+1). This follows by writing it as L/(L+1) times the left rectangle mean plus the endpoint term. Every Gram entry h_j conjugate(h_k) has Lipschitz constant at most j+k+2C<=2(C+m). Thus

||G_L-G||_op <=D/(L+1).

Assume L>=2D/delta. Then G_L>=delta I/2. The resolvent identity gives

||G_L^(-1)-G^(-1)||<=2D/(delta²(L+1)).

Also ||G_L^(-1)||<=2/delta. Using L/(L+1)=1-1/(L+1) in the exact optimum formula proves(B). The large-L assumption implies L>C/pi: since delta<=1/4 and D>=2mC, its threshold is at least16mC. Therefore the constraint equivalence has not assumed away a possible alias.

For all remaining L<2D/delta, the trivial competitor A=0 gives0<=E<=1, and kappa<=1/delta. Hence

L|L E-kappa|<=L²+L/delta <(4D²+2D)/delta².

This also covers all finite aliases without evaluating a singular Gram quotient. The large-L constant in(B) is bounded by the constant in(A), because D>=2 and delta<=1/4. This proves the all-L assertion.

## A uniform first correction

The same stabilization yields more than the requested first-order error. Define

B_end(c)=[h(0)h(0)*+h(1)h(1)*]/2,

v=G^(-1)e_0, beta(c)=v*B_end v>=0.

For L>=2D/delta,

|L E_(N,c)-kappa(c)+beta(c)/(L+1)| <=K_2/L²,              (C)

uniformly in the configuration, where one admissible explicit constant is

K_2=[2m+M_2/12]/delta²+2D²/delta³, M_2=4m(C+m)².

Proof. Composite trapezoidal quadrature of the twice continuously differentiable Gram entries gives

G_L=G+[B_end-G]/(L+1)+R_L, ||R_L||<=M_2/(12L²).

The entry second derivatives are bounded by(j+k+2C)²<=4(C+m)². Put H=B_end-G; ||H||<=2m. The second-order resolvent identity yields

G_L^(-1)=G^(-1)-G^(-1)(G_L-G)G^(-1)+error,

with error norm at most2D²/(delta³ L²). Replacing G_L-G by H/(L+1) adds at most M_2/(12delta²L²). Finally multiply its(0,0)entry by L/(L+1). The coefficient of1/(L+1) is

kappa+e_0*G^(-1)H G^(-1)e_0=e_0*G^(-1)B_end G^(-1)e_0=beta.

The leftover term from this multiplication is bounded by2m/(delta²L²), proving(C).

At complete coalescence, kappa=m² and beta=(m^4+m²)/2. The latter follows either from the inverse Hilbert matrix or by matching(C) with the exact product-ratio optimum established and independently reviewed in multiplicity_general.md. In particular the first correction approaches the limit from below for each fixed configuration unless beta=0. No monotonicity in N or in the node separations is asserted.

## What this does not establish; missing arithmetic lemma

1. m is fixed. Delta deteriorates rapidly with m; the theorem provides no uniform large-cluster bound. This matters because zero counts in growing windows need not stay bounded.
2. Optimal residuals depend on exact root positions. They need not correspond to a Dirichlet polynomial with useful arithmetic coefficients.
3. Finite-interval exponential Gram control does not bound sums of zeta principal parts, normalize the number-field spectral space, or control contour tails.
4. The compact parameter assumption controls scaled cluster diameter. It cannot be silently applied to every zero cluster at every height.
5. Source results on Riesz bases have global separation/density/generating-function assumptions. The local compact theorem does not prove these assumptions for zeta zeros.

A precise next lemma to seek is a **grouped principal-part resolvent estimate**: for a finite cluster of m zeros inside a fixed compact scaled window, construct a divided-difference representation of the entire cluster's residue contribution with coefficient norms controlled by a cluster-invariant arithmetic quantity, rather than by separate |zeta'(rho)|^(-1). One must then prove a summable bound over all clusters and a uniform tail estimate sufficient for contour shifts. This is a research requirement, not an established result or an RH criterion supplied here.

## Reproducibility and review scope

The companion multicluster experiment uses the complete-homogeneous-polynomial series for normalized exponential divided differences, avoiding subtraction of close frequencies. Numerical Gram integrations and solves are explicitly unvalidated double-precision stress tests; the proof above does not depend on them. Sources remain private reading copies. Additional source records and theorem statements are in the round2 files, not frozen master manifests.

## Two additional consequences

**Translation-invariant scope.** The compact condition may be weakened to max c_j-min c_j<=2C, with arbitrary common center. Translating every node by a multiplies all h_j by exp(iax); both continuous and discrete Gram matrices are unchanged. Rotating the circle variable by exp(-ia/L) likewise leaves the actual approximation optimum unchanged. Recenter at the midpoint of the extreme nodes before applying the constants. Thus the theorem bounds a cluster by its diameter, not its absolute location. This is the translation property already present in Avdonin–Ivanov Theorem2(iv), here applied to the polynomial optimum.

**Uniform eventual one-sided approach.** Since h_0 has unit norm and its interpolation target is1, kappa>=1. Moreover h(0)=e_0, so beta>=|v_0|²/2=kappa²/2>=1/2. Therefore(C) implies L E_(N,c)<kappa(c) uniformly once L>=2D/delta and L>4K_2. This is eventual comparison with the limiting constant; it asserts no monotonicity of finite-N errors.
