# R-102702 — Completion monotonicity does not prove the centered envelope

Claim ID: `R-102702`  
Status: **PROVED LOGICAL FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102720--L-102721`  
RH status: **unproved**

`L-102720` proves

\[
Q_\gamma(X)\ge0.
\]

The conclusion-facing scalar is instead

\[
\mathscr E_\gamma(X)
=
Q_\gamma(X)-AX+B\sqrt X,
\]

where

\[
A=16B_\gamma(3/2)>0,
\qquad
B=24B_\gamma(1)>0.
\]

Pointwise positivity of \(Q_\gamma\) does not determine this centered sign.

The elementary countermodel

\[
Q(X)=2X-\sqrt X-1
\qquad(X\ge1)
\]

satisfies \(Q(X)\ge0\), but after subtracting its first two modes,

\[
Q(X)-2X+\sqrt X=-1.
\]

Therefore no argument may infer `CCE102721` solely from positive completion
domination.  The centered envelope is precisely the remaining critical
arithmetic statement.
