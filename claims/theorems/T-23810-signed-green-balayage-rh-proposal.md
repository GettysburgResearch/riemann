# T-23810 — Signed Green–balayage carry proposal for RH

Claim ID: `T-23810`  
Title: A polylogarithmic signed quotient-layer barrier for the canonical carry scalar forces the Riemann hypothesis  
Status: **FULL PROPOSED PROOF — `SGQB(K)` IS THE SINGLE NEW RH-BEARING HINGE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: exact carry/divisor-gradient and parabolic-seed files on PR #248; `L-23820/L-23821`; proposed `L-23822`; square-screw/rightmost-zero transfer on PR #202  
Supersedes: the source-coordinate two-contact closure of `L-23806/T-23803`  
Scope: source-specific scalar carry route; RH is not claimed independently verified

## 1. Exact prime-ramp front door

Let

\[
P_X
=\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp
\tag{T-23810.1}
\]

be the ordinary-prime ramp. The proper-prime-power tail is `O(log^2 X)`, so the
complete von-Mangoldt ramp differs from `P_X` by only that amount.

Use the explicit parabolic carry seed `b_X^(0)` of PR #248. Its objective obeys

\[
\boxed{
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-C\log^2(2X).}
\tag{T-23810.2}
\]

Define its signed ordinary-prime residual

\[
r_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p)
\tag{T-23810.3}
\]

and the exact scalar debt

\[
\boxed{
\delta_X
=\sum_{p\le X}(\log p)r_X(p)
=J_{\mathbb P,X}(b_X^{(0)})-P_X.}
\tag{T-23810.4}
\]

Hence

\[
P_X
\ge4\sqrt X-C\log^2(2X)-(\delta_X)_+.
\tag{T-23810.5}
\]

The entire proof is therefore reduced to

\[
(\delta_X)_+=X^{o(1)}.
\tag{T-23810.6}
\]

## 2. Exact elimination of the false geometric burdens

### 2.1 Complete high-rank residual

`L-23820` decomposes the full residual into one logarithmic scalar mode plus a
Green-orthogonal vector. The latter is removed exactly at zero objective cost.
No lower singular value, Schur reserve, packet-rank bound, or source-coordinate
count occurs.

### 2.2 Complete quotient cells

`L-23821` transports the entire signed residual of each logarithmic cell to two
aggregate endpoint charges while preserving total and logarithmic moments and
paying exactly zero objective cost.

The two endpoints are not asserted to be the only arithmetic source
coordinates. They are merely the exact two-moment image of an arbitrarily
high-rank signed source.

Thus the same-sign Möbius hypercube and zero-reserve mutations no longer attack
the algebraic reduction.

## 3. Signed Green quotient-layer hypothesis

Assume `SGQB(K)` from `L-23822` for one fixed order `K>=6`, one fixed reserve
`eta>0`, and constants `A_K,C_K`.

Then the positive scalar debt satisfies

\[
\boxed{
(\delta_X)_+
\le
C_K(\log(2X))^{A_K}
\left[
1+
\max_{2\le Y\le X^{1-\eta}e^{O_K(1)}}
(\delta_Y)_+
\right].}
\tag{T-23810.7}
\]

This recurrence is the only new asymptotic theorem in the proposal.

It is source-specific and must preserve:

```text
the complete signed quotient layers;
the exact logarithmic scalar;
the first fixed-ratio Mertens shell;
all cutoff and transition terms.
```

## 4. Strict scale contraction

Put

\[
D(X)=1+\max_{2\le Y\le X}(\delta_Y)_+
\tag{T-23810.8}
\]

and

\[
\vartheta
=\limsup_{X\to\infty}
\frac{\log D(X)}{\log X}.
\tag{T-23810.9}
\]

Equation (T-23810.7) gives

\[
\vartheta\le(1-\eta)\vartheta.
\tag{T-23810.10}
\]

Since `vartheta>=0`,

\[
\boxed{\vartheta=0.}
\tag{T-23810.11}
\]

Therefore

\[
\boxed{(\delta_X)_+=X^{o(1)}.}
\tag{T-23810.12}
\]

Unlike the withdrawn contact-count route, one fixed order closes the exponent.
No limit `K->infinity` is used.

## 5. Prime-ramp consequence

Equations (T-23810.5) and (T-23810.12) yield

\[
P_X\ge4\sqrt X-X^{o(1)}.
\tag{T-23810.13}
\]

Restoring proper prime powers gives

\[
\boxed{
\mathcal P(X)
:=\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq
\ge4\sqrt X-X^{o(1)}.}
\tag{T-23810.14}
\]

No upper carry cover is required. This is the one-sided orientation needed by
the square-screw consumer.

## 6. Square-screw and zero exclusion

At `X=N^2`, the exact square-screw formula has the form

\[
\Psi(2\log N)
=4(N+N^{-1}-2)-\mathcal P(N^2)+O(\log N).
\tag{T-23810.15}
\]

Equation (T-23810.14) gives

\[
\Psi(2\log N)\le N^{o(1)}.
\tag{T-23810.16}
\]

The upper-envelope square-sampling/Landau transfer on PR #202 then excludes all
poles corresponding to zeros with real part greater than `1/2`. Functional
equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{T-23810.17}
\]

## 7. Why this proposal is materially stronger than the former carry closure

The former proposal required a claim that every same-scale terminal face had
only two free arithmetic contacts. Later review showed that this did not follow
from scalar affine geometry and was vulnerable to high-rank same-sign sources.

The present proposal replaces that statement by two exact theorems and one
strictly scalar barrier:

```text
all Green-orthogonal source rank is removed exactly and for free;
all cell-interior rank is transported exactly and for free;
only the logarithmic boundary debt is routed to strict lower scale.
```

There is:

- no source-rank ceiling;
- no endpoint-coordinate enumeration;
- no positive reflected reserve;
- no nonnegative monotone cover;
- no full Green-energy estimate;
- no arbitrary-vector BTP theorem;
- no `K->infinity` exponent argument.

## 8. Mandatory mutations

A review must verify `SGQB(K)` against:

1. the PR #239 rank-`K` same-sign Möbius cube;
2. a zero reflected-Schur-reserve source;
3. the macroscopic positive/negative constraint dipole of PR #254;
4. the fixed-ratio first Mertens/Farey cell;
5. an omitted quotient-transition row;
6. a live-variable Euler partition;
7. a lower-scale destination exceeding `X^(1-eta)e^(O_K(1))`.

Any failure rejects `SGQB(K)` but does not affect the exact neutralization and
balayage lemmas.

## 9. Exact status

```text
carry/divisor-gradient finite algebra       imported proposed exact
parabolic seed and prime-power reduction    imported proposed complete
Green orthogonal neutralization             proposed exact
signed two-moment cell balayage              proposed exact
SGQB(K)                                      new open RH-bearing hinge
scale contraction after SGQB(K)              complete
prime ramp / square-screw / Landau           complete conditional chain
Riemann Hypothesis                           not claimed proved
```

The proposal is intended for adversarial review as a replacement for the
withdrawn two-contact source-count theorem.
