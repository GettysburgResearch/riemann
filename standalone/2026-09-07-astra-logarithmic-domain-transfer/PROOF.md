# OEC26 — From logarithmic Euler cost to an actual causal source norm

Status: PROPOSED COMPONENT THEOREMS WITH COMPLETE PAPER PROOFS; independent
mathematical review required. RH is NOT proved. The unconditional upper
bound needed in Theorem 5 is explicitly open.
Date: 2026-09-07. Author: Astra. This is research, not a Reviewer D verdict.

This continuation uses the same outer Euler completions as OE26, but a different
convergence mechanism. A logarithmic derivative converts their boundary cost
into a norm of an admissible, locally exact source vector. Every zero strictly
to the right then forces a POWER of X in that cost, not merely log X. As a
result, a single subpower subsequence at the exact critical line suffices.
The classical Hardy, Euler and RH-to-PNT inputs are identified explicitly.
No infinite assertion follows from the bounded algebra checker.

<a id="1"></a>

## 1. Actual objects and the elementary outer facts

Use H=L2(0,infinity), Lebesgue measure, and the Laplace/Hardy normalization

    Lf(z)=integral_0^infinity exp(-zt)f(t)dt,
    ||Lf||_H2^2=(1/(2pi)) integral_R |Lf(iy)|^2dy.

Let g(t)=floor(exp t)(1-t)+log(floor(exp t)!) with right-continuous activations.
The alternate expression

    g(t)=1-{exp t}+integral_0^t {exp u}du

proves 0<g(t)<=1+t. For alpha>0 put

    d_alpha(t)=exp(-alpha t)g(t),
    D_alpha(z)=(z+alpha-1)zeta(z+alpha)/(z+alpha)^2.       (1)

The elementary floor integral proves Ld_alpha=D_alpha, initially where the
Euler series converges and then on Re z>0. The pole at z+alpha=1 is removable.
In particular

    ||d_alpha||_1 <= K_alpha=1/alpha+1/alpha^2,
    ||t d_alpha||_2 <= V_alpha,
    V_alpha^2=1/(4alpha^3)+3/(4alpha^4)+3/(4alpha^5).      (2)

For X>=2 real, set L=log X and

    Z_X(s)=product_(p<=X)(1-p^-s)^(-1),
    A_X(s)=exp(-gamma) exp(Ein((s-1)L)) Z_X(s)/(L s^2),
    Ein(w)=sum_(k>=1) (-1)^(k+1)w^k/(k k!).               (3)

All primes are ordinary primes; ALL powers of every included prime are present.
The definition at s=1 is the entire expression, not a division by s-1.
For b>0 define the finite nonnegative logarithmic cost

    E_b(X)=(1/pi) integral_R log^+|A_X(b+iy)|/(1+y^2)dy.   (4)

For every fixed b,X the function A_X(b+z) is zero-free, outer and in H2 and
H-infinity on Re z>0. Here are the analytic facts needed for this application.
The Euler denominators are nonzero on Re s>0. With E1(w)=Ein(w)-gamma-log w
on the principal cut plane, the horizontal contour identity gives

    E1(w)=exp(-w) integral_0^infinity exp(-u)/(w+u)du,
    |E1(w)|<=exp(-Re w)/|Im w|,                 |Im w|>0. (5)

Consequently exp(Ein((s-1)L)) grows at most linearly in |s| on Re s>=b;
the remaining bounded-imaginary-part region is handled by a compact set and
the positive-real E1 estimate. Since |Z_X(s)|<=Z_X(b),

    |A_X(b+x+iy)|<=C_(b,X)/|b+x+iy|, x>=0.              (6)

The bound is not uniform in X. It proves the full Hardy bound, not just a
boundary integral. Analytic nonvanishing continuation across every finite
boundary point rules out boundary singular inner factors. The only possible
inner factor at infinity, exp(-tau z), is ruled out by A_X(b+x)~1/x as x->infinity.
Thus the standard Hardy factorization theorem makes A_X(b+z) outer. Its
canonical logarithm is analytic and real at positive real z. Its real part
has the Poisson representation; there is no unaccounted linear harmonic term.
These are the same finite-approximant facts as OE26, restated to make this
continuation independent of that packet's publication timing.

<a id="2"></a>

## 2. Entropy controls a smoothed logarithmic derivative

Write U_X(t)=log|A_X(b+it)| and let h_X(z)=log A_X(b+z) be the canonical logarithm.
At z=1 the positive Euler bounds 1<Z_X(b+1)<1+1/b and 0<E1(bL)<1/(b log2)
give

    log(b/(b+1)^2)<h_X(1)<-log(b+1)+1/(b log2).

It follows that |h_X(1)|<=C_b, uniformly in X, where one may use

    C_b=2log(b+1)+|log b|+1/(b log2).                  (7)

In the range 1/2<=b<=1, the simpler C_b=3 is valid: the lower bound exceeds
log(2/9)>-2 and the upper bound is less than 3.

Poisson evaluation at z=1, followed by positive/negative part decomposition,
gives the exact identity and bound

    (1/pi) integral |U_X(t)|/(1+t^2)dt
          =2E_b(X)-h_X(1) <=2E_b(X)+C_b.             (8)

This step would fail with only a bound for a signed logarithmic mean.
The differentiated Schwarz formula is

    h_X'(z)=-(1/pi) integral U_X(t)/(z-it)^2 dt.       (9)

It is justified by weighted log integrability and uniform kernel bounds on
compact subsets. An imaginary constant in the Schwarz formula disappears
under differentiation. For x>=sigma>0, the elementary estimate

    (1+t^2)/(x^2+(y-t)^2)
       <=2+(1+2y^2)/x^2 <=C_sigma(1+y^2),
    C_sigma=2+2/sigma^2,                              (10)

then proves

    |h_X'(x+iy)|<=C_sigma(1+y^2)[2E_b(X)+C_b].        (11)

**Theorem OEC26.T1 (an entropy-to-Hardy norm bound).** For every b,sigma>0,

    Q_(b,sigma,X)(z)=h_X'(z+sigma)/(z+1)^3

is the Laplace transform of an L2 causal function q_(b,sigma,X), and

    ||q_(b,sigma,X)||_2
       <= C_sigma[2E_b(X)+C_b]/sqrt(2).               (12)

Indeed on every line Re z=x>=0 the square of the bound is at most
C_sigma^2[2E+C_b]^2/(1+y^2). Its integral with the specified 1/(2pi)
normalization is C_sigma^2[2E+C_b]^2/2. Paley-Wiener proves the assertion.
The inward shift sigma>0 is compulsory. The constants are not claimed
uniform as sigma decreases to zero. The cubic denominator is a fixed stable
smoothing, not an order chosen after a numerical experiment.

<a id="3"></a>

## 3. The same logarithmic derivative is a literal prime source

Differentiate (3), with s=alpha+z and alpha=b+sigma:

    (d/ds)log A_X(s)
       =-2/s+(1-X^(1-s))/(s-1)
                  -sum_(p<=X) log p/(p^s-1).         (13)

At s=1 the middle term is log X. There is no pole there. Its causal inverse is
the finite-total-variation signed measure

    ell_(alpha,X)(t)
      =[exp((1-alpha)t)1_[0,L](t)-2exp(-alpha t)]dt
        -sum_(p<=X,k>=1) (log p)p^(-kalpha)delta_(k log p).
                                                          (14)

The values of the continuous part at the endpoints do not matter. At an
included prime-power knot the entire atom is retained. The atom series is
absolutely summable for each finite prime BASE set and alpha>0.
Let w(t)=t^2 exp(-t)/2, with Lw(z)=(z+1)^(-3), and set

    q_X=w*ell_(alpha,X),
    y_X=d_alpha*q_X,
    f_alpha=-w*(t d_alpha).                            (15)

All are actual H functions: q_X follows also directly from Young's inequality
and the finite variation in (14). Its transform is exactly that of Theorem 1.
The vector y_X is in the original closed source domain closure(D_alpha H2).
The target has transform

    F_alpha(z)=D_alpha'(z)/(z+1)^3.                    (16)

**Theorem OEC26.T2 (local exactness with a cost bound).** For every X>=2,

    y_X(t)=f_alpha(t) for almost every 0<t<log X,
    ||y_X||_2<=A_(alpha,sigma)[2E_b(X)+C_b],
    A_(alpha,sigma)=K_alpha C_sigma/sqrt(2),
    ||f_alpha||_2<=V_alpha.                            (17)

To prove the local identity, use in an initial Euler half-plane

    D_alpha'/D_alpha
      =1/(z+alpha-1)-2/(z+alpha)+zeta'/zeta(z+alpha).

Its causal inverse is the locally finite signed distribution

    ell_alpha(t)=[exp((1-alpha)t)-2exp(-alpha t)]dt
                -sum_(n>=2)Lambda(n)n^(-alpha)delta_(log n).

It has exponential order there. It agrees with (14) before log X: every prime
power active before that horizon has base <=X. The later powers of included
primes are not deleted from (14). Initial Laplace uniqueness gives
 d_alpha*ell_alpha=-t d_alpha locally. Causality and convolution with w prove
(17). The norm bound uses (12) and (2), not a norm for the uncut distribution.

No shifted zero defines any vector in (15). In particular this is a different
construction from canceling a selected finite packet of zeros by hand.

<a id="4"></a>

## 4. Every off-line zero forces power growth of the logarithmic cost

Let rho=beta+i gamma be any nontrivial zeta zero of exact multiplicity m>=1
with beta>b. Fix ANY 0<sigma<beta-b, and put

    alpha=b+sigma, lambda=rho-alpha, delta=Re lambda>0,
    kappa_(rho,alpha)=
      (2delta)^(m-1/2) |D_alpha^(m)(lambda)|
                /[(m-1)! |lambda+1|^3] >0.             (18)

Here D_alpha^(m)(lambda)=(rho-1)zeta^(m)(rho)/rho^2. Neither zero simplicity
nor a quantitative lower bound on that derivative is assumed.

**Theorem OEC26.T3 (full-cutoff polynomial obstruction).** For every X>=2,

    E_b(X) >= [kappa_(rho,alpha)/(2A_(alpha,sigma))] X^delta
                 -C_b/2-V_alpha/(2A_(alpha,sigma)).    (19)

In particular, for EVERY 0<nu<beta-b there are c,C>0 such that

    E_b(X)>=c X^nu-C                 for all X>=2.      (20)

### Complete multiplicity proof

At lambda, D_alpha has a zero of order m, so Y_X=D_alpha Q_X vanishes through
order m-1. F_alpha from (16) vanishes through order m-2 and

    F_alpha^(m-1)(lambda)=D_alpha^(m)(lambda)/(lambda+1)^3.

Let e_X=y_X-f_alpha. By (17) it is supported in [L,infinity). The shifted
function e_L(u)=e_X(u+L) has transform exp(Lz)(Y_X-F_alpha)(z). Its derivatives
below order m-1 at lambda vanish, and its derivative of order m-1 is

    -exp(Llambda)D_alpha^(m)(lambda)/(lambda+1)^3.       (21)

There is NO power of L in (21), precisely because every lower jet vanishes.
Use the unit vector

    v_m(u)=sqrt(2delta)exp(-conj(lambda)u)L_(m-1)(2delta u)

in L2(0,infinity). Laguerre orthogonality follows from Rodrigues' formula by
integration by parts. In its inner product with e_L all polynomial terms
below degree m-1 disappear. The leading coefficient and the Laplace derivative
sign cancel, yielding

    |<v_m,e_L>|=kappa_(rho,alpha) exp(delta L).

Cauchy-Schwarz gives ||e_X||>=kappa X^delta. On the other hand, (17) gives
||e_X||<=A[2E_b(X)+C_b]+V_alpha. Rearranging proves (19). Choose
sigma=beta-b-nu to prove (20). This includes every real X and its integer/prime
endpoints. No background zero sum, density estimate, randomness, or phase
independence enters the proof. A hypothetical zero is used only in the
contradiction/lower-bound argument, not the construction.

If Theta=sup Re rho, the theorem implies the unconditional lower statement

    liminf_(X->infinity) log(1+E_b(X))/log X >=max(Theta-b,0).
                                                          (22)

No matching upper identity for general b is claimed. For b<1/2 the classical
existence of a critical-line zero already proves positive-power growth in
(20), unconditionally. At b=1/2 only a genuinely off-line zero is charged.

There is also the elementary inequality

    E_b(X)<= (1/2)log(1+2||A_X(b+.)||_H2^2),           (23)

by log^+u<=(1/2)log(1+u^2), Jensen's inequality for the probability density
1/[pi(1+y^2)], and that density's upper bound 1/pi. Thus (20) forces at least
exp(c X^nu) growth of the squared source norms. This is conditional on the
selected zero, or unconditional below 1/2 as just explained. It is not a
claim of such growth on the critical line without an off-line zero.

<a id="5"></a>

## 5. A single critical-line criterion, weaker than OE26's requirement

**Theorem OEC26.T4 (conditional critical-line upper bound).** If RH holds, then

    E_(1/2)(X) <= C(1+log X)^3,                X>=2.    (24)

Only the classical RH implication |theta(x)-x|<=C sqrt(x)log^2(2x) is imported.
There is no zero simplicity, weak Mertens conjecture or inverse-derivative sum
hypothesis. The constant is not numerically certified.

### Proof with all frequencies and all prime powers

Put E(x)=theta(x)-x and s=1/2+iy. Exactly,

    log A_X(s)=a_*(s)-2log s+C_X(s)+V_X(s),
    a_*(s)=-gamma-log(log2)+Ein((s-1)log2),
    C_X(s)=integral_[2-,X] x^(-s)/log x dE(x),
    V_X(s)=sum_(p<=X,k>=2)p^(-ks)/k.                    (25)

At X=2 the discrepancy integral is 2^(-s); the prime-2 atom is not half-weighted.
The logarithm in (25) is canonical on Re s>0. a_* and log s have integrable
real parts against the Cauchy weight, with bounds independent of X; (5) handles
the full frequency tail of a_*. At this endpoint V_X is NOT uniformly bounded:
its k=2 part is bounded in modulus by (1/2)sum_(p<=X)1/p<=C(1+log X), while
k>=3 contributes a fixed finite constant. This weaker bound is sufficient.

Stieltjes integration by parts under RH gives, uniformly for real y,

    |C_X(1/2+iy)|<=C(1+|y|)(1+log X)^2.              (26)

Indeed the upper endpoint is O(1+log X), the lower endpoint is bounded,
and the integral is bounded by
C(1+|y|) integral_(log2)^(logX)(1+u)du. The fixed lower endpoint uses E(2-).
Integrate (26) only over |y|<=X. The Cauchy integral of 1+|y| is O(1+log X),
so this part costs O((1+log X)^3). The V_X and fixed terms cost less.

For |y|>X use the original finite-product expression, not (26):

    log|A_X(1/2+iy)|
       =-log|1/2+iy|+Re E1((-1/2+iy)logX)+log|Z_X(1/2+iy)|.

The first term is negative. The second is at most sqrt(X)/(|y|logX), by (5).
The last is at most C sqrt(X), by -log(1-u)<=u/(1-u) and a comparison of
sum_(n<=X)n^(-1/2) with its integral. Its entire Cauchy-weighted tail is
O(X^(-1/2)). This proves (24). No fixed-frequency limit replaces a full norm.

**Theorem OEC26.C1 (exact equivalence and conditional end-to-end endpoint).**
The following statements are equivalent:

 (a) RH;
 (b) E_(1/2)(X)=O_epsilon(X^epsilon) for every epsilon>0;
 (c) liminf_(X->infinity) log(1+E_(1/2)(X))/log X=0;
 (d) integral_2^infinity E_(1/2)(X) X^(-1-epsilon)dX<infinity
     for every epsilon>0.

RH implies (b) and (d) by (24), and (b) implies (c). If RH fails, symmetry
supplies beta>1/2. Equation (20) refutes (c) and refutes (d) by choosing
0<epsilon<nu<beta-1/2. Thus both (c) and (d) imply RH. In particular one
unbounded subpower subsequence at EXACTLY b=1/2 suffices. The endpoints b_j
and the o(log X) bound from OE26 are no longer needed for this implication.

None of (b)-(d) is proved unconditionally here. A condition being weaker as
a growth allowance does not mean it has become easy for this exact arithmetic
source. The role of the stronger detector is to avoid paying an unnecessarily
strong norm bound, not to declare the missing estimate paid.

<a id="6"></a>

## 6. A bounded all-frequency sanity check, not asymptotic evidence

The literal value E_(1/2)(2) satisfies E_(1/2)(2)<4. Here is an analytic bound
for the entire integral, requiring no numerical zeta or Ein evaluation.
Let L=log2, with 2/3<L<7/10 and sqrt2<3/2. On |y|<=1,

    Re Ein((-1/2+iy)L)
       =integral_0^L [1-exp(u/2)cos(yu)]du/u
       <=sqrt2*y^2*L^2/4 <147/800.

Also -gamma<0, -log L<1/2, -2log|1/2+iy|<=2log2<7/5,
and -log|1-2^(-1/2-iy)|<=-log(1-1/sqrt2)<3/2.
The last inequality follows from sqrt2>7/5, so 1-1/sqrt2>2/7, and
exp(3/2)>7/2, certified by the first four exponential-series terms.
The sum is less than 4. This half of the probability weight contributes <2.
On |y|>=1 the representation in the preceding proof gives

    log^+|A_2(1/2+iy)| <=3/2+9/(4|y|).

Its remaining cost is less than
3/4+(9/(4pi))log2 <3/4+21/40=51/40, using pi>3.
Thus E_(1/2)(2)<131/40<4. The finite bound is merely a normalization check and does not support (b)-(d).

<a id="7"></a>

## 7. Status and scholarly boundary

New as a project continuation: the explicit admissible logarithmic-derivative
source, its entropy-controlled full Hardy norm, the all-cutoff power obstruction
with full multiplicity, and the critical-line subpower/subsequence/Abel criteria.
The conditional critical-line upper bound is supplied with the entire frequency
integral accounted for. An independent Abel construction and the unsuccessful
unconditional estimate are in ABEL_AND_ATTEMPT.md.

Classical mechanisms: outer factorization, the Poisson-Schwarz formula,
Paley-Wiener, Laguerre/Bessel interpolation, Euler logarithmic derivatives,
and RH-to-PNT. Logarithmic RH criteria and Hardy approximation are not new;
see EXTERNAL_INPUTS.md. No external novelty/priority or independent acceptance
is claimed. Original-domain completeness, a global critical Xi isometry, and
RH remain unproved. No finite checker certifies them.
