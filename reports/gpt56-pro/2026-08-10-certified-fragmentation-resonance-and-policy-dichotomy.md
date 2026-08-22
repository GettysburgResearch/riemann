# Certified near-conservation fragmentation resonance: GFEP and frozen BTF are false, uniform Pascal survives

Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Status: exact theorem/refutation packet plus directed interval certificate; RH unproved

## Executive result

The frozen half-binary/half-ternary first-entrance programme has a deterministic complex resonance which survives in both its bottom GFEP exit and its actual node-two producer coefficient. A directed interval certificate places one simple characteristic zero at

```text
u = 0.9965737487663334042655023867051966592...
   +108.6843160063763813085769124318175668569... i
```

inside a disk of radius `1e-18`, and proves nonzero trace numerators with margins

```text
|N_exit|     > 0.00987978337,
|N_producer| > 0.00199031875.
```

After the critical shift, the Mellin pole has real part greater than

```text
0.496573748766333403.
```

Landau plus a proved integer-interpolation theorem yields arbitrarily large positive and negative integer values of

```text
Sigma_(N,2)(2)
and
A_N(2).
```

More strongly, both positive and negative parts are not `O(N^delta)` for every fixed

```text
delta < 0.496573748766333403.
```

Consequently:

```text
GFEP-full                                   REFUTED
frozen binary-ternary pointwise positivity REFUTED
frozen BTF absolute variation              REFUTED NEAR SQUARE-ROOT SCALE
signed pairing / Cycle Debt                NOT REFUTED
RH                                           UNPROVED
```

## Why this was invisible in the finite campaign

The source coefficients are positive Stieltjes packets and all nonempty multiplicative directions are proper descendants. Those facts are exact, but they concern the deformation cone around the current source. The empty Möbius coefficient retains the deterministic renewal denominator

```text
Delta(u)=1-1/2[2^(1-u)+3^(-u)+(3/2)^(-u)].
```

The resonance is a pole of the fragmentation transfer itself. Large finite positivity is compatible with eventual sign oscillation because the certified residue is small and the first near-conservation frequency used here is high, about `108.68`. The exponent lies only about `0.00342625` below the square-root line.

## Certificate architecture

`X-90204-certified-fragmentation-resonance` uses:

1. `mpmath.iv` at 70 decimal digits;
2. a radius-`1e-18` Rouché disk certified from directed bounds on `Delta`, `Delta'`, and `Delta''`;
3. exact `Fraction` recurrence coefficients through `R=20000`;
4. directed complex interval evaluation of the finite numerator;
5. analytic shifted-difference tail bounds from the exact global increment bounds;
6. 39,998 exact trace-relation checks.

No zeta-value approximation, zeta-zero table, finite endpoint sign scan, PNT, or RH input appears in the certificate.

## Exact fixed-trace relation

For the two `n=2` exit traces,

```text
G_2(m)+G_3(m)=m.
```

The sparse producer trace is

```text
G_P=G_2+(2/3)G_3.
```

The total trace `G(m)=m` has no nonconservation characteristic pole. Hence at every characteristic zero `u!=1`,

```text
N_P(u)=N_2(u)/3.
```

The verifier nevertheless evaluates both numerators independently as a mutation-sensitive check.

## General policy theorem

The resonance is not an accident of the ratios `1/2,1/3,2/3`. Every stationary policy supported on finitely many fixed child ratios has characteristic

```text
Delta_nu(u)=1-sum_j b_j v_j^u,
sum_j b_j v_j=1,
```

and simultaneous Diophantine approximation forces characteristic zeros with real parts tending to the conservation line. Thus no finite atomic stationary fragmentation has a source-independent spectral gap.

The answer changes for non-atomic policies. The uniform continuum split has

```text
Delta_unif(u)=(u-1)/(u+1),
```

with only the conservation zero. Its exact discrete analogue, the uniform internal Pascal chain, has hitting law

```text
h_n(n)=1,
h_n(m)=2/(n+1),  m>n,
```

and deterministic transfer

```text
A_n(u)=n^(1-u)+(2-n)(n+1)^(-u)+2/(n+1) zeta(u,n+2).
```

This has no deterministic nonreal poles. The uniform Pascal/SHARP route is therefore the canonical resonance-free stationary fragmentation front.

## Two-row compression

For the critical-log average-carry inverse, the two-row scalar

```text
S(X)=5c_X(2)+3c_X(3)
```

has transform

```text
S_hat(s)
 =6/s^2
 -3(1-2^(-u))(2-2^(-u))/(s^2 zeta(u)),
u=s+1/2.
```

It is exactly the zero-safe source

```text
omega=(epsilon-delta_2)*(2epsilon-delta_2)*mu
```

already present in the two-low-row SHARP theorem. If `H(T)` denotes the corresponding square-root-hinge scalar, then in logarithmic time

```text
S(e^t)=2H(e^t)+integral_0^t H(e^u)du.
```

Thus the low-row SHARP and critical-log routes are the same source under one positive Volterra smoothing. Full SHARP is far stronger than the actual RH consumer.

## Correct route selection

The live elementary programme should no longer target positivity or subpower absolute variation of the frozen binary-ternary flow. The remaining high-value fronts are:

1. the resonance-free uniform Pascal two-row scalar;
2. signed pairing or cycle-optimized debt, which can cancel deterministic policy modes;
3. the prime-endpoint positive-occupancy/mean-age criterion;
4. state-dependent or non-atomic fragmentation policies.

The immediate recommended attack is the first: preserve the exact two-row zero-safe cancellation and seek an ordered representation or one-sided theorem for that single scalar.
