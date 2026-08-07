# Balanced-core continuation toward a full RH proposal

## Outcome

The continuation did **not** prove RH. It substantially sharpened the remaining
proof boundary and adversarially audited the newest reflected Selberg proposal.

The current decisive result is:

```text
terminal/free-lattice sectors can be closed;
the all-truncated balanced Möbius sector cannot be removed by endpoint-face
counting and retains the full rightmost-zero exponent.
```

## 1. Complete-lattice closure

`L-23005` proves a deep-contour version of terminal Euler cancellation. Every row
containing one genuinely free, complete, macroscopically large integer lattice
can be shifted left after exact pole-moment cancellation. Such rows decay
exponentially relative to any fixed logarithmic reserve.

This composes with the higher-order Euler result `L-15160` and closes a larger
family than literal terminal Type-I rows.

## 2. Exact finite inverse boundary algebra

`L-23006` gives

```text
A_(K,V)=mu-mu*r_V^(*K),
r_V=epsilon-mu_V*1.
```

The first shell of `r_V` is exactly `mu` on `(V,2V]`; the first `K`-fold boundary
layer is therefore a `K`-fold Möbius shell tensor.

`L-23007` gives the corresponding Dirichlet-series statement:

```text
A_(K,V)(s)=(1-R_V(s)^K)/zeta(s),
E_(K,V)(s)=R_V(s)^K/zeta(s).
```

At every nontrivial zero, `R_V=1`, so the residual has the **same complete
principal part** as `1/zeta` for every finite order `K`. Adjacent-order
differences are reciprocal-free. Thus the finite inverse hierarchy consists of
one common meromorphic Möbius quotient plus a family of pole-free corrections.

`X-23001` verifies the finite convolution and formal Laurent algebra exactly.

## 3. Generic closure barriers

`R-23003` proves two no-free-lunch results.

1. A factorwise homogeneous norm estimate for a complete balanced product has
   tensor scale parameter at least one. Generic Cauchy, Young, and Schur
   inequalities do not strictly contract the logarithmic scale.
2. Making the window order grow with the block scale does not create a free
   factorial gain while retaining a fixed off-line-pole response. The support
   or normalization cost neutralizes it.

`R-23004` shows that finite cross-order polarization cancels only the pole-free
corrections. Any finite combination that still represents the Möbius source
retains the common `1/zeta` principal part.

## 4. Audit of the reflected Selberg proposal

The new PR #226 proposal supplies a useful exact-looking Hermitian Selberg square
and then claims that the sole remaining hinge is an absolute bound on the number
of free terminal endpoint coordinates.

`R-23005` shows that this is not the complete hinge.

For every order `K`, the exact fixed-logarithm Heath--Brown slice is

```text
constant * mu(m),  m<=V^K/q0.
```

After all complete free-lattice rows are exponentially removed, `R-15115`
proves that the residual all-truncated balanced packet retains the full
rightmost-zero exponent. The corrected packet theorem `L-23207` therefore keeps
`BTP(K)` explicitly open.

The terminal endpoint-face count, even if proved, does not estimate this
balanced packet.

The same audit catches an unsupported scalar mutation. The exact fixed-logarithm
source remains `mu` for every `K`; it does not automatically become
`Delta_(2/3)^K M`. Corrected `L-23202` explicitly exports no such packet map.
`X-23002` gives an exact finite regression:

```text
D=100
first cell / first difference     2
second geometric difference       0
third geometric difference       -3
```

while the order-`K` packet reconstructs `mu` with zero mismatches.

Consequently:

```text
L-9517 terminal count as sole hinge     rejected
T-9509 as a complete RH proof            gap/blocked
reflected Selberg Hermitian identity     retained after normalization audit
balanced Type-II theorem BTP(K)          open
```

`O-23003` records one local sign typo in `L-9516`: the generalized von Mangoldt
coefficient is `b*(a log)`, not its negative. The reflected subtraction and
Hermitian square remain correctly oriented after this repair, but the critical
finite-packet continuation must still be written explicitly.

## 5. Exact surviving proof target

A repaired reflected proposal must prove a source-specific recurrence for every
balanced packet,

```text
E_(K,tau)(J)
 <= exp((epsilon_K+o_K(1))J)
    [1+max_(u<=(1-delta)J+O_K(1)) M_K(u)],
epsilon_K -> 0,
```

or a tensor recurrence with

```text
epsilon_K/(1-kappa_K) -> 0.
```

It must also export a genuine source map to the first-cell scalar

```text
M(D)-M(floor(2D/3)).
```

The map may target a higher geometric difference only if the actual cutoff
finite-difference operator, floors, endpoints, and inverse formula are included.

## 6. Status

```text
free unrestricted lattice rows          PROPOSED CLOSED
terminal Type-I rows                     PROPOSED CLOSED
finite inverse boundary tensor           EXACTLY IDENTIFIED
common 1/zeta principal part             EXACTLY IDENTIFIED
factorwise tensor closure                REFUTED AS NONCONTRACTING
finite cross-order pole cancellation     REFUTED FOR THE MOBIUS QUOTIENT
reflected Hermitian Selberg algebra       RETAINED WITH A SIGN FIX
terminal endpoint count as sole hinge    REFUTED
balanced source-specific BTP(K)          OPEN
first-cell packet decoder                OPEN
RH                                       NOT PROVED
```
