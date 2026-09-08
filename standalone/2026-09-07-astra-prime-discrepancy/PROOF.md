# PDS26: the complete critical entropy reduces to a linear prime discrepancy

Status: PROPOSED COMPONENT PROOFS; independent mathematical review pending.
The full RH proof is NOT obtained. The subpower estimate in Section 7 is OPEN.
Date: 2026-09-07. Author: Astra. This is research, not a reviewer acceptance.
Source: PR811 at 9e05a2b345369cd16c0973c531650eb37727445e.

## 1. Fixed objects and main conclusions

All primes are ordinary primes. Write L=log X, X>=2, and retain the actual
forward completion from the parent:

    A_X(s)=exp(-gamma) exp(Ein((s-1)L))
                 product_(p<=X)(1-p^-s)^(-1)/(L s^2),
    Ein(w)=integral_0^w (1-exp(-u))/u du,
    dmu(y)=dy/[pi(1+y^2)],
    U_X(y)=log|A_X(1/2+iy)|,
    E(X)=integral (U_X)_+ dmu.                         (1)

The product cutoff is on PRIME BASES, not on prime powers. Define the complex
linear discrepancy and the full higher-power term

    C_X(y)=sum_(p<=X) p^(-1/2-iy)
                     -integral_2^X x^(-1/2-iy)/log x dx,
    V_X(y)=sum_(p<=X) sum_(k>=2) p^(-k/2-iky)/k.       (2)

The expression p^(-k/2-iky) means exp[-(k/2+iky)log p]. In particular the
frequency of the k-th harmonic is k log p. Every k>=2 is retained.
Let ||.||_(r,mu) mean the ordinary Lr norm in this probability measure.

**PDS26.T1 (all higher powers are uniformly controlled).** V_X converges in
L2(mu) to V_infinity. For every real X>=2,

    ||V_X||_(2,mu)<14,
    ||V_infinity-V_X||_(2,mu)
             <=8/sqrt(log X)+4/sqrt X.                (3)

This theorem uses only an elementary Chebyshev bound, not PNT or RH. At y=0
V_X diverges as X increases, so no uniform pointwise convergence is asserted.
A failure at a measure-zero frequency is compatible with (3). Euler's harmonic-prime divergence, proved by comparing the harmonic sum through X
with product_(p<=X)(1-1/p)^(-1), explains that exceptional value.

**PDS26.T2 (uniform-error linearization of the entropy).** For every X>=2,

    |2E(X)-||Re C_X||_(1,mu)|<32.                     (4)

Thus the nonlinear feedback of EFB26 can be bypassed for the sign/growth
question. The positive part and the original physical measure are not
replaced by an independent-prime model.

For the ordinary weighted prime-counting discrepancy put

    R(x)=sum_(p<=x) sqrt p - integral_2^x sqrt u/log u du,
    I(X)=integral_2^X R(x)^2/x^3 dx + R(X)^2/(2X^2),
    c_X=sum_(p<=X) p^-3/2 - integral_2^X x^-3/2/log x dx.  (5)

**PDS26.T3 (exact complete one-state norm).**

    ||C_X||_(2,mu)^2=2I(X),
    ||Re C_X||_(2,mu)^2=I(X)+c_X^2/2,
    |c_X|<5,
    E(X)<16+(1/2)sqrt(I(X)+25/2).                    (6)

The endpoint R(X)^2/(2X^2) is the ENTIRE infinite future of a stopped
first-order filter. It is not an omitted or asymptotic tail.
All cross terms, including prime/continuum and continuum/continuum, occur
in (6). I(X) is not the diagonal of a prime Gram matrix.

The remaining subpower bound for (4), or the sufficient one for I(X), is not
proved. Sections 6-7 explain the available conditional/unconditional estimates.
The elementary norm and Fourier arguments below are not claimed new in general;
the contribution is their source-specific combination and the complete bounds.

## 2. Elementary prime bounds needed for the infinite higher-power tail

Let theta(x)=sum_(p<=x)log p. At dyadic n=2^j, the product of primes in
(n/2,n] divides binom(n,n/2), which is at most 2^n. Hence

    theta(2^k)<=sum_(j=1)^k 2^j log2<2^(k+1)log2.

For 2^(k-1)<x<=2^k this is <4x log2<3x. The endpoint x=2^(k-1) is handled
by the previous dyadic interval; theta(x)<3x holds for all x>=2.
Splitting primes at sqrt x gives

    pi(x)<=sqrt x+2theta(x)/log x<7x/log x<8x/log x,   (7)

because (log x)/sqrt x<=2/e<1. These intentionally coarse constants avoid
any finite numerical prime-counting input.

Partial summation now yields, for P>=2,

    sum_(p>P) 1/(p log p)
       <=8[1/log P+1/(2log^2 P)]<14/log P.           (8)

Indeed the negative lower boundary term can be discarded, the boundary at
infinity vanishes, and the remaining integral is
8 integral_P^infinity [1/(x log^2 x)+1/(x log^3 x)]dx.
Use log2>2/3 for the last inequality. A prime exactly at P is excluded here.

## 3. Proof of the complete higher-power theorem

The exact Cauchy Fourier identity is

    integral exp(-iy u)dmu(y)=exp(-|u|).             (9)

It follows by a contour integral, or by Fourier inversion of exp(-|u|).
No equidistribution or prime-phase independence is involved.
First consider a finite block of SQUARE harmonics,

    B_(P,Y)(y)=(1/2)sum_(P<p<=Y) p^-1 exp(-2iy log p).

Its exact physical norm is

    ||B_(P,Y)||^2
      =(1/4)sum_(P<p,q<=Y) (pq)^-1[min(p,q)/max(p,q)]^2
      =(1/4)sum_(P<p<=Y)p^-2
       +(1/2)sum_(P<q<=Y)q^-3 sum_(P<p<q)p.         (10)

The primes in the outer off-diagonal sum are q; its inner sum has strict p<q.
By (7), sum_(p<q)p<=q pi(q)<8q^2/log q. Also
sum_(p>P)p^-2<=sum_(n>P)n^-2<=1/(P-1). Therefore

    ||B_(P,Y)||^2
       <1/[4(P-1)]+4 sum_(q>P)1/(q log q)
       <(225/4)/log P<64/log P.                    (11)

Here log P<=P-1 was used. The bound is uniform in Y. Applying it with P
equal to the smaller cutoff proves the square series is Cauchy in L2(mu).
Its infinite tail norm is at most 8/sqrt(log P). The single p=2 term has
norm 1/4. Thus every square partial sum has norm <11, since
1/4+8/sqrt(log2)<1/4+sqrt(96)<11.

For k>=3, the COMPLETE double series converges absolutely and uniformly in y:

    sum_p sum_(k>=3) p^-k/2/k
       <=(2+sqrt2)/3 sum_(n>=2)n^-3/2
       <=2(2+sqrt2)/3<3.                            (12)

At bases p>X the same bound and an integral comparison give

    sum_(p>X,k>=3)p^-k/2/k
       <=[2sqrt2(2+sqrt2)/3]/sqrt X<4/sqrt X.       (13)

Use floor X>=X/2 when making the integer comparison. Equations (11)-(13)
prove (3), including all higher powers and the entire frequency line.
A prime-base tail is meant in (3); no hard prime-power cutoff is substituted.

### Optional sharper asymptotic; this paragraph imports ordinary PNT

Under the classical PNT (an unconditional imported theorem),

    (log X)||V_infinity-V_X||_(2,mu)^2 ->1/4,
    (log X)||Re(V_infinity-V_X)||_(2,mu)^2 ->1/8.     (14)

Here is the full asymptotic calculation. PNT and partial summation give
S(q-):=sum_(p<q)p~q^2/(2log q) and
sum_(q>X)1/(q log q)~1/log X, uniformly in the required tails. In (10),
the diagonal is O(1/X). The subtraction S(X)sum_(q>X)q^-3 is O(1/log^2 X),
by (7) and partial summation. The remaining term is
(1/2)sum_(q>X)q^-3 S(q-)~1/(4log X).
The k>=3 tail is O(X^-1/2) in norm, so its square and its cross term are
negligible after multiplying by log X. For the real part use

    ||Re f||^2=(||f||^2+Re integral f^2 dmu)/2.

All frequencies here are positive. The last integral is the square of the
safe value sum_(p>X,k>=2)p^-3k/2/k=O(X^-2), by (9) and absolute convergence
at that safe exponent. It is negligible. This proves both limits in (14).
The limits are not inferred from the bounded checker, and are not needed
for the uniform theorem (3) or the entropy bound (4).

## 4. The initial field and the entropy linearization

Let L0=log2 and let U_*(y) be (1) at cutoff 2 with NO prime included. The exact
cutoff identity, with the full prime-2 jump, is

    U_X(y)=U_*(y)+Re C_X(y)+Re V_X(y).                (15)

A self-contained coarse bound is ||U_*||_(2,mu)<12. To verify it, use

    U_*=-gamma-log L0-log(1/4+y^2)
              +integral_0^L0[1-exp(u/2)cos(yu)]du/u.

The part integral (exp(u/2)-1)/u is less than sqrt2-1<1/2. The other part
satisfies

    integral_0^L0 (1-cos(yu))/u du
         <=1/4+2log_+(|y|L0)<=1/4+2log(1+|y|).

This follows by splitting at u=1/|y| when that point lies in the interval;
use 1-cos v<=v^2/2 before it and <=2 after it. At y=0 it is immediate.
Since 0<gamma<1, |log L0|<1/2, and
|log(1/4+y^2)|<=log4+2log(1+|y|), we obtain

    |U_*(y)|<4+4log(1+|y|).

Finally ||log(1+|y|)||_(2,mu)<2: the |y|<=1 contribution to its square is
less than 1/2, and the rest is at most
(2/pi)integral_1^infinity(1+log y)^2/y^2 dy=10/pi<10/3.
Minkowski gives the stated bound of 12.

The complete signed logarithmic mean is

    m_X:=integral U_X dmu=log A_X(3/2),   |m_X|<3.    (16)

One can derive this directly using (9),
integral log|b+iy|dmu=log(b+1), and the finite real integral for Ein.
Near u=0, splitting into (1-exp(u/2)) and exp(u/2)(1-cos(yu)) justifies
Tonelli for the latter and absolute integration for the former. Thus there
is no unproved continuation of a boundary Euler product in (16).
At the safe point, exactly

    A_X(3/2)=(2/9) exp(E1(L/2)) Z_X(3/2),
    E1(v)=integral_v^infinity exp(-t)dt/t.

Here 1<Z_X(3/2)<3, 0<E1(L/2)<2/log2<3, and log(2/9)>-2. Hence (16).
The logarithmic integral identity for b follows by differentiation in b and
the elementary rational integral; its integration constant follows at b=1.

The identity 2u_+=|u|+u and the Lipschitz property of the absolute value give

    |2E(X)-||Re C_X||_1|
       <=|m_X|+||U_*+Re V_X||_1
       <=|m_X|+||U_*||_2+||V_X||_2
       <3+12+14=29<32.                              (17)

This proves (4) without estimating the adaptive tanh feedback. The error is
UNIFORMLY bounded, not merely O(log log X). It is an additive L1 error;
no pointwise sign or zero-free region follows from (17) alone.

Combining (17) with the frozen EFB26 theorem gives, if desired,

    |W(X)-||Re C_X||_1|<40+24log(1+log X).           (18)

That consequence uses the parent's unreviewed component theorem at its
pinned source. No subpower estimate for either side has been obtained.

## 5. An exact one-state representation in the physical measure

Put a=log2, L=log X, and define the real signed finite measure

    dnu_X(t)=sum_(p<=X)p^-1/2 delta_(log p)(dt)
                         -exp(t/2)/t 1_[a,L](t)dt.  (19)

It has transform C_X(y)=integral exp(-iyt)dnu_X(t). Let

    v_X(t)=integral_[0,t] exp(-(t-u))dnu_X(u).

This is the stable filter v'+v=nu_X, zero before the first event. Fubini is
valid since nu_X has finite total variation. Direct integration gives

    integral_0^infinity exp(-(t-u))1_(t>=u)
                         exp(-(t-v))1_(t>=v)dt
          =(1/2)exp(-|u-v|).

Consequently (9) yields

    ||C_X||_(2,mu)^2=2||v_X||_2^2.                   (20)

For log2<=t<=L the state is v_X(t)=exp(-t)R(exp t). For t>=L it is
v_X(t)=exp(-t)R(X). Changing variable x=exp t proves

    ||v_X||_2^2=integral_2^X R(x)^2/x^3 dx
                                  +R(X)^2/(2X^2)=I(X).  (21)

This proves the first formula of (6). The second follows because

    integral C_X(y)^2 dmu(y)
       = [integral exp(-t)dnu_X(t)]^2=c_X^2.          (22)

All t in the source are nonnegative, so the absolute value in (9) is
simply t+u for this non-conjugated square. Thus
||Re C_X||^2=(2I+c_X^2)/2, with the factor two fixed exactly.
The bound |c_X|<5 follows from
sum_(n>=2)n^-3/2<=2 and
integral_2^infinity x^-3/2/log x dx<=sqrt2/log2<9/4.
Cauchy--Schwarz in the PROBABILITY measure mu, followed by (17), gives (6).

For a normalization check at X=2, the continuum is empty:
I(2)=1/4, c_2^2=1/8, and ||Re C_2||^2=5/16.
No numerical quadrature is needed for this check.

## 6. Applying the available prime estimates

Let E_theta(x)=theta(x)-x. Integration by parts with the left endpoint 2-
gives the exact identity

    R(x)=sqrt x/log x E_theta(x)+2sqrt2/log2
                       -integral_2^x E_theta(u)d(sqrt u/log u).  (23)

The lower endpoint constant is compulsory: E_theta(2-)=-2. At x=2,
(23) returns R(2)=sqrt2, as it must. The derivative in the integral is
(log u-2)/(2sqrt u log^2 u); its sign changes and is not discarded in (23).

**Conditional improvement.** Under RH, the classical implication
E_theta(x)=O(sqrt x log^2(2x)) gives

    R(x)=O(x log(2x)),
    I(X)=O((1+log X)^3),
    E(X)=O((1+log X)^(3/2)).                          (24)

The first bound follows from (23), the second from (21), and the last from
(6). This treats the ENTIRE frequency line without a frequency cutoff.
There is no simplicity or inverse-zeta-derivative assumption. The constants
are not numerically certified. RH is used only in this paragraph, not in
(3), (4), or (6). It improves the parent's conditional cubic-log entropy
budget; it is not an unconditional estimate.

**Unconditional stopping point.** The classical PNT remainder
E_theta(x)=O(x exp(-c sqrt(log x))) gives only

    R(x)=O(x^(3/2)exp(-c_1 sqrt(log x))),
    I(X)=O(X exp(-c_2 sqrt(log X))),
    E(X)=O(1+sqrt X exp(-c_3 sqrt(log X)))             (25)

for some positive c_j, after decreasing them to absorb fixed polynomial
factors. For example split the integrals at sqrt x and sqrt X to bound
the part near the upper endpoint and the earlier part separately. These
estimates are NOT subpower. They give no new unconditional zero-free strip.
Ordinary PNT also supplies the optional sharper higher-power asymptotic (14).
No external PNT producer or zero verification is rerun by this packet.

## 7. Exact closure boundary

By (4), a subpower upper bound for ||Re C_X||_(1,mu), even along an unbounded
subsequence, would yield the parent's critical entropy criterion and RH.
The exact L1 condition is not proved here.

A sufficient, potentially stronger bound at finite X is I(X)=X^o(1).
On the ACTUAL prime source, it is also RH-equivalent when coupled with the
conditional upper bound (24):

    RH iff I(X)=O_epsilon(X^epsilon) for every epsilon>0
       iff liminf log(1+I(X))/log X=0.               (26)

For the SUBSEQUENCE reverse implication use (6) and the frozen parent's
OEC26.T3: any zero beta>1/2 forces E(X)>=c X^nu-C for every
0<nu<beta-1/2 and all X. That source-domain lower bound retains multiplicities
and implies a positive lower exponent for I via (6), contradicting the
indicated liminf. Reflection then gives RH. This use of the parent is
explicit; it is not a new proof of that dependency or a bound for I.

For the ALL-X subpower statement there is also an independent direct ending,
which does not use the parent's domain-detection theorem. Define the uncut
local state v(t)=exp(-t)R(exp t), zero for t<log2. Its past norm through T is
at most I(exp T). Under the indicated all-X bounds, e^(-sigma t)v(t) belongs
to L2 for every sigma>0, by integrating the cumulative past energy against
2sigma exp(-2sigma T). Its Laplace transform V(z) is consequently analytic
for Re z>0 (Cauchy--Schwarz supplies uniform bounds on compact subsets).
In the absolute Euler half-plane, the filter identity gives

    (s+1/2)V(s-1/2)
       =sum_p p^-s-integral_2^infinity x^-s/log x dx.

Let a_*(s)=-gamma-log(log2)+Ein((s-1)log2). For Re s>1/2 put

    J(s)=a_*(s)+(s+1/2)V(s-1/2)
                         +sum_(p,k>=2)p^(-ks)/k.

The higher-power series is absolutely convergent LOCALLY INSIDE this open
half-plane; no absolute convergence on its boundary is asserted. Thus J is
analytic there. On Re s>1, ordinary Euler expansion and the positive-real
E1 integral give exp(J(s))=(s-1)zeta(s). The right side is analytic on
Re s>1/2 with its pole at one removed, so analytic uniqueness extends the
identity throughout. An exponential is zero-free. This excludes every zero
right of 1/2, and functional-equation reflection gives RH. The analytic
logarithm was constructed from the ASSUMED energy bound, not assumed across
hypothetical zeros. This is a self-contained conditional ending, not proof
of its central energy assumption.

The positive state energy I cannot be bounded by its prime diagonal alone:
its square includes all prime/prime, prime/continuum and continuum/continuum
interactions. Deleting them alters the object. The paper proves its exact
formula, not the required cancellation estimate for it. ATTEMPT_AND_REVIEW.md
records the failed attempt to deduce that estimate from PNT-size information.

No unconditional RH proof or original-domain completion is asserted.
