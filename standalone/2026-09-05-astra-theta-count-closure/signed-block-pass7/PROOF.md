# Signed blocks: full three-sparse positivity and growing-rank prime-tail cancellation

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required.
The unrestricted arithmetic form and RH remain UNPROVED.
Base: PR #790 at f0584f7a49550540eaed005868422a83cb3e1011.
Scope: the literal invariant xi source, real signed coefficients, every stated
integer order; complete tails and zero multiplicities are retained.
Local labels ASTRA-SB-01 through ASTRA-SB-05 are confined to this packet.
No external novelty claim. Standard Jacobi, Laguerre and interpolation tools
are credited in REVIEW.md. Finite tests are not proofs of the analytic theorems.

## 1. Source, conventions, and what is actually being extended

Keep X(u)=xi(1/2+sqrt(u+1/4)), h=X'/X, and A=rho(1-rho), where rho ranges
over every nontrivial zero with Im rho>0, including multiplicities. Conjugation
closes the A multiset. A nonreal pair of A's is one off-line zeta quartet.
The unchanged heat-Hankel source gives, with x=Re A and y=Im A,

    x>1, y^2<=x, sum_A 1/x <1.                              (1)

For clarity this requires no finite zero census: h(0)=H=1+gamma_E/2-log(4pi)/2
lies in (0,1/2), Re(1/A)>=1/(x+1), so x>=1/H-1 and
sum_A 1/x<=H/(1-H)<1. The invariant product and the critical strip justify
these identities before any positivity assumption on the operator.

For a real exponential polynomial f let R(A)=Laplace(f)(A), d=1/4, c=5/4,

    Q(f)=sum_A R(A)^2 = <f,Gamma_0 f>,
    g(w)=R(w^2+d)^2, I(f)=integral_R g(w)dw,
    ghat(l)=integral_R g(w)exp(-ilw)dw,
    Omega(w)=Re digamma(1/4+iw/2)-log pi.

Individual zero summands are not squared absolute values. The full sum is
real. Our rational transforms have real coefficients and poles only at -1.
They are Laplace transforms of real L2 exponential polynomials. We impose
R(0)=0, so the unconditional explicit formula is exactly

    4pi Q(f)=G(f)-2P_leX(f)-2P_gtX(f),                       (2)
    G(f)=integral_R g(w)Omega(w)dw,
    P_leX(f)=sum_(2<=n<=X) Lambda(n)n^(-1/2)ghat(log n),
    P_gtX(f)=sum_(n>X) Lambda(n)n^(-1/2)ghat(log n).

For unrestricted tests the omitted endpoint would be 4pi R(0)^2. It vanishes
here by construction, not by a sign estimate. Every prime power is retained.
For each finite test all sums converge absolutely: g is analytic on
|Im w|<sqrt(5/4), and a Fourier contour with height in (1/2,sqrt(5/4)) pays
the complete prime sum. No uniform-in-order absolute estimate is assumed.

The parent prime-cutoff-pass6 proves pair-entry positivity for its generators,
not positive definiteness on their signed span. Define unnormalized generators

    U_j(A)=A/(A+1)^j,
    u_j(t)=exp(-t)[t^(j-2)/(j-2)!-t^(j-1)/(j-1)!], j>=2.     (3)

They differ from the parent's f_j by the positive factor 4(5/4)^j.
Thus every statement about signed linear spans transfers exactly.

## 2. ASTRA-SB-01: actual positivity of EVERY three-sparse signed combination

For ANY integers 5<=j_1<j_2<j_3 the matrix

    K(j_1,j_2,j_3)_(r,s)=sum_A A^2/(A+1)^(j_r+j_s)          (4)

is positive definite. Thus Q is positive on EVERY nonzero real combination
of any three generators whose orders are at least five, with no restriction
on the gaps. In particular K_M(i,j)=sum_A A^2/(A+1)^(2M+i+j), i,j=0,1,2,
is positive definite for all M>=5. These are exact infinite-source matrices,
not prime-cutoff matrices or entrywise-positivity statements.

This theorem uses the imported V100 assertion: all zeros with 0<gamma<=100
are on the line. It also uses one critical-line zero in each of (14,15),
(21,22),(25,26). The new interval script proves the required endpoint sign
changes with an explicit eta-series remainder; no completeness or simplicity
is claimed by those six endpoint evaluations. V100 is a restriction of the
published Platt--Trudgian verification, not rerun here.

### Proof, including every signed cross term

Choose the three indicated invariant parameters a_1,a_2,a_3. They satisfy

    196<a_i<677, a_i+1<678,
    |a_i-a_j|>141 for i!=j.                                  (5)

Their actual disjoint intervals are (196.25,225.25), (441.25,484.25), and
(625.25,676.25). Put z_i=1/(a_i+1), M=j_1, v=j_2-M, w=j_3-M. For
P(z)=c_0+c_1 z^v+c_2 z^w, 0<v<w, let
R(A)=A(A+1)^(-M)P(1/(A+1)) and retain the positive reservoir

    E_P=sum_(i=1)^3 a_i^2 z_i^(2M) P(z_i)^2.                 (6)

The generalized Vandermonde below is invertible, so nonzero P gives E_P>0.
Multiplicity can only add positive low-zero contributions. All other zeros
below 100 are critical and hence contribute nonnegatively.

For gamma>100, (1) gives x>10000 and |z|=|1/(A+1)|<1/10000.
The three-monomial interpolation cardinal is the generalized Vandermonde
row-replacement determinant divided by the original determinant. Its exact
factorization is

    ell_i(z)=product_(j!=i)(z-z_j)/(z_i-z_j)
             * S(z,z_other1,z_other2)/S(z_i,z_other1,z_other2).

Here S is the Schur factor of det[1,z^v,z^w]. Only its NONNEGATIVE monomial
coefficients are needed, and they have this explicit elementary proof:

    S(x,y,z)=sum_(r=v-1)^(w-2) sum_(s=0)^(v-1)
       z^(v+w-3-r-s) (xy)^s sum_(k=0)^(r-s) x^(r-s-k)y^k.

All exponents are nonnegative. Summing the inner geometric series and then
the r and s series gives
 det[1,x^v,x^w;1,y^v,y^w;1,z^v,z^w]
   =(y-x)(z-x)(z-y)S(x,y,z).
For a direct check multiply S by (x-y)(z-x)(z-y); the two remaining products
are x^v(z^(w-v)-x^(w-v))(z^v-y^v) and its x/y-swapped counterpart.
Their difference is minus the displayed determinant. This also proves
S>0 at positive nodes and invertibility, with no external Schur-sign premise.

Since |z|<min_i z_i, coefficient positivity gives
 |S(z,z_other1,z_other2)|<=S(|z|,z_other1,z_other2)
                       <=S(z_i,z_other1,z_other2).
Consequently the cardinal bound is INDEPENDENT of both exponent gaps:

    |ell_i(z)| <= (11/10)^2 * 678^2/141^2.                   (7)

Indeed |z-z_j|<(11/10)z_j and
|z_i-z_j|=|a_i-a_j| z_i z_j. Weighted Cauchy--Schwarz, BEFORE any sum over
the unverified zeros, therefore gives

    |P(z)|^2 <= E_P * 3(11/10)^4 * 678^(2M+4)/(196^2 141^4).

For M>=2 the complete tail satisfies

    sum_(gamma>100) |A|^2/|A+1|^(2M)
        <=2*10000^(3-2M) sum_(gamma>100)1/x
        <2*10000^(3-2M).                                   (8)

Here |A|^2<=x^2+x<=2x^2 and x^(3-2M) is decreasing. Thus

    Q(f) >= (1-theta_M)E_P,
    theta_M=6(11/10)^4 * 678^4*10000^3/(196^2 141^4)
                                      * (678/10000)^(2M).    (9)

The exact rational inequality theta_5<1/3 and the ratio
 theta_(M+1)/theta_M=(678/10000)^2<1 prove

    Q(f) > (2/3)E_P >0, every M>=5.                        (10)

This handles ALL signs and ALL gaps of the three orders with one bound. No limit
interchange in M or an infinite list of determinant computations is used.
The bound is in the reservoir coordinates (6), not a uniform unit-L2 gap.

Every entry in (4) can alternatively be built from safe arithmetic derivatives:
put s_j=(-1)^(j-1)h^(j-1)(1)/(j-1)!=sum_A(A+1)^(-j). Then
K_(r,s)=s_(n-2)-2s_(n-1)+s_n, n=j_r+j_s. The result is therefore a theorem
about actual safe-source jets of unbounded order, though its proof uses V100.

### General finite-reservoir version

If d distinct critical parameters obey a_i>=a_*>0, a_i+1<=B<T, pairwise
gaps >=Delta, and every noncritical parameter has Re A>=T, the same proof
gives positivity on span{u_M,...,u_(M+d-1)} whenever M>=2 and

    theta_(M,d)=2d(1+B/T)^(2d-2)(B/Delta)^(2d-2)
                              *T^3/a_*^2*(B/T)^(2M) <1.    (11)

No claim is made that arbitrarily many critical reservoir nodes have been
verified. Formula (11) makes the rank cost explicit rather than hiding it.

## 3. A growing-dimensional family with arbitrary signed coefficients

Let D>=1, m>=1 be integers and define

    R_(m,q)(A)=[c/(A+1)]^m q((A-d)/(A+1)),
    q in R[t], deg q<=D, q(-1/4)=0.                         (12)

This is a D-dimensional linear space; signs of all coefficients are free.
Since (A-d)/(A+1)+1/4=cA/(A+1), it is exactly

    span{U_(m+1),...,U_(m+D)}.                              (13)

It is NOT the nonnegative cone of these generators. The denominator order
is at most m+D, so the inverse transforms are finite exponential polynomials.
For real w set t=w^2/(w^2+c), beta=2m-3/2. Then

    I= sqrt(c) int_0^1 t^(-1/2)(1-t)^beta q(t)^2 dt.         (14)

This I is a positive-definite quadratic form in q; it is not the original
L2 metric. Also I<=pi||f||_2^2 follows directly from
|R(a)|^2<=||f||_2^2/(2a), a=w^2+1/4.

## 4. Jacobi energy pays the entire signed-polynomial variance

**Lemma.** If m>=256D, the probability density g/I satisfies

    integral w^2 g(w)dw / I < 12D/m.                       (15)

Proof. On [0,1] use w_beta=t^(-1/2)(1-t)^beta and norm squared N_q.
The Jacobi differential operator, integrated by parts, has eigenvalues
j(j+beta+1/2). Its orthogonal polynomial expansion gives

    int t(1-t) q'(t)^2 w_beta dt
       <=D(D+beta+1/2)N_q =: L N_q.                        (16)

One can prove this without importing an explicit Jacobi normalization:
Gram--Schmidt polynomials diagonalize the symmetric degree-preserving
operator -w_beta^(-1)(t(1-t)w_beta d/dt)', whose leading term on t^j is the
stated eigenvalue. All boundary terms vanish since beta>0 and alpha=-1/2.

Write Z=int [t/(1-t)]q^2w_beta/N_q. Integrating
(t^(1/2)(1-t)^beta q^2)' and applying Cauchy--Schwarz gives

    beta Z <= 1/2+2sqrt(LZ)
            <= 1/2+(beta/2)Z+2L/beta,
    Z <=1/beta+4L/beta^2 <=(8D+1)/beta <9D/m.

Here beta>m and D+1/2<=beta, so L<=2D beta. Since w^2=ct/(1-t),
(15) follows from 9c=45/4<12. The inequality holds for every signed q.

The parent digamma bound is global:

    Omega(0)<-5, 0<=Omega(w)-Omega(0)<=17w^2.                (17)

For completeness, partial fractions give the difference as
(w^2/4)sum_(j>=0)[(j+1/4)((j+1/4)^2+w^2/4)]^(-1); its cubic reciprocal
sum is <68. Reflection/duplication give
Omega(0)=-gamma_E-pi/2-3log2-log pi<-5 by the elementary bounds in pass6.
Thus (15), m>=256D, and 204/256<1 imply

    G(f)<-4I.                                               (18)

Also cos z>=1-z^2/2 gives, uniformly over every real q in (12),

    ghat(l)/I >=1-6D l^2/m >=1/2
                      if l^2<=m/(12D).                     (19)

## 5. ASTRA-SB-02: exponentially small full form in the real-spectral norm

For EVERY D>=1, m>=100D and nonzero real q of degree <=D (the endpoint constraint
is not needed for this estimate),

    |Q(f)| < exp(-m/2) I(f).                                (20)

This is a two-sided estimate, NOT nonnegativity. It uses (1), not RH, PNT,
a verified zero prefix, or a sign claim about the heat kernel.

Proof. Put a=D/m<=1/100 and restrict the norm (14) to [0,a]. Then

    int_0^a q(t)^2 dt <=sqrt(a/c)(1-a)^(-beta) I.

For any complex z with |z|<=1, the Legendre reproducing kernel on [0,a]
gives

    |q(z)|^2 <=(D+1)^2/a * (7/a)^(2D) int_0^a q(t)^2 dt.

Indeed the normalized basis is sqrt((2j+1)/a)P_j(2t/a-1). The elementary
Legendre recurrence proves |P_j(z)|<=(2|z|+1)^j by induction; for |t|<=1,
2|2t/a-1|+1<=7/a. Summing 2j+1 gives (D+1)^2. Therefore

    sup_(|z|<=1)|q(z)|^2/I
       <=(D+1)^2 sqrt(m/D) (7m/D)^(2D) exp(3D).              (21)

We used c>1 and (1-a)^(-beta)<=exp(2D/(1-a))<exp(3D).
For each source parameter, |(A-d)/(A+1)|<1, and (1) yields

    sum_A [c/|A+1|]^(2m)
       <=(5/8)^(2m)sum_A 1/x <(5/8)^(2m).                 (22)

Here x[c/(x+1)]^(2m) is decreasing on x>=1 for m>=1. Insert (21) into
the absolute zero sum, retaining all multiplicities.

The resulting coefficient is <=exp(-m/2). To check the constants for ALL
m,D, write r=m/D>=100. Use D+1<=2^D, log2<3/4, log7<2,
log(8/5)>2/5, and log r<=r/20 on r>=100. Its logarithm is at most

    D[(5/2)log r+17/2-(4/5)r]
       <= D[(1/8)r+(17/200)r-(4/5)r]
       =-(59/100)m < -m/2.

The elementary logarithm bounds follow from 8/3<e<3, log100<5, and
(8/5)^5>9; log r-r/20 is decreasing after 100. This proves (20).

## 6. ASTRA-SB-03: full signed prime-tail matrix cancellation

For every D>=1, m>=256D and cutoff

    2<=X<=exp(sqrt(m/(12D))),                               (23)

the ENTIRE quadratic forms on every nonzero test in the D-dimensional space (12) satisfy

    Q_X(f):=[G(f)-2P_leX(f)]/(4pi) < -I(f)/pi,
    P_gtX(f) < -I(f),                 f!=0,                 (24)
    |P_gtX(f)-G(f)/2+P_leX(f)|
                            <2pi exp(-m/2) I(f).           (25)

There are no coefficient sign restrictions. Equivalently the tail matrix
is strictly negative definite relative to the positive spectral Gram I,
and (25) is an operator-norm approximation in that inherited spectral metric.
It is not a claim about a single tested vector or only the diagonal entries.

Proof. Equations (18)--(19) make G<-4I and every retained prime term
nonnegative. The exact identity (2) gives

    P_gtX=G/2-P_leX-2pi Q.

Now apply (20). Since m>=256 and pi<4, 2pi exp(-m/2)<1; this proves
(24)--(25). Every infinite sum was already absolutely convergent per test.
A fixed integer bound L>=log X gives the simpler sufficient condition
m>=256D(1+L^2). The rank D can tend to infinity, with m and X satisfying
(23). These estimates do not evaluate a large prime list.

The bound is stronger than a generator-cone tail estimate, but the remainder
-2pi Q in (25) has an UNKNOWN sign at arbitrary D. Completing its leading
cancellation to exponentially small error is not the same as proving that sign.

## 7. ASTRA-SB-04: these growing blocks are not a dense approximation sequence

The spaces with m>=256D move to large t in the ORIGINAL L2 metric. Every
f in (12) is of the form t^(m-1)exp(-t)P_D(t), deg P_D<=D. For every T>0,

    int_0^T |f(t)|^2dt <=(3T/m)||f||_2^2.                  (26)

Proof. Set x=2t and alpha=2m-2. The Laguerre energy inequality for
polynomials p of degree <=D is

    int x p'(x)^2 x^alpha exp(-x)dx
                 <=D int p(x)^2 x^alpha exp(-x)dx.

As for (16), integration by parts and Gram--Schmidt for the symmetric
Laguerre operator prove the inequality. If Z is the expectation of 1/x
in the normalized density p^2 x^alpha exp(-x), integration of its derivative
and Cauchy--Schwarz give

    alpha Z <=1+2sqrt(DZ), Z<=2/alpha+4D/alpha^2.

Thus E(1/t)<=4/alpha+8D/alpha^2<3/m when m>=256D. Multiplication by T
bounds the mass on [0,T] and proves (26).

No bounded-norm sequence selected from these blocks with m tending to
infinity can converge strongly to a fixed nonzero L2 test. Therefore even
a sign theorem limited to these growing blocks would not, by density alone,
prove positivity of Gamma_0. The linear span of their union is a different
object: it allows widely separated orders and is not covered by (23).
Likewise positivity of all three-sparse combinations in Section 2 does not
prove positivity of combinations with four or more nonzero coefficients.

## 8. ASTRA-SB-05: the exponential remainder really can have a negative sign

This is a SYNTHETIC control, not the actual Euler source. Take invariant
parameters a=100, b=200+10i, bar b. They satisfy x>1, y^2<=x and
sum 1/x=1/50<1, and their heat sum is strictly positive for every t>0:
for t<=1/100 its cosine is positive, and for t>=1/100 the first term
dominates the other two because exp(100t)>=e>2.

Nevertheless for EVERY integer M>=2 there is a real linear combination
of U_M,U_(M+1),U_(M+2) with quadratic value -2. Explicitly set

    W=i(b+1)^(M+2)/[b(b-a)],
    u=Im W/10, v=Re W-200u,
    R(A)=A(A-a)(uA+v)/(A+1)^(M+2).                          (27)

All u,v are rational. R(a)=0, R(b)=i, R(bar b)=-i, so sum R(A)^2=-2.
The numerator after its factor A has degree two, giving the asserted span.
Choosing M=769 puts the example inside m=M-1=768, D=3 of (20). This is
consistent with (20): its spectral norm I is enormous. It proves that (1),
positive heat and the exponential residual bound do not determine its sign.
The actual-source triple theorem uses the additional real reservoir absent
from this model. No conflict or actual off-line xi zero is asserted.

## 9. Exact end-to-end status

Completed here: full-source positivity on EVERY three-sparse signed
combination of orders >=5, independently of their gaps; a finite-reservoir signed-block theorem; an arbitrary-rank
signed prime-tail inequality and exponentially accurate compensation formula;
and a quantitative description of why these moving blocks are not cofinal.

Not completed: positivity of the full rational hierarchy for arbitrary rank
and arbitrary widely separated signed coefficients. The rank-D theorem is
about the TAIL and a two-sided residual bound, not positivity of the residual.
The three-sparse theorem cannot be promoted to four-sparse or all-rank positivity
by overlap or entrywise positivity.
A proof of the unbounded Schur-complement signs must use further arithmetic
information; none is assumed in the theorems above. RH remains unproved.
