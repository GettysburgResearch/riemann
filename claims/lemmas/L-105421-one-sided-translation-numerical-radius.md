# L-105421 — Numerical radius of one-sided translation

On `L^2(0,L)`, let

\[
(S_xf)(t)=\mathbf1_{x<t<L}f(t-x),\qquad x>0.
\]

Decomposition by the residue class of `t` modulo `x` gives a direct integral of
finite unilateral shift chains. The largest chain has length
`q=ceil(L/x)`, hence

\[
\boxed{w(S_x)=\cos\frac\pi{\lceil L/x\rceil+1}.}
\]

For `0<x<=L`,

\[
\boxed{1-w(S_x)\ge 2x^2/(9L^2).}
\]

For `x>=L`, `S_x=0`.
