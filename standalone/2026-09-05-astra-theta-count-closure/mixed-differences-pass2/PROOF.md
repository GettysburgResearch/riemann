# Mixed differences: proved infinite regions and the exact exponential obstruction

Status: PROPOSED PROVED THEOREMS; independent mathematical review required.
RH and the unrestricted mixed inequality remain UNPROVED.
Scope: actual invariant xi; stated uniform index regions; exact spectral-rate
identity; one explicitly imported zero-count estimate.
Parent: PR #790 @ bc3c35d8f434949748a2185783bf831d3afd9126.
Dependencies: the parent's HEAT_BERNSTEIN.md and THETA_COUNT.md; Trudgian's
zero-count corollary, in the weakened form specified in Section 5.
Computation: bounded rational/complex-rational identities only. The proofs
below, not the checker, establish the infinite quantifiers.
Smallest remaining gap: a source-side subexponential bound for the Laguerre
traces in Section 10, equivalently the unrestricted mixed inequality.
No external priority or novelty claim is made.

## 1. Normalization and three exact forms of the target

Keep the parent normalization without a factor-two change:

    X(u)=xi(1/2+sqrt(u+1/4)),   X(0)=1/2,   h=X'/X,
    A_rho=rho(1-rho),          rho=beta+i gamma, gamma>0,
    S(t)=sum_(gamma>0) exp(-A_rho t).

Zeros are counted with multiplicity. The upper-half-plane list gives one
invariant parameter per functional-equation orbit; an off-line quartet
gives TWO conjugate A's. Write A=x+i y. The critical strip implies

    x=gamma^2+beta(1-beta)>=gamma^2,
    |y|=|gamma(1-2beta)|<=gamma,
    |A|<=gamma^2+1/2.                                         (1.1)

For the last inequality, put q=beta(1-beta) in [0,1/4]. Then

    |A|^2=gamma^4+(1-2q)gamma^2+q^2
          <=gamma^4+gamma^2+1/4=(gamma^2+1/2)^2.

The parent proves N(T)<=T^2 for T>=100, N(T)=O(T log(T+2)), and

    h(u)=sum_A 1/(u+A)=integral_0^infinity exp(-ut) S(t)dt.

We import its V100 (all zeros through height 100 are on the line) and its
Z14/15 sign certificate (at least one line zero has 14<gamma_0<15).
For the selected real invariant parameter A_0 this gives

    196<A_0<226.                                               (1.2)

It is a SELECTED zero, not an assertion that there are no earlier zeros.

For v>0 set k_A=v/(v+A). The logarithmic factorial coordinates satisfy

    p_n^*(v)=sum_A k_A^n,  n>=1,
    H_(a,b)(v)=sum_(j=0)^b (-1)^j binom(b,j)p_(a+j+1)^*(v).

Absolute convergence follows from sum |A|^(-1)<infinity. Therefore

    H_(a,b)(v)=sum_A k_A^(a+1)(1-k_A)^b
              =sum_A v^(a+1) A^b/(v+A)^(a+b+1).                (1.3)

All these sums are real by conjugation. Two further exact forms are

    H_(a,b)(v)=v^(a+1)/(a+b)! integral_0^infinity
                     t^(a+b) exp(-vt) (-1)^b S^(b)(t)dt,       (1.4)

    H_(a,b)(v)=(-1)^a v^(a+1)/(a+b)!
                    [D_u^(a+b)(u^b h(u))]_(u=v).              (1.5)

For (1.5), divide u^b by u+A. The polynomial part has degree b-1
and is killed, leaving (-A)^b/(u+A); the case b=0 is direct.
Equation (1.4) follows by the gamma integral. Near t=0 the absolute
integrand is O(t^(a-1/2) log(2/t)), so it is integrable for every a>=0.
No exchange here presumes RH or a sign of S^(b).

## 2. Weighted Gaussian tails, uniformly in derivative order

**Lemma MD-01a.** Let k>=0 be an integer, B>=100, t>0, and
`t B^2>=2(k+1)`. Then

    sum_(gamma>B) |A|^k exp(-t Re A)
      <=2 exp(k/(2B^2)) B^(2k+2) exp(-tB^2).                   (2.1)

Proof. By (1.1), |A|^k<=gamma^(2k) exp(k/(2B^2)). The function
f(x)=x^(2k)exp(-tx^2) is decreasing for x>=B. Stieltjes integration by
parts and N(x)<=x^2 give

    sum_(gamma>B) f(gamma)
       <=integral_B^infinity [-f'(x)]N(x)dx
       <=2t integral_B^infinity x^(2k+3)exp(-tx^2)dx
       =t^(-k-1) Gamma(k+2,tB^2).

The discarded lower endpoint and the -2k term are both nonpositive.
For z>=2(k+1), the elementary integer incomplete-gamma identity gives

    Gamma(k+2,z)/(z^(k+1)exp(-z))
      =sum_(j=0)^(k+1) (k+1)_falling_j/z^j
      <=sum_(j>=0)((k+1)/z)^j<=2.

This proves (2.1), also at a zero ordinate B under the strict-tail
convention. All infinite endpoints vanish by Gaussian decay. QED.

## 3. All-time heat derivatives through order 22

For 0<=k<=22 define the explicit RATIONAL constant

    C_k=20000 (2500/49)^k (60/163)^97.                         (3.1)

The elementary exponential series gives e>163/60. Exact rational
arithmetic establishes

    C_k<=C_22<3/5                (0<=k<=22),
    C_k<=C_20<1/4096             (0<=k<=20).                   (3.2)

**Theorem ASTRA-MD-01.** For every t>0 and every integer 0<=k<=22,

    (-1)^k S^(k)(t)>(1-C_k)196^k exp(-226t)>0.                 (3.3)

Consequently, for EVERY a>=0 and v>0 and 0<=b<=22,

    H_(a,b)(v)>(1-C_b)196^b v^(a+1)/(v+226)^(a+b+1)>0.         (3.4)

Proof. First let 0<t<=1/100 and B=1/t. For every unverified zero with
100<gamma<=B, the phase of A^k exp(-At) is

    k arg A-t Im A.

The two terms have the same sign before subtraction. Hence its absolute
value is at most max(k/gamma,t gamma)<=1. Its cosine is positive. All
zeros below 100 have real A and contribute positively by V100. Retain the
selected term A_0^k exp(-A_0t)>196^k exp(-226t), and bound only gamma>B
in absolute value. The hypothesis of Lemma MD-01a holds since
`t B^2=B>=100>2(k+1)`.

Writing w=1/t, the relative error is at most

    E_k(w)=2 exp(k/(2w^2)) w^(2k+2)196^(-k)exp(-w+226/w).

For w>=100 its logarithmic derivative is

    (2k+2)/w-1-226/w^2-k/w^3<0.

Thus E_k(w)<=E_k(100). For t>=1/100 use B=100 and V100 directly;
Lemma MD-01a gives the same maximum relative error, now at t=1/100.
Finally

    E_k(100)=20000(2500/49)^k exp(-100+226/100+k/20000)
              <20000(2500/49)^k exp(-97)<C_k.

This proves (3.3). Insert it in (1.4) and integrate t^(a+b) to prove
(3.4). The original b=0 theorem in the parent is retained unchanged.
No finite sampling of t, a, or v is used. QED.

**Probability corollary.** For every r>0 and 0<c<1,
`[X(cu)/X(u)]^r` is completely monotone on u>=0. Indeed S is decreasing
by k=1, and

    log X(u)-log X(cu)
       =integral_0^infinity (1-exp(-ut))[S(t)-S(t/c)]dt/t

has a positive Levy density. This is a self-decomposability consequence,
not a Stieltjes or real-zero theorem.

## 4. A phase rectangle and an unbounded small-ratio cone

For A=x+i y with y>=0 put alpha=arg A and beta_v=arg(A+v). Then

    0<=beta_v<=alpha<=1/gamma,
    0<=alpha-beta_v
       =integral_0^v y/((x+s)^2+y^2)ds
       <=v/(gamma(gamma^2+v)).                                (4.1)

Conjugation handles y<0. The phase in (1.3), writing n=a+1, is

    b(alpha-beta_v)-n beta_v.

The absolute value is bounded by the MAXIMUM, not the sum, of the two
nonnegative quantities in (4.1).

**Lemma MD-02a (phase rectangle).** If

    a+1<=100,        b v<=100(10000+v),                        (4.2)

then H_(a,b)(v)>0. In fact every unverified zero term has positive real
part, and the verified terms are positive. The selected zero alone gives

    H_(a,b)(v)>[v/(v+226)]^(a+1)[196/(v+196)]^b.

This is a uniform elementary region, not a zero search.

**Theorem ASTRA-MD-02 (unbounded cone at one scale).** At v=1,

    a>=2, 0<=b<=100a
       ==> H_(a,b)(1)>(1/2)227^(-a-1)(196/197)^b>0.            (4.3)

Proof. Since Re A>0, |A/(1+A)|<1. For a>=1,

    sum_(gamma>100) |1/(1+A)|^(a+1)
       <=sum_(gamma>100) gamma^(-2a-2)
       <=((a+1)/a)100^(-2a),                                 (4.4)

by Stieltjes integration and N(x)<=x^2. The verified prefix is positive;
its selected term is greater than 227^(-a-1)(196/197)^b. For b<=100a
the ratio of (4.4) to that lower bound is at most

    (3/2)*227*r^a,
    r=(227/10000)(197/196)^100<1.

The exact rational inequality `(3/2)*227*r^2<1/2` proves (4.3).
Both a and b can tend to infinity in this region. QED.

## 5. A minimal imported reservoir of high zeros

We now add ONE independent classical input; it is not used in Sections
1--4 or 7--10. Trudgian, arXiv:1208.5846v2, Corollary 1 (p.2), together
with its displayed Riemann--von Mangoldt formula (p.3), implies the weaker
bound, for T>=100,

    |N(T)-F(T)|<=.112 log T+.278 log log T+2.512,
    F(T)=(T/(2pi)) log(T/(2pi e))+7/8.                         (5.1)

The v2 corollary prints the stronger constants .111, .275, 2.450 and
+.2/T0. The displayed weaker version also accommodates the published
2014 statement's .112, .278, 2.510. We set T0=100. Only (5.1) is used.
The two relevant PDF pages were inspected. The theorem is IMPORTED;
this pass does not independently reprove Trudgian's argument.
Zero-height endpoint conventions extend the nonexceptional-height bound
by one-sided limits. In particular the next conclusion holds for a closed
interval regardless of whether N uses < or <=.

**Lemma MD-03a.** For every real T>=100, there is a nontrivial zero with
T<=gamma<=2T. It need NOT lie on the critical line.

Proof. The error in (5.1) is less than log T. To check this for all T>=100,
the difference `.888 log T-.278 log log T-2.512` is increasing there;
at T=100 it is positive using log100>4 and loglog100<2. The main increment is

    F(2T)-F(T)=(T/(2pi)) log(2T/(pi e))>T/4.

Here pi<4, e<3, and 2T/(pi e)>T/6>=100/6>e^2. The sum of the two errors
is smaller than log T+log(2T)<=sqrt T+sqrt(2T)<(5/2)sqrt T<=T/4.
Therefore the zero-count increment is positive. Passing to one-sided
limits handles endpoints without an assumption of simplicity. QED.

## 6. The opposite unbounded direction: whole columns and a cubic wedge

All theorems in this section are at the ONE FIXED scale v=1.
Write n=a+1 and, for an integer b>10^6, T=b^(1/3)>100.
If n<=T, every zero with gamma>=T has positive real part in (1.3), since
(4.1) bounds its phase by max(n/T,b/T^3)<=1. Zeros with gamma<=100
also contribute positively by V100. Only 100<gamma<T can be negative.

For gamma>=100, a useful modulus bound is

    log(|1+A|/|A|)
       =(1/2)log(1+(2 Re A+1)/|A|^2)
       >=(Re A)/|1+A|^2
       >=gamma^2/(gamma^2+3/2)^2
       >(99/100)/gamma^2.                                    (6.1)

Use log(1+w)>=w/(1+w), and (1.1). The last comparison follows from
`(1+3/20000)^2<100/99`. Therefore the TOTAL possible negative contribution
in 100<gamma<T is at most

    E=T^(2-2n) exp(-.99T),                                    (6.2)

provided `.99T>=n`. Indeed gamma^(-2n)exp(-.99b/gamma^2) is increasing
up to T under this condition, and N(T)<=T^2.

For a positive contribution apply Lemma MD-03a with L=sqrt(b/n).
When T>=max(100,n), L>=T>=100, so a zero exists in [L,2L], entirely in
the positive-phase region. Its real part is greater than

    P=(1/2)(n/(15b))^n.                                      (6.3)

To see this, its cosine is at least cos1>1/2, |1+A|<=gamma^2+3/2<=5b/n,
and |A|/|1+A|>=gamma^2/(gamma^2+1)>=(1+n/b)^(-1).
The b-th power of the latter is at least exp(-n)>3^(-n).
This uses a zero of unrestricted real part, not an assumed line zero.

The ratio of (6.2) to (6.3) is bounded by

    R(T,n)=2T^2(15T/n)^n exp(-.99T).                           (6.4)

**Theorem ASTRA-MD-03a (complete columns).**

    0<=a<=19, b>=0 ==> H_(a,b)(1)>0.                           (6.5)

For b<=10^6, Lemma MD-02a applies. For b>10^6, n<=20 and T>100.
R(T,n) is increasing in n on 1<=n<=20 and decreasing in T>=100, by
its explicit logarithmic derivatives. Hence

    R(T,n)<=20000*75^20*exp(-99)
             <20000*75^20*(60/163)^99<1/10.

The last inequality is exact rational arithmetic. Thus (6.2) cannot cancel
(6.3). In particular, in this large-b region,

    H_(a,b)(1)>(1/4)(n/(15b))^n.                              (6.6)

**Theorem ASTRA-MD-03b (unbounded cubic wedge).** For ANY a>=0,

    b>=max(10^6,8000(a+1)^3)
       ==> H_(a,b)(1)>(1/4)((a+1)/(15b))^(a+1)>0.              (6.7)

For the equality case b=10^6 with T=100, the phase rectangle or the same
bounds with an empty negative interval apply. Otherwise T>=max(100,20n).
The logarithmic derivative in T of R(T,n) is `(n+2)/T-.99<0` on T>=20n.
Thus

    R(T,n)<=800 n^2 (300 exp(-19.8))^n
            <800 n^2 q^n,
    q=300(60/163)^19<1/8000,      4q<1.

Since n^2<=4^(n-1), this is at most 800q<1/10. Use (6.2)--(6.3).
The comparisons at T=20n are purely scalar; when 20n<100 no application
of the zero-count bound at that smaller T is made. QED.

Together with Section 4, these results prove that each fixed row and each
fixed column is eventually positive; the stated boundary rows and columns
are positive throughout. They also give two doubly unbounded regions.
They do NOT fill the expanding intermediate region. At v=1 a convenient
superset of the still-uncontrolled indices is

    a>=20,   100a<b<max(10^6,8000(a+1)^3).                     (6.8)

The phase rectangle pays some additional cells in (6.8). It is not claimed
that every cell in (6.8) is negative or genuinely difficult. It remains an
infinite region, not a finite verification task.

## 7. An exact quantitative obstruction, not only an equivalence

For fixed v>0 and N>=0 define the binomial row and its total variation:

    w_(N,a)=binom(N,a)H_(a,N-a)(v),       0<=a<=N,
    V_N=sum_(a=0)^N |w_(N,a)|,
    D_N=sum_(a=0)^N max(0,-w_(N,a)),
    M=p_1^*(v)=v h(v)>0.

The binomial theorem gives the conservation law

    sum_a w_(N,a)=M,        V_N=M+2D_N.                        (7.1)

Put

    R(v)=sup_A (v+|A|)/|v+A|.                                (7.2)

**Theorem ASTRA-MD-04 (exact exponential rate).**

    limsup_(N->infinity) V_N^(1/N)=R(v).                       (7.3)

Consequently the following statements are equivalent at ONE fixed v>0:

    RH;
    H_(a,b)(v)>=0 for all a,b;
    R(v)=1;
    limsup_(N->infinity) log(M+2D_N)/N=0.                      (7.4)

If RH is false, R(v)>1 and the negative row mass is exponentially large
along an unbounded sequence of rows. In particular infinitely many rows
contain an actual negative mixed difference. No linear independence of
zero ordinates and no simple-zero hypothesis are used.

Proof of (7.3). Let k=k_A and C=sum_A |k|<infinity. The binomial theorem
and the triangle inequality imply

    V_N<=sum_A |k|(|k|+|1-k|)^N<=C R(v)^N.                    (7.5)

For the lower bound, the row polynomial is

    Q_N(z)=sum_a w_(N,a)z^a
          =sum_A k_A(1-k_A+k_A z)^N.                         (7.6)

On |z|=1, |Q_N(z)|<=V_N. If R(v)>1, the supremum in (7.2) is attained:
A's form a discrete multiset escaping to infinity, and their ratios tend
to one. Select A_* attaining it and put z_*=A_*/|A_*|. A_* is nonreal,
so z_*!=1. Then

    |1-k_*+k_* z_*|=(v+|A_*|)/|v+A_*|=R(v).

For this fixed z_* set b_A=1-k_A+k_A z_*. The generating function is

    sum_(N>=0) Q_N(z_*) t^N=sum_A k_A/(1-t b_A).               (7.7)

It is normally convergent initially and extends meromorphically to |t|<1.
To justify this statement locally away from the finitely many relevant
poles, note b_A->1, sum|k_A|<infinity, and 1-t is bounded away from zero
on every compact subset of |t|<1. Because z_*!=1, A->k_A->b_A is injective
on distinct A locations. A pole from a repeated location has residue
`-m k_A/b_A`, which is nonzero. Distinct locations cannot cancel it.
Thus the nearest pole has modulus 1/R(v), and Cauchy--Hadamard gives
`limsup |Q_N(z_*)|^(1/N)=R(v)`. Combine with |Q_N|<=V_N and (7.5).
If R(v)=1, triangle equality forces every A positive real; every row is
nonnegative and V_N=M. This proves (7.3) in all cases. Finally, because
Im A=gamma(1-2beta) with gamma>0, A is real exactly when beta=1/2.
The parent's exclusion of real nontrivial zeros completes the equivalence.
Equations (7.1)--(7.3) prove (7.4). QED.

The rate is an exact invariant of horizontal displacement. It is not
newly bounded by one in this packet. A small positive rate is still an
exponential obstruction and cannot be rounded down to zero.

## 8. Where the amplification lives, and a rigorous unconditional rate bound

For A=x+i y and r=|A|,

    ((v+r)/|v+A|)^2=1+2v(r-x)/|v+A|^2.                       (8.1)

Since r-x=y^2/(r+x)<=1/2 by (1.1), V100 implies

    0<=log R(v)<=v/[2(v+10000)^2].                            (8.2)

The real verified zeros have rate exactly one. This estimate is NOT a
subexponential bound: its exponent is small but strictly positive.

For z=exp(i theta), the summand base in (7.6) is

    b_A(z)=(A+v exp(i theta))/(A+v).

Writing alpha=arg A,

    |b_A(exp(i theta))|>1
       iff cos(theta-alpha)>cos alpha.                      (8.3)

The maximal modulus for this A occurs at theta=alpha, not on a fixed
macroscopic arc. V100 confines unverified |alpha| below arctan(1/100).
Therefore with theta in [-pi,pi],

    |theta|>=2 arctan(1/100)
       ==> |Q_N(exp(i theta))|<=sum_A |k_A|, for every N.      (8.4)

For example, a fixed macroscopic phase cannot substitute for control of
the narrow unresolved arc about theta=0. At theta=0, Q_N(1)=M exactly;
a bound at that one point does not control its punctured neighborhood.

For fixed v and bounded delta=beta-1/2, a zero of height gamma tending to
infinity has

    log[(v+|A|)/|v+A|]=2v delta^2/gamma^4+O_v(gamma^(-6)).      (8.5)

This is a one-atom expansion, not a claim that any off-line zero exists.
It follows by expanding (8.1), using x=gamma^2+1/4-delta^2 and y=-2delta gamma.
An arbitrarily small nonzero displacement is still visible at sufficiently
large N. The tests below verify exact finite counterparts, not this limit.

## 9. A countermodel to the missing subexponential inference

The parent's polynomial

    F(u)=(1+u)((u+2)^2+1)/5

has positive heat at all times and positive p_n^* at all orders, but its
A-list is 1,2+i,2-i. At v=1,

    R^2=(3+sqrt(5))/5>1.

For the rational unit-circle point z=(4+3i)/5 the three bases in (7.6) are

    9/10+3i/10,      1+i/5,      22/25+4i/25,

with squared moduli 9/10, 26/25, 4/5. Their coefficients k_A are nonzero;
the middle base is uniquely dominant. Thus this already gives exponential
row variation, while the exact earlier witness is

    H_(0,14)=-433316717939/10^15.

The checker reconstructs complete rows, Q_N in two ways, conservation, and
an N=100 violation of |Q_N(z)|<=M, all over rational complex arithmetic.
Neither this polynomial nor the parent's positive-source quartet is actual
zeta. They refute promotion of the already-proved heat information to the
new subexponential condition.

## 10. Return to the literal theta/prime source: the exact open inequality

The row polynomial is available without inserting zero locations:

    Q_N(z)=sum_(j=0)^N binom(N,j)(z-1)^j p_(j+1)^*(v)
          =integral_0^infinity exp(-x) S(x/v)
                              L_N((1-z)x) dx,                (10.1)

where L_N is the ordinary Laguerre polynomial. For |t| sufficiently small,

    sum_(N>=0) Q_N(z)t^N
       =v/(1-t) h(v(1-zt)/(1-t)).                            (10.2)

These follow from the finite Laguerre expansion and its generating function.
Initial exchanges in (10.2) occur in a small disk where the transformed
Laplace parameter has positive real part. It is NOT claimed that the
parameter stays Euler-safe for every |t|<1 and |z|=1. Extending it through
a possible pole is exactly the unpaid step, not a formal manipulation.

The parent's finite connected-cumulant formula computes every p_n^* from
its actual theta probability law. Alternatively, for u>0 set

    r=sqrt(u+1/4),       s=1/2+r>1.

The ordinary, absolutely convergent Euler series gives

    h(u)=1/u + [psi(s/2)-log pi]/(4r)
                  -[1/(2r)]sum_(m>=2) Lambda(m)m^(-s).        (10.3)

At each FIXED finite derivative order and u>0, differentiation under this
series is legitimate locally. In (1.5), when b>=1 the 1/u term is killed
exactly. What remains is an archimedean derivative minus a signed prime sum.
For ell=log m define a rational-polynomial kernel by

    R_(0,b)(r;ell)=(r^2-1/4)^b/r,
    R_(j+1,b)=(partial_r R_(j,b)-ell R_(j,b))/(2r).             (10.4)

Then

    D_u^j[u^b exp(-r ell)/r]=exp(-r ell)R_(j,b)(r;ell).

This retains every prime-power term and is suitable for exact source work.
The prime kernel is not termwise positive. Already b=1,j=1,r=1 gives

    R_(1,1)(1;ell)=5/8-3ell/8.

At the actual prime m=2 it is positive; at m=7 it is negative, since
log2<1 and log7>5/3. The latter follows from e<3 and 3^5<7^3.
Taking absolute values before summing discards the needed cancellation.

### The current conclusion-bearing source target

At one fixed v>0, prove for every epsilon>0 a finite C_(epsilon,v) such that

    sup_(|z|=1) |Q_N(z)| <= C_(epsilon,v) exp(epsilon N)
                              for every integer N>=0.        (10.5)

This would prove RH, hence ALL the mixed inequalities, by Theorem MD-04.
Indeed Cauchy's coefficient formula gives
`V_N<= (N+1) sup_(|z|=1)|Q_N(z)|`; the polynomial factor has rate one.
Conversely under RH, (7.6) gives the stronger bound |Q_N(z)|<=M on |z|<=1.
Thus (10.5) is RH-equivalent, not asserted to be an easier theorem.

The complete attempt has reached the literal signed arithmetic sum
(10.3)--(10.4). Neither the positive heat theorem nor the newly proved
regions bound (10.1) subexponentially on the remaining angular arc. This
packet does not claim that estimate, an unconditional RH proof, or a
finite reduction of the remaining infinite region.
