# Actual source polarization, the prime-core domain, and four-node residuals

Status: NEW PROOF AND BOUNDED CONTROLS; independent exact-SHA review required.
Authoring base: `8f01064df805624c045877655893c324a220975d`.
RH remains unproved. No external novelty or priority claim is made.

## Frozen pre-computation design

This design is committed before evaluating any new actual-Xi matrix. The
algebraic four-node identity was discovered analytically and checked on the
single exact rational cell x=(1,2,3,4), p=(1,3,2,7). That discovery cell is
not held out. The arithmetic controls below will retain it as a known control.

The intended analytic results are: the exact full-line polarization of the
actual Fourier density; the equivalence between RH and closability of the
full prime multiplier on the finite exponential core; an exact four-node
factorization, its singular-anchor-safe residual, and its literal source
reconstruction. A pointwise positive one-spectator Volterra factorization
of the coefficient u+v is impossible. This last obstruction does not rule
out global factorization or an arithmetic source-specific construction.

Normalization: X(z)=xi_R(1/2+iz), Y(x)=xi_R(1/2+x)=X(ix),
F=Y'/Y, p(t)=F(sqrt(t))/sqrt(t), safe nodes x>1/2. The full-line
Fourier density is Phi=2 phi0 in XL1--XL4, not the historical half-density.

The numerical panel is fixed to these six ordered rational quadruples:

1. (3/4,1,3/2,2);
2. (1,2,4,8);
3. (1,65/64,33/32,67/64);
4. (2,3,5,7);
5. (8,16,32,64);
6. (16,32,64,128).

For every quadruple, compute the full native safe matrix, all its principal
minors, both four-node factors and divided-difference residuals, and the
fraction-free three-anchor residual. Use literal completed Xi through the
native FLINT zeta/Gamma series, with a fresh signed first jet at each node;
512-bit precision, no escalation, domain 1/2<x<=128. Retain every nonfinite,
zero-containing, or wrong-sign enclosure as unresolved or failed as
appropriate; do not move nodes. All six panels are finite controls only.

Exact controls use Fraction arithmetic and two independent determinant
routes (permutation expansion and elimination), including Gaussian rank-one
data, one-atom and two-atom Stieltjes data, the known discovery cell, and a
fixed rational grid of non-Stieltjes data. Test dimensions are capped at four.
The existing positive smooth exact-Xi-tail counterfeit is used as an
analytic countercontrol, not numerically integrated: its previously proved
off-real zero and wrong-sign Laguerre point imply that its polarized source
is not PSD. No new location, finite-order witness, or Xi zero is inferred.

Arithmetic class: MIXED {DIRECTED_BALL_ENCLOSURES, EXACT_RATIONAL,
CERTIFIED_INTEGER_COVERAGE}. Native ball endpoints are rounded outward to
dyadic rational intervals. Ordinary decimal output is display only.
Artifact and source seals, strict types/caps, fresh reconstruction, semantic
mutations, normal/optimized tests and exact emits are required before freeze.

The earlier integrated size-three theorem is used only in its repaired PSD
form, for safe real nodes, with grouped C2 convergence, multiplicities,
the corrected external lock, and the single shared critical reserve. It
does not provide strict three-anchor invertibility. No all-order source
positivity, prime factorization, closability, or RH premise is assumed.

## 1. Exact source kernel and function domains

Write xi_R(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2, with its
removable values. The pinned XL1--XL4 proof establishes

\[
 X(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,\qquad
 \Phi(u)=2\sum_{n\ge1}(2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2})
                  e^{-\pi n^2e^{2u}}.                         \tag{SP1}
\]

Use the even extension; Phi is smooth, strictly positive, and decays
superexponentially with all the real derivatives needed here. In particular
every polynomial/exponential weighted integral below is absolutely
convergent. Set s=a+b, d=a-b and

\[
 A(a,b)=\frac12\int_{|s|}^{\infty}
        \xi\Phi((\xi-d)/2)\Phi((\xi+d)/2)\,d\xi.       \tag{SP2}
\]

This is a real continuous symmetric kernel, invariant under (a,b)->(-a,-b).
It is pointwise positive. It need not be a positive-semidefinite kernel
merely because its integrand is positive.

For every M>=0, A and its first weak directional derivative are integrable
against exp(M(|a|+|b|)); A is also square integrable. To check the assertion,
use da db=ds dd/2 and |a|+|b|=max(|s|,|d|). Tonelli on absolute values
changes the s range to -xi<=s<=xi. Its length is 2xi; the remaining
integrand is bounded by a polynomial in xi,|d| times exp(M(xi+|d|))
|Phi((xi-d)/2)Phi((xi+d)/2)|. With u=(xi-d)/2,v=(xi+d)/2,
xi+|d|<=2(|u|+|v|), so the stated weighted integrability of Phi applies.
The same estimate with pointwise exponential bounds on Phi proves boundedness
and arbitrary exponential decay of A, hence A in L2. These arguments also
justify all subsequent finite sums, derivatives and integrations by parts.

For s>=0, changing xi=s+2r gives the exact Volterra expression

\[
 A(a,b)=\int_0^\infty(a+b+2r)\Phi(a+r)\Phi(b+r)\,dr.    \tag{SP3}
\]

For s<0 use reflection, not this unreflected formula. On both open
half-planes, and distributionally across s=0,

\[
 (\partial_a+\partial_b)A(a,b)=-(a+b)\Phi(a)\Phi(b).     \tag{SP4}
\]

Indeed the operator is 2 partial_s, and differentiating the lower endpoint
of SP2 gives SP4. At s=0 the derivative agrees from both sides and is zero;
there is no delta term. Integration by parts, with v=conjugate(w), gives

\[
 \boxed{\quad
 \frac{X'(z)X(v)-X(z)X'(v)}{v-z}
 =\iint_{\mathbb R^2}e^{iza}e^{-ivb}A(a,b)\,da\,db
 =:B_X(z,w).\quad}                                      \tag{SP5}
\]

For clarity, the transform of SP4 is i(v-z) times the transform of A;
the numerator in SP5 is i times the transform of (a+b)Phi(a)Phi(b),
using evenness to write X(v) with phase -ivb. The signs therefore give
SP5. The diagonal v=z is its removable entire continuation. There is no
factor 2pi: X uses the unnormalized forward Fourier transform in SP1.

Calibration: for Phi(u)=exp(-alpha u^2), alpha>0, direct integration gives

\[
 A(a,b)=\frac{e^{-\alpha(a^2+b^2)}}{2\alpha},\qquad
 B_X(z,w)=\frac{X(z)X(\bar w)}{2\alpha}.                \tag{SP6}
\]

This is a rank-one positive source and checks both the normalization and
the reflected half of SP2.

Here ``A is PSD'' means its quadratic form is nonnegative for every
complex compactly supported smooth function. Since A is a bounded
Hilbert--Schmidt integral operator, this is equivalent to positivity on L2.
It is equivalent to PSD of B_X at every finite upper-half-plane packet:
in the forward direction approximate each exponentially weighted feature
in SP5 by compact truncations, using the weighted bounds above. In the
reverse direction take continuous limits to real Fourier nodes. Finite
PSD then gives integrated PSD for compactly supported Fourier test functions
by Riemann sums. Fourier unitarity and density transfer it to all Schwartz
source tests and hence to L2. The harmless positive Fourier normalization
constants do not affect the sign. Thus this is an operator-kernel statement,
not pointwise positivity of A.

## 2. The full prime-core operator: closability is exactly RH

All Hilbert inner products below are conjugate-linear in the first argument.
On H=L2(0,infinity), put e_x(t)=exp(-xt), x>1/2, and let D be their
finite complex span. Distinct exponentials are linearly independent.
Laplace uniqueness, or the identity theorem followed by Fourier uniqueness,
shows that D is dense. The operator

\[
 T_0 e_x=F(x)e_x,\qquad F(x)=Y'(x)/Y(x),\quad
 Y(x)=\xi_R(1/2+x),                                    \tag{SP7}
\]

is consequently well-defined and densely defined. Y(x)>0 on this ray.
Let L map H unitarily to the right-half-plane Hardy space with norm
sup_(sigma>0) (2pi)^(-1) integral |h(sigma+it)|^2 dt, by
(Lh)(z)=integral exp(-zt)h(t)dt. Plancherel proves isometry; the
Paley--Wiener representation identifies its range. Point evaluation is
bounded, with reproducing kernel 1/(z+conjugate(w)).

For h in D(T_0*) with k=T_0*h, the adjoint identity on each e_x gives

\[
 (Lk)(x)=F(x)(Lh)(x)\quad(x>1/2).                     \tag{SP8}
\]

Both sides continue meromorphically to Re z>0; the identity theorem makes
SP8 valid there. Conversely, whenever F Lh extends holomorphically across
its apparent poles and belongs to H2, its inverse Laplace transform k
satisfies the adjoint identity for every element of D. This characterizes
the entire adjoint domain, not only a convenient subset.

If Y has a zero b in Re b>0 of multiplicity m>=1, then F has a simple
pole there with residue m. SP8 forces (Lh)(b)=0 for every h in D(T_0*).
This domain lies in the kernel of a nonzero bounded evaluation functional,
a proper closed hyperplane of H. It is not dense, so T_0 is not closable.
An off-critical zeta zero supplies such a b, after functional reflection
if needed. Therefore

\[
 T_0\text{ closable}\ \Longrightarrow\ \mathrm{RH}.    \tag{SP9}
\]

Conversely assume RH, now explicitly. The even genus-zero product in the
squared variable gives, locally uniformly on Re z>0,

\[
 F(z)=\sum_{\gamma>0}m_\gamma
   \left(\frac1{z-i\gamma}+\frac1{z+i\gamma}\right),
 \qquad\sum m_\gamma/\gamma^2<\infty.                 \tag{SP10}
\]

Thus F is holomorphic and Re F>=0. On H2 let M_F be maximal multiplication
by F: its domain is {h in H2: Fh in H2}. This operator is closed by bounded
point evaluation. Its domain is dense: for epsilon>0,
q_epsilon=(1+epsilon F)^(-1) is a bounded analytic multiplier of norm at
most one, F q_epsilon is bounded by 1/epsilon, and q_epsilon h belongs
to D(M_F). As epsilon decreases to zero, q_epsilon h converges pointwise
to h and stays norm bounded by ||h||. Density of reproducing kernels gives
weak convergence to h, and
||q_epsilon h-h||^2<=2||h||^2-2 Re<h,q_epsilon h> gives strong convergence.
This proves density without an unproved boundary-value interchange.

SP8 now says exactly L T_0* L^(-1)=M_F. Hence T_0 is closable and

\[
 \boxed{\quad \mathrm{RH}\iff T_0\text{ closable},\qquad
 L\overline{T_0}L^{-1}=M_F^*\quad\text{under RH}.\quad} \tag{SP11}
\]

The closed realization is an adjoint Hardy multiplier, not a self-adjoint
spectral multiplier on L2. This is a domain theorem, not a proof of its RH
premise. It is consistent with classical unbounded analytic Toeplitz theory;
the elementary argument here supplies the exact safe core and pole obstruction.

For g=sum c_i e_(x_i), direct integration gives

\[
 2\Re\langle g,T_0g\rangle
   =\sum_{i,j}\bar c_i c_j\frac{F(x_i)+F(x_j)}{x_i+x_j}.
                                                               \tag{SP12}
\]

If this form is nonnegative on D, T_0 is accretive and closable. Here is
the domain step explicitly: if g_n->0 and T_0 g_n->h, apply accretivity
to g_n+zv for each fixed v in D and z in C. Taking limits leaves a linear
term in z involving <v,h>, plus a nonnegative quadratic term. Varying z
arbitrarily near zero forces <v,h>=0; density gives h=0.
Together with SP9 and SP10 this proves the exact equivalences

\[
 \mathrm{RH}\iff H_F\text{ PSD on every finite safe packet}
 \iff T_0\text{ accretive}\iff T_0\text{ closable}.      \tag{SP13}
\]

Under RH the full right-half-plane kernel is positive by SP10's rank-one
pole features. Rotating to the upper half-plane gives B_X PSD, with
continuity at zeros. Conversely B_X PSD restricts at z=ix,w=iy to

\[
 B_X(ix,iy)=Y(x)Y(y)\frac{F(x)+F(y)}{x+y},              \tag{SP14}
\]

so SP13 applies. Consequently A in SP2 is PSD if and only if RH.
Neither smoothness, pointwise positivity, nor the positive theta tail pays
this sign. The pinned exact-tail counterfeit has a proved wrong-sign
Laguerre point on the real axis: there B_F(t,t)=F'(t)^2-F(t)F''(t)<0.
SP5 and continuity therefore show its A is not PSD, without any new
numerical integration or assertion about which safe packet detects it.

## 3. Prime expansion and the resolvent trap

Let A_0=-d/dt on H1(0,infinity), with no boundary condition. Then
exp(-u A_0)g(t)=g(t+u), and A_0 e_x=x e_x. The exact Euler identity on D is

\[
 T_0=(A_0+1/2)^{-1}_{D}+(A_0-1/2)^{-1}_{D}
 -\tfrac12\log\pi+\tfrac12\psi((A_0+1/2)/2)_{D}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\exp(-\log(n)A_0)|_D.
                                                               \tag{SP15}
\]

Subscripts D mean the algebraic diagonal operation on these exponential
eigenvectors. The formula is obtained by logarithmically differentiating
the literal completed xi expression at s=x+1/2>1. Each prime-power series
converges absolutely in H on each fixed finite core vector, because
sum Lambda(n)n^(-x-1/2)<infinity. No operator-norm convergence or extension
to all H is claimed.

The plus inverse is the restriction of the genuine bounded resolvent,
(A_0+1/2)^(-1)g(t)=integral_t^infinity exp(-(u-t)/2)g(u)du.
The minus inverse is not: e_(1/2) is in the kernel of A_0-1/2. Even its
algebraic restriction to D is nonclosable. For x_n=1/2+1/n,
g_n=(x_n-1/2)e_(x_n) tends to zero in H while
(A_0-1/2)^(-1)_D g_n=e_(x_n) tends to nonzero e_(1/2).
Individual pieces in SP15 therefore cannot be closed independently and
added as if they were ordinary self-adjoint functional calculus.

The cancellations in the full completed F must be retained. An equality
``T+T*=V*V'' needs specified operator or quadratic-form domains; the core
identity SP12 alone does not define such an operator sum or prove a
closable positive source factor. SP11 shows how strong an unconditional
closed realization of the full core would already be.

## 4. Exact four-node factorization

Take 1/2<x1<x2<x3<x4, set t_i=x_i^2, p_i=F(x_i)/x_i,
and H_ij=(x_i p_i+x_j p_j)/(x_i+x_j). Define

\[
 A_4=\det[1,t_i,p_i,t_i p_i]_{i=1}^4,\qquad
 C_4=\det[1,t_i,t_i p_i,t_i^2p_i]_{i=1}^4.
\]

The second factor is named C_4 here to distinguish it from B_X; the
producer's short JSON key for it is B. Then

\[
 \boxed{\det H=\frac{A_4 C_4}{\prod_{i<j}(x_i+x_j)^2}.} \tag{SP16}
\]

Here is a full polynomial proof, not an inference from sampled cells.
For fixed distinct positive t_i, A_4 is an irreducible quadratic in the
p_i over C. In its restriction p4=0 the coefficients of p1p2,p1p3,p2p3
are all nonzero (products of distinct t differences), with no squared
terms. The corresponding three-by-three symmetric coefficient matrix has
nonzero determinant, so the quadratic has rank at least three and cannot
factor into two linear forms. C_4 is obtained by replacing p_i by t_i p_i
and is likewise irreducible. They are not associates: their p_i p_j
coefficient ratios are t_i t_j, which are not constant over pairs.

On a dense open part of A_4=0, the four p values lie on a fractional-linear
function p(t)=c+d/(t+s). Its constant part contributes rank one to H;
the pole part contributes
d(x_i x_j+s)/((t_i+s)(t_j+s)), of rank at most two. Thus det H=0.
The generic fractional-linear parametrization follows directly from the
linear dependence among the four columns defining A_4; the exceptional
vanishing denominators and constant-denominator cases form proper algebraic
subsets. Similarly C_4=0 generically makes tp(t) fractional-linear, so
p(t)=c/t+d/(t+s), a rank-one zero-pole plus a rank-two pole contribution.
Therefore both coprime irreducible quadratics divide the homogeneous
degree-four polynomial det H in p, and det H=c(x) A_4 C_4.

Compare coefficients of p1^2 p2^2. In A_4 C_4 the coefficient is
t1 t2 (t2-t1)^2(t4-t3)^2. In det H it is the square of the cross-block
Cauchy determinant, namely
t1 t2 (x2-x1)^2(x4-x3)^2 / product_(i=1,2;j=3,4)(x_i+x_j)^2.
The ratio is precisely SP16. Polynomial continuation includes every
degenerate p configuration. Repeated x nodes follow by continuity, though
divided differences then need their confluent definitions.

Write Delta(t)=product_(i<j)(t_j-t_i) and use ordinary divided differences.
Newton row reduction gives

\[
 \frac{A_4}{\Delta(t)}=D_p,\qquad
 \frac{C_4}{\Delta(t)}=D_{tp},\qquad
 D_f=f[t1,t2,t3]f[t2,t3,t4]-f[t2,t3]f[t1,t2,t3,t4].    \tag{SP17}
\]

Indeed det[1,t,f,tf]/Delta is
f[123](tf)[1234]-(tf)[123]f[1234]; the identity
(tf)[1,...,r]=t1 f[1,...,r]+f[2,...,r] yields SP17.
Thus four-node PSD, when every proper principal minor is already PSD,
is exactly D_p D_(tp)>=0. This uses the principal-minor characterization
of PSD, not a division by a possibly zero three-node determinant.

In the confluent limit, D_f tends to (f''/2)^2-f'f'''/6,
the negative Schwarzian numerator divided by twelve. This identifies the
precise overlap with the older p-Schwarzian/impedance work at PR460.
The four-point residual is not claimed to be a wholly new classical
invariant. Nor does the older two-node Loewner statement automatically
constitute a source-exact proof of both factors' required global signs.
The tp factor and a uniformly valid source-controlled sign or product
estimate remain explicit burdens here.

## 5. Literal source reconstruction and singular anchors

No zeros or formal positive spectral measure are needed to compute SP16.
Since Y_i=integral Phi(u) exp(x_i u)du and
Y'_i=integral u Phi(u) exp(x_i u)du, row multilinearity gives

\[
 A_4=\frac{\int_{\mathbb R^4}\prod_i\Phi(u_i)e^{x_i u_i}
             \det[x_i,x_i^3,u_i,x_i^2u_i]_{i=1}^4\,du}
            {\prod_i x_iY_i},                           \tag{SP18}
\]

and C_4 has determinant rows [x_i,x_i^3,x_i^2u_i,x_i^4u_i]
in the same integral. Absolute integrability follows from SP1's exponential
moments; this is an exact source formula, not a PSD assertion for its signed
polynomial. It exposes what a source-level elimination must control.

For a complementary quadratic reconstruction let M=H[1,2,3], h_i=H_(i4),
delta=det M, alpha=adj(M)h and c=(-alpha_1,-alpha_2,-alpha_3,delta).
The adjugate identities, valid even when M is singular, give

\[
 \det H=\delta H_{44}-h^T\operatorname{adj}(M)h,
 \qquad c^THc=\delta\det H.                            \tag{SP19}
\]

This follows by expanding the bordered determinant and using
M adj(M)=delta I. Consequently, for
q(a)=sum_i c_i exp(-x_i a)/Y_i, SP5 and SP14 give

\[
 \iint A(a,b)q(a)q(b)\,da\,db=\delta\det H.           \tag{SP20}
\]

All q integrals converge by the earlier weighted bounds. If delta>0,
dividing gives the usual Schur residual and its conditional source sign.
If delta=0, SP20 can vanish without detecting a negative determinant;
one must retain SP16 and all proper principal minors. The canonical
size-three theorem provides PSD, not this missing strictness.

## 6. A precise local Volterra factorization obstruction

On a,b>=0 and a fixed r>=0, the integrand in SP3 has coefficient
u+v, where u=a+r,v=b+r. For two distinct u,v>r its coefficient matrix is

\[
 \begin{pmatrix}2u&u+v\\u+v&2v\end{pmatrix},\qquad
 \det=-(u-v)^2<0.                                      \tag{SP21}
\]

Multiplication by the strictly positive Phi(u),Phi(v) preserves this
negative determinant. Thus no family of positive-Hilbert-space features,
with any nonnegative measure, can factor this fixed-r integrand as a Gram
kernel on all a,b>=0. This rules out the natural pointwise, one-spectator,
positive Volterra factorization. It does not rule out cancellations across
r, a global change of variables, nonlocal features, or additional arithmetic
structure. Indeed SP6's Gaussian integrated kernel is PSD despite SP21.

## 7. Finite outcome, provenance, and the next mathematical burden

At the frozen six actual-Xi quadruples all 90 principal minors have strict
positive directed enclosures; A_4 and C_4 are strictly negative in all six.
The clustered quadruple has determinant approximately 3.5023e-42, so it
also checks that near-confluence was not silently replaced by a midpoint
or a diagonal limit. All six three-anchor determinants are positive on
this finite panel only. These facts provide no global positivity evidence
and do not establish the sign for any untested packet.

Exact reconstruction covers 30 Gaussian/Stieltjes model cells, all 486
declared rational grid cells, the known discovery cell, and ten fixed-r
Volterra determinant controls. Permutation and elimination determinant
routes agree. All source identities and principal-minor coverage are
retained. Gaussian and single-pole rank deficiencies are intentional,
not failed positivity certificates. The native primitive uses a fresh
two-term signed acb_series jet at each of the 24 declared evaluations.

The companion manifest pins the actual source, its counterfeit, the
canonical size-three repairs, the old exact three-node and all-order
criteria, the historical Schwarzian work, and both recent synthesis
identities. The Segre synthesis is provenance/architecture context only:
no cofactor or syzygy theorem is imported into this analytic source proof.
Classical Fourier/Paley--Wiener, closed-adjoint and Cauchy determinant
theory are used explicitly. Related primary references include
[Rosenfeld's unbounded Toeplitz study](https://arxiv.org/abs/1412.5969)
and [Ishikawa--Okada--Tagawa--Zeng's generalized Cauchy identities](https://arxiv.org/abs/math/0411280).
They provide context, not an asserted priority comparison or a substitute
for SP16's proof. The literal xi normalization is [DLMF25.4.4](https://dlmf.nist.gov/25.4.E4).

The worthwhile next burden is a uniform arithmetic/source sign estimate
for the paired SP18 integrals (or SP20 on a legitimately strict anchor),
including degeneration and unbounded node separation. Proving closability
of T_0 without assuming RH would solve the same all-order obstruction;
calling it a harmless domain repair would be circular. No new global
positivity, closed prime form, all-order factorization or RH conclusion
is asserted by this packet.
