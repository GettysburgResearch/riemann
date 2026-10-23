# A weighted, arbitrary-degree Ford detector at a global minimum

2026-10-23. Proposed source-dependent analytic lemma for independent review.
The floating searches beside this note are not acceptance certificates.
No new global zero-free constant is asserted by this note alone.

## 1. Source and changes

Use Kevin Ford, *Zero-free regions for the Riemann zeta function*, corrected
arXiv:1910.08205v5 (18 February 2025),
<https://arxiv.org/pdf/1910.08205v5>. The downloaded PDF has SHA256
`df92c2e7fd3aa54634258c4e803c63c4eaea210c5b3faab1abcb7128700194f4`.
The relevant inputs are Lemmas 4.4--4.6, equations (4.4)--(4.5), the
Euler-product argument (5.3)--(5.4), and (7.2)--(7.8). We rederive the
inequality preceding Lemma 9.2, instead of changing constants in its
conclusion or in the final Theorem 3.

Three changes are made explicitly: the nonnegative trigonometric
polynomial can have any fixed degree; each frequency keeps its own
critical-line and zero-count bound; and the kernel parameter is free,
with its remainder constant evaluated from (7.5). The relation (6.4)
between theta and b1 is an optimization choice, not needed for these
three earlier arguments. We do not use the simplified identity in (7.12)
that does require that relation.

## 2. Kernel and its two compatible remainder bounds

Fix 0<theta<pi/2, put k=tan(theta), U=2theta/k, and define

    g(u)=sec(theta)^2[cos(ku)-cos(theta)]  (|u|<=theta/k),
    g(u)=0 otherwise,  w=g*g,
    W(z)=integral_0^U exp(-zu)w(u)du,
    w0=sec(theta)^2[theta*k+3theta/k-3].

Thus w>=0 and Re W(iy)>=0. The convolution is continuously
differentiable with the boundary regularity required by Ford Lemma 4.5.
The algebraic expressions (7.2)--(7.3) hold for this whole theta family:

    W(z)=w0/z+W0(z),
    W0(z)=c0{c2[(z+1)^2 exp(-Uz)+z^2-1]-c1*z-c3*z^3}
                       /[z^2(z^2+k^2)^2],
    c0=1/(sin(theta)cos(theta)^3),
    c1=(theta-sin(theta)cos(theta))*k^4,
    c2=k^3 sin(theta)^2,
    c3=(theta-sin(theta)cos(theta))*k^2.

Choose R0>max(3,k), and set

    H=c0{c2*(R0+1)^2/R0^3*(exp(U)+1)+c1/R0^2+c3}
                                      /(1-k^2/R0^2)^2,
    c4=1+1/R0+H*(R0+1)^2/(R0^3*w0),
    c5=(4/pi^2)*(c4-1/R0).                         (G1)

For Re z>=-1 and |z|>=R0 the explicit expression gives
|W0(z)|<=H/|z|^3. Let 0<lambda<=1/[2(R0+1)] and put

    f(u)=lambda exp(lambda*u)w(lambda*u),
    f0=lambda*w0, F(z)=W(z/lambda-1),
    V_c(z)=c*w0*(cot(z)-1/z)+W(z/c-1), c=pi*lambda.

Ford's (7.5)--(7.8), with eta=1/2, now give the compatible bounds

    |F(z)-f0/z|<=c4*lambda*f0/|z|^2
                                  (Re z>=0, |z|>=1/2),
    Re V_c(z)>=-c5*c^2*w0
                                  (Re z>=c, |z|<=pi/2). (G2)

For completeness, the second bound follows on Re z=c from Fourier
positivity of w and Lemma 4.4. On |z|=pi/2 it follows by inserting W0
and bounding its remainder by H*c^3/(pi/2-c)^3. The maximum principle
then fills the half-disc. The condition c<=pi/[2(R0+1)] gives (G1).
In particular the local zero-count coefficient is exactly

    pi^2*c5-4*c4=-4/R0<0.                           (G3)

This uses (7.8) directly. The printed inequality eta<=80lambda in the
discussion after (9.3) has the opposite direction from the sufficient
condition (7.5); it is not used. Neither is the printed expression (9.6).

## 3. General polynomial and weighted source bounds

Let

    P(x)=1+sum_(j=1)^K b_j cos(jx)>=0,
    b_j>=0, b1>0, K>=1.                             (G4)

Suppose zeta(beta+it)=0, t>=10000, d=1-beta satisfies

    0<lambda<=d<=1/160,
    zeta(s)!=0 for 1-lambda<Re s<=1,
                      t-1<=Im s<=Kt+1.              (G5)

Write h_j=log(jt+1). Suppose the entire smoothing integral has an upper
bound I(jt)<=2J_j, where

    I(v)=integral_R log|zeta(1/2+i(v+u/pi))|sech(u)^2 du.

Each j has, separately, the zero-count bound

    sum_(|1+ijt-rho|>=1/2) |1+ijt-rho|^-2
       <=3.2357*h_j+5.316*log(h_j)+16.134-4N(jt,1/2). (G6)

Indeed (4.4), applied at q=jt, gives
.8664 log q+1.772 loglog q+5.77 for |Im rho-q|>=1.
The remaining zeros outside the half-disc contribute at most four
times N(q+1)-N(q-1)-N(q,1/2). Equation (4.5) bounds this difference by
.59231 log q+.886 loglog q+2.591-N(q,1/2). Their sum has log coefficient
3.23564<3.2357. Replacing log q by h_j only enlarges it. This proves
(G6) for each positive integer j, with no upper restriction j<=4.

Likewise the gamma/remainder term in Lemma 4.6 is bounded, frequency
by frequency, by D[1.8+h_j/3], with D=c4*lambda*f0. The zero-frequency
term is bounded by F(0)+1.8D, exactly as in (6.3).

The right-line Euler-product smoothing in (9.1) needs only P>=0.
It therefore gives the same constant .851 with b0=1 for every K.
The left Dirichlet sum is nonnegative since f>=0 and P>=0.
Consequently the proof of (6.3) and (9.7), keeping the individual j
bounds and using (G2), yields

    0 <= W(-1)-b1*V_(pi*lambda)(pi*d)
       +lambda*w0[sum b_j*J_j+.851]
       +c4*lambda^2*w0
          [sum b_j(3.5691*h_j+5.316*log(h_j)+17.934)+1.8]. (G7)

The omitted local-count coefficient is (G3), multiplied by
lambda*f0*sum b_j N(jt,1/2), and hence is nonpositive. All other local
zeros satisfy the half-disc hypothesis because of (G5). The one
selected zero beta+it is retained in the j=1 term. If it has larger
multiplicity, retaining just one copy only weakens the inequality.

The source estimate cot(x)-1/x>=-.3334x for 0<x<=pi/160 implies

    V_(pi*lambda)(pi*d)
       >=W(d/lambda-1)-.3334*pi^2*lambda*d*w0.

We have therefore proved the following necessary scalar inequality:

    b1*W(d/lambda-1)/w0-W(-1)/w0
      -.3334*pi^2*b1*lambda*d
      -lambda[sum b_j*J_j+.851]
      -c4*lambda^2
        [sum b_j(3.5691*h_j+5.316*log(h_j)+17.934)+1.8]
       <=0.                                          (G8)

Every constant in (G8) is either from the specified source estimates or
is explicitly computed from the new kernel. No term from the published
fixed-polynomial final bound is reused after changing the polynomial.

## 4. Application at the same global minimum

Use the established finite-RH verification and a published Littlewood
region to obtain a zero above H=3*10^12 minimizing
B=(1-beta)log t, if a target classical strip is violated. This is the
same minimum as in the logistic proof; the present inequality is not
applied to an arbitrary zero without its minimum property.

Put l=log t, h=log(Kt+1), d=B/l, lambda=B/h. For every zero in the height
window of (G5), minimality gives a gap >=B/log(Im rho)>=B/h; any zero
below H has real part 1/2. Thus (G5) holds. At l>=60 and B<=.22 we have
d<1/160 and lambda<1/160, so R0=79 is allowed.

The global envelope from `../three-hour-root/REVERS_SHIFTED_ENVELOPE.md`
gives, without any high-height localization gap,

    J_j=j(jt)+1/D,
    j(v)=(1/6)log(v+D)+log(a log(v+D)+b),
    a=.469028, b=3.99399, D=2*10^18.                  (G9)

For log v>=60, D/v<2*10^-8 and the derivative of
q(x)=x/6+log(ax+b) is below1; hence the simpler common-domain bound

    J_j <= q(h_j)+10^-7                              (G10)

is valid. This larger buffer is deliberate: the earlier 10^-10
version was only proved when log v>=70. The fully shifted expression
(G9) can instead be used at any height.

For a uniform endpoint reduction set epsilon=10^-20, c=log K,

    h0=l+c, s_j=l+log j+epsilon, eplus=(c+epsilon)/l.

For l>=60, exp(-l)<epsilon, so h0<=log(Kt+1)<=h0+epsilon
and h_j<=s_j. Since W is decreasing on the real axis, a lower bound for
the left side of (G8) is

    M(A,l)=b1*W(eplus)/w0-W(-1)/w0
      -.3334*pi^2*b1*A^2/[l*h0]
      -(A/h0){sum b_j[q(s_j)+10^-7]+.851}
      -c4*(A/h0)^2
         {sum b_j[3.5691*s_j+5.316*log(s_j)+17.934]+1.8}. (G11)

Here 0<B<=A, and every negative term increases in absolute value
with A. The signal is independent of A. Thus M(A,l)>0 excludes the
minimizing zero for every B<=A.

For 1<=K<=32, l>=60, the function M(A,l) is increasing in l for
fixed A>0. Indeed W(eplus) increases since eplus decreases. All
remaining terms are positive multiples of decreasing functions.
For the only less immediate one, the derivative numerator of
[q(s_j)+10^-7]/h0 is

    (c-log j-epsilon)/6
      +a*h0/(a*s_j+b)-log(a*s_j+b)-10^-7.

Since c<4, h0/s_j<=16/15, and log(60a+b)>3, this is at most
4/6+16/15-3<0. Also s_j/h0^2 decreases because
h0-2s_j<=-l+4<0. The derivative numerator of log(s_j)/h0^2
is h0/s_j-2log(s_j)<16/15-8<0. The reciprocal terms plainly
decrease. This proves the infinite-tail assertion directly, without
a numerical grid at large heights.

The separate `verify_general_ford.py` evaluates (G11) with exact
rational intervals, including trigonometric and exponential Taylor
remainders and an exact sum-of-two-squares polynomial. It also checks
the elementary constants used in this monotonicity proof. Its finite
checks do not certify the imported analytic inequalities.

## 5. Scope and work remaining

The lemma above is an analytic candidate requiring independent review,
especially the preservation of the source constants through (G6)--(G7).
The existing exact degree12 sum-of-two-squares polynomial can be reused
without optimizing a new polynomial. The parameter theta=23/20 is
independent of the logistic kernel parameter; the two detectors need
not use the same kernel. Numerical searches suggest a substantially
shorter tail cap. A full new boundary still requires the complementary
logistic rectangle, rigorous endpoint arithmetic, and an assembly review.
