# L-104637 — Exact frozen-carrier Bézout transport of the fifth endpoint

Claim ID: `L-104637`  
Status: **PROVED EXACT SOURCE-MODULE IDENTITY**  
Created: 2026-08-27  
Depends on: `L-106620--L-106612` at PR #731 head
`433490c133b26bce4163f4edf7ad04aeda9d33e3`  
RH status: **not assumed**

Fix one mesoscopic window and freeze the Riemann--Siegel frequency at
`omega_j>0`. Put

\[
\mathcal X={i\over\omega_j}(D+q).
\]

For the frozen carrier operator

\[
D+q+i\omega_j=i\omega_j(1-\mathcal X),
\]

so the normalized fifth packet is

\[
(i\omega_j)^{-5}H_{5,j}^{\rm fr}=(1-\mathcal X)^5h.
\]

The two denominator channels and two numerator channels become

\[
\mathbf d=
\begin{pmatrix}
\mathcal Xh\\
(2-\mathcal X)(1-\mathcal X)^5h
\end{pmatrix},
\qquad
\mathbf n=
\begin{pmatrix}
(2-\mathcal X)h\\
\mathcal X(1-\mathcal X)^5h
\end{pmatrix}.
\tag{L-104637.1}
\]

## 1. Exact polynomial Bézout identity

Define

\[
A(X)={-X^5+7X^4-20X^3+30X^2-25X+11\over2}.
\tag{L-104637.2}
\]

Then direct polynomial division gives

\[
\boxed{
XA(X)+{1\over2}(2-X)(1-X)^5=1.
}
\tag{L-104637.3}
\]

Consequently

\[
\boxed{
\mathbf n=\mathcal M(\mathcal X)\mathbf d,
}
\tag{L-104637.4}
\]

where

\[
\boxed{
\mathcal M(X)=
\begin{pmatrix}
(2-X)A(X)&(2-X)/2\\
(1-X)^5&0
\end{pmatrix}.
}
\tag{L-104637.5}
\]

Indeed, the second row is immediate, while the first is (L-104637.3)
multiplied by `(2-X)h`.

Every coefficient of `M` has degree at most six. Thus the seven Krylov grades

\[
1,\mathcal X,\ldots,\mathcal X^6
\]

are sufficient to transport the complete frozen numerator source from the
complete frozen denominator source with zero algebraic residual.

## 2. Exact variable-carrier remainder

Let

\[
\mathscr L=D+q+i\omega(t),
\qquad
\mathscr L_j=D+q+i\omega_j,
\qquad
E_j=i(\omega-\omega_j).
\]

The noncommutative telescoping identity gives

\[
\boxed{
\mathscr L^5-\mathscr L_j^5
=\sum_{r=0}^{4}\mathscr L^{4-r}E_j\mathscr L_j^r.
}
\tag{L-104637.6}
\]

Thus every term in the actual-minus-frozen fifth packet contains at least one
explicit carrier mismatch `omega-omega_j` or one of its derivatives after
expansion. `L-106620` gives on each mesoscopic window

\[
\|1-\omega/\omega_j\|_\infty
\ll(\log T)^{-B-1},
\]

while Stirling gives the derivative bounds. The remainder is therefore a
finite, source-visible order-six differential packet.

## 3. Scope firewall

Equation (L-104637.4) is a source-module identity. By itself it does not imply
containment of the numerator and denominator model spaces, because inner
factorization is nonlinear and differentiation is not a bounded analytic
multiplier. Its valid consequence is that the seven-dimensional transport of
`L-104633` has zero principal algebraic residual in the frozen-carrier model;
the remaining finite-matrix estimate measures physical observation,
inner-factor and carrier-variation effects.
