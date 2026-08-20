# L-99800 — Continuous Jordan completion and its unavoidable real carrier

Let

\[
\beta_R=(\varepsilon-\delta_R)*\mu,
\qquad
J_u=\mu*\operatorname{id}^{u},
\qquad
J_u(n)=n^u\prod_{p\mid n}(1-p^{-u})\ge0,
\]

and

\[
K_{R,u}=\beta_R*\operatorname{id}^{u}
       =(\varepsilon-\delta_R)*J_u.
\]

Write \(n=R^am\), \((m,R)=1\). Then

\[
K_{R,u}(n)=
\begin{cases}
J_u(m),&a=0,\\
(R^u-2)J_u(m),&a=1,\\
R^{(a-2)u}(R^u-1)^2J_u(m),&a\ge2.
\end{cases}
\]

Hence

\[
\boxed{K_{R,u}(n)\ge0\ \forall n\iff R^u\ge2.}
\]

For \(R=67\), the sharp threshold is

\[
u_{67}=\frac{\log2}{\log67}.
\]

At this threshold the local factor is

\[
\frac{(1-x)^2}{1-2x}
=1+0x+\sum_{a\ge2}2^{a-2}x^a.
\]

But

\[
\sum_n\frac{K_{R,u}(n)}{n^z}
=\frac{1-R^{-z}}{\zeta(z)}\zeta(z-u)
\]

has a genuine real pole at \(z=1+u_{67}\), or physical
\(s=\tfrac12+u_{67}\). That real carrier lies to the right of every translated
open-strip zero \(s=\rho-\tfrac12\). Thus the infinite-order completion crosses
the fixed-grade sign barrier but cannot by itself close Landau.
