# L-106612 — The carrier-free fifth endpoint is a finite zeta-derivative packet

Claim ID: `L-106612`  
Status: **PROVED EXACT**  
Created: 2026-08-26  
Depends on: `L-106610--L-106611`  
RH status: **not assumed**

Let

\[
\alpha=q+i\omega,
\qquad
h(t)=\zeta\!\left(\frac12+it\right),
\qquad
H_5=(D+\alpha)^5h.
\]

The noncommutative binomial expansion is

\[
\boxed{
\begin{aligned}
H_5={}&D^5h
+5\alpha D^4h
+10(\alpha^2+\alpha')D^3h\\
&+10(\alpha^3+3\alpha\alpha'+\alpha'')D^2h\\
&+5(\alpha^4+6\alpha^2\alpha'
+3(\alpha')^2+4\alpha\alpha''+\alpha''')Dh\\
&+\bigl(
\alpha^5
+10\alpha^3\alpha'
+15\alpha(\alpha')^2
+10\alpha^2\alpha''\\
&\hspace{22mm}
+10\alpha'\alpha''
+5\alpha\alpha'''
+\alpha''''
\bigr)h .
\end{aligned}
}
\tag{L-106612.1}
\]

Since

\[
D^jh=i^j\zeta^{(j)}(s),
\]

\(H_5\) is an explicit linear combination of

\[
\zeta,\zeta',\ldots,\zeta^{(5)}.
\]

The packets \(C_5\) and \(R_5\) use one additional derivative and are explicit
linear combinations through \(\zeta^{(6)}\). Their coefficients are finite
differential polynomials in \(q,\omega\), and Stirling gives on a dyadic
window

\[
\omega\asymp\log T,
\qquad
q=O(1),
\qquad
\omega^{(j)},q^{(j)}=O_j(T^{-j})
\quad(j\ge1),
\]

with the sharper constant expansions in `L-106610`.

For \(\Re s>1\),

\[
\zeta^{(j)}(s)
=
\sum_{n\ge1}
\frac{(-\log n)^j}{n^s}.
\]

Therefore the four packets in (L-106611.1) have literal, finite
logarithmic-polynomial Dirichlet coefficients on every right safe line.
After the standard approximate-functional-equation transfer they are
classical mollifier/mean-value objects. No inverse Xi companion, root
interpolation, or denominator-multiplied Hankel source is introduced.

The theorem is an exact source typing statement. It does not supply the
required sixth-derivative mean value or the inner phase-angle bound.
