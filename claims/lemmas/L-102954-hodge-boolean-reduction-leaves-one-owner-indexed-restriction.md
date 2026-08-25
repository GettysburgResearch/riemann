# L-102954 — Hodge–Boolean reduction leaves one owner-indexed restriction

Claim ID: `L-102954`  
Status: **PROVED EXACT REDUCTION; FINAL RESTRICTION OPEN**  
Created: 2026-08-25  
Depends on: `L-102951--L-102953`; PR #751 `L-106080--L-106081`  
RH status: **unproved**

Let `H_harm` be the fixed derivative/common-mother observation of the unique
harmonic midpoint class from `T-102950`.

By `L-102951`, modulo a polylogarithmic squared-activity field, `H_harm` is the
observation of the native squarefree Euler parity source. Apply the exact
Boolean Vaughan identity with a dyadically frozen cutoff `U=Y^(1/6)`.

## 1. Type-I row

`L-102953` proves that the complete squarefree Type-I row is an `l1`-bounded
square-shift transform of the parent zero-moment Type-I row and satisfies a
power-saving bound. It may therefore be removed before the conclusion-facing
negative part.

## 2. Balanced row

The remaining source is

\[
b_U=a_U\star a_U\star\mu_{\rm sf}.
\]

`L-102952` proves that `b_U` is one universal core coefficient, independent of
the selected owner pair on every allowed core.

Choose the horizon-safe minimum-owner pair of `L-106081`. Every nonzero
balanced core contains two distinct primes and satisfies

\[
\lambda^2\le a.
\]

After the linear block projection

\[
B\le a<2B,
\qquad L\le\lambda<2L,
\]

one has

\[
L^2<2B.
\]

## 3. The exact remaining map

Let `H_lab(B,L)` be the owner-labelled Hilbert packet containing:

```text
the universal Boolean core coefficient b_U(a)/a;
the distinguished owner lambda;
the co-owner and marked-67 data;
carrier, shell, factorization and renewal labels;
the nonzero owner phases.
```

Let

\[
J_{B,L}:H_{\rm lab}(B,L)\to H_{\rm phys}(B,L)
\]

be the literal distinct-product physical collapse after the frozen shared-owner
and owner/core renewals.

All algebraic, Type-I, diagonal, equal-product, same-owner, repeated-label,
terminal and squared-activity terms are already closed. Therefore

\[
\boxed{
H_{\rm harm}
=
\sum_{B,L}J_{B,L}\mathcal B_{B,L}
+H_{\rm closed},
}
\tag{L-102954.1}

with

\[
\int_1^Y|H_{\rm closed}(X)|\frac{dX}{X}=Y^{o(1)}.
\]

There are only `O(log^2 Y)` nonempty `(B,L)` blocks.

Thus the full arithmetic problem is equivalent to the single operator family

```text
OICP102960:
  ||J_(B,L) B_(B,L)||, or its conclusion-facing negative part, is X^o(1)
  uniformly for every minimum-owner block L^2<2B.
```

## Consequence

\[
\boxed{
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

This theorem proves that PR #751 targets the correct unique Hodge class and
that its Type-I and range reductions are genuine. It does not supply the
owner-indexed physical restriction required in the last display.
