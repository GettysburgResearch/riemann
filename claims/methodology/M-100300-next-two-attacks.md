# M-100300 — Exact next attacks for the two endgames

## Route A: activation-deficit compression

Work only with the actual prime-labelled source. For each double-negative cell:

1. compute \(A,B,C\) from the native moments;
2. intersect the roots of \(At^2+Bt+C\) with the activation interval;
3. charge the exact deficit from `L-100300.3`;
4. group cells by the first positive-parity activation product;
5. seek a product-band inequality for the **sum of deficit areas**, not
   pointwise positivity of every cell.

A successful theorem may allow sparse bad cells. Replacing actual prime
products by arbitrary dense shifts is invalid by PR #679's separator.

## Route B: balanced dispersion

Use

\[
a_U(n)=\sum_{\substack{d\mid n\\d>U}}\mu(d)
\qquad(n>1)
\]

inside the exact ranges \(r,s>U\), \(m\le U\), \(rsm\asymp X\).

Promising decompositions are:

```text
large gcd versus coprime r,s;
near diagonal versus separated r/s;
one large prime factor versus genuinely composite a_U;
Mellin frequency zero versus nonzero phase.
```

The continuous prime main term is already killed by the extra half-order
moment. Any estimate must preserve the signs of `a_U(r)a_U(s)mu(m)` through
the compact kernel. A diagonal large sieve or absolute divisor bound is not a
proof.

## Acceptance rule

A closure claim must bound the literal `CATD100300` or `BVD100310` left-hand
side by \(Y^{o(1)}\) without importing a Mertens square-root estimate, an
RH-equivalent local moment theorem, or an unsigned enlargement of the source.
