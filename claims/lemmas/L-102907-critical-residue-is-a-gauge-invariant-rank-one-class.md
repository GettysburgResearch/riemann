# L-102907 — The critical residue is a gauge-invariant rank-one class

Claim ID: `L-102907`  
Status: **PROVED EXACT QUOTIENT/INVARIANT THEOREM**  
Created: 2026-08-25  
Depends on: `L-102905--L-102906`; `L-102900`  
RH status: **not assumed**

For one labelled prime define the critical-residue functional on a two-factor tensor `T` by

\[
\boxed{
\mathfrak c_p(T)
=
\left.
{d\over dx}
\pi_p(T)
\right|_{x=0}.
}
\tag{L-102907.1}
\]

It has the following exact properties.

## 1. Gauge and square ideals are invisible

If `T` belongs to the local convolution kernel, then

\[
\mathfrak c_p(T)=0.
\]

If

\[
\pi_p(T)\in x^2\mathbf C[[x]],
\]

then again

\[
\mathfrak c_p(T)=0.
\]

Thus `c_p` descends to the critical Hodge quotient of `L-102905`.

## 2. The detector-bearing class is nonzero and fixed

For every complementary factorization,

\[
\pi_p(F_t\otimes G_t)=E_pC_p=1-x_p-x_p^2+x_p^3,
\]

so

\[
\boxed{
\mathfrak c_p(F_t\otimes G_t)=-1.
}
\tag{L-102907.2}
\]

The harmonic midpoint tensor has the same residue:

\[
\boxed{
\mathfrak c_p(M_p\otimes M_p)=-1.
}
\tag{L-102907.3}
\]

Therefore the quotient has one normalized critical direction. The arithmetic midpoint is its unique minimum-energy lift; the scalar `-1` is its gauge-invariant charge.

## 3. Global native-current identification

Summing the local residues over the labelled primes and restoring the logarithmic weights gives the first-chaos connection

\[
\boxed{
\Pi_1(z)=
\sum_{\ell}p_\ell^{-z}.
}
\tag{L-102907.4}
\]

After the positive square-lattice inverse of `L-102893`, `L-102900` gives

\[
\omega*\dot\Gamma_{1/2}
=
2\beta*\Pi_1
+
2\beta*\Pi_{\ge2}.
\]

The higher-power term is polylogarithmic. Hence the global Hodge charge is exactly the native prime owner/transfer current exposed by the stopped-source coordinate.

## 4. Three equivalent coordinates

The same nonzero critical class appears as:

```text
PCOI102930:
  physical orientation of the arithmetic midpoint core;

CTZD102897:
  positive drift of the completion-temperature zero;

SGIC102890:
  stopped owner/gcd/phase resolution of the native prime current.
```

They are not three independent gates. They are the physical, scalar-temperature, and arithmetic-owner coordinates of one rank-one critical residue.

No flat-gauge, endpoint-color, or squared-activity theorem can change the value `-1` in (L-102907.2).
