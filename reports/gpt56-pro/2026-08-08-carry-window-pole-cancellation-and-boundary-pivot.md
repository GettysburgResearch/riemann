# Carry-window pole cancellation and the corrected final boundary theorem

Date: 2026-08-08  
Branch: `agent/gpt56-pro-262-dyadic-two-contact`  
PR: #269  
Status: **exact scope correction; boundary-commutator theorem open; RH unproved**

## Why this addendum was necessary

The source/carry consolidation produced a large body of exact algebra:

```text
fixed-q0=2 physical source
-> omega_2 opposite-parity source
-> pointwise compact carry wavelet
-> factor-five localization
-> positive inverse and generalized primes
-> uniform carry-space reserve
-> exact Selberg-carry moment tower.
```

The remaining proposal initially asked for a bounded same-scale map from the independent-frequency physical normal block to the carry Gram. A final transform audit shows that this direct bulk bridge cannot preserve the RH pole.

## Exact carry-window transform

For `0<theta<1`, let

```text
C(x,theta)=floor(x)-floor(theta x)-floor((1-theta)x)
```

and

```text
H_theta(u)=exp(-u/2) C(exp u,theta).
```

For `sigma=z+1/2`, the exact transform is

```text
Hhat_theta(z)
 =zeta(sigma)/sigma
  [1-theta^sigma-(1-theta)^sigma].
```

Thus every atomized carry analysis window contains the full factor `zeta(sigma)` and vanishes at every nontrivial zeta zero.

The generalized-prime signal for

```text
Omega_2(sigma)=E(sigma)/zeta(sigma),
E(sigma)=(1-2^-sigma)(1-2^(-sigma-1)),
```

has logarithmic derivative

```text
-zeta'/zeta+E'/E.
```

Multiplying by `Hhat_theta` gives

```text
B_theta(sigma)/sigma
[-zeta'(sigma)+zeta(sigma)E'(sigma)/E(sigma)],
```

which is holomorphic at every nontrivial zeta zero. The pole has canceled.

Likewise the compact opposite-parity carry wavelet has transform

```text
E(sigma) B_theta(sigma)/sigma,
```

with no zeta factor left at all.

## Exact consequence

The following shortcut is rejected:

```text
uniform same-scale carry Gram estimate
-> RH-sensitive same-scale physical estimate.
```

A hypothetical off-line zero is a common null frequency of the pure carry-window bank. Carry-space coercivity cannot, on its own, exclude that zero.

This does not refute the carry identities or reserves. It reassigns their role:

```text
carry sector:
    controls the pole-canceling transverse factor-five transition;

physical boundary/commutator sector:
    must retain the inverse-zeta pole and produce the lower-scale recurrence.
```

## Corrected final theorem

The remaining object is now the **Boundary-Commutator Factor-Five Transition Certificate (`BCF5TC`)**.

It must emit an exact source decomposition

```text
I=P+B,
```

where:

- `P` is the direct carry-window sector and may be compared to the carry Gram;
- `B` is the independent-frequency physical boundary/commutator retaining the `m=1` source, bottom charges, parity/Bezout endpoints, and fixed-ratio Mertens cell.

The producer must prove:

1. a bounded transverse physical-to-carry map on `P`;
2. preservation of the uniform carry reserve on that transverse sector;
3. an independent physical Schur reserve on `B` before the carry zeta factor is introduced;
4. an explicit lower-scale recurrence for the physical boundary energy, bottom charge, DSS scalar, or fixed-ratio shell.

## Relationship to the moment tower

`L-26904` gives

```text
sum_m a_omega(m)Z_m=0,
sum_m a_omega(m)log(m)Z_m>=0,
sum_m a_omega(m)log(m)^2Z_m>=0.
```

The unit source `m=1` is absent from the two positive logarithmic moments. This is not an accident: it is exactly the RH-bearing boundary coordinate canceled by the pure carry windows.

The moment tower therefore supplies both:

- a positive transverse source ledger;
- an exact warning that the boundary cannot be absorbed into it.

## Consolidated review front door

Review in this order:

```text
1. T-26903 boundary-commutator conditional theorem
2. M-26903 production/review protocol
3. R-26902 carry-window pole-cancellation refutation
4. L-26904 moment tower and boundary firewall
5. L-26901--L-26903 factor-five source/carry package
6. PR #263 parity-paired physical source frame
7. PR #241 independent-frequency physical block
8. future concrete BCF5TC matrices and recurrence
```

## Final status

```text
source/filter/carry algebra             proposed complete
factor-five localization                proposed complete
carry-space reserve                     proposed complete
moment tower and boundary firewall      proposed complete
direct bulk physical/carry shortcut     refuted
boundary/transverse decomposition       open
boundary physical Schur reserve         open
lower-scale boundary recurrence         open
conditional BCF5TC -> RH                proposed complete
Riemann Hypothesis                      unproved
```

The consolidation is ready for adversarial review. It is not an unconditional proof of RH.
