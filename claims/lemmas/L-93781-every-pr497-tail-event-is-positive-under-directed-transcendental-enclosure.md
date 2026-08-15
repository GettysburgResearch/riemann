# L-93781 — Every PR #497 tail event is positive under directed transcendental enclosure

Claim ID: `L-93781`  
Status: **PROVED DIRECTED FINITE-EVENT CERTIFICATE ON THE PR #497 ANALYTIC FORMULA**  
Created: 2026-08-15  
Depends on: `L-93600`, exact event reduction in `L-93601`, `L-93780`  
Replay: `X-93780-target-lorenz-directed-tail`  
RH status: **unproved**

Let `Theta_j(p,y)` be the causal proportional determinant of PR #497, with
`x=py>=166000`, `p>=67`, `1<=y<67` and `2<=j<=66`. Then the complete lower
envelope used in `L-93601` satisfies

\[
\boxed{\underline\Theta_j(x)>26.7858>26}
\tag{L-93781.1}
\]

on every real tail interval. Its parent part satisfies

\[
\boxed{\underline\Theta_j^{par}(x)>79.2368>79}
\tag{L-93781.2}
\]

and every finite-interval derivative enclosure satisfies

\[
\boxed{\frac d{dt}\underline\Theta_j^{par}(t^2)>0.2397>0.23.}
\tag{L-93781.3}
\]

## Directed arithmetic contract

The event abscissae

\[
x=d,\qquad x=jd,\qquad x=(j+1)d,
\qquad d\mid P_{61},
\]

are sorted exactly as unsigned 128-bit integers. Every conversion of an
integer event to `long double` is bracketed by its adjacent representable
numbers. All square roots, logarithms, prefix sums, coefficient products,
values, derivatives and final-tail persistence polynomials are propagated by
`Boost.Numeric.Interval` under saved hardware-directed rounding. Compilation
uses

```text
-frounding-math -fno-fast-math.
```

The constants `zeta(1/2)` and `zeta'(1/2)` enter only through the rational
intervals of `L-93780`.

The 65 independent row sweeps process exactly

\[
65\cdot3\cdot2^{18}=51118080
\]

event records. The global directed records are

```text
full determinant lower:       26.785819887137002938...
parent determinant lower:     79.236873638887636066...
parent derivative lower:       0.239715873017393344...
minimum row:                   66
minimum x:                     166000
```

For the final unbounded interval, the directed lower endpoints of both the
second-derivative persistence polynomial and its derivative are positive.
Therefore no floating-point point evaluation or informal “one-unit reserve” is
used in (L-93781.1)--(L-93781.3).

The aggregate proof-object digest is

```text
536e814f8f51bd8994c305f312f22fd9d4d2005cd1f7f9d8461393f0b30a0fe3
```

before the outer replay wrapper, and the complete wrapper digest is recorded
in `results/verification.json`.
