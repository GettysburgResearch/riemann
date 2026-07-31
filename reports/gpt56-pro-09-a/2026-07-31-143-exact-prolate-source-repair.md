# Positive-path source audit: exact three-mode radical repair and zeta-factor closure

Agent: `gpt56-pro-09-a`  
Date: 2026-07-31  
Issue: #143  
Stack: PR #152 over PR #150  
Disposition: source-space gap confirmed; exact algebraic and smooth repair supplied

## Executive result

The lower-floor continuation correctly identified radical-tail transport as a
promising way to charge the prolate defect quadratically. Its application to
the CCM two-mode target, however, required a source-space audit.

The audit found:

1. the global arithmetic radical source space requires **two** conditions,
   `f(0)=0` and `integral f=0`;
2. CCM equation (7.6) imposes only vanishing integral on its two-mode finite
   prolate combination;
3. because `integral p_j=chi_j p_j(0)` and the two finite `chi_j` are distinct,
   no nonzero two-mode combination can satisfy both conditions;
4. three same-sign prolate modes give an exact cross-product repair;
5. zero extension of a prolate mode is not automatically Schwartz, so a second
   regularity gate remained;
6. constraint-preserving `C_c^infinity` approximation repairs that gate with
   arbitrarily small `L2` cost and at most twice that cost in Fourier leakage.

Thus the first honest exact source packet is based on

```text
h_0, h_4, h_8,
```

with `h_12` as the first excluded same-sign comparison mode.

## Source reconstruction

The 2023 Connes--Consani paper defines `S_0^ev` as real even Schwartz
functions satisfying

```text
f(0)=0,
integral f=0,
```

and states the radical map and Poisson identity

```text
E(f)(u)=sqrt(u) sum_(n>=1) f(nu),
E(Fourier f)(u)=E(f)(u^-1).
```

The same paper's original prolate construction explicitly forms combinations
that vanish at zero before applying `E`. The 2025 CCM outlook instead chooses
a combination of `h_(0,lambda)` and `h_(4,lambda)` with vanishing integral and
uses it as an educated approximation to the ground eigenfunction. The latter
is sufficient for its Xi-convergence lemma but not, without another argument,
for exact global radical membership.

## L-14312

For three orthonormal supported modes with

```text
P_lambda Fourier(p_j)=chi_j p_j,
v_j=p_j(0),
m_j=chi_j v_j,
```

set `a=v cross m`. Then `a dot v=a dot m=0`, while

```text
||Fourier(p)-p||_2^2
 = 2 sum a_j^2(1-chi_j)/sum a_j^2
 <= 2(1-chi_2).
```

The two-mode determinant is `v_j v_k(chi_k-chi_j)`, proving that dimension
three is minimal for distinct finite concentration eigenvalues.

For every epsilon, the normalized packet can be approximated by an even
`C_c^infinity(-lambda,lambda)` function with both constraints exact. One bump
away from zero repairs the integral, and Fourier unitarity gives only a
`2 epsilon` additional leakage charge. This produces a legitimate exact
`S_0^ev` source.

## L-14313

For a radical split `r=k+t`, the weighted projective numerator is exactly

```text
inf_c ||(A-mu I)k-c k||_(W^-1)
 = sup_(<k,v>=0, ||v||_W=1) |Q(t,v)|.
```

For the compact exact source, Poisson gives the exterior tail itself:

```text
t(u)=E(Fourier(f)-f)(u^-1),  0<u<lambda^-1,
t(u)=0,                       u>lambda.
```

This removes any ambiguity about what the numerator measures. It also shows
precisely why ordinary `L2` leakage is not the final theorem: a named
source-to-Weil graph/form continuity estimate is still required.

## T-14303

The Xi-specific target is stronger than necessary. If entire finite functions
with only real zeros converge on the centered critical strip to

```text
zeta(1/2-i z) Phi(z),
```

with `Phi` holomorphic and not identically zero, Hurwitz already implies RH.
A holomorphic multiplier cannot cancel a zeta zero. Thus any fixed-dimensional
exact prolate source subspace with a nonzero subsequential Mellin factor is a
valid positive target; identifying the factor with Riemann's special Hermite
completion is unnecessary.

## Exact regression

`X-14307` is a standard-library-only checker. The retained object proves
exactly

```text
three-mode coefficients              (-3/5,3/5,-1/5)
normalized Fourier leakage squared    6/19
first-excluded bound squared          3/5
weighted projective tail squared      4/11
```

Eight adversarial tests pass and all six SHA ledger rows verify.

## Remaining theorem

The strongest path remains the block lower floor of PR #152. Its sharp missing
estimate is now correctly stated as

```text
exact source Fourier leakage
   -> exact Weil radical-tail cross-form norm
   -> Schur residual loss below first-excluded coercivity,
```

with prime cancellation preserved through the full localized symbol. A cofinal
bound `F_lambda >= -epsilon(lambda)`, `epsilon(lambda)->0`, would invoke
`T-14302` and prove RH. No such bound is claimed here.
