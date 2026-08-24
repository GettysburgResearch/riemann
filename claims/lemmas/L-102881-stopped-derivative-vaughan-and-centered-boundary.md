# L-102881 — Exact stopped derivative Vaughan decomposition

Claim ID: `L-102881`  
Status: **PROVED EXACT SOURCE DECOMPOSITION; TWO CENTERED ROWS RETAINED**  
Created: 2026-08-24  
Depends on: `L-102869`; `L-102880`  
RH status: **unproved**

Fix the second owner prime `q`, put

\[
\mathbb N_{<q}=\{n:P^+(n)<q\},
\]

and retain the stopped functions `mu^(<q)`, `mu_(U,q)` and `a_(U,q)` of `L-102869`.

For

\[
Y={X\over pq},
\qquad U=\lfloor Y^{1/6}\rfloor,
\]

define the derivative-core scalar

\[
\boxed{
\mathcal C^K_{p,q}(Y)
=\sum_{a\in\mathbb N_{<q}}{\mu(a)\over a}K_L(Y/a^2).
}
\tag{L-102881.1}
\]

Because the finite-Euler Vaughan identity is coefficientwise,

\[
\boxed{
\mathcal C^K_{p,q}
=\mathcal T^K_{p,q}+\mathcal B^K_{p,q}
}
\tag{L-102881.2}
\]

outside the same fixed terminal range as `L-102869`, where

\[
\mathcal T^K_{p,q}(Y)
=-\sum_{d,e\le U}
{\mu^{<q}(d)\mu^{<q}(e)\over de}
\sum_{\substack{m\ge1\\P^+(m)<q}}
{1\over m}K_L\!\left({Y\over d^2e^2m^2}\right),
\tag{L-102881.3}
\]

and

\[
\boxed{
\mathcal B^K_{p,q}(Y)
=\sum_{\substack{r,s>U\\r,s,m\in\mathbb N_{<q}}}
{a_{U,q}(r)a_{U,q}(s)\mu(m)\over rsm}
K_L\!\left({Y\over r^2s^2m^2}\right).
}
\tag{L-102881.4}
\]

The support still gives

\[
r,s>Y^{1/6},
\qquad m\ll Y^{1/6},
\qquad rsm\asymp\sqrt Y.
\]

## 1. Unrestricted Type-I closes absolutely

Split the stopped lattice exactly as in `R-102866`:

\[
\mathcal T^K_{p,q}
=(\mathcal T^K_{p,q})^{\rm full}
+(\mathcal T^K_{p,q})^{\rm bdry}.
\]

By `L-102880`,

\[
\boxed{
(\mathcal T^K_{p,q})^{\rm full}(Y)
=O_K(Y^{-1/6}).
}
\tag{L-102881.5}
\]

No favorable-but-unknown square remains in this derivative coordinate.

## 2. Exact derivative smooth boundary

The retained boundary is

\[
\boxed{
\begin{aligned}
(\mathcal T^K_{p,q})^{\rm bdry}(Y)
={}&\sum_{d,e\le U}
{\mu^{<q}(d)\mu^{<q}(e)\over de}
\sum_{\ell\ge q}{1\over\ell}\\
&\times
\sum_{P^+(k)\le\ell}{1\over k}
K_L\!\left({Y\over d^2e^2\ell^2k^2}\right),
\end{aligned}}
\tag{L-102881.6}
\]

with only support-active `ell`.  It has one new largest prime and is compatible with the exact greatest-owner and decreasing-prime renewal coordinates.  It is not absorbed by (L-102881.5).

## 3. Differential and phase functoriality

Since `K_L=DR_L`,

\[
\boxed{
\mathcal C^K_{p,q}=D\mathcal C_{p,q},
\quad
\mathcal T^K_{p,q}=D\mathcal T_{p,q},
\quad
\mathcal B^K_{p,q}=D\mathcal B_{p,q}
}
\tag{L-102881.7}
\]

as logarithmic distributions.  The stopped identity commutes coefficientwise with every nonzero owner phase, every adaptive phase choice, the Euler/half-divisor/Wick gauges, source regions and the fixed one-octave observation.

## Exact retained rows

```text
KSCB102881:
  subpower logarithmic negative mass of the derivative smooth-boundary current
  in (L-102881.6);

KBCQDSP102881:
  subpower logarithmic negative mass of the coherent stopped balanced current
  in (L-102881.4), after exact owner-phase recombination.
```

Together with (L-102881.5), either an exact source-cover estimate for these two rows or a single joint estimate implies the derivative detector criterion of `L-102880`.

```text
unrestricted derivative Type-I           PROVED POWER-SMALL
stopped derivative source typing          PROVED EXACT
derivative smooth boundary                OPEN / RH-BEARING
stopped balanced Type-II                  OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```
