# T-105470 — F1 dyadic-cell localization and one-Hardy-primitive frontier

Claim ID: `T-105470`

Status: **MAJOR UNCONDITIONAL DISCRETIZATION; ONE SOURCE-SPECIFIC HARDY GATE OPEN**

This theorem continues `T-105460` on durable PR #730 and composes the latest
frozen source coordinates from PRs #719 and #751.

## 1. Frozen source and physical current

The canonical equal-pair Boolean source is first formed in the prime-box
configuration algebra, then physically realized.  Repeated-label contractions
are retained in the inherited closed ledger.  For the resulting ordinary
physical coefficients \(a_n=\sigma_U(n)/\sqrt n\), the live derivative-outer
current is

\[
H_K(X)=\sum_na_nK_L(X/n).
\tag{T-105470.1}
\]

`L-106134.14` identifies this with

\[
\frac12D(D-1)(5D+3/2)(2D-1)\mathcal J_U
\]

modulo the closed contraction field.  By the reflection identity of
`T-105460`,

\[
H_K=-2D_{\rm out}\mathcal O_U+H_{\rm closed}.
\tag{T-105470.2}
\]

Hence the total-variation gate `F1VAR105460` is equivalent to subpower
logarithmic `L1` mass of \(H_K\).

## 2. Exact removal of continuous kernel geometry

`L-105470` proves that on every integer cell

\[
H_K(X)=A_m+B_m\sqrt X.
\]

The cell's exact logarithmic absolute integral is given by one elementary
primitive and is uniformly equivalent to the two endpoint values.

Define

\[
\begin{aligned}
P(x)&=\sum_{n\le x}a_n,\\
Q(x)&=\sum_{n\le x}{a_n\over\sqrt n},\\
W(x)&=2P(x)-\sqrt xQ(x),\\
\Delta_2&=(I-S)^2(I-\sqrt2S),
\qquad (Sf)(x)=f(x/2).
\end{aligned}
\tag{T-105470.3}
\]

Then `L-105471` gives the exact right sample

\[
\boxed{H_K(m+)=4\Delta_2W(m).}
\tag{T-105470.4}
\]

The right/left discrepancy is a four-term arithmetic jump filter.  The frozen
source-diagonal and equal-product energy proves its weighted contribution is
\(M^{-1/2+o(1)}\) by `L-105472`.

## 3. The one-sequence frontier

Define

```text
F1HARDY105470:
  for every frozen dyadic source block,

  sum_{M<=m<=2M} |Delta_2 W(m)|/m = M^(o(1)).
```

Then

\[
\boxed{
\mathrm{F1HARDY}_{105470}
\Longleftrightarrow
\mathrm{F1VAR}_{105460}
\Longleftrightarrow
\mathrm{REFSIG}_{106150}
\Longleftrightarrow
\mathrm{SFSC}_{106150}.
}
\tag{T-105470.5}
\]

Together with the frozen implication chain,

\[
\boxed{
\mathrm{F1HARDY}_{105470}
\Longrightarrow
\mathrm{WKSFSC}_{106150}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105470.6}
\]

All displayed equivalences use the same frozen source and dyadic-boundary
convention.  The closed fields may be added or removed in either direction by
the triangle inequality because their logarithmic `L1` norms are subpower.

## 4. Exact dual form

Weighted `l1` duality gives an equivalent scalar source test:

\[
\boxed{
\sum_{m=M}^{2M}{|\Delta_2W(m)|\over m}
=
\sup_{|\varepsilon_m|\le1}
\left|
\sum_n a_n\,\mathcal K_{M,\varepsilon}(n)
\right|,
}
\tag{T-105470.7}
\]

where

\[
\mathcal K_{M,\varepsilon}(n)
={1\over4}
\sum_{m=M}^{2M}{\varepsilon_m\over m}K_L(m/n).
\tag{T-105470.8}
\]

The factor `1/4` follows from (T-105470.4).  Thus the final theorem can be
viewed either as one Hardy-variation estimate or as a uniform family of
one-dimensional signed source correlations.  No pair-owner tensor remains.

## 5. Binding firewalls

`R-105470` proves that one sample per cell, including the midpoint, cannot
control the cell mass.  `R-105460` proves that the positive half-kernel is not
`TP_3`.  Therefore the open gate cannot be bypassed by either sparse
quadrature or source-blind higher total positivity.

## Exact boundary

```text
integer-cell affine normal form                    PROVED EXACT
cell logarithmic L1 primitive                      PROVED EXACT
two-endpoint equivalence                           PROVED UNIFORMLY
right sample = one dyadic Hardy primitive          PROVED EXACT
endpoint jump = finite dyadic coefficient filter   PROVED EXACT
weighted jump ledger                               PROVED / SUBPOWER
continuous F1VAR = discrete F1HARDY                PROVED MODULO CLOSED LEDGER
l1-dual scalar source form                         PROVED EXACT
one-interior-sample shortcut                       REFUTED EXACTLY
TP3 shortcut                                       REFUTED EXACTLY

F1HARDY105470                                      OPEN / RH-BEARING
F1VAR105460 / REFSIG106150                         OPEN / RH-BEARING
BCI102990                                          OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```

The surviving F1 task is now a single weighted dyadic Hardy variation of one
explicit cumulative coefficient sequence.  Every finite F1 owner, Hodge,
homotopy, reflection, diagonal, continuous-cell, and endpoint bookkeeping
layer has been discharged before this gate.
