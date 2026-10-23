# A quantified finite hierarchy of heat-trace derivative signs

23 October2026. Proposed elementary extension of Suvrit Sra's retained-real-zero
comparison, *On some positivity properties of the Riemann Xi function*, v1,
20 October2026, Lemma2.2:
<https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf>.
External novelty of this finite-order extension has not been established.
It gives no new zero-free region, verified height, PF order, or RH conclusion.

For upper-half-plane nontrivial zeta zeros rho=beta+i gamma, with multiplicity,
put delta=beta-1/2, lambda_rho=(gamma-i delta)^2, and

    H(t)=sum_(gamma>0) exp(-lambda_rho*t), t>0.

The conjugate symmetry makes H real. Classical zero counting permits every
fixed finite order of differentiation, locally uniformly on t>0.

## Proposition

Suppose T>=100, every zero with 0<gamma<=T is on the critical line, the first
positive ordinate satisfies 14<gamma_1<15, and

    sum_(gamma>T) gamma^(-2) < 1.                         (H1)

Let q=gamma_1^2 and N be a nonnegative integer with

    8 N log T <= T.                                      (H2)

Then, simultaneously for every integer 0<=n<=N and every t>0,

    (-1)^n H^(n)(t)
       >= [1-T^2 exp(-3T/4)] q^n exp(-q*t) > 0.          (H3)

At the published verified height T=3*10^12 one can take

    N = 12,500,000,000.                                  (H4)

Here H1 follows, for example, from the standard explicit count
`N(Y)<=Y log Y` for Y>=100: integration by parts gives the stronger bound
`sum_(gamma>T)gamma^-2 <= 2(log T+1)/T`. Sra's section2.1 states this
explicit consequence of the published zero-counting input. The finite RH
input is Platt--Trudgian (2021), Theorem1, at height exceeding3*10^12.
These are imported analytic theorems, not checked by finite arithmetic here.

## Proof

Write lambda=a-i b with a=gamma^2-delta^2 and b=2gamma delta. By symmetry it
suffices to take b>=0. Its argument is `-theta`, where

    theta=2 arctan(delta/gamma),  0<=theta<=1/gamma,

using the classical critical strip |delta|<1/2. The real contribution to the
n-th signed derivative is

    |lambda|^n exp(-a*t) cos(b*t-n*theta).                (H5)

For gamma>T and n<=N, H2 gives
`n theta <= N/T <= 1/(8 log T) < pi/2`. As t increases from0, the phase
in H5 starts between -pi/2 and0. Therefore a negative contribution requires
`b*t>pi/2+n theta>=pi/2`. Since b<=gamma, necessarily

    t>pi/(2gamma).                                      (H6)

For gamma>=100 and q<225,
`a-q >= gamma^2-1/4-225 >= 3gamma^2/4`. At a time satisfying H6, its
negative part divided by the retained positive term `q^n exp(-q*t)` is at most

    (|lambda|/q)^n exp(-(a-q)*t)
       <= gamma^(2n) exp(-gamma).                       (H7)

Indeed `|lambda|=gamma^2+delta^2<=q gamma^2`, and `3pi/8>1`.
The function log x/x decreases for x>=T. Hence H2 implies, for gamma>=T,

    2n log gamma <= gamma/4.

Thus H7 is at most `exp(-3gamma/4)`. Since `x^2 exp(-3x/4)` decreases
for x>=100, H1 gives

    sum_(gamma>T) exp(-3gamma/4)
       <= T^2 exp(-3T/4) sum_(gamma>T)gamma^-2
       < T^2 exp(-3T/4).                                (H8)

All zeros up to T contribute positive real terms to every signed derivative.
Retain only the first one, subtract the bound H8 for every possible negative
tail term, and obtain H3. Its bracket is positive for T>=100; for example
the decreasing function T^2 exp(-3T/4) is at most `10000 exp(-75)<1/2`.

For H4 it suffices that log(3*10^12)<30. This follows entirely rationally
from `e>8/3` and `(8/3)^30>3*10^12`; then
`8*(12,500,000,000)*30=3*10^12`. QED.

## Scope of this hierarchy

Complete monotonicity requires every derivative order, with no fixed upper
limit. This proposition supplies only a finite hierarchy derived from a fixed
verified height. Increasing its order requires another input, such as a higher
verified height; there is no argument here that iterates H4 to all orders.
Derivative sign positivity of H is also distinct from total positivity of
the reciprocal-xi density: H4 does not assert PF of order12,500,000,000.

The mechanism is transparent: possible high-zero oscillations begin only
after their Gaussian damping beats the finite power associated with n.
For unbounded n that domination is no longer licensed. Thus a very large
finite set of global signs remains compatible with the unresolved RH problem.
