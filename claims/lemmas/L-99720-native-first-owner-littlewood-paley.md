# L-99720 — Exact native first-owner Littlewood–Paley identity

Claim ID: `L-99720`  
Status: **PROVED EXACT HILBERT-SPACE IDENTITY**  
Created: 2026-08-20  
Depends on: the native first-owner coefficient identity of PR #652  
RH status: **not assumed**

Let `H` be a Hilbert space and let `U_1,...,U_k` be commuting isometries. Put

\[
0<r_i<1,\qquad s_0=1,\qquad s_i=\prod_{h\le i}(1-r_h),
\]

and

\[
F_i=\prod_{h=i}^{k}(I-r_hU_h)f,\qquad F_{k+1}=f.
\]

## One-prime identity

For every isometry `U`, every `0<r<1`, and every `g in H`,

\[
\boxed{
\|(I-rU)g\|^2=(1-r)^2\|g\|^2+r\|(I-U)g\|^2.
}
\tag{L-99720.1}
\]

Both sides equal

\[
(1+r^2)\|g\|^2-2r\Re\langle g,Ug\rangle.
\]

## Telescoping identity

Apply (L-99720.1) to `g=F_{i+1}` and multiply by `s_{i-1}^2`. Since `s_i=s_{i-1}(1-r_i)`,

\[
s_{i-1}^2\|F_i\|^2=s_i^2\|F_{i+1}\|^2+r_is_{i-1}^2\|(I-U_i)F_{i+1}\|^2.
\]

Summing over `i` gives

\[
\boxed{
\left\|\prod_{i=1}^{k}(I-r_iU_i)f\right\|^2
=s_k^2\|f\|^2+
\sum_{i=1}^{k}r_is_{i-1}^2
\left\|(I-U_i)\prod_{h>i}(I-r_hU_h)f\right\|^2.
}
\tag{L-99720.2}
\]

The square-function terms are exactly the future-completed first-owner currents

\[
\Delta_i^{\rm fut}f=(I-U_i)\prod_{h>i}(I-r_hU_h)f.
\]

## Native coefficient identity

With `lambda_i=r_i s_{i-1}`, the commuting-shift algebra satisfies

\[
\boxed{
\prod_{i=1}^{k}(I-r_iU_i)
=s_kI+\sum_{i=1}^{k}\lambda_i(I-U_i)\prod_{h>i}(I-r_hU_h).
}
\tag{L-99720.3}
\]

Every rough subset appears once with coefficient

\[
(-1)^{|A|}\prod_{i\in A}r_i.
\]

Thus (L-99720.2) is an energy identity for the literal native Euler source, not for the rejected contracted alpha-child operator.

## Scope

This theorem controls the labelled Hilbert-space source. It does not assert that the physical scalar observation is contractive; that separate interface is isolated in `R-99720` and `T-99720`.
