# Quantitative future realization and a complete-source conditioning bound

Status: PROPOSED COMPONENT THEOREMS; independent mathematical review required.
RH, the original full-source block gain, and the growing-horizon optimal-tail
upper bound are NOT proved. This is research, not an independent acceptance.

The continuation addresses two concrete prerequisites left by OC26: pricing
finite-section conditioning, and replacing a closed-domain impulse correction
by a specified compact L2 input. It also certifies a stronger, fixed-horizon
correction. None of these is silently promoted to a rate for the limiting
arithmetic projection as the horizon tends to infinity.

## 0. Exact source and classical inputs

Work in H=L2(0,infinity), with causal shifts S_s, causal convolution, and
Laplace transform D(z)=integral exp(-zt)d(t)dt. Set

    g(t)=floor(exp(t))(1-t)+log(floor(exp(t))!),
    d(t)=exp(-t/2)g(t),
    D(z)=(z-1/2)zeta(z+1/2)/(z+1/2)^2.                 (0.1)

The value D(1/2)=1 is its analytic removable value, not a raw totalized product.
The source formula gives 0<g(t)<=1+t. Hence

    ||d||_1<=6,   ||d||_2^2<=5.                        (0.2)

These facts and the compact source inverse are reconstructed in PR #804,
CD26, at the exact source listed in SOURCES.md. They do not assume RH.
Let R be the bounded causal all-pass operator with multiplier

    r(z)=(z-1/2)/(z+1/2)=1-1/(z+1/2).

It is an L2 isometry. Put phi_j=R^j d and G_K=(<phi_i,phi_j>)_(0<=i,j<=K).
The closed span of this dictionary is the original closed source space M.
Its Hardy inner factor may be nontrivial; no outerness is assumed below.

Classical analytic inputs: Laplace--Hardy Plancherel, inner--outer factorization
in H2 of the disk, the outer Poisson formula for log modulus, Jensen's inequality
for a nonzero H2 function, and Stirling's limiting normalization. They are used
in their usual unconditional forms. The quantitative bounds needed here are
proved below, not cited as black-box convergence rates. Classical existence
of one critical-line zero is used only for the upper obstruction in Section 2.

## 1. FR26.1: an explicit all-rank Gram floor, without RH

For every integer K>=0, let n=K+1. Then

    exp(-8 sqrt(K+4))/n^2 <= lambda_min(G_K),
    lambda_max(G_K)<=5n.                               (1.1)

In particular the entirely rational lower bound

    gamma_K = 1/[n^2 2^(13 ceil(sqrt(K+4)))]             (1.2)

is valid at every rank. These are conservative bounds, not optimal condition
numbers and not bounds for an infinite inverse.

Proof. The unitary Cayley image of d is

    A(w)=D((1+w)/(2(1-w)))/(1-w)
        =w zeta(1/(1-w)),   A(0)=1,   ||A||_H2^2<=5.  (1.3)

The apparent pole at w=0 is removable. The Gram is exactly the Gram of
A,wA,...,w^K A in disk H2, with normalized circle measure.
Factor A=B O with B inner, O outer, and O(0)>0. Write l=log|A| on the
boundary. Jensen gives integral l>=log|A(0)|=0. Since

    log^+(x) <= x^2/5,  x>=0,

we have integral l_-<=integral l_+<=1. The elementary logarithm inequality
follows by maximizing log(x)/x^2 for x>=1: its maximum is 1/(2e)<1/5.
The outer Poisson formula and the Poisson-kernel bound therefore give

    log|O(w)| >= -2/(1-r),  |w|<=r<1.                (1.4)

This constructs a bound for the reciprocal of the OUTER factor. It does not
assert that A is outer, and it never analytically inverts an interior zero.

Write 1/O(w)=sum c_j w^j. With r=1-1/sqrt(K+4)>=1/2, Cauchy's estimate
and -log r<=(1-r)/r yield, for 0<=j<=K,

    |c_j| <= r^(-j) exp(2/(1-r)) <= exp(4 sqrt(K+4)).   (1.5)

If p has degree at most K and y=Op, its first K+1 coefficients determine p
by triangular convolution with (c_0,...,c_K). The finite convolution norm
is at most sum |c_j|. Thus

    ||p||_H2 <= n exp(4 sqrt(K+4)) ||Op||_H2
              =n exp(4 sqrt(K+4)) ||Ap||_H2.

This is (1.1). The upper bound is the Gram trace n||d||^2<=5n.
Finally e<3 and 3^8<2^13 show that (1.2) is smaller than the lower bound
in (1.1). End of proof.

The same argument applies to ANY H2 source A with A(0)=1 and ||A||^2<=5.
It is a quantitative use of classical outer factorization, not an arithmetic
zero-exclusion theorem. For example A(w)=1-2w has precisely these values,
and a nontrivial inner factor. Its finite Grams are uniformly bounded below
by I, yet the distance of 1 to its closed polynomial orbit is 3/4 in squared
norm. At its zero a=1/2, Hardy evaluation gives the lower bound 1-|a|^2=3/4,
and the Blaschke projection attains it. Good conditioning does not prove
cyclicity or absence of an intrinsic tail cost.

## 2. FR26.2: the actual infinite source has no uniform Gram floor

There is nevertheless an unconditional obstruction to replacing gamma_K by
a rank-independent positive constant. Take one classical critical-line zero
rho=1/2+i gamma, and put

    w0=(i gamma-1/2)/(i gamma+1/2).

Then |w0|=1, w0!=1, and A extends analytically through w0 with A(w0)=0.
The function A(w)/(1-conj(w0)w) is in H2: the denominator zero is cancelled
locally, and off that neighborhood its reciprocal is bounded on the circle.
Let its squared norm be J_rho<infinity. The unit-coefficient-norm polynomial

    p_K(w)=(1+conj(w0)w+...+(conj(w0)w)^K)/sqrt(K+1)

satisfies

    lambda_min(G_K) <= ||A p_K||^2 <= 4 J_rho/(K+1).    (2.1)

The last bound uses the finite geometric-series identity and
|1-(conj(w0)w)^(K+1)|<=2 on the circle. Thus lambda_min(G_K)->0.
No zero height, simplicity, or numerical zero table is needed. This is fully
compatible with (1.1): a root-exponential lower envelope and a reciprocal-rank
upper envelope are not contradictory.

## 3. FR26.3: a sharp translation modulus for the literal factorial source

Extend d by zero to negative times. For 0<s<=1/4, set

    L(s)=||S_s d-d||_2^2.

Then

    L(s)<=20s(1+log(1/s)),                             (3.1)
    L(s)=s log(1/s)+O(s) as s decreases to zero.        (3.2)

The leading coefficient in (3.2) is exactly one. This theorem is about the
source itself, not a numerical zero model or a presumed RH consequence.

First record the all-real Stirling remainder in source form. For x>=1,

    S(x)=floor(x)log x-log(floor(x)!)
        =x-(log x)/2-c+epsilon(x), c=log(2pi)/2,
    |epsilon(x)|<=1/(6x),
    epsilon'(x)=-({x}-1/2)/x between integer knots.    (3.3)

A proof is obtained from the periodic Bernoulli polynomial B2(u)=u^2-u+1/6:

    epsilon(x)=-B2({x})/(2x)+(1/2)integral_x^infinity B2({u})du/u^2.

Its derivative is the displayed one, and Stirling fixes the constant at
infinity. Since |B2|<=1/6, (3.3) follows including every knot. Consequently

    g(t)=t/2+c-1/2+a(t),
    a(t)=-({exp t}-1/2)-epsilon(exp t),
    |a(t)|<=2/3.                                     (3.4)

For the explicit upper bound put X=1/(2s), L0=log X. On [0,s] the contribution
to the squared translation difference is at most 2s by g<=1+t. On [s,L0],
d is locally BV. Its regular derivative and jumps are

    d'_reg=-d/2-exp(-t/2)floor(exp t),
    jump at log n = n^(-1/2), n>=2.

Write d(t)-d(t-s)=V_s(t)+J_s(t), its derivative integral plus its jump sum.
The jump windows in this interval are disjoint: successive log n through
n<=X are separated by at least 1/n>=2s. Therefore

    integral_s^L0 J_s(t)^2dt <= s log X.

Cauchy--Schwarz and (0.2) give

    integral_s^L0 V_s(t)^2dt
      <=s^2 integral_0^L0 |d'_reg|^2
      <=s^2(5/2+2X)<2s.

Their combined squared contribution is at most 4s+2s log X.
For t>=L0, split d=p+r, where

    p(t)=exp(-t/2)(t/2+c-1/2), |r(t)|<= (2/3)exp(-t/2).

We have 1/2<c<1, ||p'||_2^2<1, and exp(s)<=4/3. It follows that

    integral_L0^infinity |r(t)-r(t-s)|^2dt <5s,
    integral_L0^infinity |p(t)-p(t-s)|^2dt <=s^2.

Twice the sum is less than 11s. Adding the three regions gives
17s+2s log X, which is bounded by (3.1).

For the asymptotic, the disjoint jump-square integral on [s,L0] equals
s log(1/s)+O(s); any clipped endpoint window changes it by O(s).
The regular-square, initial, and far-tail terms just bounded are O(s).
The cross term is also O(s), not merely O(s sqrt(log(1/s))). Indeed on the
window following log n its absolute integral is bounded by

    s^2 exp(s/2)[1+(1+log n+s)/(2n)].

Summing n<=X gives O(s^2 X+s^2(1+log X)^2)=O(s). This proves (3.2).
Every estimate is for ordinary time integrals, with endpoints of measure zero
handled by the fixed right-continuous source convention. End of proof.

## 4. FR26.4: quantitative replacement by ordinary compact inputs

Let b_epsilon=epsilon^(-1)1_[0,epsilon]. For 0<epsilon<=1/4,

    ||d-d*b_epsilon||^2
      =epsilon^(-2)integral_0^epsilon s L(s)ds
      <=10 epsilon(1+log(1/epsilon)),                 (4.1)
    ||d-d*b_epsilon||^2
      =(epsilon/3)log(1/epsilon)+O(epsilon).           (4.2)

To prove the equality, expand the squared norm of the average S_s d. The
variance identity and shift isometry use ||S_s d-S_t d||^2=L(|s-t|).
The double integral reduces to (4.1)'s single integral. Apply Section 3.
There is no Dirac delta input in b_epsilon; it is a compact L1/L2 function.

For any finite polynomial p(R)=sum_(j=0)^K c_j R^j,

    ||p(R)d-d*(p(R)b_epsilon)||
      <=sum |c_j| sqrt(10epsilon(1+log(1/epsilon))).    (4.3)

This uses the isometry of every R^j, not a contraction of the arithmetic
source inverse. If c is the least-squares vector correcting a tail q0, then

    ||c||_2<=||q0||/sqrt(gamma_K),
    sum |c_j|<=sqrt(K+1)||q0||/sqrt(gamma_K).            (4.4)

Indeed the squared norm of its projection is c*G_K c<=||q0||^2.
Thus (4.3)-(4.4) price realization at every finite rank. A dyadic epsilon
satisfying any prescribed error budget can be found using the rational floor
(1.2) and log2<1, without assuming an infinite bounded inverse.

The input p(R)b_epsilon is ordinary L1/L2 but initially has an infinite stable
tail. This too can be cut explicitly. Its impulse polynomial away from zero is

    exp(-t/2) P_c(t),
    P_c(t)=sum_(k=1)^K (-1)^k [sum_(j=k)^K c_j binom(j,k)] t^(k-1)/(k-1)!.

For U>=max(1,epsilon), define L_c(t) by replacing each bracket by its absolute
value. Truncating v=p(R)b_epsilon after U changes the OUTPUT by at most

    6 exp(epsilon/2) [integral_U^infinity exp(-t)L_c(t)^2dt]^(1/2). (4.5)

The box part of the impulse is already zero there. Bound the convolution on
[t-epsilon,t] and apply ||d||_1<=6. The remaining integral is a finite polynomial
in U times exp(-U), evaluated by integer factorial moments. All corrections
S_T(d*v) with this truncated v are generated by compact L2 inputs and are zero
before T, exactly. No finite prefix is traded for a smaller norm.

## 5. FR26.5: full finite-section truncation can now be priced

Let d^S=d 1_[0,S]. Its complete omitted norm is bounded by

    e_S=(S+3)exp(-S/2).                                (5.1)

Let G_K^S be the Gram of R^j d^S, including their entire future filter tails.
Then

    ||G_K-G_K^S||_op <=(K+1)(2sqrt(5)e_S+e_S^2).        (5.2)

If e_S<=min(1,gamma_K/[12(K+1)]), then G_K^S>=gamma_K I/2.
For example S=32(m+l+2), with m=ceil sqrt(K+4) and l=ceil log2(K+2), suffices.
To check this use exp(-S/2)<2^(-S/2), n<2^l, and
S+3<=64(m+l+2)<=64*2^(m+l+1). The resulting integer powers dominate
12n^3(S+3). This is a conservative prescription with S=O(sqrt K+log K);
the largest primitive factorial argument is exp(O(sqrt K+log K)). No claim
about its practical constant, bit complexity, or a fast high-rank run is made.

Given a computed vector c and any approximation q^S to the seed tail,

    ||q0-sum c_j R^j d||
      <=||q^S-sum c_j R^j d^S|| + ||q0-q^S||
                         +sqrt(K+1)||c||_2 e_S.       (5.3)

This is a valid full-norm certificate. One must not drop the filtered tails of
d^S in its first term. Equations (5.1)-(5.3) control approximation of a FINITE
optimization. They do not bound its unknown limit as the horizon grows.

## 6. FR26.6: a fixed actual-source compact-input correction

Take T=log2, h(t)=t exp(-t/2), and

    f0=d*(exp(t/2)1_[0,T)(t)).

Finite divisor inversion gives f0=h on [0,T]. Define

    (c0,c1,c2,c3,c4)=(4284,-1839,-1199,-742,-371)/10000,
    p(R)=sum_(j=0)^4 c_j R^j,
    f_star=f0+S_T p(R)d.                               (6.1)

These coefficients were chosen by non-directed discovery and then rounded;
only the exact rational vector (6.1) is used in the proof-producing replay.
No optimality is claimed. The complete-tail certificate proves

    ||f0-h||^2>3/10,
    ||f_star-h||^2<1/1200.                             (6.2)

Now put epsilon=2^(-40), U=128,

    v(t)=1_[0,U](t) [p(R)b_epsilon](t),
    f_comp=f0+S_T(d*v).                                (6.3)

The entire input of f_comp is an explicitly specified compact L2 FUNCTION.
It preserves the same prefix. Because sum |c_j|=8435/10000<1, (4.3) is below
1/10000: its squared bound is 410/2^40<1/10^8. For t>=1,
L_c(t)<=4+6t+2t^2+t^3/6<13t^3. Equation (4.5) is therefore at most

    156 exp(-64)134^3 < 156*134^3/2^64 <1/10^8.

Use integral_U^infinity exp(-t)t^6dt<=exp(-U)(U+6)^6. Thus the total norm
change in making (6.3) is less than 1/5000. Since 1/1200<(29/1000)^2,

    ||f_comp-h||^2 < (29/1000+1/5000)^2 < 1/1000.        (6.4)

In particular this is a greater-than-300-fold squared-error reduction relative
to f0. It is a deliberately tiny fixed horizon, NOT a new best approximation
record, a new zero-free region, or an infinite-horizon convergence claim.

## 7. Complete numerical proof of (6.2), without numerical quadrature

Set x=exp u, and write S(x) as in (3.3). The shifted seed error is

    q0(u)=2^(-1/2)exp(-u/2)[S(2x)-2S(x)-log(2x)].       (7.1)

Let H0=g and, for k>=1,

    Hk(u)=integral_0^u (u-v)^(k-1)g(v)/(k-1)! dv.

Then R^j d=exp(-u/2) sum_(k=0)^j (-1)^k binom(j,k)Hk(u).
On a cell u=u0+s, x in [m/2,(m+1)/2], n=floor(m/2),

    g(u)=g0-ns,
    Hk(u0+s)=sum_(l=0)^(k-1) H_(k-l)(u0)s^l/l!
                 +g0 s^k/k! -n s^(k+1)/(k+1)!.

The seed bracket is linear in u on this cell:

    (m-2n-1)u+(m-1)log2-log(m!)+2log(n!).

Thus the integrand is exp(-u) times the square of a polynomial of degree at
most five. Its exact cell moments satisfy

    I0=1-x0/x1,   Ir=r I_(r-1)-(log(x1/x0))^r x0/x1.

Outward dyadic arithmetic evaluates these identities; cancellation is not
replaced by midpoint agreement. All 4094 half-integer cells through X=2048
are included. The integrated seed error exceeds 0.313411805394 and the
corrected partial error lies in (0.000635301235,0.000635301236).

For the infinite tail, use the smooth part m(t)=t/2+c-1/2 of g and a=g-m.
Equation (3.3) gives the stronger primitive control

    |integral_(log X)^(log X+s) a(u)du|<=1/(3X), s>=0. (7.2)

Indeed a(u)=(d/du)epsilon(exp u)-epsilon(exp u). Substitute (3.3); the
endpoint and integral upper bounds add exactly to 1/(3X).
Repeated integration makes the tail Hk its explicit smooth polynomial plus
an error at most s^(k-1)/[3X(k-1)!], for k>=1. At k=0 use
|a(log X+s)|<=1/2+1/(6X).

The seed tail bracket is

    -(log X+s)/2+c-(3/2)log2 + error,
    |error|<=5/(12X).

The checker constructs the resulting full corrected polynomial P(s) and the
positive remainder polynomial E(s). By Minkowski,

    tail squared norm <= X^(-1)
       [sqrt(integral_0^infinity exp(-s)P(s)^2ds)
        +sqrt(integral_0^infinity exp(-s)E(s)^2ds)]^2.  (7.3)

Both integrals are finite polynomial sums with integer factorial moments.
The complete tail upper bound is below 0.000177691679. Adding it to the
outward partial sum gives ||f_star-h||^2<0.000812992915<1/1200.
The constant c is enclosed using Machin's formula for pi and explicit
atan/atanh remainders. No floating-point value, numerical zero, numerical
quadrature, or external special-function oracle enters acceptance.

## 8. The end-to-end attempt and the precise remaining failure

For every horizon T, the previous OC26 source hierarchy has

    U_K(T)=||q0||^2-r*G_K^(-1)r decreasing to C_B(T),

where C_B(T) is the unavoidable complete zero-imposed continuation cost.
Sections 1, 4 and 5 now price finite conditioning, ordinary input realization,
and full source truncation. They leave no unbounded inverse or impulse-domain
assumption in any finite certificate. Section 6 demonstrates the procedure on
the literal source, with a full infinite-tail guarantee.

But applying (1.1) to the projection term only bounds coefficient sensitivity.
It does not bound how much of q0 the finite dictionary captures. In particular

    U_K(T)-C_B(T)=||(I-P_K)P_M q0||^2

still has no proved horizon/rank rate. A lower spectral bound for G_K does not
control this target-dependent residual; the nonouter example after (1.5) shows
why it cannot imply domain completeness by itself.

A hypothetical zero rho=1/2+delta+i gamma, delta>0, forces for any source output
matching h=t exp(-t/2) before T,

    ||f-h||^2 >= 2delta exp(2delta T)/|rho|^4.

This is the full-domain evaluation bound reconstructed in the parent. Thus
source-defined corrections with subexponential error on unbounded horizons
would prove RH. This pass does NOT construct such a sequence or prove such a
bound. The only unconditional growing-horizon ceiling still obtained by direct
seed estimates is exponential in T. Fixed T and increasing rank is not the
missing simultaneous limit. The new positive results are quantitative finite
realization and conditioning, not an end-to-end RH completion.
