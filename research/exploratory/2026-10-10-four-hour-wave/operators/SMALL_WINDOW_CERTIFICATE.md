# A native full-source continuum base window

Status: PROPOSED_EXACT, rational producer/checker replay passes; independent
review pending.  Scope: **every** complex L2 test on the fixed interval
[0,1/20], for the literal arithmetic kernel of OPERATOR_AUDIT.md O1.  This is
a continuum lower bound, not a positive sampled section.  Exact sources:
that kernel definition; Euler's identity zeta(2)=pi²/6 and its absolutely
convergent logarithmic derivative at 2; Machin's pi identity.  What was run:
`check_small_window.py`, with normal Python and Python -O and identical results.
Smallest remaining global gap: no propagation to arbitrary L, nor to L=1,
is obtained.  The predecessor's terminal xi/Weil identification stays separate.

## Statement with full quantifiers

Use the unchanged b=3/2 and source W from the codimension-18 note.  Put
L=1/20.  For h in L2(0,L), define H(t)=integral_0^t h(u)du and mu=H(L).
Then the complete source form satisfies

\[
q_L(h,h)=b\int_0^L\int_0^L\overline{h(t)}W(t-u)h(u)\,du\,dt
\ge\left\|H-\frac\mu2\right\|_2^2
 +\frac{37}{2000}|\mu|^2.
\tag{S1}
\]

In particular it is strictly positive for every nonzero h.  This primitive
norm is not a uniform L2 spectral gap.  By restriction, the same positivity
holds on each shorter interval; S1 concerns the exact interval L=1/20.

## 1. Complete prime source bound from elementary tails

Write P2=sum_(n>=2) Lambda(n)/n².  Absolute Euler-product differentiation and
zeta(2)=pi²/6 identify

\[
P2=\frac6{\pi^2}\sum_{n\ge2}\frac{\log n}{n^2}.
\]

For f(t)=log(t)/t² and N=128, f''(t)=(6log(t)-5)/t^4>0 for t>=N.
On each unit interval, the trapezoid error is

\[
\frac{f(n)+f(n+1)}2-\int_n^{n+1}f(t)dt
=\frac12\int_n^{n+1}(t-n)(n+1-t)f''(t)dt
\le\frac18\int_n^{n+1}f''(t)dt.
\]

Summing, including the half endpoint, and using -f'(N)=(2log(N)-1)/N³ gives

\[
\sum_{n\ge N}f(n)\le\frac{\log N+1}{N}
 +\frac{\log N}{2N^2}+\frac{2\log N-1}{8N^3}.
\tag{S2}
\]

The checker encloses each prefix log by a positive atanh series after dyadic
range reduction, rounds upper terms upward at scale 2^100, and uses a rational
Machin lower bound on pi.  Equation S2 then proves **P2<57/100**.  The computed
complete upper bound is <0.56996110.  For a needed lower bound the single n=2
term gives P2>=log2/4; its log is enclosed by the same rational series.

## 2. Point and whole-interval curvature inequalities

There is no prime-power cusp on [0,L], because exp(L)<2.  The exact complete
source therefore has, for x>=0 in this interval,

\[
W(x)=\frac12e^{x/2}+C_be^{-bx}+S_\Gamma(x)-(P2/b)\cosh(bx),
\quad S_\Gamma(x)=\sum_{j\ge1}\frac{e^{-\lambda_jx}}{\lambda_j^2-b^2}.
\]

The constants checker gives C_b> -59/125.  For x>0 the gamma series can be
differentiated termwise; its coefficients and second derivative terms are
positive.  Its first derivative is negative.  Rational exponential Taylor
series with an explicit geometric upper remainder give

\[
W(L)>1/250,\qquad W'(L)<-1/3,\qquad W''(x)>0\ (0<x\le L).
\tag{S3}
\]

The complete coverage for the third inequality is analytic: for every x<=L,
the growing positive term is >=1/8, C_b b² exp(-bx)>=-(59/125)b², each of
the first 64 positive gamma second-derivative terms is at least its value at L,
and -(bP2)cosh(bx)>=-(57/100)b*cosh(bL).  All omitted gamma terms are positive.
The same 64 terms give a lower bound on S_Gamma(L) and on -S_Gamma'(L), which
enclose the first two scalars.  The P2 lower bound is used in the W' upper
bound.  The artifact stores rational directed enclosures for all three.

Convexity implies W'(x)<=W'(L)<0 for 0<x<=L, and W(x)>=W(L)>0.  Its derivative
has a logarithmic singularity at zero, but the weighted curvature is integrable.
Tonelli gives

\[
\int_0^L xS_\Gamma''(x)dx
=\sum_{j\ge1}\frac{1-(1+\lambda_jL)e^{-\lambda_jL}}
 {\lambda_j^2-b^2}
\le\sum_{j\ge1}\frac1{\lambda_j^2-b^2}<\infty.
\tag{S4}
\]

The other curvature terms are bounded on the compact interval.  No bounded
second derivative at zero is assumed.

## 3. Positive triangle mixture covers all tests

For 0<=x<=L, integration twice, with S4 handling the x=0 endpoint, gives

\[
W(x)=W(L)+[-W'(L)](L-x)
 +\int_0^L(s-x)_+W''(s)ds.
\tag{S5}
\]

For any s>0 the triangle kernel is positive on the whole real line:

\[
(s-|t-u|)_+=\int_{\mathbb R}
 1_{[r,r+s]}(t)1_{[r,r+s]}(u)dr.
\]

Its form is the squared L2 norm of the moving interval integral of the zero
extension of h.  The W'' mixture in S5 is therefore positive.  Absolute Fubini
is justified by S4, bounded W, and h in L1 on the finite interval.
For the triangle with s=L its form is exactly

\[
\int_0^L\bigl(|H(t)|^2+|\mu-H(t)|^2\bigr)dt
=2\|H-\mu/2\|_2^2+(L/2)|\mu|^2.
\]

Using bW(L)>3/500 and b[-W'(L)]>1/2, and dropping only the positive curvature
mixture, gives S1 because L/4+3/500=37/2000.  If the right side vanishes,
mu=0 and the continuous primitive H is zero almost everywhere, hence h=0.

## Limits

This certificate authenticates a native source-positive interval.  It does not
give an interval-joining theorem: cross terms between disjoint windows retain
the prime-power cusps and need their own control.  The same simple convex
mixture cannot continue even to L=1, where W(L) and source curvature are not
globally positive.  The separate codimension-14 reduction is the useful larger
window tool; its effective lower sign is still open.
