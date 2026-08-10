# Certified fragmentation resonance: GFEP and frozen BTF are false, uniform Pascal survives

Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Status: exact theorem/refutation packet plus directed interval certificate; RH unproved

## Executive result

The frozen half-binary/half-ternary first-entrance programme has a deterministic complex resonance which survives in both its bottom GFEP exit and its actual node-two producer coefficient. A directed interval certificate places one simple characteristic zero at

```text
u = 0.7422293980561885240...
   +17.3619424994722740597... i
```

inside a disk of radius `1e-18`, and proves nonzero trace numerators with margins

```text
|N_exit|     > 0.2815082855,
|N_producer| > 0.0895557448.
```

After the critical shift, the Mellin pole has real part greater than

```text
0.242229398056188523.
```

Landau plus a proved integer-interpolation estimate yields arbitrarily large positive and negative integer values of

```text
Sigma_(N,2)(2)
and
A_N(2).
```

Both signs exceed every fixed power `N^delta`, in the non-O sense, for every `delta<0.242229398056188523`.

Consequently:

```text
GFEP-full                                   REFUTED
frozen binary-ternary pointwise positivity REFUTED
frozen BTF absolute variation              REFUTED POLYNOMIALLY
signed pairing / Cycle Debt                NOT REFUTED
RH                                           UNPROVED
```

## Why this was invisible in the finite campaign

The source coefficients are positive Stieltjes packets and all nonempty multiplicative directions are proper descendants. Those facts are exact, but they concern the deformation cone around the current source. The empty Möbius coefficient retains the deterministic renewal denominator

```text
Delta(u)=1-1/2[2^(1-u)+3^(-u)+(3/2)^(-u)].
```

The resonance is a pole of the fragmentation transfer itself. Large finite positivity is therefore compatible with eventual sign oscillation: the first certified resonance has imaginary frequency about `17.36` and a relatively small power exponent about `0.2422`.

## Certificate architecture

`X-90204-certified-fragmentation-resonance` uses:

1. `mpmath.iv` at 70 decimal digits;
2. a Rouché disk certified from directed bounds on `Delta`, `Delta'`, and `Delta''`;
3. exact `Fraction` recurrence coefficients through `R=20000`;
4. directed complex interval evaluation of the finite numerator;
5. analytic shifted-difference tail bounds from the exact global increment bounds;
6. 39,998 exact trace-relation checks.

No zeta-value approximation, zero table, finite endpoint sign scan, PNT, or RH input appears in the certificate.

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

This has no deterministic nonreal poles. The uniform Pascal/SHARP route is therefore the canonical resonance-free fragmentation front.

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
S(e^t)=2H(e^t)+integral_0^t H(e^u) du.
```

Thus the low-row SHARP and critical-log routes are the same source under one positive Volterra smoothing. Full SHARP is far stronger than the RH consumer.

## Correct route selection

The live elementary programme should no longer target positivity or subpower absolute variation of the frozen binary-ternary flow. The remaining high-value fronts are:

1. the resonance-free uniform Pascal two-row scalar;
2. signed pairing or cycle-optimized debt, which can cancel deterministic policy modes;
3. the prime-endpoint positive-occupancy/mean-age criterion;
4. state-dependent or non-atomic fragmentation policies.

The immediate recommended attack is the first: preserve the exact two-row zero-safe cancellation and seek an ordered representation or one-sided theorem for that single scalar.
