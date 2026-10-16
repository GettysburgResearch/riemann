# Unconditional divisibility covariance for the coupled Gaussian source

Status: proposed mathematics with complete proofs; no unproved arithmetic
hypothesis is used. These are new source-specific estimates relative to the
inspected #952 packet, not a claim of priority for Euler products or Mellin
asymptotics. No new full-energy exponent, native higher moment, or RH theorem
is asserted. Proof and diagnostic authorship is shared; independent review
has not occurred.

## 1. Source and headline statements

Fix K=Q(omega), omega^2+omega+1=0, and a finite set S of prime ideals containing
the primes over 2 and 3. All remaining prime-ideal norms q are at least 7.
Different prime ideals of the same norm are always different indices. Let
m>=3 be an integer. Give each good prime two phases a_p,b_p of modulus at most
one. At a masked prime put BOTH phases equal to zero. Define multiplicative
ideal coefficients c_m by

    c_m(1)=1,
    c_m(p)=-(1-1/q)a_p,
    c_m(p^m)=-q^(m/2-1)b_p,
    c_m(p^j)=0 for j not in {0,1,m}.                       (1.1)

A row u can specify the phases; the usual prescription is
 a_p(u)=nu(p)chi_p(u), b_p(u)=eta_p[nu(p)chi_p(u)]^m.
This retains the original zero at every nonunit, even at exponent m=6.
The algebraic parameter m is NOT a constructed automorphic cover.

For real c put

    W_c(y)=y^(-c)exp(-(log y)^2/4)/(2sqrt(pi)),
    B_m(X)=sum_n c_m(n)W_c(Nn/X),
    beta=2c-1, kappa_c=exp(beta^2/2)/(2sqrt(2pi)).          (1.2)

The source uses c=5/6. Its critical energy has the exact kernel

    E_m(D)=integral_0^D |B_m(X)|^2 dX/X^2
          =sum_(n,l) c_m(n)conj(c_m(l)) K_D(Nn,Nl),
    K_D(v,z)=kappa_c/sqrt(vz) * exp(-(log(v/z))^2/8)
                 *Phi(log D-log(vz)/2-beta),              (1.3)

where Phi is the standard normal CDF. This kernel and absolute Fubini are
inherited from #952 and reconstructed below as needed. All sums here are over
nonzero integral IDEALS, not one representative of each rational norm.

The new conclusions are:

**Theorem A (an entire off-diagonal sector is paid).** Uniformly in m>=3,
phases and masks, for D>=1,

    sum_(n!=l; n|l or l|n) |c_m(n)c_m(l)| K_D(Nn,Nl)
                  <= C_(K,c)(1+log D).                    (1.4)

For any finite nonnegative physical row weights of total mass Z, the same
absolute sector is <= C_(K,c) Z(1+log D). No constant depends on the masks or
on m. The same statement holds for the native Mobius source. This is an
actual upper bound, not a condition on a future arithmetic estimate.

**Theorem B (signed prime-quotient asymptotic).** Suppose a_p=1 and |b_p|=1
at every p outside the fixed S. This includes the principal coupled source
with its arbitrary unit theta phases. Let P_m(D) be the subtotal of (1.3)
whose quotient in either direction is a PRIME IDEAL. Then, for any
0<epsilon<1/(2m),

    P_m(D)=-L_S log D+B_(m,S,c)-J_(m,S,c)D^(-1/m)
                  +O_(m,S,c,epsilon)(D^(-3/(2m)+epsilon)), (1.5)

where L_S>0 (with c held fixed) and J_(m,S,c)>0 are explicit absolutely convergent Euler/prime
expressions in Section 6. L_S is independent of m and all b_p; so are the
underlying leading square-mass density and the exact sign P_m(D)<0 for D>0.
The constant term B and secondary coefficient J may depend on m.

In particular the genuine sixth-power source satisfies

    P_6(D)=-L_S log D+B_(6,S,c)-J_(6,S,c)D^(-1/6)
                    +O_(S,c,epsilon)(D^(-1/4+epsilon)).   (1.6)

This evaluates an infinite signed unequal-ideal family, including its
nonzero secondary term. It is not a global off-diagonal estimate.

**Theorem C (nonzero secondary term in the actual square coefficients).**
Under the unit-phase assumptions of B, there are explicit delta_S>0 and
r_(m,S)<0 such that

    sum_n |c_m(n)|^2 W_c(Nn/X)
      =delta_S exp((1-c)^2)X
         +r_(m,S) exp((1-1/m-c)^2)X^(1-1/m)
         +O_(m,S,c,epsilon)(X^(1-3/(2m)+epsilon)).          (1.7)

The leading delta_S is independent of m and the unit phases. At m=6,c=5/6,
(1.7) is A_S X-B_S X^(5/6)+O(X^(3/4+epsilon)), with A_S,B_S>0. Thus the
5/6 term is proved and nonzero for this nonnegative coefficient observable;
it is not a claim about zeros or a Patterson asymptotic for another source.

## 2. Elementary counting and the kernel

The number I_K(t) of integral ideals of norm <=t is O_K(t). Indeed O_K is the
Eisenstein lattice; the norm-Euclidean property makes every ideal principal,
and its six generators of any given norm differ by units. Counting lattice
points in a disk gives the bound. Write I_K(t)<=A_K t for t>=1.

Each supported ideal is uniquely r d^m with r,d squarefree and coprime. Hence

    sum_(Nn<=t)|c_m(n)|^2
      <= A_K t sum_d (Nd)^(-2) <= A_K zeta_K(2)t.          (2.1)

For the first absolute coefficient moment the final exponent is -m/2-1,
so the same constant suffices. These estimates are uniform in m and masks.
They also prove absolute convergence of every finite-horizon Gaussian pair
sum in (1.3): partial summation bounds sum |c_m(n)|W_c(Nn/X) by C_(K,c)X,
and its squared integral with dX/X^2 on (0,D) is finite. Gaussian decay also
makes the source flat at X=0. No signed infinite Euler product is used here.

To check (1.3), put t=log X, a=log v, b=log z, mu=(a+b)/2. The exponent in
W_c(v/X)W_c(z/X)dX/X^2 is

    -(t-mu-beta)^2/2-mu+beta^2/2-(a-b)^2/8.

Gaussian integration through log D gives (1.3), with its displayed CDF shift.
This is a physical integral, not a contour moved through unknown zeta zeros.

A consequence of (2.1), for every additional prime exclusion R, is

    H_R(x):=sum_(h coprime R) |c_m(h)|^2/(Nh)
                         *Phi(log x-log Nh-beta)
           <= C_(K,c)(1+max(0,log x)), x>0.               (2.2)

Proof: t^(-1)Phi(log x-log t-beta) is nonnegative decreasing. Integrating
against (2.1), then setting v=log t, bounds the sum by a constant times
1+integral_(-infinity)^(log x-beta)Phi(v)dv. The latter integral equals
A Phi(A)+exp(-A^2/2)/sqrt(2pi), and is <=max(A,0)+1/sqrt(2pi).
Exclusions only decrease this positive bound. The distinction between ideal
diagonal and equal-rational-norm pairs remains essential.

## 3. Exact reduced-ratio classification and proof of Theorem A

First consider supported n,l with l|n. Put R=n/l and g=gcd(n,l)=l.
At a prime of R the positive valuation difference can ONLY be

       1, m-1, m.                                        (3.1)

These are distinct because m>=3. Difference 1 forces exponents (1,0),
difference m forces (m,0), and difference m-1 forces (m,1). Accordingly let
G_R be the product of the primes having valuation m-1 in R. Every such pair
has the UNIQUE form

    n=R G_R h, l=G_R h, (h,R)=1,                         (3.2)

with h supported in exponents 0,1,m. No further coprimality is inserted.
The factors c_m(n)conj(c_m(l)) equal gamma_R |c_m(h)|^2, where the factor
of gamma_R at a prime with difference j is

    j=1:     -(1-1/q)a_p,
    j=m:     -q^(m/2-1)b_p,
    j=m-1:   (1-1/q)q^(m/2-1)b_p conj(a_p).              (3.3)

This is valid with zero phases as well. If a pair has an inadmissible local
exponent then its original coefficient is zero, rather than repaired.

Put T_R=(NG_R)sqrt(NR). Its normalized local absolute factors are bounded by

    |gamma_R|/T_R:   q^(-1/2), q^(-1), q^(-3/2)
                    for j=1,m,m-1 respectively.         (3.4)

In particular |gamma_R|/T_R<=1. Substitute (3.2) into the inherited kernel.
The absolute contribution for this single R is at most

    kappa_c |gamma_R|/T_R * exp(-(log NR)^2/8)
                              H_R(D/T_R).                (3.5)

By (2.2) this is <=C_(K,c)(1+log D)exp(-(log NR)^2/8), since T_R>=1.
Finally

    sum_R exp(-(log NR)^2/8)<infinity,                    (3.6)

by I_K(t)=O(t) and the integrability of exp(v-v^2/8) on v>=0.
Sum (3.5) over all nonunit R, and include the other orientation by doubling.
This proves A with a constant independent of m. There is no restriction on
how large R or either original ideal can be; the entire Gaussian tail stays.

For native Mobius coefficients the allowed difference is only 1 and h is
squarefree. The same argument uses its square-coefficient count <=A_K t.
For row-dependent phases apply the uniform absolute bound before summing the
nonnegative fixed row weights. QED.

More generally, for coprime reduced cores A,B (neither need equal one), the
same classification applies to positive/negative differences, conjugating
(3.3) on the B side. With G the product of all primes with difference m-1,
the pair is n=AGh,l=BGh, (h,AB)=1. The exact kernel subtotal is

    kappa_c gamma_(A,B)/[(NG)sqrt(NA NB)]
        *exp(-(log(NA/NB))^2/8)
        *H_(AB)(D/[(NG)sqrt(NA NB)]).                     (3.7)

When both cores grow at comparable norms, the Gaussian factor in (3.7)
need not be small. Thus (3.6) does NOT sum all incomparable cores, and no
full-energy theorem follows by extending this last summation.

## 4. A two-pole square-coefficient Dirichlet series

Now impose |a_p|=|b_p|=1 outside the fixed S. In particular the positive
square-coefficient function d_m(n)=|c_m(n)|^2 is independent of all phases.
Set v_q=(1-1/q)^2 and, initially for Re(s)>1, define

    Q_q(s)=1+v_q q^(-s)+q^(m-2-ms),
    D_(m,S)(s)=sum_n d_m(n)(Nn)^(-s)=product_(p notin S)Q_q(s),
    zeta_S(s)=zeta_K(s)product_(p in S)(1-q^(-s)).         (4.1)

Let alpha=1-1/m and sigma_m=1-3/(2m). Then

    D_(m,S)(s)=zeta_S(s) zeta_S(ms-m+2) H_(m,S)(s),
    H_(m,S)(s)=product_(p notin S)
      (1-q^(-s))(1-q^(m-2-ms))Q_q(s).                    (4.2)

The product H converges normally on Re(s)>sigma_m. To prove this without
any assumed zero-free region, write A=q^(-s), B=q^(m-2-ms), v=v_q. Exactly,

    (1-A)(1-B)(1+vA+B)-1
       =(v-1)A-vA^2-vAB-B^2+vA^2B+AB^2.                 (4.3)

Its absolute value on Re(s)>=sigma_m+epsilon is bounded by a constant times

    q^(-1-sigma)+q^(-2sigma)
        +q^(m-2-(m+1)sigma)+q^(2m-4-2m sigma).            (4.4)

Every prime-sum exponent is strictly less than -1. At the boundary the
mixed decay exponent is 3/2-3/(2m)>=1, the B^2 exponent is -1, and
2sigma_m>=1. Comparison with convergent ideal series proves the claim.
For real s>sigma_m every local factor in H is positive and the product is
nonzero. Also Q_q(s) has no zeros anywhere in this half-plane: on the closed
boundary, |v_q A+B|<=2/sqrt(q)<=2/sqrt(7)<1. In particular |1/Q_q(s)|<5
uniformly in q>=7 and Re(s)>=sigma_m.

Here is all the continuation theory needed. The splitting law in K gives
zeta_K(s)=zeta(s)L(s,chi_-3) in Re(s)>1, retaining two factors at a split
prime and one norm-p^2 factor at an inert prime. For Re(s)>0,

    zeta(s)=s/(s-1)-s integral_1^infinity {x}x^(-s-1)dx,
    L(s,chi_-3)=s integral_1^infinity A_chi(x)x^(-s-1)dx,
    |A_chi(x)|<=1.                                      (4.5)

These elementary partial-summation formulae continue both functions and
bound them polynomially on each closed positive vertical strip, away from
the pole at one. They require no assertion about their zeros.
The residue kappa_S of zeta_S at one is positive. For 0<t<1,
zeta(t)<0 by the alternating-series formula, whose numerator is positive
and denominator 1-2^(1-t) is negative. Further,

    L(t,chi_-3)=sum_(j>=0)[(3j+1)^(-t)-(3j+2)^(-t)]>0.

Thus zeta_S(t)<0 for 0<t<1, since its removed Euler factors are positive.
This elementary sign fact is specific to the stated field; no corresponding
sign for every number field is assumed.

It follows that (4.2) has exactly two poles in Re(s)>sigma_m, at 1 and alpha,
with nonzero residues

    delta_S=kappa_S zeta_S(2)H_(m,S)(1)>0,
    r_(m,S)=(kappa_S/m)zeta_S(alpha)H_(m,S)(alpha)<0.      (4.6)

There are no other poles, because H is holomorphic and (4.5) has only the
pole at one. The leading density is independent of m:

    delta_S=kappa_S product_(p notin S)
          (1-q^(-1))[1+(1-q^(-1))^2/q+q^(-2)].           (4.7)

The local factor in this last product is 1-2/q^2+2/q^3-1/q^4, so it
converges to a positive value. This is not obtained by substituting s=1
into a divergent unnormalized Euler product.

Let b_(m,S) be the finite Laurent coefficient of D_(m,S) at 1. If one more
prime p is excluded, division by Q_q gives

    delta^p=delta_S/Q_q(1),
    b^p=b_(m,S)/Q_q(1)-delta_S Q_q'(1)/Q_q(1)^2,
    r^p=r_(m,S)/Q_q(alpha),
    Q_q'(1)=-(log q)[v_q/q+m/q^2].                        (4.8)

All vertical bounds for D_(m,S)/Q_q on the contours below are uniform in p,
by |1/Q_q|<5. This uniformity is what permits the infinite prime sum in B.

## 5. Gaussian asymptotics and the uniform one-prime removal

Mellin inversion of W_c gives

    sum_n d_m(n)W_c(Nn/X)
       =(1/(2pi i))integral_(a) exp((s-c)^2)D_(m,S)(s)X^s ds,
       a>1.                                             (5.1)

Shift to Re(s)=sigma_m+epsilon, where 0<epsilon<1/(2m).
The horizontal integrals tend to zero: (4.5) gives polynomial vertical
bounds, H is uniformly bounded, and the Gaussian has exp(-t^2) decay.
The two residues in (4.6) give exactly Theorem C. This does not shift an
inverse zeta function through its unknown zeros; (4.2) contains only zeta
functions as multiplicative factors.

For the critical harmonic CDF sum H_S(x) of (2.2), define

    h_(m,S,c)=b_(m,S)-beta delta_S,
    A_(m,S,c)=-m r_(m,S) exp(beta/m+1/(2m^2))>0.          (5.2)

The Gaussian CDF inversion formula is

    Phi(y)=(1/(2pi i))integral_(a)exp(sy+s^2/2) ds/s, a>0.

It follows by integrating the Gaussian inversion from -infinity to y;
positive a and exp(-t^2/2) justify Fubini. Therefore

    H_S(x)=(1/(2pi i))integral_(a)
             x^s exp(s^2/2-beta s) D_(m,S)(1+s) ds/s.     (5.3)

Shift (5.3) to Re(s)=-3/(2m)+epsilon. The double pole at zero contributes
delta_S log x+h_(m,S,c); the simple pole at -1/m contributes A_(m,S,c)x^(-1/m).
Consequently, for ALL x>0,

    H_S(x)=delta_S log x+h_(m,S,c)+A_(m,S,c)x^(-1/m)
                      +O_(m,S,c,epsilon)(x^(-3/(2m)+epsilon)). (5.4)

For small x this error is large; no small-x asymptotic is being asserted.
Stating the inequality for all x is useful when x=D/sqrt(q). In particular
(1.3)'s ideal diagonal equals kappa_c times (5.4) at x=D, improving its
previous O(log D) bound to a power-saving expansion.

For the additional exclusion p, (4.8) gives, uniformly in p and x>0,

    H_(S+p)(x)=delta_S/Q_q(1) log x
        +h_(m,S,c)/Q_q(1)-delta_S Q_q'(1)/Q_q(1)^2
        +A_(m,S,c)/Q_q(alpha) x^(-1/m)
        +O_(m,S,c,epsilon)(x^(-3/(2m)+epsilon)).          (5.5)

Uniformity here is only for adjoining ONE prime to fixed S. Arbitrary
moving-field or unrestricted moving-mask asymptotics are not asserted.

## 6. Proof of the signed infinite prime-quotient theorem

For m>=3, both h and p h can have nonzero coefficients only when p does not
divide h. With a_p=1,

    c_m(p h)conj(c_m(h))=-(1-1/q)|c_m(h)|^2, (h,p)=1.    (6.1)

This remains true for every unit b_p profile: those phases disappear in the
square at h, and the multiplying prime has exponent one. Put

    w_q=(1-1/q)q^(-1/2) exp(-(log q)^2/8).                (6.2)

Both orientations of the quotient-p pairs in the original energy give
exactly

    P_m(D)=-2 kappa_c sum_(p notin S) w_q H_(S+p)(D/sqrt(q)). (6.3)

All terms on the right are strictly negative; H contains its positive unit
term for every D>0. This establishes an exact sign of this complete selected
family, not a sign assigned to the full off-diagonal.

Substitute (5.5) into (6.3). The constants in Theorem B are

    L_S=2 kappa_c delta_S sum_p w_q/Q_q(1)>0,

    B_(m,S,c)=-2 kappa_c sum_p w_q *
       [(h_(m,S,c)-(delta_S/2)log q)/Q_q(1)
                              -delta_S Q_q'(1)/Q_q(1)^2],

    J_(m,S,c)=2 kappa_c A_(m,S,c)
                          sum_p w_q q^(1/(2m))/Q_q(alpha)>0. (6.4)

All sums converge absolutely. Their tails are bounded using I_K(t)=O(t)
and the log-Gaussian, which beats every fixed power of q. In particular the
sum of errors is bounded by

    C D^(-lambda) sum_p w_q q^(lambda/2)<infinity,
    lambda=3/(2m)-epsilon>0.                             (6.5)

Thus the use of ALL primes, including q>D^2, is justified by the uniform
all-x error in (5.5); no prime tail is silently cut off. Equations (6.3)--(6.5)
prove (1.5). At s=1, Q_q(1)=1+v_q/q+q^(-2) is independent of m; together
with (4.7), this proves the claimed leading-coefficient independence. QED.

If a_p is a nontrivial unit character value, (6.3) has Re(a_p) multiplying
each summand and no general negative sign follows. If a row is a nonunit at
p the original summand is zero. Theorem A still covers such rows uniformly;
Theorem B deliberately concerns the principal scalar source, not an
unjustified row average or an angular-twist corollary.

## 7. A forced positive remainder: four prime ideals already exceed the diagonal

Take specifically S=S0, the two prime ideals over 2 and 3, with no additional
exclusions, and keep the principal unit-phase assumptions. Let P_4(D) be
(6.3) restricted to the two split ideals over 7 and the two over 13. Define
R_4(D) to be ALL remaining off-diagonal pairs, so exactly

    E_m(D)=Delta_m(D)+P_4(D)+R_4(D).

Write f_q=w_q/Q_q(1). Then

    f_7=147 exp(-(log 7)^2/8)/(193 sqrt(7)),
    f_13=1014 exp(-(log 13)^2/8)/(1177 sqrt(13)).

The elementary strict bounds

    sqrt(7)<8/3, sqrt(13)<11/3,
    log 7<2, log 13<8/3,
    exp(-1/2)>3/5, exp(-8/9)>2/5

imply

    4(f_7+f_13)>
      4(1323/7720+6084/64735)
        =26522577/24987710>21/20.                         (7.1)

For a wholly rational verification of the exponential bounds, use the
positive Taylor polynomial through degree five to prove e^2>7 and e^(8/3)>13.
For x=1/2 and 8/9, the upper estimate

    e^x <= sum_(j=0)^3 x^j/j! + (x^4/24)/(1-x/5)

is valid because every subsequent term ratio is <=x/5<1. It gives respectively
2849/1728<5/3 and 196847/80919<5/2. No floating sign decision is needed.

By (5.4), the ideal diagonal is kappa_c delta_S log D+O(1); by the already
proved uniform one-prime formula, P_4(D)=-4 kappa_c delta_S(f_7+f_13)log D+O(1).
Nonnegativity of the ORIGINAL energy now yields the unconditional inequality

    R_4(D) >= (kappa_c delta_S/20)log D-C_(m,S,c), D>=1.   (7.2)

In particular R_4(D)>0 for all sufficiently large D and is at least a positive
multiple of log D. This is a proved sign and lower growth for another complete
native signed family, not a consequence conditional on RH. It shows why one
cannot assume every remaining cross term is favorable after isolating some
negative channels. R_4 includes other divisible pairs as well as incomparable
pairs; (7.2) does NOT locate its entire positive mass in the incomparable set.
For larger fixed S, including exclusions of 7 or 13, the general theorems stay
valid but this particular four-prime lower bound is not asserted.

## 8. Scope of the advance

Theorem A bounds infinitely many genuine off-diagonal pairs of the actual
source at the same logarithmic scale as its ideal diagonal. Theorem B
calculates a complete signed infinite subfamily, with positive explicit L,J
and a power-saving error. Theorem C identifies a nonzero secondary term in
the full square-coefficient observable. None assumes a critical energy
bound, a quasi-RH theorem, a theta-source estimate, or any zero-free region.

The unresolved covariance is concentrated among pairs with BOTH nonunit
coprime reduced cores. Distinct equal-norm ideals, including conjugate ideals,
are in that remaining set. Summing (3.7) over it using absolute values does
not give a logarithmic bound. The statements above also do not transfer
this particular off-diagonal subtotal through an arbitrary convolution:
the full-source comparisons from #952 retain their original scopes.

Classical methods are credited in SOURCES.md. The new claims are the displayed
source-specific quantitative estimates, not the general Mellin-residue
method, the splitting law, or multiplicative covariance as a concept.
