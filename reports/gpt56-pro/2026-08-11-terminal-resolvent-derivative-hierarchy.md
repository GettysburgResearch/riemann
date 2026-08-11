# Terminal resolvent-derivative hierarchy: fixed safe Euler points replace the moving Gaussian limit

**Date:** 2026-08-11  
**Base:** PR #375 head `a3662f62ac0f1a7ec21bca3498938fedcbeeddba`  
**Status:** new proposed-complete normal form and RH criterion; independent review required  
**RH:** unproved

## Executive result

PR #375 showed that a terminal hypothetical off-line zero pair is detected by a
large-heat-time Gaussian scalar.  The remaining arithmetic sign was still
presented through a parameter `sigma -> infinity` and a moving Gaussian prime
cutoff.

This continuation Laplace-transforms the heat time and then takes high Laplace
moments.  At order `k` the exact zero kernel is

```text
R_(k,y)(z)
 = k! [
     (1-z^2)^(-k-1)
   - 1/2 (1-z^2-2yz)^(-k-1)
   - 1/2 (1-z^2+2yz)^(-k-1)
   ].
```

It has the two signs needed by the Weil criterion:

```text
R_(k,y)(iu) >= 0,
R_(k,y)(y)  < 0.
```

Normalize by `r_(k,y)=R_(k,y)(y)`.  The corresponding scalar is obtained from
only three completed-log-derivative sample points:

```text
s_x + 1,
s_x + sqrt(1+y^2) - y,
s_x + sqrt(1+y^2) + y,
```

and alpha derivatives of these samples through order `k`.  Every point lies
uniformly in `Re(s)>1` for `0<y<1/2`.

Under RH the exact zero expansion is nonnegative.  If RH is false, the terminal
pair of PR #364 contributes exactly `-2m`, while every critical-line and
terminal-nuisance contribution tends to zero exponentially as `k -> infinity`.
Therefore a finite derivative order is negative.

Subject to the terminal-pair theorem:

```text
RH
<=> C_k(x,y) >= 0
    for all k>=0, x real, 0<y<1/2.
```

Dyadic `x,y` suffice, so this is countable.  Every finite member uses absolutely
convergent Euler series and explicit gamma/polygamma terms.

## Why high derivative order works

The target heat residue grows like `exp(3y^2 tau)`.  With the fixed Laplace
weight `exp(-tau)`, the order-`k` target moment is governed by

```text
tau^k exp[-(1-3y^2)tau] d tau.
```

Its normalized mean heat time is asymptotic to

```text
(k+1)/(1-3y^2).
```

Thus raising `k` sends the effective heat time to infinity without moving any
zeta evaluation point.

For a terminal nuisance with exponent `beta<3y^2`, its normalized contribution
has the denominator ratio

```text
[(1-3y^2)/(1-beta)]^(k+1),
```

up to the two subdominant channels, and hence vanishes exponentially.

This is the exact analogue of large-`sigma` terminal isolation in an all-order
resolvent coordinate.

## Complete monotonicity and the new sum-of-squares target

For general safe `alpha`, put

```text
G_(x,y)(alpha)=-Re F_(alpha,y)(1/2+ix).
```

Under RH the exact critical-line expansion is a Laplace transform

```text
G_(x,y)(alpha)
 = integral_0^infinity exp(-alpha tau) W_(x,y)(tau)d tau,
W_(x,y)(tau)>=0.
```

Therefore `G` is completely monotone.  At `alpha=1`, the sequence

```text
A_k=(-1)^k G^(k)(1)=-Re F_k
```

is a Stieltjes moment sequence, so every finite Hankel matrix

```text
H_d=(A_(i+j))_(0<=i,j<=d)
```

is positive semidefinite, with the exact Gram formula

```text
c* H_d c
 = integral |sum c_j tau^j|^2 exp(-tau)W(tau)d tau.
```

A terminal false-RH pair makes `A_k<0` for all sufficiently large `k`, so a
finite Hankel diagonal fails.  This gives a second exact criterion and a more
structured next attack: prove Hankel positivity directly from the three safe
Euler samples.

## The zeroth-order firewall

A direct Abel transform has two incompatible boundaries:

```text
target convergence:          alpha > 3y^2;
absolute Euler interchange:  alpha > y + 1/4.
```

Their gap is exactly

```text
y + 1/4 - 3y^2
 = 3(1/2-y)(y+1/6) > 0.
```

This is the phase-blind saddle exponent isolated on PR #367.  A zeroth-order
resolvent cannot approach the terminal boundary while retaining termwise
absolute Euler summation.

The derivative hierarchy bypasses the firewall by fixing `alpha=1`, safely
above both boundaries, and concentrating through `k` rather than through
`alpha`.

## Finite certificate consequence

For `Re(w)>1`,

```text
-Xi'(w)/Xi(w)
 = sum Lambda(n)n^(-w)
   -1/w-1/(w-1)
   +(1/2)log pi-(1/2)digamma(w/2).
```

At finite `k`, chain rule gives a finite linear combination of derivatives at
the three safe points.  Prime tails are bounded by elementary integral tests
for

```text
sum_(n>P) (log n)^(j+1) n^(-sigma).
```

Hence false RH implies a finite certificate consisting of:

```text
finite derivative order k;
dyadic x,y;
finite prime-power cutoff P;
standard gamma/polygamma intervals;
a strict negative outward-rounded scalar interval.
```

No negative Riemann-data instance is claimed.

## Verification

The retained replay checks:

- rational partial-fraction/product identity;
- Laplace-moment integral against the closed kernel;
- alpha derivatives through order five;
- the inverse-Gaussian three-shift identity;
- critical-line positivity and target negativity;
- exact target coefficient `-2`;
- the uniform safe-Euler margin;
- exact rational factorization of the Abel/Euler gap;
- synthetic terminal-packet convergence to `-2`;
- a line-only moment-Hankel Gram and terminal diagonal failure;
- summable far-zero decay.

Retained verdict:

```text
PASS_TERMINAL_RESOLVENT_DERIVATIVE_HIERARCHY
```

The synthetic scalar evolves as

```text
k=0    10.9693510922...
k=4    -0.2499478783...
k=8    -1.6732085555...
k=16   -2.0012688276...
k=32   -2.0000044420...
k=64   -1.99999999997...
```

This is a diagnostic packet, not evidence about actual zeta zeros.

## Honest frontier

Closed, subject to review:

```text
Gaussian heat family -> rational resolvent family       exact
resolvent -> three fixed safe Euler points               exact
critical-line kernel sign                               exact
target normalized contribution                           -2m exactly
terminal nuisance suppression in derivative order        proposed complete
countable all-order RH criterion                         proposed complete
complete-monotone / moment-Hankel criteria              proposed complete
finite safe-Euler witness under false RH                 proposed complete
zeroth-order Fubini firewall                             exact
```

Open:

```text
unconditional nonnegativity of every resolvent scalar;
a prime-side sum-of-squares / Hankel total-positivity proof;
RH.
```

The next legitimate positive attack is now sharply algebraic: search for a
source-ordered sum-of-squares or variation-diminishing theorem for the
three-point completed-log-derivative hierarchy, rather than estimating the
large Gaussian scalar by absolute values.
