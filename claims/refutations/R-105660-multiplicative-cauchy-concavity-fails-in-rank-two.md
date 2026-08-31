# R-105660 — Multiplicative Cauchy concavity fails in rank two

**Claim ID:** `R-105660`  
**Status:** proved exact rational counterexample  
**Date:** 2026-08-31

For

\[
G_s(i,j)=(\overline\lambda_i+\lambda_j+s)^{-1},
\quad \lambda_1=1,\quad\lambda_2=1+i,\quad H=2,
\]

the proposed residual

\[
E=G_{2H}G_H^{-1}G_{2H}-G_{4H}
\]

is

\[
\begin{pmatrix}
77/3330&(27886-7879i)/1244421\\
(27886+7879i)/1244421&77/3330
\end{pmatrix},
\]

with

\[
\boxed{\det E=-8471/1119978900<0.}
\]

Thus universal `MLC105656` is false. The conclusion-facing inequalities
survive on the same packet:

\[
\mathcal O_H=13210/12321,\qquad \mathcal T_H=13/17,
\]

\[
\boxed{\mathcal O_H-\mathcal T_H=64397/209457>0,}
\]

and the `FNI105658` gap equals `9389/58378>0`. Only the overstrong Loewner
route is refuted.
