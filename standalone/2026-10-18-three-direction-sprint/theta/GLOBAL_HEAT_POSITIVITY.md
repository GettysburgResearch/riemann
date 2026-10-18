# A global positive inequality for the actual prime--Gamma heat kernel

**Status: PROPOSED native analytic proof with a directed primitive zero
census.** The actual kernel defined below is strictly positive for every
positive argument. Complete monotonicity, positivity of every polynomial
quadratic form, RH, and an improved zero-free strip are NOT concluded.
The spectral-zeta/heat viewpoint is classical; see Voros,
[Zeta functions for the Riemann zeros](https://www.numdam.org/item/10.5802/aif.1955.pdf).
No priority claim is made for heat-trace positivity. The point here is a
complete explicit arithmetic inequality with a short fresh primitive
census, no imported zero table, and a paid infinite complement.

## 1. Exact target and theorem

Use `xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2`. For y>0 put

    I(y)=integral_0^infty
             [e^(-u)-e^(-u/4-u^2/(16y))]/(1-e^(-u)) du,

    k(y)=e^(y/4)+[I(y)-gamma-log pi-2S(y)]/(4sqrt(pi y)),
    S(y)=sum_(n>=2)Lambda(n)n^(-1/2)e^(-(log n)^2/(4y)). (1)

Every prime power is present. The simultaneous endpoint cancellation in I
and the convergence of S are proved in
[ARITHMETIC_STIELTJES_KERNEL.md](ARITHMETIC_STIELTJES_KERNEL.md), which also
derives the exact transform, for x>1/4,

    d/dx log[xi(1/2+sqrt(x))/xi(1/2)]
                      =integral_0^infty e^(-xy)k(y)dy.       (2)

**Theorem.** For this literal arithmetic kernel,

    k(y)>1/(2000sqrt(y)),             0<y<=1/50,
    k(y)>(1/3)e^(-200y),              y>=1/50.              (3)

The small-y estimate is purely analytic and bounds ALL prime powers by
an explicit integral. The large-y estimate uses only the complete fresh
zero census below height20, the native whole-theta Gaussian bound
`|xi(1/2+iz)/xi(1/2)|<=exp(5|z|^2/176)`, and an infinite zero-count tail.
No off-axis zero above20 is assumed real or omitted.

## 2. A global elementary bound for the archimedean integral

For u>0 let

    R(u)=1/(1-e^(-u))-1/u-1/2.

The following bounds hold on the ENTIRE positive half-line:

    u/12-u^3/720 <= R(u) <= u/12.                         (4)

They can be proved directly without a truncated asymptotic expansion.
After multiplication by positive denominators, the upper inequality is

    e^u(u^2-6u+12)-(u^2+6u+12)>=0.

Its Taylor coefficients through degree4 vanish, and the coefficient of
u^n for n>=5 is `(n-3)(n-4)/n!>0`. The lower inequality is

    (720+360u+60u^2-u^4)
        -e^u(720-360u+60u^2-u^4)>=0.

Its coefficients through degree6 vanish, and for n>=7 the coefficient
is `(n-3)(n-5)(n-6)(n+8)/n!>0`. This proves (4) globally.

Write `E(u)=e^(-u)-e^(-u/4-u^2/(16y))`. It is negative exactly when
`0<u<12y`. On the positive part of E use the lower bound in (4), and on
its negative part use the upper bound. Therefore

    integral E(u)R(u)du
       >=(1/12)integral uE(u)du
                    -(1/720)integral u^3 max(E(u),0)du
       >=(1-8y)/12-1/120
        =3/40-2y/3.                                    (5)

Here `max(E,0)<=e^(-u)`, `integral u^3e^(-u)du=6`, and
`integral u e^(-u/4-u^2/(16y))du<=8y`.

The other two pieces follow from elementary Gaussian integrals. First,

    J0=integral_0^infty [e^(-u)-e^(-u^2/(16y))]du/u
                     =-gamma/2-(1/2)log(16y).

For example, subtract the two exponential integrals with a common lower
cutoff epsilon and pass to zero. Using
`1-e^(-u/4)>=u/4-u^2/32` gives

    integral E(u)du/u >= J0+sqrt(pi y)/2-y/4.              (6)

Using `e^(-u/4)<=1-u/4+u^2/32` gives

    (1/2)integral E(u)du
                  >=1/2-sqrt(pi y)+y-sqrt(pi)y^(3/2)/4.  (7)

All integrations above are absolute after the stated numerator
differences are kept together. Combining (5)--(7),

    I(y)>=I_lower(y)
      :=-gamma/2-(1/2)log(16y)+23/40
                  -sqrt(pi y)/2+y/12-sqrt(pi)y^(3/2)/4.  (8)

This lower bound remains valid for every y>0; it is used only in its
effective small-y range below.

## 3. Every prime-power tail is paid on 0<y<=1/50

Let `y0=1/50`, `L=log2`. Since `Lambda(n)<=log n`,

    S(y)<=sum_(n>=2)log(n)n^(-1/2)e^(-(log n)^2/(4y)).

For y<=y0 the summand, viewed as a function of real n>=2, decreases:
its logarithmic derivative in a=log n is `1/a-1/2-a/(2y)<0`.
The elementary sum--integral bound consequently gives

    S(y0)<=P0
      :=L/sqrt(2)e^(-L^2/(4y0))
           +2y0 L/(L-y0)e^(L/2-L^2/(4y0)).               (9)

For the integral substitute a=log n. The derivative of
`a/2-a^2/(4y0)` is `-(a-y0)/(2y0)`; one integration and the decreasing
exponential bound on the remaining integral give precisely the second
term in (9). Thus the sum is not truncated at a convenient prime.
Also S(y)<=S(y0) because each term increases with y.

Define

    B0(y)=4sqrt(pi y)+I_lower(y)-gamma-log pi.

Multiplying (1) by `4sqrt(pi y)` and using `e^(y/4)>=1` gives

    4sqrt(pi y)k(y)>=B0(y)-2S(y).                        (10)

The derivative of B0 is negative throughout `(0,y0]`: after multiplying
it by y and dropping its last negative term, its upper bound is

    -1/2+(7sqrt(pi)/4)sqrt(y)+y/12
    <=-1/2+(7sqrt(pi)/4)sqrt(y0)+y0/12<0.                (11)

The endpoint arithmetic, independently checked with outward arb balls,
is

    B0(y0)-2P0 > 0.00919377004398 > 1/200,              (12)
    -1/2+(7sqrt(pi)/4)sqrt(y0)+y0/12 < -0.059.

These are inequalities between explicit elementary constants, not a
numerical quadrature of k. Coarse rational constants already suffice:
`gamma<.578`, `log pi<1.145`, `sqrt(pi) in(1.772,1.773)`,
`log(25/8)>1.138`, `sqrt(1/50) in(.1414,.1415)`, and `P0<.0015`
give a lower bound greater than.006 in (12). The included directed
checker evaluates the stronger displayed margin directly.

Equations (9)--(12) imply `4sqrt(pi y)k(y)>1/200` on the whole range.
Since pi<4, this proves the first bound in (3), with slack.

## 4. Spectral identity without RH and the complete zero count

Write a nontrivial zeta zero with positive imaginary part as

    rho=1/2+delta+i gamma_rho,
    0<gamma_rho,  |delta|<=1/2.

All multiplicities are retained. Classical even paired Hadamard
factorization of xi, of order1, gives

    d/dx log[xi(1/2+sqrt(x))/xi(1/2)]
                 =sum_(Im rho>0)1/[x-(rho-1/2)^2].          (13)

There is no quadratic exponential factor. Summability of the paired
reciprocal squares is part of this classical factorization. For x>1/4,
termwise Laplace integration is absolute, since
`Re (rho-1/2)^2=delta^2-gamma_rho^2` and the reciprocal-square sum
converges. Uniqueness of the Laplace transform in (2) yields

    k(y)=sum_(Im rho>0)exp((rho-1/2)^2 y),  y>0.           (14)

This continuous series is real by the functional equation and
conjugation symmetry. An off-axis pair contributes a cosine and is NOT
assumed positive. In particular we will only use

    |exp((rho-1/2)^2y)|<=e^(y/4)e^(-gamma_rho^2 y).        (15)

Let N_+(T) count ALL nontrivial zeros with `0<Im rho<=T`, including
off-axis zeros and multiplicities. The actual full-theta Gaussian bound
from [THETA_GROWTH.md](THETA_GROWTH.md) is

    H(z)=xi(1/2+iz)/xi(1/2),  |H(z)|<=e^(A|z|^2),
    A=5/176, H(0)=1.

Jensen at radii r and `sqrt(e)r` shows that the number n(r) of ALL H
zeros in `|z|<=r` satisfies `n(r)<=2e A r^2`. Boundary radii are obtained
by an arbitrarily small enlargement if necessary. Each positive-height
zeta zero counted by N_+(T), together with its negative-height partner,
lies in `|z|<=sqrt(T^2+1/4)`. Hence

    N_+(T)<=C(T^2+1/4),  C=e A=5e/176.                  (16)

This deliberately coarse global count uses the exact actual theta
growth, not a numerical extrapolation of the low zeros.

## 5. The fresh first20 census

The directed checker [check_heat_positive.py](check_heat_positive.py)
evaluates the literal completed-zeta formula on the counterclockwise
rectangle

    -1/8<=Re s<=9/8,  1<=Im s<=20.                      (17)

The gamma and zeta factors are evaluated by python-flint0.9.0 acb/arb
with256-bit outward rectangular balls. No moment/source JSON and no
stored zero location enter the calculation.

Each COMPLETE contour segment is an acb input rectangle containing
every point of that segment. Its output rectangle is enlarged to contain
the exact dyadic rational midpoints of both endpoint evaluations. If
that convex output rectangle excludes0, the exact image curve is
homotopic to the chord of those rational endpoint values without meeting0.
Otherwise the input segment is bisected, with no segment omitted.
Thus the whole exact contour image is homotopic to an exact rational
polygon. Its winding number is computed by Fraction arithmetic and
signed crossings of the positive real ray; no floating angles are used.

The fresh result has892 accepted segments, winding number1. A separate
fully covered rectangle with top height10 has winding number0. Reversing
exact test polygons reverses the winding sign, and a translated empty
polygon has zero winding. The recorded [HEAT_POSITIVITY_CHECKS.json]
(HEAT_POSITIVITY_CHECKS.json) binds the checker source and all margins;
`--check` reruns the primitive evaluations before comparing the record.

There are no zeros below height1: the positive even theta measure gives
`|H(z)-1|<=exp(A|z|^2)-1<1` on `|z|<=4`, since
`exp(5/11)-1<1`. Every zero of xi is in `0<=Re s<=1`, so a positive-height
zero below1 would be in this disk. The census (17) therefore covers ALL
positive-height zeros through20, not just zeros near the critical line.

Finally, the literal real values `xi(1/2+14.13i)` and
`xi(1/2+14.14i)` have opposite directed signs. Their reality is the exact
functional symmetry; the acb imaginary enclosures also contain0. The
intermediate value theorem supplies a critical-line zero. The count1
above proves that it is the only positive-height zero below20 and has
multiplicity1. Denote its height by gamma0; in particular

    gamma0^2<(14.14)^2<200.                               (18)

## 6. Every remaining zero is paid for y>=1/50

Separate the first term of (14). Every other zero has gamma_rho>=20.
From (15), Stieltjes summation and (16),

    |k(y)-e^(-gamma0^2 y)|
       <=e^(y/4)sum_(gamma_rho>=20)e^(-gamma_rho^2 y)
       <=e^(y/4) 2y integral_20^infty tN_+(t)e^(-yt^2)dt
       <=C(400+1/4+1/y)e^(-(400-1/4)y).                 (19)

The discarded integration boundary term is nonpositive. The inequality
still counts the first zero inside the cumulative upper bound N_+, so
it enlarges rather than shrinks the remaining tail. All multiplicities
and possible off-axis cosine phases are covered by (15).

By (18), dividing (19) by the first positive term gives the upper bound

    C(400+1/4+1/y)e^(-(799/4)y).                         (20)

Both factors decrease with y. At y=1/50 the directed upper bound is

    0.640028163231122 < 2/3.

For an elementary coarse check, use `C<.0773`, the parenthesis<451,
and `exp(-799/200)<.019`: their product is.6623837<2/3.
Thus (19) is strictly smaller than two thirds of the first term at every
y>=1/50. Equation (18) now proves the second inequality in (3).

## 7. Replay and remaining all-order gate

With the bundled Python executable and the sibling pinned flint package,

    python theta/check_heat_positive.py --check theta/HEAT_POSITIVITY_CHECKS.json
    python -O theta/check_heat_positive.py --check theta/HEAT_POSITIVITY_CHECKS.json

both perform the full primitive contour replay and all elementary
constant checks. An explicit `--dependency-dir` is supported. The proof
imports Arb/acb's directed special-function enclosure contract, classical
xi factorization and the theta/xi identity; the actual theta growth bound
and both infinite complements are proved in this packet.

This is a global inequality for the literal signed prime--Gamma kernel.
It does not establish `(-1)^m k^(m)(y)>=0` for every m, nor
`P(-d/dy)^2 k(y)>=0` for every real polynomial P. Positivity of k by itself
does not supply the weighted canonical/Hamburger positivity gate in#1003.
No derivative or moment ladder is inferred from (3). The uniform
all-order arithmetic cancellation remains open.
