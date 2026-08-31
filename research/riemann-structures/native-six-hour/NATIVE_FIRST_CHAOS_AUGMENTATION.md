# Native first-chaos augmentation, physical-mask leakage and a variational source

Status: exact finite-source theorems; bounded replay awaiting serialized validation.
Scope: the L-102707 half-geodesic tensor and its primewise endpoint-preserving
deformations. This is not a common projector already identified with every
quadratic-class, Boolean-degree or finite-field Wick decomposition.

## 1. FC-1: the native tangent has only constant and singleton Walsh sectors

Fix a labelled product K=prod_p p^(e_p), with each local exponent allocation
a_p in {0,...,e_p}. On its complete factor space let J_p replace a_p by e_p-a_p.
These commuting involutions preserve the actual product K. The finite group
is (Z/2)^r, and its character projectors are

\[
 \Pi_S=\prod_{p\in S}(I-J_p)/2\prod_{p\notin S}(I+J_p)/2,
 \qquad \mathcal A=\Pi_\varnothing.                 \tag{1}
\]

Write ell_p=ell_(u_p(s)) for the half-geodesic local source, with the full
chain-rule derivative along a primewise path. The native current density is

\[
 2\dot\Lambda\otimes\Lambda
 =\sum_p2\dot\ell_p\otimes\ell_p
             \bigotimes_{q\ne p}(\ell_q\otimes\ell_q).             \tag{2}
\]

Every factor q!=p is invariant under J_q. Decomposing the one differentiated
factor into its symmetric and antisymmetric parts proves, coefficientwise,

\[
 \Pi_S(2\dot\Lambda\otimes\Lambda)=0\quad(|S|\ge2).                 \tag{3}
\]

The same holds after integration: int(2 dotLambda tensor Lambda)ds equals
int(dotLambda tensor Lambda)(2 ds), with the factor two used exactly once. The constant
sector is the endpoint tensor lambda tensor lambda minus lambda^square tensor
lambda^square; the singleton sectors contain the path-dependent antisymmetric
connection integrals. Derivative-site labels are summand provenance in this
coefficient statement. Their separate literal diagonal is retained before
aggregation, as specified in GEODESIC_FACTOR_EXCHANGE.md.

The local symmetric and antisymmetric dimensions are
s_e=floor(e/2)+1 and a_e=ceil(e/2). Hence the allowed subspace has dimension

\[
 d_{\le1}=\prod_p s_{e_p}
            +\sum_p a_{e_p}\prod_{q\ne p}s_{e_q}.                   \tag{4}
\]

For the authenticated zero chart, the full factor space has dimension 3888,
the constant sector dimension 32, and the singleton sectors total 208.
For the held-out positive chart, the corresponding numbers are 720,12,68.
These are dimensions of the allowed Walsh subspace, not a claim that the
one-parameter native curve spans it. No accessibility theorem is inferred.

## 2. FC-2: a source-defined augmentation with an exact physical shadow

Let J=prod_p J_p. On the first-chaos range (3),

\[
 \mathcal A=(I+J)/2,\qquad I-\mathcal A=(I-J)/2.                    \tag{5}
\]

Product collapse C_K satisfies C_K A=C_K. The scalar ratio observation R_K
of GEODESIC_FACTOR_EXCHANGE.md intertwines J with t-reflection T. Thus, on
this exact source range,

\[
 R_K\mathcal A=E_+R_K,\qquad R_K(I-\mathcal A)=E_-R_K.             \tag{6}
\]

The original measure nu=|kappahat(t)|^2dt/(2pi) is even. The mean and the sum
of singleton sectors are therefore orthogonal in its Hilbert space.
Different singleton sectors need not be mutually orthogonal there.
Individual J_p do not generally act by a transformation of the one scalar
Mellin variable; coordinate reflections exist before restriction in a
multivariate Mellin representation, which is a different observation space.

This supplies an actual augmentation/reflection bridge for the source (2).
It does not identify its r primewise characters with the four quadratic
classes, nor with parity of the number of core primes. On a general source,
even higher Walsh sectors survive global exchange, so (5) would be false.
Moreover the constant sector can have zero product collapse and a nonzero
ratio field, as the complete zero chart already shows.

## 3. FC-3: an actual physical mask creates an order obstruction

Use the zero-chart ordered pair N=1005930209094, M=997518551435. Consider its
local-swap orbit O: every exponent-one or exponent-two label lies wholly on
one side. It has d=512 elements. At the endpoint, every factor product has
the same coefficient

\[
 a=-1/524288.
\]

By the exact endpoint identity, (A v)|_O is the constant a. Let P be the
physical ratio mask 1/8<n/m<8, and let h be the number of orbit elements it
retains. The pair (N,M) and its swap are retained; moving 71^2 from the left
to the right changes N/M by 71^(-4) and leaves the mask. Hence 0<h<512.
P is invariant under global exchange, but not under each J_p. Pairing every
retained factorization with its swap gives

\[
 (\mathcal A P v)|_O=a\,h/512,\qquad
 (P\mathcal A v)|_O=a\,1_{\{1/8<n/m<8\}}.                         \tag{7}
\]

The actual source commutator is nonzero, and its physical counting norm on
this orbit is exactly

\[
 \|[\mathcal A,P]v\|^2_{\ell^2(O)/K}
 =\frac{|a|^2}{K}\,h(1-h/512).                                    \tag{8}
\]

All factor frequencies are distinct, so the corresponding ratio field is
also nonzero in L2(nu); this follows from independence of finite exponentials
and nonzero absolutely continuous nu. Equation (8) is not a lower bound for
that observed norm or for a numerical condition number.

There is nevertheless a correct ordered identity. Since P commutes with
global exchange, on the original native first-chaos source

\[
 R_KP\mathcal A v=E_+R_KPv.                                      \tag{9}
\]

It is the reverse order A P that is not justified. The replay checks the
full vector, all local projectors and this mask without deleting the
complementary factor allocations.

The completed principal metric also requires a separate transport. For the
two zero-chart core lists, the original least primes are 71 and 401; after
the 71-square move they are 73 and 71. The weight
g^2 ell rho c_ell c_rho, with c_q=(q+1)/(q-1), changes. Thus local swaps are
not unitary for that reselected metric merely because they are unitary in
the fixed-K counting space. No full completed-source norm theorem is claimed.

## 4. FC-4: the actual Boolean half-source has a higher Walsh sector

The primitive first-chaos theorem must not be silently transported to the
canonical Boolean half-square. The exact L-106132/133 source permits a direct
test. On a core whose every prime exceeds U, a_U(empty)=0 and a_U(S)=-1 for
nonempty S. Its authenticated half-source f_U=a_U star h therefore satisfies

\[
 f_U(S)=\frac{(-1)^{|S|}-1}{2^{|S|}}.                              \tag{B1}
\]

Indeed the sum over nonempty subsets A of S is
-sum_A(-1/2)^(|S|-|A|)=(-1/2)^|S|-(1/2)^|S|. Thus f_U has only odd core
degrees. Its Boolean square gives b_U=2 at nonempty even depth and zero at
odd depth, with b_U(empty)=0.

On the complete r-label core-allocation cube, for positive even r,

\[
 f_U(S)f_U(C\setminus S)
 =2^{1-r}(1-\chi_C(S)),\qquad \chi_C(S)=(-1)^{|S|}.                \tag{B2}
\]

For odd r the whole array is zero. Equation (B2) has precisely the constant
and the full r-character Walsh sectors. At even r>=2 both are globally
exchange even. Hence the global-even projector is the identity on this array,
while the local augmentation removes a nonzero full-character term. The
first-chaos equivalence (5) is false for this actual canonical source.
This comparison uses two explicitly defined source constructions; it does
not assert an unproved linear map from the geodesic tangent to the half-square.

A literal bounded case is U=64, core {71,73,79,83}, and owners {2,3}.
There are eight nonzero core allocations per ordered owner assignment,
each with coefficient 1/4. The depth factor is theta^4 and the actual
L-106133 measure is (1-theta)dtheta, with integral 1/30. The two ordered
owner assignments therefore give

\[
 2\cdot8\cdot\frac14\cdot\frac1{30}=\frac2{15}.                  \tag{B3}
\]

the exact b_U(core)/binom(6,2) coefficient. Each of the sixteen nonzero
ordered half-source terms has coefficient 1/120 before the common physical
weight 1/(sqrt(6)*71*73*79*83). This is the Beta measure, not 2 d_tau.
At the original zero chart's three-prime left core, every already aggregated
f_U-half product vanishes: one of the two half-cores has even depth. This
explains its canonical zero without assigning invented weights to the
earlier 24 literal Vaughan histories.

The core-degree parity character in (B2) has thus been bound to an actual
slot-Walsh character in this rough Boolean allocation cube. It is the full
character, not the mean-zero projector on a residue cell. The nonzero mean
survives, so this parity observation does not remove the growing canonical
constant component or identify the full retained-gamma decoder.

## 5. FC-5: a source-derived probability simplex and an exact minimizer

For a squarefree product K=prod_(j=1)^r p_j, let the primewise schedules be
nondecreasing and piecewise continuously differentiable, with endpoints 0,1.
Define the activation numbers

\[
 q_j=\int_0^1u'_j(s)\prod_{i\ne j}u_i(s)\,ds.
\]

They are nonnegative and sum to one by differentiating prod_i u_i. This is
a probability vector derived from the source path; the primitive integration
measure remains 2 ds. If S records the primes in the left factor, then

\[
 v_K(S)=2(-1/2)^r\sum_{j\in S}q_j.                               \tag{10}
\]

The power schedules u_j=s^(a_j), a_j positive integers, give
q_j=a_j/sum_i a_i. Every positive rational probability vector is therefore
realized by a genuine path with the full chain rule. Sequential monotone
activation reaches the vertices as well. The uniform native geodesic gives
q_j=1/r; many parameterizations realize the same vector.

Take the explicit primes 3,11,101. Their eight divisors in increasing order
are 1,3,11,33,101,303,1111,3333, and adjacent ratios are at least 3. Consequently
every two distinct ratio frequencies differ by more than log8. The actual
kernel kappa has support of length log8, so its autocorrelation is zero on
all these differences. The full observed energy is therefore exactly

\[
 \|R_Kv(q)\|^2
 =\frac{\Gamma(0)}{2^rK}\left(1+\sum_j q_j^2\right).              \tag{11}
\]

It follows that the original uniform geodesic minimizes this actual positive
ratio energy among all monotone primewise schedules, with a unique minimizing
activation vector q=(1/r,...,1/r). This is not uniqueness of the path itself.
The minimum and maximum factors in parentheses are 1+1/r and 2. All these
paths have exactly the same signed product/Hankel current. The energy is
absolutely small, with its displayed 1/K normalization.

For more closely spaced primes, the off-diagonal kernel correlations need
not vanish; the same source reduction gives a finite quadratic optimization
in q, but (11) and the uniform minimizer cannot be assumed. This is the next
bounded deformation experiment, using the original kernel rather than
fitted arithmetic coefficients.

## 6. Replay boundary

The producer reuses only authenticated frozen geodesic coefficient code,
checks the complete two tuples, constructs every local involution and the
constant plus singleton decomposition, and replays the physical ratio mask.
It also checks the source-derived activation coefficients and the exact
frequency separation of the three-prime variational fixture. No large matrix,
prime search, approximate kernel quadrature or horizon extrapolation is used.

The results provide a real source projector, an exact observation map, a
specific failure to commute with a later physical restriction, and a positive
variational statement on an authenticated source deformation. They leave the
post-renewal decoder and the full amplified moment separate.
