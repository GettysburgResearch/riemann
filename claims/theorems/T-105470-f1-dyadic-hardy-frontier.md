# T-105470 — Bounded-detector dyadic-cell and Hardy discretization

Claim ID: `T-105470`

Status: **RETAINED EXACT GENERIC DISCRETIZATION; OLD SOURCE-TO-RH ARROW SUPERSEDED**

Corrected: 2026-08-27

Superseded conclusion disposition: `R-105500`, `T-105500`

For any finite real coefficient sequence \((a_n)\), let

\[
H_K(X)=\sum_na_nK_L(X/n)
\]

for the exact bounded density \(K_L\).  Every breakpoint is one of
\(n,2n,4n,8n\), so on every open integer cell

\[
H_K(X)=A_m+B_m\sqrt X.
\tag{T-105470.1}
\]

Define

\[
P(x)=\sum_{n\le x}a_n,
\qquad
Q(x)=\sum_{n\le x}\frac{a_n}{\sqrt n},
\]

\[
W(x)=2P(x)-\sqrt xQ(x),
\qquad
\Delta_2=(I-\mathsf S)^2(I-\sqrt2\,\mathsf S).
\]

Then

\[
\boxed{H_K(m+)=4\Delta_2W(m).}
\tag{T-105470.2}
\]

The cell logarithmic \(L^1\) mass is uniformly equivalent to its two endpoint
values.  For any source whose atomic coefficient square has the declared
subpower ledger, the right/left jump contribution is subpower.

Define the source-indexed condition

```text
F1HARDY105470[a]:
  sum_(M<=m<=2M) |Delta_2 W_a(m)|/m = M^(o(1)).
```

It is equivalent to subpower logarithmic \(L^1\) mass of the corresponding
bounded current, modulo its endpoint ledger.  Weighted \(l^1\) duality gives

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

## Binding source correction

The generic identities above remain exact.  The previous unqualified arrow

```text
F1HARDY105470 -> RH
```

used the now-withdrawn completed-source `QPTI/BCI/HMO` identification.
`QPTI103112` is false, and no replacement source theorem is supplied by this
bounded-current discretization alone.  The cutoff-dependent balanced source is
not refuted by the QPTI semiprime main, but its conclusion interface is
reopened.

The native ordinary-Möbius repair uses the derivative same-\(K_1\) kernel
\(K_2\), not a silent reassignment of the old coefficient sequence.  Its exact
ratio-sixteen cell gate `NATIVECELL105504` is RH-equivalent by `T-105500`.

```text
integer-cell affine normal form                    PROVED EXACT
closed logarithmic cell primitive                  PROVED EXACT
two-endpoint equivalence                           PROVED
right sample = one dyadic Hardy primitive          PROVED EXACT
weighted dual source form                          PROVED EXACT
old QPTI alternative                               REFUTED
old unqualified F1HARDY -> RH arrow                WITHDRAWN

F1HARDY105470[b_U]                                 OPEN / SOURCE INTERFACE REOPENED
NATIVECELL105504                                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
