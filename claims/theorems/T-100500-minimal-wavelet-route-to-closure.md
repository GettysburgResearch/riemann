# T-100500 — Minimal ordinary-Möbius wavelet route to closure

Claim ID: `T-100500`
Status: **COMPLETE ROUTE REDUCTION — FINAL ARITHMETIC ESTIMATE RH-EQUIVALENT**
Created: 2026-08-20
Base: PR #675 at `7b28224ba1b072d4ccd5b93ad37c0a64e7939740`

The route is

\[
M(x)
\longrightarrow
G_\mu(X)
\longrightarrow
\text{compact Hardy energy}
\longrightarrow
\text{Mellin pole exclusion}.
\]

Every interface is exact:

1. `L-100500` gives the compact Abel–Mertens formula.
2. PR #674 gives the unique minimal ratio-eight kernel and positive
   factor-67 desmoothing.
3. PR #675 gives the exact \(L^2\) spectral abscissa.
4. `L-100501` proves that a source-blind inverse necessarily pays
   \(\sqrt X\).

The final conclusion-producing theorem may be written in any of the equivalent
forms

\[
G_\mu(X)=X^{o(1)},
\]

\[
\int_1^Y Q_X\,\frac{dX}{X^3}=Y^{o(1)},
\]

or

\[
M(X)=X^{1/2+o(1)}.
\]

Each is equivalent to RH. The wavelet route is nevertheless attractive because
it is:

```text
ordinary-Mobius;
fixed support ratio eight;
three explicit activation bands;
free of factor-67 source ownership;
free of Hall, Volterra, score, and capacity interfaces.
```

The first unsupported statement is the actual ordinary-Möbius compact
cross-core cancellation. It is not proved here.

```text
minimal wavelet and multiplier       PROVED
compact Mertens frame                PROVED
quantitative exponent dictionary     PROVED
source-blind inverse shortcut        REFUTED
MWOC100500                            OPEN / RH-EQUIVALENT
Riemann Hypothesis                   UNPROVED
```
