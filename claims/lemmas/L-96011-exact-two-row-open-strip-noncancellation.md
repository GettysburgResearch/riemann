# L-96011 — Rows two and three cannot simultaneously cancel any open-strip point

Claim ID: `L-96011`  
Status: **PROVED EXACT TWO-ROW NONCANCELLATION**  
Created: 2026-08-16  
Depends on: `L-96010`  
RH status: **not assumed**

For the two smallest rows, (L-96010.3) simplifies to

\[
P_2(z)=2\,2^{-z}-1-3^{-z},
\tag{L-96011.1}
\]

and

\[
3P_3(z)=5\,3^{-z}-1-2^{-z}-3\,4^{-z}.
\tag{L-96011.2}
\]

Suppose \(P_2(z)=P_3(z)=0\). Put

\[
x=2^{-z},\qquad y=3^{-z}.
\]

Equation (L-96011.1) gives \(y=2x-1\). Substitution into
(L-96011.2) gives

\[
5(2x-1)-1-x-3x^2=0,
\]

hence

\[
(x-1)(x-2)=0.
\tag{L-96011.3}
\]

If \(x=1\), then \(|2^{-z}|=1\), so \(\Re z=0\). If \(x=2\), then
\(|2^{-z}|=2\), so \(\Re z=-1\). Therefore

\[
\boxed{
0<\Re z<1\quad\Longrightarrow\quad
(P_2(z),P_3(z))\ne(0,0).
}
\tag{L-96011.4}
\]

This exact two-row argument replaces the large-\(j\) Euler--Maclaurin
noncancellation imported by PR #542. For every hypothetical nontrivial zero,
one of the fixed rows \(j=2,3\) retains it.
