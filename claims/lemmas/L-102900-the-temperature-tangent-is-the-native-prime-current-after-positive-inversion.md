# L-102900 — Positive inversion maps the midpoint temperature tangent to the native prime current

Claim ID: `L-102900`  
Status: **PROVED EXACT GENERATOR/OWNER IDENTIFICATION**  
Created: 2026-08-24  
Depends on: `L-102893`; `L-102898`; `L-102600--L-102604`  
RH status: **not assumed**

Let

\[
\Gamma_t=\sigma_t*\sigma_t
\]

and retain the positive square-lattice inverse

\[
\omega*\Gamma_{1/2}=\beta
\]

from `L-102893`.

Put

\[
\Lambda(z)
=
\sum_{\ell}\log(1+p_\ell^{-z}).
\]

Then

\[
\partial_t\Gamma_t=2\Gamma_t*\Lambda,
\]

and therefore

\[
\boxed{
\omega*(\partial_t\Gamma_t)|_{t=1/2}
=
2\beta*\Lambda.
}
\tag{L-102900.1}
\]

This is an exact coefficient identity on every finite horizon.

## 1. Critical prime current and higher-power gauge

Split

\[
\Lambda=\Pi_1+\Pi_{\ge2},
\]

where

\[
\boxed{
\Pi_1(z)=\sum_\ell p_\ell^{-z}
}
\tag{L-102900.2}
\]

and

\[
\boxed{
\Pi_{\ge2}(z)
=
\sum_\ell\sum_{k\ge2}
\frac{(-1)^{k+1}}{k}p_\ell^{-kz}.
}
\tag{L-102900.3}
\]

The first term is the native half-order prime current.  After the exact
greatest-owner disintegration it is the same critical owner/transfer current
isolated in `L-102600`.

The higher-power operator has only polylogarithmic half-order mass:

\[
\boxed{
\sum_{\substack{p_\ell^k\le Y\\k\ge2}}
\frac1{k\,p_\ell^{k/2}}
\ll
\log\log(3Y).
}
\tag{L-102900.4}
\]

Thus it introduces no new critical source type; it is a polylogarithmically
bounded prime-power gauge acting on the same native field.

Consequently,

\[
\boxed{
\omega*\dot\Gamma_{1/2}
=
2\beta*\Pi_1
+
2\beta*\Pi_{\ge2},
}
\tag{L-102900.5}
\]

with one critical first-chaos term and one already-typed higher-power gauge.

## 2. Source-level secant at the transition zero

Let \(\vartheta(X)\) be the unique temperature zero of `L-102896`.  Define the
finite-horizon secant source

\[
\mathfrak D_X
=
\int_0^1
\dot\Gamma_{\,1/2+s(\vartheta(X)-1/2)}\,ds.
\tag{L-102900.6}
\]

Then

\[
\boxed{
\Gamma_{\vartheta(X)}-\Gamma_{1/2}
=
\left(\vartheta(X)-\frac12\right)\mathfrak D_X.
}
\tag{L-102900.7}
\]

Applying the fixed outer observation and using

\[
\mathscr S_{\vartheta(X)}(X)=0
\]

gives the exact source-normalized drift formula

\[
\boxed{
\mathscr S_{1/2}(X)
=
-\left(\vartheta(X)-\frac12\right)
\mathcal O_{R_L}[\mathfrak D_X](X).
}
\tag{L-102900.8}
\]

Inside the transition layer,

\[
\mathcal O_{R_L}[\mathfrak D_X](X)
\asymp
\frac{\sqrt X}{(\log X)^2}>0.
\]

At \(\vartheta(X)=1/2\), the source is interpreted as
\(\mathfrak D_X=\dot\Gamma_{1/2}\).

## 3. Unification of the two live frontiers

Equation (L-102900.5) identifies the source which normalizes the
critical-temperature drift with the same native prime current whose
source/owner/gcd/phase geometry is exposed by `SGIC102890`.

Thus the two live coordinates are not independent:

```text
CTZD102897:
  sign and displacement of the unique temperature zero;

SGIC102890:
  source-faithful physical dispersion of the native prime current.
```

They are respectively the scalar drift and arithmetic owner coordinates of
one completion-temperature connection.

The theorem does not prove either criterion.  In particular, the
polylogarithmic operator bound for \(\Pi_{\ge2}\) is not an independent
one-sided sign estimate for the hard native field.
