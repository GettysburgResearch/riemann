# MHB32: an exact Mellin–Hankel bridge and a smaller microscopic bandwidth loss

**Status: PROPOSED component mathematics; independent mathematical review required.**
**The full native subquadratic recurrence and RH are NOT proved.**
Date: 21 September 2026. Continuation of #904 at
`aaea3f9605a430600bea0189397d93ca315b5f98`.

This packet estimates the SAME smoothly selected microscopic contribution as
MCB31. It replaces its bandwidth factor H^4 by H^(191/82), with a substantially
larger absolute constant. It does not replace the quadratic input-energy
exponent by a subquadratic one. The old bound remains useful and unchanged.

The argument connects the additive-frequency selection to a Mellin multiplier
by a rederived classical Müntz identity. A rank-one term and the complex square
of the source transform are retained. It is NOT an assertion that additive and
Mellin projections commute. The imported Patel–Yang zeta bound is credited;
no new subconvexity theorem or external novelty claim is made.

## 1. Exact source, modes, and theorem

Let c be any finite real source supported on {1,...,L}, L>=2, with

    sum_n c(n)/n = 0,
    x_r = sum_(n<=r)c(n)/n, x_0=x_L=0,
    J(c) = sum_(r=1)^(L-1) x_r^2.

The last identity with the whole physical source norm follows from
1/max(r,s)=min(r,s)/(rs); it is the inherited NIR26 innovation isometry.
No coefficient cap, multiplicativity, or Möbius assumption is imposed yet.
Use ordinary Dirichlet convolution and put

    z(d)=(c*c)(d),      B_q=sum_(q|d)z(d)/d.

For 0<alpha<1 define the FULL centered harmonic mode

    Z_alpha(k)=sum_(n=1)^k exp(2*pi*i*n*alpha)/n
                            +log(1-exp(2*pi*i*alpha)).       (1.1)

The logarithm is the radial Abel value, equivalently
Z_alpha(k)=-sum_(n>k)exp(2*pi*i*n*alpha)/n. This converges by Dirichlet's
test. The centering constant is not optional.

Fix integers H>=1, X>=8H, and X<=M<2X. Assume L^2<=8X. Let chi_H(t) be 1
on [0,H], zero on [2H,infinity), and on H<t<2H be

    chi_H(t)=1-10u^3+15u^4-6u^5, u=(t-H)/H.

It is C^2, between zero and one, nonincreasing, and flat through its second
derivative at both ends. Define the real microscopic contribution

    U(k)=sum_(q=2)^(L^2) B_q
            sum_(1<=a<q,gcd(a,q)=1)
                  chi_H(X*||a/q||) Z_(a/q)(k),               (1.2)
    ||alpha||=min(alpha,1-alpha).

Every available denominator is admitted; the smooth numerator mask alone
selects the contribution. It has weight one for ||a/q||<=H/X. Its entire
transition to zero at 2H/X is included in (1.2).

Set

    a0=max(0,floor(X/(2HL))-1),
    E_local=sum_(r=a0+1)^(L-1) x_r^2,
    theta=27/164, p=2+2theta=191/82.

**MHB32-1 (bandwidth theorem).** Uniformly under these hypotheses,

    sum_(k=X)^M |U(k)|^2 <= 2^60 H^(191/82) E_local^2.       (1.3)

Together with the unchanged MCB31 estimate, one may use the MINIMUM of
2^60 H^(191/82) and 2^21 H^4 as the multiplying factor. The new large constant
means that a smaller exponent is not a numerical improvement at the tested
small bandwidths. Both estimates are generic in c. Native inversion will
identify their output but does not supply a new input-energy exponent.

## 2. Unreduce the frequencies before taking a norm

For 0<t<=2H put

    z_Xk(t)=2 Re Z_(t/X)(k)
       =2 sum_(n<=k) cos(2*pi*n*t/X)/n
                               +2 log(2 sin(pi*t/X)),
    g(t)=chi_H(t) z_Xk(t).

Extend g by zero above 2H. There is no ambiguity at a half-turn: 2H/X<=1/4.
Let

    f(d)=sum_(j>=1) g(jX/d), d>0,     f(0)=0.                (2.1)

For every fixed d the sum is finite. A numerator j/d reduces uniquely to a/q
with q|d. Expanding B_q and pairing conjugate numerators proves EXACTLY

    U(k)=sum_(r,s<=L) c(r)c(s)/(rs) f(rs).                  (2.2)

Thus there are no independent replacement amplitudes or missing product
collisions. Since c(r)/r=x_r-x_(r-1), two finite summations by parts give

    U(k)=sum_(r,s<L) x_r x_s
        [f(rs)-f((r+1)s)-f(r(s+1))+f((r+1)(s+1))].          (2.3)

The square-bracketed term is the integral of f'(uv)+uv f''(uv) over the
unit rectangle [r,r+1] x [s,s+1]. The sign is positive because both finite
differences have the same reversed orientation. The C^2 cutoff makes f C^2
through every entry/exit of a summand in (2.1).

Also f(d)=0 for d<=X/(2H). For r<=a0 and s<L, the ENTIRE rectangle has
uv<=(r+1)L<=X/(2H). All such rows/columns vanish. Hence (2.3) is unchanged
if x_r is set to zero for r<=a0. Write x(u)=x_floor(u) on the remaining
unit cells, zero elsewhere. Its support is in [1,L], and

    integral |x(u)|^2 du=E_local,
    U(k)=integral integral x(u)x(v)[f'(uv)+uv f''(uv)]du dv. (2.4)

This localization is performed in the original exact kernel, BEFORE a
rank-one term and its remainder are separately estimated below.

## 3. The centering correction and exact Mellin–Hankel identity

Put

    A_g=integral_0^infinity g(t)dt,
    G(s)=integral_0^infinity g(t)t^(s-1)dt,
    f0(d)=f(d)-(A_g/X)d.                                  (3.1)

Near zero g(t)=O(1+|log t|), g'(t)=O(1/t). G is holomorphic on Re s>0.
The subtraction in f0 is indispensable. In particular reciprocal balance
of c does NOT imply sum c(n)=0.

### A complete Müntz calculation for this logarithmic kernel

For v>0, integration by parts against the counting function gives

    sum_(j>=1)g(jv)-A_g/v
                  =integral_0^infinity {t/v}g'(t)dt.       (3.2)

The lower boundary t*g(t) tends to zero; the upper boundary vanishes by
compact support. For 0<sigma<1, Fubini is absolutely justified by

    integral_0^infinity |g'(t)|t^sigma dt < infinity,
    integral_0^infinity {w}w^(-sigma-1)dw < infinity.

The latter integrability uses {w}<=w near zero and {w}<=1 at infinity.
Euler summation, or its direct cell-by-cell derivation, gives the classical
identity

    integral_0^infinity {w}w^(-s-1)dw=-zeta(s)/s,
                                                   0<Re s<1.

Integrating (3.2) against v^(s-1) and using
integral t^s g'(t)dt=-sG(s) therefore yields

    integral_0^infinity f0(d)d^(-s-1)dd
                           =X^(-s) zeta(s)G(s).           (3.3)

The same absolute Fubini bound proves integrability of the left side with
f0 replaced by |f0| at each fixed sigma in (0,1). No divergent uncentered
Mellin integral is being used. The general Müntz mechanism is classical;
this derivation checks its hypotheses for the logarithmic kernel at hand.

### Hankel, rather than orthogonal diagonalization

Use the Fourier convention hat h(tau)=integral h(w)exp(-i*tau*w)dw, and let

    s=1/2+i*tau,
    K(w)=exp(w/2)[f0'(exp w)+exp(w) f0''(exp w)].

Equation (3.3) and differentiation in the sense of tempered distributions give

    hat K(tau)=s^2 X^(-s) zeta(s)G(s).                    (3.4)

Indeed, for F0(w)=exp(-w/2)f0(exp w), K=(D+1/2)^2 F0. F0 is L1 by the
absolute bound just proved. This distributional formulation avoids assuming
an unproved absolutely integrable bound on K itself.

Set h(w)=exp(w/2)x(exp w). Then ||h||_2^2=E_local. The exact bilinear identity is

    U(k)=(A_g/X)(integral x(u)du)^2
        +(1/(2pi)) integral_R hat h(tau)^2 hat K(-tau)dtau. (3.5)

The square is hat h(tau)^2, NOT |hat h(tau)|^2. This is a Hankel form (the
physical kernel depends on a sum of logarithms), not a positive Fourier
energy. In particular, signs and phases remain in the exact identity.

For rigor, first take smooth compactly supported h. Equation (3.5) is the
distributional Fourier pairing with h*h. Section 4 bounds hat K uniformly.
Approximation then extends the right side continuously in L2. With supports
in one compact interval, h_n*h_n converges uniformly to h*h by Cauchy–Schwarz;
K is locally continuous, so the ordinary integral on the left converges too.
This proves (3.5) for our piecewise constant source. The Fourier integral is
absolutely bounded by ||hat K||_infinity ||h||_2^2.

### Relation to the actual Dirichlet polynomial

Without local row removal, write C(s)=sum c(n)n^(-s). Summation by parts gives

    hat h(tau)=C(s)/(s-1),       integral x=-sum c(n).

Using 1-s=conjugate(s), (3.5) becomes

    U(k)=(A_g/X)(sum c(n))^2
      +(1/(2pi)) integral_R C(1-s)^2 X^(-s)zeta(s)G(s)dtau. (3.6)

This is the promised exact link with the Mellin formulation in #905. It is
not obtained by commuting a rational-angle mask with a Mellin projection.
The full C is retained; replacing it by 1/zeta would be an unsupported
assumption about the limit of truncated inverse series.

As an exact finite control, take g(t)=(1-t)^4 for 0<t<1, zero thereafter,
X=1, and c=delta_1-2delta_2. Then A_g=1/5 and G(s)=24/[s(s+1)...(s+4)].
The source sum is 33/128, the centered part is 37/640, and the missing
rank-one term would be 1/5. Thus even a balanced source gives a nonzero
correction. The checker verifies these rational values independently of
any numerical Mellin quadrature.

## 4. Uniform oscillatory bounds for the symbol

The following estimates are the analytic improvement over termwise absolute
differentiation. They hold uniformly in X<=k<2X, X>=8H, H>=1:

    |s G(s)| <= 2^10                       for all real tau,
    |s G(s)| <= 2^14 H^(3/2)/tau^2         if |tau|>=64H. (4.1)

### Elementary mode and cutoff bounds

Dirichlet summation of the complete tail in (1.1), and
sin(pi*t/X)>=2t/X for t<=X/2, give |z_Xk(t)|<=1/t. The exact derivative is

    z_Xk'(t)=(2pi/X) cos((2k+1)pi*t/X)/sin(pi*t/X).       (4.2)

The logarithmic centering term is required for this cancellation. Therefore,
with D=t*d/dt,

    |Dz|<=4,       |t^2 z''|<=64t+8,
    |D^2z|<=64t+12,
    |z(t)|<=1+4|log t| for 0<t<=1.                     (4.3)

For example the first bound follows from pi<4, and differentiation of (4.2)
gives the next one since (2k+1)pi/X<4pi<16. The last follows by integrating
|z'|<=4/t from 1. For the cutoff, direct differentiation of its polynomial gives

    |chi'|<=2/H, |chi''|<=6/H^2, |chi'''|<=60/H^3.       (4.4)

The third derivative bound is piecewise; only its integrability is used.

### A bounded oscillatory primitive

For every real tau, lambda>=1, and T>0,

    |integral_0^T t^(-1/2+i*tau) exp(+/-i*lambda*t)dt|<=64. (4.5)

Here is an elementary proof including the possible stationary point. Scaling
reduces to lambda=1 at a cost lambda^(-1/2)<=1, and conjugation leaves the
phase phi(t)=t+tau log t. On an interval where phi' is monotone and has one
sign with |phi'|>=d, one integration by parts bounds its exponential primitive
by 2/d; Abel summation with a decreasing positive amplitude consequently costs
at most 4 times its initial amplitude divided by d.

For tau>=0, bound [0,1] absolutely by 2 and use phi'>=1 on [1,T]. For tau=-A,
0<=A<=4, bound [0,8] absolutely by 2sqrt(8)<6 and use phi'>=1/2 afterwards.
For A>4 split at A/2, A-sqrt(A), A+sqrt(A), and 2A, intersecting each piece
with (0,T). Before A/2, integrate with t^(-1/2)/phi'=-sqrt(t)/(A-t);
its boundary and total variation cost at most 2sqrt(2)/sqrt(A). On
[A/2,A-sqrt(A)], |phi'|>=1/sqrt(A), costing at most 4sqrt(2). The stationary
interval has absolute cost at most 2sqrt(2). On [A+sqrt(A),2A],
phi'>=2/(3sqrt(A)), costing at most 6. Beyond 2A the cost is at most
8/sqrt(2A). Every partial interval satisfies the same bounds. Their sum is
less than 64. This proves (4.5), without using a stationary-phase asymptotic.

### The first estimate in (4.1)

Integration by parts gives

    sG(s)=-I0-Ichi,
    I0=integral chi(t)t^s z'(t)dt,
    Ichi=integral chi'(t)t^s z(t)dt.

Put lambda=(2k+1)pi/X and

    a(t)=chi(t) a_base(t),
    a_base(t)=(2pi*t/X)/sin(pi*t/X).

On 0<t<=2H, 2<=a_base<=4 and a_base increases. Hence the total variation
of a is at most 6. Equation (4.2) identifies I0 with
integral a(t)t^(-1/2+i*tau)cos(lambda*t)dt. Stieltjes integration by parts
and (4.5) give |I0|<=384. Also (4.3)–(4.4) give

    |Ichi| <= (2/H) integral_H^(2H)t^(-1/2)dt <2.

Thus |sG|<2^10.

### Complete high-tau estimate

For a_base, elementary differentiation with w=pi*t/X<=pi/4 gives

    |a_base|<=4, |Da_base|<=4, |D^2a_base|<=24.

One can check this from Da_base=a_base(1-w cot w),
0<=1-w cot w<=1, and |D(1-w cot w)|<=5. With (4.4),

    |a|<=4, |Da|<=20, |D^2a|<=168.

In logarithmic coordinates u=log t, let q(u)=exp(u/2)a(exp u). Its complete
L1 derivative bounds are

    ||q||_1<=12sqrt(H), ||q'||_1<=64sqrt(H),
    ||q''||_1<=535sqrt(H).                                (4.6)

For instance q''=sqrt(t)(a/4+Da+D^2a), and the integral of sqrt(t)du from
0 to 2H is 2sqrt(2H). The other bounds follow in the same way.
The phases in I0 are tau*u +/- lambda*exp(u). When |tau|>=64H, their
first derivatives have magnitude at least |tau|/2, while the absolute
second and third derivatives are at most |tau|/2. There is no stationary
point in this regime. Twice integrating by parts bounds each exponential by

    [4||q''||_1+12||q'||_1+16||q||_1]/tau^2
                                <2^12 sqrt(H)/tau^2.       (4.7)

To verify the constants, with p=phi', the differentiated amplitude is
q''/p^2-3q'p'/p^3-qp''/p^3+3q(p')^2/p^4. The boundary terms vanish because
q,q' tend to zero at -infinity and chi,chi' vanish at the upper endpoint.

For Ichi, set b(t)=t chi'(t). Its log-coordinate amplitude is
qchi(u)=sqrt(t)b(t)z(t). On H<=t<=2H,

    |b|<=4, |Db|<=28, |D^2b|<=556.

Indeed D^2b=t chi'+3t^2 chi''+t^3 chi'''. Equations (4.3)–(4.4) give

    |D^2(sqrt(t)b z)| <=1385 H sqrt(t),
    ||qchi''||_1 <= 2^11 H^(3/2).

Explicitly the coefficient is
bD^2z+(2Db+b)Dz+(D^2b+Db+b/4)z; its absolute value is at most
560H+240+585/H<=1385H. The integral of sqrt(t)du on [H,2H] is less than
sqrt(H). Both qchi and qchi' vanish at the endpoints. Two ordinary Fourier
integrations by parts therefore cost at most 2^11 H^(3/2)/tau^2.
Combining this with (4.7) proves the second bound in (4.1).

### Imported zeta bound and final symbol norm

Use precisely the unconditional Patel–Yang theorem, arXiv:2302.13444v1:

    |zeta(1/2+i*tau)| <= (667/10)|tau|^(27/164), |tau|>=3. (4.8)

This is an IMPORTED theorem, not independently reproved here. Its exact
statement is given on the primary arXiv abstract. It is also used by DMC31
on #905. We make no claim that it is the latest or best available estimate.
For |tau|<=3, Euler summation gives the elementary bound |zeta(s)|<=16:
use zeta(s)=1/(s-1)+1-s integral_1^infinity {x}x^(-s-1)dx and Re s=1/2.

For |tau|<=64H, use |s|<=65H, (4.1), and (4.8) or the small-height bound.
For |tau|>=64H, use the second line of (4.1), |s|<=2|tau|, and
|tau|^(theta-1)<=(64H)^(theta-1). These give the uniform conservative bound

    sup_tau |s^2 zeta(s)G(s)| <=2^28 H^(1+theta).          (4.9)

At high tau the actual resulting power is H^(1/2+theta), smaller than the
one displayed. Thus the entire Mellin tail, not a finite integral, is paid.
From (3.4),

    ||hat K||_infinity<=2^28 X^(-1/2)H^(1+theta).          (4.10)

## 5. Finish the component bound, with the rank-one price retained

Equations (4.3) and |z(t)|<=1/t show

    |A_g|<=5+log(2H)<=8H.

The first term in (3.5) is therefore at most

    (8H/X)L E_local <=32H X^(-1/2)E_local,

by Cauchy–Schwarz and L^2<=8X. The second is at most
2^28 X^(-1/2)H^(1+theta)E_local by Plancherel and (4.10). Thus

    |U(k)|<=2^29 X^(-1/2)H^(1+theta)E_local.

There are at most X integer observations in [X,M]. Squaring proves (1.3),
with the advertised slack from 2^58 to 2^60. No covariance was discarded:
the bound was applied after the entire frequency and product sums.

This closes the adapter/centering/whole-tail obligations for this particular
Mellin representation. It does NOT close the arithmetic estimate that would
replace E_local^2 by a smaller power on the native inputs.

## 6. Native recent-energy assembly and a complete covariance inequality

### The same native sources and complete completion price

For a global cutoff Y let b=Y+1, B=b^2-1. Partition b,...,B into
[X_j,M_j], X_j=b*2^j, M_j=min(2X_j-1,B). Set y_j=floor(sqrt(M_j)).
Then y_j<=Y and M_j<(y_j+1)^2. Use the inherited cap-three reciprocal
completion of the native prefix through y_j, supported through L_j<=2y_j.
For X_j>=8 it satisfies L_j<=X_j and L_j^2<8X_j.

The classical short-source Newton identity

    mu-(2c-1*c*c)=mu*(delta-1*c)*(delta-1*c)

makes its output exactly native below (y_j+1)^2. Its reciprocal output on
the observation block is m(k)=-sum_q B_q Z_q(k), since m_c(k)=0 there.
This follows by divisor expansion of the finite Newton expression and
harmonic summation; all prime-power logarithms cancel only in the full sum.
The cutoff sources use no future mu values. Each complete source and mask is
transformed first, and only then restricted to its own block. No blockwise
stitched source is substituted inside a nonlocal transform.

For any integer H with 1<=8H<=b define

    Delta_j=F_(y_j)-F_max(0,floor(y_j/(8H))-1),
    Delta_max=max_j Delta_j,
    N_H=12+2ceil(log_2 H).

The clipped-completion tail has energy at most
F_(y_j)-F_floor(y_j/2). This is the inherited PCR26/MCB31 paid completion
estimate, which follows by comparing its monotone residual to the reversed
last native increments. Since X_j>y_j^2/2 and L_j<=2y_j, the localized
native part in (1.3) is contained in Delta_j. The completion tail is also
bounded by Delta_j, so E_local,j<=2Delta_j.

Each fixed r can occur in only N_H of these windows. Indeed participation
implies r<=y_j<8H(r+1)<=16Hr, whereas y_j^2/2<X_j<(y_j+1)^2. Hence
r^2/2<X_j<(17Hr)^2, which permits fewer than N_H dyadic scales.
Consequently

    sum_j Delta_j<=N_H F_Y,
    sum_j Delta_j^2<=N_H F_Y Delta_max.

Applying (1.3) on the disjoint observation blocks proves

    ||U||_[b,B]^2 <=2^62 H^(191/82) N_H F_Y Delta_max.       (6.1)

This is the same complete band contribution as MCB31, with a different
bandwidth budget. No sublinear bound on Delta_max in terms of F_Y has been
proved. In particular Delta_max<=F_Y only gives exponent two.

### Every remaining frequency included, but with a visible cutoff loss

For a fixed native block, use the exact complementary mask 1-chi_H.
It is supported on ||alpha||>=H/X and its magnitude is at most one.
NCL29's proof bounds arbitrary such weighted coefficients: its Fourier
coefficient-square majorant only decreases after multiplication by a weight
of magnitude at most one. Thus its complete far-component bound applies:

    ||V||_[X,infinity)^2 <=2^21 K^4 (X/H) H_L^9.            (6.2)

This imports NCL29's component estimate, with the weight extension just
explained, not a new frequency-orthogonality assertion. The exact equality
m=-U-V on [X,M] retains every numerator, denominator, centering constant,
and their covariance. Therefore

    sum_(k=X)^M m(k)^2
       <=2^61 H^(191/82) E_local^2
                              +2^22 K^4 (X/H) H_L^9.     (6.3)

This is a full native-block upper inequality, not an estimate with an
unmentioned remainder. Its X/H term prevents an RH-strength conclusion.

### Optimizing the proved inequality, and its precise limitation

For the native cap-three source write F=F_y, y=floor(sqrt(M)). Up to an
absolute constant, choose integer H nearest above

    (X/(1+F)^2)^(82/273),

when this lies in the allowed range. Absorb a fixed finite range of X into
the constant. If 1+F>=sqrt(X), use the elementary native bound |m(k)|<=1
instead. (It follows from sum_(n<=k)mu(n)floor(k/n)=1 and |mu|<=1.)
For 1+F<sqrt(X), the displayed H is >=1 and <=2X^(82/273), hence <=X/8
for all sufficiently large X. With E_local<=2F and H_L<=C(1+log X), (6.3)
gives the genuine full-block estimate

    sum_(k=X)^M m(k)^2
       <= C (1+log X)^9 X^(191/273)(1+F_y)^(164/273).     (6.4)

The earlier H^4 tradeoff instead yielded the schematic powers X^(4/5)
and (1+F_y)^(2/5). The new exponents are not new zero-free exponents.
The exact identity

    191/273+(164/273)/2=1

shows that the elementary scale F_y of order sqrt(X) still leads only to
an X-scale upper bound. More generally inserting F_y<=y^kappa changes the
output power in X to (191+82kappa)/273. The fixed point is kappa=1, and
for kappa<1 this bound alone is weaker than kappa. It cannot bootstrap RH.

Summing (6.4) over the square step, using F_y<=F_Y and a geometric sum
of X_j^(191/273), gives

    F_B <= F_Y+C(1+log Y)^9 Y^(382/273)(1+F_Y)^(164/273).  (6.5)

The explicit positive power of Y remains. Stating (6.5) is not a substitute
for the desired cutoff-subpower, input-subquadratic recurrence.

## 7. Why the complete remaining gap has not closed

The generic MCB31 sharpness family continues to apply at fixed H. It rules
out a uniform improvement of the input exponent below two based only on
reciprocal balance, coefficient caps and the input energy. This packet neither
refutes that family nor claims its phase pattern occurs for mu.

The exact equation (3.6) shows the additional structure a native argument
could use: the complex square C(1-s)^2 and its coherent interaction with
zeta(s)G(s). Bounding the multiplier by its absolute supremum forgets those
phases. Replacing the square by a modulus square is not an identity, and
replacing finite C by reciprocal zeta assumes the missing continuation.

The parameterized complete bound (6.3) accounts for the intermediate-frequency
contribution, but only at a positive power cost. The two outstanding issues
are therefore still a native gain at the critical quadratic input threshold,
and a sufficiently mild budget across all bandwidths. Combining #904 and
#905 by name or commuting their projections supplies neither.

## 8. Finite evidence and validation boundary

The new accepting program verifies 120 exact polynomial-kernel source/rank/
mixed-difference fixtures, the nonzero 1/5 rank correction, and the exponent
algebra. It directly evaluates smooth band differences at H=1,2,4 on the
native block [128,255] and H=1,2,4,8 on [512,1023]. All shell covariances
and the exact complementary component are retained; no orthogonality is assumed.
Every local Newton coefficient is checked against a separately produced sieve.

The accepting calculations use the inherited, explicitly authenticated
144-bit outward backend. Enlarging H exposed width inflation in its old
uninterrupted trigonometric rotation: at H=8, y=31 the valid enclosures
became too wide to certify even the generous finite budget. The new evaluator
recomputes exact rational phases every 32 steps and intersects the two valid
enclosures after checking overlap. No midpoint rounding, shrinking without
proof, change of native data, or weakened acceptance predicate is used.

At y=31, X=512, M=1023, descriptive outward values are

    native block energy: 0.0197124703956821...,
    H=1 band energy:     0.0024153077378267...,
    H=2 band energy:     0.0122383776051349...,
    H=4 band energy:     0.0172392482081484...,
    H=8 band energy:     0.0186124426311633...,
    H=8 complement:     0.0010438750143420...,
    H=8 twice covariance: +0.0000561527501767... .

Individual shell covariances have BOTH signs. The smaller complement in this
finite example is not an asymptotic theorem. These 640 observed cells are two
blocks, not a complete new square step; 1278 coefficient checks count overlap.
The complement is evaluated by the exact full native identity after direct
band evaluation, not by a second exhaustive sum of all unused frequencies.

No finite computation proves (3.3), the multiplier estimate, the imported
sub-Weyl theorem, or an all-scale native gain. The proof and its attribution
are review obligations, distinct from successful local execution.
