# A quantitative cost of prescribed quadratic prime signs

23 October2026. Supplement to
`ARTIN_RESCALE_AND_NORMAL_FAMILY_OBSTRUCTIONS.md`, SHA256
`655e3bdc371499d89246f820a4919bba5cb018794f367e197c61d642a581f620`.
This is a conditional analytic obstruction, not a zero-free improvement.

Retain its primitive quadratic characters chi_y, with chi_y(p)=-1 for every
prime p<=y. Assume they are all nonzero on Re(s)>beta for a common beta<1.
Fix `0<R<min(1/2,1-beta)` and put

    delta_y = 3 log log y / log y,
    M_y = max(1, max_(|s-1|<=R) |L(s,chi_y)|).

Then, for all sufficiently large y (depending on R),

    M_y >= delta_y * (3/2)^((R-3delta_y)/(2delta_y)).       (Q1)

In particular

    liminf_(y->infinity) [log M_y * log log y / log y]
       >= R log(3/2)/6 > 0.                              (Q2)

This explicitly prevents conductor-independent local boundedness; it does not
assert that the zero-free premise is false.

## Proof

Set F_y(s)=L(s,chi_y) and F_infinity(s)=zeta(2s)/zeta(s). The coefficients
of their Dirichlet series agree for every n<=y and have absolute value at most1.
For real v>0 the decreasing-series integral estimate therefore gives

    |F_y(1+v)-F_infinity(1+v)| <= 2 y^(-v)/v.             (Q3)

At v=delta_y this upper bound is
`2/[3 (log y)^2 log log y]`, which is o(delta_y). At v=2delta_y it is
even smaller. The simple pole of zeta at1 gives

    F_infinity(1+v)=zeta(2)*v+O(v^2) as v->0+.

Consequently

    F_y(1+2delta_y)/F_y(1+delta_y) -> 2,
    F_y(1+2delta_y) >= delta_y                            (Q4)

for all sufficiently large y. Both quantities are positive, either from their
quadratic Euler products in Re(s)>1 or from Q3 and the asymptotic. In particular
the ratio in Q4 is at least3/2 eventually.

Since F_y has no zeros on the closed disk |s-1|<=R, the function

    u_y(s)=log M_y-log|F_y(s)|

is nonnegative and harmonic on a neighborhood of that disk. Use Harnack's
inequality in the disk centered at `s2=1+2delta_y` of radius `R-2delta_y`.
This disk is contained in |s-1|<=R. The point `s1=1+delta_y` lies at distance
delta_y from its center. For delta_y<R/3, Harnack gives

    u_y(s1) <= C_y u_y(s2),
    C_y=(R-delta_y)/(R-3delta_y).

Rearranging, without replacing either logarithm by an absolute value,

    log M_y >= log F_y(s2)
                +(R-3delta_y)/(2delta_y)*log(F_y(s2)/F_y(s1)).

Insert Q4 and its ratio lower bound to obtain Q1. Multiplying its logarithm
by log log y/log y yields Q2, because log delta_y contributes o(1). QED.

The estimate concerns the size forced somewhere in a fixed complex disk; it
does not claim growth at s=1 itself. The conductor of chi_y is allowed to
grow, and no unproved uniform bound on that conductor or least-prime theorem
is used. All primes up to y are prescribed by the explicit CRT construction
in the companion note. The only additional analytic input here is the usual
Harnack inequality for a nonnegative harmonic function on a disk.

This strengthens the companion normal-family obstruction: any proposed
field-limit bootstrap of this particular sequence must explicitly accommodate
at least the growth in Q1. The argument is compatible with GRH and provides
no contradiction to RH or to the common-strip hypothesis.
