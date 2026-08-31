# Actual Xi odd currents: a uniform crossover and separated saddles

Status: PROPOSED ANALYTIC THEOREMS; independent frozen-source review pending.

Scope: the literal real Xi theta kernel, positive odd current orders that may
grow with real source frequency, and scalar current observables. This changes
the current family; it does not change the prescribed physical gauge of a
fixed-order problem. No RH, inner-function, source-Pick, cofinal-capture or
physical Hilbert--Schmidt conclusion is asserted.

Exact parent: the actual-kernel proof at
`3b6972320899a82c6caa3a98e2ada5ff703a605a`, especially XL1--XL7,
XL11--XL13 and the source identity preceding XL21. Its fixed-order asymptotic
is not used with a growing order. All growing-order estimates are below.

Companion computation: `xi_odd_current_scaling.py` authenticates four frozen
sources and enumerates 896 exact current identities, all 31 odd-order
successor comparisons through K=63, and nine Gaussian moment/translation
identities. Its fixture declares the full finite panel. The separate theta
scout uses explicitly non-directed, bounded high-precision quadrature.
Neither establishes the analytic theorem from a finite table.

Smallest remaining acceptance gap: independent review of the uniform tail
estimates and the separated-saddle normalization, followed by exact replay.

## 1. Literal source and two scales

Write E=exp(xi), epsilon=(pi E)^(-1/2), delta=epsilon/xi and
kappa=K delta, where xi>0 and K is a positive odd integer. Keep

    H_xi(d)=Phi_Xi((xi-d)/2) Phi_Xi((xi+d)/2),
    W_(K,xi)(d)=d[((xi+d)/2)^K-((xi-d)/2)^K],
    dmu_(K,xi)(d)=W_(K,xi)(d) H_xi(d) dd / Z_(K,xi).

Here Phi_Xi is the full-line Fourier kernel of Xi, twice the historical
half-kernel. It is even and strictly positive. The parent proves, on the
ENTIRE real d-line,

    0 < H_xi(d)/H_xi(0) <= 9 exp[-2pi E(cosh d-1)]
                            <= 9 exp[-pi E d^2].                 (1.1)

The current is positive away from zero. All normalizations below exist.
The full-line factor of two cancels from these normalized observables.

For x real set

    P_K(x^2)=[(1+x)^K+(1-x)^K]/2,
    Q_K(x^2)=[(1+x)^K-(1-x)^K]/(2x),
    F_K(x)=Q_K(x^2)/K,

with continuous values at x=0. These are even positive polynomials. An
identity especially useful when the degree grows is

    F_K(x)=(1/2) integral_(-1)^1 (1+t x)^(K-1) dt.              (1.2)

Consequently P_K(x^2), F_K(x) >=1 and both are at most exp(K|x|).
The pushforward nu_(K,xi) of mu by u=d/epsilon has density proportional to

    u^2 F_K(delta u) R_xi(u),
    R_xi(u)=H_xi(epsilon u)/H_xi(0).                          (1.3)

Thus kappa controls the first crossover, at K comparable to xi exp(xi/2).
A second parameter b=K/(xi E) controls macroscopic separation, at K
comparable to xi exp(xi). Neither is the physical companion parameter lambda.

## 2. Uniform compact-kappa theorem

Define sinhc(z)=sinh(z)/z, sinhc(0)=1, and the probability density

    p_kappa(u)=(2/sqrt(pi)) exp(-kappa^2/4)
               u^2 sinhc(kappa u) exp(-u^2).                 (2.1)

For every fixed A,T>=0 and integer m>=0 there are finite constants C and
xi_0, depending only on A,T,m, such that, for xi>=xi_0 and EVERY positive
odd K with 0<=kappa<=A,

    integral (1+|u|^m) exp(T|u|)
       |density(nu_(K,xi))(u)-p_kappa(u)| du
       <= C [delta+E^(-1)].                                 (2.2)

The theorem includes fixed K and sequences K tending to infinity. Its
comparison density uses the actual kappa at each xi, not a rounded limit.

### Proof: the kernel error is uniform and includes the exterior

For |d|<=1 and xi>=2, the parent's first-orbit expression writes the exact
kernel ratio as

    exp[-2pi E(cosh d-1)] B_xi(d),
    B_xi(d)=theta_*(Ee^d) theta_*(Ee^-d)/theta_*(E)^2,
    theta_*(X)=1-3/(2pi X)+r(X),
    0<=r(X)<= (512/31) exp(-3pi X).

In this region |B_xi(d)-1|<=C/E. Also

    0<=2pi E(cosh(epsilon u)-1)-u^2<=C u^4/E

when |epsilon u|<=1. Since 1-exp(-v)<=v for v>=0, this yields

    |R_xi(u)-exp(-u^2)|
       <= C E^(-1)(1+u^4) exp(-u^2)                         (2.3)

on that region. Outside it, (1.1) bounds the difference by
10 exp(-u^2). Integrating this tail, with any fixed polynomial and
exp(C_0|u|), contributes O(E^(-1)). This proves the corresponding weighted
L1 kernel estimate without discarding the unbalanced source region.

### Proof: resumming the current rather than fixing its degree

When |delta u|<=1/2, use |log(1+y)-y|<=y^2 for |y|<=1/2.
For P_K this compares the two powers to exp(+/-kappa u), with error bounded
by C_A delta u^2 exp[A|u|+A delta u^2]. For (1.2), the exponent differs
from kappa t u by at most delta(|u|+A u^2), uniformly in |t|<=1.
It follows that F_K(delta u) differs from sinhc(kappa u) by at most

    C_A delta (|u|+u^2)
         exp[(A+1)|u|+A delta u^2].                         (2.4)

Choose xi_0 so A delta<=1/4. Products with the Gaussian, fixed polynomial
weights and exp(T|u|) are integrable with a common majorant. On the omitted
region |u|>1/(2delta), the exact bound exp(A|u|) for P_K and F_K, and the
same bound for cosh and sinhc, make the Gaussian tail O(delta).
Thus the weighted L1 errors for the current factors are O(delta).

Combining (2.3)--(2.4) gives the weighted L1 error for the unnormalized
density in (1.3). Its comparison normalization is exactly

    integral u^2 sinhc(kappa u) exp(-u^2) du
       = sqrt(pi) exp(kappa^2/4)/2.                         (2.5)

It is bounded below independently of kappa, and bounded above for kappa<=A.
The exact normalization is therefore also uniformly bounded away from zero
for sufficiently large xi. Dividing establishes (2.2). QED.

## 3. Moments, gain and translated current

The comparison law has moment generating function

    M_kappa(t)=exp(t^2/4)
       [cosh(kappa t/2)+(t/kappa)sinh(kappa t/2)],           (3.1)

with continuous value exp(t^2/4)(1+t^2/2) at kappa=0.
This follows by differentiating the ordinary Gaussian integral before
normalization. In particular,

    E_(p_kappa)[u^2]=3/2+kappa^2/4,
    E_(p_kappa)[u^4]=15/4+5kappa^2/4+kappa^4/16.             (3.2)

More generally, if D_0(x)=1 and D_(n+1)=D_n'+xD_n/2, the 2q-th moment is
2D_(2q+1)(kappa)/kappa, continuously interpreted at zero. These are
polynomials in kappa^2, not an inferred finite-moment law.

Retain the parent's exact scalar definitions g_K and p_K. Cancelling Q_K
before taking a limit gives

    K g_K/(pi xi^2 E)
      =(1/2) [integral P_K(delta^2 u^2) R_xi(u) du]
               /[integral u^2 F_K(delta u) R_xi(u) du],
    2K p_K
      =[integral u^2 P_K(delta^2 u^2) R_xi(u) du]
               /[integral u^2 F_K(delta u) R_xi(u) du].     (3.3)

Uniformly for kappa<=A, (2.2) and its proof imply

    K g_K/(pi xi^2 E)=1+O_A(delta+E^(-1)),
    2K p_K=1+kappa^2/2+O_A(delta+E^(-1)).                   (3.4)

These leading uniform statements do not claim the parent's finer fixed-K
second coefficient uniformly. At K=1 the exact p_1=1/2 remains unchanged.

For the literal untranslated current, let tau=h epsilon. Its exact source
identity is J_(K,h)/(hL_K)=E_mu[sinhc(hd)], extended at h=0.
For every fixed A,T and |tau|<=T, the uniform theorem gives

    J_(K,h)/(hL_K)
       =exp(tau^2/4) sinhc(kappa tau/2)
          +O_(A,T)(delta+E^(-1)).                         (3.5)

Indeed multiply (2.1) by sinhc(tau u); the two u denominators cancel and
the Gaussian integral of sinh(kappa u)sinh(tau u) gives the displayed
formula, including either zero parameter by continuity. The reciprocal
current ratio is consequently

    r_sharp=exp(-tau^2/4)/sinhc(kappa tau/2)
                +O_(A,T)(delta+E^(-1)).                  (3.6)

For eta=lambda xi/2, the parent identity rho=g/eta+(p-g)eta remains exact.
If eta=1+w/(pi xi^2 E) with w in a fixed compact interval, then

    2K rho=1+kappa^2/2-4w+O_(A,w)(delta+E^(-1)).             (3.7)

This is a scalar parameter evaluation, not a Fourier-multiplier substitution
into a physical fixed-lambda index theorem.

## 4. Separated-saddle theorem

Now assume xi tends to infinity, kappa tends to infinity, and

    0 < b=K/(xi E) <= B                                   (4.1)

for some fixed B. The positive number a=a_(K,xi) is defined BEFORE any
numerical fitting as the unique solution

    K/(xi+a)=2pi E sinh a.                                (4.2)

Uniqueness follows because the left side decreases and the right side
strictly increases from zero to infinity. Define

    J=2pi E cosh a+K/(xi+a)^2.                            (4.3)

Condition mu on d>0, which has probability exactly 1/2. Under this
conditional law, v=sqrt(J)(d-a) tends to the standard normal distribution.
The convergence holds in L1 with every fixed weight
(1+|v|^m) exp(T|v|). The negative half is its exact reflection.

Moreover,

    E_mu[d^(2q)]/a^(2q) ->1       (each fixed q>=1),
    2a g_K/xi ->1,
    2xi p_K/a ->1.                                        (4.4)

These assertions are sequentially uniform under (4.1) and kappa->infinity:
no fixed positive lower bound on b is required.

### Proof: localization and an exact centering

Put

    L(d)=K log(xi+d)-2pi E cosh d,   d>0.

It has its unique maximum at a, and L''(d)<=-2pi E globally. Under (4.1),
a is bounded above by a constant depending only on B. From (4.2) and the
boundedness of sinh(a)/a, a sqrt(E)>=c_B kappa, hence a sqrt(E)->infinity.
Also J/E is bounded above and below by positive constants depending on B.

On each fixed v-interval, Taylor expansion gives

    L(a+v/sqrt(J))-L(a) -> -v^2/2.                         (4.5)

The cubic remainder is uniform there: L'''(d)=2K/(xi+d)^3-2pi E sinh d,
and its ratio to J^(3/2) tends to zero in the indicated neighborhood.
The lower endpoint v=-a sqrt(J) tends to negative infinity.

For d>0 set r(d)=(xi-d)/(xi+d), so |r|<1. Exactly,

    W_(K,xi)(d)=2^(-K) d(xi+d)^K [1-r(d)^K].               (4.6)

The bracket lies between zero and two. In the neighborhood (4.5), d/a->1,
the kernel first-orbit correction tends uniformly to one, and

    |r(d)|^K <= exp[-2Kd/xi] ->0,                         (4.7)

where that neighborhood has d<xi and Kd/xi>=c_B kappa^2.
The local rescaled density therefore tends to exp(-v^2/2).

For global domination, the parent bound (1.1), (4.6), and strict concavity
give a constant times

    (d/a) exp[-pi E(d-a)^2]
       <= (1+|v|) exp(-c_B v^2)                          (4.8)

for sufficiently large xi, because a sqrt(J)->infinity. This includes
d>=xi, where a balanced first-orbit asymptotic was NOT used.
Local normalization is positive and the majorant is integrable with all
the stated weights. Dominated convergence proves the conditional normal
law and the weighted L1 assertion.

For the scalar ratios one also needs the integral without the factor d.
Apply exactly the same argument to the positive integrands

    (xi+d)^K [1+r(d)^K] H_xi(d),
    d^r (xi+d)^K [1-r(d)^K] H_xi(d)  (fixed r>=0).

Both brackets are nonnegative and at most two; both tend to one locally.
After division by a^r their rescaled integrals have the same Gaussian
normalization. Thus, writing I_r^+/- for these half-line integrals,

    I_r^+/- / (a^r I_0^+) ->1.                           (4.9)

The parent's exact definitions become

    g_K=(xi/2) I_0^+/I_1^-,
    p_K=(1/(2xi)) I_2^+/I_1^-.

Equation (4.9) proves (4.4), without invoking a singular inverse-d moment.
QED.

## 5. Macroscopic separation and the original untranslated observable

If in addition b->b_0>0, then (4.2) gives

    a -> a_0=arsinh(b_0/(2pi)),
    mu_(K,xi) -> (delta_(-a_0)+delta_(a_0))/2,
    J/E ->2pi cosh(a_0).                                 (5.1)

The exact centering a in (4.2) is essential for the normal limit. Centering
at a_0 generally leaves an O(1/xi) error, much larger than E^(-1/2).
No rate of b->b_0 was assumed, so even that O(1/xi) comparison is not
asserted for arbitrary sequences b; the exact center avoids the issue.

For fixed bounded real h, (4.8) also gives uniform integrability and

    J_(K,h)/(hL_K) -> sinhc(h a_0),
    r_sharp ->1/sinhc(h a_0).                             (5.2)

Thus fixed-order source softness does not extend to all growing orders.
The statement is about the changed family of positive odd currents and its
literal scalar readout, not a failure of any fixed-K theorem.

If b->0 while kappa->infinity, then a~K/(2pi xi E). The peaks still merge
on the original d-axis but are separated by increasingly many Gaussian
widths. This intermediate regime links (2.1) to (5.1) without claiming
uniformity at unbounded kappa in the compact-kappa error estimate.

The scalar carrier zero eta_c=sqrt(g/(g-p)) in the macroscopic regime obeys

    xi^2(eta_c-1) -> a_0^2/2.                            (5.3)

For any fixed M>0 the exact interval |rho|<=M has width

    eta_+-eta_-=M/(g-p) ~2a_0 M/xi.                      (5.4)

These polynomial scalar widths replace the fixed-order exponential width
only because K has changed. They supply no permitted physical gauge change.

## 6. Acceptance and remaining boundaries

The main new analytic inputs are the uniform current resummation (1.2),
the weighted L1 estimates (2.3)--(2.4), and global concavity in the
separated-saddle normalization (4.8). The exact parent theta bound is
retained literally. Independent review must check all four.

An exact producer can check current polynomials, Gaussian derivative
recurrences and scalar algebra. A floating or high-precision theta scout
can test the proposed regimes and centering, but neither establishes the
uniform analytic quantifiers. Directed finite computations, if later
supplied, will be labeled separately.

No claim is made about moment orders increasing with xi, kappa-uniform
compact-regime constants as A->infinity, b unbounded in the saddle theorem,
complex xi, non-real saddles, innerness, actual zero capture, a complete
source map, or a number-field positivity theorem. Classical Laplace and
Gaussian methods are not claimed as new; external priority for this
particular actual-Xi growing-order formulation has not been established.
