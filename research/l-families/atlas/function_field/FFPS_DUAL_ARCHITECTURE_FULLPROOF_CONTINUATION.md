# Dual-architecture full-proof continuation after PR #760 head 5122e939

Status: **three exact new reductions; the remaining Architecture A estimate
and Architecture B one-place trace theorem are open; RH and GRH remain
unproved**

Frozen remote head:
`5122e939df2fa322b5a3185cf1d78d4b402f3d5f` on draft PR #760.

This continuation keeps the two routes separate.

## Architecture A: the exact remaining analytic shape

The current branch already reduces RH conditionally to the high, balanced, far-shift
shared-gcd wavelet gate `HIGHFARGCDWAVE`.  The two new packets

- [`FFPS_DIVISOR_WAVE_WITT_ZETA_TOWER.md`](FFPS_DIVISOR_WAVE_WITT_ZETA_TOWER.md),
- [`FFPS_GCD_WAVE_MODE_DECOUPLING.md`](FFPS_GCD_WAVE_MODE_DECOUPLING.md),

prove the following exact facts for the untruncated multiplicative modes.

First, each one-variable divisor mode has a complete free-Lie/Witt factorization

\[
 F_\xi(s)
 =\prod_{n\ge1}\prod_{a+b=n}
 \zeta^{(67)}(ns-i(a-b)\xi)^{-\ell_{a,b}},
\]

with an arbitrary finite truncation whose residual Euler product is normal for
`Re(s)>1/(R+1)`.  The first hidden factor beyond the two shifted degree-one
terms is `1/zeta^(67)(2s)`.

Second, the common-gcd two-frequency mode satisfies

\[
 \mathcal G_{\xi,\eta}(s,t)
 =\mathcal H_{\xi,\eta}(s,t)F_\xi(s)F_\eta(t),
\]

where the coupling product `H` is normally convergent and nonzero after a
fixed finite-prime deletion on the critical product half-plane
`Re(s),Re(t)>=1/2`.  Thus the unsigned common gcd contributes no new critical
Euler obstruction.

The remaining Architecture A gate is now exactly the **high/far sharp
hyperbola and dyadic endpoint assembly** of two one-variable Witt-zeta modes.  A proof must
retain the balanced divisor truncation, Fourier/Perron shifts, and the
assembled signed block sum.  Neither packet bounds reciprocal zeta near a
hypothetical zero.

## Architecture B: finite bivariate algebra is externalized

The packet
[`FFPS_RELATIVE_TRACE_TENSOR_CLOSURE.md`](FFPS_RELATIVE_TRACE_TENSOR_CLOSURE.md)
proves two exact trace-level statements.

1. The all-`k` centered cyclic identity survives every common source
   restriction and the final signed outer recombination.  This is
   `TRACE-NATREL`.
2. The coprime family square and literal Wick diagonal are finite signed sums
   of one-sided tensor products, with horizon-independent outer costs at most
   `zeta(2)^2` and `zeta(4)` respectively.  This is
   `COPRIME-WICK-EXT`.

Together with the predecessor's one-sided phase externalization, this removes
the explicit bivariate phase, coprimality, and Wick-algebra obstruction.  It
does not construct a complete Weil complex.  The remaining Architecture B
stack is

```text
ONEPLACEWEIL
  complete one-sided source amplitudes descend uniformly to fixed
  closed-point spaces

ONEPLACETRACE / RELTRACE
  uniform compactly-supported trace control for every Adams row, retaining
  the signed conductor recombination

PRINCIPAL-BINDING
  the extracted trace is the exact native principal moment

FROZEN PRINCIPAL CONSUMER
  -> RH.
```

## Exact scientific boundary

The continuation proves neither decisive open input:

- no sharp hyperbola/Witt-mode estimate in Architecture A;
- no one-place Weil descent or uniform trace theorem in Architecture B.

Accordingly **RH and GRH remain unproved**.  The gain is that both routes now
have smaller and more explicit first open arrows, with several previously
coupled interfaces removed exactly rather than assumed away.
