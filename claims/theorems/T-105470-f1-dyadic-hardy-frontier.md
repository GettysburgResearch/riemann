# T-105470 — Corrected F1 dyadic-cell and one-Hardy-primitive frontier

Claim ID: `T-105470`

Status: **MAJOR UNCONDITIONAL DISCRETIZATION; ONE BOUNDED-CURRENT HARDY GATE OPEN**

Corrected: 2026-08-26

For the exact bounded density \(K_L\), let

\[
H_K(X)=\sum_na_nK_L(X/n).
\]

Every breakpoint is one of \(n,2n,4n,8n\). Hence on every open integer cell

\[
H_K(X)=A_m+B_m\sqrt X.
\tag{T-105470.1}
\]

Define

\[
P(x)=\sum_{n\le x}a_n,\qquad
Q(x)=\sum_{n\le x}\frac{a_n}{\sqrt n},
\]

\[
W(x)=2P(x)-\sqrt xQ(x),
\qquad
\Delta_2=(I-\mathsf S)^2(I-\sqrt2\,\mathsf S).
\]

Then

\[
\boxed{
H_K(m+)=4\Delta_2W(m).
}
\tag{T-105470.2}
\]

The cell logarithmic \(L^1\) mass is uniformly equivalent to its two endpoint
values, and the right/left jump ledger is \(M^{-1/2+o(1)}\).

Define

```text
F1HARDY105470:
  sum_(M<=m<=2M) |Delta_2 W(m)|/m = M^(o(1))
```

on every frozen dyadic source block. Then `F1HARDY105470` is equivalent to
subpower logarithmic \(L^1\) mass of the bounded current \(H_K\), modulo the
closed endpoint ledger. Weighted \(l^1\) duality gives the exact scalar
source form

\[
\sum_{m=M}^{2M}\frac{|\Delta_2W(m)|}{m}
=
\sup_{|\varepsilon_m|\le1}
\left|
\sum_na_n\frac14
\sum_{m=M}^{2M}\frac{\varepsilon_m}{m}K_L(m/n)
\right|.
\tag{T-105470.3}
\]

## Corrected relation to reflection

Historical versions identified \(H_K\) directly with the differential
reflection current. `L-105490--L-105491` replace that equality by a stable
resolvent. Therefore

\[
\boxed{
\mathrm{F1VAR}_{105460}
\Longleftrightarrow
\mathrm{REFSIG}_{106150}
\Longrightarrow
\mathrm{F1HARDY}_{105470}
\Longrightarrow
\mathrm{RH},
}
\tag{T-105470.4}
\]

but the reverse arrow from `F1HARDY105470` to the reflection variation is not
claimed.

The quarter-power normal form on corrected PR #719 gives the alternative sharp
coordinate

\[
\mathrm{QPTI}_{103112}
\Longleftrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
\tag{T-105470.5}
\]

```text
integer-cell affine normal form                    PROVED EXACT
closed logarithmic cell primitive                  PROVED EXACT
two-endpoint equivalence                           PROVED
right sample = one dyadic Hardy primitive          PROVED EXACT
weighted endpoint jump ledger                      PROVED SUBPOWER
bounded-current L1 = discrete F1HARDY              PROVED
reflection variation -> F1HARDY                    PROVED
F1HARDY -> reflection variation                    NOT CLAIMED
F1HARDY105470 / QPTI103112                         OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
