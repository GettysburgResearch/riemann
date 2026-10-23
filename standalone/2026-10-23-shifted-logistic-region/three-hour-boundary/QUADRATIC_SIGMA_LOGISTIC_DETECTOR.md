# A quadratic frequency profile: proposed R=4.806 extension

2026-10-21. This separate extension retains the exact degree-12 polynomial,
theta=5669/5000, four-prime lower bound, curvature bound 51, and published
finite-height, Littlewood and zero-count inputs of the earlier detector.
It changes only the frequency-dependent real parts. The scalar certificate
and the following analytic interfaces are separate proof obligations.
The fixed-width Hecke boundary and RH are not improved by this argument.

## 1. Exact parameters and positive definiteness

Use a0,...,a12 from LOGISTIC_DEGREE12_PRIME_GAIN.md, and put

    c=9/16, d=3/50, eta=A/l, u=eta/l,
    a=1/2-eta+c*u, lambda=2*a*d*u,
    sigma_k=1/2+sqrt(a^2+lambda*k^2), k=0,...,12,
    alpha_k=2*sigma_k-1,
    f_k(v)=eta*w(eta*v)/(1+exp(-alpha_k*v)).             (Q1)

On 0<A<=500/2403 and 28<=l<=83, a>.4925, eta<.0075,
and .99<sigma_0<=sigma_k<1. Indeed, concavity of the square root gives

    0<=sigma_k-sigma_0<=d*u*k^2,                       (Q2)

and c+144d<28. In particular 0<=1-sigma_k<=eta. The old adapter,
negative archimedean correction and uniform exterior-zero tail bounds
therefore apply separately to each k.

The function h(s)=sech(sqrt(s)), s>=0, is completely monotone. One
direct proof uses the product for cosh: each reciprocal factor
(1+s/b_j)^(-1) is completely monotone, their finite products are
Laplace transforms of positive measures, and their limit h is again
completely monotone. See the product at https://dlmf.nist.gov/4.36.E2
and the Bernstein theorem/closure argument pinned in
SHIFTED_SECH_POSITIVITY.md. Thus h(s)=integral exp(-s*x) dmu(x), with
mu a probability measure. For every v>=0,

    q_k=sech((sigma_k-1/2)*v)
       =integral exp(-a^2*v^2*x) exp(-lambda*v^2*x*k^2) dmu(x)       (Q3)

is a positive-definite sequence on the integers. This follows from
the Gaussian positive-definite kernel, also at lambda=0.

For each n with v=log n, the arithmetic coefficient is

    n^(-sigma_k)f_k(v)=(eta/2)w(eta*v)exp(-v/2)q_k.

The exact polynomial is a sum of two absolute squares. Applying the
positive-semidefinite Toeplitz matrix (q_(i-j)) to each square after
multiplying its coefficients by exp(i*j*t*v) proves
sum_(k=0)^12 ak q_k cos(k*t*v)>=0. Therefore every prime-power
summand omitted below is nonnegative. Neither coefficientwise
positivity of f_k nor positivity of the original polynomial alone
would justify this step with differing real parts.

## 2. Retained prime terms

Compare the retained prime powers (2,m<=10),(3,m<=6),(5,m<=5),
(7,m<=4) to the constant-sigma_0 detector. Its proved lower bound is
1.26eta-90eta^3. Since |sech'|<=1/2, w<=6 and (Q2) holds, the
absolute change in these retained terms is bounded above by

    (3/2)*eta*d*u*(sum_(k=1)^12 k^2 ak)
             sum_(p,m retained) (log p)^2*m*p^(-m/2).

The exact rational coefficients give sum k^2 ak<14. The same rational
upper logarithms and reciprocal square roots as the earlier variable
detector bound the larger infinite prime-power sum by 16. Consequently

    D >= 1.26eta-90eta^3-336*d*eta^2/l.                (Q4)

The companion checker verifies these constants. All other prime powers
are discarded using (Q3), so no variation loss is charged to them.

## 3. Individual zero cutoffs

Use the global minimum B=(1-beta0)log t from the earlier wrapper,
set A=B, l=log t, and let T_k=kt+10^10 for k>=1. For k=0 use
T_0=10^10<3*10^12, inside the verified RH range. Put L_k=log(k+.01).
Since 10^10 exp(-28)<.01, it suffices to prove

    sigma_k >= 1-eta+(eta/l)*L_k.                     (Q5)

For L_k<=c this follows from sigma_k>=sigma_0. Otherwise squaring
positive quantities shows that (Q5) is equivalent to

    L_k-c + [eta/(2*a*l)]*(L_k-c)^2 <= d*k^2.          (Q6)

The directed checker proves the stronger finite inequalities obtained
by replacing eta/(2*a*l) by .21/(2*.4925*28^2), for k=1,...,12.
The smallest margin occurs at k=3 and remains positive. Hence

    sigma_k >= 1-B/log(kt+10^10),                     (Q7)

because L_k/l >= log(k+10^10 exp(-l))/(l+log(k+10^10 exp(-l))).
All zeros below each T_k lie in its permitted reflection strip;
the chosen zero and its reflection are retained at frequency one.

The omitted-zero estimate is exactly the individually cut off version
in VARIABLE_SIGMA_LOGISTIC_DETECTOR.md Section 3: |gamma|>T_k implies
|gamma-kt|>10^10, log T_k<l+3, and the real arguments stay in
[-eta,alpha_k+eta]. The direct Lehman bound and the full old 1e-7
aggregate error allowance remain valid. No common cutoff 12t+T0
or old numerical zero-free baseline is used.

## 4. Exact sufficient scalar inequality

Define

    r=sqrt(a^2+2*a*d*eta/l),
    rho=c/l+2*a*d/[l*(r+a)],
    sigma_0=1-eta+c*eta/l, sigma_1=1-eta+eta*rho,
    z0=sigma_0-1, z1=eta*rho, z2=sigma_1-eta.

The rationalized rho formula is continuous at A=0 and avoids dividing
by eta. The selected-zero terms use alpha_1; the pole uses alpha_0.
The exact explicit formula, Carch<=-3.00317, E_(f_0)(sigma_0)<=-.31eta
and (Q4) give the same necessary inequality as before, with signal

    a1*[F_1(z1)+F_1(z2)]-F_0(z0).

The curvature/logistic-complement lower bound for that signal is

    a1*W(rho)-W(-1+c/l)
    +eta*w0*[a1/z2+J(z0,alpha_0)
                         -a1*J(z1,alpha_1)-a1*J(z2,alpha_1)]
    -51eta^3*[(z0+alpha_0)^(-3)
                         +a1*(z1+alpha_1)^(-3)+a1*z2^(-3)].       (Q8)

Subtract from (Q8) the resource
w0*[A*aP/4-3.00317*eta/2]+1e-7, and add
1.57eta-90eta^3-336*d*eta^2/l. The resulting margin must be
nonpositive at a violating minimizing zero.

`probe_quadratic_sigma.py` defines this interval margin; its point
probes are exploratory only. `certify_quadratic_sigma.py` proves
strict positivity on the full closed rectangle

    0<=A<=500/2403, 28<=l<=83.                        (Q9)

Its initial directed run accepts 17 rational boxes, minimum lower
bound greater than .00003560. The same rigorous W Taylor/moment
remainder and positive J-series remainder as the baseline are kept.
The JSON records exact source hashes and every box. The separate
exact Fraction replay is an independent review obligation.

## 5. Global assembly and comparison scope

Take Astar=500/2403=1/4.806. Published Littlewood excludes violations
above exp(exp(21.233*Astar)), and exp(21.233*Astar)<83. Verified RH
excludes the range up to 3*10^12; log(3*10^12)>28. If any violation
exists, the classical strict strip, discreteness and this upper
localization yield a positive global minimum B<=Astar. The detector
at its zero satisfies (Q7) and contradicts (Q9). Conjugation gives
the negative-height statement. Thus the proposed assembled conclusion,
subject to the analytic/imported inputs and independent review, is

    zeta(s)!=0 for Re s>1-1/(4.806 log|Im s|), |Im s|>=3.

This extension uses the published constant 21.233, not the thesis
constant 19.62 mentioned in a later author-post comparison. It does
not assert priority over results with other inputs, prove RH, or
lower the independent fixed-width Hecke boundary. Human mathematical
review remains outstanding.
