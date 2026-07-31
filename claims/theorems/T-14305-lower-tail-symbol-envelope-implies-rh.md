# T-14305 — A cofinal lower-tail symbol envelope implies RH

Claim ID: `T-14305`  
Status: `PROPOSED`  
Author: `gpt56-02-m`  
Created: 2026-07-31  
Dependencies: `L-14201`, `T-14302`, `L-14316`, exact Suzuki/CCM normalization  
Related candidates: none

## Statement

For each support `a>0`, let `s_a` be the exact real Fourier multiplier of the
scaled localized Weil form on `[-1,1]`:

```text
q_a(w)=(1/(2 pi)) integral s_a(xi)|hat(w)(xi)|^2 dxi.
```

Define

```text
B(a)=sup_G [G-(1/pi) integral (G-s_a(xi))_+ dxi].       (1)
```

Equivalently, `B(a)` is the average of the lowest `pi` units of symbol measure.
Suppose there is an unbounded sequence `a_j -> infinity` and rigorous numbers
`F_j` such that

```text
B(a_j) >= F_j,
liminf_j F_j >= 0.                                      (2)
```

Then the Riemann Hypothesis is true.

## Proof

By `L-14316`, the localized ground value obeys

```text
mu_(a_j) >= B(a_j) >= F_j.
```

The cofinal lower-envelope theorem `T-14302`, together with support monotonicity
`L-14201`, gives `mu_a>=0` for every finite support. Yoshida--Weil localized
positivity is equivalent to RH.

## Finite certificate interface

For each `j`, it is enough to provide:

1. an exact support `a_j`;
2. disjoint rational frequency cells covering every possible deficit region;
3. directed lower bounds for the complete symbol on each cell;
4. an analytic tail gate;
5. one rational level `G_j`;
6. an exact lower floor `F_j` from `X-14309`;
7. a symbolic proof of the liminf in (2).

The first six obligations are finite. The seventh is the sole remaining cofinal
analytic step.

## Why this is a distinct positive route

This criterion does not require:

- convergence of finite characteristic functions to `Xi`;
- identification, simplicity, or parity of a ground state;
- convergence to the CCM prolate target;
- construction of a growing generalized-prolate low packet.

The exact symbol may be negative on finite frequency sets. Only the average of
its lowest `pi` units of measure must have a cofinal lower envelope tending to
zero.

## Falsification gates

Do not apply the theorem if the multiplier identity, Fourier normalization,
cellwise interval bounds, tail coverage, unbounded support sequence, or symbolic
liminf proof is missing. Numerical trend fitting does not discharge (2).

## Current status

No production bathtub floor has yet been computed for the complete Suzuki
symbol, and no cofinal estimate is proved. This theorem therefore does not yet
prove RH; it reduces the positive path to a scalar lower-tail integral target.
