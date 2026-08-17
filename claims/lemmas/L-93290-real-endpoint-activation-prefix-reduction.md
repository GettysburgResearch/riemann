# L-93290 — Exact activation-prefix reduction for the two large-prime rows

Claim ID: `L-93290`  
Status: **EXACT UNCONDITIONAL LEMMA**  
Created: 2026-08-18  
Depends on: the coefficient dictionaries of `L-93284`  
RH status: **not assumed**

Let `a(n)` be any real sequence with finite support below every endpoint, and
put

\[
 A_a(N)=\sum_{n\le N}\frac{a(n)}{\sqrt n},
\qquad
 C_a(X)=\sum_{n\le X}\frac{a(n)}{\sqrt n}\log\frac Xn.
\tag{L-93290.1}
\]

## 1. Exact open-cell derivative

For every integer `N>=1` and real `N<X<N+1`, the active set is fixed and

\[
\boxed{
 \frac{d}{d\log X}C_a(X)=A_a(N).
}
\tag{L-93290.2}
\]

At an activation knot the new term has factor `log 1=0`, so `C_a` is
continuous.

## 2. Exact integer recurrence

Integrating (L-93290.2) over one cell gives

\[
\boxed{
 C_a(N+1)-C_a(N)
 =A_a(N)\log\left(1+\frac1N\right).
}
\tag{L-93290.3}
\]

Consequently, prefix nonnegativity is equivalent to monotonicity of the Riesz
row on every activation cell and at every integer knot.

## 3. The actual `LPTRP_23` prefixes

Let

\[
 \mu_{>3}(n)=\mu(n)\mathbf1_{(n,6)=1}
\tag{L-93290.4}
\]

and let `a_2,a_3^sharp` be (R-93290.4)--(R-93290.5). Define

\[
 A_2(N)=\sum_{n\le N}\frac{a_2(n)}{\sqrt n},
\qquad
 A_3^\sharp(N)=\sum_{n\le N}\frac{a_3^\sharp(n)}{\sqrt n}.
\tag{L-93290.5}
\]

The large-prime rows are

\[
 c_X^{>3}(2)=C_{a_2}(X),
\qquad
 c_X^{>3}(3)=\frac13C_{a_3^\sharp}(X).
\tag{L-93290.6}
\]

Both vanish before their first active knot. Hence

\[
\boxed{
 A_2(N)\ge0,\ A_3^\sharp(N)\ge0\ (1\le N\le L)
 \Longrightarrow
 c_X^{>3}(2),c_X^{>3}(3)\ge0
 \quad(1\le X<L+1).
}
\tag{L-93290.7}
\]

This is a stronger finite producer than a row-value scan: it covers all real
endpoints and is exactly the coordinate needed by the prime-adjoining
recurrence.
