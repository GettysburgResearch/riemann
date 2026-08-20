# L-100140 — Exact Cauchy–Poisson tail-square and signed-square identities

Claim ID: `L-100140`
Status: **PROVED EXACT ANALYTIC IDENTITY**
Created: 2026-08-20
Frozen parent: PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`
RH status: **not assumed**

Let \((c_n)\) be a finite real sequence and let \(\tau>0\). Define

\[
D_\tau(\gamma)=\sum_{n\ge1}c_n n^{\tau-i\gamma},
\qquad
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)}.
\]

Put

\[
Q_\tau(c)=\int_{\mathbb R}|D_\tau(\gamma)|^2P_\tau(\gamma)\,d\gamma.
\]

The Cauchy characteristic function is

\[
\int_{\mathbb R}e^{-i\gamma v}P_\tau(\gamma)\,d\gamma
=e^{-\tau|v|}.
\tag{L-100140.1}
\]

## 1. Positive Poisson norm

Finite expansion gives

\[
\boxed{
Q_\tau(c)=\sum_{m,n}c_mc_n\min(m,n)^{2\tau}.
}
\tag{L-100140.2}
\]

Define

\[
C_c(u)=\sum_{n\ge u}c_n.
\]

Since

\[
\min(m,n)^{2\tau}=2\tau\int_0^{\min(m,n)}u^{2\tau-1}\,du,
\]

finite Tonelli yields

\[
\boxed{
Q_\tau(c)=2\tau\int_0^\infty|C_c(u)|^2u^{2\tau-1}\,du.
}
\tag{L-100140.3}
\]

As all indices satisfy \(n\ge1\), \(C_c(u)=\sum_nc_n\) on \(0<u\le1\). Hence

\[
\boxed{
Q_\tau(c)=\left|\sum_nc_n\right|^2
+2\tau\int_1^\infty|C_c(u)|^2u^{2\tau-1}\,du.
}
\tag{L-100140.4}
\]

The off-diagonal owner packing is exactly the positive square of every
arithmetic coefficient tail. It is not supplied by the coefficient diagonal.

## 2. Signed Poisson square

Without conjugating the second factor,

\[
\boxed{
\int_{\mathbb R}D_\tau(\gamma)^2P_\tau(\gamma)\,d\gamma
=\left(\sum_nc_n\right)^2.
}
\tag{L-100140.5}
\]

For real coefficients, \(D_\tau(-\gamma)=\overline{D_\tau(\gamma)}\), so the
mixed real/imaginary term is odd. Consequently

\[
\boxed{
Q_\tau(c)-\left(\sum_nc_n\right)^2
=2\int_{\mathbb R}|\Im D_\tau(\gamma)|^2P_\tau(\gamma)\,d\gamma.
}
\tag{L-100140.6}
\]

Equations (L-100140.4) and (L-100140.6) identify the same loss in two exact
coordinates:

```text
multiplicative coordinate: weighted square of every coefficient tail;
phase coordinate:          Cauchy-averaged imaginary phase energy.
```

A positive-norm proof must bound this loss. Replacing the signed square by the
positive norm is not a cancellation theorem.
