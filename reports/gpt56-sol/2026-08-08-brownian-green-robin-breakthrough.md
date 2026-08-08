# Brownian Green–Robin breakthrough report

Agent: `gpt56-sol`  
Date: 2026-08-08  
Branch: `agent/gpt56-sol/217-brownian-norlund-real-zero`  
Status: **full global proposal; one finite real-zero theorem open; RH unproved**

## Executive result

The Brownian approximation programme has moved from an empirically stable logarithmic average to two exact positive structures.

1. **Green/occupation identity.** Every positive mixture of finite gamma cutoffs has one cardinal Green profile `G_lambda`. Its finite Dirichlet factor is exactly
   
   ```text
   2(s-1) zeta(s)
   -2 pi sin(pi s/2) Mellin[A_lambda](s),
   ```
   
   where `A_lambda>=0`, and `A_lambda(sqrt(q))` is the Laplace transform of the actual Brownian tail-occupation measure between `S_K` and `S_infinity`.

2. **Robin-fiber identity.** Every symmetrized approximant is exactly
   
   ```text
   integral W(a)[cosh(a z)+2z sinh(a z)] da,
   s=1/2+z,
   W(a)>0.
   ```
   
   Positive logarithmic lengths `a>0` are self-adjoint Robin determinants and have only critical-line zeros. Negative lengths have exactly one reflected off-line pair. The finite theorem is therefore a global no-double-spend transport or Schur complement between explicitly favorable and unfavorable Sturm fibers.

These identities apply independently of the Riemann hypothesis and expose why positivity of the truncation defect alone cannot close the route: the raw cutoffs have the same positive occupation structure and nevertheless exhibit off-line finite pairs.

## Canonical central-binomial producer

Put

```text
omega_K=[binom(2K,K)/4^K]^2,
lambda_(N,K)=omega_K/sum_(J<=N)omega_J.
```

Then the complete Green profile is

```text
G_N(z)=Z_N^-1 sum_(K<=N) p_K(z)^2,

p_K(z)=Gamma(2K+1)/[4^K Gamma(K+1-z)Gamma(K+1+z)].
```

For integer `n`, `p_K(n)` is a simple-random-walk transition probability. Thus `G_N` is a normalized truncated diagonal Green profile for two independent walks.

The exact coefficient collapse is

```text
D_N(s)=2 sum_(n<=N)[(s-1)G_N(n)-nG_N'(n)]n^-s.
```

The elementary recurrence for `omega_K` gives

```text
omega_K>=1/(4K),
Z_N>=H_N/4,
```

and therefore local uniform convergence

```text
|C_N(s)-4xi(s)|
 <=4 zeta(2) H_N^-1 (|s|+|1-s|)
```

on the critical strip.

## Exact Brownian occupation theorem

For a general positive cutoff mixture,

```text
A_lambda(y)=[G_lambda(iy)-1]/sinh^2(pi y)>=0.
```

If the finite and infinite sums use the same gamma sequence, then

```text
pi^2 A_lambda(sqrt(q))
 = integral exp(-q x)b_lambda(x)dx,

b_lambda(x)
 =sum_K lambda_K P(S_K<=x<S_infinity)>=0.
```

Consequently

```text
2xi(s)-m_lambda(s)
 =(s/2)pi^(-s/2)
  integral b_lambda(x)x^(s/2-1)dx.
```

This is an exact physical interpretation of the finite approximation error, not an asymptotic expansion.

## Exact Robin split

For the tail `T(x)=P(S>x)`, put

```text
W(a)=exp(a/2)T(pi exp(2a)),
H_a(z)=cosh(az)+2z sinh(az).
```

Then

```text
C(1/2+z)=integral_R W(a)H_a(z)da.
```

The single-fiber verdict is binary:

```text
a>0: H_a is a nonnegative self-adjoint Robin determinant;
     every zero is on the imaginary z axis.

a<0: H_a has exactly one real reflected pair;
     2z tanh(|a|z)=1.
```

Equal reflected lengths can be paired sharply:

```text
u H_a+v H_(-a) has only imaginary zeros iff u>=v.
```

The continuous mixture still needs a common-interlacing, canonical-system, Lee–Yang, or Schur theorem. Pairing each unfavorable fiber independently would double-spend favorable mass and is invalid.

## Exact replay

`X-21704` verifies with integer/Fraction arithmetic:

```text
coefficient rows             408
normalization rows            48
finite-product order rows    680
Wallis rows                  512
mutations                    4/4

PASS_EXACT_BROWNIAN_GREEN_DEFECT_ALGEBRA
65442b5fb1ff09e06c7f237102cc289bb9c28f6d33f1b12cea7f54d0670277d7
```

The contour identity and Sturm theorem remain human analytic review obligations; the checker certifies neither zeros nor RH.

## Reconnaissance

The central-binomial producer has matching strip-winding and critical-line counts through height `5000`:

```text
N=100      4520 / 4520
N=500      4520 / 4520
N=1000     4520 / 4520
```

These binary64 scans are discovery only.

## Correct sole theorem

The preferred hinge is now `BGRRZ`:

```text
for an unbounded sequence N_j,
every zero of C_(N_j) in 0<Re(s)<1
lies on Re(s)=1/2.
```

A proof must construct one source-complete global Sturm/canonical-system or Lee–Yang certificate. The exact Green and Robin identities sharply restrict what that object must do.

`BGRRZ` plus local uniform convergence gives RH by Rouché. No prime-ramp, Mertens, WSTS, balanced Type-II, Weil-positivity, or square-screw estimate enters this composition.

## Honest boundary

```text
finite Brownian construction          proposed complete
Green coefficient collapse            proposed complete + exact replay
positive occupation defect            proposed complete
Robin-fiber localization              proposed complete
central-binomial convergence          proposed complete
BGRRZ                                 OPEN / RH-bearing
Riemann Hypothesis                     UNPROVED
```
