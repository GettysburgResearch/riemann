# L-100702 — The completed core and first-transition packet carry equal critical power modes which cancel only in balance

Claim ID: `L-100702`  
Status: **PROVED EXACT LOCAL CANCELLATION + ASYMPTOTIC PHYSICAL AUDIT**  
Created: 2026-08-20  
Depends on: `L-100701`; PR #674 minimal ratio-eight kernel  
RH status: **not assumed**

Let `K_0` be the compact ratio-eight ordinary-Möbius wavelet kernel of PR #674.
Its Mellin transform is

\[
\widehat K_0(s)=
\frac{(s+\frac32)(1-\sqrt2\,2^{-s})(1-2^{-s})^2}
{s^2(s-\frac12)}.
\]

The removable value at the critical real carrier is

\[
\boxed{
 c_0:=\widehat K_0(1/2)
 =2(2-\sqrt2)^2\log2>0.
}
\tag{L-100702.1}
\]

## 1. One-prime carrier ledger

At physical Mellin coordinate `s=1/2`, put `x_p=1/p`. The three local factors
from `L-100701` become

\[
E_p=1-x_p,
\qquad
Q_p=1-x_p^2,
\qquad
R_p=x_p-x_p^2.
\]

Thus

\[
\boxed{E_p=Q_p-R_p}
\tag{L-100702.2}
\]

at the critical carrier itself.

For a finite ordered prime set, (L-100701.2) specializes exactly to

\[
\boxed{
\prod_p(1-p^{-1})
=
\prod_p(1-p^{-2})
-
\sum_t
\left[\prod_{h<t}(1-p_h^{-2})\right]
(p_t^{-1}-p_t^{-2})
\left[\prod_{h>t}(1-p_h^{-1})\right].
}
\tag{L-100702.3}
\]

As the finite set exhausts the primes,

\[
\prod_p(1-p^{-1})\longrightarrow0,
\qquad
\prod_p(1-p^{-2})\longrightarrow\zeta(2)^{-1}.
\]

Hence the transition sum tends to the same value `zeta(2)^(-1)`. The positive
completed carrier is not a harmless reserve; it is cancelled at leading order
by the first-transition packet.

## 2. Physical one-owner carrier

The prime number theorem and the compact support of `K_0` give

\[
\boxed{
\sum_p{1\over\sqrt p}K_0(X/p)
=
{c_0\sqrt X\over\log X}
+O\!\left({\sqrt X\over\log^2X}
\right).
}
\tag{L-100702.4}
\]

Indeed, partial summation replaces the prime sum by

\[
\int_{X/8}^{X}t^{-1/2}K_0(X/t){dt\over\log t},
\]

and the substitution `y=X/t` gives the main constant

\[
\int_1^8K_0(y)y^{-3/2}dy=\widehat K_0(1/2)=c_0.
\]

Thus the diagonal/single-owner region is power-sized on its own.

## 3. Fully squared cofactor carrier

The largest-prime plus squared-cofactor core contains the model packet

\[
\mathcal P_{\rm sq}(X)
=
\sum_{a\ge1}{\mu(a)\over a}
\sum_{p>P^+(a)}{1\over\sqrt p}
K_0\!\left({X\over pa^2}\right).
\tag{L-100702.5}
\]

Uniform prime partial summation for `a<=(log X)^3`, followed by the crude
absolute tail bound

\[
\sum_{a>(\log X)^3}{1\over a}
\sum_p{1\over\sqrt p}
\left|K_0\!\left({X\over pa^2}\right)\right|
\ll {\sqrt X\over(\log X)^3},
\]

gives

\[
\boxed{
\mathcal P_{\rm sq}(X)
=
{c_0\over\zeta(2)}{\sqrt X\over\log X}
+o\!\left({\sqrt X\over\log X}ight).
}
\tag{L-100702.6}
\]

The owner condition `p>P^+(a)` is automatic in the main polylogarithmic range
and only reduces the tail.

Equation (L-100702.6) is the physical counterpart of the completed carrier
`prod_p(1-p^-2)` in (L-100702.3).

## 4. Consequence

Any regional proof which estimates

```text
completed squared core;
first-transition packet;
diagonal owner region;
```

independently by nonnegative majorants pays a term of order
`sqrt(X)/log X`. Such a proof cannot yield the subpower logarithmic negative
mass required by the compact-wavelet detector.

The carrier cancellation must occur **before** one-sided inequalities are
applied. The correct state is the balanced completed-minus-transition homotopy
of `L-100701`, with common interval and owner labels retained.

This theorem repairs the regional assignment in PR #691: finite squaring is a
useful internal coordinate, but the completed and transition regions are not
separate conclusion-facing estimates.