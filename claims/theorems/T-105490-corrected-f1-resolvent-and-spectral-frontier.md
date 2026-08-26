# T-105490 — Corrected bounded-detector resolvent and spectral geometry

Claim ID: `T-105490`

Status: **RETAINED MULTIPLIER CORRECTION; OLD COMPLETED-SOURCE CONCLUSION SUPERSEDED**

Corrected: 2026-08-27

Superseded conclusion disposition: `R-105500`, `T-105500`

## 1. Binding multiplier correction

The bounded derivative-outer density and the historical differential
analytic-square packet are not equal.  Their exact symbols satisfy

\[
\boxed{
(5s+\tfrac32)(1-\sqrt2\,2^{-s})\widehat K_L(s)
=
4P(s)\widehat A(s)^2.
}
\tag{T-105490.1}
\]

Thus, at a fixed source and with its explicitly retained diagonal field,

\[
\boxed{
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)H_K
=
4P(D)J+H_{\rm diag}.
}
\tag{T-105490.2}
\]

The reflection decomposition of \(J\) remains exact.  The old direct
identification of \(P(D)J\) with \(H_K\) is superseded.

## 2. Stable one-way transfer

The missing dyadic factor has the stable anti-causal inverse

\[
(I-\sqrt2\,\tau_{\log2})^{-1}
=
-\sum_{j\ge1}2^{-j/2}\tau_{\log2}^{-j},
\]

and \((5\partial+3/2)^{-1}\) is a positive causal resolvent.  Therefore the
reflection total variation controls the bounded-current logarithmic \(L^1\)
norm at the declared diagonal-ledger scope.  The reverse direction is not
asserted.

## 3. Correct positive spectral square

Historical `L-105483` omitted the resolvent denominator.  Its unregularized
weight is asymptotically constant and gives an infinite integral for every
nonzero finite packet.

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
\tag{T-105490.3}
\]

For the exact normal-ordered analytic source square
\(\mathscr Q_U^\diamond\),

\[
\int e^{-x/2}|H_K^\diamond(e^x)|^2dx
=
\frac1{2\pi}\int
\Omega_K(t)|\mathscr Q_U^\diamond(t)|^2dt.
\tag{T-105490.4}
\]

At that fixed source,

\[
\mathrm{F1KASQ}_{105492}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}
\Longleftrightarrow
\mathrm{F1HCNC}_{105481},
\tag{T-105490.5}
\]

and

\[
\mathrm{F1KFOURTH}_{105493}
\Longrightarrow
\mathrm{F1KASQ}_{105492}.
\tag{T-105490.6}
\]

## 4. Binding source correction

The former equation identifying `QPTI103112` with `BCI102990` and then RH is
withdrawn.  `QPTI103112` is false by corrected PR #719.  `R-105500` separates
that harmonic source from the cutoff-dependent balanced coefficient \(b_U\),
so the semiprime refutation is not silently transferred; nevertheless no old
completed-source RH arrow is retained without a fresh proof.

The independent native ordinary-Möbius conclusion theorem is `T-105500`.

```text
bounded K_L Mellin symbol                         PROVED EXACT
historical K_L = P(D)(A*A)                        REFUTED
exact dyadic/differential bridge                  PROVED EXACT
anti-causal dyadic inverse                        PROVED STABLE
old nondecaying spectral weight                   REFUTED / INFINITE
correct Omega_K positive H^-1 weight              PROVED EXACT
fixed-source spectral/Gram identities             PROVED EXACT
QPTI103112 / EBD103120                            REFUTED
old completed-source RH conclusion                WITHDRAWN

F1KFOURTH/F1KASQ/F1HCNC on balanced b_U           OPEN SOURCE ESTIMATES
NATIVEF1XD105504 / NATIVECELL105504               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
