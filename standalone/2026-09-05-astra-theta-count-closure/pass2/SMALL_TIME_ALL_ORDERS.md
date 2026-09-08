# An order-uniform small-time theorem and its global mixed-moment consequence

Status: PROPOSED COMPLETE PROOFS OF THE STATED REGIONS; independent review
required. Not a proof of complete monotonicity on the whole positive axis.
Scope: all derivative orders for 0<t<=10^-8; all t>0 through order 10^15.
Dependencies: parent normalization, S>0, V100 and Z14/15; classical
argument-principle zero-count identity, Euler--Maclaurin and Stirling;
the large finite-order corollary ALSO imports V_(3*10^12).
Computation: rational controls only. No unbounded claim is inferred from
finite tests. No external-priority assertion is made.

## 1. The theorem to be proved

Keep S and D_m=(-1)^m S^(m) from MIXED_HEAT_STRIPS.md. Set tau_*=10^-8.

**Theorem ASTRA-TC2-04.** Every integer m>=0 satisfies

    D_m(t)>0                         (0<t<=tau_*).            (1)

For m>=1 the following explicit lower bound holds:

    D_m(t) > exp(-t/4)/1024 * (m/t)^m exp(-m)
                    * t^(-1/2) log(sqrt(m/t)).               (2)

This is simultaneous in m and t, not "for every m, eventually as t->0."
The proof uses the complete zero count and the cancellation of the two
components of each summand's phase at its Gaussian saddle. It uses no
RH assertion above height 100.

## 2. A coarse explicit counting remainder

Let N(T) count ALL nontrivial zeros with 0<Im rho<=T, with multiplicity, and

    M(T) = T/(2pi) log(T/(2pi e)).

We use the classical argument-principle identity, at ordinates not containing
zeros,

    N(T)=1+theta(T)/pi+Arg_T zeta(1/2+iT)/pi,                  (3)

where theta(T)=Im log Gamma(1/4+iT/2)-(T/2)log pi, and Arg_T is continued
from 2 up the line Re s=2 and then horizontally to 1/2+iT. The log Gamma
branch is the continuous one on Re z>0, real on the positive real axis.
Identity (3) is a classical imported theorem (Titchmarsh, 2nd ed., Ch. 9),
not a new contribution; it follows by applying the argument principle to
completed xi and using its reflection and conjugation symmetries. Its N
counts off-line zeros as well as critical-line zeros. Endpoint values below
are obtained by taking right limits. We do NOT import any optimized bound
for the argument term.

**Lemma ASTRA-TC2-05.** For T>=100,

    |N(T)-M(T)| <= 20 log(T+2).                               (4)

Here is an elementary, deliberately wasteful derivation of the constant.
For fixed T define the holomorphic function on |z-2|<=2

    f_T(z)=(zeta(z+iT)+zeta(z-iT))/2.

It is real on real z, and f_T(2)=Re zeta(2+iT)>1/3, since zeta(2)<5/3.
One integration by parts of the Euler--Maclaurin representation gives

    zeta(s)=1/(s-1)+1/2+s/12
           -s(s+1)/2 * integral_1^infinity B2_tilde(x)x^(-s-2)dx,
                                                                  (5)

valid for Re s>-1 away from s=1. Here |B2_tilde|<=1/6. For s=z+/-iT on
that disk, Re s>=0, |s|<=T+4, |s+1|<=T+5 and |s-1|>=T-2. Therefore

    |zeta(s)| <= 1/(T-2)+1/2+(T+4)/12+(T+4)(T+5)/12 <2T^2.   (6)

Jensen, with inner radius 3/2 and outer radius 2, bounds the number q_T of
zeros of f_T in |z-2|<=3/2 by

    q_T <= log(6T^2)/log(4/3) < 8 log T+8.                   (7)

If a circle contains a zero, use a limiting radius. The strict estimate
log(4/3)>1/4 and log 6<2 suffice.

For T not a zero ordinate, the horizontal path contains no zeta zero.
Its real part can vanish at most q_T times. On each intervening segment
its continuous argument lies in an interval of length pi. On the vertical
Re s=2 path zeta stays in the right half-plane. It follows that

    |Arg_T zeta(1/2+iT)|/pi <= q_T+3/2 <8 log T+19/2.         (8)

For completeness, a standard Euler--Maclaurin remainder for log Gamma is

    log Gamma(z)=(z-1/2)log z-z+(1/2)log(2pi)+R(z),
    R(z)=1/(12z)-(1/2) integral_0^infinity B2_tilde(x)/(x+z)^2 dx.

Thus |R(z)|<=1/(12|z|)+1/(12 Re z). At z=1/4+iT/2 this is less than
2/3. Writing b=T/2, the difference between the elementary part of theta
and (T/2)log(T/(2pi e))-pi/8 has magnitude at most

    (b/2)log(1+1/(16b^2))+(1/4)atan(1/(4b)) <=3/(16T).

So that difference, including R, is less than 1. Equations (3), (8) imply
|N(T)-M(T)|<8 log T+12<20 log(T+2). Right limits extend the bound to all
T>=100, including multiple zeros. Formula (5) and the Gamma remainder are
classical Euler--Maclaurin identities, explicitly credited in SOURCES.md.

## 3. Two uniform window-count bounds

For real L>=10000 and r>=L, (4) gives

    N(r+L/2)-N(r-L/2) >= L/(8pi) log r.                      (9)

Indeed M'(x)=log(x/(2pi))/(2pi). Across this interval it is at least
log(r/(4pi))/(2pi)>=log r/(4pi). The two count errors sum to at most
60 log r, and L/(8pi)>60. This proves (9).

For any half-open interval I=(A,B] in the positive ordinate axis of length
at most L, we also have

    number of ordinates in I <= 2L log(B+2).                 (10)

For A>=100, integrate M' and add the two errors, to obtain at most
[L/(2pi)+40]log(B+2). For A<100<B, use B<=L+100<=2L and the total bound
N(B)<[B/(2pi)+20]log(B+2). If B<=100 use N(100)<=10000 from the parent.
Each is bounded by (10). Intervals clipped at zero satisfy the same bound.
All counts retain multiplicities. Half-open intervals prevent counting an
endpoint atom twice; the upper estimates also hold by limits for alternate
endpoint conventions.

## 4. Remove the invariant shift before estimating phases

For rho=beta+i gamma put

    eta=1/2-beta,    w=gamma+i eta,    A=w^2+1/4,
    U_j(t)=sum_(gamma>0) w^(2j) exp(-tw^2),       j>=0.        (11)

The w-list is invariant under complex conjugation. All these sums are real,
and absolutely convergent for fixed j,t. The exact binomial identity is

    D_m(t)=exp(-t/4) sum_(j=0)^m binom(m,j)4^(-(m-j))U_j(t).  (12)

Since U_0(t)=exp(t/4)S(t)>0 by the original theorem, it suffices to establish
U_j(t)>0 for every j>=1, uniformly in 0<t<=10^-8.

Fix such j,t, and set

    L=t^(-1/2)>=10000,   r=sqrt(j)L,
    g(x)=x^(2j)exp(-tx^2),   G=g(r)=(j/t)^j exp(-j).           (13)

The saddle r increases with the derivative order, but its width L does not.

## 5. Uniform Gaussian control of every complex atom

For each zero,

    |w^(2j)exp(-tw^2)| <=2G exp(-(gamma-r)^2/(2L^2)).          (14)

For gamma<=100 this follows with constant 1 from V100 and
(log g)''=-2j/x^2-2t<=-2t.
For gamma>100 define

    ell(x)=j log(x^2+eta^2)-tx^2+t eta^2.

On x>=|eta|, ell''<=-2t. Its maximum occurs at
r_eta=sqrt(r^2-eta^2), with value log G+2t eta^2. Moreover
|r-r_eta|<=1/(4r)<=1/(4L). Applying strong concavity between gamma and
r_eta, and using (x-d)^2>=x^2/2-d^2, proves (14). The prefactor is bounded
by exp(t/2+t/(16L^2))<2. Both points in this concavity argument are at
least |eta|; no estimate through the origin is being asserted.

Inside the central interval |gamma-r|<=L/2 there is also the lower bound

    |w^(2j)exp(-tw^2)| >=g(gamma)>=G exp(-5/4)>G/4.           (15)

Here x>=r/2 and (log g)''>=-10t, while (log g)'(r)=0.
The elementary inequality e^(5/4)<4 can be proved using e<11/4 and
(11/4)^5<4^4.

## 6. The stationary phase cancellation that is uniform in j

Use the continuous phase

    theta_j=2j atan(eta/gamma)-2t gamma eta.                  (16)

Every summand with |gamma-r|<=5L has

    |theta_j|<11/10,    cos(theta_j)>1/4.                    (17)

For gamma<=100 this is immediate from V100. For gamma>100 and j<=100,

    |theta_j|<=j/gamma+t gamma
              <=1+(sqrt(j)+5)/L<=1+15/10000<11/10.

For j>=100 and |gamma-r|<=5L, gamma>=r/2. Crucially the linear pieces in
(16) CANCEL at the saddle:

    |theta_j| <= |j/gamma-t gamma|+j/(12 gamma^3)
               <=15/L+2/(3L^3)<11/10.                       (18)

The error uses |atan x-x|<=|x|^3/3 and |eta|<=1/2. For the main term,
t|r^2-gamma^2|/gamma<=3t|r-gamma|<=15/L. Finally
cos(11/10)>=1-(11/10)^2/2=79/200>1/4.

Bounding the two parts of (16) separately for large j would lose this
uniformity. Equation (18), not a fitted saddle approximation, is the key.

## 7. The positive central mass exceeds the entire exterior tail

By (9), (15), (17), the central interval contributes strictly more than

    (G/16)*(L/(8pi))*log r > GL log r/512.                   (19)

All remaining terms in |gamma-r|<=5L have nonnegative real parts.
Partition the exterior into the two possible intervals
kL<|gamma-r|<=(k+1)L, k>=5, clipping at zero. By (10), (14), their total
absolute contribution is at most

    8GL log r * sum_(k>=5) (k+3) exp(-k^2/2).                (20)

We used log(r+(k+1)L+2)<=(k+3)log r. A complete, rational tail bound is

    8 sum_(k>=5)(k+3)exp(-k^2/2)
      < 64(3/8)^12 / [1-(9/8)(3/8)^5]
      < 1/1024.                                            (21)

To prove the first inequality, use e>8/3,
floor(k^2/2)>=12+5(k-5), and k+3<=8(9/8)^(k-5). The second inequality
is exact rational arithmetic. Thus

    U_j(t) > GL log r/1024 >0.                              (22)

Equations (12), (22) prove (1). Retaining the j=m term proves (2).
All constants are deliberately conservative; none is an optimized claim.

## 8. A parameter theorem and a large finite-depth corollary

**Corollary ASTRA-TC2-06.** Suppose V_H holds for H>=100. If an integer M
satisfies

    2(M+1) <= 10^-8 H^2,
    M log((H^2+1)/196)+log(32H^2) <= 10^-8(H^2-226),          (23)

then D_m(t)>0 for ALL t>0 and 0<=m<=M. Consequently H_(a,b)(v)>0 for
EVERY a>=0, v>0 and 0<=b<=M.

Proof. The small-time interval is (1); for t>=10^-8 use ASTRA-TC2-03.
Its two threshold conditions hold for every m<=M by (23). The mixed
inequality is then the positive integral (2) of MIXED_HEAT_STRIPS.md.

**Corollary ASTRA-TC2-07 (published-prefix application).** The above holds
for

    H=3*10^12,    M=10^15.                                  (24)

This corollary imports the FULL Platt--Trudgian verification, not just its
height-100 restriction. That calculation was NOT rerun. No simplicity input
is used. For a rational certificate of (23), note

    log((H^2+1)/196)<60,   log(32H^2)<100;
    60*10^15+100 < 10^-8(H^2-226),
    2(10^15+1)<10^-8H^2.

The logarithm bounds follow from e>8/3, (8/3)^60>H^2,
(H^2+1)/196<H^2, and e>2, 2^100>32H^2. These are the finite integer-power
comparisons checked by verify_pass2.py; the 10^15 orders are NOT enumerated.

An explicit bound, valid throughout this corollary, is obtained by retaining
only the t>=tau_* part of the mixed integral:

    H_(a,b)(v) > (15/16) 196^b v^(a+1)/(v+226)^(a+b+1)
        * exp(-(v+226)tau_*)
        * sum_(j=0)^(a+b) [((v+226)tau_*)^j/j!].              (25)

For b<=27, equation (7) of MIXED_HEAT_STRIPS.md is stronger.

## 9. What this does NOT prove

The all-order small-time theorem is not complete monotonicity on (0,infinity).
The all-time theorem is finite in m, even at the conservative large bound
10^15. For an arbitrary m, only the intervals

    0<t<=10^-8    and    t>=T_m(3*10^12)

are paid by this pass. For sufficiently large m they leave a nonempty
intermediate interval. Positivity of S itself does not control its m-th
derivative there. The count asymptotic and strip geometry used above are
also shared by some counterfeit spectra with nonreal zeros. No argument
from these coarse data alone to global RH is asserted.

A proof of all the parent's mixed inequalities remains open in this packet.
The alternative exact formulation in BERNSTEIN_GROWTH.md makes the unpaid
information a subexponential bound on signed Bernstein-row mass.
