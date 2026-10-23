# Exact real-axis and gamma constants for logistic smoothing

2026-10-21. Companion to `LOGISTIC_ADMISSIBILITY.md`. The checker
`verify_logistic_constants.py` uses rational interval arithmetic only
for every pass/fail decision. Decimal output is informational.

Assume theta=1.1338, 0<eta<=.0075, and .99<=sigma<=1. Write a=2sigma-1
and f(u)=eta w(eta u)/(1+exp(-au)), as in the companion note.

## 1. The signed real-axis correction

The exact correction is

    E_f(sigma)=integral_0^infinity
       exp(-(sigma+2)u)[f(0)-f(u)]/(1-exp(-2u))du.

The exact trigonometric enclosures in the checker imply

    5.67<w(0)<6,   ||w''||_infinity<350<1000.

For 0<=u<=10, Taylor's theorem and w'(0)=0 give

    w(eta u)>=w(0)-500 eta^2 u^2.

It follows that f(u)>=f(0) if

    1000 eta^2 u^2 <= w(0)(1-exp(-a u)).                  (R1)

The function u^2/(1-exp(-a u)) is increasing for u>0: its derivative
has the sign of 2(exp(a u)-1)-a u, which is positive. Thus it suffices
to check (R1) at u=10, eta=.0075, a=.98. The checker proves

    1000*(.0075)^2*100 = 5.625
       < 5.67*(1-1/10000) < w(0)(1-exp(-9.8)).

The last inequality uses the positive Taylor lower bound exp(9.8)>10000.
The contribution from u<=10 is therefore nonpositive. Since f>=0,
the remaining positive part is at most

    f(0) exp(-29.9)/[2.99(1-exp(-20))]
      < eta * 3/1495000000000
      < 10^-10 eta.                                    (R2)

For the displayed rational bound use f(0)<3eta, exp(29.9)>19^10>10^12,
and exp(20)>2. The first exponential inequality follows by raising the
positive Taylor bound exp(2.99)>19 to the tenth power. Thus (R2) is
uniform; it is not a grid computation.

## 2. The source trigonometric polynomial and the archimedean constant

Use BTY's exact integer vector c_0,...,c_16 and normalization 14912370,
so that P(x)=|sum c_j exp(ijx)|^2/14912370=sum a_k cos(kx).
The checker reconstructs the rational a_k directly and verifies

    a_0=1, a_1=865534/497079,
    a=sum_(k>=1) a_k=2919857/828465,  a_k>=0.

The coefficient independent of log t in the gamma contribution is
bounded above, for sigma<=1, by

    C_arch = -log(pi)/2 + psi(3/2)/2
                   + (1/2)sum_(k>=1) a_k log(k/(2pi)).   (R3)

Here psi is increasing on the positive real axis and
psi(3/2)=2-gamma-2log2. The small high-height error in replacing
Re psi((sigma+ikt)/2+1) by log(kt/2) is separate; it has not been
silently included in (R3).

The checker encloses pi by Machin's formula with alternating rational
arctangent series. Logarithms use

    log x = 2 sum_(j>=0) z^(2j+1)/(2j+1), z=(x-1)/(x+1),

after exact powers of two reduce x to [1,2]. The positive tail is
bounded geometrically. A sufficient elementary lower bound for Euler's
constant is

    gamma > H_100-log(100)-1/200.

Indeed H_N-log N-1/(2N) increases to gamma, by the trapezoidal upper
bound for the integral of the convex function 1/x on [N,N+1]. No
precomputed decimal value of gamma is used.

Substitution in (R3) gives the exact rational enclosure

    C_arch < -3.0127153623... < -3.0126.                 (R4)

Only the final decimal rendering is rounded. The comparison with the
rational -15063/5000 is exact.

## 3. Explicit derivative bounds and scope

The checker also certifies global derivative bounds for the compact
extension of the source w:

    ||w||_infinity   < 4047/64,
    ||w'||_infinity  < 20967/160,
    ||w''||_infinity < 17319/50,
    ||w'''||_infinity< 235953/250.

The third derivative is interpreted piecewise; the second derivative
is continuous at the support endpoint. These follow directly from
the elementary sine/cosine formula and uniform bounds for its linear
factor. They justify the relaxed bound 1000 used by the companion.

The checker has 22 positive checks and four deliberately false negative
controls. It does not prove a new zero-free constant. A final numerical
zero-free argument still needs the logistic transform at the two
real zero-detector arguments, uniform parameter control, the induction
over heights, and the external large-height zero-free region.
