# A compact ordinary-zeta detector and complete signed energy experiments

Status: **PROPOSED exact reductions and finite directed calculations.**
The global critical energy bound remains OPEN. These computations do not
certify an asymptotic bound or any new zero-free region.

The purpose of changing the smoothing is concrete: make the full physical
energy at any finite horizon exactly finite, while retaining every
hypothetical off-critical zero of ordinary zeta. Unlike a Gaussian source,
this experiment needs no infinite arithmetic tail truncation.

## 1. Compact support does not erase any off-critical target zero

For h>0 put

    psi_h(u)=(1-|u|/h)_+,
    W_h(y)=y^(-1/2)psi_h(log y),
    a(n)=product_(p|n)(1-p)/n,
    A_h(X)=sum_n a(n)W_h(n/X),
    f_h(X)=X^(-1/2)A_h(X),
    E_h(T)=integral_0^T |f_h(X)|^2 dX/X.

The support is y in [exp(-h),exp(h)]. Thus the full source up to horizon
T has ONLY n<=exp(h)T, and is zero for X<exp(-h).

The exact Mellin transform is

    What_h(s)=2[cosh(h(s-1/2))-1]/[h(s-1/2)^2].           (1)

Its value at s=1/2 is the removable value h. All its actual zeros are

             s=1/2+2pi i k/h, k a nonzero integer.        (2)

The coefficient Dirichlet series is zeta(s+1)/zeta(s). Hence, initially
for Re s>1, absolute interchange gives

    integral_0^infinity A_h(X)X^(-s)dX/X
                    =What_h(s) zeta(s+1)/zeta(s).        (3)

At EVERY nontrivial zeta zero rho with Re rho>1/2, What_h(rho) is
nonzero by (2), and zeta(rho+1) is nonzero by its absolutely convergent
Euler product. The pole of (3) at rho retains its full multiplicity.
No auxiliary field, family quantifier, or unknown zero-location premise
is used in this statement.

**Energy consumer.** Fix 0<=kappa<1. If, for every epsilon>0,

                 E_h(T)<<_epsilon T^(kappa+epsilon),    (4)

then ordinary zeta has no zero to the right of (1+kappa)/2. To prove
this, rewrite the left side of (3) as
integral f_h(X)X^(1/2-s)dX/X. On dyadic intervals, Cauchy--Schwarz and
(4) give a convergent geometric majorant whenever Re s>(1+kappa)/2.
The lower endpoint is already compact. This integral is holomorphic
throughout that half-plane, contradicting any retained pole in (3).
The same bound on compact subsets justifies complex differentiation.

Thus the subpower case kappa=0 is an RH-facing criterion, and an estimate
with kappa below the working imported exponent would improve the strip.
Nothing in the finite calculations below establishes (4).

## 2. Exact full-energy algorithm at h=log 2

Put b_n=a(n)/sqrt(n), t=log X. The full source is the sum of tents

                 f_h(exp t)=sum_n b_n psi_h(t-log n).

For h=log2 every breakpoint is t_k=log(k/2), k>=1. At t_k the slope
in t has the exact jump

    Delta_k=[b_k-2*1_(2|k)b_(k/2)+1_(4|k)b_(k/4)]/h.    (5)

This accounts respectively for entry, midpoint, and exit of every tent.
At t_1=-h the value and pre-entry slope are zero. On each full interval
[t_k,t_(k+1)] the amplitude is linear. If its two endpoint values are
v,w and its length is d=log((k+1)/k), its exact squared integral is

                       d(v^2+vw+w^2)/3.                 (6)

Consequently E_h(T) at an integer T is computed by precisely 2T-1
intervals. Terms n>2T are exactly absent, not bounded heuristically;
the full physical interval below X=1/2 is exactly zero. Directed
evaluation of (5)--(6) gives the entire energy.

The checker reconstructs every a(n) from an integer prime sieve, with
an independent trial-factor check through n=5000. It verifies the
log-slope source against direct tent summation at five nodes. It also
compares the FULL Gram sum at T=1,2,5,17, including every ordered
arithmetic pair, with the independent piecewise-linear integration.
Neither comparison uses a deposited certificate as an acceptance input.

## 3. Complete prime rays, with no discarded common-factor sector

For distinct primes p<q with q/p<2, write delta=log(q/p) and let
u=t-log(dp). The product of the two tents in the ray (n,m)=(dp,dq)
is supported on [delta-h,h]. Its three polynomial pieces are

    (u+h)(u-delta+h)/h^2,     delta-h<=u<=0,
    (h-u)(u-delta+h)/h^2,     0<=u<=delta,
    (h-u)(h+delta-u)/h^2,     delta<=u<=h.                (7)

Integrate each through the exact upper endpoint log(T/(dp)). The ray's
arithmetic coefficient is a(dp)a(dq)/(d sqrt(pq)), with NO restriction
on common primes between d,p,q. There is exactly zero overlap if
d>=2T/q; including the equality as a zero term is harmless. Thus the
sum over all d is a literal finite sum through floor(2T/q).

For the independent full-Gram toy checks the checker also covers
2<q/p<4: only the middle quadratic in (7) remains, on [delta-h,h].
At q/p>=4 the overlap is identically zero. Coincident endpoints are
handled by exact integer comparisons before any interval arithmetic.

## 4. Actual full-source cancellation, certified at two horizons

The 256-bit python-flint 0.9.0 run retains all source modes, every
physical cell, all selected prime pairs, and all their common factors.
The following strict rational gates follow from its complete balls:

| Horizon T | Full E_h(T) | Selected prime-ray sector | Signed complement |
|---|---:|---:|---:|
| 65536 | (1.137, 1.138) | (1.616, 1.617) | (-0.479, -0.478) |
| 262144 | (1.138, 1.139) | (2.725, 2.726) | (-1.588, -1.587) |

The first sector uses all distinct ordered primes in [256,384]: 22 primes,
462 ordered rays, and 88975 nonnegative common-factor indices before
their signed coefficients are applied. The second uses [512,768]:
38 primes, 1406 ordered rays, and 543014 common-factor indices.

The signed complement is defined by the exact identity
Full=PrimeSector+Complement. It is strictly negative at both horizons.
This does not conflict with nonnegativity of the FULL energy; a selected
Gram sector is not itself a squared norm. It directly exhibits coherent
compensation in the actual arithmetic source. Summing absolute sector
bounds would lose this cancellation.

The finite ranges give no global E_h(T) upper bound. They authenticate
the observable and the presence of signed compensation, rather than
support an extrapolated numerical proof of RH.

## 5. Further legal smoothing freedom

Every h>0 in (1) retains all off-critical target zeros. Products of such
Mellin factors do too; in log space they correspond to convolutions of
compact tents. This raises smoothness and preserves compact support.
If phi is another compact log-kernel supported in [-H,H], Minkowski gives

    E_(psi*phi)(T)^(1/2)<=||phi||_1 E_psi(exp(H)T)^(1/2). (8)

In particular such convolutions preserve a known energy exponent, with
its scale and constants explicitly paid. One can also place a kernel's
critical-line notches near finitely known critical zeros without ever
canceling an off-critical zero. Whether a chosen profile makes the
remaining complete signed estimate easier is an analytic question; a
smaller finite residual by itself does not answer it.

Reproduction:

```
python certify_tent_energy.py --dependency-dir /path/to/python-flint
```

`TENT_ENERGY_CHECKS.json` records the complete balls, source/checker
identities, independent full-Gram comparisons and exact finite coverage.
No inherited repository source or integrated scientific status is changed.
