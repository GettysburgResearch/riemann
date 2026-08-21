# Reflected Selberg–Möbius full RH proposal

Date: 2026-08-07  
Agent: `gpt56-08`  
Branch: `agent/gpt56-08/9512-critical-energy-exponent`

## Executive result

This continuation supplies a full proposed proof architecture for RH. It is not
represented as independently verified. The exact new ingredient is a reflected
Selberg coefficient identity that produces the Hermitian vertical square
required by the prime-Hardy route:

\[
2\,\Lambda_t*\Lambda_{-t}
=C_\times-C_t-C_{-t},
\]

and therefore, on a real vertical line,

\[
2\left|\frac{\zeta'}{\zeta}(\sigma+it)\right|^2
=\mathcal C_\times(\sigma,t)-\mathcal C_+(\sigma,t)-\mathcal C_-(\sigma,t).
\]

This resolves the structural mismatch between the analytic Selberg square
`H(z)^2` and the Hermitian Hardy energy `|H(z)|^2`.

## Proposed completion

The reflected forcing is expanded by the exact finite Möbius resolvent in both
inverse-zeta variables. The high-order safe window supplies a null quotient
through degree `K`, while the fixed-reserve first-crossing partition and finite
complexity induction route every nonterminal row to lower scale.

The new closing proposal is that after exact signed terminal recombination,
every surviving same-scale endpoint face has at most an absolute number `C_*`
of free divisor coordinates. Since the Möbius cutoff is

\[
V=\lceil X^{1/K}\rceil,
\]

this produces the terminal exponent

\[
\eta_K\le C_*/K.
\]

The existing scale-contraction theorem then gives

\[
2\Theta_\zeta\le\frac{C_*}{K\delta}
\]

for every sufficiently large fixed `K`; sending `K` to infinity yields
`Theta_zeta=0`, hence RH.

## Independent scalar mutation

The `q_0=2` fixed-logarithm slice reduces the proposed terminal estimate to

\[
G_K(D)=\Delta_{2/3}^{K}M(D)
=O_{K,\varepsilon}
\left(D^{1/2+C_*/(2K)+\varepsilon}\right).
\]

The exact finite inversion of the geometric difference gives the same exponent
for `M(D)`. Choosing fixed `K` after a requested `epsilon` recovers

\[
M(D)=O_\varepsilon(D^{1/2+\varepsilon}),
\]

the classical Mertens criterion. This mutation prevents the packet machinery
from silently deleting the coherent first Farey cell.

## Exact regression

`X-9514` verifies the reflected Selberg coefficient identity through `n=30`
over a formal Laurent-polynomial ring, using one variable per prime and a
completely additive integer derivation in place of `log(n)`.

```text
PASS_EXACT_L9516_REFLECTED_SELBERG_IDENTITY
proof-object SHA-256
807779c2d1debb67eeb2d971dd244930e5296f3fc014f8197dee43645cc9d94f
```

This is exact finite algebra only; it does not verify the terminal enumeration.

## Decisive review hinge

The proof proposal stands or falls on the claim

\[
\#\{\text{free endpoint divisor coordinates on every recombined terminal face}\}
\le C_*
\]

with `C_*` independent of `K`.

An adversarial review should attempt to exhibit a terminal face with
`Omega(K)` free endpoint coordinates. Such a face would destroy the vanishing
`C_*/K` exponent. The review must also confirm:

1. every interior row belongs to the declared high-order null quotient;
2. every same-scale nonnull row lowers residual-word complexity;
3. all transition surfaces and cutoff faces are declared;
4. reflected cross terms are consumed by the exact Hermitian Selberg identity;
5. the first-cell Mertens mutation reproduces the proposed exponent.

## Review order

1. `claims/lemmas/L-9516-reflected-selberg-vertical-energy-identity.md`
2. `experiments/X-9514-reflected-selberg/verify.py`
3. `claims/lemmas/L-9517-reflected-mobius-terminal-contraction.md`
4. `claims/theorems/T-9509-reflected-selberg-mobius-full-rh-proposal.md`
5. `L-23201`--`L-23204` from PR #233
6. `L-15155`--`L-15159` and the fixed-reserve/complexity dictionaries
7. `L-23003/T-23002` first-cell decoder and fixed-ratio Mertens equivalence
8. the exact endpoint-face enumeration requested above

## Status

```text
reflected Hermitian Selberg identity     PROPOSED EXACT + finite replay
finite double Möbius resolvent           PROPOSED EXACT / imported
packet reduction and fixed reserve       PROPOSED EXACT / imported
terminal endpoint-count theorem          PROPOSED NEW HINGE
conditional deduction to RH              COMPLETE
RH independently verified                NO
```
