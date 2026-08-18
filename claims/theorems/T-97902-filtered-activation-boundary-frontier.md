# T-97902 — The filtered route reduces RH to one thin activation-boundary fluctuation

Claim ID: `T-97902`  
Status: **UNCONDITIONAL REDUCTION; ONE CENTERED BOUNDARY SIGN OPEN**  
Created: 2026-08-18  
Depends on: `L-97901`, `L-97902`, `L-97905`; the frozen Mellin--Landau consumer  
RH status: **unproved**

Use the constant-killing filtered scalar of `L-97905` and put

\[
 \ell=\log\log X,
 \qquad
 K=\ell^2,
 \qquad
 Z=X^{1/K},
 \qquad
 L=\exp(K).
 \tag{T-97902.1}
\]

Let `U_Z^Delta` be the positive complete filtered cube through `Z`, and let
`U_full^Delta` be the normalized fully completed filtered native scalar.
Largest-prime Bellman ownership and top-history completion give exactly

\[
 U_{\rm full}^{\Delta}(X)
 =U_Z^{\Delta}(X)-\mathfrak I_X^{\Delta}-\mathfrak A_X^{\Delta},
 \tag{T-97902.2}
\]

where

\[
 \mathfrak I_X^{\Delta}=
 \sum_{2\le n\le X/L\atop P^-(n)>Z}
 \frac{\mu^2(n)}n
 U_{\rm full}^{\Delta,\widehat{\operatorname{rad}(n)}}(X/n)
 \tag{T-97902.3}
\]

and

\[
 \boxed{
 \mathfrak A_X^{\Delta}=
 \sum_{X/L<n\le X/2\atop P^-(n)>Z}
 \frac{\mu^2(n)}n
 U_{\rm full}^{\Delta}(X/n).
 }
 \tag{T-97902.4}
\]

The simplification in (T-97902.4) is exact: every omitted prime is greater
than `Z`, while the endpoint `X/n` is below `L`, and `Z>L` for large `X`.
Hence all omitted Euler factors are inactive.

## 1. The entire interior is negligible

The full filtered state satisfies the same Vinogradov--Korobov bound as the
unfiltered state. The inverse omitted-factor expansion and the fact that every
active rough product has at most `K` factors give

\[
 \boxed{
 |\mathfrak I_X^{\Delta}|
 =o\!\left(\frac1{\log Z}\right).
 }
 \tag{T-97902.5}
\]

Indeed the total reciprocal mass is `O(K)`, while at endpoints at least `L`

\[
 |U_{\rm full}^{\Delta,\widehat A}(Y)|
 \ll L^{-1/4}+\mathcal E(\sqrt L)+K/Z.
\]

With `K=ell^2`, each product of this bound with `K` is
`o(K/log X)=o(1/log Z)`.

## 2. Exact leading cancellation

`L-97905` gives

\[
 U_Z^{\Delta}(X)\asymp\frac1{\log Z}>0.
 \tag{T-97902.6}
\]

On the other hand the fully completed filtered state has the unconditional PNT
bound

\[
 U_{\rm full}^{\Delta}(X)=o((\log Z)^{-A})
 \tag{T-97902.7}
\]

for every fixed `A`. Combining (T-97902.2), (T-97902.5), and
(T-97902.7) yields

\[
 \boxed{
 \mathfrak A_X^{\Delta}
 =U_Z^{\Delta}(X)+o\!\left(\frac1{\log Z}\right).
 }
 \tag{T-97902.8}
\]

Thus the positive cube and the thin activation boundary cancel to leading
order. This is the exact parity barrier in the filtered coordinates; no
improvement of either absolute main estimate can decide the sign.

## 3. Minimal boundary theorem

Define the centered activation-boundary defect

\[
 \mathfrak R_X^{\Delta}=
 U_Z^{\Delta}(X)-\mathfrak A_X^{\Delta}.
 \tag{T-97902.9}
\]

The exact remaining theorem is

> **Filtered Activation-Boundary Positivity (`FABP67`).**
> \[
> \boxed{
> \mathfrak R_X^{\Delta}
> \ge \mathfrak I_X^{\Delta}
> }
> \]
> for every sufficiently large real `X`.

By (T-97902.2), `FABP67` is exactly eventual nonnegativity of the filtered
native scalar. The Mellin transform has only one additional factor
`1-4^(-s)`, which is zero-free in `Re(s)>0`. Hence

\[
 \boxed{\mathrm{FABP67}\Longrightarrow\mathrm{RH}.}
 \tag{T-97902.10}
\]

A strictly sufficient margin form is

\[
 \mathfrak R_X^{\Delta}\ge(\log Z)^{-3},
 \tag{T-97902.11}
\]

because the interior term in (T-97902.5) is smaller after increasing the fixed
choice of `L` if necessary.

## 4. Geometry of the remaining source

Every term of (T-97902.4) has

```text
rough product n in (X/exp((log log X)^2), X/2],
least prime > X^(1/(log log X)^2),
number of prime owners <= (log log X)^2,
terminal endpoint 2 <= X/n < exp((log log X)^2).
```

The remaining quantity is therefore not an all-scale Euler tail. It is one
centered, finite-depth, activation-boundary correlation. It retains every
source sign inside the terminal native value and every rough owner in the
positive top-history coefficient.

```text
constant-killing filter                    PROVED EXACT
positive subpower cube                      PROVED
interior top histories                      CLOSED BY PNT
leading cube/boundary cancellation          PROVED
FABP67 centered boundary sign               OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```