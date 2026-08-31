# L-107112 — Shallow primitive rays and terminal common cores are polylogarithmic

**Claim ID:** `L-107112`  
**Status:** proved unconditional absolute-range closure  
**Date:** 2026-08-31  
**Depends on:** `L-107110--L-107111`  
**RH:** not assumed

Retain `q=67` and

\[
\Lambda_q(v)=\left(1-{|v|\over\log q}\right)_+.
\]

For `Y>=2`, the q-free stationary annular square is

\[
\mathcal Q_q(Y)
 =\sum_{\substack{m,n\le Y\\q\nmid mn}}
 {\mu(m)\mu(n)\over\sqrt{mn}}
 \Lambda_q\!\left(\log{m\over n}\right).
\]

On squarefree support write uniquely

\[
m=da,\qquad n=db,\qquad (a,b)=1.
\]

Then `d,a,b` are pairwise coprime and q-free and

\[
\boxed{
\mathcal Q_q(Y)
 =\sum_{\substack{d\le Y\\d\ {m sf},\ q\nmid d}}{1\over d}
 \sum_{\substack{a,b\le Y/d\\
 (a,b)=1,\ (ab,dq)=1}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \Lambda_q\!\left(\log{a\over b}\right).
}
\tag{L-107112.1}
\]

This is an exact common-core interference identity. The sign of the common
core cancels because `mu(da)mu(db)=mu(a)mu(b)`.

Fix `R>=2`. The total absolute contribution of the terms with

\[
\min(a,b)\le R
\]

is

\[
\boxed{
O_q\bigl(R(1+\log Y)\bigr).
}
\tag{L-107112.2}
\]

## Proof of the shallow bound

The kernel support forces

\[
q^{-1}\le a/b\le q.
\]

By symmetry, take `a<=R`. For fixed `a`,

\[
\sum_{a/q\le b\le qa}{1\over\sqrt{ab}}
\le C_q.
\]

For each surviving pair,

\[
\sum_{d\le Y/\max(a,b)}{1\over d}
\le1+\log Y.
\]

Coprimality, squarefreeness and q-freeness only decrease the absolute sum.
Summing over `a<=R` and doubling proves (L-107112.2).

Every term with

\[
d>{Y\over R}
\]

is already in this shallow range, because `da,db<=Y` then imply
`a,b<R`. Hence the terminal common-core tail costs no additional theorem.

Taking

\[
R=(\log(eY))^A
\]

for any fixed `A>0`, the complete shallow/terminal contribution is `Y^{o(1)}`.
The remaining signed scalar has the simultaneous geometry

\[
\boxed{
\begin{gathered}
d\le Y/R,\qquad a,b>R,\\
(a,b)=1,\quad(ab,dq)=1,\quad q^{-1}\le a/b\le q.
\end{gathered}}
\tag{L-107112.3}
\]

It is a genuinely balanced high-primitive pair problem. Since `(a,b)=1`, its
diagonal is absent: `a=b` would force `a=b=1`, already removed by the shallow
bound.

## Consequence

Let `\mathcal H_R(Y)` denote the restriction of (L-107112.1) to
(L-107112.3). Then

\[
\boxed{
\mathcal Q_q(Y)=\mathcal H_R(Y)
 +O_q(R(1+\log Y)).
}
\tag{L-107112.4}
\]

For polylogarithmic `R`, subpower control of the stationary annular detector
is therefore equivalent to subpower control of one assembled signed
high-primitive interference scalar.

## Scope

No cancellation is claimed in the remaining high-primitive region. The lemma
proves that low primitive rays, the full diagonal and terminal common cores
are not part of the final arithmetic obstruction.