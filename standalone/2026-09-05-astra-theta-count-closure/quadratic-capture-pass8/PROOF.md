# A sharp quadratic-width limit for the actual signed test spaces

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required.
RH and the full arithmetic sign remain UNPROVED.
Scope: the exact L2(0,infinity) metric, all integer orders specified below,
strong limits of prescribed projections, and trace-norm limits for the full
invariant heat-Hankel operator. No finite zero verification is used.
Scientific base: PR #790, 513d8f206bb597747afcb7a7410cdf768519d548.
Local labels ASTRA-QC-01 through ASTRA-QC-06 belong only to this packet.
General Laguerre, spectral-calculus, and trace-class tools are classical.
No external novelty claim is made.

## 1. The spaces, and the change of scale this pass actually makes

Use exactly the generators from both pass-seven packets:

    U_j(A)=A/(A+1)^j,
    u_j(t)=exp(-t)[t^(j-2)/(j-2)!-t^(j-1)/(j-1)!], j>=2.

Laplace(u_j)=U_j and integral u_j=0. Put

    E_(m,d)=span{u_m,...,u_(m+d)}, m>=3, d>=0,
    W_(r,n)={t^r exp(-t) p(t): deg p<=n}, r>=1, n>=0,
    r=m-2.

All spans can be complexified without changing the real symmetric matrices.
Let P_(r,n) and Pi_(m,d) denote ORIGINAL-L2 orthogonal projections.
The exact inclusion is E_(m,d) subset W_(r,d+1), of codimension one.

For a>=0 let P_a be multiplication by 1_[a,infinity). Also set P_infinity=0.
The convention at the single point a is immaterial in L2.

**ASTRA-QC-01 (sharp projection transition).** Suppose r tends to infinity
through positive integers and d_r/r^2 tends to c in [0,infinity]. Then

    P_(r,d_r) -> P_a strongly,
    Pi_(r+2,d_r) -> P_a strongly,
    a=1/(2c),                                      (QC1)

where c=0 means a=infinity and c=infinity means a=0. In particular:

- d=o(r^2): both projections tend strongly to ZERO;
- d/r^2 -> c in (0,infinity): the limit retains exactly t>=1/(2c);
- d/r^2 -> infinity: both projections tend strongly to the IDENTITY.

These projections are not nested as r varies. No nested-space theorem is
being applied. The zero-integral endpoint condition is retained in the
second assertion, not discarded as harmless.

The earlier m>=constant*d and m>=constant*d*log(d+2) tail regimes lie in
c=0. A small compressed form there can occur for ANY compact operator,
including an indefinite one. This does not invalidate their signed prime
identities. It identifies their limitation in the original metric.

## 2. Exact Laguerre spectral realization

Write L_j^(alpha) for generalized Laguerre polynomials, with the convention

    L_j^(alpha)(x)=sum_(k=0)^j (-1)^k binom(j+alpha,j-k)x^k/k!.

For integer r>=1 the functions

    phi_(r,j)(t)=sqrt(2^(2r+1) j!/(j+2r)!)
                      t^r exp(-t) L_j^(2r)(2t), j>=0,       (QC2)

form a complete orthonormal basis of L2(0,infinity).
Orthogonality follows by the substitution x=2t and Rodrigues integration
by parts with weight x^(2r)exp(-x); its norm is (j+2r)!/j!.
Boundary terms vanish at both ends. For completeness, if f is orthogonal
to every t^(r+j)exp(-t), then

    F(z)=int_0^infinity conjugate(f(t)) t^r exp(-(1+z)t)dt

is analytic for Re z>-1 and all its derivatives at zero vanish. The identity
theorem, then uniqueness of the Fourier transform on a positive vertical
line, gives f=0. Cauchy-Schwarz supplies absolute convergence and derivative
bounds on compact sub-half-planes. This proves completeness independently
of an unmentioned choice of self-adjoint boundary condition.

Define a self-adjoint positive operator H_r by this basis and eigenvalues

    H_r phi_(r,j)=(2j+2r+1)phi_(r,j).

Its domain consists of basis expansions with square-summable coefficients
weighted by (2j+2r+1)^2. On C_c^infinity(0,infinity), the Laguerre equation
and integration by parts give the differential expression

    H_r f=-(t f')'+(t+r^2/t)f.                              (QC3)

To verify membership of a compactly supported smooth g in the spectral
domain, integrate against each phi: the coefficients of the classical
right side are (2j+2r+1)<phi,g>. Parseval proves the weighted square sum
is finite and identifies the operators there. In particular no unstated
operator-core claim for H_r is required.

Let A_r=H_r/r^2 and let M be multiplication by 1/t on its natural domain.
On compactly supported smooth g,

    (A_r-M)g=r^-2 H_0 g,    H_0 g=-(t g')'+t g.             (QC4)

The expression H_0 is used only on such g in this identity.

## 3. Resolvent convergence, with the spectral limit justified

Set B_r=(I+A_r)^(-1) and B=(I+M)^(-1). All are positive contractions.
For f=(I+M)g, g in C_c^infinity(0,infinity), the exact resolvent equation is

    B_r f-g=-r^-2 B_r H_0 g.

Consequently ||B_r f-Bf||<=r^-2||H_0 g||. Such f form a dense set (indeed
multiplication by 1+1/t is an invertible smooth operation on each compact
subinterval away from zero). Contraction bounds extend convergence to
EVERY f in L2. Thus

    B_r -> B strongly,   (Bf)(t)=t/(1+t) f(t).             (QC5)

Polynomial functional calculus and uniform polynomial approximation give
v(B_r)->v(B) strongly for every continuous v on [0,1]. Here is the needed
passage to a moving discontinuous cutoff, rather than a tacit assumption.
The projection P_(r,n_r) is exactly

    1_[b_r,1](B_r),    b_r=1/[1+(2n_r+2r+1)/r^2].

If n_r/r^2->c, b_r->b=1/(1+2c), with the endpoint conventions b=1,0.
For a small delta, approximate 1_[b,1] by continuous functions agreeing
outside the delta neighborhood of b. For large r, the moving threshold
b_r is also within that neighborhood. The squared norm of the error on
f is bounded by <f,v_delta(B_r)f>, where 0<=v_delta<=1 is continuous,
equals one on the neighborhood, and vanishes outside a slightly larger
one. Equation QC5 passes this upper bound to B. Multiplication by t/(1+t)
has no spectral atom at ANY b in [0,1], including its two endpoints.
Dominated convergence therefore makes the limiting bound tend to zero
with delta. Continuous functional calculus on the middle term proves

    P_(r,n_r) -> 1_[b,1](B)=P_(1/(2c)) strongly.            (QC6)

This proves the W part of QC1, including both extreme regimes.
Only ordinary self-adjoint spectral calculus was used; no asymptotics of
individual Laguerre zeros or oscillatory Laguerre kernels are imported.

## 4. The endpoint-zero constraint has the SAME limit

Define the bounded causal operator

    (Vf)(t)=int_0^t exp(-(t-s))f(s)ds,   T=I-V.

Young's inequality gives ||V||<=1, hence T is bounded. Its Laplace multiplier
is A/(A+1), so exactly

    T W_(r,d)=E_(r+2,d).                                   (QC7)

The factorial factors merely rescale basis vectors. T is injective, and
the image has dimension d+1. Its inclusion in W_(r,d+1) has codimension one.
It is precisely the kernel of the integral functional on that finite space.
Let v_r be a unit vector spanning its orthogonal complement there. Then

    Pi_(r+2,d)=P_(r,d+1)-|v_r><v_r|.                       (QC8)

We prove v_r converges weakly to zero; this is the load-bearing endpoint
argument. Both W projections in QC7/QC8 have strong limit P_a by QC6.
Any weakly convergent subsequence of v_r has a limit v in P_a L2: for
h in ker P_a, <v_r,h>=<v_r,P_(r,d+1)h> tends to zero.
For h in P_a L2, orthogonality in QC7 gives

    <v_r,T P_(r,d)h>=0.

The second factor tends in norm to Th, so <v,Th>=0. T preserves P_a L2
by causality and has dense range ON that space. To check density directly,
translate a to zero. If T^*g=0, then g=V^*g, that is,

    g(t)=int_t^infinity exp(-(s-t))g(s)ds=:G(t).

Locally in the weak sense G'=G-g=0; G is constant and is in L2, so g=0.
Therefore ker T^*=0 and the range is dense. This also covers a=0.
For a=infinity the space is zero already.
It follows that v=0 for every weak cluster point. Boundedness and weak
sequential compactness in the Hilbert space give v_r weakly ->0.
Thus the rank-one projections in QC8 tend strongly to zero. The second
assertion of QC1 follows.

One cannot remove a moving rank-one condition without this argument:
a fixed omitted direction WOULD change a strong limit. Its disappearance
here is a consequence of the causal multiplier's dense range on every
limiting tail space.

## 5. Two quantitative checks on the sharp scale

**ASTRA-QC-02 (finite-time energy).** Every f in W_(r,n) satisfies

    int_0^T |f(t)|^2 dt <= [2T(n+r)/r^2] ||f||_2^2.         (QC9)

For E_(m,d), r=m-2, replace n by d+1. To prove QC9, write f=t^r exp(-t)p.
In the Laguerre weight w=t^(2r)exp(-2t), put I=int w|p|^2 and
J=int w|p|^2/t. The degree-n Sturm energy is

    int t w |p'|^2 <=2n I.

It follows either by the orthogonal expansion of p, or by the symmetric
operator -w^-1(tw p')', whose eigenvalues are 2j. Integration of
(w|p|^2)' has zero endpoints and gives

    r J <= I+sqrt(2n I J).

With x=J/I, Young's inequality bounds sqrt(2nx)<=rx/2+n/r. Hence
x<=2(n+r)/r^2. Finally int_0^T |f|^2 <=T J. All coefficient signs and complex
cross terms are retained. This proves quantitative escape when n=o(r^2).

**ASTRA-QC-03 (exact calibration on one fixed vector).** With e(t)=exp(-t),

    ||P_(r,n)e||^2/||e||^2
      = (n+r)!^2/[n!(n+2r)!]
      = product_(j=1)^r (n+j)/(n+r+j).                      (QC10)

For a direct proof, integration of QC2 against e gives

    |<phi_(r,j),e>|^2
       = (r^2/2) (j+r-1)!^2/[j!(j+2r)!].

The cumulative sum telescopes: if q_n=(n+r)!^2/[n!(n+2r)!], then
q_0=(r!)^2/(2r)! and q_n-q_(n-1)=r^2(n+r-1)!^2/[n!(n+2r)!].
As ||e||^2=1/2, QC10 follows. Also

    exp[-r^2/(n+1)] <= q_n <= exp[-r^2/(n+2r)].             (QC11)

Use x/(1+x)<=log(1+x)<=x in the finite product to prove both bounds.
Consequently when n/r^2->c in (0,infinity), q_n->exp(-1/c).
This is exactly the norm fraction of e on [1/(2c),infinity), independently
checking the factor TWO in QC1. The constrained projections have the same
asymptotic fraction by Section 4, not necessarily the same finite formula.

In particular strong convergence of E projections to the identity occurs
IFF d_r/r^2->infinity. Necessity follows by passing to a subsequence with
bounded ratio and using E subset W_(r,d+1) together with QC10/QC11.
This is stronger than saying the algebraic span of a union is dense.

## 6. Trace-norm limit for the full xi operator

Use the parent's actual invariant source

    X(u)=xi(1/2+sqrt(u+1/4)), h=X'/X,
    A=rho(1-rho), Im rho>0, including all multiplicities,
    S(t)=sum_A exp(-At), Gamma_tau(s,t)=S(tau+s+t).

No positivity is assumed. The exact source H=h(0) and the critical strip give

    H=1+gamma_E/2-log(4pi)/2 in (0,1/2),
    x=Re A>=1/H-1>1, (Im A)^2<=x,
    sum_A 1/x<=H/(1-H)<1.

For reference, h(0)=sum Re(1/A), each term is at least 1/(x+1), and
1/x<=[1/(1-H)]Re(1/A). This proves the last two bounds from the product.
The expansion

    Gamma_tau=sum_A exp(-tau A)|exp(-A t)><exp(-bar A t)|

is trace-norm absolutely convergent, its total norm bounded by
(1/2)sum exp(-tau x)/x. Conjugate nodes make the sum self-adjoint.
The possible kernel singularity at (0,0) for tau=0 is interpreted by this
trace-class expansion. This is the source and metric of heat-hankel-pass5.

**ASTRA-QC-04 (critical blocks retain a thermal copy of the FULL operator).**
Let d_r/r^2->c in [0,infinity], let Pi_r=Pi_(r+2,d_r), and a=1/(2c). Then

    ||Pi_r Gamma_0 Pi_r-P_a Gamma_0 P_a||_1 ->0.             (QC12)

More generally the same assertion holds with ANY trace-class operator K
in place of Gamma_0. Proof: strong convergence of uniformly bounded
projections implies convergence in trace norm after multiplication on either
side by a finite-rank operator; approximate K in trace norm by finite rank
and use ||Pi_r||,||P_a||<=1. Expand the difference of the two compressions.

For finite a, the isometry U_a f(t)=1_[a,infinity)(t)f(t-a) gives exactly

    P_a Gamma_0 P_a=U_a Gamma_(2a) U_a^*.                   (QC13)

Thus c>0 finite retains Gamma_(1/c), not zero. At c=infinity it retains
Gamma_0; at c=0 it tends to zero for every trace-class K, independently of
any arithmetic positivity. This is not a claim of an explicit finite-r
error rate; the convergence established here is qualitative.

## 7. Exact safe-source matrices and full obstruction capture

Let m=r+2 and j,k run from m through m+d_r. Define the raw matrices

    Q_jk=sum_A A^2/(A+1)^(j+k),
    G_jk=int_0^infinity u_j(t)u_k(t)dt.

G is positive definite by linear independence. With a=j-1, b=k-1, its
closed rational formula is

    G_jk=(a+b-2)!/[2^(a+b-1)(a-1)!(b-1)!]
                         *[(a+b)-(a-b)^2]/(4ab).          (QC14)

Off-diagonal entries of G may be negative. This formula follows by
integrating the two terms of each u_j; it is not an imposed new metric.
If

    s_l=(-1)^(l-1) h^(l-1)(1)/(l-1)!=sum_A(A+1)^(-l),

then every exact arithmetic entry is

    Q_jk=s_(j+k-2)-2s_(j+k-1)+s_(j+k).                     (QC15)

The source h at u=1 is evaluated via s=(1+sqrt(5))/2>1 in

    h(u)=[1/s+1/(s-1)-log(pi)/2+digamma(s/2)/2
                        -sum_(n>=2)Lambda(n)n^(-s)]/(2s-1).

Each fixed jet has an absolutely convergent Euler expression, with its
analytic tail retained. No finite prime cutoff is substituted. The
orthogonal compression is represented by M_r=G^-1/2 Q G^-1/2.
Congruence suffices for a PSD test; eigenvalue magnitudes and limiting
negative traces MUST use G. Raw Euclidean eigenvalues are not interchangeable.

**ASTRA-QC-05.** Take the specific predetermined schedule d_r=r^2. Then

    Tr(M_r)_- -> Tr(Gamma_1)_-.                             (QC16)

Here T_- is the positive negative part of a self-adjoint T. The inequality
|Tr A_--Tr B_-|<=||A-B||_1 and QC12/QC13 prove QC16.

The parent's exact inertia theorem says n_-(Gamma_tau) is the number of
distinct nonreal conjugate invariant pairs, i.e. distinct off-line zeta
quartets, for every tau>=0. A brief account of the nontrivial converse:
remove any finite target pairs; the other distinct nodes satisfy the
right-half-plane Blaschke condition by sum 1/x<infinity. Its Blaschke
product is nonzero at the omitted targets. Residual Cauchy kernels permit
arbitrary interpolation there while annihilating the ENTIRE background.
The two target evaluations carry the Hermitian form
m[[0,exp(-tau bar A)],[exp(-tau A),0]], with one negative direction.
Every finite family of targets can be treated together. Conversely each
pair supplies at most one negative direction, while real A terms are
positive. Multiplicities are weights, not separate evaluation directions.
The detailed proof and its review boundary are imported from the exact
heat-hankel-pass5/PROOF.md cited in SOURCE_LOCK.json.

Therefore a hypothetical quartet gives a fixed negative eigenvalue in the
limit Gamma_1 and is detected by EVERY sufficiently large square-width
matrix M_r. This is not a target-adapted sequence and uses no spacing
hypothesis. If the number of quartets is finite q, n_-(M_r)=q eventually:
the lower bound follows from norm convergence and its q negative limiting
eigenvalues, and the upper bound from compression of Gamma_0. If q is
infinite, for each K all sufficiently large r have n_-(M_r)>=K.
No effective universal first detection r is asserted.

In particular the following ONE scheduled arithmetic statement is equivalent
via QC16 and the inherited inertia theorem to RH:

    liminf_(r->infinity) Tr(G^-1/2 Q G^-1/2)_-=0,
                    m=r+2, d=r^2.                        (QC17)

An all-rank lower bound Q>=-eta_r G with eta_r->0 would also suffice:
a fixed negative limiting vector would contradict it. Merely bounding
raw entries, spectral-frequency norms, or a different escape schedule does
not imply QC17. QC17 and that lower bound remain OPEN here.

## 8. The actual completion attempt and its failure

**ASTRA-QC-06 (regime audit and explicit countercontrol).** The proposed
completion was to combine the earlier exponentially small full residual
on growing signed spaces with their density, then force the negative trace
of Gamma_0 to vanish. QC1 proves precisely why this inference is invalid.
All earlier estimates requiring m>=constant*d, or the stronger m>=constant*
d*log(d+2), have d/(m-2)^2->0. Their compressions converge to zero for ANY
trace-class source. The identity/squared-width threshold cannot be reached
by extending those estimates without a new argument.

At the critical schedule d=(m-2)^2, the retained operator is Gamma_1. Applying
its exact source formula only reproduces the full sign problem:

    4pi<f,Gamma_1 f>
       =4pi R(0)^2+int_R exp(-(x^2+1/4))R(x^2+1/4)^2 Omega(x)dx
        -2sum Lambda(n)/sqrt(n) Fourier[g](log n).

The endpoint is generally present for a LIMITING f. The finite E tests all
have R(0)=0, but the integral functional is not L2-continuous; Section 4
proves its kernel condition disappears strongly. Dropping R(0)^2 from this
limiting formula would be a further mistake. Prime sums must not be passed
termwise through the limit without a separate dominating estimate.
The operator limit uses trace-class convergence, not such an interchange.

An exact synthetic source also tests the proposed use of THREE-SPARSE
positivity to complete the critical blocks. Take

    A in {10,20,30,1000+i,1000-i}.                           (QC18)

It has x>1, y^2<=x, sum 1/x=139/750<1, and h(0)<1/2. Its heat is
positive: for t>=log(2)/990 the term exp(-10t) dominates the absolute
size 2exp(-1000t); for smaller positive t, cos(t)>0. The other two real
terms are positive throughout. This is NOT actual xi and has no original
Euler product or the exact xi value of h(0).

Nevertheless it has the following stronger property:

    Q is positive definite on EVERY three-sparse signed span
    {u_(j1),u_(j2),u_(j3)} with 5<=j1<j2<j3.               (QC19)

Here is the full constant argument. Put B=31, Delta=10, T=1000, a_*=10.
The three real nodes give positive evaluation energy E. For P(z) with
three monomials and z_i=1/(a_i+1), generalized Vandermonde interpolation
factors into ordinary Lagrange factors times a Schur polynomial with
nonnegative coefficients. The explicit three-variable formula and its
proof are in signed-block-pass7/PROOF.md Section 2, at the pinned source.
Consequently, for |z|<=1/T<min z_i, each cardinal has modulus at most
(1+B/T)^2(B/Delta)^2, independently of both exponent gaps. Weighted
Cauchy-Schwarz then bounds the entire nonreal tail, at M=min j_i, by

    theta_M E,
    theta_M=6(1+B/T)^4(B/Delta)^4 T^3/a_*^2 (B/T)^(2M).

The exact rational check gives theta_5<1/100000; the ratio at successive
M is (31/1000)^2. Every nonzero three-monomial polynomial has nonzero real
evaluation vector. Thus Q>(1-1/100000)E>0. This proves QC19 for ALL gaps,
not just the bounded examples replayed by the checker.

For ANY m>=2, however, prescribe a degree-at-most-four real polynomial p by

    [A/(A+1)^m]p(1/(A+1))=0 at A=10,20,30,
                               i at A=1000+i,
                              -i at A=1000-i.

The five distinct nodes give a Vandermonde inverse, and conjugation makes
all coefficients rational real numbers. This five-generator test has
quadratic value exactly -2. At every subquadratic width the ENTIRE
compression still tends to zero by QC12. At square width it tends to
Gamma_1 with one negative eigenvalue. Thus the actual collection of
previous structural successes--positive heat, the source strip budget,
all-gap three-sparse positivity, and vanishing subquadratic compression--
does not logically establish the all-width sign. No negative value for
actual xi is asserted.

What is actually new within this continuation is the sharp three-regime
projection limit, its endpoint-preserving version, and the trace-norm
identification at square width. No new arithmetic lower bound in QC17 is
proved. No unconditional RH completion is deposited.

## 9. Review boundary and classical sources

The polynomial definitions, orthogonality, and differential equation are
classical; see NIST DLMF 18.3 and 18.8 (especially row 10 of Table 18.8.1).
The elementary resolvent and cutoff arguments are supplied above to avoid
hiding the moving-parameter limit in a citation. The spectral theorem,
Laplace uniqueness, and finite-rank density in trace class are standard
functional analysis. General Hankel sign/inertia theory is credited to
Yafaev, *Quasi-diagonalization of Hankel operators*, arXiv:1403.3941;
that reference is context, not an unproved positivity premise.

No Riemann-Hilbert steepest-descent theorem or random-matrix limit is used.
No external priority claim: the Laguerre large-parameter limit may have
antecedents in spectral/semiclassical approximation theory; specialist
comparison remains pending. The finite exact checker covers the named
algebraic constants and synthetic controls only. It does not machine-prove
strong convergence, trace-norm convergence, the inherited index theorem,
or the actual arithmetic sign.
