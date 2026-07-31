# M-14303 — Exact adjacent-prolate source and lower-floor program

Claim ID: M-14303  
Title: Proof-producing program joining exact source repair, radical-tail duality, and the block lower floor  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: L-14308 through L-14313; T-14302 and T-14303  
Scope: positive RH route on stacked PR #152  
Related counterexample candidates: none

## Objective

The current lower-floor route is strongest when its low packet consists of
actual near-radical directions and its complement is certified by the full
Suzuki symbol rather than an absolute prime sum. The source audit changes the
first production packet: two modes are insufficient for exact global radical
membership, while three same-sign modes admit an exact algebraic repair.

The first production target is therefore

```text
included source modes:       h_0, h_4, h_8
first excluded same-sign:    h_12
```

with an explicit Schwartz source approximation and separately certified
source-to-Weil graph transport.

## Gate 1 — exact source algebra

For directed enclosures of

```text
v_j   = h_(4j,lambda)(0),
chi_j = concentration eigenvalue,
```

construct

```text
m_j = chi_j v_j,
a   = v cross m.
```

Fail closed unless:

- all `v_j` exclude zero;
- `1 >= chi_0 > chi_1 > chi_2 > 0` is directed and strict;
- the exact/directed coefficient vector is nonzero;
- both source constraints are verified after rational freezing;
- the normalized leakage upper bound is retained.

The two-mode target may remain as an empirical Xi-oriented comparison, but it
must not enter the radical-tail theorem without an independent `f(0)=0` gate.

## Gate 2 — explicit Schwartzification

Choose fixed rationally described even bumps inside `(-lambda,lambda)` and
construct a smooth compactly supported approximation to the three-mode packet.
Correct its integral by one bump supported away from zero. Retain directed
bounds for

```text
L2 source approximation,
Fourier leakage,
value and integral constraints,
support margin.
```

The correction is allowed to be polynomially small. The lower-floor route
needs the final Schur loss to vanish; it does not require preserving the full
exponential prolate rate.

## Gate 3 — source-to-form transport

Use `L-14313` to report the numerator as the exact weighted dual norm

```text
sup_{<k,v>=0, ||v||_W=1} |Q(t,v)|,
```

with

```text
t(u)=E(Fourier(f)-f)(u^-1),  u<lambda^-1.
```

No ordinary `L2 -> Weil graph` implication is accepted. The producer must
supply a directed continuity theorem for Suzuki's complete scalar,
prime-translation, and smooth-convolution form. Prime cancellation must be
preserved through the exact symbol from `L-14311`.

## Gate 4 — finite bad-symbol packet

For a chosen symbol floor, certify:

```text
bad-frequency set B_lambda,
measure |B_lambda|,
global lower symbol m_lambda,
outside lower symbol G_lambda,
concentration threshold eta.
```

Use `L-14311` to produce an explicit generalized-prolate rank cap. The low
packet must contain:

- the three source modes;
- every bad-symbol concentration mode above `eta`;
- any parity controls required by the finite matrix convention.

## Gate 5 — block Schur floor

Build directed blocks

```text
A = [[B,R*],[R,C]]
```

and certify the complement inequality `C-gamma I >= h M`. Apply `L-14308` to
obtain

```text
F_lambda
 = min(gamma,
       lambda_min(B-h^-1 R* M^-1 R))
   - complete assembly radius.
```

Retain separately:

```text
uncorrected low Ritz floor,
Schur residual loss,
complement floor,
assembly radius,
final F_lambda.
```

## Gate 6 — cofinal symbolic envelope

Finite positive levels are reconnaissance. The RH proof target is a symbolic
bound

```text
F_lambda >= -epsilon(lambda),
epsilon(lambda) -> 0
```

on an unbounded support sequence. `T-14302` then proves RH even when every
finite lower endpoint remains negative.

The alternative `T-14303` route may be run on the same source packet: projective
convergence of simple-even ground transforms to any nonzero zeta-factor target
also suffices.

## Exact checker

`X-14307` verifies the finite algebra independent of prolate numerics:

- exact three-mode cross-product source constraints;
- exact leakage identity and first-excluded-mode bound;
- exact global radical truncation identities;
- exact weighted projective quotient/dual equality.

The retained control returns

```text
coefficients                       (-3/5,3/5,-1/5)
normalized leakage squared         6/19
leakage bound squared              3/5
projective radical-tail squared    4/11
```

with eight adversarial tests.

## Scheduling metric

Rank supports by the tuple

```text
(bad-symbol measure,
 source-to-form residual / complement coercivity,
 Schur-corrected floor moat,
 proof radius,
 finite packet rank).
```

Do not rank by a tiny positive Ritz value alone. The same source packet should
be evaluated at several `lambda` values before increasing mode count, so one
can distinguish support asymptotics from finite-coordinate conditioning.

## Proof boundary

- No directed production prolate packet is yet available.
- The source-to-Weil graph continuity theorem is still missing.
- The bad-symbol construction and block floor remain proposed until source
  constants are independently audited.
- Neither a cofinal lower envelope nor a zeta-factor target sequence has been
  proved.
- RH is not claimed.
