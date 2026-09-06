# A positive extension of the actual arithmetic kernel on a full length-one window

Status: PROPOSED COMPUTER-ASSISTED THEOREM; independent proof and code review required.
RH IS NOT PROVED. The sign is established on every interval of length at most ONE,
not on an unbounded sequence of support lengths. There are NO moment constraints
on the tests in the principal theorem. All complex cross terms are retained.
Date: 2026-09-06. Local names WP1--WP5 are not canonical claim identifiers.
Parent research: PR #803 at 4370ed19eb7b2630602740468cd9ecbaa870d848.
Arithmetic source: #792 at 465cb28ed8cbfa1bb071d9a85eeda9890decfe6b.

The earlier packet justified a convergent effective-Schur search but supplied
no actual positive lower certificate. This packet proves a sign instead: a
finite rational positive extension, with an independently bounded infinite
Fourier tail, establishes the full-source length-one inequality. Its proof
does NOT assume RH, a zero census, a sampled continuum sign, or positivity of
an uncomputed Schur matrix. Classical local Weil positivity and positive
extension theory have prior art; no priority or largest-window claim is made.

## 1. The literal source and the theorem

Set b=3/2, c=1/2, a=3/4 and

    C_b=(1-gamma_E-log(2pi))/3,
    P2=-zeta'(2)/zeta(2)=sum_(n>=2) Lambda(n)/n^2,
    alpha_j=2j+1/2,
    S_G(x)=sum_(j>=1) exp(-alpha_j x)/(alpha_j^2-b^2).

The exact arithmetic source, extended evenly, is

    W(x)= exp(x/2)/2+C_b exp(-bx)+S_G(x)-(P2/b)cosh(bx)
          +(1/b)sum_(2<=n<=exp(x)) Lambda(n)/sqrt(n)
                                         sinh(b(x-log n)), x>=0.    (1)

This is the source of the parent PRs, not a raw prime cutoff. In particular
P2 contains every omitted prime power. The series for S_G converges uniformly
on [0,infinity), since its coefficients are O(j^-2). The source is continuous.
For x<=1 only n=2 is activated: 2<e<3. Put

    d=log 2, q=log 2/sqrt(2),
    F(x)= exp(cx)/2+C_b exp(-bx)-(P2/b)cosh(bx)
                         +(q/b)sinh(b(x-d))1_(x>=d).                (2)

Thus W(x)=S_G(x)+F(x) exactly on [0,1], including the prime cusp. The
contribution at d is zero but the derivative jump q is NOT dropped.

For h in complex L2(0,1), define

    Q(h)=b int_0^1 int_0^1 conjugate(h(t))W(t-u)h(u)du dt,
    hhat(w)=int_0^1 h(t)exp(-iwt)dt,
    w_n=n*pi/2, delta=2^-35.

**WP1 (full-source positivity).**

    Q(h) >= (3 delta/4) sum_(n in Z) |hhat(w_n)|^2/(1+w_n^2) >0
                                                               (3)

for every nonzero h in L2(0,1). The final sum is a periodic H^-1 norm,
not an L2 norm. Formula (3) is compatible with compactness of the original
operator. It applies to arbitrary signs and arbitrary complex functions.

For T(t,u)=b exp(-a(t+u))W(t-u), substitute h(t)=exp(-at)f(t).
The same positivity holds for every nonzero f supported in ANY interval of
length at most one in the half-line. Translation changes the damping and
Fourier phases correctly; it does not supply a theorem at larger diameter.

## 2. The certificate: cosine atoms plus a periodic remainder

Everything in certificate.json is an exact rational string. There are twenty
positive rational frequencies lambda_j in (0,100), twenty NONNEGATIVE rational
weights w_j (zero weights are allowed), and 64 rational extension values v_k.
The frequencies were suggested by noncertifying zero reconnaissance. They are
not asserted to be zeros; the acceptance proof treats them as arbitrary fixed
rational numbers and never evaluates zeta at them.

Put x_k=1+k/64, 0<=k<=64. Define F_ext on [0,2] to equal F on [0,1], and
to be affine on each [x_k,x_(k+1)], with

    F_ext(x_0)=F(1) EXACTLY,   F_ext(x_k)=v_k for k>=1.

The first endpoint is evaluated from the arithmetic source, not taken from
a rounded optimizer output. Define on [0,2]

    R(x)=S_G(x)+F_ext(x)-sum_j w_j cos(lambda_j x).                  (4)

Extend R evenly and 4-periodically to the real line. It is continuous at every
join, including +/-2. Let

    I_n=int_0^2 R(x)cos(w_n x)dx,  a_n=I_n/2.                      (5)

The exact finite and infinite certificates in Sections 3--5 give

    I_0>delta,
    w_n^2 I_n>delta                  (1<=n<=2048),
    w_n^2 I_n>2/5                    (n>=2049).                     (6)

Consequently a_n>=delta/[2(1+w_n^2)] for every n>=0.

The Fourier coefficients are O(log(n+2)/(n+1)^2). For S_G, split its positive
coefficient sum at j=n to obtain this bound directly. For F_ext, integrate
by parts twice on its finitely many smooth pieces, retaining the cusp jumps.
The periodicized cosine atoms have coefficients O(n^-2). Therefore the
Fourier series is absolutely convergent and represents the continuous R:

    R(x)=a_0+2 sum_(n>=1) a_n cos(w_n x).                           (7)

Define the globally positive-definite extension

    K(x)=R(x)+sum_j w_j cos(lambda_j x).                            (8)

It satisfies K(x)=W(x) for |x|<=1. Its positive Fourier expansion gives

    Q(h)=b sum_(n in Z) a_|n| |hhat(w_n)|^2
              +(b/2)sum_j w_j(|hhat(lambda_j)|^2+|hhat(-lambda_j)|^2).

Termwise integration is justified by uniform absolute convergence and h in
L1(0,1). Formula (6) proves (3). If the sum in (3) vanishes, every Fourier
coefficient of the zero extension of h to a circle of length four vanishes.
Completeness of the ordinary Fourier basis implies h=0. This is a proof for
all L2 functions, not a check of a finite test basis.

## 3. Closed coefficient formulas; no numerical quadrature

All integrals used in (5) are evaluated by elementary formulas and one
explicitly enclosed digamma expression. Let w>=0. For any real k!=0,

    E(k,l,w)=[exp(kl)(k cos(wl)+w sin(wl))-k]/(k^2+w^2).             (9)

This equals int_0^l exp(kx)cos(wx)dx. In particular the integral of F is

    E(c,1,w)/2+C_b E(-b,1,w)
       -P2/(2b)[E(b,1,w)+E(-b,1,w)]
       +q/(2b){exp(-bd)[E(b,1,w)-E(b,d,w)]
                  -exp(bd)[E(-b,1,w)-E(-b,d,w)]}.                  (10)

Let m_k=64(F_ext(x_(k+1))-F_ext(x_k)). For n>0 the extension contributes

    w_n^2 int_1^2 F_ext(x)cos(w_n x)dx
      =-F(1)w_n sin(w_n)+m_63(-1)^n-m_0 cos(w_n)
          -sum_(k=1)^63 (m_k-m_(k-1))cos(w_n x_k).                (11)

For n=0 its integral is sum_(k=0)^63 [F_ext(x_k)+F_ext(x_(k+1))]/128.
The potentially large 1/w boundary terms in (10)--(11) cancel exactly;
directed interval arithmetic retains their cancellation rather than taking
absolute values separately.

A cosine atom has the exact coefficient

    int_0^2 cos(lambda x)cos(w_n x)dx
         =(-1)^n lambda sin(2lambda)/(lambda^2-w_n^2).              (12)

No denominator encloses zero for the fixed witness; a violation is rejected.

For the full gamma series, partial fractions and the digamma series give

    int_0^2 S_G(x)cos(w_n x)dx
      =[2 Re psi(5/4+i w_n/2)+2gamma_E+2log2-1]
                                           /[4(b^2+w_n^2)]
        -(-1)^n sum_(j>=1)
           alpha_j exp(-2alpha_j)
                    /[(alpha_j^2-b^2)(alpha_j^2+w_n^2)].           (13)

Indeed alpha/(alpha^2-b^2) and alpha/(alpha^2+w^2) differ by four
harmonic reciprocals. The special values psi(1/2)=-gamma_E-2log2 and
psi(2)=1-gamma_E give the displayed numerator. This also verifies the n=0
normalization. The tail after j=32 in the second sum has absolute value
less than 2^-132: its rational coefficient is at most one, and

    sum_(j>=33) exp(-(4j+1)) < (16/15)2^-133 <2^-132.

The full logarithmic gamma tail has therefore been integrated, not omitted.

## 4. Primitive enclosure contract and all 2049 finite inequalities

The accepting implementation uses only Python integer and Fraction arithmetic.
Every interval endpoint is an integer multiple of 2^-192. Each arithmetic
operation rounds its lower endpoint down and upper endpoint up. Floating point,
NumPy/SciPy, numerical zeta, a zero table and the discovery optimizer are absent
from the acceptance path. Caching retains exact endpoint pairs only.

The elementary enclosures are reconstructed as follows.

* pi=16 atan(1/5)-4 atan(1/239), using 160 alternating/geometric terms and
  an explicit absolute geometric tail.
* log x: reduce by exact powers of two to 1<=x<=2; use
  log x=2 sum_(k>=0) z^(2k+1)/(2k+1), z=(x-1)/(x+1), through k=79.
  The tail is at most 2*(1/3)^161/[161*(1-1/9)]. Endpoint monotonicity
  handles interval input, including power-of-two crossings.
* exp x: halve a nonnegative argument to [0,1/2], use the degree-89 Taylor
  polynomial with error <=2*(1/2)^90/90!, then square. Inversion handles
  negative arguments. For x<=-128, [0,2^-128] is a valid cheaper enclosure.
* sin and cos: subtract an integer multiple of pi/2, with the interval for
  pi retained, and reject unless the reduced interval lies in [-1,1]. The
  degree-78/79 Taylor sums have absolute error <=1/80!. Quadrant identities
  restore the requested value. The integer choice need not itself be exact:
  the trigonometric identity holds for every integer chosen.

For psi(z), shift z to z+64, use the expansion through B_38,

    psi(Z)=log Z-1/(2Z)-sum_(k=1)^19 B_(2k)/(2k Z^(2k))+error,

and subtract sum_(k=0)^63 1/(z+k). We use the classical explicit remainder
bound from DLMF 5.11(ii). For Re Z>0, its secant factor is below 2^21, so

    |error| <= 2^21 |B_40|/[40 (Re Z)^40].                         (14)

Only Re log Z=log((Re Z)^2+(Im Z)^2)/2 is needed. Bernoulli numbers through
40 are constructed by their exact rational recurrence. gamma_E=-psi(1).
The use of the DLMF remainder theorem is an analytic input, not a floating
point assertion that an asymptotic series is accurate.

P2 is independently enclosed at its safe real arithmetic point. At N=64,
Euler--Maclaurin through B_40 gives for zeta'(2) the finite expression

    -sum_(n=1)^63 log(n)/n^2 -(log N+1)/N-log N/(2N^2)
       +sum_(k=1)^20 B_(2k) N^(-2k-1) [H_(2k)-1-log N].           (15)

On |s-2|=1/4, the remainder in zeta(s) is bounded by

    E=|B_40|/40! * product_(j=0)^39 (9/4+j) / (40 N^40).

This follows from the periodic-Bernoulli integral remainder, Re s>=7/4,
and sup |B_40({x})|<=|B_40|. Cauchy's derivative inequality gives error
<=4E in (15). Finally P2=-6zeta'(2)/pi^2. The Euler product is used only at
Re s=2, where absolute convergence is classical. No conjectural prime bound
is needed. The exact source geometry 0<log2<1 and 2<e<3 is also checked.

The driver evaluates (10)--(13) for n=0,...,2048 and rejects unless the
lower endpoint of I_0 or w_n^2 I_n is strictly greater than delta. Every
entry is checked, not a mesh in n or in t. The worst finite lower bound
is at n=149, and is greater than 9.36*10^-11. The retained rational lower
endpoint and all-coefficient digest are in result.json; the displayed
rounded number is not the accepting threshold. delta=2^-35 is smaller.

## 5. Every remaining Fourier coefficient: a finite residue-class proof

There is no unbounded extrapolation from Section 4. The following estimates
cover all n>=2049 simultaneously.

Integrating F by parts on [0,1] gives

    w^2 int_0^1 F cos(wx)
      =F(1)w sin w+F'(1)cos w-F'(0)
          -q cos(wd)-int_0^1 F''_reg(x)cos(wx)dx.                 (16)

Here

    F'(0)=c/2-b C_b,
    F'(1)=c exp(c)/2-b C_b exp(-b)-P2 sinh b+q cosh(b(1-d)).

The regular F'' is continuous at d; its value from the activated sinh term
is zero there. Another integration by parts therefore bounds the last
integral in (16) by E_F/w, where the explicit positive upper bound is

    E_F = c^2 exp(c)/2+|C_b|b^2 exp(-b)+P2 b cosh b
             +qb sinh(b(1-d))
          +c^2(exp(c)-1)/2+|C_b|b^2(1-exp(-b))
             +P2 b(cosh b-1)+qb sinh(b(1-d)).                      (17)

The atom contribution to -w^2 I_n differs from
(-1)^n sum_j w_j lambda_j sin(2lambda_j) by at most

    sum_j w_j lambda_j^3/(w_0^2-lambda_j^2),
    w_0=3*2049/2 < w_n.                                          (18)

All denominators are positive, since lambda_j<100<w_0.

Combining (11),(16),(18), all the remaining boundary/slope phases have
period 256 in n. Define for r=0,...,255

    B_r=[F'(1)-m_0]cos(r*pi/2)-F'(0)+m_63(-1)^r
          -sum_(k=1)^63 (m_k-m_(k-1))cos(r*pi(64+k)/128)
          +(-1)^r sum_j w_j lambda_j sin(2lambda_j).               (19)

The driver encloses every B_r and takes the least lower endpoint beta.
It obtains beta>-2.759. This replaces a gross absolute total-variation
bound, which would lose the oscillatory cancellation and be too weak.

The gamma part is positive term by term. Keeping ONLY j<=1024 is a valid
LOWER bound for it, and for every n>=2049 it is at least the exact rational

    G_0=sum_(j=1)^1024 alpha_j/(alpha_j^2-b^2)
                *w_0^2/(alpha_j^2+w_0^2)*(1-2^(-(4j+1))).          (20)

This uses monotonicity of w^2/(alpha^2+w^2), pi>3, and e>2. The remaining
gamma terms are discarded only on the positive lower-bound side. The sum
is accumulated with outward rounding; there is no exact-rational sum with
an uncontrolled numerical approximation afterward.

Consequently, for EVERY n>=2049,

    w_n^2 I_n >=G_0+beta-q-E_F/w_0
                         -sum_j w_j lambda_j^3/(w_0^2-lambda_j^2).

The lower endpoint is greater than 0.4883, and the accepting comparison is
the more conservative exact inequality >2/5. This proves the third line
of (6) for all remaining n. The irrational prime phase cos(w_n log2) has
been bounded by one here, not presumed periodic with the spline grid.

Sections 2--5 complete WP1.

## 6. WP2: an explicit positive lower bound for the complete effective S_1

This consequence answers the length-one Schur question without forming an
unvalidated 104-by-104 quadrature matrix.

Take the exact parent exceptional basis on (0,1):

    e_1=exp(-t/2), e_2=exp(t/2), e_3=cosh(3t/2),
    e_(3+j)=sin(j*pi*t), 1<=j<=101.

It is linearly independent. Let G_ij=int_0^1 e_i e_j. Extend e_i to a
4-periodic H1 function Psi_i as follows: equal e_i on [0,1]; interpolate
linearly from 0 to e_i(0) on [-1,0], and from e_i(1) to 0 on [1,2]; equal
zero on [2,3]. Endpoint values at -1 and3 agree. Its H1 Gram is EXACTLY

    H_ij=int_0^1 (e_i e_j+e_i' e_j')
                      +(4/3)[e_i(0)e_j(0)+e_i(1)e_j(1)].         (21)

Both G and H are positive definite elementary Gram matrices. Their entries
have exact elementary integrals; no unknown zeta-zero data occurs.

For h=e_u-v, with e_u=sum_i u_i e_i and v in the parent's V=E^perp,

    <Psi_i,h>=<e_i,e_u>=(Gu)_i.

On a circle of length four, Parseval and Cauchy--Schwarz give, simultaneously
for arbitrary linear combinations of the Psi_i,

    sum_(n in Z) |hhat(w_n)|^2/(1+w_n^2)
                               >=4 u* G H^(-1) G u.              (22)

For completeness, the pairing has Fourier factor1/4 and
||Psi||_H1^2=(1/4)sum(1+w_n^2)|Psihat(w_n)|^2. Optimizing the resulting
finite-dimensional dual inequality proves (22). These factors fix the
normalization in the next bound.

Taking the infimum over v in V in WP1 yields

    S_1 >= 3 delta G H^(-1) G >0.                                (23)

The parent defines u*S_1u as exactly this infimum, including every infinite
positive-sector coupling. No assumption that the infimum is attained in L2
is necessary. This proves positive definiteness of the ACTUAL full effective
matrix at length one, without RH and without computing its individual
entries. It also implies positivity for all shorter windows by restriction.
It is NOT an L2 eigenvalue gap for the original compact T_1.

## 7. WP3: why the construction does not finish unbounded support

The positive-definite K in (8) is globally defined, but K=W is proved only
on [-1,1]. The extension endpoint values are freely chosen rational values,
not actual further prime data. In particular the first right derivative
of F_ext at1 is m_0, generally not F'(1). The driver records this difference
and can verify it is nonzero. W is smooth near1 because1 is not a prime-log
knot. Therefore K is NOT the entire arithmetic kernel W.

An arbitrary global positive extension of a local kernel is not a proof
that a separately prescribed global continuation is positive. As an exact
logical countercontrol, start with any positive-definite K, subtract a
large even continuous bump supported outside[-1,1], and make its value at
some x_0>1 less than -K(0). It still agrees on[-1,1], but its two-point
matrix at0,x_0 is indefinite. This is a synthetic continuation, not zeta.

The attempted larger-window fits at9/8,5/4,3/2 were NOT certified. The
binary64 solver reported an extremely small margin for9/8, even a slightly
negative nominal margin at5/4, and infeasibility for the selected3/2 ansatz.
These outcomes neither refute source positivity nor establish it. They
show why solver status, nominal margins, and a fixed certificate size must
not be extrapolated. Only the exact length-one witness is published as a
sign certificate.

For all-window closure one still needs actual positivity for lengths in an
unbounded predetermined sequence, for example S_L>=0 for every integer L.
WP1/WP2 provide the first such integer window, not an induction step. The
new practical avenue is to construct finite positive spectral extensions
that match increasingly long stretches of the SAME arithmetic W, with
complete signed coupling and tail bounds at each stage. No theorem here
asserts that these extensions can be constructed at all lengths.

## 8. Scope, trust and replication

The theorem is conditional on the correctness of the explicit finite
interval calculation in the standard computer-assisted sense, with its
full mathematical coverage proof above. It is not an independently
kernel-checked theorem. Review the dyadic rounding primitives, the psi and
Euler--Maclaurin remainders, the derivative-jump signs, the finite residue
period, and the Fourier/Sobolev factors.

Ordinary and optimized Python give identical result.json and coefficient
digests. The intervals are rebuilt from primitive constants. Discovery
used floating point linear programming and approximate zero ordinates only
to choose fixed rational witness parameters. Discovery is not imported by
the checker and its success status is not accepted as evidence.

No original research or review source is modified. No RH proof, zero
verification record, public priority, larger-window sign, or Lean build is
claimed. The preceding operator-core and convergence theorems remain
proposed at their frozen versions; WP1's positivity proof is independent
of them, and WP2 uses only the exact effective-form definition.
