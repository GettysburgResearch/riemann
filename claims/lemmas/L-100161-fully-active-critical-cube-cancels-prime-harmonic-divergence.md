# L-100161 — Fully active critical cubes cancel the prime-harmonic divergence exactly

Status: **PROVED EXACT FINITE EULER-PRODUCT IDENTITY**  
Created: 2026-08-20  
RH status: **not assumed**

For the first critical Bernstein kernel

\[
\kappa(t)=\begin{cases}2t-t^2,&0<t\le1,\\1,&t\ge1,\end{cases}
\]

fix a finite labelled rough-prime set `P` and assume every labelled subset product is active at endpoint `x`, equivalently

\[
x\ge\prod_{p\in P}p
\]

(with the second 67 label treated as a distinct copy when present).

For a subset `A`, put `n_A=prod_(p in A)p`. Since `n_A<=x`,

\[
n_A^{-3/2}\kappa(\sqrt{n_A/x})
={2\over\sqrt x}{1\over n_A}-{1\over x}{1\over\sqrt{n_A}}.
\]

Summing with parity sign gives

\[
\boxed{
\sum_{A\subseteq P}(-1)^{|A|}
 n_A^{-3/2}\kappa(\sqrt{n_A/x})
={2\over\sqrt x}\prod_{p\in P}\left(1-{1\over p}\right)
-{1\over x}\prod_{p\in P}\left(1-{1\over\sqrt p}\right).
}
\tag{L-100161.1}
\]

The right side is strictly positive. Indeed

\[
\prod_{p\in P}\left(1-{1\over\sqrt p}\right)
<\prod_{p\in P}\left(1-{1\over p}\right)
\]

and, for `x>=1`,

\[
{2\over\sqrt x}>{1\over x}.
\]

Thus every fully active critical cube is positive **without** paying the divergent bound `sum 1/p`. The prime-harmonic wall in the adjacent-level proof is therefore not an interior Euler-product obstruction. It is entirely an activation-boundary / partial-cube phenomenon.

For a partially active cube, extending the fully-active polynomial formula beyond activation introduces the exact correction

\[
\boxed{
d_x(n)=x^{-3/2}
{(\sqrt{n/x}-1)^2\over(n/x)^{3/2}}
\qquad(n>x),
}
\tag{L-100161.2}
\]

and hence

\[
\text{partial critical cube}
=\text{positive full-product term}
+\sum_{n_A>x}(-1)^{|A|}d_x(n_A).
\]

`R-100160` proves that this signed upper-ideal correction is not always nonnegative. Therefore the exact remaining arithmetic is the cancellation of this activation-boundary upper ideal, not the fully active Euler product.
