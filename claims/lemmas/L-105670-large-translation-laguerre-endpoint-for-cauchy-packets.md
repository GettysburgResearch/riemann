# L-105670 — Every finite Cauchy packet satisfies CTI at large translation

**Claim ID:** `L-105670`  
**Status:** proved all-rank asymptotic theorem  
**Date:** 2026-08-31  
**Depends on:** `T-105655`, `L-105661`  
**RH:** not assumed

Let

\[
K=\operatorname{span}\{e^{-\lambda_jx}:1\le j\le n\}
 \subset L^2(0,\infty),
\qquad \Re\lambda_j>0,
\]

after repeated nodes have been replaced by the usual confluent derivative
coordinates. Let `P` be the orthogonal projection onto `K`, and let

\[
T_H=M_{e^{-Hx}},
\qquad
Q_H=P_{T_H^2K}.
\]

The Cauchy trace quantities are

\[
\mathcal T_H=\operatorname{tr}(PT_HP)
 =\operatorname{tr}(G_0^{-1}G_H),
\]

\[
\mathcal O_H=\operatorname{tr}(PQ_H)
 =\operatorname{tr}
 (G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H}).
\]

Let `K_P(x,y)` be the integral kernel of `P` and put

\[
\boxed{
\kappa_K=K_P(0,0)
 =\mathbf1^*G_0^{-1}\mathbf1>0.
}
\tag{L-105670.1}
\]

For confluent coordinates, the last expression is interpreted as the squared
norm of evaluation at zero on `K`.

Then, as `H->infinity`,

\[
\boxed{
\mathcal T_H={\kappa_K\over H}+O_K(H^{-2}),
}
\tag{L-105670.2}
\]

and

\[
\boxed{
\mathcal O_H={n\kappa_K\over H}+O_K(H^{-2}).
}
\tag{L-105670.3}
\]

Consequently

\[
\boxed{
\mathcal O_H-\mathcal T_H
 ={(n-1)\kappa_K\over H}+O_K(H^{-2}).
}
\tag{L-105670.4}
\]

For every packet of rank `n>=2`, CTI is therefore strict for all sufficiently
large `H`. Rank one is already strict for every `H>0`, with the exact formula

\[
\mathcal O_H-\mathcal T_H
 ={H\delta^2\over(H+\delta)^2(H+2\delta)}>0,
\qquad \delta=\Re\lambda.
\tag{L-105670.5}
\]

## Proof of the current asymptotic

Since

\[
\mathcal T_H
 =\int_0^\infty e^{-Hx}K_P(x,x)\,dx,
\]

set `y=Hx`. The finite-rank kernel is analytic near `(0,0)`, so

\[
K_P(y/H,y/H)=\kappa_K+O_K(y/H).
\]

Exponential domination gives (L-105670.2).

## The deep packet has a universal Laguerre limit

Let `U_H` be the unitary dilation

\[
(U_Hf)(y)=H^{-1/2}f(y/H).
\]

The dilated deep space is

\[
U_H(T_H^2K)
 =\operatorname{span}
 \{e^{-2y}e^{-\lambda_jy/H}:1\le j\le n\}.
\]

A (generalized, in the confluent case) Vandermonde change of basis shows that
these subspaces converge in the finite-dimensional Grassmannian to

\[
\boxed{
\mathcal L_n
 =e^{-2y}\operatorname{span}\{1,y,\ldots,y^{n-1}\}.
}
\tag{L-105670.6}
\]

An orthonormal basis of `mathcal L_n` is

\[
q_m(y)=2e^{-2y}L_m(4y),
\qquad 0\le m<n,
\]

where `L_m` is the ordinary Laguerre polynomial. The exact identities

\[
\int_0^\infty q_m(y)q_r(y)\,dy=\delta_{mr},
\]

\[
\boxed{
\int_0^\infty q_m(y)\,dy=(-1)^m
}
\tag{L-105670.7}
\]

imply

\[
\iint P_{\mathcal L_n}(v,u)\,du\,dv
 =\sum_{m=0}^{n-1}
 \left|\int q_m\right|^2
 =n.
\tag{L-105670.8}
\]

Writing the overlap trace in scaled kernel coordinates gives

\[
\mathcal O_H
 ={1\over H}
 \iint K_P(u/H,v/H)
 \widetilde Q_H(v,u)\,du\,dv,
\]

where `widetilde Q_H` is the projection kernel of the dilated deep space.
Projection convergence, (L-105670.8), and the local expansion of `K_P` prove
(L-105670.3).

## Scope

The threshold after which CTI is strict depends on the packet. The theorem
proves the large-translation endpoint, not the arbitrary intermediate-height
trace inequality or the cofinal Xi passage.