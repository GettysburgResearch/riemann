# Integration addendum — full physical-input Hardy delay colligation

## Freeze

```text
parent PR:      #400
child PR:       #429
base child SHA: 80ba1f2958ab6e561dc5e91430ffd21c05d02f11
session date:   2026-08-13
RH:             unproved
```

## Advance

`L-91322` gave the exact resident/leakage dilation for inputs already in a
Suzuki model space. `L-91323` removes that input restriction.

Every positive-Hardy physical input has canonical coordinates

```text
F = g + Theta q,
```

and every raw delay has the exact three-channel output

```text
model:     T_tau g + B_tau q;
amplitude: S_tau* q;
leakage:   L_tau^K g + L_tau^Theta q,
```

where

```text
B_tau = S_tau* M_Theta - M_Theta S_tau*
```

is the amplitude-to-model forcing commutator. The full polarized packet norm
is the sum of the three channel norms, so every cross-carrier and cross-delay
entry is retained exactly.

For the rational Cauchy mother, the base model coordinate is explicit from the
standard model-kernel projections at

```text
x+i a, x+2 i a, x+4 i a,
```

including first derivatives of `Theta_a` for the double poles. The resident
delayed physical vector is

```text
r_(a,x,tau) = T_tau g_(a,x) + B_tau q_(a,x).
```

## Exact regression

```text
experiments/X-91323-full-hardy-delay-colligation/
PASS_FULL_HARDY_DELAY_COLLIGATION
```

The retained verifier uses Gaussian-integer arithmetic and no floating point.
It checks:

```text
50  explicit block formulas;
25  pairwise three-channel cross-Gram identities;
245 upper-triangular state semigroup identities;
245 leakage cocycle identities;
1   nonzero amplitude-to-model forcing example;
1   five-input full packet Pythagorean identity.
```

The packet certificate is

```text
27200 = 16584 + 5388 + 5228.
```

## Correct boundary

```text
physical positive-Hardy input coordinates          PROVED
arbitrary physical-delay bookkeeping               PROVED
full physical cross-delay L2 Gram                   PROVED
Fisher-Hankel domain membership                     OPEN
completed Jordan+gamma+pole domination             OPEN / RH-BEARING
mixed orientation and bridge arithmetic block      OPEN
Riemann Hypothesis                                  UNPROVED
```

This is a geometric and operator-theoretic advance. It is not the remaining
arithmetic positivity theorem and must not be presented as a proof of RH.
