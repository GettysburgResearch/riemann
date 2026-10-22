# T-90206 — The minimax critical-neutral Pascal scalar is a one-inequality RH criterion

Claim ID: `T-90206`  
Status: **FULL CONDITIONAL PROPOSAL — ONE EXPLICIT THREE-SOURCE INEQUALITY OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: minimax filter and tail sweep `L-90221`; the standard Landau one-sign theorem used throughout the repository  
Scope: one real scalar criterion; RH is not claimed

## 1. The critical-neutral source

Put

\[
 Q_\star(t)=(1-t)(1-\sqrt2\,t)
\]

and

\[
 b_\star
 =Q_\star(\delta_2)*\mu
 =(\varepsilon-\delta_2)
  *(\varepsilon-\sqrt2\,\delta_2)*\mu.
 \tag{T-90206.1}
\]

For real `X>=1`, define

\[
 \boxed{
 \mathcal K_\star(X)
 =-\sum_{2\le q\le X}b_\star(q)
  \left(q^{-1/2}-X^{-1/2}\right).
 }
 \tag{T-90206.2}
\]

`L-90221` proves that this is the unique minimax uniform-Pascal realization
among all finite dyadic filters having both the neutral root and the
square-root critical root.

It also proves the positive-renewal identity

\[
 \mathcal P\mathcal K_\star=\Psi_\star\ge0
 \tag{T-90206.3}
\]

on the complete causal domain, where `mathcal P` is the positive critical
divisor operator.

## 2. Exact Pascal compression

Let

\[
 U_X(n)=\sum_{k\le X/n}\mu(k)
 \left((nk)^{-1/2}-X^{-1/2}\right)
\]

with the usual zero convention at the unit target, and put

\[
 s_n=n[U_X(n)-U_X(n+1)].
 \tag{T-90206.4}
\]

The complete infinite Pascal reward of `Q_star` has the exact pairing

\[
 \boxed{
 \mathcal K_\star(X)
 =-s_1+\frac{\sqrt2}{2}s_2+\frac{\sqrt2}{3}s_3.
 }
 \tag{T-90206.5}
\]

Consequently the sole proposed inequality is

> **Critical-neutral three-source inequality (`CN3`).**  For every
> sufficiently large endpoint `X`,
> \[
> \boxed{
> 3s_2+2s_3\ge3\sqrt2\,s_1.
> }
> \tag{CN3}

Equivalently,

\[
 \boxed{
 2[U_X(2)-U_X(4)]
 \ge
 \sqrt2[U_X(1)-U_X(2)].
 }
 \tag{T-90206.6}
\]

By (T-90206.5),

\[
 \mathrm{CN3}
 \iff
 \mathcal K_\star(X)\ge0
 \quad(X\gg1).
 \tag{T-90206.7}
\]

No triangular matrix, infinite reward tail, or optimization variable remains.

## 3. Mellin transform

For `q>=1` and `Re s>0`,

\[
 \int_q^\infty
 (q^{-1/2}-X^{-1/2})X^{-s-1}\,dX
 =
 \frac{q^{-s-1/2}}{2s(s+1/2)}.
 \tag{T-90206.8}
\]

The complete source series is

\[
 \sum_{q\ge1}\frac{b_\star(q)}{q^u}
 =
 \frac{Q_\star(2^{-u})}{\zeta(u)}.
 \tag{T-90206.9}
\]

Since `b_star(1)=1`, finite switching gives initially in a right half-plane

\[
 \boxed{
 \widehat{\mathcal K_\star}(s)
 =
 \frac{
  1-Q_\star(2^{-s-1/2})/\zeta(s+1/2)
 }{
  2s(s+1/2)
 }.
 }
 \tag{T-90206.10}
\]

The right side gives the meromorphic continuation needed below.

At the origin,

\[
 Q_\star(2^{-1/2})=0,
\]

so the numerator in (T-90206.10) equals one.  Thus `s=0` is the explicit
critical main pole; it lies on the boundary of the RH-facing half-plane.

## 4. Pole audit

Let `rho` be a hypothetical zeta zero with

\[
 \Re\rho>\frac12.
\]

Then

\[
 s_\rho=\rho-\frac12
\]

lies in `Re s>0`.  The local numerator cannot cancel the reciprocal-zeta pole:
the only roots of `Q_star(t)` are `1` and `1/sqrt(2)`, while

\[
 |2^{-\rho}|<2^{-1/2}.
\]

Hence

\[
 \boxed{
 \widehat{\mathcal K_\star}
 \text{ has a genuine nonreal singularity at }
 s=\rho-\frac12.
 }
 \tag{T-90206.11}
\]

On the positive real axis there is no corresponding singularity:

- zeta has no real zero on `(1/2,1)`;
- its pole at `u=1` makes `1/zeta(u)` vanish;
- zeta is positive and zero-free for `u>1`;
- the explicit factors in (T-90206.10) are regular for `s>0`.

Therefore

\[
 \boxed{
 \widehat{\mathcal K_\star}
 \text{ is holomorphic at every positive real }s.
 }
 \tag{T-90206.12}
\]

## 5. Landau completion

Assume `CN3`, equivalently eventual nonnegativity of `K_star`.  If an
off-line zero existed, (T-90206.11) would force the abscissa of convergence
of the eventually nonnegative Mellin source to be positive.  Landau's
one-sign theorem would then force a singularity at that positive real
abscissa, contradicting (T-90206.12).

Thus

\[
 \boxed{
 \mathrm{CN3}\Longrightarrow\mathrm{RH}.
 }
 \tag{T-90206.13}
\]

Functional-equation symmetry supplies the left half of the critical strip.

The same argument works if `K_star` is eventually nonpositive; the preferred
finite evidence and positive-renewal orientation point to the nonnegative
form.

## 6. Why this is smaller than the neighboring frontiers

```text
full SHARP:
    every average-carry inverse row is nonnegative;

OBH:
    every ordered-balanced hinge occupation is nonnegative;

15:4 low-row criterion:
    one two-row scalar is nonnegative;

CN3:
    one explicit linear inequality among s1,s2,s3.
```

The infinite signed critical reward has already been summed exactly.  The
deterministic renewal forcing is already nonnegative.  The only unproved
statement is the arithmetic boundary inequality `CN3`.

This does not make the theorem soft: the reciprocal-zeta pole audit proves
that `CN3` itself is RH-bearing.

## 7. Proof boundary

Closed exactly:

- source/filter construction;
- global minimax property of the adapter;
- exact Pascal tail sweep;
- reduction to `CN3`;
- complete Mellin transform and zero-safety audit;
- `CN3 -> RH`.

Open:

- `CN3`;
- eventual sign of `K_star`;
- RH.
