# HC26: quantitative capture of the removable tail, with the intrinsic defect retained

Status: PROPOSED COMPONENT THEOREMS, with paper proofs for independent review.
**The requested growing-horizon bound (10) and RH are NOT proved.**
Date: 2026-09-07. This is an author continuation, not an independent acceptance.

This paper targets the unpriced target-dependent projection rate in the previous
future-correction manuscripts. It proves a rate toward the ORIGINAL source
space, including when that space is proper. It does not replace that space by
its outer completion. The conclusion is substantially narrower than (10).

The source-stability manuscript was supplied as an immutable handoff and its
publication was subsequently confirmed in PR #814 at
`dc7babb830cb696810fb68bd74f6a33459f5f921`. PR #812 was separately read at
`2d683186cb3dd4f304159d8176215ceae8ac59fb`. SOURCE_LOCK.json records these
versions. No unpublished work is a prerequisite: the source and the needed
small-value estimate are reconstructed below.

## 0. Spaces, source, and the distinction to be proved

On the circle use normalized measure dm=dtheta/(2pi). Put

    ||f||_(s)^2 = sum_(n in Z) (1+|n|)^(2s) |f_hat(n)|^2,
    s=1/16.

This is a boundary fractional Sobolev norm, not the analytic Hardy H^s norm.
We write H^p exclusively for Hardy spaces. For an analytic f the negative
Fourier coefficients vanish. The equivalent difference seminorm is

    [f]_(s)^2 = integral integral |f(e^(i theta))-f(e^(i phi))|^2
                       / |e^(i theta)-e^(i phi)|^(1+2s) dm(theta)dm(phi).
                                                               (0.1)

Constants of equivalence depend only on s. To check this, use Parseval on
translations and then substitute u=n h in the h integral; the multiplier
integral is comparable to |n|^(2s) for n != 0. This also proves the boundedness
of Fourier projection P_+ and of the circular Hilbert transform in this norm.

The actual time-domain source, all-pass filter and disk image are

    d(t)=exp(-t/2)[floor(exp t)(1-t)+log(floor(exp t)!)], t>=0,
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2,
    r(z)=(z-1/2)/(z+1/2),  phi_j=R^j d,
    A(w)=D((1+w)/(2(1-w)))/(1-w)=w zeta(1/(1-w)).       (0.2)

All removable values are analytic values: D(1/2)=A(0)=1. Elementary source
integration gives ||d||_1<=6 and ||d||_2^2=||A||_H2^2<=5. The transform in
(0.2) is unitary from L2(0,infinity) onto disk H2. Let

    A=B O,  O(0)>0,
    M=closure{A p:p is a polynomial}=B H2,
    V_K=span(A,wA,...,w^K A),
    U_K(q)=dist(q,V_K)^2,  C(q)=dist(q,M)^2.           (0.3)

Inner-outer factorization and Hardy cyclicity are classical inputs. B is NOT
assumed constant. Every finite V_K is contained in the actual M.

MAIN COMPONENT THEOREM. There are absolute finite C,c>0 such that, for every
analytic q with q in H-infinity and ||q||_(s)<infinity, and every K>=2,

    0 <= U_K(q)-C(q)
      <= C (||q||_(s)+||q||_infinity)^2
                           exp[-c sqrt(log(K+2))].             (HC1)

The constants depend on fixed, unconditional bounds for the literal source,
not on RH, q, K, the horizon, or selected zero positions. They are not sharp,
and no numerically certified values of the final C,c are asserted here.
Their finiteness, dependence, and a construction of the rate are proved below.
No numerical campaign is an input to this theorem.

## 1. Boundary regularity of the actual source

We use the classical approximate functional equation ONLY to obtain

    |zeta(1/2+it)| <= C0 (1+|t|)^(1/4).               (1.1)

Its two sums of length O(sqrt(|t|)) have absolute sum O(|t|^(1/4)); on this
line the functional-equation factor has modulus one. The bounded-height
part is continuous. See DLMF 25.9.1. This is not Lindelof or RH.

A cruder bound suffices for a derivative. The Euler summation formula with
cutoff N=ceil(|t|+2) gives zeta(s)=O((1+|t|)^(3/4)) uniformly on the circle
of radius 1/4 around 1/2+it for |t|>=2. Indeed the Dirichlet sum, pole term,
and fractional-part integral are each bounded at Re s>=1/4. Cauchy's
formula gives

    |zeta'(1/2+it)| <= C1 (1+|t|)^(3/4).              (1.2)

On w=e^(i theta), 1/(1-w)=1/2+it with t=(1/2)cot(theta/2). If |theta|
is circular distance to 0, (1.1)-(1.2) imply, for 0<|theta|<=pi,

    |A(e^(i theta))| <= C |theta|^(-1/4),
    |d/dtheta A(e^(i theta))| <= C |theta|^(-11/4).    (1.3)

These are boundary estimates; zeros do not cause poles in either expression.
In particular A is in H^3. To control translations, remove an arc of length
O(eta) around 0 and its translate. The integral of |A|^2 on those arcs is
O(eta^(1/2)). On the complement the fundamental theorem of calculus and
(1.3) bound the squared translation difference by O(h^2 eta^(-9/2)).
For eta=|h|^(2/5), both terms are O(|h|^(1/5)). Thus

    ||A(.-h)-A||_2^2 <= C |h|^(1/5).                (1.4)

For sufficiently small h the chosen eta exceeds 2|h|. All remaining h are
absorbed in the constant. Equation (0.1), or its translation form, proves

    A in H^3,  ||A||_(s)<infinity, s=1/16,           (1.5)

since 2s=1/8<1/5. In particular |A| has the same fractional regularity,
by ||a|-|b||<=|a-b|.

## 2. A uniform small-value distribution, not a zero-free assertion

We reconstruct the source-stability handoff's small-value input, rather than
assuming that the Gram-floor statement alone implies it.

Let F(s)=(s-1)zeta(s), entire with the removable value at 1. For real t,

    max_(|z|<=4) |F(2+it+z)| <= (|t|+10)^6,
    |F(2+it)| >= |1+it|/2.                           (2.1)

For the first bound the fifth periodic-Bernoulli Euler--Maclaurin remainder
is

 zeta(s)=1/(s-1)+1/2+s/12-s(s+1)(s+2)/720
  -[s(s+1)(s+2)(s+3)(s+4)/120]
          integral_1^infinity B5({x})x^(-s-5)dx.

It is valid for Re s>-4, with B5(v)=v^5-(5/2)v^4+(5/3)v^3-v/6. On the disk
Re s>=-2 and |B5|<6. For U=|t|+10, multiplication by s-1 bounds the result
by 1+U/2+U^2/12+U^4/720+U^6/40 <= U^6. The second bound follows from
|1/zeta(2+it)|<=zeta(2)<2. These inputs are Euler-safe.

LOCAL LEMMA. If f is analytic near |z|<=4, f(0)=1, and |f|<=2^L there,
then the number of zeros in |z|<3 is <4L, including multiplicities. If
z0=-3/2 is at distance at least delta (0<delta<=1) from those zeros, then

    |f(z0)| >= 2^(-3L) (delta/8)^(4L).                (2.2)

Proof. Jensen gives the zero count since log(4/3)>log(2)/4. Select a
zero-free boundary radius 5/2<=R<3 and divide out the disk-R Blaschke
factors. The quotient g is zero-free and bounded by 2^L in the disk, and
|g(0)|>=1. Harnack applied to L log2-log|g| gives |g(z0)|>=2^(-3L), since
(R+3/2)/(R-3/2)<=4. Each divided factor is at least delta/8 at z0.
The zero count proves (2.2). Jensen also bounds the number in |z|<7/2 by
8L. No zero is presumed absent.

For an integer n>=1 put

    ell=ceil(log2(n+1)), L=23+6ell, a=16+4ell, delta=2^(-a).

Discard the arc |t|>4n. Its normalized circle measure is less than
1/(12n). Collect all zeros in disks |s-(2+ij)|<7/2 at integer centers
|j|<=4n+4, including repeated counting. By (2.1) and the local lemma there
are at most 72(n+1)L such zeros. Discard each interval |t-Im rho|<delta.
Since |dtheta/dt|<=4, their total normalized measure, multiplied by n,
is at most

    96 n(n+1)L 2^(-a) <=3/256 <1/64.                (2.3)

Here ell>=1, n(n+1)<=2^(2ell), and L<=2^(ell+4). For every retained t,
the local disk around 2+it has all relevant zeros at distance at least delta
from 1/2+it: moving its center to the nearest integer ordinate moves it by
at most 1/2. Applying (2.2), with the safe normalization in (2.1), gives

    |A(e^(i theta))| >= 2^[-1-L(4a+15)].             (2.4)

Consequently for EVERY n>=1 there is a measurable E_n with

    m(E_n)<1/n,
    |A|>=exp[-11000(1+log n)^2] off E_n.              (2.5)

For the last constant use ell<=3(1+log n) and
[1+L(4a+15)]log2=(1818+842ell+96ell^2)log2
 <=11000(1+log n)^2. No numerical zero list defines E_n or the constants.
The sets appear only in this measure proof; this is not an exclusion of zeros.

Put V(theta)=log^-|A(e^(i theta))| and

    J(v)=integral (V-v)_+ dm,  v>=0.

Since A(0)=1, Jensen and log^+ x<=x^2/5 imply integral V dm<=1. For
v>=44000 choose n=floor(exp(sqrt(v/11000)-1)). Then n>=2 and (2.5) yields

    m{V>v} <=2e exp[-sqrt(v/11000)].                  (2.6)

Integrate this distribution bound. Extending it to smaller v using J(v)<=1
proves the convenient all-v bound

    J(v) <=300000 exp[-sqrt(v)/(2sqrt(11000))].       (2.7)

The constants are intentionally loose. The logarithmic deficit is small
because the set of VERY small source values is small, not because |A| is
bounded below everywhere.

## 3. Clipped outer inversion, with the inner factor left in place

Factor A=B O with O(0)>0. Let O_v be the outer function, normalized at zero,
whose boundary modulus is

    |O_v|=max(|A|, exp(-v)),  v>=0,
    p_v=1/O_v,       ||p_v||_infinity<=exp(v).         (3.1)

The logarithm of this modulus is integrable. The Poisson formula gives the
last inequality on the entire disk. This construction inverts an OUTER
regularization, not A; it does not invert hypothetical off-line zeros.

The ratio F_v=O/O_v is Schur, and

    F_v(0)=exp[-J(v)],
    ||1-F_v||_2^2 <=2(1-exp(-J(v)))<=2J(v).           (3.2)

Indeed the logarithm of its boundary modulus is nonpositive, so its outer
Poisson integral has nonpositive real part. Its zero value is the exponential
of that logarithmic mean. Expand ||1-F_v||^2 and use ||F_v||_2<=1.

We also need a quantitative polynomial approximation to p_v. The real
function max(log x,-v) is exp(v)-Lipschitz on [0,infinity). Thus the boundary
logarithm l_v of |O_v| satisfies

    [l_v]_(s) <=exp(v)[A]_(s).

Its harmonic conjugate has the same Fourier multiplier bounds. On the
half-plane Re z>=-v the map exp(-z) is exp(v)-Lipschitz: integrate its
derivative along the straight line segment between two points. Applying
this to the boundary values of log O_v proves

    ||p_v||_(s) <=C_A exp(2v),                         (3.3)

where C_A is a finite constant depending only on (1.5) and s. Its L2 part is
bounded by exp(v). No Sobolev algebra property at s<1/2 is being assumed.

Let p_(v,N) be the analytic Fejer polynomial of p_v of degree N:

    p_(v,N)(w)=sum_(j=0)^N (1-j/(N+1)) p_hat_v(j) w^j.

Positivity of the Fejer kernel and Parseval give

    ||p_(v,N)||_infinity<=exp(v),
    ||p_v-p_(v,N)||_2<=C_A exp(2v)(N+1)^(-s).          (3.4)

The second inequality follows coefficientwise from
min(j/(N+1),1)<=(j/(N+1))^s. Interpolating its L2 bound with the L-infinity
bound 2exp(v) yields

    ||p_v-p_(v,N)||_6 <=C_A exp(4v/3)(N+1)^(-s/3).

Since O is in H^3 and ||O||_3=||A||_3, Holder now gives

    ||O(p_v-p_(v,N))||_2
       <=C_A exp(4v/3)(N+1)^(-s/3).                  (3.5)

Select v=(s/8)log(N+1). Equations (2.7), (3.2), and (3.5) imply

    ||1-O p_(v,N)||_2
       <=C_A exp[-a0 sqrt(log(N+1))],                (3.6)
    a0=(1/4)sqrt(s/(8*11000))>0.

The algebraic remainder in (3.5) is (N+1)^(-s/6), which is bounded by a
constant times the displayed slower rate; complete the square in
-a log(N+1)+a0 sqrt(log(N+1)). This accounts for ALL N>=1 after increasing
C_A. Thus no asymptotic relation is applied outside its range.

This gives quantitative approximation of 1 by the OUTER source. For the
actual source the resulting approximation is to B, not to 1. That distinction
is retained in the next two sections.

## 4. The actual inner factor has enough fractional regularity

We prove this without assuming B is constant and without a zero census.
A is analytic through the circle away from w=1. A singular inner measure
could only be supported at 1; finite-order ordinary boundary zeros do not
carry singular inner atoms. On r increasing to 1, A(r)=r*zeta(1/(1-r))
tends to 1. A positive singular mass at 1 would give a factor exp[-c(1+r)/(1-r)],
which cannot be offset by the outer H2 point bound ||O||_2/sqrt(1-r^2).
Thus B is pure Blaschke. Its zeros, with multiplicity, are

    a_rho=(rho-1)/rho,   Re rho>1/2,
    1-|a_rho|^2=(2Re rho-1)/|rho|^2.                 (4.1)

For a disk inner function I, alpha=2s in (0,1), the identity

 integral_0^1 [1-||I(r .)||_2^2](1-r)^(-1-alpha) dr
 =sum_(j>=1)|I_hat(j)|^2
               integral_0^1(1-r^(2j))(1-r)^(-1-alpha)dr

shows that the integral is comparable to sum j^alpha |I_hat(j)|^2. This
follows by splitting at 1-r=1/j, or by scaling, with constants depending only
on alpha. For a finite product of Blaschke factors, 1-product |b_a|^2 is at
most sum(1-|b_a|^2). Therefore its fractional energy is bounded by a constant
times the sum of the individual energies. A single factor has coefficients
of magnitudes |a| at zero and (1-|a|^2)|a|^(j-1) for j>=1, so

    sum_(j>=1) j^alpha |b_hat_a(j)|^2
       <=C_alpha (1-|a|^2)^(1-alpha).                (4.2)

The series estimate follows by comparison with an exponential integral; the
case |a|<=1/2 is bounded separately. Formula (2.1) and Jensen bound the number
of nontrivial zeros with ordinate in [j,j+1] by C log(|j|+11). For large |j|,
(4.1)-(4.2) are summable because

    sum_(j>=1) log(j+11)/(1+j)^(2(1-alpha)) <infinity
       when alpha<1/2.

For the finitely many low bands, 1-|a|^2<=1 and the same Jensen count suffices.
Finite Blaschke products converge in H2 to B, and lower semicontinuity of
the nonnegative weighted coefficient sum gives

    ||B||_(s) <=C_B<infinity,  s=1/16.               (4.3)

C_B is bounded using the convergent zero-count majorant, not unknown zero
coordinates. This argument includes arbitrary multiplicities and all
hypothetical right-of-line zeros.

For the target class of (HC1), set

    g=P_+(conjugate(B)q),     P_M q=B g.

Fourier projection is bounded in the Sobolev norm, and the difference form
(0.1) gives the elementary product estimate

    ||g||_(s)<=C (||q||_(s)+||q||_infinity ||B||_(s))
             <=C (||q||_(s)+||q||_infinity).          (4.4)

It uses |B|=1 a.e. and |q|<=||q||_infinity. We do not assume that P_+ maps
L-infinity to itself, nor that g is bounded.

## 5. HC26.1 -- a target-dependent rate to the TRUE intrinsic floor

Let g_L=sum_(j=0)^L g_hat(j)w^j. Then

    ||g-g_L||_2 <=(L+1)^(-s)||g||_(s),
    ||g_L||_infinity<=sqrt(L+1)||g||_2.               (5.1)

For N>=1 choose v as in Section 3 and

    L+1=floor(exp(a0 sqrt(log(N+1)))).

The right side is at least 1 and at least half the exponential. It is at
most N+1, since a0^2<log2. Hence L<=N, and the following polynomial has
degree at most 2N:

    p=g_L p_(v,N).

Equations (3.6) and (5.1) imply

 ||g-O p||_2
 <=||g-g_L||_2+||g_L||_infinity ||1-O p_(v,N)||_2
 <=C ||g||_(s) exp[-s a0 sqrt(log(N+1))].             (5.2)

The second term in this sum has the faster exponent a0/2; s<1/2. Since
multiplication by B is an isometry, (5.2) approximates B g by the ACTUAL
source A p=B O p. The error q-Bg is orthogonal to M, so exactly

    ||q-Ap||_2^2=C(q)+||g-O p||_2^2.                (5.3)

Take N=floor(K/2). For K>=2, (N+1)^3>=K+2. The best finite projection is
no worse than this candidate, and (4.4)-(5.3) prove (HC1), for example with

    c=2s a0/sqrt(3)>0

and a finite source-dependent absolute C. This c is conservative. The
constant C also includes the unconditional norms in Section 1; no final
numeric value of C is certified. The theorem is a bound on squared error.

The candidate in this proof uses inner/outer factors only to prove the rate.
It is NOT the implementation. The implementation solves the original finite
arithmetic Gram system, with target cross-correlations computed from q. No
unknown zero or inner factor is an input to that finite minimization.

## 6. Uniform application to the compact-inverse horizon seeds

For real T>=1 let m(x)=sum_(n<=x)mu(n)/n and set

    v_T(t)=exp(t/2)m(exp t)1_[0,T)(t),
    f_T=d*v_T,   h(t)=t exp(-t/2),
    q_T(u)=f_T(T+u)-h(T+u), u>=0.                    (6.1)

The classical finite divisor identity yields |m(x)|<=1. The distributional
jumps of v_T at log n<T have amplitudes mu(n)/sqrt(n), and its regular
derivative is v_T/2. Including the origin and terminal jumps therefore gives

    ||v_T||_1<=2 exp(T/2),
    Var(v_T)<=5 exp(T/2),
    Var(t v_T)<=C(1+T)exp(T/2).                     (6.2)

All these are bounds on genuine compact functions. No Dirac input is used.
Local Dirichlet inversion gives f_T=h before T. One direct verification,
with X=exp T, is

 P_T(s)=sum_(n<=X)mu(n)n^(-s)-X^(1-s)m(X),
 Lv_T(z)=P_T(z+1/2)/(z-1/2),
 Lf_T(z)=zeta(z+1/2)P_T(z+1/2)/(z+1/2)^2.            (6.3)

At an integer X the coefficient at X can be combined with the terminal term;
its activation does not change the initial interval. P_T(1)=0 exactly. The
identities first hold in an absolute half-plane; causality and the finite
coefficient identity prove the exact horizon, including endpoints where
appropriate for the continuous convolution output. Thus q_T is the shifted
WHOLE error, not a tail after discarding an initial mismatch.

Let q_T^disk be its unitary Cayley image. We claim

    ||q_T^disk||_infinity+||q_T^disk||_(s)
             <=C(1+T)exp(T/2), s=1/16.              (6.4)

Here is the full boundary estimate. For |y|>=2, (6.2) and integration by
parts for the zero-extended compact BV functions give

 |V_T(iy)|<=C exp(T/2)/|y|,
 |V_T'(iy)|<=C(1+T)exp(T/2)/|y|.

The ordinary derivative V_T' is the transform of -t v_T. By (1.1)-(1.2),

 |D(iy)|<=C |y|^(-3/4),
 |D'(iy)|<=C |y|^(-1/4).

Since Lq_T(z)=exp(Tz)[D(z)V_T(z)-(z+1/2)^(-2)], its boundary value is
O(exp(T/2)|y|^(-7/4)), and its y derivative is
O((1+T)exp(T/2)|y|^(-5/4)). Multiplication by the Cayley prefactor
1/(1-w) and differentiation with |dy/dtheta|=O(y^2) yield

 |q_T^disk(e^(i theta))|<=C exp(T/2)|theta|^(3/4),
 |(q_T^disk)'(e^(i theta))|<=C(1+T)exp(T/2)|theta|^(-7/4)

near theta=0. On the remaining compact arc, use (6.2), analyticity of D,
and the same elementary transform bounds. In particular q_T^disk is bounded.
The weaker pointwise bounds (1.3), with constant C(1+T)exp(T/2), hold as well,
so the translation proof of Section 1 proves (6.4). This establishes a
uniform target class; it is not assumed from a finite numerical example.

Every admissible f in the original source space that matches h before T
has f-f_T=S_T r0 for some r0 in L2. Its Hardy transform satisfies
exp(-T z) Lr0(z) in B H2. Since the exponential has no zeros, Lr0 has
every zero jet of B. Pure-Blaschke division therefore puts r0 in the
same source space. Conversely S_T preserves
that space. Hence all feasible continuations are exactly f_T+S_T M; no
backward-shift invariance of an arbitrary invariant subspace is assumed.

Let C_B(T)=dist(q_T^disk,M)^2 be the intrinsic minimum, and U_K(T) the actual
best squared error after degree-K future correction of f_T. Equations (HC1)
and (6.4) prove

    0<=U_K(T)-C_B(T)
      <=C(1+T)^2 exp(T) exp[-c sqrt(log(K+2))].       (HC2)

This is the first complete growing-horizon rate in this packet, but it is a
rate for the EXCESS ABOVE the intrinsic minimum. In particular a constant
C_*>0 exists, independent of T, for which the predetermined schedule

    K(T)=ceil(exp(C_*(T+1)^2))

gives U_K(T)-C_B(T)<=exp(-T). To see the constants, take
sqrt(C_*)>=[4+log^+ C]/c and use 2log(1+T)<=2T. These ranks are enormous;
no practical complexity claim or numerical instance of C_* is asserted.

The finite minimizer is computed from source Gram entries and target
cross-correlations. Quasipolynomial finite conditioning, source-tail bounds,
and ordinary box-input realization from the source-stability/future-realization
packets allow finite rational coefficients and a compact L2 realization to
any chosen output tolerance. Alternatively, compact inputs are dense in the
closed source dictionary by the causal approximate identity. Choosing the
output perturbation <=exp(-2T)/[4(1+||q_T||)] preserves the exact prefix and
changes the squared error by O(exp(-2T)). Thus a compact realization has
error at most C_B(T)+2exp(-T) for T>=1.
This statement permits large input norms. It does not reuse one fixed
feedback multiplier, and it does not assert a bound for C_B(T).

## 7. Why HC2 does not prove the requested statement (10)

Every feasible correction has exactly

    ||f-h||^2=C_B(T)+removable excess.                (7.1)

HC2 and compact realization control the second term at growing horizons.
The first term is NOT an artifact of a slow finite algorithm. If
rho=1/2+delta+i gamma is a zeta zero with delta>0, then every f in the
original source domain satisfies Lf(rho-1/2)=0. If f=h before T, evaluation
of its delayed error and Cauchy--Schwarz give

    C_B(T)>= [2delta/|rho|^4] exp(2delta T).          (7.2)

For h the transform is (z+1/2)^(-2), so its value is 1/rho^2 and cannot
cancel the hypothetical zero. This proof does not need simplicity.

The still-missing assertion in (10) is therefore

    log(1+C_B(T_j))/T_j -> 0 for some T_j -> infinity. (HC.OPEN)

In fact, in this pure-Blaschke source setting, RH would make B constant
and C_B(T)=0 for EVERY T. Conversely (7.2) makes HC.OPEN exclude every
right-of-line zero, and reflection yields RH. No bound on C_B(T) at an
unbounded sequence is proved here. HC2 quantitatively removes the finite
approximation issue but cannot remove the intrinsic factor B.

An explicit control shows why even a very fast all-horizon excess bound is
insufficient. For A_*(w)=1-2w the Gram of n successive shifts has diagonal
5 and adjacent entries -2. Its eigenvalues lie between 1 and 9. For the
constant target 1, exact continuants give

    U_n=3*4^n/(4^(n+1)-1),
    C_*=3/4,
    U_n-C_*=3/[4(4^(n+1)-1)].                        (7.3)

For targets q_j=2^j, use n=j^2+1. The excess tends to zero faster than any
fixed exponential in j, while the full minimum is (3/4)4^j. Thus good finite
conditioning and extremely rapid target-dependent capture of the reachable
part coexist with exponential intrinsic cost. This is a synthetic example,
not the literal factorial source and not a counterexample to RH.

The tempting final step would replace the factor B in (5.3) by 1. That is
exactly an assumption of source completeness. The clipped inverse is 1/O_v,
not 1/A. This paper leaves B in every relevant formula and does NOT make
that step. No independent reviewer is being asked to invent HC.OPEN or
accept it as a consequence of the component estimates.

## 8. Scientific outcome and execution boundary

The positive outcome is the source-specific target capture theorem HC1 and
its uniform horizon form HC2. These go beyond an eigenvalue/conditioning
bound: they estimate an actual target-dependent approximation residual.
Their complete arguments retain hypothetical off-line zeros and arbitrary
multiplicity. The arithmetic implementation uses finite Gram systems, not
an oracle for those zeros.

The attempted complete proof stops at the intrinsic term in (7.1).
Neither (10), HC.OPEN nor RH has been proved. A fixed-horizon error, or a
rate toward a nonzero limit, cannot be promoted to that conclusion.

The companion finite checker verifies declared rational identities, exponent
bookkeeping, finite synthetic projection formulas and integrity/rejection
contracts. It does not machine-prove fractional Sobolev estimates, infinite
factorization, classical zeta bounds, or HC1/HC2. There is no new actual-source
energy certificate, cofinal experiment, formal build or independent acceptance.
