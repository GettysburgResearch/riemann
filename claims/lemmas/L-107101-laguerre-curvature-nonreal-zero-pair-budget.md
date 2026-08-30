# L-107101 — Laguerre curvature is sourced only by nonreal zero pairs

Claim ID: `L-107101`  
Status: **PROVED EXACT ZERO-PAIR DECOMPOSITION AND NEGATIVE-MASS BUDGET**  
Created: 2026-08-30  
Depends on: `L-107100`  
RH status: **not assumed**

Let `f` be a real entire function of genus at most one, with the usual conjugation symmetry. Away from its real zeros define

\[
Q_f(x)
={f'(x)^2-f(x)f''(x)\over f(x)^2}
=-\left({f'\over f}\right)'(x).
\tag{L-107101.1}
\]

The genus-one logarithmic derivative gives, locally normally away from zeros,

\[
\boxed{
Q_f(x)=\sum_\rho {1\over(x-\rho)^2},
}
\tag{L-107101.2}
\]

with zeros counted with multiplicity. The affine exponential factor in the canonical product disappears after the second logarithmic derivative.

## 1. Real zeros are purely positive curvature

A real zero `rho=r` contributes

\[
{1\over(x-r)^2}>0.
\]

Hence negative Laguerre curvature can only be produced by nonreal conjugate pairs.

For one pair

\[
\rho=a+ib,
\qquad
\bar\rho=a-ib,
\qquad b>0,
\]

the combined contribution is

\[
\boxed{
q_{a,b}(x)
=
{2((x-a)^2-b^2)\over((x-a)^2+b^2)^2}.
}
\tag{L-107101.3}
\]

It is negative exactly on `|x-a|<b`.

## 2. Exact pair budget

The complete negative mass of one conjugate pair is

\[
\begin{aligned}
\int_\mathbb R (q_{a,b})_-(x)\,dx
&=
\int_{a-b}^{a+b}
{2(b^2-(x-a)^2)\over((x-a)^2+b^2)^2}\,dx\\
&={2\over b}
\int_{-1}^{1}{1-u^2\over(1+u^2)^2}\,du\\
&=\boxed{{2\over b}}.
\end{aligned}
\tag{L-107101.4}
\]

Since the negative part of a sum is bounded by the sum of the negative parts,

\[
\boxed{
\int_\mathbb R (Q_f)_-(x)\,dx
\le
2\sum_{\substack{\rho:\Im\rho>0}}
{m(\rho)\over\Im\rho},
}
\tag{L-107101.5}
\]

whenever the right side is finite; otherwise the statement holds for every finite canonical-product truncation and yields the corresponding local inequality. On compact real intervals, locally normal truncation gives the same bound with the full right side, possibly infinite.

## 3. Relation to reverse Rolle

At a simple nonshared critical point `c`,

\[
Q_f(c)
={\mathcal L_f(c)\over f(c)^2}.
\]

Thus the simple extra extrema charged by `L-107100` are precisely the zeros of `f'` lying in the negative-curvature set

\[
\{x:Q_f(x)<0\}.
\]

This identifies the exact complex source of the real reverse–Rolle defect.

## 4. A quantitative depth lemma

Let `C_eta` be a finite set of simple extra extrema such that

\[
Q_f(c)\le-\eta<0
\qquad(c\in C_\eta).
\]

Assume the intervals

\[
I_c=
\left[c-{\eta\over2L},c+{\eta\over2L}\right]
\]

are pairwise disjoint and `|Q_f'|<=L` on their union. Then `Q_f<=-eta/2` on every `I_c`, and hence

\[
\boxed{
\#C_\eta
\le
{2L\over\eta^2}
\int_\mathbb R(Q_f)_-(x)\,dx.
}
\tag{L-107101.6}
\]

Combining with (L-107101.5) turns zero-pair height, curvature depth and curvature variation into an explicit defect-counting route.

## Scope

The zero-pair budget alone does not prove a useful Xi descent: shallow or highly clustered negative wells can contain many derivative zeros unless Xi-specific depth/separation information is supplied. The theorem identifies the missing quantitative input rather than assuming it.