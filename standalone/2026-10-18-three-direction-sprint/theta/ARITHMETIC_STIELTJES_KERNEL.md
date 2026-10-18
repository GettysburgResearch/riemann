# The actual arithmetic Stieltjes kernel and complete polynomial-tail bounds

**Exact analytic representation and paid far tails. The central positivity
estimate is open. No RH or new zero-free band is claimed.** The squared
variable, spectral-zeta and explicit-formula viewpoint is classical;
compare Voros, [Zeta functions for the Riemann zeros]
(https://www.numdam.org/item/10.5802/aif.1955.pdf), especially Sections3--5.
The purpose here is to keep the literal prime-power term and every tail
in an all-order positivity attack on the weighted canonical gate in #1003.

## 1. One literal kernel, without an assumed zero location

Let

    F(x)=xi(1/2+sqrt(x))/xi(1/2),  G(x)=F'(x)/F(x).           (1)

Evenness of xi about1/2 makes F entire; the square root in (1) introduces
no branch in F. For x>1/4 the elementary Gamma/Euler calculation gives

    G(x)=integral_0^infty exp(-xy) k(y)dy,                   (2)

where

    I(y)=integral_0^infty
       [exp(-u)-exp(-u/4-u^2/(16y))]/[1-exp(-u)] du,

    k(y)=exp(y/4)
       +[I(y)-gamma-log(pi)
          -2sum_(n>=2) Lambda(n)n^(-1/2)
                    exp(-(log n)^2/(4y))]/[4sqrt(pi y)].    (3)

Here Lambda is the ordinary von Mangoldt function, including ALL prime
powers. Formula (3) is absolutely defined for every y>0. It does not
replace the full arithmetic component by a prime-only or squarefree sum.

**Derivation.** Write t=sqrt(x)>1/2. Logarithmic differentiation of the
definition of xi gives

    G(x)=1/(x-1/4)
       +[psi(1/4+t/2)-log(pi)]/(4t)
       -(1/(2t))sum_(n>=2) Lambda(n)n^(-1/2)exp(-t log n).  (4)

The first term includes BOTH polynomial factors s and s-1 of xi; no
uncanceled pole of zeta has been discarded. The Euler series in (4) is
absolute because 1/2+t>1.

For a>=0 and x>0 the elementary subordination identity is

    integral_0^infty exp(-xy-a^2/(4y))/sqrt(pi y)dy
                       =exp(-a sqrt(x))/sqrt(x).            (5)

One proof differentiates its left side twice in a. The Gaussian kernel
satisfies partial_a^2=partial_y, so integration by parts gives f''=xf
for a>0. Decay as a tends to infinity and the Gamma integral at a=0 fix
the unique solution (5). The endpoint operations are dominated first
for a>0 and then passed continuously to a=0.

Use also the exact digamma integral

    psi(z)+gamma=integral_0^infty
                   [exp(-u)-exp(-zu)]/[1-exp(-u)]du,

for Re z>0; this is [DLMF5.9.16](https://dlmf.nist.gov/5.9.E16).
Subordination (5) with a=u/2 gives the Gamma term in (3), with precisely
the exponent u^2/(16y). The rational term transforms to exp(y/4), and
each prime power transforms with a=log n. This proves (2)--(3).

The exchanges are absolute. For the only delicate joint endpoint u=0,
split the digamma numerator into

    exp(-u)-exp(-u/4)
       +exp(-u/4)[1-exp(-u^2/(16y))].

The first difference is O(u). For the second use
`1-exp(-z)<=min(1,z)` and split the y integral at y=u^2: its integral
against `y^(-1/2)exp(-xy)` is O(u). Division by `1-exp(-u)` therefore
remains integrable in u. The prime-power exchange follows from its
positive absolute majorant and the absolute Dirichlet series in (4).

The kernel k extends holomorphically to Re y>0. On compact subsets the
prime series has a Gaussian majorant in log n, and the same is true of
the u integral after the preceding endpoint subtraction. At y down to0,
`k(y)=O(y^(-1/2)(1+|log y|))`; split the u integral at sqrt(y),1 and
use the same numerator subtraction. At infinity a crude absolute bound
is `k(y)=O((1+y)exp(y/4))`. For the prime series this follows by bounding
Lambda(n)<=log n, completing the square in
`a/2-a^2/(4y)`, and paying finitely many initial terms separately.
These bounds also establish Laplace uniqueness in the class used below.

## 2. The exact positivity that would complete the real-node route

The following is a classical Stieltjes reformulation, not a new theorem
about the unknown zeros:

    k is completely monotone on (0,infinity)  <=>  RH.       (6)

For the forward implication, the Bernstein--Widder theorem represents
k as `integral exp(-lambda y) dsigma(lambda)` with sigma positive on
[0,infinity). The explicit imported theorem, including possibly infinite
total mass, is Schilling--Song--Vondracek, *Bernstein Functions* (2010),
Theorem1.4, read in the [publisher's primary preview]
(https://api.pageplace.de/preview/DT0400.9783110215311_A15706968/preview-9783110215311_A15706968.pdf).
Tonelli in (2) then gives

    G(x)=integral_[0,infinity) dsigma(lambda)/(x+lambda).     (7)

Finiteness at one x>1/4 gives the usual integrability of this Stieltjes
transform. Its right side is holomorphic off the nonpositive real axis.
Meromorphic continuation of F'/F from x>1/4 shows that F has no zeros
off that axis. Thus xi has only critical-line zeros.

Conversely, under RH the paired Hadamard product of xi gives

    G(x)=sum_(gamma_j>0)1/(x+gamma_j^2).

The zero count/order-one estimates make this absolute for x>0 and make
`sum_j exp(-gamma_j^2 y)` locally uniform for y>0. Laplace uniqueness in
(2) therefore identifies k with that positive heat trace. It is completely
monotone. These canonical-product facts and the spectral-zeta setting are
the classical ones discussed in the cited Voros paper; the arithmetic
derivation (3) itself does not assume them or RH.

The all-order unproved inequality is now literal:

    (-1)^m k^(m)(y)>=0, EVERY integer m>=0 and EVERY y>0.    (8)

Under (8), every real polynomial P also satisfies

    P(-D_y)^2 k(y)>=0.                                     (9)

The native positive theta density does not itself give (8) or (9).
In particular even k(y)>=0 would be insufficient. If all the weighted
absolute moments below are integrable, differentiation through the
Laplace integral at x=0 gives the raw physical logarithmic coefficients

    A_r=(r-1)!^(-1) integral_0^infty y^(r-1)k(y)dy.

This formula requires those weighted-moment hypotheses; mere integrability
of k at0 does not justify arbitrarily many derivatives. Under complete
monotonicity they follow from positivity and the actual analyticity of G
at x=0, by monotone convergence applied to its derivatives as x decreases
to0.

Thus their Hankel form contains the kernel
`y^(i+j+1)/(i+j+1)!`, not a polynomial square. Its2x2 determinant is
`-y^4/12`. Positivity of a heat density alone cannot silently replace the
Stieltjes positive spectral measure in the weighted canonical consumer.

The intended log representation is the stronger Thorin form
`log F(x)=integral log(1+b x)dmu(b)` with mu positive. Its derivative
is Stieltjes. A general complete Bernstein function need not have a
Stieltjes derivative; for example x/(1+x) has a double-pole derivative.

## 3. Complete far-prime control for arbitrary polynomial tests

The following estimate pays an actual part of (9) uniformly over degrees.
For a real polynomial `P(t)=sum_i c_i t^i`, put

    C_y(P)=sum_i |c_i| i! (4/y)^i.

For integer N>=8, let L=log N and assume L>3y/2. The contribution of
ALL prime powers n>N to (9) has absolute value at most

    [3sqrt(2y)/(2sqrt(pi))]
      *[1+3y/(2L-3y)] * C_y(P)^2
      *exp[L/2-L^2/(6y)].                                  (10)

There is no omitted prime-power diagonal, arithmetic coprimality condition
or coefficient support hypothesis in this estimate.

**Proof.** For a>=0 set `g_a(z)=z^(-1/2)exp(-a^2/(4z))` on Re z>0.
On `|z-y|=y/2`,

    |z|>=y/2,  Re(1/z)>=2/(3y),

and Cauchy's derivative estimate gives

    |g_a^(m)(y)|<=sqrt(2/y) m!(2/y)^m exp(-a^2/(6y)).

Using `(i+j)!<=2^(i+j)i!j!` and summing the full quadratic polynomial
therefore bounds

    |P(-D_y)^2 g_a(y)|
       <=sqrt(2/y) C_y(P)^2 exp(-a^2/(6y)).                 (11)

Multiply by the literal coefficient Lambda(n)/(2sqrt(pi n)) in (3).
The function

    f(x)=log(x)x^(-1/2)exp[-(log x)^2/(6y)]

is decreasing for log x>=2. Hence the n>N sum is bounded by

    integral_L^infinity a exp[a/2-a^2/(6y)]da
       <=3y[1+3y/(2L-3y)] exp[L/2-L^2/(6y)].

The last inequality completes the square at a=3y/2 and uses the elementary
Gaussian-tail bound. Together with (11) it is exactly (10). QED.

The analogous m-th derivative tail follows from the same proof with
`C_y(P)^2` replaced by `m!(2/y)^m`; no special polynomial basis or
floating coefficient bound is required.

## 4. The remaining archimedean tail is also explicit

For U>0, the contribution of the u>U part of I(y) to (9) is at most

    sqrt(2/y) C_y(P)^2/[4sqrt(pi)(1-exp(-U))]
       *[exp(-U)
          +exp(-U/4-U^2/(24y))/(1/4+U/(12y))].              (12)

Indeed apply (11) with a=0 and a=u/2 to the two terms of the integral,
bound its denominator below by1-exp(-U), and integrate their decreasing
majorants. The derivative of `u/4+u^2/(24y)` is at least
`1/4+U/(12y)` on the tail, giving (12). The constants gamma, log pi
and the rational exp(y/4) term are kept exactly, not treated as tails.

Equations (10)--(12) give a full-source, degree-independent truncation
protocol for any proposed proof of (9), at its actual coefficient resource
C_y(P). They do not give the sign of the retained, highly correlated
prime--Gamma form. Absolute values on that retained core would discard
the cancellation responsible for the actual heat trace.

## 5. Why the existing generic theta inequalities cannot fill the gap

There is a precise actual-target deformation test. Replace the theta
density Phi(u) by its normalized `exp(-epsilon u^2)Phi(u)`, epsilon>0.
It remains positive, symmetric and double-exponentially decreasing. If
the original potential V=-log Phi has V' convex on the positive axis,
the new potential V+epsilon u^2 does too; its strong log-concavity only
improves. Nevertheless its Fourier transform has a nonreal zero for
EVERY epsilon>0.

The last conclusion uses the explicitly imported published theorem of
Rodgers--Tao, [The de Bruijn--Newman constant is non-negative]
(https://arxiv.org/pdf/1801.05914), Theorem1 together with the defining
threshold property on pages1--3. Their kernel uses e^(4u) rather than
this packet's e^(2u), so the time parameter scales by a positive factor4;
its sign is unchanged. Negative time is below the threshold Lambda>=0.
Normalization and variance rescaling do not change whether zeros are
nonreal. No new proof of that deep imported theorem is claimed.

Consequently generic positivity, convexity and the GHS property cannot
alone prove (8), the actual Q-Hankel positivity, or the weighted canonical
completion. A successful proof must use a feature broken by quadratic
damping, such as the exact theta modular/arithmetic identity. Formula
(3) isolates that feature without dividing it away. Its far tails are
paid above; the required sign of the complete retained form is open.
