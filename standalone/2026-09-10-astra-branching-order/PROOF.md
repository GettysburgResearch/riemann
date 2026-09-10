# BOR26: an ordered Brownian–Xi orbit and a genuine zero-preservation test

Date: 2026-09-10. **PROPOSED COMPLETE COMPONENT PROOFS and one computer-assisted
counterexample; independent mathematical/code review required. RH is NOT proved.**
This is a continuation of BSR26 / PR #850 at
`5c26d1f7e1075fdea18119a5abb447102ab5850b`, not an alteration of that packet.

The prescribed Gamma(5/2, rate 5/2) orbit has a new all-depth invariant:
third-order convex ordering. Its ideal-metric error is exactly geometric,
and its complete complex Mellin error has an explicit polynomial-in-height
bound with the same geometric rate. An exact positive Peano remainder retains
the unmodified Brownian fixed law. These assertions do NOT prove the complex
zero property. Separately, the literal map applied ONCE to Gamma(1,1) creates
a certified off-central zero INSIDE the critical strip, although its input
has the parent's whole-strip zero property. This disproves a broader proposed
preservation rule, not preservation of the different Gamma(5/2) orbit.

Classical ingredients are identified in SOURCES.json: BPY's distributional and
Mellin identities, beta–gamma algebra, third-order convex/ideal metrics,
Peano interpolation, elementary complex analysis, and gamma remainder bounds.
No external novelty or priority claim is made for those mechanisms.

## 1. The fixed source and the three statements

On nonnegative mean-one probability laws define

    T(nu) = Law((X_1+X_2)/U^2),

where X_1,X_2 are independent with law nu and the SAME independent uniform
U on [1,2] scales their sum. Set

    nu_0 = Gamma(5/2, rate 5/2),  nu_(n+1)=T(nu_n),
    c=pi/6,  V_n=c(X_n+X_n'),
    M_n(s)=E V_n^(s/2),
    H_n(s)=[M_n(s)+M_n(1-s)]/[2(1+M_n(1))].                (1)

The parent proves the W2 contraction constant sqrt(7/12), reconstructing
BPY's fixed law

    X_*=(6/pi^2) sum_(j>=1) E_j/j^2,
    psi_*(t)=sqrt(6t)/sinh(sqrt(6t)),
    E V_*^(s/2)=2 xi(s),  V_*=c(X_*+X_*'),                 (2)

where the E_j are independent mean-one exponentials. The last equality is
BPY Proposition 1 at its specified scale, with the analytic xi completion.
It is an explicit classical import, not derived from a zero assumption.
In particular H_*=xi and |2xi(s)|<=1 on 0<=Re s<=1 by Holder between the
real moments M_*(0)=M_*(1)=1. Probability is a representation of this source,
not a statistical assumption about primes.

For laws with equal moments through order two and finite third moments,
write nu <=_3 eta when E_nu f<=E_eta f for every real C3 function on [0,infinity)
whose third derivative is nonnegative and bounded. Such a function grows at
most cubically. Define

    zeta_3(nu,eta)=sup_(||f'''||_infinity<=1) |E_nu f-E_eta f|.   (3)

The matching lower moments make the unbounded coefficients of the quadratic
Taylor polynomial irrelevant. This is an ideal metric, not quadratic W2 and
not ordinary first-order stochastic dominance.

**BOR1 (exact ordered orbit).** At every finite depth,

    nu_0 <=_3 nu_1 <=_3 ... <=_3 nu_*,
    zeta_3(nu_n,nu_*) = (4/175)(31/80)^n.                  (4)

All these laws have mean one and second moment 7/5. In addition, for n>=1,

    E X_n^(-b) <=12,  E X_*^(-b)<=12,  0<=b<=3.           (5)

**BOR2 (positive complete remainder and explicit Mellin rate).** Put
r=31/80. For every n>=1 and every s with 0<=Re s<=1,

    |M_n(s)-2xi(s)| <= (12/175)|s(s-2)(s-4)| r^n,         (6)

    |H_n(s)-xi(s)| <= (6/175) r^n *
       [ |s(s-2)(s-4)| + |(1-s)(1+s)(3+s)| +3 ].          (7)

There is also an exact positive-measure formula (19) below. The bounds retain
all probabilities, all Mellin tails, both reflected terms and normalization.
They hold on the CLOSED strip and at ALL heights. They are ABSOLUTE errors;
relative control near zeros or an unbounded-height zero certificate does not
follow. The zero-preservation target for this orbit remains open.

**BOR3 (generic gamma preservation is false for the literal map).** Start
instead with eta_0=Gamma(1,1), let eta_1=T(eta_0), and use exactly the same
pair-Mellin definition (1). H_(eta_0) has no off-central zeros in the critical
strip, but H_(eta_1) has a simple zero in a radius-10^-20 disk about the exact
Gaussian rational given in Section 6, near

    0.8720593240460351928 + 41.23914521852251227 i.         (8)

This is NOT a zero of xi, not a zero of an actual Gamma(5/2) iterate, and not
a counterexample to RH. The variance of eta_0 is one, not 2/5. The example
refutes closure of the whole zero-safe gamma starting FAMILY under T, not a
special invariant on the exact mean/variance orbit in BOR1.

## 2. A beta comparison proves the new invariant

Let W=U^-2 and let B be independent Beta(5/2,5/2). Their densities are

    w(x)=1/(2x^(3/2)) 1_[1/4,1](x),
    b(x)=(128/(3pi)) x^(3/2)(1-x)^(3/2) 1_(0,1)(x).     (9)

Their zeroth, first and second moments agree: 1,1/2,7/24. Their third moments
are respectively 31/160 and 3/16, differing by 1/160.

On [1/4,1], w(x)>b(x) iff

    x^2(1-x) < (3pi/256)^(2/3).

The cubic increases up to 2/3 and decreases thereafter. The strict rational
comparisons obtained from 3<pi<22/7 are

    (3/64)^3 < (9/256)^2,
    (66/1792)^2 < (4/27)^3.

They show exactly two crossings a,b with 1/4<a<2/3<b<1. Thus w-b has sign
pattern -,+,-,+ on the four intervals determined by 1/4,a,b.

Take any C3 f with f'''>=0. Its degree-two interpolant at those three
switches has an error with the sign of

    (x-1/4)(x-a)(x-b).

This is the repeated-Rolle interpolation remainder, valid also outside the
three nodes within [0,1]. Multiplying that error by w-b is nonnegative
pointwise. The interpolating polynomial integrates to zero against w-b,
since moments 0,1,2 agree. It follows that

    B <=_3 W.                                           (10)

This is a complete continuum sign argument, not sampling the two densities.

Take an independent G~Gamma(5, rate 5/2). Beta–gamma factorization gives
BG~Gamma(5/2,rate5/2). One direct proof changes variables from independent
Gamma(5/2,5/2) variables to their sum and ratio; the Jacobian factors their
joint density into Gamma(5,5/2) times Beta(5/2,5/2). WG has law T(nu_0).
For fixed G>0 the third derivative of f(Gx) is G^3 f'''(Gx). Integrate (10)
and use the finite third moment of G. This proves nu_0<=_3 nu_1.

If nu<=_3 eta, then T(nu)<=_3 T(eta). Replace the first independent child,
then the second, keeping the same law of the other child and U in each
comparison. For fixed y,u, the third derivative of f((x+y)/u^2) is
u^-6 f'''((x+y)/u^2), with the correct nonnegative sign. Quadratic moment
matching is preserved. Iterating proves nu_n<=_3 nu_(n+1).

The same two-replacement argument proves the ideal-metric contraction

    zeta_3(T(nu),T(eta)) <=2 E U^-6 zeta_3(nu,eta)
                           =(31/80)zeta_3(nu,eta).       (11)

This rate is distinct from the parent's W2 constant.

## 3. Passage to the fixed law and sharp metric normalization

The moment recurrence is elementary:

    a_j=E U^(-2j)=(1-2^(1-2j))/(2j-1), j>=1, a_0=1,
    m_(j,n+1)=a_j sum_(l=0)^j binom(j,l)m_(l,n)m_(j-l,n). (12)

It keeps m_1=1, m_2=7/5. For order three it gives exactly

    m_(3,n)=93/35-(24/175)(31/80)^n.                      (13)

The fixed third moment follows from (12) at stationarity (or from the
exponential series in (2)). For uniform integrability, order four has
coefficient 2a_4=127/448<1 and forcing a_4(8m_3+6m_2^2). With m_3<=93/35,

    a_4[16+8(93/35)+6(7/5)^2]=544703/78400 <8.

Since m_(4,0)<8, all fourth moments are at most eight. W2 convergence to the
fixed law, established by the parent's elementary coupling and reconstructed
in (24) below, and this fourth-moment bound permit passing expectations of
continuous functions of at most cubic growth to the limit. Thus nu_n<=_3 nu_*.

If |f'''|<=1, both x^3/6+f(x) and x^3/6-f(x) have nonnegative third derivative.
The order therefore bounds |E_*f-E_n f| by (m_3^*-m_(3,n))/6. Equality is
attained by f(x)=x^3/6. This proves the EXACT expression (4), not merely an
upper rate extrapolated from finite moments.

For t>0, -exp(-tx) has positive third derivative, so

    psi_n(t)>=psi_(n+1)(t)>=psi_*(t).                     (14)

The inequalities between successive finite n are strict: the density
interpolation in Section2 is strict for this test after every positive
scaling; the operator on Laplace transforms psi -> integral psi(t/u^2)^2 du
preserves strict inequalities at all positive t. The limit is strictly below
each finite stage by combining successive strictness with (14).

For b>0 use x^-b=Gamma(b)^-1 integral_0^infinity t^(b-1)exp(-tx)dt. Tonelli
and (14) show inverse moments are nonincreasing in n, including their
extended values. At depth one,

    X_1=G/U^2, G~Gamma(5,rate5/2),
    E X_1^-3 = (127/7)(5/2)^3/24 =15875/1344 <12.         (15)

Holder gives the same bound for 0<=b<=3. The fixed-law inequality follows
by the Laplace comparison (or by Fatou). This proves (5), including the
negative-moment control needed for complex Mellin tests near zero.

## 4. The exact positive error kernel

Define

    K_n(t)=(1/2)[E(X_*-t)_+^2-E(X_n-t)_+^2], t>=0.       (16)

It is nonnegative by nu_n<=_3 nu_*; a smooth approximation to the squared
positive part justifies applying the stated C3 definition. The complete
positive integral is

    integral_0^infinity K_n(t)dt
      =(m_3^*-m_(3,n))/6=(4/175)r^n.                     (17)

Tonelli applies to each third-moment integral before subtraction. Taylor's
formula with integral remainder, and equality of moments0,1,2, give

    E_*f-E_n f=integral_0^infinity f'''(t)K_n(t)dt        (18)

whenever f''' is bounded (and for the smoothed power tests used next).

Let p=s/2. Applying (18) twice to the two independent coordinates of
c^p(x+y)^p proves the WHOLE-source identity

  2xi(s)-M_n(s)
   = c^p p(p-1)(p-2) integral_0^infinity K_n(t)
          integral_0^infinity (t+y)^(p-3)[nu_n+nu_*](dy)dt.     (19)

For 0<=Re s<=1 all interchanges are absolutely justified by (5) and (17),
including at the real endpoints; the principal power is along t+y>0.
In particular (19) is a polynomial factor times the Mellin transform of a
FINITE POSITIVE measure: push K_n(t)(t+y)^-3 dt[nu_n+nu_*](dy) forward by
v=c(t+y). Its total mass is at most24(4/175)r^n.

The source on the right is exact, but involves the fixed law as well as the
current iterate. It is an analytical identity, not a finite producer with an
unknown fixed-law oracle silently treated as computed. More importantly, a
positive measure can have a complex Mellin transform with zeros and rotating
phase. Equation(19) does NOT establish zero-preservation by positive addition.

## 5. Complete complex error with the improved geometric rate

Put a=Re p in [0,1/2]. For Y of law nu_n or nu_*, the test

    g_Y(x)=E[c(x+Y)]^p

has bounded third derivative on x>=0, with

    sup |g_Y'''(x)|
       <=c^a |p(p-1)(p-2)| E Y^(a-3)
       <=12 |p(p-1)(p-2)|.                               (20)

It also has at most cubic growth. For a complex-valued test, rotate its
expectation discrepancy and take its real part; the bound defining zeta_3
applies without an additional real/imaginary factor. Replacing both marginals
and using (4) gives

    |2xi(s)-M_n(s)|
      <=24 |p(p-1)(p-2)| (4/175)r^n,

which is exactly (6). This also follows directly from (19).

Let Delta_n(s)=M_n(s)-2xi(s). Using reflection xi(1-s)=xi(s), the subtraction
of the two NORMALIZED transforms is exactly

    H_n(s)-xi(s)
      =[Delta_n(s)+Delta_n(1-s)-2xi(s)Delta_n(1)]
                                      /[2(1+M_n(1))].    (21)

Here M_n(1)>0 and |2xi(s)|<=1. Equation(6) at s=1 has cubic factor3.
Bounding the denominator by2 proves (7). There is no dropped normalizing
error. Notice also that for real 0<s<1, (19) proves M_n(s)<2xi(s): both
negative factors p-1,p-2 give a positive product. Monotonicity of H_n itself
is NOT asserted, since its denominator changes.

The new bound improves the parent's Holder/W2 conversion for THIS prescribed
orbit and is uniform on the entire closed strip with a cubic height factor.
It does not compare |H_n-xi| to |xi|, and no Rouché conclusion on an unbounded
family of contours is inferred.

## 6. Test the hoped-for zero invariant on a different literal gamma seed

A proof that EVERY zero-safe gamma seed remains zero-safe after T would have
closed the proposed induction too cheaply. Here it is rigorously falsified.
The prescribed nu_n is not changed; this section deliberately uses eta_0=Exp(1).

### 6.1 The input really is zero-safe on the whole strip

For eta_0, let f(s)=(pi/6)^(s/2)Gamma(2+s/2). The harmless positive factor
Gamma(2) is1. Zeros of H_(eta_0) are zeros of f(s)+f(1-s).

The classical digamma integral on Re z=a>0 gives

    |psi(z)-log z+1/(2z)|<=1/(12a^2).                    (22)

For reference its remainder is minus integral e^(-zt)[(1/2)coth(t/2)-1/t]dt;
the bracket lies between0 and t/12. Those bounds follow by differentiating
x cosh x-sinh x and (1+x^2/3)sinh x-x cosh x.

For 0<=sigma<=1 and |t|<=4, integrate log(pi/6)+Re psi(2+sigma/2+iu)
over u from0 to t/2. Since a in[2,5/2], |u|<=2,

    -13/24 < arg f(sigma+it) <243/168<3/2<pi/2

for nonnegative t, and conjugate bounds hold for negative t. One obtains
the upper constant from (pi/6)sqrt((5/2)^2+4)<143/84, log v<=v-1,
and (22); the lower bound uses (pi/6)a>1. Both reflected terms have positive
real part, so no zero occurs in this closed rectangle.

For |t|>=4, differentiation gives

 d/dsigma log|f(sigma+it)/f(1-sigma-it)|
  >=log(pi/3)+(1/2)log2-1/4-1/48 >1/16.

Use log2>2/3 and pi>3 in the last step. The modulus ratio is1 at sigma=1/2;
therefore it cannot equal the modulus of -1 off that line. This proves the
input's whole-strip property without any numerical zero census.

### 6.2 The first output and its exact compact mixing law

Under the SAME map eta_1=T(eta_0), X=G/U^2 with G~Gamma(2,rate1).
For two independent output copies, write G_1+G_2=G_4~Gamma(4,1) and
B=G_1/(G_1+G_2)~Beta(2,2), independent of G_4,U,V. Consequently

    M_(eta_1)(s)=(pi/6)^(s/2) Gamma(4+s/2)/6 * A(s),
    A(s)=E W^(s/2), W=B/U^2+(1-B)/V^2 in[1/4,1].        (23)

This is the actual one-step distribution, not an empirical discretization.
Define G(s)=M_(eta_1)(s)+M_(eta_1)(1-s). Its zeros are those of the normalized
H_(eta_1), whose denominator is a fixed positive real number.

The certified exact Gaussian-rational center is

real:
0.8720593240460351927678950449864720764922472047284135048292993961077024803759264272174986835
imaginary:
41.239145218522512266175746388258629308518291094194602398581416957401708987395360042877048938

With r0=10^-20, the disk |s-s_c|<r0 lies entirely in 1/2<Re s<1.
The complete directed computation proves

    |G(s_c)|<10^-48,
    Re G'(s_c)>8*10^-13,
    sup_disk |G''|<1000.

Therefore |G(s_c)|+500r0^2<|G'(s_c)|r0. Rouché's theorem, comparing with
G'(s_c)(s-s_c), proves exactly ONE zero counted with multiplicity in the disk.
It is simple. Reflection and conjugation give its partners. The certificate
makes no assertion about other zeros or a complete zero count.

### 6.3 Complete mixing-series remainder, without three-dimensional quadrature

Put Z=8W/5-1, so |Z|<=3/5. For j>=0 its raw W moment is rational:

 mu_j=6/[(j+1)(j+2)(j+3)]
        * sum_(l=0)^j (l+1)(j-l+1) a_l a_(j-l),
 a_l=E U^(-2l).

Indeed expand W^j and integrate each B^l(1-B)^(j-l) against the beta density.
Then eta_j=E Z^j is the exact binomial sum of these mu_l. The code reconstructs
EVERY coefficient through j=600 from rational arithmetic, independently of
any scout-produced moment file.

For p=s/2,

    A(s)=(5/8)^p sum_(j>=0) binom(p,j) eta_j.

On the z-circle |z|=4/5 and on either s-disk of radius1 around s_c or1-s_c,
we have |1+z| in[1/5,9/5], -1/2<Re p<1, |Im p|<22 and
|arg(1+z)|<2. Thus |(1+z)^p|<5*3^44 and |(5/8)^p|<2.
Cauchy bounds each binomial coefficient by 5*3^44*(5/4)^j.
Since |eta_j|<= (3/5)^j, the ENTIRE omitted series and its derivative in s
are each bounded by

    error =100*3^50*(3/4)^601.

The derivative assertion applies Cauchy in the radius-one s-disk to the
already bounded analytic omitted series. Both reflection disks are covered.
Nothing past degree600 is set to zero without a bound.

### 6.4 Gamma factors and primitive interval arithmetic

The evaluator uses integer/Fraction arithmetic and outward dyadic intervals
with denominator2^512. Final output rectangles are widened to2^-256.
Pi is reconstructed with Machin's formula. Real logarithms use a range-reduced
atanh series; exponentials and sine/cosine use range-reduced Taylor series
with explicit complete remainders. Square roots use integer-square-root
brackets, and arctangents use half-angle reduction and their alternating
series. Every complex logarithm is evaluated in Re z>0; no argument branch
crossing occurs.

For logGamma and psi shift the argument by64 and retain Bernoulli terms
k=1,...,23. DLMF5.11(ii) bounds the two remainders after k=m-1 by the first
omitted term times sec^(2m)(arg z/2), respectively sec^(2m+1)(arg z/2).
On Re z=a>0, cos(arg z)<=cos^2(arg z/2), so these are bounded by

    |B_(2m)|/[2m(2m-1)a^(2m-1)],
    |B_(2m)|/[2m a^(2m)],             m=24.

This follows, for example, by replacing |z|^-j with a^-j cos^j(arg z) and
checking the remaining power of cos(arg z/2) is nonnegative. The bound is
valid for the full complex remainders, not just on the positive real axis.
The64 recurrence factors are evaluated and subtracted with directed logs
and reciprocals. Gamma normalization uses the same reconstructed pi.

The code separately encloses the complex value and derivative of (23),
including all series and gamma errors. It does not import mpmath, scipy,
a zeta routine, an incomplete-gamma routine or a supplied numerical root
as an accepting primitive. The rational center WAS chosen by a non-directed
scout; the defining-function reconstruction, not that scout, certifies it.

Finally, on 1/10<=Re s<=9/10, let V=c(X+X'). Here E X^2=7/4 and
E V^2=(pi/6)^2(11/2)<3. For 0<v<=1,

    v^(sigma/2)(log v)^2 <1600,

using sigma/2>=1/20 and maximizing e^(-ar)r^2; for v>=1 the expression
is <=v^2. Differentiating the Mellin integral gives each |M''|<1603/4.
The reflected sum has |G''|<1603/2<1000 throughout the disk. This is a
complete global expectation bound, not a sampled second derivative.

## 7. The full-problem implication and the still open step

For clarity, the parent W2 argument remains independent of complex zeros.
Couple equal-mean X,Y optimally, take two independent copies and a common U:

    E|T(X)-T(Y)|^2 <=2 E U^-4 E|X-Y|^2=(7/12)W2(nu,eta)^2. (24)

The complete normalized space is closed in W2. Laplace uniqueness and the
explicit sinh identity identify its unique fixed law as (2). BOR1 adds a
source-specific order invariant and replaces the slower Holder error route
by (6)-(7). None assumes xi has only critical-line zeros.

If H_n is zero-free in both open half-strips at an UNBOUNDED sequence of
depths, (7) gives locally uniform convergence there to the nonzero function
xi; Hurwitz then proves RH. There is no remaining approximation or source
identification premise after that zero assertion. Conversely, convergence
and order alone do not establish the assertion. Positive Peano remainders
may have oscillating complex Mellin phase.

BOR3 means one cannot prove it by claiming preservation for all k>=1 gamma
starting laws. That broad rule is false at k=1. It leaves open the particular
k=5/2 orbit, which has a different variance and the special third-order
comparison in Section2. An invariant must exploit that distinction or use a
different source-faithful zero-safe approximation class.

This packet does NOT claim: all-depth zero preservation; any off-line xi zero;
an all-order Lee–Yang realization; a lower bound for xi on an unbounded
contour; independent acceptance of BSR26; or a completed RH proof.
