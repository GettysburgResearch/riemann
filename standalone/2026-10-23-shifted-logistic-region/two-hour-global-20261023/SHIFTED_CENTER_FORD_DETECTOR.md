# A shifted-center Ford detector with a cubic zero-tail error

2026-10-23. Proposed analytic lemma, under active independent review.
This note does not assert a new global zero-free region. The scalar
replay and complementary low-height argument are separate obligations.
The earlier R=4.75 component files remain unchanged.

## 1. Inputs and the physical shift

Use the corrected Ford arXiv:1910.08205v5, Lemma 2.2, its elementary
cotangent bound in Section 7, and the explicit kernel in (7.2)--(7.3).
The pinned PDF SHA256 is
`df92c2e7fd3aa54634258c4e803c63c4eaea210c5b3faab1abcb7128700194f4`.
Use also the exact compact-test explicit formula (L3)--(L4) in
`../three-hour-type/LOGISTIC_ADMISSIBILITY.md`, with its displayed
derivation from the BTY explicit formula. Here the test has f'(0)=0,
so no derivative-removal extension is needed.

Let theta=23/20 and let w, W, w0 and H be as in
`GENERAL_WEIGHTED_FORD_DETECTOR.md`, taking R0=79. The elementary
kernel inequalities required below are

    w>=0, w(u)<=w0, Re W(iy)>=0,
    w0>6, ||w''||_infinity<70,
    |W(z)-w0/z|<=H/|z|^3, H<70
                              (Re z>=-1, |z|>=79).       (S1)

The value w0 is about6.67404; H is about69.89858. The final acceptance
checker must certify the rational upper bounds in (S1); those decimal
approximations are not an acceptance argument.

Put

    sigma=1-lambda, eta=1/2-lambda,
    f(u)=lambda*w(lambda*u), f0=lambda*w0,
    F(z)=W(z/lambda), F0(z)=F(z)-f0/z.                    (S2)

Assume 0<lambda<=1/160. Then eta>=79lambda and sigma>.99.
The Dirichlet weight at the new center is exactly

    n^(-sigma)f(log n)=lambda*n^-1*exp(lambda log n)
                                      *w(lambda log n).

It is the same weight as in the original center-1 detector. Likewise
the pole is F(sigma-1)=W(-1), and a selected zero beta+it contributes
F(sigma-beta)=W((1-beta)/lambda-1). The shift changes neither of those
two principal terms.

## 2. Exact explicit formula and real-center gain

Write K(s)=sum_n Lambda(n)n^-s f(log n), a finite sum. For Re s>1/2,

    Re K(s)=f0 Re A(s)+Re F(s-1)-Re sum_rho F(s-rho)
                                                   +Re E_f(s),
    A(s)=psi(1+s/2)/2-log(pi)/2,
    E_f(s)=integral_0^infinity exp(-(s+2)u)
                        [f0-f(u)]/(1-exp(-2u)) du.       (S3)

The zero sum is symmetric; the real parts of the paired terms
converge locally absolutely. The Hadamard identity therefore gives
the equivalent form

    Re K(s)=-f0 Re[zeta'(s)/zeta(s)]+Re F0(s-1)
                   -Re sum_rho F0(s-rho)+Re E_f(s).      (S4)

At a zero, the apparent singularities on the right cancel. We can
first work off the zeros and take a limit in the combined expression.
This avoids extrapolating the constants in Ford Lemma 4.5 below1.

Since 0<=w0-w(v)<=35v^2 globally,

    |E_f(s)|<=70lambda^3 sum_(j>=0)(Re s+2+2j)^-3
             <4lambda^3                         (Re s>.99). (S5)

For the last strict bound put a=299/100, retain j=0,1 and bound the
remaining decreasing sum by its integral from1:

    70[a^-3+(a+2)^-3+1/(4(a+2)^2)]<4.

At the real center sigma, reflection of zeros about1/2 gives

    Re[1/(sigma-beta-i gamma)
          +1/(sigma-1+beta-i gamma)]>0.

Indeed its numerator is (2sigma-1)
[gamma^2+(sigma-beta)(sigma-1+beta)]>0, since |gamma|>14.
Thus the f0/z part of the zero sum in (S3) has a favorable sign.
Also A(sigma)<=A(1)<-.55: A increases on the positive real axis,
and A(1)=1-gamma_E/2-log2-log(pi)/2. Finally, Ford Lemma3.3 and
|gamma|>14 give

    sum_rho |gamma|^-3
       <=(197/196)*.0463/14 <.00333.

Consequently (S1), (S3), and (S5) give

    K(sigma)<=W(-1)-.55lambda*w0+lambda^3*w0.             (S6)

For example the unused absolute numerator error is less than
4+70*.00333<4.234, whereas w0>6. No RH assumption above the finite
verification height is used in this real-center estimate.

## 3. Local zeros and an exactly compatible outside bound

At s=sigma+iq put z=s-rho and define the regular function

    V(z)=F(z)+f0[(pi/(2eta))cot(pi*z/(2eta))-1/z].        (S7)

For Re z>=0 and |z|<=eta,

    Re V(z)>=-Hlambda^3/eta^3.                           (S8)

On Re z=0 this follows from Re W(iy)>=0. On |z|=eta,
the real part of the cotangent term is nonnegative and (S1) bounds
F0. The singularity at0 is removable, and the real-part minimum
principle fills the half-disc.

For all nontrivial zeros, x=Re z>=-lambda>=-eta/2. Put r=|z| and

    P_rho(q)=Re[1/(sigma+eta+iq-rho)]
            =(x+eta)/[(x+eta)^2+(q-gamma)^2]>0.

If r>=eta, the identity

    (2x+eta)(r^2-eta^2)>=0

is precisely the assertion r^-2<=(2/eta)P_rho(q). If instead
Re z>=0 and r<=eta, then P_rho(q)>=1/(2eta). Assign the boundary
to the closed local disc. If every zero in that disc has Re z>=0,

    sum_(r>eta) r^-3
       <=(2/eta^2)sum_rho P_rho(q)-N(q,eta)/eta^3.       (S9)

The outside error from F0 is Hlambda^3 times this quantity. Its
negative local count cancels exactly the loss in (S8). This is the
reason for using the shifted center; the surviving error is cubic
in lambda, with no uncancelled local-count term.

For the selected zero put d=1-beta and x=d-lambda>=0. If
pi*x/(2eta)<=pi/160, Ford's elementary cotangent bound gives

    V(x)>=W(d/lambda-1)
                  -.3334*pi^2*f0*x/(4eta^2).            (S10)

## 4. The far cotangent terms cannot simply be discarded

Let beta+it be a zero attaining the global minimum B=(1-beta)log t
above the finite verification height. Fix a polynomial degree K<=32,
put l=log t>=40, and set

    h=log(Kt+100), lambda=B/h, 0<B<=.22.                 (S11)

By minimum ordering, every zero with ordinate in [t-100,Kt+100]
has real part<=sigma. Zeros below the verification height have real
part1/2 and satisfy the same conclusion. In particular every local
disc in Section3 has the required horizontal sign. Moreover d-lambda
is small enough for (S10): h-l<4 and l>=40 imply
x<lambda/10<=1/1600, while2eta> .98.

Ford Lemma2.2 also contains zeros in its full vertical strip. A zero
with beta>sigma can have a cotangent of the wrong sign. Such a zero
must satisfy |gamma-jt|>100 for every1<=j<=K. For |y|>=100,

    |Re cot(pi*(x+iy)/(2eta))|<=4exp(-6|y|).             (S12)

This follows directly from sin(2a)/(cosh(2b)-cos(2a)), since eta<1/2
and pi>3. Rosser's bound (Ford (4.3)) implies the coarse uniform count

    #{rho:m<=|gamma-q|<m+1}<=16log(q+m+3),
                                     q>=exp40, m>=100. (S13)

To check (S13), on any positive interval [T,T+1] with T>=14 use the
main-term derivative bound plus the two endpoint errors
.137log T+.443loglog T+1.588. This is at most4log(T+3).
Intervals below14 contain no zeros; an interval meeting14 is covered
by the same endpoint estimate at15. Reflect the two signed-distance
intervals into the positive half-line, using at most four intervals.

After division by w0, the entire adverse cotangent tail at q=jt is
at most

    400lambda(log q+103)exp(-600)<10^-100.              (S14)

Here lambda(log q+103)<=.22(1+103/40)<1. The sum over frequencies
still is negligible for sum b_j<4. The pole at1 has a favorable
cotangent sign at sigma<1, so dropping its cotangent only enlarges
the upper bound. This step explicitly repairs the sign issue that
would arise from reusing the center-1 disposal of all far zeros.

Exceptional widths in Lemma2.2 are handled by nearby widths and a
limit, as in Ford Lemma4.1. The left-line integrals converge through
zeros; the combined local expression is continuous. Enlarging the
window slightly before the limit gives the same closed-disc result.

## 5. Weighted Hadamard control

Let P(v)=1+sum_(j=1)^K b_j cos(jv)>=0, with b_j>=0 and bP=sum b_j<4.
At sigma'=sigma+eta=3/2-2lambda>1, Euler positivity gives

    sum_j b_j Re[zeta'(sigma'+ijt)/zeta(sigma'+ijt)]
       <=-zeta'(sigma')/zeta(sigma').                    (S15)

Indeed the left side is -sum Lambda(n)n^-sigma'[P(tlog n)-1].
The same elementary digamma estimate as in
`POISSON_KERNEL_ZERO_TAIL.md` gives, at q>=exp40,

    sum_j b_j sum_rho P_rho(jt)
       <=(1/2)sum_j b_j log(jt)+3.                      (S16)

For this deliberately coarse bound it is enough to certify
-zeta'(37/25)/zeta(37/25)<2. The gamma term contributes
-(log(2pi)/2)bP plus a negligible positive remainder; dropping the
negative constant and allowing1 for the remainder proves (S16).
The elementary certificate
`../two-hour-root-20261023/verify_shifted_euler.py`, SHA256
`aa9f8bc15a384712d14eb6037837769c3b82ecc8d8dc2ef023985c2a688d01bc`,
proves this bound and C(lambda)<9/10 on the full interval
0<=lambda<=1/160. It enumerates all1280 prime powers through10000
and bounds the remaining positive sum with Lambda(n)<=log n and
an elementary integral. See `../two-hour-root-20261023/SHIFTED_EULER_BOUNDS.md`.

## 6. Right-line arithmetic and the necessary inequality

The critical-line integral now has width2eta/pi. Suppose it is at
most2J_j at center jt. The global shifted Revers envelope remains
valid at this narrower width, since its proof only enlarges the
Lipschitz correction to1/D. Thus one may take

    J_j=j(jt)+1/D,
    j(v)=log(v+D)/6+log(.469028log(v+D)+3.99399),
    D=2*10^18.                                         (S17)

The right-line Euler integral is exact. Its constant term is f0*C,
where

    C=C(lambda)=sum_n Lambda(n)n^(-sigma)/(n^(2eta)-1)
               =sum_(m>=1) [-zeta'/zeta](sigma+2m eta). (S18)

The remaining term has P(tlog n) and a favorable sign. Combining it
with the unchanged left Dirichlet sum gives at least the old four-
prime gain .255lambda-18lambda^3 after division by w0. Indeed the
new right weight n^-sigma/(n^(2eta)-1) is at least1/(n^2-n).
The exact old prime certificate therefore remains a lower bound.

Combining (S4)--(S18), retaining one copy of the selected zero, and
using bP<4 yields the following necessary inequality (a harmless
10^-20 budget covers the far cotangents and the high pole F0 term):

    b1*W(d/lambda-1)/w0-W(-1)/w0
      -.3334*pi^2*b1*lambda*(d-lambda)/(4eta^2)
      -lambda/(2eta)*sum_j b_j J_j
      -lambda*[C(lambda)-.805]
      -(2H/w0)*lambda^3/eta^2
                         *[(1/2)sum_j b_j log(jt)+3]
      -[19+(4/w0)*bP]*lambda^3-10^-20
      <=0.                                             (S19)

Here .805=.55+.255; the19 collects the real-center error1 and prime
error18. The 4bP/w0 is the uniform high-frequency E_f error. Every
constant and favorable term has been assigned once.

## 7. A uniform endpoint reduction

Use the elementary Euler estimate C(lambda)<9/10 certified above
for0<=lambda<=1/160. Set epsilon=10^-14, c=log K, h0=l+c,
lambda_plus=A/h0, eta_minus=1/2-lambda_plus, with0<A<=.22 and l>=40.
The minimum window satisfies

    h0<=log(Kt+100)<=h0+epsilon,

because100exp(-40)<epsilon. Define J_j by (S17), with the actual
center jt=exp(l+log j). An explicit lower bound for the left side
of (S19), valid simultaneously for every0<B<=A, is

    M(A,l)=b1*W((c+epsilon)/l)/w0-W(-1)/w0
      -.3334*pi^2*b1*A^2*(c+epsilon)
                                 /[l*(h0-2A)^2]
      -A/(h0-2A)*sum_j b_j J_j
      -.095*A/h0
      -(8H/w0)*A^3/[h0*(h0-2A)^2]
                            *[(1/2)sum_j b_j(l+log j)+3]
      -[19+(4/w0)*bP]*(A/h0)^3-10^-20.                 (S20)

First combine the favorable linear terms with C at the actual
lambda: C-.805<=.095. This positive adverse coefficient can then
be bounded using lambda_plus. In particular the favorable gain
has not been evaluated separately at an upper endpoint. The
selected x=d-lambda is at most A(c+epsilon)/(l*h0), giving the
displayed cotangent term. Every other adverse term increases with
A, whereas the exact signal d/lambda-1=h/l-1 is independent of B.

For fixed A, M(A,l) increases on l>=40. The signal increases because
W is decreasing and (c+epsilon)/l decreases. The rational adverse
terms decrease immediately; the linear numerator in the zero-tail
term is divided by h0*(h0-2A)^2. Its logarithmic derivative is at
most1/l, whereas that denominator has logarithmic derivative at
least3/(l+4)>1/l.

For the critical-line term put s_j=log(exp(l+log j)+D) and
q(s)=s/6+log(.469028s+3.99399). Then0<s_j'<=1, s_j>=l, and
q'(s)<=1/6+1/s. The derivative numerator of
[q(s_j)+1/D]/(h0-2A) is at most

    4/6+(l+4)/l-log(.469028l+3.99399)<0,

since l>=40 and log(.469028*40+3.99399)>3. This proves the required
monotonicity without replacing the shifted envelope by an
inapplicable high-height asymptotic. Thus M(A,L)>0 excludes the
global minimizing zero at every log-height l>=L, not only at a
sampled endpoint. These observations also justify replacing B by A.

`verify_shifted_ford.py` evaluates (S20) by exact rational intervals
using the frozen kernel/moment engine in `verify_general_ford.py`.
Its acceptance decisions use no binary floating point. The Euler
constant hypotheses and the analytic proof are separate inputs.

## 8. Scope and acceptance obligations

The new analytic interfaces requiring review are the below-1
center in the exact formula, the cotangent tail (rather than an
unlicensed sign discard), the exact local-count cancellation, and
the favorable real-center term. A final scalar replay must certify
(S1), the Euler bounds in (S16)/(S18), and a uniform lower bound for
(S19). It must retain the exact shifted envelope when l<60.
Floating probes are only search diagnostics. The complementary
logistic rectangle, minimum-attainment proof, source provenance,
and full assembly review remain separate requirements. No claim
about the Riemann Hypothesis follows from this component.
