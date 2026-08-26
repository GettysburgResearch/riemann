# T-105490 — Corrected F1 bounded-detector, resolvent and spectral frontier

Claim ID: `T-105490`

Status: **BINDING MULTIPLIER CORRECTION AND NEW POSITIVE SPECTRAL NORMAL FORM; RH UNPROVED**

Created: 2026-08-26

Base: durable draft PR #730

Frozen inputs:

```text
PR #730  f534df7ad3a180c35a95b57cd7a91b6233702408
PR #719  426fe1c34a35d21b38a393456a7071c0902170f1
PR #751  98af0db6ec7f77d6333a77a3dac53c4698852f43
```

## 1. Binding correction

The bounded derivative-outer density and the historical differential
analytic-square packet are not equal. Their exact symbols satisfy

\[
\boxed{
(5s+\tfrac32)(1-\sqrt2\,2^{-s})\widehat K_L(s)
=
4P(s)\widehat A(s)^2.
}
\tag{T-105490.1}
\]

Thus, sourcewise,

\[
\boxed{
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)H_K
=
4P(D)J.
}
\tag{T-105490.2}
\]

The reflection decomposition of \(J\) remains exact. The old identification
of \(P(D)J\) with the bounded current \(H_K\) is superseded.

## 2. Reflection remains a sufficient route

The missing factor has the stable anti-causal inverse

\[
(I-\sqrt2\,\tau_{\log2})^{-1}
=
-\sum_{j\ge1}2^{-j/2}\tau_{\log2}^{-j},
\]

and \((5\partial+3/2)^{-1}\) is a positive causal resolvent. Therefore

\[
\|H_K\|_{L^1}
\le
\frac{8}{3(\sqrt2-1)}
\|P(D)J\|_{\rm TV}
\tag{T-105490.3}
\]

modulo the inherited closed field.

Consequently

\[
\boxed{
\mathrm{F1VAR}_{105460}
\Longleftrightarrow
\mathrm{REFSIG}_{106150}
\Longleftrightarrow
\mathrm{SFSC}_{106150}
\Longrightarrow
\mathrm{F1HARDY}_{105470}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105490.4}
\]

The reverse implication from the bounded Hardy current to the differential
reflection variation is not claimed.

## 3. Correct positive spectral square

Historical `L-105483` omitted the resolvent denominator. Its weight is
asymptotically constant, so its unregularized integral is infinite for every
nonzero finite source packet.

The corrected bounded-detector weight is

\[
\boxed{
\Omega_K(t)
=
\frac{
16|P(\tfrac14+it)|^2r_A(t)^4
}{
((\tfrac{11}{4})^2+25t^2)
(1+\sqrt2-2\,2^{1/4}\cos(t\log2))
}
\asymp\frac1{1+t^2}.
}
\tag{T-105490.5}
\]

For the exact normal-ordered analytic source square
\(\mathscr Q_U^\diamond\),

\[
\int e^{-x/2}|H_K^\diamond(e^x)|^2dx
=
\frac1{2\pi}\int
\Omega_K(t)|\mathscr Q_U^\diamond(t)|^2dt.
\tag{T-105490.6}
\]

This gives the exact packet equivalence

\[
\boxed{
\mathrm{F1KASQ}_{105492}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longleftrightarrow
\mathrm{F1HCNC}_{105481}.
}
\tag{T-105490.7}
\]

The corrected Beta fourth-moment premise satisfies

\[
\boxed{
\mathrm{F1KFOURTH}_{105493}
\Longrightarrow
\mathrm{F1KASQ}_{105492}.
}
\tag{T-105490.8}
\]

Every premise in (T-105490.7)--(T-105490.8) remains open.

## 4. Sharp and square frontiers

The strongest unaffected direct route is

\[
\boxed{
\mathrm{F1HCNC}_{105481}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longrightarrow
\mathrm{F1HARDY}_{105470}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105490.9}
\]

The corrected PR #719 quarter-power route is

\[
\boxed{
\mathrm{QPTI}_{103112}
\Longleftrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105490.10}
\]

`QPTI103112` is a one-sided coherent owner-collapse theorem.
`F1HCNC105481` is a stronger positive square/near-collision theorem.
No equivalence between them is asserted.

## Exact status

```text
bounded K_L Mellin symbol                         PROVED EXACT
historical K_L = P(D)(A*A)                        REFUTED
exact dyadic/differential bridge                  PROVED EXACT
anti-causal dyadic inverse                        PROVED STABLE
reflection variation -> bounded Hardy current     PROVED
reverse Hardy -> reflection variation             NOT CLAIMED
old Omega_A analytic-square L2                    INFINITE / WITHDRAWN
correct Omega_K positive weight                   PROVED EXACT
Omega_K asymptotic (1+t^2)^(-1)                   PROVED
correct bounded spectral Plancherel                PROVED EXACT
correct Beta fourth moment -> F1 Gram              PROVED EXACT

F1KFOURTH105493 / F1KASQ105492                     OPEN / RH-BEARING
F1HCNC105481 / F1GRAM105480                        OPEN / RH-BEARING
F1HARDY105470                                      OPEN / RH-BEARING
QPTI103112 / BCI102990                             OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
