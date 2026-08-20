# T-100510 — Complex quadratic / activation-free route to closure

Claim ID: `T-100510`
Status: **COMPLETE ROUTE REDUCTION — FINAL VARIATION ESTIMATE RH-EQUIVALENT**
Created: 2026-08-20
Base: PR #676 at `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9`

The route begins from a genuinely unconditional theorem:

\[
Q_z(X)\ge0
\]

on the complex disk of `L-100510`.  The real interval of PR #673 is only its
diameter. `L-100511` strengthens this to every mixed Bernstein carrier of total
degree at least two and derives the activation-free differential chain

\[
G_0\ge0,
\quad
G_0+G_0'\ge0,
\quad
G_0+3G_0'+2G_0''\ge0.
\]

The critical scalar satisfies

\[
G_0'(u)=4e^{-u}L_-(e^u).
\]

Therefore

\[
4\int_1^X(L_-(x))_-\frac{dx}{x}
=
\int_{[0,\log X]}e^u\,d(-G_0)_+(u).
\tag{T-100510.1}
\]

The Mellin transform of \(L_-\) is zero-safe and retains every off-line
reciprocal-zeta pole. Standard Littlewood bounds under RH give the converse.
Hence

\[
\boxed{
\int_{[0,U]}e^u\,d(-G_0)_+(u)=e^{o(U)}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{T-100510.2}
\]

`R-100510` proves that all presently available positivity and ordinary
variation constraints are insufficient for (T-100510.2). The remaining
theorem must use the actual squarefree arithmetic of the downward variation.

This route is distinct from the minimal wavelet route:

```text
route A: signed compact ordinary-Mobius wavelet energy;
route B: positive quadratic carrier and weighted downward variation.
```

```text
complex-disk shifted positivity       PROVED
all mixed Bernstein carriers          PROVED
activation-free differential chain    PROVED
positivity-only closure               REFUTED
AFCD100510                             OPEN / RH-EQUIVALENT
Riemann Hypothesis                     UNPROVED
```
