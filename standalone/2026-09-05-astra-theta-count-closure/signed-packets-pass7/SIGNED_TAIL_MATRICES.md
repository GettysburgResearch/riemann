# A signed prime-tail matrix theorem in unbounded dimension

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
The full xi quadratic form is NOT proved nonnegative in unbounded dimension.
Base: PR #790, f0584f7a49550540eaed005868422a83cb3e1011.
Local labels SP7-1 through SP7-3 belong only to this packet.
No external novelty or priority is claimed.

The predecessor controlled individual rational tests and a nonnegative cone.
Here all real coefficients in an entire finite-dimensional packet are allowed.
The packet dimension is unbounded and its required denominator order is
explicit. The result concerns the OMITTED PRIME TAIL, not the sign of the
exponentially smaller full form left after cancellation.

## 1. Definitions, source, and the precise metric

Put d0=1/4, c=5/4. Retain X(u)=xi(1/2+sqrt(u+1/4)) and h=X'/X.
Let A=rho(1-rho), one occurrence for each nontrivial zero with Im rho>0,
including multiplicity. Functional-equation reflection closes this list
under conjugation. For A=x+iy the critical strip gives x>0 and y^2<=x.
The standard invariant genus-zero product gives h(u)=sum_A 1/(u+A).

As in heat-hankel-pass5, the safe source constant

    H=h(0)=1+gamma_E/2-log(4pi)/2

satisfies 0<H<1/2. Indeed Re(1/A)>0, gamma_E<1 and log(4pi)>2.
Since Re(1/A)>=1/(x+1), each x>=1/H-1>1. Also

    sum_A 1/x <= H/(1-H) < 1.                         (S1)

This follows from 1/x=(1+y^2/x^2)Re(1/A) and the preceding lower bound
on x. These arguments use no verified zero prefix or PNT. The ordinary
analytic continuation, strip, and canonical product of xi are imported
classical facts, not a claimed independent proof of those facts here.

For integers m>=2, d>=0 and a real polynomial p of degree at most d, set

    z(A)=(A-d0)/(A+1),
    R_(m,p)(A)=A/(A+1)^m p(z(A)).                     (S2)

This is a Laplace transform of a real exponential polynomial. More
explicitly define

    u_m(t)=exp(-t)[t^(m-2)/(m-2)!-t^(m-1)/(m-1)!].

Since z(A)=1-c/(A+1), the transforms in (S2) describe exactly

    E_(m,d)=span{u_m,u_(m+1),...,u_(m+d)}.             (S3)

The basis change is triangular and invertible. The dimension is d+1 and
R_(m,p)(0)=0 for every p. Thus all endpoint terms vanish by an actual
condition on these tests, not by deletion.

For a nonzero p define

    g_(m,p)(x)=R_(m,p)(x^2+d0)^2,
    I_(m,p)=integral_R g_(m,p)(x)dx > 0,
    ghat(ell)=integral_R g(x)exp(-i ell x)dx,
    Omega(x)=Re digamma(1/4+ix/2)-log pi,
    Q_(m,p)=sum_A R_(m,p)(A)^2.

The last sum is real and absolutely convergent. It is the parent's
unshifted heat-Hankel quadratic form, not a sum of absolute squares at
complex zeros. In particular no positivity is inserted into its definition.
The unconditional Guinand--Weil formula, in the parent's convention, is

    4pi Q_(m,p)=integral_R g Omega
                   -2 sum_(n>=2) Lambda(n)n^(-1/2)ghat(log n). (S4)

Each fixed rational test has poles only at x=+/-i sqrt(c); contour shifting
to any height between 1/2 and sqrt(c) proves absolute convergence of the
prime series. All prime powers, with literal von Mangoldt weights, remain.

For an integer cutoff X>=2 let L be the smallest integer with X<=2^L.
Define Q_X by retaining the exact gamma integral in (S4) and just the
prime powers n<=X. Define the omitted tail

    T_X(m,p)=sum_(n>X) Lambda(n)n^(-1/2)ghat(log n).

Then exactly

    T_X(m,p)=2pi[Q_X(m,p)-Q_(m,p)].                    (S5)

The natural positive matrix used BELOW is the real-frequency Gram matrix

    G_ij=integral_R r_i(x^2+d0)r_j(x^2+d0)dx,
    r_j(A)=A/(A+1)^m z(A)^j,  0<=i,j<=d.             (S6)

For p(z)=sum a_j z^j, a^T G a=I_(m,p). This is NOT the time-domain L2
Gram matrix and is not silently substituted into the parent's operator
norm. All comparisons below name (S6) explicitly. Matrix sign itself is
invariant under an invertible change of real basis.

## 2. SP7-1: concentration uniform over ALL signed polynomials

For m>=d+4 and m>=4,

    integral_R x^2 g_(m,p)(x)dx / I_(m,p)
                      < 10(d+2)/m.                  (S7)

There is no coefficient-sign restriction and no coefficient norm on the
right side. In particular this remains true after arbitrarily strong
cancellation between the generators in (S3).

### Proof using a finite polynomial differential operator

Make the exact change t=x^2/(x^2+c), including both signs of x. Then

    I_(m,p)=c^(1/2-2m) integral_0^1
      t^(-1/2)(1-t)^beta [(t+d0)p(t)]^2 dt,
    beta=2m-7/2,
    x^2=c t/(1-t).                                    (S8)

Set q(t)=(t+d0)p(t), n=d+1, and w(t)=t^(-1/2)(1-t)^beta.
For every polynomial q of degree at most n,

    integral_0^1 t(1-t)q'(t)^2 w(t)dt
       <= K integral_0^1 q(t)^2 w(t)dt,
    K=n(n+beta+1/2).                                  (S9)

For clarity (S9) need not be imported as a mysterious Jacobi estimate.
The differential operator

    Jq=-t(1-t)q''-[1/2-(beta+3/2)t]q'

preserves the polynomials of degree at most n, is self-adjoint for w, and
has triangular diagonal j(j+beta+1/2), 0<=j<=n, in the monomial basis.
Its eigenvalues are those diagonal entries, and their maximum is K.
Integration by parts identifies its quadratic form with the left side
of (S9); all boundary terms vanish. This proves (S9). It is the classical
Jacobi differential-operator argument in the shifted convention [D1,D2].

Normalize integral q^2 w to one and write M=integral t/(1-t) q^2 w.
Integration of (t w q^2)' gives

    beta M=1/2+2 integral t q q' w
            <=1/2+2 sqrt(M K).

The inequality 2sqrt(MK)<=beta M/2+2K/beta therefore implies

    M<=1/beta+4K/beta^2.

Our hypotheses give beta>=n+1/2, so K<=2n beta and
M<=(8n+1)/beta. Also beta>=m for m>=4. Multiplying by c yields

    cM <= (5/4)(8d+9)/m <10(d+2)/m,

as asserted. The integrals with (1-t)^(-1) converge because beta>0. QED.

## 3. Consequence for the complete cutoff matrix

The elementary digamma estimates from prime-cutoff-pass6 are

    Omega(0)=-gamma_E-pi/2-3log2-log pi<-5,
    0<=Omega(x)-Omega(0)<17x^2.                         (S10)

They follow from the digamma partial fractions and
sum_(j>=0)(j+1/4)^(-3)<68; see [D3]. The bound gamma_E>1/2 used in the
first inequality also has the finite certificate in the predecessor.

Assume

    m >= 40(d+2)(17+L^2).                               (S11)

This implies the hypotheses of SP7-1 and makes the second moment in
(S7) less than 1/[4(17+L^2)]. Therefore

    integral g Omega < -(19/4) I,
    ghat(ell)/I = E cos(ell x) >7/8,   |ell|<=L.        (S12)

For the second statement use cos v>=1-v^2/2. Since log n<=log X<L
for n<=X, every retained prime term in (S4) is nonnegative. Consequently

    Q_X(m,p)<-I_(m,p)/pi <0                            (S13)

for EVERY nonzero real p of degree at most d. This is a strictly negative
definite matrix statement, not merely a collection of diagonal signs.
It provides a simultaneous rank/order/cutoff theorem. For d=0 it is not
as sharp as the predecessor's specialized linear-frequency estimate;
the new assertion is uniform over arbitrary coefficients and growing d.

## 4. SP7-2: the full form is uniformly exponentially smaller

For m>=max(4,d+4) and any p as above,

    |Q_(m,p)| <= eta_(m,d) I_(m,p),
    eta_(m,d)=2592 m(d+1)^4(8m)^(2d)(25/64)^m.          (S14)

In particular,

    D=min{integer j>=1: d+2<=2^j},
    m>=256(d+2)(D+1)  ==>  eta_(m,d)<exp(-m/4)<1/16.     (S15)

Neither statement asserts a sign for Q. Both use only (S1), the critical
strip, and elementary polynomial estimates, not a verified zero prefix.

### Proof of the coefficient-uniform evaluation estimate

For each invariant A, |z(A)|<1, since

    |A+1|^2-|A-1/4|^2=(5/2)Re A+15/16>0.

Let P_j^*(t) be shifted Legendre polynomials normalized by
integral_0^1 P_j^*(t)^2 dt=1/(2j+1). Their explicit coefficients give

    P_j^*(t)=sum_(r=0)^j (-1)^(j-r) binom(j,r)binom(j+r,r)t^r,
    |P_j^*(m z)| <= (j+1)(8m)^j,          |z|<=1.       (S16)

The coefficient bound uses binom(j,r)<=2^j and binom(j+r,r)<=4^j.
Expand any p in this orthogonal basis on [0,1/m]. Cauchy--Schwarz and
sum_(j=0)^d(2j+1)=(d+1)^2 give

    sup_(|z|<=1)|p(z)|^2
       <=m(d+1)^4(8m)^(2d) integral_0^(1/m) p(t)^2dt. (S17)

There is no replacement of arbitrary signed coefficients by positive ones.
On [0,1/m], m>=2, the factors in (S8) obey

    (t+1/4)^2>=1/16, t^(-1/2)>=sqrt m,
    (1-t)^beta >=(1-1/m)^(2m)>=exp(-4)>1/81.

The last inequality follows from log(1-a)>=-a/(1-a) and e<3.
Combining (S8) and (S17),

    sup_(|z|<=1)|p(z)|^2
      <=1296 c^(2m-1/2) sqrt(m)(d+1)^4(8m)^(2d) I.    (S18)

For the zero sum use |A|^2<=2x^2, |A+1|>=x+1, x>1, and (S1):

    sum_A |A|^2/|A+1|^(2m)
      <= sum_A (1/x) [2x^3/(x+1)^(2m)] <2/4^m.        (S19)

Here x^3/(x+1)^(2m) is nonincreasing for x>=1 and m>=3.
Multiplying (S18) and (S19), then using sqrt(m)<=m and sqrt(c)>1,
proves (S14).

To verify (S15) uniformly, put m0=256(d+2)(D+1). Since d+2<=2^D,
D+1<=2^D, and log2<1,

    log m0 < 8+2D,       log(8m0)<11+2D,
    log[2592 m0(d+1)^4(8m0)^(2d)]
                        <20+6D+22d+4dD < m0/4.

The final difference is the positive polynomial
60dD+42d+122D+108. For m>=m0 the difference between m/4 and the logarithm
of the prefactor is increasing: its derivative is
1/4-(2d+1)/m>0. Thus the prefactor is <exp(m/4) for every such m.
Since 25/64<1/2 and log2>1/2, eta_(m,d)<exp(-m/4)<1/16; here m0>=1024.
These are all-parameter inequalities, not an extrapolation from the checker.

## 5. SP7-3: a complete signed prime-tail matrix inequality

Let

    m >= (d+2) max{256(D+1), 40(17+L^2)},
    D=min{integer j>=1: d+2<=2^j},
    L=min{integer l>=1: X<=2^l}.                         (S20)

Then for EVERY nonzero real polynomial p of degree at most d,

    T_X(m,p)<-(3/2) I_(m,p)<0.                           (S21)

Equivalently, if T_X is the (d+1)-by-(d+1) real symmetric matrix obtained
by polarizing the prime tail and G is (S6),

    T_X  strictly precedes  -(3/2) G  in Loewner order.   (S22)

Proof. By (S5), (S13), and (S15),

    T_X(m,p) < 2pi[-I/pi+I/16]
                   =(-2+pi/8)I <-(3/2)I,

using pi<4. QED.

This theorem is unbounded in d and X. The required m is
O((d+2)[log(d+2)+log^2 X]), with the constants in (S20) specified. It retains
ALL cross terms for an arbitrary vector in E_(m,d); this is more than
entrywise positivity or a nonnegative generating cone.

It uses no PNT, finite zero verification, zero simplicity, or broad prime
scan. It also does NOT prove Q>=0. Indeed (S14) leaves its exponentially
small residual free to have either sign. The full form, the cutoff form,
and the omitted prime-tail form are different matrices. Their distinction
is the essential scope boundary, not an optional qualification.

The sibling proof ACTUAL_BLOCKS.md establishes positivity of the FULL form
on every E_(m,2), m>=5, by a separate finite-real-reservoir argument with
explicit inputs. It does not extend that conclusion to unbounded d.
