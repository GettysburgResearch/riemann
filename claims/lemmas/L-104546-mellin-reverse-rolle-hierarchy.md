# L-104546 — Mellin reverse-Rolle hierarchy and complete monotonicity

Claim ID: `L-104546`  
Status: **PROVED EXACT**  
Created: 2026-08-24  
Depends on: `L-104545`  
RH status: **not assumed**

Retain the assumptions and notation of `L-104545`. Put

\[
a_c=|f(c)|.
\]

For every `p>0` for which the sums converge, define the signed critical
amplitude moment

\[
\mathfrak D_f(p)
=
\sum_{c\in G}a_c^p-\sum_{c\in W}a_c^p.
\tag{L-104546.1}
\]

## 1. Layer cake and coarea

The layer-cake identity and `L-104545.1` give

\[
\begin{aligned}
\mathfrak D_f(p)
&=
p\int_0^\infty y^{p-1}(G_y-W_y)\,dy\\
&=
\frac p2\int_0^\infty y^{p-1}N_y\,dy.
\end{aligned}
\tag{L-104546.2}
\]

The one-dimensional coarea formula gives

\[
\int_{\mathbb R}|f(t)|^{p-1}|f'(t)|\,dt
=
\int_0^\infty y^{p-1}N_y\,dy.
\tag{L-104546.3}
\]

Therefore

\[
\boxed{
\mathfrak D_f(p)
=
\frac p2
\int_{\mathbb R}|f|^{p-1}|f'|\,dt
=
\frac p2
\int_0^\infty y^{p-1}N_y\,dy
>0.
}
\tag{L-104546.4}
\]

For `p=1` this is the critical-value total-variation law of `L-104540`. The new
statement supplies the complete positive Mellin hierarchy.

## 2. Complete monotonicity in the Mellin parameter

Let

\[
A=\|f\|_\infty>0
\]

and define

\[
\mathfrak H_f(p)
=
\frac{2\mathfrak D_f(p)}{pA^p}.
\tag{L-104546.5}
\]

Substitute `y=Ae^{-x}` in (L-104546.2). Then

\[
\boxed{
\mathfrak H_f(p)
=
\int_0^\infty
e^{-px}N_{Ae^{-x}}\,dx.
}
\tag{L-104546.6}
\]

Thus `H_f` is the Laplace transform of the nonnegative level-crossing function.
For every integer `r>=0`,

\[
\boxed{
(-1)^r\mathfrak H_f^{(r)}(p)
=
\int_0^\infty
x^re^{-px}N_{Ae^{-x}}\,dx
\ge0.
}
\tag{L-104546.7}
\]

In particular `H_f` is decreasing and log-convex:

\[
\boxed{
\mathfrak H_f(p)\mathfrak H_f(p+2)
\ge
\mathfrak H_f(p+1)^2.
}
\tag{L-104546.8}
\]

More generally, every Hankel matrix

\[
\left[
\mathfrak H_f(p_i+p_j)
\right]_{i,j=1}^m
\]

is positive semidefinite.

## 3. Meaning for Xi

For `f=Xi''`, double-exponential source decay and Stirling decay imply
convergence for every `p>0`.

The parameter `p` has a direct geometric meaning: as `p` decreases it moves
from the largest persistent excursions toward the numerous small high-height
excursions. Hence the small-`p` asymptotics of (L-104546.6) are a
source-visible Abel/Mellin route to the unweighted reverse-Rolle density.

No parent real zero is inserted into (L-104546.4--6). The input is the absolute
variation or, equivalently, the unsigned level-crossing function.
