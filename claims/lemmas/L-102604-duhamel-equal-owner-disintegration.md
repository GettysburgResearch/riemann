# L-102604 — Duhamel gives a canonical equal-owner disintegration

Claim ID: `L-102604`  
Status: **PROVED EXACT OWNER AND OCCUPANCY REDUCTION**  
Created: 2026-08-22  
Depends on: `L-102603`  
RH status: **not assumed**

Consider the squarefree part of the finite Duhamel current

\[
E-C
=
-\int_0^1
\sum_{\ell}
r_\ell Z_\ell A_{t,\ne\ell}E\,dt.
\]

Let \(S\) be a nonempty labelled squarefree monomial of cardinality
\(k=|S|\).  Its coefficient in the native source is

\[
(-1)^k r_S.
\]

Fix one distinguished label \(\ell\in S\).  In the \(\ell\)-th Duhamel
summand, every other selected label contributes

\[
-(1-t)r_hZ_h.
\]

Hence the contribution assigned to \(\ell\) is

\[
\begin{aligned}
-\int_0^1
r_\ell
(-1)^{k-1}(1-t)^{k-1}
r_{S\setminus\{\ell\}}\,dt
&=
\frac{(-1)^k}{k}r_S.
\end{aligned}
\]

Therefore

\[
\boxed{
(-1)^kr_S
=
\sum_{\ell\in S}
\frac{(-1)^k}{|S|}r_S.
}
\tag{L-102604.1}
\]

The completion homotopy has produced the canonical random-order owner:
every selected prime owns exactly \(1/|S|\) of the same native occurrence.

## Same-product physical collapse

Before physical collapse, retain the owner coordinate.  For one integer product
\(n\) with \(k=\omega(n)\) labelled squarefree owners, let \(v_{n,\ell}\) be
its owner components.  Cauchy--Schwarz gives

\[
\left\|
\sum_{\ell\mid n}v_{n,\ell}
\right\|^2
\le
k\sum_{\ell\mid n}\|v_{n,\ell}\|^2.
\]

On the horizon \(n\le16Y\),

\[
k\le\frac{\log(16Y)}{\log2}.
\]

Thus equal-product owner collapse has only logarithmic squared-norm cost.

For the canonical equal-owner allocation in (L-102604.1), all owner
components are identical fractions of the native coefficient, so this bound is
sharp only at logarithmic order and introduces no power loss.

## Exact remaining occupancy

After `L-102604`, the physical occupancy gate no longer includes duplicate
owner representations of one integer.  Its only unresolved part is overlap of
**distinct** integer products after translation by the compact mother kernel:

```text
NC-DEFECT102604:
  subpower near-collision embedding for distinct products in the
  carrier-recombined Duhamel current.
```

This is strictly narrower than the original AR-OCC row.
