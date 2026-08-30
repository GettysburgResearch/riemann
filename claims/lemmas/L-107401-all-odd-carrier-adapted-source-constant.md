# L-107401 — Every fixed odd Xi endpoint has carrier-adapted source constant \(1/(2K)\)

Claim ID: `L-107401`  
Programme aliases: `XI90.ALL_ODD_SOURCE_CONSTANT`, `XI.CARRIER_ADAPTED_LIMIT`  
Status: **PROVED FROM EXACT FOURIER ALGEBRA AND THE ACTUAL-XI CONCENTRATION THEOREM**  
Created: 2026-08-30  
Depends on: `L-106500`, `L-106710`; PR #765 actual-Xi Laplace concentration  
Programme issue: #744  
RH status: **not assumed**

Let \(K\ge1\) be fixed and odd. Retain the positive densities

\[
L_K(\xi)
=
\frac12\int
(v-u)(v^K-u^K)\Phi(u)\Phi(v)\,du
\]

and the antiphase density \(a_{K,\lambda}\) of `L-106710`.

Put

\[
s=\frac\xi2,\qquad
d=v-u,\qquad
x=\frac d\xi,
\qquad
\lambda_\xi=\frac2\xi.
\]

Let \(\mu_{K,\xi}\) be the conditional probability measure of `L-106502`,
whose density is proportional to

\[
d(v^K-u^K)\Phi(u)\Phi(v).
\]

A direct division of the two exact Fourier integrands gives

\[
\boxed{
\frac{a_{K,\lambda_\xi}(\xi)}
     {\lambda_\xi L_K(\xi)}
=
\int g_K\!\left(\frac d\xi\right)
\,d\mu_{K,\xi}(d),
}
\tag{L-107401.1}
\]

where

\[
\boxed{
g_K(x)
=
\frac{x\bigl((1+x)^K+(1-x)^K\bigr)}
     {2\bigl((1+x)^K-(1-x)^K\bigr)}
}
\tag{L-107401.2}
\]

with the removable value

\[
\boxed{g_K(0)=\frac1{2K}.}
\tag{L-107401.3}
\]

The function \(g_K\) is even and analytic near zero, so

\[
g_K(x)=\frac1{2K}+O_K(x^2).
\tag{L-107401.4}
\]

PR #765 proves for the actual Xi kernel that, for every fixed \(q\),

\[
\int |d|^{2q}\,d\mu_{K,\xi}(d)=O_{K,q}(e^{-q\xi}).
\]

Splitting at \(|d|=\xi/2\), using (L-107401.4) on the central part and a
high moment on the tail, yields

\[
\boxed{
\frac{a_{K,2/\xi}(\xi)}
     {(2/\xi)L_K(\xi)}
=
\frac1{2K}
+
O_K\!\left(\frac{e^{-\xi}}{\xi^2}\right).
}
\tag{L-107401.5}
\]

For \(K=31\),

\[
\boxed{
\frac{a_{31,2/\xi}(\xi)}
     {(2/\xi)L_{31}(\xi)}
=
\frac1{62}
+
O\!\left(\frac{e^{-\xi}}{\xi^2}\right).
}
\tag{L-107401.6}
\]

This generalizes the fifth-order constant \(1/10\) without changing the
physical source.

## Scope

The multiplier \(2/\xi\) is Fourier-adapted. A physical companion uses one
constant scale on each mesoscopic real window. `L-107403` identifies exact
matching at the frozen carrier, but spread, phase transport and the
topological index remain open.
