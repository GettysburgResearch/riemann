# Reciprocal gamma continuation: certified strip failure and a variance-scale repair

Date: 2026-09-10. Local labels GFC1--GFC5 are **PROPOSED**, pending independent
mathematical and code review. This is new research, not integration or acceptance.
**RH and the expanding-window zero-confinement theorem remain unproved.**

Source: PR #849 at `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`,
`standalone/2026-09-10-reciprocal-gamma-cascade/PROPOSAL.md`, Git blob
`c324ba15d3f7f3e073b902042ec61c685b555f53`. That complete manuscript was read;
its bytes agree with the earlier delivered source. No parent executable or
uploader full-checkout receipt is represented as a new execution here.

## 1. What changed in the attempted ending

The parent builds an explicit positive gamma cascade whose reciprocal projections
converge to the entire original xi function. Its first member has a classical
Bessel/Sturm real-zero proof. It proposes controlling zero motion during the
positive gamma steps. This continuation actually tests that motion.

Two full defining-integral certificates prove nonreal zeros of finite sources.
One confirms the previously numerical N=4 observation. The other is **inside the
critical strip** at the exact intermediate parameter u=7/10 of the 2-to-3 step.
Thus a claim that this whole continuous path preserves the critical strip's real
zeros is false. This does not refute the parent's weaker, asymptotic confinement
target and does not assert a nonreal xi zero.

There is a positive replacement. Keeping the entire omitted tail's mean, instead
of deleting it, gives explicit nonnegative compactly supported reciprocal kernels
with full horizontal-strip convergence O_R(N^-3). We also justify the parent's
previously formal translation model for the original cascade: the complete
random-tail error is O_R(N^-3), and the first deterministic drift is an explicit
imaginary-step difference of xi. Neither faster convergence nor this exact drift
proves zero confinement. They make that attempted spectral problem better specified.

## 2. Source, coordinates and classical input

Let G_n be independent Gamma(shape 2, rate 1) variables. Put

    X_N = sum_(n<=N) G_n/n^2,       X = sum_(n>=1) G_n/n^2,
    tau_N = E(X-X_N) = 2 sum_(n>N) n^-2,
    v_N = Var(X-X_N) = 2 sum_(n>N) n^-4.

These gamma variables describe an exact analytic probability law, not random
primes or random zero ordinates. Let f_N and f be the densities. The classical
Biane--Pitman--Yor representation, in this scaling, gives

    E X^s = 2 pi^s xi(2s),
    f(x) = sum_(n>=1) (4n^4 x-6n^2) exp(-n^2 x),                 (2.1)
    f(pi^2/x) = (x/pi)^(5/2) f(x).

The series is analytic on Re x>0. Jacobi transformation proves the last identity
there with the principal power, not just as a formal real asymptotic. Define

    x(t)=pi exp(2t),  y(t)=pi exp(-2t),  x(t)y(t)=pi^2,
    h(t)=sqrt(f(x(t)) f(y(t)))=exp(5t/2)f(x(t)),
    Phi(z)=int_R h(t)exp(izt)dt / int_R h(t)dt = Xi(z)/Xi(0).

Here Xi(z)=xi(1/2+iz); the entire completion has xi(0)=xi(1)=1/2.
The ordinary positive square root defines each real-line density. A complex
square-root continuation is used only on explicitly proved zero-free disks in
the numerical argument, never on an unproved global strip.

The parent's original finite function is

    h_N(t)=sqrt(f_N(x(t))f_N(y(t))),
    F_N(z)=int_R h_N(t)exp(izt)dt / int_R h_N(t)dt.              (2.2)

Conditioning on the first Gamma(2,1) summand and telescoping the remaining tilt
proves, for every N and for the full f,

    f_N(x), f(x) <= 4x exp(-x)  (x>0),
    h_N(t), h(t) <= H(t):=4pi exp[-pi cosh(2t)].               (2.3)

The Laplace transform is product_(n<=N)(1+q/n^2)^-2. Its partial fractions and
the fixed-n coefficient limits prove (2.1) and the analytic convergence f_N->f
locally on Re x>0; this uses the complete sum. The parent supplies the detailed
normalization and classical source proof. No theorem concerning zero locations
is imported into the new convergence argument.

## 3. GFC1: two certified nonreal zeros, including a critical-strip flow failure

For distinct positive rational rates a_j, let f_a be the convolution of the
Gamma(2,a_j) densities. The exact formula is

    f_a(x)=sum_j b_j(x+c_j)exp(-a_j x),
    b_j=a_j^2 product_(k!=j)[a_k/(a_k-a_j)]^2,
    c_j=-2 sum_(k!=j)1/(a_k-a_j).                            (3.1)

All b_j are positive. Individual terms need not be positive. The formula follows
by taking both coefficients at every double pole of the rational Laplace
transform; there is no discarded boundary or spectral term.

Form h_a and F_a by (2.2). Each disk below has radius r=10^-6 and exactly one
zero, counted with multiplicity, so the zero is simple:

| Source | Exact center (the displayed decimal is a rational number) |
|---|---|
| a=(1,4,9,16), the actual N=4 approximant | 28.0555855384091825810295021076097455522309 + 2.6219979332686197954925378014004831147962 i |
| a=(1,4,90/7), the actual u=7/10 point of the 2-to-3 step | 26.8135855368140614010181412691765400069731 + 0.4209949404628029929584207065487732398251 i |

The second source is X_2+uG/9, exactly the parent's continuous gamma update.
Its certified disk lies strictly inside 0<Im z<1/2. This is a stronger diagnostic
than the earlier N=4 nonreal root outside that band. Symmetry supplies the
conjugate/reflected disks, but this is not a complete zero census or a certified
parameter-wise pairing of roots. The exploratory collision location was not
turned into a multiple-zero theorem.

### 3.1 Analytic domains for the quadrature remainder

We integrate the unnormalized half-line function

    I_a(z)=int_0^infinity h_a(t)cos(zt)dt.

The normalizer is positive and does not affect zeros. Use 256 equal intervals
covering [0,2], each half-width 1/256, and Taylor degree 40 about its exact rational
midpoint. Every complex t disk of radius rho=1/32 about these midpoints supports
the analytic square root required for Cauchy's estimate:

* For x=pi exp(2t), Re x>29/10 and |x|<2 Re x. In (3.1) the a_1=1 term dominates.
  The exact rational bound used by the checker is

      sum_(j>1) (b_j/b_1)
         [2+|c_j|/(29/10)]/[1-|c_1|/(29/10)]
         *2^(-floor((a_j-1)29/10)) < 1/2.                   (3.2)

  This bounds the ratio of the entire remaining sum to the nonzero first term,
  using e>2. It proves f_a(x) has no zero on these disks.

* For y=pi exp(-2t), |Im y|<pi/15. The convolution has the exact simplex formula

      f_a(y)=C y^(m-1) E exp(-y A),
      C=product a_j^2/(m-1)!, m=2*#rates, min a_j<=A<=max a_j.

  A is the positive Dirichlet-simplex average of the rates, with each rate
  repeated twice. After extracting exp[-(min a+max a)y/2], every remaining
  integrand has argument of modulus strictly below pi/2, since max a-min a<=15.
  Its integral has positive real part. Thus f_a(y) is also zero-free.

The estimates on x,y use exp(1/16)<16/15 and |sin(1/16)|<1/16. For example
(31/10)(15/16)(511/512)>29/10 proves the real-part bound. The simplex formula is
an integration identity, not an assumed complex positivity of the density.

The product is nonzero on each simply connected disk. Its unique square-root
branch positive at the real midpoint agrees with h_a along the real subinterval.
The simplex bound also gives |h_a(t)|<=C pi^(m-1)<2^21 there. For each recorded
center |Re z|<29, |Im z|<3, hence |cos(zt)|,|sin(zt)|<e^7<2^12. Multiplication
by t or t^2 costs less than 8. Therefore each of the three integrands for
I,I',I'' has modulus less than 2^36 on the full disks.

The **total** Taylor integration error, for each complex jet, is at most

    E_quad = 2*2^36*(1/8)^41/(1-1/8)
           < 1.478*10^-26.                                (3.3)

The arithmetic evaluates Taylor coefficients by exponential/product/square-root
recurrences with outward fixed-point intervals. Cauchy's estimate pays every
omitted term. It is not an empirical comparison of quadrature meshes.

### 3.2 Entire omitted real-line tail and local zero count

The exact tilt product product_(j>1)(a_j/(a_j-1))^2 is at most 4 for both sources.
Thus (2.3) holds for them. For j=0,1,2 and |Im z|<3, the tail t>=2 is bounded by

    2pi int_(exp4)^infinity v^2 exp(-pi v/2)dv
      =2pi exp(-aV)[V^2/a+2V/a^2+2/a^3],
        a=pi/2, V=exp4,
      < 6.924*10^-34.                                    (3.4)

We used t^j<=exp(2t), v=exp(2t), and cosh(2t)>=v/2. This bound includes the
entire future, not a second finite cutoff. Both negative and positive real t
halves are represented by the cosine integral.

A separate complete bound controls the third derivative on |Im z|<=3:

    |I_a'''(z)| <=4pi exp(-pi+9/(4pi))
                  int_0^infinity t^3 exp(-pi t^2)dt
                =(2/pi)exp(-pi+9/(4pi)) <1.               (3.5)

Here cosh(2t)>=1+2t^2 and 3t<=pi t^2+9/(4pi).

At each exact center c, the checker obtains intervals for I(c), I'(c), I''(c)
including (3.3)--(3.4), then proves with exact rationals

    |I(c)|_upper + r^2 |I''(c)|_upper/2 + r^3/6
                         < r |I'(c)|_lower.              (3.6)

The certified upper/lower ratio is below 0.000109 for N4 and below 0.000445 for
the flow source. A component absolute value supplies the derivative lower bound;
no approximate norm is rounded inward. Taylor's theorem and Rouche compare
I(c+w) with the linear polynomial I'(c)w. This proves the two root counts.

All elementary arithmetic uses 512-bit outward integer intervals. Pi uses
Machin arctangent series; exponential and trigonometric functions use rational
Taylor remainders; square roots use integer-square-root brackets. No zeta,
gamma, Bessel, floating quadrature, or supplied actual-zero primitive enters
these accepting calculations. The written analytic bounds and implementation
remain separate obligations for an independent reviewer.

## 4. GFC2: exact infinite differential deconvolution with a paid remainder

Let the list alpha contain each n^-2, n>N, twice. Denote its elementary
symmetric functions by e_k, with e_0=1. Thus

    sum alpha_i=tau=tau_N,  sum alpha_i^2=v=v_N,
    0<=e_k<=tau^k/k!.

For any real x>0 and circle radius 0<r<x with tau<r, let
M(x,r)=sup_(|w-x|=r)|f(w)|. Then

    f_N(x) = sum_(k>=0) e_k f^(k)(x),                     (4.1)
    |f_N(x)-f(x+tau)|
       <= v M(x,r)/[r^2(1-tau/r)^3].                     (4.2)

These are convergent identities and inequalities, not formal application of an
infinite-order differential operator at a singular point.

**Proof of (4.1).** For finite M>N, the rational Laplace identity and zero initial
jets of f_M give

    product_(N<n<=M)(1+partial_x/n^2)^2 f_M = f_N

on x>0. The boundary jets required here vanish because f_M(x)=O(x^(2M-1));
the maximum differentiation order is 2(M-N). From the parent's explicit partial
fractions, B_(n,M)<=4 and |c_(n,M)|<=1/2+2n^2. Hence f_M and all fixed derivatives
converge locally analytically to f on Re x>0, and sup_M M_M(x,r)<infinity.
Cauchy's estimate bounds the kth summand by M_M(x,r)(tau/r)^k, uniformly in M.
Dominated summation proves (4.1).

**Proof of (4.2).** The coefficient difference satisfies

    0<=tau^k/k! - e_k <= (v/2) tau^(k-2)/(k-2)!  (k>=2). (4.3)

Indeed tau^k sums all ordered k-tuples of indices, k!e_k sums distinct tuples,
and a union bound over the k(k-1)/2 equal-index pairs bounds the missing weight.
No statistical independence of zeros or primes is involved. Taylor's theorem for
f(x+tau), Cauchy's derivative bound, and
sum_(k>=2)k(k-1)q^(k-2)=2/(1-q)^3 give (4.2). QED.

This realizes the parent's translation heuristic with an error proportional to
the variance of the entire omitted tail, not its squared mean. The small-x region
where tau>=r is deliberately NOT covered by (4.2); it is handled separately below.

## 5. A source-specific relative Cauchy bound, including near zero

Set

    r(x)=min(1,x^2)/1000.

For every x>0,

    sup_(|w-x|<=r(x)) |f(w)| <=16 f(x).                   (5.1)

This is where the **actual Jacobi reciprocal identity**, rather than finite
 evenness or generic log-concavity, enters the new quantitative proof.

For x>=pi and |w-x|<=1/64, the positive real series in (2.1) gives
f(x)>=(4x-6)exp(-x). The n=1 modulus divided by this term is <4. For n>=2,
the corresponding ratios are at most 4n^4 exp[-2(n^2-1)] and their sum is <2.
For an entirely elementary bound, use e^2>4, n^4<=16^(n-1), and
sum_(j>=1)4^(1-j^2)<=64/63. This proves the stronger bound 6f(x) in that region.

For 0<x<=pi, |w-x|<=r(x) implies |w-x|<=x/1000. Therefore

    |pi^2/w-pi^2/x| <= pi^2/(999) <1/64,
    |x/w|^(5/2)<2.

The reciprocal identity, holomorphic in the right half-plane, reduces to the
previous large-x bound and gives 12f(x)<16f(x). This proves (5.1). In particular,
all fixed derivatives satisfy |f^(k)(x)|<=16 k! f(x)/r(x)^k. The radius shrinks
quadratically at zero; no uniform analyticity across zero is claimed.

## 6. GFC3: a positive mean-completed source converging at the variance scale

Instead of deleting R_N=X-X_N, replace it by its **exact mean**:

    Xhat_N=X_N+tau_N,
    g_N(x)= f_N(x-tau_N) for x>tau_N, and 0 otherwise,
    hhat_N(t)=sqrt(g_N(x(t))g_N(y(t))),
    Fhat_N(z)=int_R hhat_N(t)exp(izt)dt / int_R hhat_N(t)dt. (6.1)

No signed Richardson extrapolation, fitted parameter or unknown zero is used.
The mean is explicit: tau_N=pi^2/3-2 sum_(n<=N)n^-2. Likewise
v_N=pi^4/45-2 sum_(n<=N)n^-4. These are exact real numbers, not unstated numerical
primitive enclosures.

Every g_N is a probability density. Since 0<tau_N<pi, hhat_N is positive exactly
on

    |t|<T_N,  T_N=(1/2)log(pi/tau_N)=(1/2)log N+O(1).     (6.2)

It is even and nonnegative, vanishes at the endpoints, and has positive integral.
Thus Fhat_N is entire of exponential type at most T_N. It is NOT asserted that
Fhat_N is real-rooted, or that compact support is a zero-location theorem.

**Theorem.** For every R>=0 there is an explicit finite K_R such that, for
N>=2,000,000,

    sup_(|Im z|<=R) |Fhat_N(z)-Phi(z)| <= K_R v_N
                                     <= 2K_R/(3N^3).     (6.3)

Every fixed spectral derivative has the analogous bound. The supremum includes
all real frequencies. The constants below are intentionally very coarse; this
is not a practical N or zero-verification complexity guarantee.

### 6.1 Exact tail scales

Integral comparison gives

    2/(N+1)<=tau<=2/N,
    2/[3(N+1)^3]<=v<=2/(3N^3),
    tau^3/96 <= v <= tau^3/4.                             (6.4)

For the upper relation use v<=tau/(N+1)^2 and tau>=2/(N+1). For the lower one,
v>=1/(12N^3) and tau<=2/N suffice. All relations concern the complete infinite
tail. When N>=2,000,000, tau<=10^-6.

### 6.2 Relative control on the growing central region

Call a real t good when both x=x(t) and y=y(t) are >=1000 sqrt(tau).
For such an x put a=x-tau. Then a>=x/2 and

    r(a)>=r(x)/4,   tau/r(a)<=1/250.

Equations (4.2),(5.1), and f(a)<=16f(x) prove

    |g_N(x)/f(x)-1| <=10^10 v max(1,x^-4).                (6.5)

The constant follows, for example, from
16*16*16*10^6*(1-1/250)^-3<10^10. The right side is less than 10^-8 throughout
the good region: use v<=tau^3/4 and x>=1000 sqrt(tau). In particular it is <1/2.

The partial derivatives of sqrt(uv) on [1/2,3/2]^2 have modulus <1. Applying this
to the two relative densities proves

    |hhat_N-h| <=10^10 v h(t)[2+x(t)^-4+y(t)^-4]           (6.6)

on the good region. This is a relative estimate followed by integration, not
square-rooting a crude absolute error and losing half the rate again.

### 6.3 Both omitted reciprocal ends are smaller than the same budget

From (2.3), g_N(x)<=4x exp(tau-x), hence hhat_N<=exp(tau)H. On the bad region
we may therefore use |hhat_N-h|<=3H, without dividing by f or g_N.
There the larger reciprocal argument exceeds

    b_N=pi^2/[1000 sqrt(tau)]>9.

For m=ceil(R/2), substituting x=pi exp(2|t|) yields

    int_bad exp(R|t|) H(t)dt
      <=16*4^(m+1)m! exp(-b_N/4).                         (6.7)

One proof bounds x^(R/2-1) by x^m on x>=b_N>1 and splits exp(-x/2) into two
exp(-x/4) factors before integrating the complete gamma tail. With c=9/4000,

    exp(-b_N/4)<=exp[-c/sqrt(tau)]
                 <=720 tau^3/c^6 <=720*96 v/c^6,          (6.8)

using the sixth term of the positive exponential series. Thus the moving cutoff
and the region g_N=0 are both paid; support truncation does not leave an unknown
tail term.

Let M_R=int_R exp(R|t|)H(t)dt. All these integrals are finite; the parent's
M_R<16 ceil(R/2)! is also usable. Define the explicit constant

    L_R=10^10[2M_R+2pi^-4 M_(R+8)]
         +48*4^(ceil(R/2)+1)ceil(R/2)!*720*96/c^6.         (6.9)

Equations (6.6)--(6.8) prove int exp(R|t|)|hhat_N-h|<=v L_R.

### 6.4 Normalization is not left as an unknown small denominator

On |t|<=1/10, both x,y lie in [12/5,4]. Write X=G_1+S. Since E S<=3/2,
P(S<=2)>=1/4 and f(x)>=exp(-4)/10 there. Thus

    Z=int h>=exp(-4)/50>1/4050.

That interval is good, and (6.5) implies hhat_N>=h/2. Therefore
Zhat_N>=1/8100. Dividing the numerator estimates with both denominator errors
retained gives (6.3), for example with

    K_R=8100 L_R+8100*4050 M_R L_0.                       (6.10)

For derivatives insert |t|^k in the same integrals; |t|^k<=k!exp(|t|) supplies
explicit constants from the R+1 bounds. This completes the theorem. QED.

## 7. GFC4: the original cascade's deterministic bias is now justified

For epsilon>=0 define the normalized reciprocal transform Phi_epsilon from
f(x+epsilon), just as in the parent's translation calculation. Then for fixed
R and N sufficiently large,

    ||F_N-Phi_(tau_N)||_R = O_R(v_N),                     (7.1)
    F_N=Phi+tau_N B Phi+O_R(N^-2),                        (7.2)

where ||.||_R is the supremum on the **entire** strip |Im z|<=R and

    (A P)(z)=[(2iz-1)P(z-2i)-(2iz+1)P(z+2i)]/(8pi),
    B Phi=A Phi-Phi A Phi(0)
         =A Phi+Phi(2i)Phi/(4pi).                         (7.3)

**Proof of (7.1).** Apply (4.2) at x rather than x-tau on the same good region.
Equation (5.1) also gives |f(x+tau)/f(x)-1|<=16q/(1-q), with q=tau/r(x)<=1/1000.
The relative geometric-mean comparison therefore bounds the good-region error
by a constant times v h(2+x^-4+y^-4). On the bad region,

    sqrt(f(x+tau)f(y+tau))
      <=4 sqrt((x+1)(y+1)) exp[-(x+y)/2].                 (7.4)

When x is the larger argument it is bounded by 32 sqrt(x) exp(-x/2).
The proof of (6.7)--(6.8), increasing the integer polynomial degree by one,
bounds this complete tail by another explicit constant times v. The fixed
central interval supplies the same positive denominator lower bounds. This
proves (7.1), not merely a fixed-t weak expansion.

**Proof of (7.2)--(7.3).** Let r_f(x)=f'(x)/f(x). Differentiating the projected
unnormalized density at epsilon=0 gives h[r_f(x)+r_f(y)]/2. From (2.1) and the
evenness of h this equals

    -h'(t)sinh(2t)/(2pi)-5h(t)cosh(2t)/(4pi).

Integration by parts gives A acting on the Fourier transform. Normalization
subtracts Phi A Phi(0). The derivative is a right derivative. To justify a
uniform second-order remainder, use (5.1) for k=1,2: all shifted score derivatives
are bounded by fixed polynomials in x^-1,y^-1, since r(x+epsilon)>=r(x).
Combine them with (7.4). The resulting envelope, with exp(R|t|), is integrable
at both ends. Dominated differentiation and Taylor's theorem give
Phi_epsilon=Phi+epsilon B Phi+O_R(epsilon^2). Now tau=O(N^-1), v=O(N^-3).
No complex epsilon neighborhood across the support endpoint is assumed. QED.

For real z, Phi(z-2i)=xi(5/2+iz)/xi(1/2), and Phi(z+2i) is its conjugate.
Thus the deterministic bias is expressed using a safe Euler half-plane. This
identity does NOT make A a real-zero-preserving operator; GFC1 warns against
assuming such a conclusion.

For a fixed simple real xi zero gamma, local Rouche and the real symmetry give
one real zero of F_N near gamma for all sufficiently large N, with

    gamma_N=gamma-tau_N (A Phi)(gamma)/Phi'(gamma)+O_gamma(N^-2).

The mean-completed family instead has displacement O_gamma(N^-3). These are
conditional local asymptotics at a fixed simple zero, not a uniform result in
height, a proof of simplicity, or an exclusion of hypothetical nonreal zeros.
At a fixed nonreal zero, uniform convergence would also preserve nearby zeros.

## 8. GFC5: exact end-to-end implication and the remaining spectral obligation

The positive mean-completed family has the following complete conditional ending.
Suppose there are N_j->infinity, U_j->infinity, and epsilon_j->0 such that every
zero of Fhat_(N_j) in |Re z|<=U_j, |Im z|<=1 satisfies |Im z|<=epsilon_j.
Then RH follows.

Indeed a hypothetical nonreal xi zero lies in |Im z|<1/2. Take a small disk
strictly off the real axis, with zero-free boundary, around it. The full-strip
convergence (6.3) and Rouche force the same positive zero count in that disk for
all sufficiently large j. The stipulated confinement forbids those zeros. This
argument retains multiplicities and does not assume any actual nonreal zero.

**The stipulated confinement has not been proved.** The certificates falsify
critical-strip invariance of the original continuous path, not this asymptotic
assertion. The rate O(N^-3) is an absolute approximation theorem. It neither
supplies a lower bound on |Phi| nor turns a positive source into a Lee--Yang law.

The revised concrete task is a scale-dependent birth/escape estimate for the
mean-completed family, or a discrete comparison between successive integer
stages that allows temporary off-real pairs. A theorem on a window c log N
would suffice, but is not established. The certified intermediate root means
that a proof by "simple real roots stay real, hence the whole path does" is
invalid: collisions and boundary entry cannot be omitted.

A separate noncertifying scout suggests even the centered N=5 approximant has a
nonreal zero near 31.08351638+0.23477912i. This is NOT one of the two certified
roots: it uses multiprecision quadrature without an outward remainder. It is
retained to prevent quietly replacing the failed conjecture by untested global
real-rootedness of the new approximants. No centered zero census was performed.

## 9. Evidence, priority and review scope

`certificate.py` reconstructs both complete root certificates in integer interval
arithmetic; `check.py` (the accepting entry point) authenticates the declared
packet inventory and compares strictly typed reconstructed receipts. Neither
program establishes the all-N analytic theorems by finite extrapolation.
`test_check.py` tests interval primitives, finite rational Laplace identities,
coefficient collision bounds and actual malformed-receipt refusals. Unperformed
full repository/Lean/CI/parameter-continuation checks are listed in VALIDATION.md.

The second certificate is for a changed finite source, not xi. The proof of the
all-N rate uses the actual infinite source and its reciprocal identity, not that
certificate or a finite theta-zero computation. Classical gamma convolution,
Cauchy estimates, probability union bounds, geometric means and Rouche are
credited as standard methods; no exhaustive external novelty claim is made.

### References

[P] PR #849, exact commit/blob identified above. Full proposed source manuscript
read and rederived where used, including finite density, reciprocity, positive
Bessel seed, entire-source limit and translation tangent. This is not independent
acceptance of the parent or a replay of its Windows publication tests.

[E1] P. Biane, J. Pitman, M. Yor, *Probability laws related to the Jacobi theta
and Riemann zeta functions, and Brownian excursions*, Berkeley report 569 (1999),
Electronic Journal of Probability 5 (2000), paper 12; arXiv:math/9912170.
https://statistics.berkeley.edu/sites/default/files/tech-reports/569.pdf
Proposition 1 and equations (6)--(8), printed pages 4 and 7, were read including
page images. The gamma/xi representation is classical. With their Sigma_2,
X=(pi^2/2)Sigma_2 and their Y=sqrt(X/pi). Their paper also studies finite Mellin
approximants; that is not a zero-confinement theorem for the reciprocal projection.

The attempted FLINT installation failed DNS; no Arb/FLINT result is claimed.
The final accepting computation instead uses the supplied standard-library
outward implementation and the explicit analytic remainder proof above.
