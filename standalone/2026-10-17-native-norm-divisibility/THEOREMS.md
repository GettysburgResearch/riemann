# Complete native norm-divisibility covariance at a fixed center

Status: PROPOSED complete unconditional component proofs. Same-author proofs
and checkers; no independent mathematical review or formal proof build.
Scope: the original principal ideal-Mobius source over Q(omega), with exactly
the primes above 2 and 3 excluded. A fixed real Mellin twist, not an average
of twists, is used. No quasi-RH input or unknown native moment is assumed.
No full moment exponent, zero-free boundary, or proof of RH is obtained.

The new object is **divisibility of rational norms**, not divisibility of
ideals. All distinct equal-norm ideals are retained before forming products.
The infinite divisor sector contains both signs and ideals which are not
comparable under ideal divisibility. Its complete signed value is evaluated,
including a power-decaying remainder. The previously known norm-diagonal
logarithm and Gaussian kernel are not claimed as new.

## 1. Source and main results

Let K=Q(omega), omega^2+omega+1=0, and let S consist of the prime ideals over
2 and 3. All ideals I below are nonzero integral ideals coprime to S. Put

    a(n) = sum_(NI=n) mu_K(I),
    W_c(y) = y^(-c) exp[-(log y)^2/4]/(2 sqrt(pi)),
    A_t(X) = sum_I mu_K(I) (NI)^(it) W_c(NI/X),
    E_t(D) = integral_0^D |A_t(X)|^2 dX/X^2,                (1)

where c is any fixed real number; the imported detector uses c=5/6. All
Gaussian tails are retained. The source is scalar and principal; arbitrary
complex row phases, additional exclusions and growing conductors are not
included in the numerical constants below.

Write beta=2c-1 and kappa=exp(beta^2/2)/(2 sqrt(2pi)). Let Phi be the standard
normal CDF. The exact kernel is

    K_D(n,m) = kappa/sqrt(nm) exp[-log(n/m)^2/8]
                      Phi(log D - log(nm)/2 - beta).       (2)

Define three disjoint sectors of the complete energy:

    Delta(D) = sum_n a(n)^2 K_D(n,n),
    P_t(D) = sum_(n!=m; n|m or m|n)
                    a(n)a(m) exp(it log(n/m)) K_D(n,m),
    R_t(D) = sum_(n does not divide m; m does not divide n)
                    a(n)a(m) exp(it log(n/m)) K_D(n,m).

Both orientations are included. Each sector is real by conjugate pairing.
They satisfy E_t=Delta+P_t+R_t exactly. These definitions are equivalent to
summing the underlying ideal pairs; they do not select one ideal per norm.

### Theorem 1: an entire infinite covariance sector is bounded

For D>=2 and every real t,

    sum_(NI!=NJ; NI|NJ or NJ|NI)
                   |mu_K(I)mu_K(J)| K_D(NI,NJ)
           <= C_c (1+log D)^2.                             (3)

In particular |P_t(D)| has the same upper bound. The ratios and the common
factors are unrestricted; this is not a fixed-ratio graph or finite box.

### Theorem 2: a three-term signed asymptotic

There is c_*>0 such that

    Delta(D)=c_* (log D)^2+d_1 log D+d_0
                       +O_(c,epsilon)(D^(-1/2+epsilon)).   (4)

For every 0<epsilon<1/2 there are explicitly defined bounded real functions
B(t),C(t),Lambda(t), independent of D, for which

    P_t(D)=-Lambda(t)c_* (log D)^2+B(t)log D+C(t)
                       +O_(c,epsilon)(D^(-1/2+epsilon)),   (5)

uniformly over ALL real t. This is an asymptotic for a signed sector of the
original source, not a bound for E_t. Formulae (17)-(19) specify every
coefficient as an absolutely convergent series of Laurent coefficients of
explicit Euler products. No assertion about zeros of an inverse L-function
is used in shifting the contour.

### Theorem 3: rigorously certified fixed-center cancellation

The exact infinite leading coefficient satisfies

    2.153 < Lambda(0) < 2.155.                             (6)

Its certified enclosure from the code is the outward decimal interval

    [2.1533394320086571, 2.1542699672498351].

Moreover

    Lambda(t)>21/10   for every |t|<=1/20.                 (7)

This is a fixed-center interval, not a mean over centers. The interval in
(6) is certified using integer arithmetic AND the proved infinite tail
bound in Section 6, not by extrapolating a finite prime or norm census.
The coefficient is independent of c: c changes c_*,B,C, not Lambda.

Consequently the complete still-uncontrolled rationally incomparable
sector satisfies, uniformly for |t|<=1/20 and D>=2,

    R_t(D) >= (11/10) Delta(D)-C_c(1+log D).               (8)

Thus that remaining signed sector is eventually positive and has at least
log-squared growth. It cannot be discarded as nonpositive. Inequality (8)
is a LOWER bound, not the needed upper bound for the full energy.

## 2. Literal norm coefficients and absolute convergence

At a rational prime p>=5, the local coefficients of the native source are

    p=1 mod 3:    1-2x+x^2,
    p=2 mod 3:    1-x^2,                                  (9)

where x=p^(-s). The factor is 1 at 2 and 3. Indeed a split p has TWO prime
ideals of norm p, each with local Mobius factor 1-x. An inert p has ONE
prime ideal of norm p^2. This gives, multiplicatively,

    a(p)=-2, a(p^2)=1       (p split),
    a(p)=0,  a(p^2)=-1      (p inert),
    a(p^e)=0 for e>2.

All ideals in a nonempty norm fiber have the same Mobius sign. At a split
prime that sign is (-1)^e; at an inert prime it is (-1)^(e/2). Therefore

    sum_(NI=n)|mu_K(I)|=|a(n)|.                            (10)

This fact is already explicitly established in #955 and is not new here.
It is essential for passing from the ideal absolute sum in (3) to norm
coefficients. It is NOT asserted for arbitrary row phases or completions.

For completeness, the usual Eisenstein ideal count has the explicit bound
I_K(x)<=3x for x>=1. The ring is norm-Euclidean and hence every ideal is
principal. If N(a+b omega)=a^2-ab+b^2<=x, then |a|,|b|<=2sqrt(x/3)<3sqrt(x)/2.
The number of nonzero lattice points is at most (3sqrt(x)+1)^2-1. Dividing
by the six units bounds I_K(x) by (3/2)x+sqrt(x)<= (5/2)x<3x.
The norm-Euclidean assertion can itself be seen by rounding the two real
coordinates of any point in the basis 1,omega: the error has coordinates
in [-1/2,1/2], so its norm is at most 3/4<1. This gives Euclidean division.

In particular sum_(n<=x)|a(n)|<=3x. Positive partial summation gives
sum_n |a(n)| W_c(n/X)<=C_c X. Its square is integrable against dX/X^2 on
(0,D); the Gaussian also gives flatness at X=0. This proves absolute Fubini
for every sector and the complete pair expansion. Completing the square
in x=log X yields (2), with the full lower tail -infinity. No positivity is
asserted after deleting arbitrary off-diagonal terms.

## 3. Exact classification of ALL rationally divisible pairs

For a supported integer r let

    P1(r) = product_(p split, v_p(r)=1) p,
    H_r(x) = sum_((h,r)=1) a(h)^2/h
                              Phi(log x-log h-beta).      (11)

A pair with larger norm n and smaller norm m, with n/m=r>1, has nonzero
coefficient exactly when it can be written uniquely as

    n=r d h,    m=d h,    d|P1(r),    (h,r)=1,              (12)

where a(r)a(h) is nonzero. The signs obey the EXACT identity

    a(rdh)a(dh)=a(r)a(h)^2.                               (13)

At a split prime of r-exponent one, the exponent pairs are (1,0) and (2,1);
both products are -2. They are respectively d-exponent zero and one. At a
split prime of r-exponent two, only (2,0) occurs, with product +1. At an
inert prime, only ratio exponent two is possible, with product -1. At
primes outside r the exponents agree and contribute a(h)^2. This proves
(12)-(13), including all shared split primes and both signs.

Substitution into (2) gives the exact all-ratio identity

    P_t(D)=2 kappa sum_(r>1) a(r)/sqrt(r) exp[-(log r)^2/8]
            cos(t log r) sum_(d|P1(r)) (1/d) H_r(D/(d sqrt(r))). (14)

The sum over r is over every positive integer, with a(r)=0 on the
unsupported ones. The shift is d sqrt(r), NOT just sqrt(r). Omitting the
d=p branch already fails for norms (49,7). Ideal comparability is not
imposed: for example I=bar(p_7)*p_13, J=p_7 have norms 91 and 7 and are
incomparable as ideals; their term nevertheless occurs in (14).

### Absolute upper bound

Let F(s)=sum_n a(n)^2 n^(-s). At p>=5 its local factors Q_p are

    Q_p(s)=1+4p^(-s)+p^(-2s)     (p split),
    Q_p(s)=1+p^(-2s)             (p inert).

Factoring against zeta_K(s)^2 gives

    F(s)=zeta_K(s)^2 G(s),
    G_2(s)=(1-2^(-2s))^2,   G_3(s)=(1-3^(-s))^2,
    G_p(s)=(1+4z+z^2)(1-z)^4=1-9z^2+16z^3-9z^4+z^6 (split),
    G_p(s)=(1+z^2)(1-z^2)^2=1-z^2-z^4+z^6          (inert), (15)

where z=p^(-s). The coefficients of G have summable absolute mass at weight
1 because the first nonconstant rational-prime term has degree at least two.
The two ideal-count convolutions in zeta_K^2 and I_K(x)<=3x give
sum_(n<=x)a(n)^2<=C x(1+log x). Positive partial summation, retaining the
normal-CDF tail, therefore gives

    H_r(x)<=H_1(x)<=C_c(1+max(0,log x))^2, x>0.

For example integrate the decreasing function Phi(log x-log v-beta)/v
against the prefix bound; on v>=1, write v=e^y. The resulting integrals
are a polynomial of degree at most two in the positive part of log x,
plus bounded Gaussian tails. This also treats x<1.

In (14) all x=D/(d sqrt(r))<=D. The remaining absolute constant is finite:

    sum_r |a(r)| r^(-1/2) exp[-(log r)^2/8]
                                      sum_(d|P1(r)) 1/d < infinity.

Even the crude estimates |a(r)|<=r and sum_d1/d<=r suffice, since a
log-Gaussian beats every fixed power as r tends to infinity. Applying
(10) proves (3), including absolute values before all ideal-pair sums.

## 4. Meromorphic continuation, with the moving exclusions retained

We give the analytic details needed for the power-decaying error; real
Tauberian information alone would not yield it. Product (15) converges
normally on Re s>1/2, uniformly bounded on every smaller closed half-plane.
There are no denominators or assumed inverse-zeta estimates in G.

The classical splitting identity zeta_K(s)=zeta(s)L(s,chi_-3) holds first
on Re s>1 by the same split/inert Euler factors. For Re s>0 the elementary
partial-summation formulae

    zeta(s)=s/(s-1)-s integral_1^infinity {x}x^(-s-1)dx,
    L(s,chi_-3)=s integral_1^infinity A_chi(x)x^(-s-1)dx,
    |A_chi(x)|<=1,

give continuation, polynomial vertical growth and the sole pole at 1.
The residue of zeta_K at 1 is L(1,chi_-3)>0: pair terms
(3j+1)^(-1)-(3j+2)^(-1). Every real local factor of G(1) is positive,
and the product converges absolutely. Hence

    mathfrak_a = lim_(s->1)(s-1)^2 F(s)
                = L(1,chi_-3)^2 G(1) > 0.

This establishes the required facts without a PNT, QRH, RH or a zero census.

For a moving supported integer r define

    F_r(s)=sum_((h,r)=1) a(h)^2 h^(-s),
    Q_r(s)=product_(p|r) Q_p(s).

Although F_r=F/Q_r where initially defined, DO NOT bound 1/Q_p on the
shifted contour. Such a local polynomial can have complex zeros in the
region. Instead form G_r directly: at a removed split prime its factor
is (1-p^(-s))^4; at a removed inert prime it is (1-p^(-2s))^2. At all
other primes retain (15). Thus F_r=zeta_K^2 G_r is holomorphic on Re s>1/2
except for its double pole at one, and for every fixed delta,eta>0,

    |G_r(s)|<=C_(delta,eta) r^eta,  Re s>=1/2+delta.

Indeed the unremoved factors have a uniform absolutely convergent
majorant. The removed factors are bounded by exp(4 sum_(p|r)p^(-1/2-delta)).
For all sufficiently large p, 4p^(-1/2-delta)<=eta log p; the finitely many
smaller primes contribute a fixed constant. Polynomial vertical bounds
for F_r follow. This argument explicitly avoids a false uniform division
by a local factor at one of its complex zeros.

Write the Laurent expansion at one as

    F_r(1+z)=A_r/z^2+B_r/z+C_r+O_r(z),
    A_r=mathfrak_a/Q_r(1)>0,
    U_r=B_r-beta A_r,
    V_r=C_r-beta B_r+(beta^2+1)A_r/2.                     (16)

All these are explicit in (15) and the classical Dedekind Laurent
coefficients. On a small fixed circle about 1 the same r^eta bounds,
after removing the double pole, give A_r,B_r,C_r=O_eta(r^eta).
Their real values are used below. No uniformity in a new number field or
additional unbounded conductor is asserted.

For x>0 the CDF has the absolutely convergent Mellin representation
Phi(y)=integral_(Re z=b>0) exp(z^2/2+zy) dz/(2pi i z).
It follows by differentiating to recover the normal density and using its
limit at y=-infinity. Fubini on b>0 now yields

    H_r(x)= integral_(b) F_r(1+z) exp(z^2/2-beta z) x^z dz/(2pi i z).

Shift to Re z=-1/2+epsilon. The only crossed pole is the triple pole at z=0.
The Gaussian kills the horizontal contour integrals, while the preceding
polynomial bounds control the vertical line. Consequently, for every x>0,

    H_r(x)= (A_r/2)(log x)^2+U_r log x+V_r
              +O_(epsilon,eta,c)(r^eta x^(-1/2+epsilon)). (17)

The uniform statement for ALL x>0 is important: (14) contains x<1 for
large ratios. Its error grows there, rather than silently applying a
large-x expansion outside its range. At r=1 this proves (4), with
c_*=kappa*mathfrak_a/2, d_1=kappa U_1 and d_0=kappa V_1.

## 5. Summing the complete signed asymptotic

Define b(r) multiplicatively by b(1)=1, by zero at primes 2,3, and by

    b(p)= -2p(p+1)/(p^2+4p+1),
    b(p^2)=p^2/(p^2+4p+1)                     (p split),
    b(p)=0,
    b(p^2)=-p^2/(p^2+1)                       (p inert),
    b(p^e)=0 for e>2.

Equivalently, preserving the shared factors,

    b(r)=a(r)/Q_r(1) * sum_(d|P1(r)) 1/d.

Then

    Lambda(t)=-2 sum_(r>1) b(r)/sqrt(r)
                         exp[-(log r)^2/8] cos(t log r).  (18)

Put v_(r,d)=log d+(log r)/2 and
w_r(t)=a(r)r^(-1/2) exp[-(log r)^2/8]cos(t log r). The remaining coefficients
in (5) are

    B(t)=2 kappa sum_(r>1) w_r(t)
                      sum_(d|P1(r)) (U_r-A_r v_(r,d))/d,
    C(t)=2 kappa sum_(r>1) w_r(t)
               sum_(d|P1(r)) [A_r v_(r,d)^2/2-U_r v_(r,d)+V_r]/d. (19)

These are absolutely convergent and bounded uniformly in real t. Substitute
(17) into (14). For gamma=1/2-epsilon the sum of the absolute errors is at
most a constant times

    D^(-gamma) sum_r |a(r)| r^(-1/2+eta+gamma/2)
                 exp[-(log r)^2/8] sum_(d|P1(r)) d^(gamma-1).

This converges even under crude polynomial bounds. It proves the uniform
error and every interchange in (5). The log-squared coefficient is
kappa*mathfrak_a sum_(r>1) b(r)r^(-1/2)exp[-log^2(r)/8]cos(t log r)
=-Lambda(t)c_*, as claimed. In particular no common-norm terms or repeated
split-prime channels disappear into an unspecified remainder.

## 6. An infinite-constant certificate and a fixed-center neighborhood

All local formulae give |b(r)|<=|a(r)|. Hence, at EVERY real x>=1,

    sum_(r<=x)|b(r)|<=I_K(x)<=3x.                         (20)

Let L=log N>4, g(v)=v/2-v^2/8 and alpha=(L-2)/4. For
f(x)=x^(-1/2)exp[-(log x)^2/8], both f and f(x)log^2 x decrease on x>=N.
Stieltjes integration using (20), without extrapolating a finite count,
gives the two explicit absolute tails

    sum_(r>N)|b(r)| f(r)
        <= 3 exp(g(L)) (1+1/alpha),
    sum_(r>N)|b(r)| f(r)log^2 r
        <= 3 exp(g(L)) [L^2(1+1/alpha)+2L/alpha^2+2/alpha^3]. (21)

For the first, bound -A(N)f(N)+integral_N^infinity A(x)(-f'(x))dx by
3[Nf(N)+integral_N^infinity f(x)dx]. After x=e^v,
g(L+y)<=g(L)-alpha*y. Integrate 1 for the first tail and (L+y)^2 for the
second. This proves (21) with an explicit infinite remainder.

The supplied checker enumerates every rational integer r<=N=65536 and
uses its exact Fraction coefficient b(r). There are 6293 nonzero such
coefficients, including r=1. Integer dyadic intervals of 112 fractional
bits enclose the finite signed sum and second absolute log moment. Its
reported outward bounds are

    sum_(r<=N)b(r)f(r)
      in [-0.0769023498146231,-0.0769023498146230],
    first absolute tail <=0.0002326338102945,
    sum_(r>=1)|b(r)|f(r)log^2 r <15.5176113160626648<16.

Thus (18) at zero proves (6). Every transcendental operation in this
certificate is reduced to integers: ln(n)=j ln(2)+ln(n/2^j), the atanh
series with ratio at most 1/3 has its explicit positive geometric tail;
exp(-u/32) is enclosed by a degree-40 Taylor polynomial with remainder
at most 3/41!, then squared five times. Every fixed-point operation rounds
outwards by integer floor/ceiling. The proof e<3 follows from the elementary
factorial series. No binary floating-point or ordinary high precision is
used as a certificate. See intervals.py and CHECKS.json for exact numerators.

Finally 2|1-cos y|<=y^2 implies

    |Lambda(t)-Lambda(0)|
       <= t^2 sum_r |b(r)|f(r)log^2 r <16t^2.

For |t|<=1/20 the certified lower bound is greater than
2.1533394320086571-15.5176113160626648/400>2.1145>21/10.
The interval reported for this LOWER-BOUND EXPRESSION is not an upper bound
on Lambda(t) throughout the band. This proves (7).

## 7. The compensated remainder, and the unchanged RH boundary

The original E_t(D) is nonnegative. Combining E=Delta+P+R with (4)-(5)
yields, for each real t,

    R_t(D)>=(Lambda(t)-1)c_*log^2 D-O_c(1+log D),

with uniform constants in t because the coefficient series are absolutely
summable. On |t|<=1/20, (7) and (4) give precisely (8), for all D>=2 after
absorbing bounded small-D terms into the constant.

The remaining sum can also be written without ambiguous ideal/norm gcds.
For coprime rational integers A,B>1, apply the same local classification to
AB. Both ordered orientations are now retained in the double sum, so there
is NO exterior factor two:

    R_t(D)=kappa sum_(A,B>1; (A,B)=1)
      a(A)a(B)/sqrt(AB) exp[-log(A/B)^2/8] exp(it log(A/B))
      *sum_(d|P1(AB)) H_(AB)(D/(d sqrt(AB)))/d.             (22)

This is an exact, absolutely convergent finite-horizon identity inherited
from the original pair expansion. Unlike (14), its ratio Gaussian does not
decay when A and B grow together. Formula (17) therefore CANNOT be summed
termwise over all of (22) using the argument of Section 5: the resulting
absolute error sum need not converge. Direct absolute coefficient counting
only gives the old O_c(D) full-energy scale, not a critical estimate. This
is the explicit failure point of the attempted extension to an upper bound
for the entire fixed-center source.

This identifies a larger, explicitly evaluated signed sector than ideal
divisibility, and a positive main-order compensation in the remaining
rationally incomparable sector. The missing estimate is still an UPPER
bound for that remainder after compensation. At t=0 an all-epsilon bound
E_0(D)<=C_epsilon D^epsilon would have the previously stated critical
significance. It does not follow from (3), (5), (6) or (8).

The power D^(-1/2+epsilon) in (5) is the remainder of this selected-sector
ASYMPTOTIC. It is NOT a new full-moment saving or a zero-free exponent.
The constant and the fixed-center band are for the declared native source
and exclusions only; neither arbitrary row phases nor the complete physical
sextic family is bounded here. No general historical novelty claim is made
for Euler products, Gaussian kernels, contour shifts, or covariance grouping.
